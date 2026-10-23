// Builds the "School" dashboard for a shared family tablet: one tab per child with today's
// subject checklist, assignments to check off, what to read now, shared documents and the
// school calendar. Run in the Home Assistant browser console (or by Claude) while signed in
// as an admin; it finds the VenvLearning entities by their unique IDs, so names don't matter.
//
//   await buildSchoolDashboard(document.querySelector('home-assistant').hass)
async function buildSchoolDashboard(hass, { urlPath = 'school', title = 'School' } = {}) {
  const reg = await hass.callWS({ type: 'config/entity_registry/list' });
  const venv = reg.filter((e) => e.platform === 'venvlearning');
  const byDevice = new Map();
  for (const e of venv) {
    if (!e.device_id) continue;
    const kind = (e.unique_id.match(/_(tasks|assignments|calendar|reading_now|assignments_due|documents)$/) || [])[1];
    if (!kind) continue;
    if (!byDevice.has(e.device_id)) byDevice.set(e.device_id, {});
    byDevice.get(e.device_id)[kind] = e.entity_id;
  }
  const devices = await hass.callWS({ type: 'config/device_registry/list' });
  const kids = [...byDevice.entries()].filter(([, k]) => k.tasks && k.assignments).map(([id, k]) => {
    const d = devices.find((x) => x.id === id);
    return { name: d?.name_by_user || d?.name || 'Student', model: d?.model || '', ...k };
  }).sort((a, b) => a.model.localeCompare(b.model));
  if (!kids.length) throw new Error('No VenvLearning students found. Is the integration (v1.2.0+) set up?');
  const dateEntity = venv.find((e) => e.unique_id.endsWith('_school_date'))?.entity_id;
  const todayButton = venv.find((e) => e.unique_id.endsWith('_school_today'))?.entity_id;

  const view = (k) => {
    const due = k.assignments_due, read = k.reading_now, docs = k.documents;
    const header = {
      type: 'markdown',
      content: [
        `# Hi, ${k.name.split(' ')[0]}!`,
        `{{ now().strftime('%A, %B') }} {{ now().day }}` +
          (due ? ` · {% set d = states('${due}')|int(0) %}{% if d == 0 %}All assignments done 🎉{% else %}**{{ d }}** assignment{{ 's' if d != 1 }} to do{% if state_attr('${due}','late') %} · ⚠️ {{ state_attr('${due}','late') }} late{% endif %}{% endif %}` : ''),
      ].join('\n'),
    };
    const reading = read && {
      type: 'markdown',
      title: '📖 Reading now',
      content: [
        `{% set b = '${read}' %}`,
        `### [{{ states(b) }}]({{ state_attr(b,'link') }})`,
        `*{{ state_attr(b,'author') }}* · {{ state_attr(b,'module') }} ({{ state_attr(b,'dates') }})`,
        ``,
        `{{ state_attr(b,'pace') }}`,
        ``,
        `[Read online]({{ state_attr(b,'link') }}) · [Download e-book]({{ state_attr(b,'download') }})`,
        `{% set p = state_attr(b,'prompts') or [] %}{% if p %}`,
        `**Think about it:**`,
        `{% for q in p %}- {{ q }}`,
        `{% endfor %}{% endif %}`,
        `{% for x in (state_attr(b,'books') or []) if x.role != 'core' %}`,
        `**Also this module:** [{{ x.title }}]({{ x.read_online }}) by {{ x.author }}`,
        `{% endfor %}`,
        `{% set n = state_attr(b,'up_next') %}{% if n and n.books %}`,
        `<small>Up next ({{ n.module_label }}): {% for x in n.books %}{{ x.title }}{{ ', ' if not loop.last }}{% endfor %}</small>{% endif %}`,
      ].join('\n'),
    };
    const documents = docs && {
      type: 'markdown',
      title: '📎 From your teacher',
      content: `{% set d = state_attr('${docs}','documents') or [] %}{% if d %}{% for f in d %}- [{{ f.title }}]({{ f.url }}) <small>{{ f.added }}</small>\n{% endfor %}{% else %}Nothing shared right now.{% endif %}`,
    };
    const attachments = due && {
      type: 'markdown',
      title: '🗂️ Assignment files',
      content: `{% set items = state_attr('${due}','items') or [] %}{% set ns = namespace(any=false) %}{% for a in items if a.attachments and a.status != 'graded' %}{% set ns.any = true %}**{{ a.title }}** <small>due {{ as_datetime(a.due).strftime('%a %b %-d') }}</small>\n{% for f in a.attachments %}- [{{ f.title }}]({{ f.url }})\n{% endfor %}\n{% endfor %}{% if not ns.any %}No files for open assignments.{% endif %}`,
    };
    const feedback = due && {
      type: 'markdown',
      title: '⭐ Graded work',
      content: `{% set items = state_attr('${due}','items') or [] %}{% set g = items | selectattr('status','eq','graded') | list %}{% if g %}{% for a in g %}- **{{ a.title }}**: {{ a.score }} / {{ a.points }}{% if a.feedback %} — *{{ a.feedback }}*{% endif %}\n{% endfor %}{% else %}Nothing graded in the last two weeks.{% endif %}`,
    };
    return {
      title: k.name.split(' ')[0],
      path: k.name.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
      icon: 'mdi:school-outline',
      type: 'sections',
      max_columns: 3,
      sections: [
        { type: 'grid', cards: [header, { type: 'todo-list', entity: k.tasks, title: "✅ Today's lessons", hide_completed: false }].filter(Boolean) },
        { type: 'grid', cards: [{ type: 'todo-list', entity: k.assignments, title: '📝 Assignments', hide_completed: false }, attachments, feedback].filter(Boolean) },
        { type: 'grid', cards: [reading, documents].filter(Boolean) },
        { type: 'grid', column_span: 3, cards: [
          ...(dateEntity ? [{ type: 'tile', entity: dateEntity, name: 'Showing lessons for', icon: 'mdi:calendar-edit' }] : []),
          ...(todayButton ? [{ type: 'button', entity: todayButton, name: 'Back to today', icon: 'mdi:calendar-today', tap_action: { action: 'perform-action', perform_action: 'button.press', target: { entity_id: todayButton } }, show_state: false }] : []),
          ...(k.calendar ? [{ type: 'calendar', entities: [k.calendar], initial_view: 'listWeek', title: 'This week' }] : []),
        ] },
      ],
    };
  };

  const config = { title, views: kids.map(view) };
  const dashboards = await hass.callWS({ type: 'lovelace/dashboards/list' });
  if (!dashboards.some((d) => d.url_path === urlPath)) {
    await hass.callWS({ type: 'lovelace/dashboards/create', url_path: urlPath, title, icon: 'mdi:school', show_in_sidebar: true, require_admin: false, mode: 'storage' });
  }
  await hass.callWS({ type: 'lovelace/config/save', url_path: urlPath, config });
  return { url: `/${urlPath}/${config.views[0].path}`, kids: kids.map((k) => k.name) };
}
