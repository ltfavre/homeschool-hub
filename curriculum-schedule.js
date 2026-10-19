// One source for both the website agenda and the Home Assistant calendar.
export const subjectLabels = {math:'Math',ela:'ELA',science:'Physical Sciences',social:'Social Studies',art:'Art',life:'Life Sciences',computer:'Computer Science',skills:'Life Skills',spanish:'Spanish',review:'Friday Review / Projects / Catch-up'};
export const taskPrefixes = {math:'Math:',ela:'ELA:',science:'Sci:',social:'SS:',art:'Art:',life:'Life:',computer:'CS:',skills:'Skills:',spanish:'Sp:',review:'Friday:'};
export const taskPattern = /\s+(?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)/;
export function subjectsForDay(day, mapping) {
  if (!day || !mapping) return [];
  return (day.subjects || Object.keys(mapping)).filter(key => mapping[key]);
}
export function curriculumForDay(day) { return day?.curriculum || 'khan-primary-v1'; }
export function taskForSubject(day, subject) {
  return String(day?.tasks || '').split(taskPattern).find(text => text.startsWith(taskPrefixes[subject])) || '';
}
export function studentResourceLibrary(library) {
  const resources = Object.fromEntries(Object.entries(library.resources).filter(([,r]) => !r.teacher_only));
  const weeks = Object.fromEntries(Object.entries(library.weeks).map(([id,mapping]) => [id,Object.fromEntries(Object.entries(mapping).map(([key,subject]) => {
    const {teacher_resources,mini,...safe} = subject;
    return [key,{...safe,resources:(safe.resources || []).filter(id => resources[id])}];
  }))]));
  return {...library,resources,weeks};
}
