import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {readCurriculum as read} from './curriculum-test-data.js';
import {buildTodo,todoKeys,simplify} from './todo-core.js';
const days=read('daily-packets.json'),lib=read('planner-resources.json'),tb=JSON.parse(fs.readFileSync(new URL('./textbook-schedule.json',import.meta.url))).grades;
const todo=(date,g)=>{const day=days[date]?.[g];return buildTodo({day,date,mapping:day&&lib.weeks[`${g}-${day.module}-${day.week}`],book:tb[g][date],resources:lib.resources});};
test('a textbook day lists each lesson with unit, textbook pages, and workbook pages',()=>{
 const g=todo('2026-10-28','4'),math=g.find(x=>x.subject==='math');
 assert.equal(math.unit,'Unit 1: Place Value, Rounding, and Whole Numbers');assert.equal(math.title,'Lesson 1.2: Place Value to One Million');
 assert.deepEqual(math.tasks.map(t=>t.text),['Read Textbook Lesson 1.2 (pp. 12–13)','Complete Workbook Lesson 1.2 (pp. 12–13)']);
 assert.deepEqual([...new Set(g.map(x=>x.subject))],['math','ela','science','spanish','art']);
 assert.ok(g.filter(x=>x.subject==='art').length===2,'art elective activity and art textbook lesson');
});
test('students never get teacher pages or parent-only links, and every task key is unique',()=>{
 for(const [date,grades]of Object.entries(days))if(date>='2026-10-27')for(const g of Object.keys(grades)){
  const groups=todo(date,g),keys=todoKeys(groups);assert.equal(new Set(keys).size,keys.length,date+g);
  for(const x of groups)for(const t of x.tasks){assert.ok(t.text&&!/Parent|Teacher Edition/.test(t.text),date+g+t.text);if(t.link)assert.ok(!/teacher/.test(t.link)&&!lib.resources[Object.keys(lib.resources).find(k=>lib.resources[k].url.split('#')[0]===t.link.split('#')[0])]?.teacher_only,t.link);}
 }
});
test('Friday lists the weekly checks with workbook pages',()=>{
 const g=todo('2026-10-30','4');assert.equal(g[0].title,'Weekly Check 1: Maps and Location');assert.match(g[0].tasks[0].text,/weekly check in your workbook \(p\. \d+\)/);assert.equal(g.at(-1).subject,'review');
});
test('activity text drops parent notes and timing',()=>{
 assert.deepEqual(simplify('Art: Medieval art - Label Gothic features and sketch a gargoyle. Open the assigned student pages. Parent: use the guide. Allow about 30 minutes.'),{topic:'Medieval art',activity:'Label Gothic features and sketch a gargoyle.'});
});
test('ELA days with a Reader assignment list the Reader part and pages',()=>{
 const ela=todo('2026-11-03','7').find(x=>x.subject==='ela');
 assert.deepEqual(ela.tasks.map(t=>t.text),['Read Textbook Lesson 1.5 (pp. 16–17)','Read in your Reader: The Tempest, Act 1, Scene 2 (first section) (pp. 62–73)','Complete Workbook Lesson 1.5 (p. 19)']);
 assert.match(ela.tasks[1].link,/^\/downloads\/textbooks\/grade7-ela-reader\.pdf#page=\d+$/);
 const ka=todo('2026-11-03','4').find(x=>x.subject==='ela');assert.equal(ka.tasks[1].text,'Read in your Reader: King Arthur, Chapter 2 (pp. 3–5)');
});
