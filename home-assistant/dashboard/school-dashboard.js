// The School dashboard as installed on 2026-10-23. Paste into the Home Assistant browser console
// (signed in as an admin) to rebuild it: keeps the Checklists and Calendar tabs, adds one tab per child.
(async () => {
const hass=document.querySelector('home-assistant').hass, ws=(m)=>hass.callWS(m);
const reg=(await ws({type:'config/entity_registry/list'})).filter(e=>e.platform==='venvlearning');
const devs=await ws({type:'config/device_registry/list'});
const kids={};
for(const e of reg){const m=e.unique_id.match(/_(student-\d+)_(tasks|assignments|calendar|reading_now|assignments_due|documents)$/); if(!m) continue; (kids[m[1]] ||= {id:m[1]})[m[2]]=e.entity_id; const d=devs.find(x=>x.id===e.device_id); if(d) kids[m[1]].name=d.name_by_user||d.name;}
const list=Object.values(kids).sort((a,b)=>a.id.localeCompare(b.id));
const missing=list.filter(k=>!(k.assignments&&k.reading_now&&k.assignments_due&&k.documents));
if(missing.length) { const logs=await ws({type:'system_log/list'}).catch(()=>[]); const entry=(await ws({type:'config_entries/get'})).find(x=>x.domain==='venvlearning'); return JSON.stringify({error:'new entities not found yet', entry:entry&&{state:entry.state,reason:entry.reason}, kids:list, logs:logs.filter(l=>JSON.stringify(l).includes('venvlearning')).map(l=>({m:l.message,s:l.source,e:(l.exception||'').slice(-1200)}))}); } else {
const cur=await ws({type:'lovelace/config',url_path:'dashboard-school'});
const first=(k)=>k.name.split(' ')[0];
const headline=(k)=>`{% set d = states('${k.assignments_due}')|int(0) %}{% set late = state_attr('${k.assignments_due}','late')|int(0) %}**${first(k)}**: {% if d == 0 %}all assignments done 🎉{% else %}{{ d }} assignment{{ 's' if d != 1 }} to do{% if late %} · ⚠️ {{ late }} late{% endif %}{% endif %} · 📖 [{{ states('${k.reading_now}') }}]({{ state_attr('${k.reading_now}','link') }})`;
const readingCard=(k)=>({type:'markdown',title:'📖 Reading now',content:[
 `{% set b = '${k.reading_now}' %}### [{{ states(b) }}]({{ state_attr(b,'link') }})`,
 `*{{ state_attr(b,'author') }}* · {{ state_attr(b,'module') }} ({{ state_attr(b,'dates') }})`,'',
 `{{ state_attr(b,'pace') }}`,'',
 `[📱 Read online]({{ state_attr(b,'link') }}) · [⬇️ Download e-book]({{ state_attr(b,'download') }})`,
 `{% set p = state_attr(b,'prompts') or [] %}{% if p %}`,'**Think about it while you read:**',`{% for q in p %}- {{ q }}`,`{% endfor %}{% endif %}`,
 `{% for x in (state_attr(b,'books') or []) if x.role != 'core' %}**Also this module:** [{{ x.title }}]({{ x.read_online }}) by {{ x.author }}`,`{% endfor %}`,
 `{% set n = state_attr(b,'up_next') %}{% if n and n.books %}<small>Up next in {{ n.module_label }}: {% for x in n.books %}{{ x.title }}{{ ', ' if not loop.last }}{% endfor %}</small>{% endif %}`].join('\n')});
const filesCard=(k)=>({type:'markdown',title:'🗂️ Assignment files',content:`{% set items = state_attr('${k.assignments_due}','items') or [] %}{% set ns = namespace(any=false) %}{% for a in items if a.attachments and a.status != 'graded' %}{% set ns.any = true %}**{{ a.title }}** <small>due {{ as_datetime(a.due).strftime('%a %b %d') }}</small>\n{% for f in a.attachments %}- [{{ f.title }}]({{ f.url }})\n{% endfor %}\n{% endfor %}{% if not ns.any %}No files for your open assignments.{% endif %}`});
const gradedCard=(k)=>({type:'markdown',title:'⭐ Graded work',content:`{% set g = (state_attr('${k.assignments_due}','items') or []) | selectattr('status','eq','graded') | list %}{% if g %}{% for a in g %}- **{{ a.title }}**: {{ a.score }} / {{ a.points }}{% if a.feedback %} — *{{ a.feedback }}*{% endif %}\n{% endfor %}{% else %}Nothing graded in the last two weeks.{% endif %}`});
const docsCard=(k)=>({type:'markdown',title:'📎 From your teacher',content:`{% set d = state_attr('${k.documents}','documents') or [] %}{% if d %}{% for f in d %}- [{{ f.title }}]({{ f.url }}) <small>{{ f.added }}</small>\n{% endfor %}{% else %}Nothing shared right now.{% endif %}`});
const todo=(entity,title)=>({type:'todo-list',entity,title,hide_create:true,hide_completed:false,item_tap_action:'toggle'});
// Checklists view: keep the date chooser and calendar, add each child's assignments and reading line.
const old=cur.views.find(v=>v.path==='today')||{cards:[]};
const keepTop=old.cards.filter(c=>c.type==='entities'||c.type==='markdown');
const cal=old.cards.find(c=>c.type==='calendar');
const today={...old,title:'Checklists',path:'today',icon:'mdi:clipboard-check-outline',cards:[
 ...keepTop,
 {type:'markdown',content:list.map(headline).join('\n\n')},
 ...list.flatMap(k=>[todo(k.tasks,`${first(k)} · Lessons`),todo(k.assignments,`${first(k)} · Assignments`)]),
 ...(cal?[cal]:[])]};
const kidView=(k)=>({title:first(k),path:first(k).toLowerCase(),icon:'mdi:account-school-outline',type:'sections',max_columns:3,sections:[
 {type:'grid',cards:[{type:'markdown',content:`# Hi, ${first(k)}!\n{{ now().strftime('%A, %B') }} {{ now().day }}\n\n`+headline(k).replace(`**${first(k)}**: `,'')},todo(k.tasks,"✅ Today's lessons")]},
 {type:'grid',cards:[todo(k.assignments,'📝 Assignments'),filesCard(k),gradedCard(k)]},
 {type:'grid',cards:[readingCard(k),docsCard(k)]},
 {type:'grid',column_span:3,cards:[{type:'calendar',entities:[k.calendar],initial_view:'listWeek',title:'This week'}]}]});
const others=cur.views.filter(v=>v.path!=='today' && !list.some(k=>first(k).toLowerCase()===v.path));
const config={...cur,views:[today,...list.map(kidView),...others]};
await ws({type:'lovelace/config/save',url_path:'dashboard-school',config});
const states=Object.fromEntries(list.flatMap(k=>['assignments','reading_now','assignments_due','documents'].map(x=>[k[x],hass.states[k[x]]?.state])));
return JSON.stringify({saved:config.views.map(v=>v.path), kids:list.map(k=>({name:k.name,...k})), states});
}
})().then(console.log);
