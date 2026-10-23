#!/usr/bin/env python3
"""Adds the October 2026 gap-filling resources and the 2026-27 independent-reading list to the lesson plans.

Writes curriculum-data/assigned-resources-016.json (merged into /planner-resources.json; arrays append)
and fixes the one wrong-topic reading (Grade 7 week 2-3 science) in place. Safe to re-run."""
import json, glob

REVIEW = dict(reviewed="2026-10-23", review="Publisher page opened and contents checked 2026-10-23")
def res(title, url, provider, kind, access="Free", note="", teacher=False):
    return dict(title=title, url=url, provider=provider, kind=kind, access=access, note=note, teacher_only=teacher, **REVIEW)

CK = "Core Knowledge Foundation (CKSci, adapted from OpenSciEd)"
R = {
 # Grade 7: body systems (fixes the wrong-topic week 2-3 reading)
 "ck-g6-cells-sr": res("Cells and Systems - Student Reader - Publisher Grade 6", "https://www.coreknowledge.org/wp-content/uploads/2022/11/CKSci_G6U6_Cells-and-Systems_SR_Web.pdf", CK, "Printable book / reader", "Free printable PDF", "Bones, muscles, nerve cells and healing; written for middle school."),
 "ck-g6-cells-swp": res("Cells and Systems - Student Work Pages - Publisher Grade 6", "https://www.coreknowledge.org/wp-content/uploads/2022/11/CKSci_G6U6_Cells-and-Systems_SWP_Web.pdf", CK, "Printable workbook", "Free printable PDF"),
 "ck-g6-cells-tg": res("Cells and Systems - Teacher Guide - Publisher Grade 6", "https://www.coreknowledge.org/wp-content/uploads/2022/11/CKSci_G6U6_Cells-and-Systems_TG_Web.pdf", CK, "Teacher guide", "Free printable PDF", teacher=True),
 "kh68-bones": res("Bones, Muscles, and Joints (Grades 6–8 teacher's guide + handouts)", "https://Classroom.KidsHealth.org/classroom/6to8/body/parts/bones.pdf", "KidsHealth in the Classroom (Nemours)", "Teacher lesson + printable handouts", "Free printable PDF", "Paper-skeleton activity, joint types, injury-prevention flyer, quiz and key.", teacher=True),
 # Grade 7: grade-level physical and space science (replaces reliance on Grade 3-5 readers)
 "ck-g8-forces-sr": res("Contact Forces - Student Reader - Publisher Grade 8", "https://www.coreknowledge.org/wp-content/uploads/2022/04/CKSci_G8_Unit1_Contact-Forces_SR.pdf", CK, "Printable book / reader", "Free printable PDF"),
 "ck-g8-forces-tg": res("Contact Forces - Teacher Guide - Publisher Grade 8", "https://www.coreknowledge.org/wp-content/uploads/2022/04/CKSci_G8_Unit1_Contact-Forces_TG.pdf", CK, "Teacher guide", "Free printable PDF", teacher=True),
 "ck-g8-sound-sr": res("Sound Waves - Student Reader - Publisher Grade 8", "https://www.coreknowledge.org/wp-content/uploads/2022/05/CKSci_G8U2_SR_Web.pdf", CK, "Printable book / reader", "Free printable PDF"),
 "ck-g8-sound-tg": res("Sound Waves - Teacher Guide - Publisher Grade 8", "https://www.coreknowledge.org/wp-content/uploads/2022/05/CKSci_G8U2_TG_Web.pdf", CK, "Teacher guide", "Free printable PDF", teacher=True),
 "ck-g8-space-sr": res("Earth in Space - Student Reader - Publisher Grade 8", "https://www.coreknowledge.org/wp-content/uploads/2022/11/CKSci_G8U4_Earth-in-Space_SR_Web.pdf", CK, "Printable book / reader", "Free printable PDF"),
 "ck-g8-space-tg": res("Earth in Space - Teacher Guide - Publisher Grade 8", "https://www.coreknowledge.org/wp-content/uploads/2022/11/CKSci_G8U4_Earth-in-Space_TG_Web.pdf", CK, "Teacher guide", "Free printable PDF", teacher=True),
 # Levers and simple machines
 "te-levers": res("Levers That Lift (lesson, grades 7–9)", "https://www.teachengineering.org/lessons/view/cub_simp_machines_lesson03", "TeachEngineering (University of Colorado Boulder)", "Teacher lesson", "Free", "Lever, pulley and wheel-and-axle with mechanical-advantage formulas (effort arm ÷ load arm).", teacher=True),
 "phet-balance": res("Balancing Act: lever and torque simulation", "https://phet.colorado.edu/en/simulations/balancing-act", "PhET Interactive Simulations", "Simulation", "Free; runs in the browser", "Place masses on a lever to find the balance rule; use for mechanical advantage."),
 "te-wheeling": res("Wheeling It In! Design a wheel-and-axle vehicle (grade 4)", "https://www.teachengineering.org/sprinkles/view/cub_wheeling", "TeachEngineering (University of Colorado Boulder)", "Hands-on design activity", "Free; household materials", "50 minutes; wheels, axles and a carton body to carry a load.", teacher=True),
 # Grade 4: electricity, disease
 "te-goflow": res("Go with the Flow: conductors and insulators (lesson, grade 4)", "https://www.teachengineering.org/lessons/view/cub_electricity_lesson04", "TeachEngineering (University of Colorado Boulder)", "Teacher lesson + activity", "Free", "Build a conductivity tester, sort household objects, then design a simple switch.", teacher=True),
 "kh35-germs": res("Germs (Grades 3–5 teacher's guide + handouts)", "https://Classroom.KidsHealth.org/classroom/3to5/personal/hygiene/germs.pdf", "KidsHealth in the Classroom (Nemours)", "Teacher lesson + printable handouts", "Free printable PDF", "Infectious illness: how germs spread and prevention. Survey, Germ Art activity, quiz and key.", teacher=True),
 "kh35-immune": res("Immune System (Grades 3–5 teacher's guide + handouts)", "https://Classroom.KidsHealth.org/classroom/3to5/body/systems/immune.pdf", "KidsHealth in the Classroom (Nemours)", "Teacher lesson + printable handouts", "Free printable PDF", teacher=True),
 # Grade 4: Mississippi state and local government
 "bens-state": res("State Government (Ben's Guide, ages 9–13)", "https://bensguide.gpo.gov/j-state-government", "U.S. Government Publishing Office", "Article / activity", "Free"),
 "mshn-gov": res("The Government of Mississippi: How It Functions", "https://mshistory.mdah.ms.gov/issue/government-of-mississippi-how-it-functions", "Mississippi History Now (MDAH)", "Article", "Free", "Written for older students: read the branch sections together and summarize."),
 "msu-local": res("Political Process and Local Government Administration: City and County Government", "https://extension.msstate.edu/sites/default/files/publications/IS1132_web.pdf", "Mississippi State University Extension", "Teacher background reading", "Free printable PDF", "Boards of supervisors, mayors and aldermen in plain language; read aloud short sections.", teacher=True),
 # Grade 4: U.S. regions
 "natgeo-regions": res("United States Regions (maps + questions)", "https://education.nationalgeographic.org/resource/united-states-regions", "National Geographic Education", "Map / activity", "Free", "Five-region map with and without state labels, plus five questions with answers."),
}

