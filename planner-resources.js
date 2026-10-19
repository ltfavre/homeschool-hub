window.PlannerResources=(()=>{
 let library;
 const labels={math:'Math',ela:'ELA',science:'Physical Sciences',social:'Social Studies',art:'Art',life:'Life Sciences',computer:'Computer Science',skills:'Life Skills',spanish:'Spanish',review:'Friday Review / Projects / Catch-up'};
 const prefixes={math:'Math:',ela:'ELA:',science:'Sci:',social:'SS:',art:'Art:',life:'Life:',computer:'CS:',skills:'Skills:',spanish:'Sp:',review:'Friday:'};
 const pattern=/(?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)/;
 const names=['Monday','Tuesday','Wednesday','Thursday','Friday'];
 const node=(t,text='',cls='')=>{const e=document.createElement(t);e.textContent=text;e.className=cls;return e;};
 function links(ids,parent){const ul=node('ul','','resource-links');for(const id of ids||[]){const r=library.resources[id];if(!r)continue;const li=node('li'),a=node('a',r.title);a.href=r.url;a.target='_blank';a.rel='noopener';li.append(a,node('p',r.provider+' · '+r.access,'resource-meta'));if(r.note)li.append(node('p',r.note,'resource-note'));ul.append(li);}parent.append(ul);}
 function instructions(w,i,key){return w.days[i].split(pattern).find(t=>t.trim().startsWith(prefixes[key]))||'';}
 function render(p,w,box){
  const panel=node('section','','resource-panel');panel.append(node('h3','Books, teaching guides, and activities for this week'));
  if(!library){panel.append(node('p','Materials could not load. Refresh to try again.'));box.append(panel);return;}
  const mapping=library.weeks[`${p.grade}-${p.module}-${w.number}`];
  const toolbar=node('div','','resource-toolbar'),label=node('label','Day '),select=node('select');names.forEach((n,i)=>{const o=node('option',n);o.value=i;select.append(o)});label.append(select);
  const print=node('a','Download weekly materials and response sheet PDF','planner-link'),day=node('a','Open daily packet','planner-link');toolbar.append(label,print,day);panel.append(toolbar);
  const cards=node('div','','resource-cards');panel.append(cards);
  function show(){cards.replaceChildren();const i=+select.value,d=new Date(w.start+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+i);day.href='/daily-print?date='+d.toISOString().slice(0,10)+'&grade='+p.grade;
   const selected=w.subjects_by_day?.[i]||Object.keys(mapping);
   for(const key of selected){const s=mapping[key];if(!s)continue;const card=node('article','','resource-card');card.append(node('h4',(labels[key]||key)+': '+s.topic),node('p',instructions(w,i,key),'resource-direction'));KhanUI.priority(s,card);if(s.reading_instruction)card.append(node('p',s.reading_instruction));links(s.resources,card);
    if(s.teacher_resources?.length){const teacher=node('details');teacher.append(node('summary','Parent teaching guides'));links(s.teacher_resources,teacher);card.append(teacher);}cards.append(card);}
  }
  select.addEventListener('change',show);show();
  const sheet=node('section','','resource-print-sheet');sheet.append(node('h2',`Grade ${p.grade} · Module ${p.module} · Week ${w.number}`),node('p',w.start+' through '+w.assessment));if(w.integration)sheet.append(node('p',w.integration));
  for(const [key,s] of Object.entries(mapping)){if(key==='review')continue;const part=node('article','','print-subject');part.append(node('h3',(labels[key]||key)+': '+s.topic));if(s.reading_instruction)part.append(node('p',s.reading_instruction));links(s.resources,part);for(let i=0;i<5;i++){if(w.subjects_by_day&&!w.subjects_by_day[i].includes(key))continue;part.append(node('p',names[i]+': '+instructions(w,i,key)));}part.append(node('p','Evidence / work completed: __________________________________________\nOne correction or improvement: _____________________________________'));sheet.append(part);}
  sheet.append(node('p','Friday: choose review/module exam, independent study, project, field trip, or catch-up. Use assessments on taught work only.'));
  panel.append(sheet);box.append(panel);PrintDownload.prepare(print,sheet,`VenvLearning-Grade-${p.grade}-Module-${p.module}-Week-${w.number}-Materials.pdf`);
 }
 async function load(){try{const r=await fetch('/planner-resources.json');if(!r.ok)throw Error('Resources unavailable');library=await r.json()}catch(e){console.error(e)}}
 return {load,render};
})();
