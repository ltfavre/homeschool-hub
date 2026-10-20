// Exact assignments use physical PDF pages; printed folios are shown when verified.
export function readingsForDay(subject, date, teacher=false) {
 const day=new Date(date+'T12:00:00Z').getUTCDay(),session=day===1||day===2?1:day===3||day===4?2:0;
 return (subject?.[teacher?'teacher_readings':'readings']||[]).filter(r=>!session||!r.session||r.session===session);
}
export function readingText(r) {
 const range=a=>a[0]===a[1]?String(a[0]):a.join('–');
 return `${r.section} · ${r.printed?'printed pp. '+range(r.printed)+' · ':''}PDF pp. ${range(r.pdf)}`;
}
export function readingLink(r,resources) {const b=resources[r.resource_id];return b?{...r,title:b.title,url:b.url.split('#')[0]+'#page='+r.pdf[0]}:null;}
