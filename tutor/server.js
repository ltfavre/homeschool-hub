// The Tutor server. Runs on this computer and serves each child's chat page (opened from the Home Assistant tablet)
// and the parent's history page, over the home network.
//
//   node tutor/server.js            (or: npm start, in the tutor folder)
//
// Settings, access links, the API key, knowledge files, and chat history live in the private data folder
// (default C:\Users\<you>\VenvLearningTutor, or TUTOR_DATA_DIR), never in this repository.
import http from 'node:http';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import Anthropic from '@anthropic-ai/sdk';
import {loadKnowledge, toolsFor} from './knowledge.js';
import {Conversations, tutorTurn} from './tutor.js';

export const DATA_DIR = process.env.TUTOR_DATA_DIR || path.join(os.homedir(), 'VenvLearningTutor');
const HERE = path.dirname(fileURLToPath(import.meta.url));

function readConfig() {
  const f = path.join(DATA_DIR, 'config.json');
  if (!fs.existsSync(f)) { console.error(`No settings found at ${f}. Run "npm run setup" in the tutor folder first.`); process.exit(1); }
  return JSON.parse(fs.readFileSync(f, 'utf8'));
}

export function lanAddress() {
  for (const list of Object.values(os.networkInterfaces()))
    for (const a of list || []) if (a.family === 'IPv4' && !a.internal && !a.address.startsWith('169.254.')) return a.address;
  return 'localhost';
}

const same = (a, b) => typeof a === 'string' && typeof b === 'string' && a.length === b.length && crypto.timingSafeEqual(Buffer.from(a), Buffer.from(b));

function send(res, status, body, type = 'application/json; charset=utf-8') {
  res.writeHead(status, {'content-type': type, 'cache-control': 'no-store', 'x-content-type-options': 'nosniff', 'referrer-policy': 'no-referrer'});
  res.end(typeof body === 'string' || Buffer.isBuffer(body) ? body : JSON.stringify(body));
}

async function readBody(req, limit = 20000) {
  let size = 0; const chunks = [];
  for await (const c of req) { size += c.length; if (size > limit) throw new Error('too large'); chunks.push(c); }
  return JSON.parse(Buffer.concat(chunks).toString('utf8') || '{}');
}

function friendlyError(err) {
  if (err instanceof Anthropic.AuthenticationError || err instanceof Anthropic.PermissionDeniedError) return 'The tutor isn\'t set up correctly yet (the API key isn\'t working). Please ask your parent.';
  if (err instanceof Anthropic.RateLimitError) return 'The tutor is busy right now. Wait a minute and try again.';
  if (err instanceof Anthropic.InternalServerError || err instanceof Anthropic.APIConnectionError) return 'The tutor can\'t connect right now. Check the internet and try again in a minute.';
  if (err instanceof Anthropic.APIError) return 'Something went wrong with the tutor. Please try again, or ask your parent.';
  return 'Something went wrong. Please try again.';
}

export function start() {
  const cfg = readConfig();
  const apiKey = process.env.ANTHROPIC_API_KEY || cfg.anthropic_api_key;
  if (!apiKey) { console.error('No Anthropic API key. Run "npm run setup" again or set ANTHROPIC_API_KEY.'); process.exit(1); }
  const client = new Anthropic({apiKey});
  const K = loadKnowledge(DATA_DIR);
  const convs = new Conversations(DATA_DIR);
  const busy = new Set();
  const page = name => fs.readFileSync(path.join(HERE, 'public', name));
  const childBy = token => cfg.children.find(c => same(c.token, token));

  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url, 'http://x');
    try {
      // Child chat page: /k/<child token>; the page sends the token back on every API call.
      if (req.method === 'GET' && url.pathname.startsWith('/k/')) return childBy(url.pathname.slice(3)) ? send(res, 200, page('chat.html'), 'text/html; charset=utf-8') : send(res, 404, 'Not found', 'text/plain');
      if (req.method === 'GET' && url.pathname.startsWith('/p/')) return same(url.pathname.slice(3), cfg.parent_token) ? send(res, 200, page('parent.html'), 'text/html; charset=utf-8') : send(res, 404, 'Not found', 'text/plain');
      if (req.method === 'GET' && url.pathname === '/health') return send(res, 200, {ok: true});

      if (url.pathname.startsWith('/api/parent/')) {
        if (!same(req.headers['x-tutor-key'], cfg.parent_token)) return send(res, 403, {error: 'forbidden'});
        if (url.pathname === '/api/parent/conversations') return send(res, 200, {children: cfg.children.map(c => ({id: c.id, name: c.name, grade: c.grade, conversations: convs.list(c.id)}))});
        const m = /^\/api\/parent\/conversations\/([a-z0-9-]+)\/([0-9a-f-]{36})$/.exec(url.pathname);
        if (m) { const c = convs.load(m[1], m[2]); return c ? send(res, 200, {...c, api: undefined}) : send(res, 404, {error: 'not found'}); }
        return send(res, 404, {error: 'not found'});
      }

      const child = childBy(req.headers['x-tutor-key']);
      if (url.pathname.startsWith('/api/') && !child) return send(res, 403, {error: 'forbidden'});
      if (req.method === 'GET' && url.pathname === '/api/me') return send(res, 200, {name: child.name, grade: child.grade});
      if (req.method === 'GET' && url.pathname.startsWith('/api/conversation/')) {
        const c = convs.load(child.id, url.pathname.split('/').pop());
        return c ? send(res, 200, {id: c.id, transcript: c.transcript}) : send(res, 404, {error: 'not found'});
      }
      if (req.method === 'POST' && url.pathname === '/api/chat') {
        const body = await readBody(req);
        const message = String(body.message || '').trim().slice(0, 4000);
        if (!message) return send(res, 400, {error: 'empty message'});
        let conv = body.conversation_id ? convs.load(child.id, body.conversation_id) : null;
        if (!conv) conv = convs.create(child);
        if (busy.has(conv.id)) return send(res, 409, {error: 'still answering'});
        busy.add(conv.id);
        res.writeHead(200, {'content-type': 'text/event-stream; charset=utf-8', 'cache-control': 'no-store', 'x-accel-buffering': 'no'});
        const emit = e => res.write(`data: ${JSON.stringify(e)}\n\n`);
        emit({type: 'start', conversation_id: conv.id});
        try {
          await tutorTurn({client, child, tools: toolsFor(K, child), conv, message, emit});
        } catch (err) {
          console.error(new Date().toISOString(), child.id, err);
          const text = friendlyError(err);
          conv.transcript.push({role: 'error', text: `${text} (${err?.constructor?.name || 'Error'}: ${err?.message || err})`, at: new Date().toISOString()});
          emit({type: 'error', text});
        } finally {
          convs.save(conv); busy.delete(conv.id);
          emit({type: 'done'}); res.end();
        }
        return;
      }
      send(res, 404, {error: 'not found'});
    } catch (err) {
      console.error(err);
      if (!res.headersSent) send(res, 500, {error: 'server error'}); else res.end();
    }
  });
  const port = cfg.port || 8790;
  server.listen(port, '0.0.0.0', () => {
    const base = `http://${lanAddress()}:${port}`;
    console.log(`VenvLearning Tutor is running.`);
    for (const c of cfg.children) console.log(`  ${c.name} (Grade ${c.grade}): ${base}/k/${c.token}`);
    console.log(`  Parent history: ${base}/p/${cfg.parent_token}`);
    console.log(`Data folder: ${DATA_DIR}`);
  });
  return server;
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(HERE, 'server.js')) start();
