(() => {
  const $ = id => document.getElementById(id);
  const node = (tag, text = '') => {const e = document.createElement(tag); e.textContent = text; return e;};
  let students, daily, keys, resources, assessments, pdfUrl;
  const addDays = (date, days) => {const d = new Date(`${date}T12:00:00Z`); d.setUTCDate(d.getUTCDate() + days); return d.toISOString().slice(0, 10);};
  function monday(date) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date || '')) throw Error('Choose a valid week.');
    const d = new Date(`${date}T12:00:00Z`);
    if (isNaN(d) || d.toISOString().slice(0, 10) !== date) throw Error('Choose a valid week.');
    return addDays(date, -((d.getUTCDay() + 6) % 7));
  }
  const fmt = date => new Date(`${date}T12:00:00`).toLocaleDateString('en-US', {month: 'short', day: 'numeric', year: 'numeric'});
  function clearResult() {
    if (pdfUrl) URL.revokeObjectURL(pdfUrl);
    pdfUrl = null;
    for (const id of ['downloadBatch', 'openBatch']) $(id).removeAttribute('href');
    $('ready').hidden = true;
    $('contents').hidden = true;
  }
  function changeSelection() {
    clearResult();
    try {const start = monday($('weekDate').value); $('weekRange').textContent = `${fmt(start)} – ${fmt(addDays(start, 4))}`;}
    catch {$('weekRange').textContent = '';}
    $('batchStatus').textContent = 'Choose students and materials, then prepare the weekly PDF.';
  }
  async function json(path) {
    const response = await fetch(path);
    if (response.status === 401) {location.replace('/login'); throw Error('Please sign in.');}
    if (!response.ok) throw Error('Some materials could not load. Please refresh and try again.');
    return response.json();
  }
  async function build(event) {
    event.preventDefault();
    clearResult();
    $('build').disabled = true;
    const controls = [...$('batchForm').querySelectorAll('input')];
    controls.forEach(control => {control.disabled = true;});
    try {
      const start = monday($('weekDate').value);
      const selected = students.filter(student => document.getElementById(`student-${student.id}`).checked);
      const studentMaterials = $('includeStudents').checked, teacherMaterials = $('includeTeacher').checked;
      if (!selected.length) throw Error('Select at least one student.');
      if (!studentMaterials && !teacherMaterials) throw Error('Select student materials, teacher materials, or both.');
      const dates = Array.from({length: 5}, (_, index) => addDays(start, index));
      const jobs = [];
      for (const student of selected) {
        const grade = String(student.grade);
        const days = dates.filter(date => daily[date]?.[grade]);
        if (studentMaterials && days.length) jobs.push({teacher: false, grade, name: student.display_name, days});
      }
      if (teacherMaterials) for (const grade of new Set(selected.map(student => String(student.grade)))) {
        const days = dates.filter(date => daily[date]?.[grade]);
        if (days.length) jobs.push({teacher: true, grade, name: `Teacher · Grade ${grade}`, days});
      }
      if (!jobs.length) throw Error('No teaching materials are scheduled for this week. Choose another week.');
      const documentPdf = await PDFLib.PDFDocument.create();
      documentPdf.setTitle(`VenvLearning weekly materials · ${start}`);
      const fetched = new Map();
      async function append(bytes) {
        const source = await PDFLib.PDFDocument.load(bytes);
        const pages = await documentPdf.copyPages(source, source.getPageIndices());
        for (const page of pages) documentPdf.addPage(page);
      }
      async function appendPaper(paper, title) {await append(await PrintDownload.create(paper, title).arrayBuffer());}
      const contents = [];
      for (const job of jobs) {
        $('batchStatus').textContent = `Preparing ${job.name}…`;
        // Start each student's packet and each teacher section on a fresh sheet
        // when the combined document is printed double-sided.
        if (documentPdf.getPageCount() % 2) documentPdf.addPage().setSize(612, 792);
        const cover = node('article');
        cover.append(node('h1', job.teacher ? `TEACHER MATERIALS · Grade ${job.grade}` : `${job.name} · Grade ${job.grade}`),
          node('p', `Week of ${fmt(start)} – ${fmt(addDays(start, 4))}`),
          node('p', job.teacher ? 'Answer keys — keep separate from student packets.' : 'Daily lesson plans, practice worksheets, and scheduled assessments.'),
          node('p', `${job.days.length} teaching days: ${job.days.map(fmt).join('; ')}`));
        await appendPaper(cover, `${job.name} · Week ${start}`);
        for (const date of job.days) {
          const record = (job.teacher ? keys : daily)[date]?.[job.grade];
          if (!record) throw Error(`Teacher materials are missing for Grade ${job.grade}, ${date}.`);
          await appendPaper(PacketRenderer.day(record, resources, {teacher: job.teacher, studentName: job.name}), `${job.name} · ${date}`);
          if (record.assessment) {
            const assessment = assessments.assessments.find(entry => entry.id === record.assessment);
            const path = assessment?.[job.teacher ? 'key' : 'student'];
            if (!path || !path.startsWith('/assessments/') || !path.endsWith('.pdf')) throw Error(`An assessment is missing for Grade ${job.grade}, ${date}.`);
            if (!fetched.has(path)) {
              const response = await fetch(path);
              if (!response.ok) throw Error(`The ${job.teacher ? 'teacher key' : 'student assessment'} for ${date} could not load. Please try again.`);
              fetched.set(path, await response.arrayBuffer());
            }
            await append(fetched.get(path));
          }
        }
        contents.push(`${job.teacher ? 'Teacher keys' : job.name} · Grade ${job.grade} · ${job.days.length} teaching days${job.teacher ? ' · practice and assessment keys' : ' · worksheets and assessments'}`);
        await new Promise(resolve => setTimeout(resolve, 0));
      }
      const bytes = await documentPdf.save();
      pdfUrl = URL.createObjectURL(new Blob([bytes], {type: 'application/pdf'}));
      $('downloadBatch').href = pdfUrl;
      $('downloadBatch').download = `VenvLearning-Week-${start}-Materials.pdf`;
      $('openBatch').href = pdfUrl;
      $('contentsList').replaceChildren(...contents.map(text => node('li', text)));
      $('contents').hidden = false;
      $('ready').hidden = false;
      $('batchStatus').textContent = `Ready: ${documentPdf.getPageCount()} pages in one PDF. Download or open it to print the entire week once.`;
    } catch (error) {
      clearResult();
      $('batchStatus').textContent = error.message || 'The weekly PDF could not be prepared. Please try again.';
    } finally {
      controls.forEach(control => {control.disabled = false;});
      $('build').disabled = false;
    }
  }
  async function init() {
    try {
      const me = await json('/api/family/me');
      if (me.user.role !== 'parent') {location.replace('/agenda'); return;}
      if (!window.PDFLib || !window.PrintDownload || !window.PacketRenderer) throw Error('The PDF tools could not load. Please refresh and try again.');
      const users = await json('/api/family/users');
      students = users.users.filter(user => user.role === 'student');
      if (!students.length) throw Error('Add student accounts before preparing a weekly bundle.');
      $('students').replaceChildren(...students.map(student => {
        const label = node('label'); label.className = 'check';
        const check = node('input'); check.type = 'checkbox'; check.id = `student-${student.id}`; check.checked = true;
        label.append(check, node('span', `${student.display_name} · Grade ${student.grade}`)); return label;
      }));
      [daily, keys, resources, assessments] = await Promise.all(['/daily-packets.json', '/daily-practice-keys.json', '/planner-resources.json', '/assessment-index.json'].map(json));
      const requested = new URLSearchParams(location.search).get('date');
      try {$('weekDate').value = monday(requested || me.today);} catch {$('weekDate').value = monday(me.today);}
      $('batchForm').addEventListener('submit', build);
      $('batchForm').addEventListener('change', changeSelection);
      $('build').disabled = false;
      changeSelection();
    } catch (error) {$('batchStatus').textContent = error.message;}
  }
  init();
})();
