// Curriculum data is stored in readable, small JSON parts. Clients receive the
// same complete JSON response; authentication and student filtering stay outside.
const paths=new Set(['/daily-packets.json','/daily-practice-keys.json','/planner-data.json','/planner-resources.json','/assessment-student.json','/integrated-curriculum.json']);
export function mergeCurriculum(target,source){
 for(const [key,value] of Object.entries(source)){
  if(key==='__proto__'||key==='constructor'||key==='prototype')throw Error('Invalid curriculum key');
  if(Array.isArray(value))target[key]=[...(target[key]||[]),...value];
  else if(value&&typeof value==='object')target[key]=mergeCurriculum(target[key]||{},value);
  else target[key]=value;
 }
 return target;
}
export async function curriculumAsset(request,env,rawAsset){
 const response=await rawAsset(request,env);
 if(!response.ok||!paths.has(new URL(request.url).pathname))return response;
 const data=await response.json();
 if(data._gzip_parts){
  if(!Array.isArray(data._gzip_parts)||data._gzip_parts.length>8||data._gzip_parts.some(p=>!/^\/curriculum-data\/packed-[a-z0-9-]+\.json$/.test(p)))throw Error('Invalid compressed curriculum manifest');
  const parts=await Promise.all(data._gzip_parts.map(async path=>{const r=await rawAsset(new Request(new URL(path,request.url)),env);if(!r.ok)throw Error('Curriculum part unavailable');const p=await r.json();if(typeof p.data!=='string'||p.data.length>60000)throw Error('Invalid compressed curriculum part');return p.data;}));
  const bytes=Uint8Array.from(atob(parts.join('')),c=>c.charCodeAt(0));
  const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));
  const expanded=await new Response(stream).text();if(expanded.length>4000000)throw Error('Curriculum asset exceeds size limit');
  return Response.json(JSON.parse(expanded));
 }
 if(!data._parts)return Response.json(data);
 if(!Array.isArray(data._parts)||data._parts.some(p=>!/^\/curriculum-data\/[a-z0-9-]+\.json$/.test(p)))throw Error('Invalid curriculum manifest');
 const result={};
 // Bounded parallel reads avoid creating an unbounded set of asset subrequests.
 for(let i=0;i<data._parts.length;i+=8){
  const parts=await Promise.all(data._parts.slice(i,i+8).map(async path=>{const r=await rawAsset(new Request(new URL(path,request.url)),env);if(!r.ok)throw Error('Curriculum part unavailable');return r.json()}));
  for(const part of parts)mergeCurriculum(result,part);
 }
 return Response.json(result);
}
