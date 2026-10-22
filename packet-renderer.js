// Shared model keeps student work, lesson directions, and teacher answers separate.
window.PacketRenderer=(()=>{
 const node=(tag,text='',cls='')=>{const e=document.createElement(tag);e.textContent=text;e.className=cls;return e;};
 const labels={math:'Math',ela:'ELA + Spanish',science:'Physical Sciences',social:'Social Studies',spanish:'Spanish',art:'Art',life:'Life Sciences',computer:'Computer Science',skills:'Life Skills',review:'Friday review / projects'};
 const prefixes={math:'Math:',ela:'ELA:',science:'Sci:',social:'SS:',spanish:'Sp:',art:'Art:',life:'Life:',computer:'CS:',skills:'Skills:',review:'Friday:'};
 const fmt=date=>new Date(date+'T12:00:00Z').toLocaleDateString('en-US',{timeZone:'UTC',weekday:'long',month:'short',day:'numeric',year:'numeric'});
 const range=n=>n[0]===n[1]?String(n[0]):n.join('–');
 function reading(r,resources){const b=resources[r.resource_id];if(!b)return null;return {...r,book:b.title,url:b.url.split('#')[0]+(r.pdf?'#page='+r.pdf[0]:''),pages:r.pdf?'PDF pp. '+range(r.pdf)+(r.printed?' · printed '+range(r.printed):''):'printed pp. '+range(r.printed)};}
 function model(record,library,{parent=false}={}){
  const mapping=library.weeks[`${record.grade}-${record.module}-${record.week}`];if(!mapping)throw Error('This lesson’s materials are unavailable.');
  const weekday=new Date(record.date+'T12:00:00Z').getUTCDay(),session=weekday===1||weekday===2?1:weekday===3||weekday===4?2:0;
  const selected=record.subjects||Object.keys(mapping);
  return {record,subjects:selected.filter(k=>mapping[k]).map(id=>{
   const s=mapping[id],select=field=>(s[field]||[]).filter(r=>!session||!r.session||r.session===session).map(r=>reading(r,library.resources)).filter(Boolean);
   const readings=select('readings'),preparation=parent?select('teacher_readings'):[],assigned=new Set(readings.map(r=>r.resource_id));
   let task=PageReadings.clean(record.tasks).split(/\s+(?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)/).find(t=>t.startsWith(prefixes[id]))||s.topic;
   if(task.startsWith(prefixes[id]))task=task.slice(prefixes[id].length).trim();if(task.startsWith(s.topic+' — '))task=task.slice(s.topic.length+3);
   task=task.replace(/Open the assigned chapters and exact pages listed in Materials\./g,'').replace(/Read the selected passage with your parent; model an example and complete guided practice\./g,'Read together and model an example, then complete the student worksheet.').trim();
   const extras=(s.resources||[]).filter(k=>!assigned.has(k)).map(k=>({...library.resources[k],resource_id:k})).filter(r=>r.title&&!r.teacher_only);
   return {id,name:labels[id]||id,topic:s.topic,task,readings,preparation,extras};
  })};
 }
 function questions(section,parent,teacher){
  if(section.passage&&!teacher)parent.append(node('h3',section.passage_title||'Read the passage'),node('p',section.passage,'passage'));
  for(const c of teacher?[]:section.contexts||[])parent.append(node('p',c,'metadata'));
  for(const [i,q]of section.items.entries()){
   const block=node('div','','question');block.append(node('p',`${i+1}. ${q.prompt}${q.points?' ('+q.points+(q.points===1?' point)':' points)'):''}`));
   if(teacher){block.append(node('p',q.answer||'Use the assessment rubric or review the response with the student.','answer'));}
   else{const space=node('div','','work-space');space.style.minHeight=Math.max(3,q.lines||3)*16+'px';block.append(space);}
   parent.append(block);
  }
 }
 function work(record,{teacher=false,studentName='',exam=null}={}){
  const paper=node('article','','work-packet');if(teacher)paper.append(node('h1','TEACHER KEY · Grade '+record.grade),node('p',fmt(record.date),'metadata'));const sections=exam?.sections||record.practice||[];
  for(const [i,s]of sections.entries()){
   const part=node('section','',teacher?'work-section key-section':i?'print-section work-section':'work-section');
   part.append(node(teacher?'h2':'h1',s.title),node('p',`Grade ${record.grade} · ${fmt(record.date)}`,'metadata'));
   if(!teacher)part.append(node('p',`Name: ${studentName||'________________________'}    Date: __________________`));
   questions(s,part,teacher);paper.append(part);
  }
  if(!sections.length)paper.append(node('h1',teacher?'Teacher key':'Student work'),node('p','No separate question sheet is scheduled for this day.'));
  return paper;
 }
 function link(text,url,cls=''){const a=node('a',text,cls);a.href=url;a.target='_blank';a.rel='noopener';return a;}
 function resourceRows(refs,parent){for(const r of refs){const row=node('div','','guide-resource');row.append(link(r.section+' ↗',r.url,'guide-resource-title'),node('p',r.pages,'guide-pages'),node('p',r.book,'guide-book'));if(r.note)row.append(node('p',r.note,'guide-note'));parent.append(row);}}
 function guide(record,library,options={}){
  const m=model(record,library,options),paper=node('article','','lesson-guide');paper.append(node('p',`GRADE ${record.grade} · MODULE ${record.module} · WEEK ${record.week}`,'eyebrow'),node('h1',fmt(record.date)),node('p','Lesson directions & resources','guide-subtitle'));
  const overview=node('nav','','subject-jumps');overview.setAttribute('aria-label','Subjects for '+record.date);
  for(const s of m.subjects){const a=node('a',s.name);a.href=`#guide-${record.grade}-${record.date}-${s.id}`;overview.append(a);}paper.append(overview);
  const actions=node('div','','guide-actions');actions.append(link('Student worksheets PDF →',`/daily-print?date=${record.date}&grade=${record.grade}&kind=work`,'book-action'));paper.append(actions);
  const grid=node('div','','guide-grid');for(const s of m.subjects){const card=node('section','','guide-card');card.id=`guide-${record.grade}-${record.date}-${s.id}`;card.append(node('p',s.name.toUpperCase(),'subject-tag'),node('h2',s.topic));
   
   if(s.readings.length){card.append(node('h3','Open these pages'));resourceRows(s.readings,card);}
   else card.append(node('p','Use the review, project, or catch-up activity selected for today.','guide-note'));card.append(node('h3','What to do'));const sentences=s.task.match(/[^.!?]+[.!?]+(?:\s|$)|[^.!?]+$/g)||[s.task];card.append(node('p',sentences[0],'guide-task'));if(sentences.length>1){const more=node('details','','support-details');more.append(node('summary','More lesson directions'),node('p',sentences.slice(1).join(' ').trim(),'guide-task'));card.append(more);}
   if(s.extras.length){const extra=node('details','','support-details');extra.append(node('summary','Extra worksheets & optional practice'));for(const r of s.extras){const item=node('div','','guide-resource');item.append(link(r.title+' ↗',r.url,'guide-resource-title'));if(r.access)item.append(node('p',r.access,'guide-note'));extra.append(item);}card.append(extra);}
   if(s.preparation.length){const prep=node('details','','support-details');prep.append(node('summary','Parent preparation'));resourceRows(s.preparation,prep);card.append(prep);}
   grid.append(card);
  }paper.append(grid);return paper;
 }
 function weekOverview(records,library){
  const block=node('section','','week-overview');block.append(node('h2','Your week at a glance'));
  const grid=node('div','','week-day-grid');for(const r of records){const m=model(r,library),day=node('article','','week-day');day.append(node('h3',new Date(r.date+'T12:00:00Z').toLocaleDateString('en-US',{timeZone:'UTC',weekday:'long',month:'short',day:'numeric'})));
   for(const s of m.subjects)day.append(node('p',s.name,'week-subject'));
   day.append(link('Open day guide →',`/daily-print?date=${r.date}&grade=${r.grade}&kind=guide`));grid.append(day);
  }block.append(grid);return block;
 }
 return {labels,fmt,model,questions,work,guide,weekOverview,day:(record,library,options)=>work(record,options)};
})();
