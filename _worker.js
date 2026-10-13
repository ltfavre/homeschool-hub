const json = (data, status = 200) =>
  new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });

const parseBody = async (request) => {
  try { return await request.json(); }
  catch { return null; }
};


const clean = (v) => {
  if (v === undefined || v === null) return null;
  const s = String(v).trim();
  return s === "" ? null : s;
};

const toInt = (v) => {
  if (v === undefined || v === null || v === "") return null;
  const n = Number(v);
  return Number.isInteger(n) ? n : null;
};

const toNumber = (v) => {
  if (v === undefined || v === null || v === "") return null;
  const n = Number(v);
  return Number.isFinite(n) ? n : null;
};

const isoDate = (v) => {
  const s = clean(v);
  return s && /^\\d{4}-\\d{2}-\\d{2}$/.test(s) ? s : null;
};

const authOK = (request, env) => {
  if (!env.IMPORT_TOKEN) return false;
  const auth = request.headers.get("authorization") || "";
  return auth === `Bearer ${env.IMPORT_TOKEN}`;
};

async function resolveStudent(db, row) {
  if (row.student_id) {
    const found = await db.prepare("SELECT id,name,grade FROM students WHERE id=? AND active=1")
      .bind(Number(row.student_id)).first();
    if (found) return found;
  }
  const name = clean(row.student_name || row.student);
  const grade = clean(row.grade);
  if (name) {
    const found = await db.prepare("SELECT id,name,grade FROM students WHERE lower(name)=lower(?) AND active=1 LIMIT 1")
      .bind(name).first();
    if (found) return found;
  }
  if (grade) {
    const found = await db.prepare("SELECT id,name,grade FROM students WHERE grade=? AND active=1 ORDER BY id LIMIT 1")
      .bind(grade).first();
    if (found) return found;
  }
  return null;
}

async function resolveSubject(db, row) {
  if (row.subject_id) {
    const found = await db.prepare("SELECT id,name FROM subjects WHERE id=?")
      .bind(Number(row.subject_id)).first();
    if (found) return found;
  }
  const name = clean(row.subject);
  if (!name) return null;
  let found = await db.prepare("SELECT id,name FROM subjects WHERE lower(name)=lower(?) LIMIT 1")
    .bind(name).first();
  if (found) return found;
  await db.prepare("INSERT OR IGNORE INTO subjects(name) VALUES (?)").bind(name).run();
  return await db.prepare("SELECT id,name FROM subjects WHERE lower(name)=lower(?) LIMIT 1")
    .bind(name).first();
}

async function upsertLesson(db, row, defaults={}) {
  const student = await resolveStudent(db,row);
  const subject = await resolveSubject(db,row);
  if (!student) throw new Error("Could not resolve student");
  if (!subject) throw new Error("Could not resolve subject");
  const title=clean(row.title), date=isoDate(row.lesson_date || row.date);
  if (!title) throw new Error("title is required");
  if (!date) throw new Error("lesson_date/date must be YYYY-MM-DD");
  const externalId=clean(row.external_id);
  const status=clean(row.status) || clean(defaults.status) || "planned";
  const sourceName=clean(row.source_name) || clean(defaults.source_name);
  if (externalId) {
    const existing=await db.prepare("SELECT id FROM lessons WHERE external_id=? LIMIT 1").bind(externalId).first();
    if (existing) {
      await db.prepare(`UPDATE lessons SET student_id=?,subject_id=?,title=?,lesson_date=?,segment=?,week=?,objective=?,instructions=?,resource_url=?,source_name=?,estimated_minutes=?,status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?`)
        .bind(student.id,subject.id,title,date,toInt(row.segment),toInt(row.week),clean(row.objective),clean(row.instructions),clean(row.resource_url),sourceName,toInt(row.estimated_minutes),status,existing.id).run();
      return {action:"updated",id:existing.id,external_id:externalId};
    }
  }
  const result=await db.prepare(`INSERT INTO lessons (external_id,student_id,subject_id,title,lesson_date,segment,week,objective,instructions,resource_url,source_name,estimated_minutes,status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)`)
    .bind(externalId,student.id,subject.id,title,date,toInt(row.segment),toInt(row.week),clean(row.objective),clean(row.instructions),clean(row.resource_url),sourceName,toInt(row.estimated_minutes),status).run();
  return {action:"inserted",id:result.meta.last_row_id,external_id:externalId};
}

