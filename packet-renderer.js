// Shared printable content for the weekly bundle; assessment PDFs are merged separately.
window.PacketRenderer = (() => {
  const node = (tag, text = '', cls = '') => {
    const element = document.createElement(tag);
    element.textContent = text;
    element.className = cls;
    return element;
  };
  const labels = {math:'Math',ela:'ELA',science:'Physical Sciences',social:'Social Studies',spanish:'Spanish',art:'Art',life:'Life Sciences',computer:'Computer Science',skills:'Life Skills',review:'Friday Review / Projects / Catch-up'};
  function questions(section, parent, teacher) {
    const part = node('section', '', 'print-section');
    part.append(node('h2', section.title));
    if (section.passage) part.append(node('h3', section.passage_title || 'Supplied text'), node('p', section.passage, 'passage'));
    for (const context of section.contexts || []) part.append(node('p', context, 'metadata'));
    section.items.forEach((question, index) => {
      const block = node('div', '', 'question');
      block.append(node('p', `${index + 1}. ${question.prompt}${question.points ? ` (${question.points} points)` : ''}`));
      if (teacher && question.answer) block.append(node('p', question.answer, 'answer'));
      else {
        const space = node('div', '', 'work-space');
        space.style.minHeight = `${Math.max(2, question.lines || 2) * 14}px`;
        block.append(space);
      }
      part.append(block);
    });
    parent.append(part);
  }
  function day(record, resources, {teacher = false, studentName = ''} = {}) {
    const paper = node('article', '', 'grade-packet');
    const date = new Date(`${record.date}T12:00:00`).toLocaleDateString('en-US', {weekday: 'long', month: 'long', day: 'numeric', year: 'numeric'});
    paper.append(
      node('h1', `${teacher ? 'TEACHER PRACTICE KEY · ' : ''}Grade ${record.grade} · ${date}`),
      node('p', `Module ${record.module} · Week ${record.week}`, 'metadata'),
      node('p', teacher ? 'Teacher materials — keep separate from student packets.' : `Student: ${studentName || '________________________'}   Completed: ________________________`),
      node('h2', 'Daily lesson plan'),
      node('p', record.tasks.replace(/ (?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)/g, '\n'), 'day-plan'),
      node('p', `Weekly goals\n${record.goals.replace(/; (?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)/g, '\n')}`, 'metadata'),
      node('p', `Standards\n${record.standards.replace(/ \| /g, '\n')}`, 'metadata'),
      node('h2', 'Materials to open or print')
    );
    const mapping = resources.weeks[`${record.grade}-${record.module}-${record.week}`];
    if (!mapping) throw Error(`Resources are missing for Grade ${record.grade}, ${record.date}.`);
    for (const [key, subject] of Object.entries(mapping).filter(([key]) => !record.subjects || record.subjects.includes(key))) {
      const section = node('section', '', 'subject');
      section.append(node('h3', `${labels[key] || key}: ${subject.topic}`));
      PageReadings.append(subject,resources,section,{date:record.date});if(teacher)PageReadings.append(subject,resources,section,{date:record.date,teacher:true});KhanUI.priority(subject, section);if(subject.reading_instruction)section.append(node('p',subject.reading_instruction,'metadata'));
      const list = node('ul');
      for (const id of subject.resources) {
        const resource = resources.resources[id];
        if (!resource) throw Error(`A resource is missing for ${record.date}.`);
        const item = node('li');
        const link = node('a', resource.title);
        link.href = resource.url;
        item.append(node('p', resource.kind === 'Primary course' ? 'OPTIONAL KHAN SUPPORT' : 'BOOK / SUPPORTING PRACTICE', 'curriculum-label'), link,
          node('p', `${resource.provider} · ${resource.kind} · ${resource.access}`, 'metadata'));
        if (resource.note) item.append(node('p', resource.note, 'metadata'));
        list.append(item);
      }
      section.append(list);
      paper.append(section);
    }
    paper.append(node('p', 'Publisher worksheets require downloads at their source. Khan lessons and checks are completed online. This bundle includes the original VenvLearning worksheets and assessment papers.', 'metadata'));
    if (record.assessment) {
      KhanUI.assessments(record.primary_assessments, paper);
      paper.append(node('h2', teacher ? 'Assessment answer key' : 'Assessment paper'),
        node('p', 'The complete assessment PDF follows this daily lesson plan in the bundle.'));
    } else {
      for (const section of record.practice) questions(section, paper, teacher);
    }
    if (!teacher) paper.append(node('h2', 'Reflection / corrections'), node('p', 'One thing learned: ____________________________________________________'), node('p', 'One question or correction: _____________________________________________'));
    return paper;
  }
  return {day};
})();
