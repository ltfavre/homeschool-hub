// Curriculum data is stored as gzip+base64 parts (see tools/curriculum_pack.py).
// Cloudflare limits how much CPU and memory one request may use, so this file avoids
// parsing large JSON whenever it can:
//  - Browser requests get the stored gzip bytes as-is (Content-Encoding: gzip); the
//    browser decompresses them, the Worker never parses or re-serializes the JSON.
//  - Server code (student filtering, Home Assistant, agenda) gets the parsed data from
//    curriculumJson(), which parses once per Worker instance and reuses the result.
const paths=new Set(['/daily-packets.json','/daily-practice-keys.json','/planner-data.json','/planner-resources.json','/assessment-student.json','/integrated-curriculum.json']);
const gzipCache=new Map(),jsonCache=new Map();
export function mergeCurriculum(target,source){
 for(const [key,value] of Object.entries(source)){
  if(key==='__proto__'||key==='constructor'||key==='prototype')throw Error('Invalid curriculum key');
  if(Array.isArray(value))target[key]=[...(target[key]||[]),...value];
  else if(value&&typeof value==='object')target[key]=mergeCurriculum(target[key]||{},value);
  else target[key]=value;
 }
 return target;
}
function fromBase64(text){
 if(typeof Uint8Array.fromBase64==='function')return Uint8Array.fromBase64(text);
 const binary=atob(text),bytes=new Uint8Array(binary.length);
 for(let i=0;i<binary.length;i++)bytes[i]=binary.charCodeAt(i);
 return bytes;
}
async function gzipBytes(manifest,request,env,rawAsset){
 const parts=manifest._gzip_parts;
 if(!Array.isArray(parts)||parts.length>8||parts.some(p=>typeof p!=='string'||!/^\/curriculum-data\/packed-[a-z0-9-]+\.json$/.test(p)))throw Error('Invalid compressed curriculum manifest');
 const key=parts.join('|')+'|'+(manifest.source_sha256||'');
 if(!gzipCache.has(key)){
  const pending=Promise.all(parts.map(async path=>{const r=await rawAsset(new Request(new URL(path,request.url)),env);if(!r.ok)throw Error('Curriculum part unavailable');const p=await r.json();if(typeof p.data!=='string'||p.data.length>60000)throw Error('Invalid compressed curriculum part');return p.data;})).then(data=>fromBase64(data.join('')));
  gzipCache.set(key,pending);pending.catch(()=>gzipCache.delete(key));
 }
 return gzipCache.get(key);
}
async function legacyParts(manifest,request,env,rawAsset){
 if(!Array.isArray(manifest._parts)||manifest._parts.some(p=>!/^\/curriculum-data\/[a-z0-9-]+\.json$/.test(p)))throw Error('Invalid curriculum manifest');
 const result={};
 for(let i=0;i<manifest._parts.length;i+=8){
  const parts=await Promise.all(manifest._parts.slice(i,i+8).map(async path=>{const r=await rawAsset(new Request(new URL(path,request.url)),env);if(!r.ok)throw Error('Curriculum part unavailable');return r.json()}));
  for(const part of parts)mergeCurriculum(result,part);
 }
 return result;
}
async function manifestFor(request,env,rawAsset){
 const response=await rawAsset(request,env);
 if(!response.ok)return {response};
 return {manifest:await response.json()};
}
// Response for a browser request. Packed assets are sent still gzip-compressed.
export async function curriculumAsset(request,env,rawAsset){
 if(!paths.has(new URL(request.url).pathname))return rawAsset(request,env);
 const {response,manifest}=await manifestFor(request,env,rawAsset);
 if(response)return response;
 if(manifest._gzip_parts){
  const bytes=await gzipBytes(manifest,request,env,rawAsset);
  return new Response(bytes,{headers:{'content-type':'application/json;charset=utf-8','content-encoding':'gzip','content-length':String(bytes.length)},encodeBody:'manual'});
 }
 return Response.json(manifest._parts?await legacyParts(manifest,request,env,rawAsset):manifest);
}
// Parsed data for server code. Treat the result as read-only: it is shared between requests.
export async function curriculumJson(request,env,rawAsset){
 if(!paths.has(new URL(request.url).pathname)){const r=await rawAsset(request,env);if(!r.ok)throw Error('Curriculum unavailable');return r.json();}
 const {response,manifest}=await manifestFor(request,env,rawAsset);
 if(response)throw Error('Curriculum unavailable');
 if(!manifest._gzip_parts)return manifest._parts?legacyParts(manifest,request,env,rawAsset):manifest;
 const key=new URL(request.url).pathname+'|'+(manifest.source_sha256||'');
 if(!jsonCache.has(key)){
  const pending=gzipBytes(manifest,request,env,rawAsset).then(async bytes=>{
   const text=await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'))).text();
   if(text.length>4000000)throw Error('Curriculum asset exceeds size limit');
   return JSON.parse(text);
  });
  jsonCache.set(key,pending);pending.catch(()=>jsonCache.delete(key));
 }
 return jsonCache.get(key);
}