async function upsertAssignment(db,row,defaults={}) {
  const student=await resolveStudent(db,row);
  const subject=await resolveSubject(db,row);
  if (!student) throw new Error("Could not resolve student");
  if (!subject) throw new Error("Could not resolve subject");
  const title=clean(row.title), date=isoDate(row.due_date || row.date);
  if (!title) throw new Error("title is required");
  if (!date) throw new Error("due_date/date must be YYYY-MM-DD");
  let lessonId=toInt(row.lesson_id);
  if (!lessonId && row.lesson_external_id) {
    const lesson=await db.prepare("SELECT id FROM lessons WHERE external_id=? LIMIT 1").bind(clean(row.lesson_external_id)).first();
    if (lesson) lessonId=lesson.id;
  }
  const externalId=clean(row.external_id);
  const status=clean(row.status) || clean(defaults.status) || "assigned";
  if (externalId) {
    const existing=await db.prepare("SELECT id FROM assignments WHERE external_id=? LIMIT 1").bind(externalId).first();
    if (existing) {
      await db.prepare(`UPDATE assignments SET lesson_id=?,student_id=?,subject_id=?,title=?,due_date=?,instructions=?,resource_url=?,points_possible=?,status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?`)
        .bind(lessonId,student.id,subject.id,title,date,clean(row.instructions),clean(row.resource_url),toNumber(row.points_possible),status,existing.id).run();
      return {action:"updated",id:existing.id,external_id:externalId};
    }
  }
  const result=await db.prepare(`INSERT INTO assignments (external_id,lesson_id,student_id,subject_id,title,due_date,instructions,resource_url,points_possible,status) VALUES (?,?,?,?,?,?,?,?,?,?)`)
    .bind(externalId,lessonId,student.id,subject.id,title,date,clean(row.instructions),clean(row.resource_url),toNumber(row.points_possible),status).run();
  return {action:"inserted",id:result.meta.last_row_id,external_id:externalId};
}

