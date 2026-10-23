window.RotationSchedule={render(rotation){
 const box=document.getElementById('rotationSchedule');if(!box||!rotation?.blocks)return;
 const el=(tag,text,cls='')=>{const n=document.createElement(tag);n.textContent=text;n.className=cls;return n;};
 box.replaceChildren(el('p','STARTS MONDAY, OCTOBER 26','eyebrow'),el('h2','Three core lessons. One elective.'),el('p','Math + ELA every Monday–Thursday. Science Monday/Wednesday; Social Studies Tuesday/Thursday. Beginner Spanish stays within ELA Tuesday/Thursday. Fridays stay flexible.'));
 const details=el('details','','support-details');details.append(el('summary','View the elective rotation and dates'));
 const list=el('div','','rotation-list');for(const b of rotation.blocks){const card=el('article','','rotation-block');card.append(el('h3',`${b.number}. ${b.title}`),el('p',`${b.start} through ${b.end} · ${b.weeks} teaching weeks`),el('p',b.note,'helper-text'));const a=el('a','Open the first week →','planner-link');a.href='/batch-print?date='+b.start;card.append(a);list.append(card);}details.append(list,el('p','School breaks do not count toward a rotation. Earlier assignments retain the previous schedule. Reading, movement, household responsibilities, and short typing practice continue between elective blocks.','helper-text'));box.append(details);
}};
