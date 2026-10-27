"""Put the VenvLearning textbooks, workbooks, and teacher editions into the site's plan.

Run after building the books (python3 textbooks/build_all.py):

    python3 tools/integrate-textbooks.py

What it does, for every school day from 2026-10-26 on (the current core + electives plan):
  * adds the books to the resource library (teacher editions are parent-only),
  * makes each scheduled textbook lesson the assigned reading for that day, with exact printed and PDF pages
    for the textbook and workbook (students) and the teacher edition (parents),
  * rewrites that subject's task text to point at the lesson, and lists Friday checks and tests,
  * adds Spanish (Mon-Thu) and Art (Mon/Wed) as their own subjects on days their books cover, and takes the
    old beginner-Spanish segment out of ELA on those days,
  * records each day's lesson title so the calendar, agenda, and Home Assistant show it,
  * writes textbook-schedule.json (all books, including the parent's Data Science & Psychometrics book) and
    adds every book to the Books library.

Re-runnable: the first run saves the original plan to tools/textbook-baseline.json.gz and every run starts
from that baseline, so lessons added later (as more units are written) simply appear."""
import copy, datetime as dt, gzip, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(ROOT, "textbooks"))
from curriculum_pack import load, save
from build import BOOKS

START = "2026-10-26"
DL = "/downloads/textbooks"
COVER_PAGES = 2                     # front cover + inside cover before printed page 1
BASELINE = os.path.join(ROOT, "tools", "textbook-baseline.json.gz")
SUBJECT_OF = {"math": "math", "ela": "ela", "science": "science", "social": "social", "art": "art", "spanish": "spanish", "data": "data"}
PREFIX = {"math": "Math:", "ela": "ELA:", "science": "Sci:", "social": "SS:", "spanish": "Sp:", "art": "Art:"}
LABEL = {"math": "Math", "ela": "ELA", "science": "Science", "social": "Social Studies", "spanish": "Spanish", "art": "Art"}
KIND_TITLE = {"textbook": "Student Textbook", "workbook": "Student Workbook", "teacher": "Teacher Edition"}
TASK_SPLIT = re.compile(r"\s+(?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)")
MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
OLD_SPANISH = ["Practice beginner Spanish for 10-15 minutes.",
               "Include spelling/grammar editing and 10-15 minutes of beginner Spanish practice; read or listen to model phrases and use the current Spanish booklet."]


def iso(label):
    """'Mon Oct 26' or 'Thu Nov 5 (homework) or as needed' -> '2026-10-26'."""
    m = re.match(r"\w{3} (\w{3}) (\d+)", label or "")
    if not m: return None
    mo = MONTHS[m.group(1)]
    return dt.date(2026 if mo >= 8 else 2027, mo, int(m.group(2))).isoformat()


def stem(book):
    return "data-science-psychometrics" if book.subject == "data" else f"grade{book.grade}-{book.subject}"


def page_index(book, kind):
    """heading text -> (first printed page, last printed page)"""
    path = os.path.join(ROOT, "downloads", "textbooks", f"{stem(book)}-{kind}.toc.json")
    if not os.path.exists(path): return {}
    toc = json.load(open(path)); out = {}
    last = toc[-1]["page"] + 40
    for i, e in enumerate(toc):
        nxt = next((x["page"] for x in toc[i + 1:] if x["page"] > e["page"]), None)
        out.setdefault(re.sub(r"<[^>]+>", "", e["text"]), (e["page"], (nxt - 1) if nxt else e["page"] + 3))
    return out


def rng(p): return f"p. {p[0]}" if p[0] == p[1] else f"pp. {p[0]}–{p[1]}"


def collect(key):
    """Every dated item in a book: lessons, weekly checks, reviews, and tests, with page ranges per book kind."""
    book = BOOKS[key]()
    idx = {k: page_index(book, k) for k in book.kinds}
    items = []
    for U in book.units:
        for L in U.lessons:
            head = f"Lesson {L.num}: {L.title}"
            items.append(dict(date=iso(L.date), kind="lesson", unit=U.num, unit_title=U.title, num=L.num, title=L.title, heading=head,
                              pages={k: idx[k].get(head) for k in book.kinds}))
        for C in list(U.checks) + [U.test]:
            items.append(dict(date=iso(C.date), kind="test" if C.kind == "test" else "check", unit=U.num, unit_title=U.title, title=C.title, minutes=C.minutes,
                              pages={"workbook": idx.get("workbook", {}).get(C.title), "teacher": idx.get("teacher", {}).get(C.title + " — Answer Key")}))
        R = U.review
        items.append(dict(date=iso(R.date), kind="review", unit=U.num, unit_title=U.title, title=R.title,
                          pages={"workbook": idx.get("workbook", {}).get(R.title), "teacher": idx.get("teacher", {}).get(R.title + " — Answer Key")}))
    return book, [i for i in items if i["date"]]


