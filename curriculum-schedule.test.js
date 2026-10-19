import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {subjectsForDay,curriculumForDay,studentResourceLibrary,taskForSubject} from './curriculum-schedule.js';
import {homeAssistantApi} from './home-assistant-api.js';
const read=n=>JSON.parse(fs.readFileSync(new URL(n,import.meta.url),'utf8'));
const days=read('daily-packets.json'),lib=read('planner-resources.json');
const rotation=[['math','science','art','life'],['ela','social','computer','skills'],['math','science','art','life'],['ela','social','computer','skills'],['review']];
test('every updated school day has the requested rotation and complete resources',()=>{
 let count=0;
 for(const [date,grades] of Object.entries(days))for(const [g,d] of Object.entries(grades)){
  if(date<'2026-10-19')continue;
  const weekday=new Date(date+'T12:00Z').getUTCDay();if(weekday===0||weekday===6)continue;
  const m=lib.weeks[`${g}-${d.module}-${d.week}`];assert.deepEqual(subjectsForDay(d,m),rotation[weekday-1]);
  for(const s of d.subjects){assert.ok(taskForSubject(d,s));for(const id of [...m[s].resources,...m[s].teacher_resources])assert.ok(lib.resources[id],id)}
  assert.equal(curriculumForDay(d),'integrated-eight-v1');count++;
 }
 assert.equal(count,350);
});
test('student resource library excludes all parent guides and answer-bearing mini lessons',()=>{
 const safe=studentResourceLibrary(lib);assert.ok(Object.values(safe.resources).every(r=>!r.teacher_only));
 for(const mapping of Object.values(safe.weeks))for(const s of Object.values(mapping)){assert.equal(s.teacher_resources,undefined);assert.equal(s.mini,undefined);for(const id of s.resources)assert.ok(safe.resources[id])}
});
test('student daily packets and assessments never contain answer fields',()=>{
 const scan=v=>{if(!v||typeof v!=='object')return;assert.ok(!Object.hasOwn(v,'answer'));Object.values(v).forEach(scan)};
 scan(days);scan(read('assessment-student.json'));
});
test('Home Assistant agenda emits four items per teaching day and one Friday item, with completion version isolation',async()=>{
 const db={prepare(sql){return {bind(){return this},async first(){return {id:'connection'}},async all(){return {results:sql.includes('FROM family_users')?[{id:'s4',grade:4,display_name:'Grade 4'}]:[{user_id:'s4',school_date:'2026-10-19',subject:'math',completed:1,curriculum:'khan-primary-v1'}]}}}}};
 const response=await homeAssistantApi(new Request('https://example.com/api/home-assistant/agenda?start=2026-10-19&end=2026-10-23',{headers:{authorization:'Bearer '+'a'.repeat(64)}}),{DB:db},async(_,__,path)=>path.includes('daily-packets')?days:lib);
 assert.equal(response.status,200);const result=await response.json();assert.equal(result.students[0].items.length,17);assert.equal(result.students[0].items[0].completed,false);
 assert.equal(result.students[0].items.filter(x=>x.date==='2026-10-23')[0].subject,'review');
});
test('Home Assistant rejects off-day completion and writes the updated curriculum version',async()=>{
 let written;
 const db={prepare(sql){return {values:[],bind(...values){this.values=values;return this},async first(){return sql.includes('SELECT id,grade')?{id:'s4',grade:4}:{id:'connection'}},async run(){written=this.values}}}};
 const send=subject=>homeAssistantApi(new Request('https://example.com/api/home-assistant/completion',{method:'POST',headers:{authorization:'Bearer '+'a'.repeat(64),'content-type':'application/json'},body:JSON.stringify({student_id:'s4',date:'2026-10-19',subject,completed:true})}),{DB:db},async()=>days);
 assert.equal((await send('ela')).status,400);assert.equal(written,undefined);assert.equal((await send('art')).status,200);assert.equal(written[5],'integrated-eight-v1');
});
