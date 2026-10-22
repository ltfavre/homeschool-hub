#!/usr/bin/env python3
"""Builds books-library.json: every book/workbook/reader linked in the lesson plans, by grade and subject."""
import json, glob, collections
SUBJ = {'math':'Math','ela':'Language arts','science':'Science','social':'Social studies','art':'Art, music & theatre',
        'life':'Life science','computer':'Computer science','skills':'Life skills','spanish':'Spanish','review':'Review'}
res = {}; weeks = {}
for f in sorted(glob.glob('curriculum-data/assigned-resources-0*.json')):
    d = json.load(open(f)); res.update(d.get('resources', {}))
    weeks.update(d.get('weeks', {}))
KEYS = ('book', 'workbook', 'reader', 'booklet', 'textbook', 'activity guide')
def is_book(r):
    return any(k in (r.get('kind', '') + ' ' + r.get('title', '')).lower() for k in KEYS) and 'collection' not in r.get('kind', '').lower()
use = collections.defaultdict(set)
for k, w in weeks.items():
    g = k.split('-')[0]
    if g not in ('4', '7'): continue
    for s, v in w.items():
        if not isinstance(v, dict): continue
        for field, teacher in (('resources', False), ('teacher_resources', True)):
            for rid in v.get(field, []):
                r = res.get(rid)
                if r and is_book(r): use[(g, s, rid, teacher)].add(k)
items = {}
for (g, s, rid, teacher), wk in use.items():
    r = res[rid]
    key = (g, s, r['url'], teacher or bool(r.get('teacher_only')))
    e = items.setdefault(key, dict(grade=int(g), subject=s, title=r['title'], url=r['url'], provider=r.get('provider', ''),
                                   kind=r.get('kind', ''), access=r.get('access', ''), teacher=key[3], weeks=set()))
    e['weeks'] |= wk
out = []
for e in items.values():
    e['weeks'] = len(e['weeks']); out.append(e)
out.sort(key=lambda e: (e['grade'], list(SUBJ).index(e['subject']) if e['subject'] in SUBJ else 99, e['teacher'], -e['weeks'], e['title']))
json.dump(dict(subjects=SUBJ, items=out), open('books-library.json', 'w'), separators=(',', ':'), ensure_ascii=False)
c = collections.Counter((e['grade'], e['subject'], e['teacher']) for e in out)
print(len(out), 'books'); [print(k, v) for k, v in sorted(c.items())]
