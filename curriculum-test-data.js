import fs from 'node:fs';
import {mergeCurriculum} from './curriculum-assets.js';
import {gunzipSync} from 'node:zlib';
export function readCurriculum(name){const read=p=>JSON.parse(fs.readFileSync(new URL(p,import.meta.url),'utf8'));const data=read(name);if(data._gzip_parts)return JSON.parse(gunzipSync(Buffer.from(data._gzip_parts.map(p=>read('.'+p).data).join(''),'base64')));return data._parts?data._parts.reduce((all,p)=>mergeCurriculum(all,read('.'+p)),{}):data;}
