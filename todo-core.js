// Builds a student's simplified daily to-do list: one group per subject activity, with a checkbox task for each thing to do.
// Textbook subjects list the unit, lesson, and the textbook and workbook pages; other subjects (electives) list the
// day's activity and assigned pages. Fridays list the weekly checks and unit tests in the workbooks.
import {readingsForDay} from './page-readings-core.js';
import {taskForSubject, subjectLabels} from './curriculum-schedule.js';

const range = p => (p[0] === p[1] ? `p. ${p[0]}` : `pp. ${p[0]}–${p[1]}`);
const SKIP = /^(Parent\b|Open the assigned|Allow about|If time allows|Check only work taught|No tests on)/i;

// "Topic - Do this. Open the assigned pages. Parent: ..." -> {topic, activity: "Do this."}
export function simplify(segment) {
  const text = String(segment || '').split(/\s+Art textbook:/)[0].replace(/^[A-Za-z]+:\s*/, '');
  const cut = text.indexOf(' - ');
  const topic = (cut > 0 ? text.slice(0, cut) : '').trim();
  const body = (cut > 0 ? text.slice(cut + 3) : text).replace(/^[^—.]{2,80}\s—\s/, '');
  const sentences = (body.match(/[^.!?]+[.!?]+(\s|$)/g) || [body]).map(s => s.trim()).filter(s => s && !SKIP.test(s));
  return {topic, activity: sentences.slice(0, 2).join(' ')};
}

function lessonGroup(subject, it) {
  const tb = it.pages?.textbook, wb = it.pages?.workbook, link = k => (it.links?.[k] || '').startsWith('/downloads/textbooks/grade') ? it.links[k] : null;
  const tasks = [];
  if (tb) tasks.push({key: `${subject}:${it.num}:read`, text: `Read Textbook Lesson ${it.num} (${range(tb)})`, link: link('textbook')});
  if (wb) tasks.push({key: `${subject}:${it.num}:work`, text: `Complete Workbook Lesson ${it.num} (${range(wb)})`, link: link('workbook')});
  return {subject, name: subjectLabels[subject] || subject, unit: `Unit ${it.unit}: ${it.unit_title}`, title: `Lesson ${it.num}: ${it.title}`, tasks};
}

export function buildTodo({day, date, mapping, book, resources}) {
  const groups = [];
  if (!day) return groups;
  book = book || {};
  for (const subject of day.subjects || []) {
    if (subject === 'review') {
      for (const [s, items] of Object.entries(book))
        for (const it of items.filter(x => x.kind === 'check' || x.kind === 'test')) {
          const wb = it.pages?.workbook;
          groups.push({subject: s, name: subjectLabels[s] || s, unit: `Unit ${it.unit}: ${it.unit_title}`, title: it.title,
            tasks: [{key: `${s}:${it.title}`, text: `Complete ${it.kind === 'test' ? 'the unit test' : 'the weekly check'} in your workbook${wb ? ` (${range(wb)})` : ''}`,
              link: it.links?.workbook || null}]});
        }
      groups.push({subject: 'review', name: 'Friday', unit: '', title: 'Finish up',
        tasks: [{key: 'review:finish', text: 'Finish anything left from this week and fix any mistakes'}]});
      continue;
    }
    const lessons = (book[subject] || []).filter(x => x.kind === 'lesson');
    const isElective = day.elective?.subject === subject;
    // Elective or non-textbook subject: the day's activity plus any assigned student pages.
    if (!lessons.length || isElective) {
      const {topic, activity} = simplify(taskForSubject(day, subject));
      const tasks = [];
      if (activity) tasks.push({key: `${subject}:activity`, text: activity});
      readingsForDay(mapping?.[subject], date).filter(r => !String(r.resource_id).startsWith('tb-')).forEach((r, i) => {
        const res = resources?.[r.resource_id];
        if (!res || res.teacher_only) return;
        const what = r.section && r.section !== res.title ? `${res.title} — ${r.section}` : res.title;
        tasks.push({key: `${subject}:read:${i}`, text: r.printed ? `Read ${what} (${range(r.printed)})` : `Open ${what}`, link: res.url.split('#')[0] + (r.pdf ? '#page=' + r.pdf[0] : '')});
      });
      if (!tasks.length) tasks.push({key: `${subject}:activity`, text: topic || 'Complete today\'s activity'});
      groups.push({subject, name: isElective ? (day.elective.title || subjectLabels[subject]) : (mapping?.[subject]?.display_name || subjectLabels[subject] || subject),
        unit: isElective ? `Elective · week ${day.elective.week}` : '', title: topic || mapping?.[subject]?.topic || '', tasks});
    }
    for (const it of lessons) groups.push(lessonGroup(subject, it));
  }
  return groups;
}

export const todoKeys = groups => groups.flatMap(g => g.tasks.map(t => t.key));
