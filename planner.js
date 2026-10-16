const $=id=>document.getElementById(id);
const fmt=s=>new Date(s+'T12:00:00').toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric'});
const addDays=(s,n)=>{const d=new Date(s+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+n);return d.toISOString().slice(0,10)};
let breaks=[];
function el(tag,text,cls){const e=document.createElement(tag);e.textContent=text;if(cls)e.className=cls;return e}
let data;
function selected(){return data.plans.find(p=>p.grade===+$('grade').value&&p.module===+$('module').value)}
function renderPlan(){
 const p=selected(),w=p.weeks[+$('weekSelect').value-1],box=$('plan');box.replaceChildren(el('h3',p.title));
 box.append(el('p','Module mastery targets','eyebrow'));
 const targets=el('div','','targets');p.targets.forEach((t,i)=>{const a=el('article','');a.append(el('h4',['Math','ELA','Science','Social Studies','Spanish'][i]),el('p',t));targets.append(a)});box.append(targets,el('p','Standards: '+p.standards),el('h3','Week '+w.number+' · '+fmt(w.start)),el('p',w.goals));
 window.PlannerAssessments.render(p,w,box);
 window.PlannerResources.render(p,w,box);
 const batch=el('a','Batch Print this week · All students + teacher keys','planner-link');batch.href='/batch-print?date='+w.start;box.append(batch);
 const daily=el('div','','daily');w.days.forEach((t,i)=>{const a=el('article','');a.append(el('h4',['Monday','Tuesday','Wednesday','Thursday','Friday'][i]+' · '+fmt(addDays(w.start,i))));
 const printDay=el('a','Print this day');printDay.href='/daily-print.html?date='+addDays(w.start,i)+'&grade='+p.grade;a.append(printDay);
 t.split(/(?=Math:|ELA:|Sci:|SS:|Sp:)/).filter(Boolean).forEach(s=>a.append(el('p',s)));daily.append(a)});box.append(daily);
 const link=el('a','View original module pages in PDF');link.href='/downloads/Homeschool_Teacher_Planner_2026-2027_Grades_4_7.pdf#page='+p.page;box.append(link);
}
function renderCalendar(){
 const month=$('month').value,[y,m]=month.split('-').map(Number),count=new Date(y,m,0).getDate(),offset=(new Date(y,m-1,1).getDay()+6)%7;
 const grid=el('div','','calendar');['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].forEach(t=>grid.append(el('strong',t)));for(let i=0;i<offset;i++)grid.append(el('div',''));
 for(let day=1;day<=count;day++){
  const s=month+'-'+String(day).padStart(2,'0'),cell=el('div','','day');cell.append(el('strong',String(day)));const b=breaks.find(b=>s>=b[0]&&s<=b[1]);
  if(b){cell.classList.add('break');cell.append(el('span',b[2]))}else for(const p of data.plans.filter(p=>p.grade===4)){const w=p.weeks.find(w=>s>=w.start&&s<=w.assessment);if(w){cell.append(el('span','M'+p.module+' · W'+w.number));if(s===w.assessment){cell.classList.add('test');cell.append(el('span',w.number===4?'MODULE TEST':'QUIZ'))}const printDay=el('a','Print day');printDay.href='/daily-print.html?date='+s+'&grade=both';printDay.setAttribute('aria-label','Print lesson packet for '+fmt(s));cell.append(printDay)}}
  grid.append(cell);
 }$('calendarGrid').replaceChildren(grid);$('breaks').textContent=breaks.filter(b=>b[0].slice(0,7)<=month&&b[1].slice(0,7)>=month).map(b=>b[2]+': '+fmt(b[0])+' – '+fmt(b[1])).join(' · ');
}
async function init(){try{
 const r=await fetch('/planner-data.json?v=start-20261012');if(!r.ok)throw Error('Planner unavailable');data=await r.json();breaks=data.calendar.breaks; $('yearDates').textContent=fmt(data.calendar.start)+' – '+fmt(data.calendar.end)+' · 9 modules · 36 instructional weeks';
 await Promise.all([window.PlannerResources.load(),window.PlannerAssessments.load()]);
 data.plans.filter(p=>p.grade===4).forEach(p=>$('module').add(new Option('Module '+p.module+' · '+p.title.split('Module '+p.module+': ')[1].split(' | ')[0],p.module)));
 for(let i=1;i<=4;i++)$('weekSelect').add(new Option('Week '+i,i));
 const firstMonth=new Date(data.calendar.start+'T12:00:00'),lastMonth=data.calendar.end.slice(0,7); for(let d=new Date(firstMonth.getFullYear(),firstMonth.getMonth(),1);;d.setMonth(d.getMonth()+1)){const key=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0');if(key>lastMonth)break;$('month').add(new Option(d.toLocaleDateString('en-US',{month:'long',year:'numeric'}),key))}
 const today=new Intl.DateTimeFormat('en-CA',{timeZone:'America/Chicago',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
 const match=data.plans.filter(p=>p.grade===4).flatMap(p=>p.weeks.map(w=>({p,w}))).find(({w})=>today>=w.start&&today<=w.assessment);
 if(match){$('module').value=match.p.module;$('weekSelect').value=match.w.number}if([...$('month').options].some(o=>o.value===today.slice(0,7)))$('month').value=today.slice(0,7);
 data.plans.filter(p=>p.grade===4).forEach(p=>{const tr=el('tr','');tr.append(el('td','Module '+p.module));p.weeks.forEach(w=>tr.append(el('td',fmt(w.assessment))));$('tests').append(tr)});
 $('guide').textContent=data.guide;$('coverage').textContent=data.standards;$('sources').textContent=data.sources;
 ['grade','module','weekSelect'].forEach(id=>$(id).addEventListener('change',renderPlan));$('month').addEventListener('change',renderCalendar);renderPlan();renderCalendar();$('status').textContent='Khan primary curriculum · Required gap materials are labeled · Friday quizzes and module-end tests preserved · Original PDFs are archived.';
 }catch(e){$('status').textContent='The planner could not load. Please refresh or use the PDF download above.';console.error(e)}}init();