const legacy = {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (!url.pathname.startsWith("/api/")) {
      return env.ASSETS.fetch(request);
    }

    try {
      if (url.pathname === "/api/health") {
        return json({ ok: true, app: "homeschool-hub" });
      }

      if (url.pathname === "/api/bootstrap" && request.method === "GET") {
        const [students, subjects] = await Promise.all([
          env.DB.prepare("SELECT id,name,grade FROM students WHERE active=1 ORDER BY grade").all(),
          env.DB.prepare("SELECT id,name FROM subjects ORDER BY name").all(),
        ]);
        return json({ students: students.results, subjects: subjects.results });
      }


      if (url.pathname === "/api/import" && request.method === "POST") {
        if (!authOK(request, env)) return json({ error: "Unauthorized" }, 401);
        const body = await parseBody(request);
        if (!body || !Array.isArray(body.records)) return json({ error: "Body must be JSON with a records array" }, 400);
        if (body.records.length === 0) return json({ error: "records array is empty" }, 400);
        if (body.records.length > 500) return json({ error: "Maximum 500 records per import" }, 413);

        const defaults = body.defaults || {};
        const dryRun = body.dry_run === true;
        const results = [];
        let inserted=0, updated=0, failed=0;

        for (let i=0;i<body.records.length;i++) {
          const row=body.records[i] || {};
          const type=(clean(row.record_type || row.type || "lesson") || "lesson").toLowerCase();
          try {
            if (!["lesson","assignment"].includes(type)) throw new Error("record_type must be lesson or assignment");
            if (dryRun) {
              const student=await resolveStudent(env.DB,row), subject=await resolveSubject(env.DB,row);
              if (!student) throw new Error("Could not resolve student");
              if (!subject) throw new Error("Could not resolve subject");
              if (!clean(row.title)) throw new Error("title is required");
              const d=type === "lesson" ? isoDate(row.lesson_date || row.date) : isoDate(row.due_date || row.date);
              if (!d) throw new Error(`${type === "lesson" ? "lesson_date" : "due_date"}/date must be YYYY-MM-DD`);
              results.push({row:i+1,record_type:type,action:"valid",external_id:clean(row.external_id)});
              continue;
            }
            const out= type === "lesson" ? await upsertLesson(env.DB,row,defaults) : await upsertAssignment(env.DB,row,defaults);
            if (out.action === "inserted") inserted++;
            if (out.action === "updated") updated++;
            results.push({row:i+1,record_type:type,...out});
          } catch (error) {
            failed++;
            results.push({row:i+1,record_type:type,action:"failed",external_id:clean(row.external_id),error:error.message || "Import failed"});
          }
        }
        return json({ok:failed===0,dry_run:dryRun,summary:{total:body.records.length,inserted,updated,failed},results}, failed===body.records.length ? 400 : 200);
      }

      if (url.pathname === "/api/lessons" && request.method === "GET") {
        const start = url.searchParams.get("start") || "0000-01-01";
        const end = url.searchParams.get("end") || "9999-12-31";
        const student = url.searchParams.get("student");

        let sql = `
          SELECT l.*, s.name AS student_name, sub.name AS subject_name
          FROM lessons l
          JOIN students s ON s.id=l.student_id
          JOIN subjects sub ON sub.id=l.subject_id
          WHERE l.lesson_date BETWEEN ? AND ?`;
        const params = [start, end];

        if (student) {
          sql += " AND l.student_id=?";
          params.push(Number(student));
        }
        sql += " ORDER BY l.lesson_date, s.grade, sub.name";

        const result = await env.DB.prepare(sql).bind(...params).all();
        return json(result.results);
      }

      if (url.pathname === "/api/lessons" && request.method === "POST") {
        const b = await parseBody(request);
        if (!b?.student_id || !b?.subject_id || !b?.title || !b?.lesson_date) {
          return json({ error: "student_id, subject_id, title, and lesson_date are required" }, 400);
        }

        const result = await env.DB.prepare(`
          INSERT INTO lessons
          (student_id,subject_id,title,lesson_date,segment,week,objective,instructions,resource_url,source_name,estimated_minutes,status)
          VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        `).bind(
          b.student_id, b.subject_id, b.title, b.lesson_date,
          b.segment ?? null, b.week ?? null, b.objective ?? null,
          b.instructions ?? null, b.resource_url ?? null,
          b.source_name ?? null, b.estimated_minutes ?? null,
          b.status ?? "planned"
        ).run();

        return json({ ok: true, id: result.meta.last_row_id }, 201);
      }

      if (url.pathname === "/api/assignments" && request.method === "GET") {
        const start = url.searchParams.get("start") || "0000-01-01";
        const end = url.searchParams.get("end") || "9999-12-31";
        const result = await env.DB.prepare(`
          SELECT a.*, s.name AS student_name, sub.name AS subject_name
          FROM assignments a
          JOIN students s ON s.id=a.student_id
          JOIN subjects sub ON sub.id=a.subject_id
          WHERE a.due_date BETWEEN ? AND ?
          ORDER BY a.due_date, s.grade, sub.name
        `).bind(start, end).all();
        return json(result.results);
      }

      if (url.pathname === "/api/assignments" && request.method === "POST") {
        const b = await parseBody(request);
        if (!b?.student_id || !b?.subject_id || !b?.title || !b?.due_date) {
          return json({ error: "student_id, subject_id, title, and due_date are required" }, 400);
        }

        const result = await env.DB.prepare(`
          INSERT INTO assignments
          (lesson_id,student_id,subject_id,title,due_date,instructions,resource_url,points_possible,status)
          VALUES (?,?,?,?,?,?,?,?,?)
        `).bind(
          b.lesson_id ?? null, b.student_id, b.subject_id, b.title, b.due_date,
          b.instructions ?? null, b.resource_url ?? null, b.points_possible ?? null,
          b.status ?? "assigned"
        ).run();

        return json({ ok: true, id: result.meta.last_row_id }, 201);
      }

      return json({ error: "Not found" }, 404);
    } catch (error) {
      return json({ error: error.message || "Server error" }, 500);
    }
  },
};