# Independent-reading books from reading-list.json become resources too (ELA weeks of their module).
RL = json.load(open("reading-list.json"))
for g, grade in RL["grades"].items():
    for b in grade["books"]:
        R[b["id"]] = res(f"{b['title']} ({b['author']}) — independent reading", b["links"][0]["url"], "Project Gutenberg (public domain)",
                         "Ebook · 2026–27 reading list", "Free e-book (EPUB, Kindle, web)", b.get("note", ""))

weeks = {}
def add(key, subject, resources=(), teacher=(), readings=()):
    s = weeks.setdefault(key, {}).setdefault(subject, {})
    if resources: s.setdefault("resources", []).extend(resources)
    if teacher: s.setdefault("teacher_resources", []).extend(teacher)
    if readings: s.setdefault("readings", []).extend(readings)
def rd(rid, section, printed, note):
    return dict(resource_id=rid, section=section, printed=list(printed), session=0, note=note)

GL = "Grade-level reading added Oct 2026 (Core Knowledge Grade 8 science, OpenSciEd-based)."
# Grade 4 science
add("4-2-2", "science", ["germs"], ["kh35-germs", "kh35-immune"])
for k in ("4-4-2", "4-4-3", "4-4-4"): add(k, "science", ["circuit"], ["te-goflow"])
add("4-5-4", "science", ["phet-balance"], ["te-wheeling", "te-levers"])
# Grade 4 social studies
add("4-4-1", "social", ["bens-state", "mshn-gov"], ["msu-local"])
add("4-4-2", "social", ["bens-state"], ["msu-local"])
for k in ("4-6-1", "4-6-2", "4-6-3", "4-7-1", "4-7-4", "4-8-1"): add(k, "social", ["natgeo-regions", "states"])
# Grade 7 science
add("7-2-1", "science", ["ck-g6-cells-sr"], ["ck-g6-cells-tg"], [rd("ck-g6-cells-sr", "Collection 2 — Inside the Body", (14, 23), "Cells, tissues, organs and imaging; grade-level companion to this week's reader.")])
add("7-2-3", "science", ["ck-g6-cells-sr", "ck-g6-cells-swp", "kh68-bones"], ["ck-g6-cells-tg"])
add("7-2-4", "science", ["ck-g6-cells-sr", "ck-g6-cells-swp"], ["ck-g6-cells-tg"])
add("7-5-1", "science", ["ck-g8-forces-sr"], ["ck-g8-forces-tg"], [rd("ck-g8-forces-sr", "Collection 1 — Collisions", (4, 13), GL)])
add("7-5-2", "science", ["phet-balance", "ck-g8-forces-sr"], ["te-levers"], [rd("ck-g8-forces-sr", "Collection 5 — Structures and Forces", (44, 53), GL + " Pair with Levers That Lift for mechanical advantage.")])
add("7-5-3", "science", ["ck-g8-sound-sr"], ["ck-g8-sound-tg"], [rd("ck-g8-sound-sr", "Collection 4 — Compression Waves", (36, 45), GL)])
add("7-6-1", "science", ["ck-g8-space-sr"], ["ck-g8-space-tg"], [rd("ck-g8-space-sr", "Collection 1 — Sky Watching Since Days of Old", (4, 13), GL)])
add("7-6-2", "science", ["ck-g8-space-sr"], ["ck-g8-space-tg"], [rd("ck-g8-space-sr", "Around the World, Across Time (orbits and gravity timeline)", (10, 13), GL)])
add("7-6-3", "science", ["ck-g8-space-sr"], ["ck-g8-space-tg"], [rd("ck-g8-space-sr", "Collection 3 — Imaging and Imagining Space", (24, 37), GL)])
add("7-6-4", "science", ["ck-g8-space-sr"], ["ck-g8-space-tg"], [rd("ck-g8-space-sr", "Collection 2 — Reaching for the Moon", (14, 23), GL)])
# Independent reading in every ELA week of the book's module.
for g, grade in RL["grades"].items():
    for b in grade["books"]:
        for w in range(1, 5): add(f"{g}-{b['module']}-{w}", "ela", [b["id"]])

