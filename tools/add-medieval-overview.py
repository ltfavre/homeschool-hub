"""Add the Grade 4 medieval art overview lesson to Monday Oct 26 2026 (Art block 1, week 1).

Re-runnable: resources, readings and task text are replaced, not duplicated."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curriculum_pack import load, save

DATE, GRADE = "2026-10-26", "4"
STUDENT, TEACHER = "medieval-overview-4", "medieval-overview-4-tg"
TITLE = "Castles, Cathedrals & Colorful Glass"
OLD_ART = ("Art: Medieval European art and Gothic architecture - Identify line, shape, color, and the historical setting in medieval art. "
           "Open the assigned student pages and artwork images. Parent: use the exact teacher-guide selection. "
           "Allow about 30-40 minutes; continue unfinished art on Friday.")
NEW_ART = ("Art: Medieval European art and Gothic architecture - Start with the overview lesson “" + TITLE + "”: "
           "read pages 1-4 together (castles, Romanesque and Gothic cathedrals, stained glass, illuminated manuscripts, tapestries, mosaics), "
           "review the vocabulary, answer the five questions, then choose an art activity (illuminated initial or rose window). "
           "If time allows, look at the CKVA artwork images and identify line, shape, and color. "
           "Parent: answer guide and teaching notes are on page 8 of the parent copy. "
           "Allow about 45-60 minutes; continue unfinished art on Friday.")

res = load("planner-resources.json")
res["resources"][STUDENT] = {
    "title": TITLE + ": Medieval Art and Architecture (student lesson)",
    "url": "/downloads/integrated/grade4-art-medieval-student.pdf",
    "provider": "VenvLearning", "kind": "Printable book / activity", "access": "Free printable PDF",
    "note": "One-lesson overview: reading, vocabulary, five questions, and two art activities (7 pages).",
    "teacher_only": False, "reviewed": "2026-10-26"}
res["resources"][TEACHER] = {
    "title": TITLE + ": parent copy with answer guide",
    "url": "/downloads/integrated/grade4-art-medieval-teacher.pdf",
    "provider": "VenvLearning", "kind": "Teacher guide", "access": "Parent only",
    "note": "Same lesson as the student copy plus the answer guide and teaching notes on page 8.",
    "teacher_only": True, "reviewed": "2026-10-26"}
day = load("daily-packets.json")[DATE][GRADE]
art = res["weeks"][f"{GRADE}-{day['module']}-{day['week']}"]["art"]
if STUDENT not in art["resources"]: art["resources"].insert(0, STUDENT)
if TEACHER not in art["teacher_resources"]: art["teacher_resources"].insert(0, TEACHER)
art["readings"] = [r for r in art["readings"] if r["resource_id"] != STUDENT]
art["readings"].insert(0, {"resource_id": STUDENT, "section": TITLE + " - overview lesson, questions and art activity",
                           "pdf": [1, 7], "session": 0, "weekdays": [1],
                           "note": "Read pages 1-4 together; pages 5-7 are vocabulary, questions and the art activity."})
art["teacher_readings"] = [r for r in art["teacher_readings"] if r["resource_id"] != TEACHER]
art["teacher_readings"].insert(0, {"resource_id": TEACHER, "section": "Answer guide and teaching notes",
                                   "pdf": [8, 8], "session": 0, "weekdays": [1]})
save("planner-resources.json", res)


def retask(text):
    return text.replace(OLD_ART, NEW_ART) if OLD_ART in text else text


packets = load("daily-packets.json")
d = packets[DATE][GRADE]
assert OLD_ART in d["tasks"] or NEW_ART in d["tasks"], "unexpected art task text"
d["tasks"] = retask(d["tasks"])
d["goals"] = d["goals"]  # unchanged
save("daily-packets.json", packets)

# planner-data keeps copies of the task text
pdata = json.load(open("planner-data.json"))
packed = "_gzip_parts" in pdata
if packed: pdata = load("planner-data.json")
s = json.dumps(pdata, ensure_ascii=False)
n = s.count(json.dumps(OLD_ART, ensure_ascii=False)[1:-1])
pdata = json.loads(s.replace(json.dumps(OLD_ART, ensure_ascii=False)[1:-1], json.dumps(NEW_ART, ensure_ascii=False)[1:-1]))
if packed: save("planner-data.json", pdata)
else: json.dump(pdata, open("planner-data.json", "w"), ensure_ascii=False, separators=(",", ":"))
print("planner-data copies updated:", n)
