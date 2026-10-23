import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {curriculumAsset} from './curriculum-assets.js';
import {readCurriculum} from './curriculum-test-data.js';
const raw=async req=>{try{return new Response(fs.readFileSync(new URL('.'+new URL(req.url).pathname,import.meta.url)));}catch{return new Response('Missing',{status:404});}};
test('packed production assets expand to the complete checked curriculum before role filtering',async()=>{
 for(const name of ['daily-packets.json','daily-practice-keys.json','planner-data.json','planner-resources.json','integrated-curriculum.json']){
  const response=await curriculumAsset(new Request('https://venvlearning.com/'+name),{},raw);assert.equal(response.status,200);assert.deepEqual(await response.json(),readCurriculum(name));
 }
});
test('compressed curriculum manifests reject arbitrary asset paths',async()=>{
 await assert.rejects(()=>curriculumAsset(new Request('https://venvlearning.com/daily-packets.json'),{},async()=>Response.json({_gzip_parts:['https://example.com/private']})),/Invalid compressed curriculum manifest/);
});