part = dict(resources=R, weeks=weeks)
json.dump(part, open("curriculum-data/assigned-resources-016.json", "w"), ensure_ascii=False, indent=1)

# Register the part in the manifest.
man = json.load(open("planner-resources.json"))
if "/curriculum-data/assigned-resources-016.json" not in man["_parts"]:
    man["_parts"].append("/curriculum-data/assigned-resources-016.json")
    json.dump(man, open("planner-resources.json", "w"))

# Fix Grade 7 week 2-3 science: the old reading was about chemical reactions.
for f in sorted(glob.glob("curriculum-data/assigned-resources-0*.json")):
    if f.endswith("016.json"): continue
    d = json.load(open(f)); s = d.get("weeks", {}).get("7-2-3", {}).get("science")
    if not s: continue
    s["readings"] = [rd("ck-g6-cells-sr", "Collection 1 — Body Parts (and Breaking Them)", (4, 13), "Skeleton, skeletal muscle and how broken bones mend."),
                     rd("ck-g6-cells-sr", "Collection 3 — Cells, Health, and Healing", (24, 33), "Nerve cells (Cell Types; Extreme Cells) and muscle cells: how signals and muscles coordinate movement.")]
    s["teacher_readings"] = []
    s["resources"] = [r for r in s.get("resources", []) if r != "saved-161"]  # chemical-reactions reader
    s["teacher_resources"] = [r for r in s.get("teacher_resources", []) if r != "saved-184"]
    json.dump(d, open(f, "w"), ensure_ascii=False, separators=(",", ":"))
    print("fixed 7-2-3 in", f)
print(len(R), "resources;", sum(len(v) for v in weeks.values()), "subject-weeks updated")
