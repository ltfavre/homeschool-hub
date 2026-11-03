// First-time setup (run it yourself in a terminal; it asks for the children's names and your Anthropic API key):
//
//   npm run setup        (in the tutor folder)
//
// Writes the private settings file to the data folder, builds the curriculum knowledge files, and prints each child's
// link plus a Home Assistant script that adds a Tutor card to each child's tab. Re-run it any time; existing links stay.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import readline from 'node:readline';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {DATA_DIR, lanAddress} from './server.js';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const cfgFile = path.join(DATA_DIR, 'config.json');
const old = fs.existsSync(cfgFile) ? JSON.parse(fs.readFileSync(cfgFile, 'utf8')) : {};
const token = () => crypto.randomBytes(18).toString('base64url');

const rl = readline.createInterface({input: process.stdin, output: process.stdout});
const ask = (q, def = '') => new Promise(r => rl.question(def ? `${q} [${def}]: ` : `${q}: `, a => r(a.trim() || def)));
function askHidden(q) {   // reads the API key without echoing it
  return new Promise(resolve => {
    process.stdout.write(q); let s = '';
    const onData = chunk => {
      for (const ch of String(chunk)) {   // a paste arrives as one chunk
        if (ch === '\r' || ch === '\n' || ch === '\u0004') { process.stdin.setRawMode(false); process.stdin.off('data', onData); process.stdout.write('\n'); resolve(s.trim()); return; }
        if (ch === '\u0003') process.exit(1);
        if (ch === '\u007f' || ch === '\b') s = s.slice(0, -1); else s += ch;
      }
    };
    process.stdin.setRawMode(true); process.stdin.resume(); process.stdin.on('data', onData);
  });
}

console.log(`VenvLearning Tutor setup. Private data folder: ${DATA_DIR}\n`);
const children = [];
for (const grade of [4, 7]) {
  const prev = (old.children || []).find(c => c.grade === grade);
  const name = await ask(`First name of your Grade ${grade} student`, prev?.name || `Grade ${grade} student`);
  children.push({id: `grade${grade}`, grade, name, token: prev?.token || token()});
}
const port = Number(await ask('Port for the tutor', String(old.port || 8790)));
rl.close();   // close readline first: while it is open it echoes every keystroke, including the key
let key = await askHidden(old.anthropic_api_key ? 'Anthropic API key (press Enter to keep the saved one): ' : 'Anthropic API key (from console.anthropic.com → API keys): ');
if (!key) key = old.anthropic_api_key || '';
process.stdin.pause();
if (!key && !process.env.ANTHROPIC_API_KEY) console.log('No API key saved. Set ANTHROPIC_API_KEY or run setup again before starting the tutor.');

fs.mkdirSync(DATA_DIR, {recursive: true});
const cfg = {port, children, parent_token: old.parent_token || token(), ...(key ? {anthropic_api_key: key} : {})};
fs.writeFileSync(cfgFile, JSON.stringify(cfg, null, 2));
// Settings hold the API key: limit the file to the current Windows user.
if (process.platform === 'win32') { try { execFileSync('icacls', [cfgFile, '/inheritance:r', '/grant:r', `${process.env.USERNAME}:F`], {stdio: 'ignore'}); } catch {} }

console.log('\nBuilding the curriculum knowledge files (about a minute)…');
execFileSync(process.platform === 'win32' ? 'python' : 'python3', [path.join(HERE, 'export_knowledge.py'), path.join(DATA_DIR, 'knowledge')], {stdio: 'inherit', env: {...process.env, PYTHONUTF8: '1'}});

const base = `http://${lanAddress()}:${port}`;
const links = Object.fromEntries(children.map(c => [c.name.split(' ')[0].toLowerCase(), `${base}/k/${c.token}`]));
const ha = `// Paste into the Home Assistant browser console (signed in as an admin, on the School dashboard).
// Adds a "Tutor" card at the top of each child's tab. Safe to run again.
(async () => {
const links = ${JSON.stringify(links, null, 1)};
const hass = document.querySelector('home-assistant').hass, ws = m => hass.callWS(m);
const cur = await ws({type: 'lovelace/config', url_path: 'dashboard-school'});
const done = [];
for (const v of cur.views) {
  const url = links[v.path]; if (!url || !v.sections) continue;
  for (const s of v.sections) s.cards = (s.cards || []).filter(c => !(c.type === 'iframe' && String(c.url).includes('/k/')));
  v.sections = v.sections.filter(s => s.cards.length);
  v.sections.unshift({type: 'grid', column_span: 3, cards: [{type: 'iframe', url, aspect_ratio: '120%', title: '📚 My Tutor'}]});
  done.push(v.path);
}
await ws({type: 'lovelace/config/save', url_path: 'dashboard-school', config: cur});
return 'Tutor added to: ' + (done.join(', ') || 'no matching tabs (tab names must match the first names you gave the tutor)');
})().then(console.log);
`;
fs.writeFileSync(path.join(DATA_DIR, 'add-tutor-to-home-assistant.js'), ha);

console.log(`\nDone. Start the tutor with "npm start" in ${HERE}.\n`);
for (const c of children) console.log(`  ${c.name}'s tutor: ${base}/k/${c.token}`);
console.log(`  Your history page: ${base}/p/${cfg.parent_token}`);
console.log(`\nHome Assistant script: ${path.join(DATA_DIR, 'add-tutor-to-home-assistant.js')}`);
console.log('Keep these links private: anyone with a link can use that tutor (or read the history).');
