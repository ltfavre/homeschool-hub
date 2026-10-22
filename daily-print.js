(async()=>{
 const $=id=>document.getElementById(id),node=(t,s='',c='')=>{const e=document.createElement(t);e.textContent=s;e.className=c;return e;},q=new URLSearchParams(location.search);
 let kind=q.get('key')==='1'?'keys':['work','guide','keys'].includes(q.get('kind'))?q.get('kind'):'work';let user,daily,library,exams,keys,url,sequence=0;
 async function json(path){const r=await fetch(path);if(!r.ok)throw Error('Materials could not load. Please refresh and try again.');return r.json();}
 async function render(){const token=++sequence;const date=$('schoolDate').value,grade=$('grade').value;$('packet').replaceChildren();$('daySubjects').replaceChildren(node('p','TODAY’S SUBJECTS','eyebrow'));$('daySubjects').hidden=true;$('dailyStatus').textContent='Preparing your '+({work:'worksheets',guide:'lesson guide',keys:'teacher keys'}[kind])+'…';$('print').disabled=true;$('pdfDownload').removeAttribute('href');$('pdfDownload').setAttribute('aria-disabled','true');
  document.querySelectorAll('[data-kind]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.kind===kind)));
  try{
   const rows=(grade==='both'?['4','7']:[grade]).map(g=>daily[date]?.[g]).filter(Boolean);if(!rows.length)throw Error('No teaching materials are scheduled for this date. Choose a school day.');
   $('daySubjects').hidden=false;if(kind==='keys'&&!keys)keys=await json('/daily-practice-keys.json');if(token!==sequence)return;
   const files=[];
   for(const r of rows){const record={...r,date,grade:String(r.grade||grade)};const g=String(r.grade);const title=node('div','','day-subject-row');title.append(node('strong','Grade '+g),node('span',PacketRenderer.model(record,library).subjects.map(s=>s.name).join(' · ')));$('daySubjects').append(title);
    const teaching=kind==='keys'?{...keys[date][g],date,grade:g}:record;
    const result=kind==='guide'?await PacketFiles.guide([record],library,{parent:false}):await PacketFiles.work([teaching],{teacher:kind==='keys'});
    if(token!==sequence)return;
    const filename=`Grade-${g}-${date}-${kind==='work'?'Worksheets':kind==='guide'?'Lesson-Guide':'Teacher-Keys'}.pdf`;files.push({path:filename,bytes:result.bytes,pages:result.pages});
    if(kind==='guide')$('packet').append(PacketRenderer.guide(record,library,{parent:user.role==='parent'}));
    else if(record.assessment&&kind==='keys'){const box=node('section','','card assessment-file');box.append(node('h2','Grade '+g+' · Assessment answer key'),node('p','The full teacher key is in this separate PDF.'));const preview=document.createElement('iframe');const blob=URL.createObjectURL(new Blob([result.bytes],{type:'application/pdf'}));preview.src=blob;preview.title='Grade '+g+' assessment key preview';preview.dataset.objectUrl=blob;box.append(preview);$('packet').append(box);}
    else $('packet').append(PacketRenderer.work(teaching,{teacher:kind==='keys',exam:record.assessment?exams[record.assessment]:null}));
   }
   if(url)URL.revokeObjectURL(url);url=URL.createObjectURL(files.length===1?new Blob([files[0].bytes],{type:'application/pdf'}):PacketFiles.zip(files));$('pdfDownload').href=url;$('pdfDownload').download=files.length===1?files[0].path:`Daily-${date}-${kind}.zip`;$('pdfDownload').removeAttribute('aria-disabled');$('pdfDownload').textContent=files.length===1?'Download '+({work:'worksheets PDF',guide:'lesson guide PDF',keys:'teacher keys PDF'}[kind]):'Download separate PDFs (.zip)';
   $('exportNote').textContent=kind==='work'?'Only questions, necessary passages, and writing space.':kind==='guide'?'Directions and resources only. Student work is in its own file.':'Keep this answer file separate from student work.';
   $('dailyStatus').textContent=`Ready · ${files.reduce((n,f)=>n+f.pages,0)} pages${files.length>1?' in '+files.length+' separate PDFs':''}.`;$('print').disabled=files.length!==1;$('weeklyLink').href='/batch-print?date='+date;
   const next=new URL(location.href);next.search='';next.searchParams.set('date',date);next.searchParams.set('grade',grade);next.searchParams.set('kind',kind);history.replaceState(null,'',next);document.title=({work:'Student worksheets',guide:'Lesson guide',keys:'Teacher keys'}[kind])+' · '+date+' · VenvLearning';
  }catch(e){if(token!==sequence)return;$('packet').replaceChildren();$('dailyStatus').textContent=e.message;}
 }
 try{const me=await json('/api/family/me');user=me.user;if(user.role==='student'){kind=kind==='keys'?'work':kind;$('keysTab').hidden=true;$('weeklyLink').hidden=true;$('grade').replaceChildren(node('option','Grade '+user.grade));$('grade').options[0].value=user.grade;}
  [daily,library,exams]=await Promise.all(['/daily-packets.json','/planner-resources.json','/assessment-student.json'].map(json));$('schoolDate').value=q.get('date')||me.today;if(user.role==='parent'&&['4','7','both'].includes(q.get('grade')))$('grade').value=q.get('grade');
  $('grade').addEventListener('change',render);$('schoolDate').addEventListener('change',render);for(const b of document.querySelectorAll('[data-kind]'))b.addEventListener('click',()=>{if(b.dataset.kind==='keys'&&user.role!=='parent')return;kind=b.dataset.kind;render();});$('print').addEventListener('click',()=>{if(url)window.open(url,'_blank','noopener');});
  if(user.role==='parent'){const full=$('fullPacket');full.hidden=false;full.addEventListener('click',async()=>{
   const date=$('schoolDate').value,grade=$('grade').value;full.disabled=true;const old=full.textContent;full.textContent='Building full packet…';
   try{
    if(!keys)keys=await json('/daily-practice-keys.json');
    const parts=[];const gs=grade==='both'?['4','7']:[grade];
    for(const g of gs){const rec=daily[date]?.[g];if(!rec)continue;const record={...rec,date,grade:String(rec.grade||g)};
     parts.push((await PacketFiles.guide([record],library,{parent:true})).bytes);
     parts.push((await PacketFiles.work([record],{teacher:false})).bytes);
     parts.push((await PacketFiles.work([{...keys[date][g],date,grade:String(g)}],{teacher:true})).bytes);}
    if(!parts.length)throw Error('No teaching materials are scheduled for this date. Choose a school day.');
    const merged=await PacketFiles.merge(parts,'Full day packet '+date);
    const href=URL.createObjectURL(new Blob([merged.bytes],{type:'application/pdf'}));
    const a=document.createElement('a');a.href=href;a.download=`Full-day-packet-${date}-${grade==='both'?'Grades-4-and-7':'Grade-'+grade}.pdf`;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(href),60000);
    $('dailyStatus').textContent=`Full packet ready · ${merged.pages} pages: lesson guide, student worksheets, then teacher key${gs.length>1?' for each grade':''}. Print the key pages separately from the student's pages.`;
   }catch(e){$('dailyStatus').textContent=e.message;}
   finally{full.disabled=false;full.textContent=old;}
  });}
  await render();
 }catch(e){$('dailyStatus').textContent=e.message;}
})();
