function cleanTaskText(text){return String(text||'').replace(/Open the linked book and use its contents\/index for: .*?publisher order can differ from the current sequence\./g,'Open the assigned chapters and exact pages listed in Materials.').replace(/then use the reference contents\/index for supporting diagrams or examples\./g,'then use the assigned pages listed in Materials for supporting diagrams or examples.');}
// Exact assignments use physical PDF pages; printed folios are shown when verified.
function readingsForDay(subject, date, teacher=false) {
 const day=new Date(date+'T12:00:00Z').getUTCDay(),session=day===1||day===2?1:day===3||day===4?2:0;
 return (subject?.[teacher?'teacher_readings':'readings']||[]).filter(r=>!session||!r.session||r.session===session);
}
function readingText(r) {
 const range=a=>a[0]===a[1]?String(a[0]):a.join('–');
 if(!r.pdf)return `${r.section} · printed pp. ${range(r.printed)} (use the guide's page numbers, not the PDF viewer's)`;
 return `${r.section} · ${r.printed?'printed pp. '+range(r.printed)+' · ':''}PDF pp. ${range(r.pdf)}`;
}
function readingLink(r,resources) {const b=resources[r.resource_id];return b?{...r,title:b.title,url:b.url.split('#')[0]+(r.pdf?'#page='+r.pdf[0]:'')}:null;}

window.PageReadings={clean:cleanTaskText,append(subject,library,parent,{date,teacher=false}={}){
 const refs=date?readingsForDay(subject,date,teacher):subject?.[teacher?'teacher_readings':'readings']||[];
 if(!refs.length)return;
 const box=document.createElement('section');box.className='assigned-readings';const h=document.createElement('h4');h.textContent=teacher?'Parent preparation — exact pages':'Assigned reading — exact pages';box.append(h);
 for(const ref of refs){const r=readingLink(ref,library.resources);if(!r)continue;const item=document.createElement('div');item.className='reading-item';const a=document.createElement('a');a.href=r.url;a.target='_blank';a.rel='noopener';a.className='reading-open';a.textContent=r.section+' ↗';const book=document.createElement('p');book.className='reading-book';book.textContent=r.title;const pages=document.createElement('p');pages.className='reading-pages';const range=n=>n[0]===n[1]?String(n[0]):n.join('–');pages.textContent=(r.printed?'Printed '+range(r.printed)+' · ':'')+'PDF '+range(r.pdf);if(!date&&r.session)pages.textContent+=' · '+(r.session===1?'First meeting':'Second meeting');item.append(a,pages,book);if(r.note){const note=document.createElement('p');note.className='reading-note';note.textContent=r.note;item.append(note)}box.append(item);}parent.append(box);
}};