def rid(book, kind): return f"tb-{stem(book)}-{kind}"


def resources_for(book):
    out = {}
    for kind in book.kinds:
        name = book.title if book.subject != "data" else "Data Science & Psychometrics"
        out[rid(book, kind)] = {
            "title": f"{name}: {KIND_TITLE[kind] if book.subject != 'data' else kind.title()}",
            "url": f"{DL}/{stem(book)}-{kind}.pdf", "provider": "VenvLearning", "kind": "Teacher guide" if kind == "teacher" else "Textbook",
            "access": "Parent only" if kind == "teacher" or book.subject == "data" else "Included",
            "note": {"textbook": "The lesson to read together each day.", "workbook": "Practice pages, weekly checks, and tests for every lesson.",
                     "teacher": "Lesson plans, timing, and answer keys for every workbook page, check, and test."}[kind],
            "teacher_only": kind == "teacher" or book.subject == "data", "reviewed": "2026-10-27"}
    return out


def reading(book, kind, item, weekday, section):
    p = item["pages"].get(kind)
    if not p: return None
    return {"resource_id": rid(book, kind), "section": section, "printed": [p[0], p[1]], "pdf": [p[0] + COVER_PAGES, p[1] + COVER_PAGES], "weekdays": [weekday]}


def lesson_task(subject, book, item):
    tb, wb, te = (item["pages"].get(k) for k in ("textbook", "workbook", "teacher"))
    s = f"{PREFIX[subject]} Lesson {item['num']}: {item['title']} - Read the textbook lesson together"
    s += f" ({rng(tb)})" if tb else ""
    s += f", then complete Workbook Lesson {item['num']}" + (f" ({rng(wb)})" if wb else "") + "."
    if te: s += f" Parent: Teacher Edition {rng(te)}."
    return s


def friday_task(entries):
    parts = []
    for subject, book, item in entries:
        wb = item["pages"].get("workbook")
        parts.append(f"{LABEL[subject]}: {item['title']}" + (f" (Workbook {rng(wb)})" if wb else ""))
    return "Friday: Weekly checks and tests in the workbooks: " + "; ".join(parts) + ". Then finish, revise, take a field trip, or catch up."


def split_tasks(text):
    return [s.strip() for s in TASK_SPLIT.split(text.strip().strip('"')) if s.strip()]


def drop_old_spanish(seg):
    for s in OLD_SPANISH:
        seg = seg.replace(" " + s, "").replace(s, "Include spelling/grammar editing." if "spelling/grammar" in s else "")
    return seg.strip()


def is_spanish_resource(r):
    return bool(re.search(r"lightbulblanguages|spanishlearninglab|[Ss]panish", json.dumps(r)))


