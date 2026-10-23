export function cleanTaskText(text){return String(text||'').replace(/Open the linked book and use its contents\/index for: .*?publisher order can differ from the current sequence\./g,'Open the assigned chapters and exact pages listed in Materials.').replace(/then use the reference contents\/index for supporting diagrams or examples\./g,'then use the assigned pages listed in Materials for supporting diagrams or examples.');}
// Exact assignments use physical PDF pages; printed folios are shown when verified.
export function readingsForDay(subject, date, teacher=false) {
 const day=new Date(date+'T12:00:00Z').getUTCDay(),session=day===1||day===2?1:day===3||day===4?2:0;
 return (subject?.[teacher?'teacher_readings':'readings']||[]).filter(r=>r.weekdays?r.weekdays.includes(day):!session||!r.session||r.session===session);
}
export function readingText(r) {
 const range=a=>a[0]===a[1]?String(a[0]):a.join('–');
 if(!r.pdf)return `${r.section} · printed pp. ${range(r.printed)} (use the guide's page numbers, not the PDF viewer's)`;
 return `${r.section} · ${r.printed?'printed pp. '+range(r.printed)+' · ':''}PDF pp. ${range(r.pdf)}`;
}
export function readingLink(r,resources) {const b=resources[r.resource_id];return b?{...r,title:b.title,url:b.url.split('#')[0]+(r.pdf?'#page='+r.pdf[0]:'')}:null;}