const familyJson=(data,status=200,extra={})=>new Response(JSON.stringify(data),{status,headers:{'content-type':'application/json;charset=utf-8','cache-control':'no-store','x-content-type-options':'nosniff',...extra}});
const epoch=()=>Math.floor(Date.now()/1000);
const randomToken=()=>Array.from(crypto.getRandomValues(new Uint8Array(32)),b=>b.toString(16).padStart(2,'0')).join('');
const digest=async text=>Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(text))),b=>b.toString(16).padStart(2,'0')).join('');
const passwordHash=async(password,salt)=>{const key=await crypto.subtle.importKey('raw',new TextEncoder().encode(password),'PBKDF2',false,['deriveBits']);return Array.from(new Uint8Array(await crypto.subtle.deriveBits({name:'PBKDF2',salt:new TextEncoder().encode(salt),iterations:100000,hash:'SHA-256'},key,256)),b=>b.toString(16).padStart(2,'0')).join('');};
const equalHash=(a,b)=>{let d=a.length^b.length;for(let i=0;i<Math.max(a.length,b.length);i++)d|=(a.charCodeAt(i)||0)^(b.charCodeAt(i)||0);return d===0;};
const publicUser=u=>({id:u.id,username:u.username,display_name:u.display_name,role:u.role,grade:u.grade,ready:!!u.password_hash});
const cookie=(token,maxAge=604800)=>`__Host-venv_session=${token}; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=${maxAge}`;
async function familyUser(request,env){const t=(request.headers.get('cookie')||'').match(/(?:^|;\s*)__Host-venv_session=([a-f0-9]{64})(?:;|$)/)?.[1];if(!t)return null;return env.DB.prepare('SELECT u.* FROM family_sessions s JOIN family_users u ON u.id=s.user_id WHERE s.token_hash=? AND s.expires_at>? AND u.active=1').bind(await digest(t),epoch()).first();}
async function sessionResponse(user,env){const t=randomToken();await env.DB.prepare('INSERT INTO family_sessions(token_hash,user_id,expires_at) VALUES(?,?,?)').bind(await digest(t),user.id,epoch()+604800).run();return familyJson({user:publicUser(user),redirect:user.role==='parent'?'/planner':'/agenda'},200,{'set-cookie':cookie(t)});}
async function assetJson(request,env,path){const r=await env.ASSETS.fetch(new Request(new URL(path,request.url)));if(!r.ok)throw Error('Curriculum unavailable');return r.json();}
function centralDate(){return new Intl.DateTimeFormat('en-CA',{timeZone:'America/Chicago',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());}
function safeDate(d){if(!/^\d{4}-\d{2}-\d{2}$/.test(d))return false;const value=new Date(d+'T12:00:00Z');return !isNaN(value)&&value.toISOString().slice(0,10)===d;}
async function rateLimit(request,env,username){for(const key of ['ip:'+ (request.headers.get('cf-connecting-ip')||'unknown'),'user:'+username]){const bucket=await digest(key)+':'+Math.floor(epoch()/900);const r=await env.DB.prepare('INSERT INTO family_login_limits(bucket,attempts,expires_at) VALUES(?,1,?) ON CONFLICT(bucket) DO UPDATE SET attempts=attempts+1 RETURNING attempts').bind(bucket,epoch()+1800).first();if(r.attempts>20)return false;}return true;}
async function authRoute(request,env,user,url){
 const path=url.pathname,method=request.method;
 if(method!=='GET'&&method!=='HEAD'){
  if(request.headers.get('origin')!==url.origin||!(request.headers.get('content-type')||'').startsWith('application/json'))return familyJson({error:'Please use the website form.'},403);
  if(Number(request.headers.get('content-length')||0)>16384)return familyJson({error:'Request too large'},413);
 }
 if(path==='/api/family/login'&&method==='POST'){
  const b=await request.json(),username=String(b.username||'').trim().toLowerCase().slice(0,200),password=String(b.password||'');
  if(password.length>256||!await rateLimit(request,env,username))return familyJson({error:'Too many attempts. Try again in 15 minutes.'},429);
  const u=await env.DB.prepare('SELECT * FROM family_users WHERE username=? AND active=1').bind(username).first();
  const hash=await passwordHash(password,u?.password_salt||'invalid-account-comparison-salt');
  if(!u?.password_hash||!equalHash(hash,u.password_hash))return familyJson({error:'Username or password did not match. Children: ask a parent to set your password if this is your first login.'},401);
  return sessionResponse(u,env);
 }
 if(path==='/api/family/activate'&&method==='POST'){
  const b=await request.json();if(!/^[a-f0-9]{64}$/.test(b.token||'')||typeof b.password!=='string'||b.password.length<12||b.password.length>256)return familyJson({error:'Use the setup link and a password with at least 12 characters.'},400);
  if(!await rateLimit(request,env,'activation'))return familyJson({error:'Try again in 15 minutes.'},429);
  const h=await digest(b.token),invite=await env.DB.prepare('SELECT * FROM family_invites WHERE token_hash=? AND expires_at>?').bind(h,epoch()).first();if(!invite)return familyJson({error:'This setup link has expired or was already used.'},400);
  const salt=randomToken(),hash=await passwordHash(b.password,salt);
  const result=await env.DB.batch([env.DB.prepare('UPDATE family_users SET password_hash=?,password_salt=? WHERE id=? AND EXISTS(SELECT 1 FROM family_invites WHERE token_hash=? AND expires_at>?)').bind(hash,salt,invite.user_id,h,epoch()),env.DB.prepare('DELETE FROM family_invites WHERE token_hash=?').bind(h),env.DB.prepare('DELETE FROM family_sessions WHERE user_id=?').bind(invite.user_id)]);
  if(result[0].meta.changes!==1)return familyJson({error:'Setup link was already used.'},400);
  return sessionResponse(await env.DB.prepare('SELECT * FROM family_users WHERE id=?').bind(invite.user_id).first(),env);
 }
 if(!user)return familyJson({error:'Please sign in.'},401);
 if(path==='/api/family/me'&&method==='GET')return familyJson({user:publicUser(user),today:centralDate()});
 if(path==='/api/family/reset-link'&&method==='POST'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);
  const b=await request.json(),target=await env.DB.prepare("SELECT id FROM family_users WHERE id=? AND role='parent' AND active=1").bind(String(b.id||'')).first();
  if(!target)return familyJson({error:'Parent account not found'},404);
  const token=randomToken();await env.DB.batch([env.DB.prepare('DELETE FROM family_invites WHERE user_id=?').bind(target.id),env.DB.prepare('INSERT INTO family_invites(token_hash,user_id,expires_at) VALUES(?,?,?)').bind(await digest(token),target.id,epoch()+3600)]);
  return familyJson({url:url.origin+'/login#invite='+token});
 }
 if(path==='/api/family/logout'&&method==='POST'){const t=(request.headers.get('cookie')||'').match(/__Host-venv_session=([a-f0-9]{64})/)?.[1];if(t)await env.DB.prepare('DELETE FROM family_sessions WHERE token_hash=?').bind(await digest(t)).run();return familyJson({ok:true},200,{'set-cookie':cookie('',0)});}
 if(path==='/api/family/users'&&method==='GET'){if(user.role!=='parent')return familyJson({error:'Parent access required'},403);return familyJson({users:(await env.DB.prepare('SELECT * FROM family_users WHERE active=1 ORDER BY role,grade,username').all()).results.map(publicUser)});}
 if(path==='/api/family/account'&&method==='POST'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);const b=await request.json(),target=await env.DB.prepare('SELECT * FROM family_users WHERE id=? AND active=1').bind(String(b.id||'')).first();if(!target)return familyJson({error:'Account not found'},404);
  if(target.role==='parent'&&target.id!==user.id)return familyJson({error:'Each parent manages their own password.'},403);
  const name=String(b.display_name||'').trim().slice(0,60),username=String(b.username||'').trim().toLowerCase();if(!name||!username||username.length>200||!/^[-a-z0-9@._+]+$/.test(username))return familyJson({error:'Enter a name and valid email or username.'},400);
  if(target.role==='parent'&&username!==target.username)return familyJson({error:'Parent email changes require account verification.'},400);
  if(b.password){if(typeof b.password!=='string'||b.password.length<12||b.password.length>256)return familyJson({error:'Use at least 12 characters for the password.'},400);
   if(target.role==='parent'&&!equalHash(await passwordHash(String(b.current_password||''),target.password_salt),target.password_hash))return familyJson({error:'Current password did not match'},403);
   const salt=randomToken();await env.DB.batch([env.DB.prepare('UPDATE family_users SET username=?,display_name=?,password_hash=?,password_salt=? WHERE id=?').bind(username,name,await passwordHash(b.password,salt),salt,target.id),env.DB.prepare('DELETE FROM family_sessions WHERE user_id=?').bind(target.id)]);
  }else await env.DB.prepare('UPDATE family_users SET username=?,display_name=? WHERE id=?').bind(username,name,target.id).run();
  return familyJson({ok:true,signed_out:!!b.password&&target.id===user.id});
 }
 if(path==='/api/family/agenda'&&method==='GET'){
  const date=url.searchParams.get('date')||centralDate();if(!safeDate(date))return familyJson({error:'Invalid date'},400);
  const target=user.role==='parent'?await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(url.searchParams.get('student')||'student-4').first():user;if(!target)return familyJson({error:'Student not found'},404);
  const [days,library,exams,completion]=await Promise.all([assetJson(request,env,'/daily-packets.json'),assetJson(request,env,'/planner-resources.json'),assetJson(request,env,'/assessment-student.json'),env.DB.prepare('SELECT subject,completed FROM family_completion WHERE user_id=? AND school_date=?').bind(target.id,date).all()]);
  const d=days[date]?.[target.grade];if(!d)return familyJson({student:publicUser(target),date,teaching:false,next_date:Object.keys(days).sort().find(x=>x>date)||null});
  const mapping=library.weeks[`${target.grade}-${d.module}-${d.week}`],subjects=Object.entries(mapping).map(([key,s])=>({key,topic:s.topic,resources:s.resources.map(id=>library.resources[id]),completed:completion.results.some(r=>r.subject===key&&r.completed===1)}));
  return familyJson({student:publicUser(target),date,teaching:true,module:d.module,week:d.week,tasks:d.tasks,goals:d.goals,subjects,assessment:d.assessment?{title:exams[d.assessment].title,student_pdf:'/assessments/'+d.assessment+'-student.pdf'}:null,print_url:'/daily-print?date='+date+'&grade='+target.grade});
 }
 if(path==='/api/family/completion'&&method==='POST'){
  const b=await request.json(),id=user.role==='parent'?String(b.student_id||''):user.id;if(!safeDate(String(b.date||''))||!['math','ela','science','social','spanish'].includes(b.subject)||typeof b.completed!=='boolean')return familyJson({error:'Invalid task'},400);
  const target=await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(id).first();if(!target)return familyJson({error:'Student not found'},404);const days=await assetJson(request,env,'/daily-packets.json');if(!days[b.date]?.[target.grade])return familyJson({error:'No teaching day scheduled'},400);
  await env.DB.prepare('INSERT INTO family_completion(user_id,school_date,subject,completed,updated_at) VALUES(?,?,?,?,?) ON CONFLICT(user_id,school_date,subject) DO UPDATE SET completed=excluded.completed,updated_at=excluded.updated_at').bind(id,b.date,b.subject,b.completed?1:0,epoch()).run();return familyJson({ok:true});
 }
 return familyJson({error:'Not found'},404);
}
async function familyFetch(request,env,ctx){
 const url=new URL(request.url),path=decodeURIComponent(url.pathname);
 // Source/config files must never be delivered as public static assets.
 if(/\/(?:index\.js|_worker\.js|family-server\.js|schema\.sql|wrangler\.jsonc|package\.json|README\.md|\.dev|\.git)/i.test(path))return new Response('Not found',{status:404});
 const publicPaths=['/login','/login.html','/login.js','/forgot-password','/forgot-password.html','/family.css','/styles.css','/favicon.ico'];
 const user=await familyUser(request,env);
 if(url.pathname.startsWith('/api/family/'))return authRoute(request,env,user,url);
 if(publicPaths.includes(path))return env.ASSETS.fetch(request);
 if(!user)return path.startsWith('/api/')?familyJson({error:'Please sign in.'},401):new Response(null,{status:302,headers:{location:'/login','cache-control':'no-store'}});
 if(path.startsWith('/api/')&&!['GET','HEAD'].includes(request.method)&&(request.headers.get('origin')!==url.origin||!(request.headers.get('content-type')||'').startsWith('application/json')))return familyJson({error:'Please use the website form.'},403);
 if(path==='/'&&user.role==='student')return new Response(null,{status:302,headers:{location:'/agenda','cache-control':'no-store'}});
 if(user.role==='student'){
  const allowed=['/agenda','/agenda.html','/agenda.js','/account-nav.js','/daily-print','/daily-print.html','/daily-print.js','/daily-print.css','/print-download.js','/planner-resources.json'];
  if(path==='/daily-packets.json'){const data=await assetJson(request,env,path);return familyJson(Object.fromEntries(Object.entries(data).map(([date,g])=>[date,{[user.grade]:g[user.grade]}])));}
  if(path==='/assessment-student.json'){const data=await assetJson(request,env,path);return familyJson(Object.fromEntries(Object.entries(data).filter(([,e])=>String(e.grade)===user.grade)));}
  const pdf=path.match(/^\/assessments\/g([47])-m[1-9]-(?:w[1-3]-quiz|test)-student\.pdf$/);
  if(!allowed.includes(path)&&!(pdf&&pdf[1]===user.grade))return familyJson({error:'Parent access required'},403);
  if(/^\/daily-print(?:\.html)?$/.test(path)&&(url.searchParams.get('key')==='1'||url.searchParams.get('grade')!==user.grade)){url.searchParams.delete('key');url.searchParams.set('grade',user.grade);return new Response(null,{status:302,headers:{location:url.pathname+url.search,'cache-control':'no-store'}});}
 }
 const response=path.startsWith('/api/')?await legacy.fetch(request,env,ctx):await env.ASSETS.fetch(request);
 const secured=new Response(response.body,response);secured.headers.set('cache-control','private, no-store');secured.headers.set('x-content-type-options','nosniff');secured.headers.set('referrer-policy','same-origin');secured.headers.set('x-frame-options','DENY');return secured;
}
export default {async fetch(request,env,ctx){try{return await familyFetch(request,env,ctx)}catch(e){console.error('Family request failed',e.name);return familyJson({error:'This page could not load. Please try again.'},500)}}};
