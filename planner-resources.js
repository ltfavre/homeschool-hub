window.PlannerResources=(()=>{
 let library;
 const labels={math:'Math',ela:'ELA',science:'Physical Sciences',social:'Social Studies',art:'Art',life:'Human Sciences',computer:'Computer Science',skills:'Life Skills',spanish:'Spanish',review:'Friday Review / Projects / Catch-up'};
 const prefixes={math:'Math:',ela:'ELA:',science:'Sci:',social:'SS:',art:'Art:',life:'Life:',computer:'CS:',skills:'Skills:',spanish:'Sp:',review:'Friday:'};
 const pattern=/(?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)/;
 const names=['Monday','Tuesday','Wednesday','Thursday','Friday'];
 const node=(t,text='',cls='')=>{const e=document.createElement(t);e.textContent=text;e.className=cls;return e;};
 function links(ids,parent){const ul=node('ul','','resource-links');for(const id of ids||[]){const r=library.resources[id];if(!r)continue;const li=node('li'),a=node('a',r.title);a.href=r.url;a.target='_blank';a.rel='noopener';li.append(a,node('p',r.provider+' · '+r.access,'resource-meta'));if(r.note)li.append(node('p',r.note,'resource-note'));ul.append(li);}parent.append(ul);}
 function instructions(w,i,key){return PageReadings.clean(w.days[i].split(pattern).find(t=>t.trim().startsWith(prefixes[key]))||'');}
 function render(p,w,box){
  const panel=node('section','','resource-panel');panel.id='learningResources';panel.append(node('h3','Teach this day'),node('p','Choose a day, then open a subject.','helper-text'));
  if(!library){panel.append(node('p','Materials could not load. Refresh to try again.'));box.append(panel);return;}
  const mapping=library.weeks[`${p.grade}-${p.module}-${w.number}`];
  const toolbar=node('div','','resource-toolbar'),label=node('label','Day '),select=node('select');names.forEach((n,i)=>{const o=node('option',n);o.value=i;select.append(o)});label.append(select);
  const day=node('a','Lesson guide & links →','planner-link'),work=node('a','Student worksheets →','planner-link'),weekFiles=node('a','Prepare separate weekly files →','planner-link');weekFiles.href='/batch-print?date='+w.start;toolbar.append(label,day,work,weekFiles);panel.append(toolbar);
  const cards=node('div','','resource-cards');panel.append(cards);
  function show(){cards.replaceChildren();const i=+select.value,d=new Date(w.start+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+i);day.href='/daily-print?date='+d.toISOString().slice(0,10)+'&grade='+p.grade+'&kind=guide';work.href='/daily-print?date='+d.toISOString().slice(0,10)+'&grade='+p.grade+'&kind=work';
   const selected=w.subjects_by_day?.[i]||Object.keys(mapping);
   for(const key of selected){const s=mapping[key];if(!s)continue;const card=node('article','','resource-card'),details=node('details','','lesson-disclosure'),summary=node('summary'),title=node('div');title.append(node('span',labels[key]||key,'subject-tag'),node('h4',s.topic),node('span','Open lesson & materials','summary-hint'));summary.append(title);details.append(summary);const body=node('div','','lesson-body');const direction=instructions(w,i,key).replace(/Open the assigned chapters and exact pages listed in Materials\./g,'').trim();body.append(node('p',direction,'resource-direction'));PageReadings.append(s,library,body,{date:d.toISOString().slice(0,10)});
    if(s.teacher_resources?.length){const teacher=node('details','','support-details');teacher.append(node('summary','Parent preparation'));PageReadings.append(s,library,teacher,{date:d.toISOString().slice(0,10),teacher:true});const assigned=new Set((s.teacher_readings||[]).map(r=>r.resource_id));links(s.teacher_resources.filter(id=>!assigned.has(id)),teacher);body.append(teacher);}
    const assigned=new Set((s.readings||[]).map(r=>r.resource_id)),extraIds=s.resources.filter(id=>!assigned.has(id));if(extraIds.length){const extra=node('details','','support-details');extra.append(node('summary','Optional books & practice'));links(extraIds,extra);body.append(extra);}details.append(body);card.append(details);cards.append(card);}

  }
  select.addEventListener('change',show);show();
  box.append(panel);
 }
 async function load(){try{const r=await fetch('/planner-resources.json');if(!r.ok)throw Error('Resources unavailable');library=await r.json()}catch(e){console.error(e)}}
 return {load,render};
})();
