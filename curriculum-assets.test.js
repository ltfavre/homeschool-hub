import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {curriculumAsset,curriculumJson} from './curriculum-assets.js';
import {readCurriculum} from './curriculum-test-data.js';
const raw=async req=>{try{return new Response(fs.readFileSync(new URL('.'+new URL(req.url).pathname,import.meta.url)));}catch{return new Response('Missing',{status:404});}};
test('packed production assets expand to the complete checked curriculum before role filtering',async()=>{
 for(const name of ['daily-packets.json','daily-practice-keys.json','planner-data.json','planner-resources.json','integrated-curriculum.json']){
  const response=await curriculumAsset(new Request('https://venvlearning.com/'+name),{},raw);assert.equal(response.status,200);assert.equal(response.headers.get('content-encoding'),'gzip');
  const text=await new Response(response.body.pipeThrough(new DecompressionStream('gzip'))).text();assert.deepEqual(JSON.parse(text),readCurriculum(name));
  assert.deepEqual(await curriculumJson(new Request('https://venvlearning.com/'+name),{},raw),readCurriculum(name));
  assert.equal(await curriculumJson(new Request('https://venvlearning.com/'+name),{},raw),await curriculumJson(new Request('https://venvlearning.com/'+name),{},raw),'parsed once and reused');
 }
});
test('compressed curriculum manifests reject arbitrary asset paths',async()=>{
 await assert.rejects(()=>curriculumAsset(new Request('https://venvlearning.com/daily-packets.json'),{},async()=>Response.json({_gzip_parts:['https://example.com/private']})),/Invalid compressed curriculum manifest/);
});
