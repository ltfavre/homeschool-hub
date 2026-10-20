import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {readingsForDay,readingText,readingLink} from './page-readings-core.js';
import {studentResourceLibrary} from './curriculum-schedule.js';
const lib=JSON.parse(fs.readFileSync(new URL('./planner-resources.json',import.meta.url),'utf8'));
test('all 560 active core lessons have student and parent page assignments',()=>{let count=0;for(const [key,mapping]of Object.entries(lib.weeks)){if(key.endsWith('-1-1'))continue;for(const [sub,p]of Object.entries(mapping)){if(sub==='review')continue;assert.ok(p.readings.length,key+sub);assert.ok(p.teacher_readings.length,key+sub);for(const r of [...p.readings,...p.teacher_readings])assert.ok(r.pdf[0]>0&&r.pdf[1]>=r.pdf[0]&&lib.resources[r.resource_id]);count++}}assert.equal(count,560)});
test('first and second meetings select separate lessons and physical page anchors',()=>{const p=lib.weeks['7-2-4'].math,a=readingsForDay(p,'2026-11-30'),b=readingsForDay(p,'2026-12-02');assert.equal(a.length,1);assert.equal(b.length,1);assert.notEqual(a[0].section,b[0].section);assert.match(readingText(a[0]),/PDF pp\./);assert.ok(readingLink(a[0],lib.resources).url.endsWith('#page='+a[0].pdf[0]))});
test('student library excludes parent preparation and teacher reading sources',()=>{const safe=studentResourceLibrary(lib);for(const m of Object.values(safe.weeks))for(const p of Object.values(m)){assert.equal(p.teacher_readings,undefined);for(const r of p.readings||[])assert.ok(safe.resources[r.resource_id]&&!safe.resources[r.resource_id].teacher_only)}});
