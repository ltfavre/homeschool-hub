// Curriculum shopping list (parent only). Suggested items live in curriculum-wishlist.json so they
// can be added with the code; the parent's status, notes and own additions are saved in D1.
const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json;charset=utf-8', 'cache-control': 'no-store', 'x-content-type-options': 'nosniff' } });
const epoch = () => Math.floor(Date.now() / 1000);
const text = (v, max) => String(v ?? '').trim().slice(0, max);
const STATUSES = ['considering', 'buy', 'bought', 'skip'];
const SCHEMA = [
  `CREATE TABLE IF NOT EXISTS family_wishlist_state (item_id TEXT PRIMARY KEY, status TEXT NOT NULL DEFAULT 'considering', note TEXT NOT NULL DEFAULT '', updated_at INTEGER NOT NULL)`,
  `CREATE TABLE IF NOT EXISTS family_wishlist_custom (id TEXT PRIMARY KEY, subject TEXT NOT NULL DEFAULT '', title TEXT NOT NULL, link TEXT NOT NULL DEFAULT '', price TEXT NOT NULL DEFAULT '', notes TEXT NOT NULL DEFAULT '', created_at INTEGER NOT NULL)`,
];
export const isWishlistPath = (path) => path === '/api/family/wishlist';

export async function wishlistRoute(request, env, user, url, assetJson) {
  if (!user) return json({ error: 'Please sign in.' }, 401);
  if (user.role !== 'parent') return json({ error: 'Parent access required' }, 403);
  const db = env.DB;
  await db.batch(SCHEMA.map((s) => db.prepare(s)));
  if (request.method === 'GET') {
    let file = { items: [] };
    try { file = await assetJson(request, env, '/curriculum-wishlist.json'); } catch { /* none yet */ }
    const state = new Map(((await db.prepare('SELECT * FROM family_wishlist_state').all()).results || []).map((r) => [r.item_id, r]));
    const custom = ((await db.prepare('SELECT * FROM family_wishlist_custom ORDER BY created_at').all()).results || [])
      .map((c) => ({ id: c.id, subject: c.subject, title: c.title, link: c.link, price: c.price, notes: c.notes, added: new Date(c.created_at * 1000).toISOString().slice(0, 10), custom: true }));
    const items = [...(file.items || []), ...custom].map((i) => ({ ...i, status: state.get(i.id)?.status || (STATUSES.includes(i.status) ? i.status : 'considering'), my_note: state.get(i.id)?.note || '' }));
    return json({ items, subjects: file.subjects || {} });
  }
  if (request.method !== 'POST') return json({ error: 'Method not allowed' }, 405);
  if (request.headers.get('origin') !== url.origin || !(request.headers.get('content-type') || '').startsWith('application/json')) return json({ error: 'Please use the website form.' }, 403);
  const b = await request.json().catch(() => null);
  if (!b) return json({ error: 'Invalid JSON body' }, 400);
  if (b.add) {
    const title = text(b.add.title, 200); if (!title) return json({ error: 'Add a title.' }, 400);
    const link = text(b.add.link, 500); if (link && !/^https?:\/\//i.test(link)) return json({ error: 'Links must start with http:// or https://' }, 400);
    const id = 'my-' + Array.from(crypto.getRandomValues(new Uint8Array(8)), (x) => x.toString(16).padStart(2, '0')).join('');
    await db.prepare('INSERT INTO family_wishlist_custom(id,subject,title,link,price,notes,created_at) VALUES(?,?,?,?,?,?,?)').bind(id, text(b.add.subject, 40), title, link, text(b.add.price, 60), text(b.add.notes, 1000), epoch()).run();
    return json({ ok: true, id }, 201);
  }
  const id = text(b.id, 80);
  if (!/^[a-z0-9-]{1,80}$/.test(id)) return json({ error: 'Invalid item' }, 400);
  if (b.delete === true) {
    await db.batch([db.prepare('DELETE FROM family_wishlist_custom WHERE id=?').bind(id), db.prepare('DELETE FROM family_wishlist_state WHERE item_id=?').bind(id)]);
    return json({ ok: true });
  }
  const status = STATUSES.includes(b.status) ? b.status : null;
  if (!status) return json({ error: 'Invalid status' }, 400);
  await db.prepare('INSERT INTO family_wishlist_state(item_id,status,note,updated_at) VALUES(?,?,?,?) ON CONFLICT(item_id) DO UPDATE SET status=excluded.status,note=excluded.note,updated_at=excluded.updated_at').bind(id, status, text(b.note, 1000), epoch()).run();
  return json({ ok: true });
}
