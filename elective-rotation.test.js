import test from 'node:test';
import assert from 'node:assert/strict';
import {readCurriculum as read} from './curriculum-test-data.js';
import {readingsForDay} from './page-readings-core.js';
import {subjectsForDay,taskForSubject,studentResourceLibrary} from './curriculum-schedule.js';
import {homeAssistantApi} from './home-assistant-api.js';
const days=read('daily-packets.json'),keys=read('daily-practice-keys.json'),lib=read('planner-resources.json'),planner=read('planner-data.json'),index=read('assessment-index.json');
test('both grades have daily foundations, alternating core, one shared elective, and preserved earlier work',()=>{
 let count=0;
 for(const [date,grades]of Object.entries(days))for(const [g,d]of Object.entries(grades)){
  if(date<'2026-10-26'){assert.notEqual(d.curriculum,'core-electives-v1');continue;}
  const wd=new Date(date+'T12:00Z').getUTCDay();const mapping=lib.weeks[`${g}-${d.module}-${d.week}`];
  assert.equal(d.curriculum,'core-electives-v1');assert.equal(d.elective.title,grades[g==='4'?'7':'4'].elective.title);
  assert.deepEqual(subjectsForDay(d,mapping),wd===5?['review']:['math','ela',wd===1||wd===3?'science':'social',d.elective.subject]);
  assert.equal(d.assessment,null);assert.equal(d.primary_assessments.length,0);
  for(const s of d.subjects)assert.ok(taskForSubject(d,s),date+s);
  for(const section of d.practice){assert.ok(section.items.length);assert.ok(wd===5||d.subjects.includes(section.subject)||(section.subject==='review'&&/Friday:/.test(d.tasks)));for(const q of section.items)assert.equal(q.answer,undefined);}
  assert.equal(keys[date][g].practice.length,d.practice.length);for(const s of keys[date][g].practice)for(const q of s.items)assert.ok(q.answer);
  count++;
 }
 assert.equal(count,340);
});
test('six-week art block excludes Thanksgiving, has exact daily publisher pages and no inactive elective tests',()=>{
 const b=lib.rotation.blocks[0];assert.equal(b.start,'2026-10-26');assert.equal(b.end,'2026-12-11');assert.equal(b.weeks,6);assert.equal(days['2026-11-23'],undefined);
 let n=0;
 for(const [date,grades]of Object.entries(days))for(const [g,d]of Object.entries(grades))if(d.curriculum==='core-electives-v1'&&d.elective.block===1&&d.day<4){
  const p=lib.weeks[`${g}-${d.module}-${d.week}`].art;const all=readingsForDay(p,date),refs=all.filter(r=>!r.resource_id.startsWith('medieval-overview-'));assert.equal(refs.length,2);
  if(all.length>refs.length){assert.equal(date+g,'2026-10-264');assert.ok(lib.resources[all[0].resource_id].url.startsWith('/downloads/integrated/grade4-art-medieval-'));}
  assert.match(refs[0].resource_id,/ckva-[47]-sab/);assert.ok(refs[0].pdf[0]>=8);assert.ok(refs[0].pdf[1]<=(g==='4'?86:94));
  assert.ok(readingsForDay(p,date,true).every(r=>lib.resources[r.resource_id].teacher_only));n++;
 }
 assert.equal(n,48);
 for(const e of index.assessments.filter(e=>e.date>='2026-10-26')){assert.equal(e.curriculum,'core-electives-v1');assert.match(e.student,/kind=work/);assert.match(e.key,/kind=keys/);}
});
test('Math and ELA readings select the correct daily phase and Spanish stays Tuesday/Thursday',()=>{
 const m=lib.weeks['4-1-3'];assert.deepEqual(readingsForDay(m.math,'2026-10-26'),readingsForDay(m.math,'2026-10-27'));assert.notEqual(readingsForDay(m.math,'2026-10-26')[0].section,readingsForDay(m.math,'2026-10-28')[0].section);
 for(const [date,spanish]of [['2026-10-26',false],['2026-10-27',true],['2026-10-28',false],['2026-10-29',true]])assert.equal(readingsForDay(m.ela,date).some(r=>/Spanish/.test(r.section)),spanish);
});
test('planner and curriculum agree with every daily subject list and keep school breaks',()=>{
 for(const p of planner.plans)for(const w of p.weeks)if(w.start>='2026-10-26')for(let i=0;i<5;i++){
  const dt=new Date(w.start+'T12:00Z');dt.setUTCDate(dt.getUTCDate()+i);const d=days[dt.toISOString().slice(0,10)][p.grade];assert.deepEqual(w.subjects_by_day[i],d.subjects);assert.equal(w.days[i],d.tasks);
 }
 assert.equal(planner.calendar.end,'2027-07-23');assert.equal(lib.rotation.blocks.at(-1).weeks,4);assert.equal(lib.rotation.blocks.at(-1).partial,true);
 const safe=studentResourceLibrary(lib);assert.ok(!safe.resources['ckva-4-tg']);assert.ok(safe.resources['ckva-4-sab']);
});
test('Home Assistant feed reflects both grades with four weekday tasks and no stale elective tasks',async()=>{
 const db={async batch(){return []},prepare(sql){return {bind(){return this},async run(){return {}},async first(){return sql.includes('family_settings')?{value:'a'.repeat(64)}:{id:'connection'}},async all(){return {results:sql.includes('FROM family_users')?[{id:'s4',grade:4,display_name:'Grade 4'},{id:'s7',grade:7,display_name:'Grade 7'}]:sql.includes('family_curriculum_completion')?[{user_id:'s4',school_date:'2026-10-26',subject:'math',completed:1,curriculum:'integrated-eight-v1'}]:[]}}}}};
 const r=await homeAssistantApi(new Request('https://venvlearning.com/api/home-assistant/agenda?start=2026-10-26&end=2026-10-30',{headers:{authorization:'Bearer '+'a'.repeat(64)}}),{DB:db},async(_,__,path)=>path.includes('daily-packets')?days:path.includes('reading-list')?{grades:{},modules:{}}:lib);assert.equal(r.status,200);const result=await r.json();assert.equal(result.students.length,2);
 for(const s of result.students){assert.equal(s.items.length,17);assert.deepEqual(s.items.filter(t=>t.date==='2026-10-26').map(t=>t.subject),['math','ela','science','art']);const art=s.items.find(t=>t.subject==='art');assert.match(art.summary,/Art & Art History/);assert.match(art.description,/Elective week 1\/6/);assert.match(art.description,/CKVA_G[47]_SAB/);assert.ok(!art.description.includes('_TG_'));assert.equal(s.items[0].completed,false);}
});