def main():
    days, lib = load("daily-packets.json"), load("planner-resources.json")
    planner, ic = load("planner-data.json"), load("integrated-curriculum.json")
    books_lib = json.load(open(os.path.join(ROOT, "books-library.json")))
    if not os.path.exists(BASELINE):
        json.dump({"days": days, "lib": lib, "planner": planner, "ic": ic, "books": books_lib}, gzip.open(BASELINE, "wt"), ensure_ascii=False)
    base = json.load(gzip.open(BASELINE, "rt"))
    days, lib, planner, ic, books_lib = (copy.deepcopy(base[k]) for k in ("days", "lib", "planner", "ic", "books"))

    schedule = {"4": {}, "7": {}, "parent": {}}
    by_date = {}          # (grade, date) -> {subject: [(book, item)]}
    all_books = {}
    for key in ["math4", "math7", "ela4", "ela7", "sci4", "sci7", "ss4", "ss7", "span4", "span7", "art4", "art7", "data"]:
        book, items = collect(key)
        all_books[key] = book
        lib["resources"].update(resources_for(book))
        for it in items:
            g = "parent" if book.subject == "data" else str(book.grade)
            schedule[g].setdefault(it["date"], {}).setdefault(book.subject, []).append(
                {k: it[k] for k in ("kind", "unit", "unit_title", "title") if k in it} | ({"num": it["num"]} if "num" in it else {})
                | {"links": {k: f"{DL}/{stem(book)}-{k}.pdf#page={p[0] + COVER_PAGES}" for k, p in it["pages"].items() if p}}
                | {"pages": {k: list(p) for k, p in it["pages"].items() if p}})
            if g != "parent": by_date.setdefault((g, it["date"]), {}).setdefault(book.subject, []).append((book, it))

    spanish_ids = {k for k, r in lib["resources"].items() if is_spanish_resource(r) and not k.startswith("tb-")}
    touched = set(); changed_days = 0
    for date in sorted(days):
        if date < START: continue
        for g, d in days[date].items():
            todays = by_date.get((g, date), {})
            if not todays: continue
            wd = dt.date.fromisoformat(date).isoweekday() % 7          # JS getUTCDay: Mon=1 ... Fri=5
            wkey = f"{g}-{d['module']}-{d['week']}"
            mapping = lib["weeks"][wkey]
            segs = split_tasks(d["tasks"]); subjects = list(d["subjects"])
            if wd == 5:
                entries = [(s, b, it) for s in ["math", "ela", "science", "social", "spanish", "art"] for b, it in todays.get(s, []) if it["kind"] in ("check", "test")]
                if entries and "review" in mapping:
                    segs = [x for x in segs if not x.startswith("Friday:")] + [friday_task(entries)]
                    rv = mapping["review"]
                    for s, b, it in entries:
                        r = reading(b, "workbook", it, 5, f"{LABEL[s]}: {it['title']}")
                        if r: rv.setdefault("readings", []).append(r)
                        t = reading(b, "teacher", it, 5, f"{LABEL[s]}: {it['title']} answer key")
                        if t: rv.setdefault("teacher_readings", []).append(t)
                        for k in ("workbook",):
                            if rid(b, k) not in rv.setdefault("resources", []): rv["resources"].append(rid(b, k))
                        if rid(b, "teacher") not in rv.setdefault("teacher_resources", []): rv["teacher_resources"].append(rid(b, "teacher"))
                    rv.setdefault("daily", {})[date] = "Weekly checks: " + ", ".join(f"{LABEL[s]} {it['title'].split(':')[0]}" for s, b, it in entries)
                    touched.add(wkey)
            else:
                for s in ["math", "ela", "science", "social", "spanish", "art"]:
                    lessons = [(b, it) for b, it in todays.get(s, []) if it["kind"] == "lesson"]
                    if not lessons: continue
                    b, it = lessons[0]
                    if s not in subjects:
                        if s in ("science", "social", "math", "ela"): continue          # core rotation stays as planned
                        pos = max([subjects.index(x) + 1 for x in ("math", "ela", "science", "social", "spanish") if x in subjects] or [0])
                        subjects.insert(pos, s)
                    # weekly mapping: textbook readings replace the old selections (art keeps its elective pages alongside)
                    m = mapping.setdefault(s, {"resources": [], "teacher_resources": [], "readings": [], "teacher_readings": []})
                    if not m.get("textbook"):
                        if s != "art" or "display_name" not in m or m.get("category") != "Elective":
                            m["readings"], m["teacher_readings"] = [], []
                        m["textbook"] = stem(b)
                        if s == "spanish": m.update(display_name="Spanish", category="World language")
                        if s == "art" and not m.get("display_name"): m.update(display_name="Art", category="Arts")
                    for k in ("textbook", "workbook"):
                        if rid(b, k) not in m.setdefault("resources", []): m["resources"].insert(0 if k == "textbook" else 1, rid(b, k))
                    if rid(b, "teacher") not in m.setdefault("teacher_resources", []): m["teacher_resources"].insert(0, rid(b, "teacher"))
                    m["primary"] = rid(b, "textbook")
                    for k, label in (("textbook", "Textbook"), ("workbook", "Workbook practice")):
                        r = reading(b, k, it, wd, f"{label} · Lesson {it['num']}: {it['title']}")
                        if r: m["readings"].append(r)
                    t = reading(b, "teacher", it, wd, f"Teacher Edition · Lesson {it['num']} plan and answer key")
                    if t: m["teacher_readings"].append(t)
                    m.setdefault("daily", {})[date] = f"Lesson {it['num']}: {it['title']}"
                    m["mode"] = "VenvLearning textbook" + (" + elective pages" if s == "art" and m.get("category") == "Elective" else "")
                    m["reading_instruction"] = ("Read the textbook lesson together, then complete the matching workbook pages. "
                                                "Exact printed and PDF pages are listed for each day; the Teacher Edition pages are under Parent preparation.")
                    m.pop("gap_note", None)
                    units = sorted({(x[1]["unit"], x[1]["unit_title"]) for dd in range(5) for x in by_date.get((g, (dt.date.fromisoformat(date) - dt.timedelta(wd - 1 - dd)).isoformat()), {}).get(s, [])})
                    if units and s != "art": m["topic"] = f"Unit {units[0][0]}: {units[0][1]}"
                    elif units and m.get("category") != "Elective": m["topic"] = f"Unit {units[0][0]}: {units[0][1]}"
                    seg = lesson_task(s, b, it)
                    old = next((i for i, x in enumerate(segs) if x.startswith(PREFIX[s])), None)
                    if s == "art" and old is not None and mapping.get("art", {}).get("category") == "Elective":
                        segs[old] = segs[old] + " Art textbook: " + seg[len(PREFIX[s]) + 1:]
                    elif old is not None: segs[old] = seg
                    else:
                        at = next((i for i, x in enumerate(segs) if x.split(":")[0] + ":" in ("Art:", "Life:", "CS:", "Skills:")), len(segs))
                        segs.insert(at, seg)
                    touched.add(wkey)
                if any(it["kind"] == "lesson" for b, it in todays.get("spanish", [])):
                    segs = [drop_old_spanish(x) if x.startswith("ELA:") else x for x in segs]
                    e = mapping.get("ela")
                    if e:
                        moved = [r for r in e.get("readings", []) if r.get("resource_id") in spanish_ids]
                        e["readings"] = [r for r in e.get("readings", []) if r.get("resource_id") not in spanish_ids]
                        e["teacher_readings"] = [r for r in e.get("teacher_readings", []) if r.get("resource_id") not in spanish_ids]
                        sp_res = [x for x in e.get("resources", []) if x in spanish_ids]
                        e["resources"] = [x for x in e.get("resources", []) if x not in spanish_ids]
                        e["supplements"] = [x for x in e.get("supplements", []) if x not in spanish_ids]
                        e.pop("spanish_topic", None)
                        if e.get("gap_note"): e["gap_note"] = e["gap_note"].replace(", and a beginner Spanish segment", "")
                        if e.get("reading_instruction"): e["reading_instruction"] = e["reading_instruction"].replace(" Beginner Spanish uses its separate selection within this block.", "")
                        sp = mapping.get("spanish")
                        if sp is not None:
                            for x in sp_res:
                                if x not in sp["resources"]: sp["resources"].append(x)
                            sp.setdefault("supplements", [])
                            for x in sp_res:
                                if x not in sp["supplements"]: sp["supplements"].append(x)
            new_tasks = " ".join(segs)
            if new_tasks != d["tasks"] or subjects != d["subjects"]:
                d["tasks"], d["subjects"] = new_tasks, subjects; changed_days += 1

    # one copy of each reading per weekday (re-runs and multi-week units never duplicate)
    for wkey in touched:
        for s in lib["weeks"][wkey].values():
            for k in ("readings", "teacher_readings"):
                seen, keep = set(), []
                for r in s.get(k, []):
                    sig = json.dumps(r, sort_keys=True)
                    if sig not in seen: seen.add(sig); keep.append(r)
                s[k] = keep

    # planner keeps a copy of every day's tasks and subjects
    for p in planner["plans"]:
        for w in p["weeks"]:
            start = dt.date.fromisoformat(w["start"])
            for i in range(5):
                dd = (start + dt.timedelta(i)).isoformat(); rec = days.get(dd, {}).get(str(p["grade"]))
                if rec and dd >= START:
                    w["days"][i] = rec["tasks"]
                    if "subjects_by_day" in w: w["subjects_by_day"][i] = rec["subjects"]

    # weekly notes: Spanish now meets Mon-Thu wherever the Spanish book has lessons
    SP_OLD, SP_NEW = "Spanish is Tuesday/Thursday.", "Spanish is Monday–Thursday from the VenvLearning Spanish textbook."
    sp_weeks = set()
    for date, gd in days.items():
        for g, d in gd.items():
            if any(it["kind"] == "lesson" for b, it in by_date.get((g, date), {}).get("spanish", [])):
                d["integration"] = (d.get("integration") or "").replace(SP_OLD, SP_NEW); sp_weeks.add((g, d["module"], d["week"]))
    for p in planner["plans"]:
        for w in p["weeks"]:
            if (str(p["grade"]), p["module"], w["number"]) in sp_weeks:
                if w.get("integration"): w["integration"] = w["integration"].replace(SP_OLD, SP_NEW)
                if w.get("goals") and "Spanish Monday" not in w["goals"]:
                    w["goals"] = w["goals"].replace("Social Studies Tuesday/Thursday.", "Social Studies Tuesday/Thursday; Spanish Monday–Thursday.")
    for w in ic["weeks"]:
        if (str(w["grade"]), w["module"], w["week"]) in sp_weeks:
            w["integration"] = (w.get("integration") or "").replace(SP_OLD, SP_NEW)
            m = lib["weeks"].get(f"{w['grade']}-{w['module']}-{w['week']}", {}).get("spanish")
            if m: w["subjects"]["spanish"] = {"topic": m.get("topic", "Spanish"), "resources": m["resources"], "teacher_resources": m["teacher_resources"], "reading_instruction": m.get("reading_instruction", "")}
            e = w["subjects"].get("ela")
            if e and e.get("reading_instruction"):
                e["reading_instruction"] = re.sub(r"\s*Spanish: .*$", "", e["reading_instruction"])
                e["resources"] = [x for x in e["resources"] if x not in spanish_ids]

    # weekly pattern and subject list
    lib["rotation"]["weekly_pattern"] = {
        "Monday": ["Math", "ELA", "Science", "Spanish", "Art", "Current elective"], "Tuesday": ["Math", "ELA", "Social Studies", "Spanish", "Current elective"],
        "Wednesday": ["Math", "ELA", "Science", "Spanish", "Art", "Current elective"], "Thursday": ["Math", "ELA", "Social Studies", "Spanish", "Current elective"],
        "Friday": ["Weekly checks and unit tests from the workbooks", "Projects / field trips / catch-up"]}
    if not any(s["id"] == "spanish" for s in ic["subjects"]):
        ic["subjects"].insert(4, {"id": "spanish", "name": "Spanish", "days": "Monday–Thursday"})
    for s in ic["subjects"]:
        if s["id"] in ("math", "ela"): s["days"] = "Monday–Thursday"
        if s["id"] == "art": s["days"] = "Monday / Wednesday"
    ic.setdefault("notes", []).append("VenvLearning textbooks, workbooks, and teacher editions are the primary materials for Math, ELA, Science, Social Studies, Spanish, and Art; earlier selections remain as supporting resources.") if not any("VenvLearning textbooks" in n for n in ic.get("notes", [])) else None

    # Books library: every book (Spanish and Art have their own subject; the old ELA-filed Spanish set is retired)
    books_lib["subjects"].setdefault("spanish", "Spanish"); books_lib["subjects"]["data"] = "Data Science & Psychometrics (parent)"
    books_lib["items"] = [b for b in books_lib["items"] if not ("lightbulblanguages" in (b.get("url") or "")) and not (b.get("provider") == "VenvLearning" and b.get("kind") in ("Textbook", "Teacher guide"))]
    lesson_weeks = {}
    for (g, date), subs in by_date.items():
        for s, lst in subs.items(): lesson_weeks.setdefault((g, s), set()).add(dt.date.fromisoformat(date).isocalendar()[:2])
    new_items = []
    for key, book in all_books.items():
        g = 0 if book.subject == "data" else book.grade
        weeks = len(lesson_weeks.get((str(g), book.subject), set())) or len({it["date"] for it in [] }) or (33 if book.subject == "data" else 0)
        for kind in book.kinds:
            r = resources_for(book)[rid(book, kind)]
            new_items.append({"grade": g, "subject": book.subject, "title": r["title"], "url": r["url"], "provider": "VenvLearning", "kind": r["kind"],
                              "access": r["access"], "teacher": kind == "teacher", "weeks": weeks, "note": r["note"]})
    books_lib["items"] = new_items + books_lib["items"]

    save("daily-packets.json", days); save("planner-resources.json", lib); save("planner-data.json", planner); save("integrated-curriculum.json", ic)
    json.dump(books_lib, open(os.path.join(ROOT, "books-library.json"), "w"), ensure_ascii=False, indent=1)
    json.dump({"generated": "2026-10-27", "cover_pages": COVER_PAGES, "grades": schedule}, open(os.path.join(ROOT, "textbook-schedule.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    n = {g: sum(len(v) for v in schedule[g].values()) for g in schedule}
    print(f"days updated: {changed_days}; weeks touched: {len(touched)}; scheduled items: {n}")


if __name__ == "__main__":
    main()
