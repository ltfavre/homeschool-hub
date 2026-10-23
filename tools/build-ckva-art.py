#!/usr/bin/env python3
"""Adds Core Knowledge Visual Arts (CKVA, free, CC BY-NC-SA) to the Art course for Grades 4 and 7.

CKVA is written as 35 class days of 45 minutes per grade. The Art course has 35 weeks with two
art days each, so the FIRST art day of every week becomes the next CKVA day, and the second art day
keeps the existing topic (studio/music/theatre/media) until a studio program is chosen.

Writes curriculum-data/assigned-resources-017.json (new resources, CKVA readings, topics) and
updates the first-art-day worksheets in daily-packets / daily-practice-keys in place. Re-runnable:
it skips days already converted. Lesson, page and supply data were read from the CKVA Teacher
Guides and Student Activity Books on 2026-10-23."""
import glob, json, re

CK = "https://www.coreknowledge.org/wp-content/uploads/"
FILES = {
 "4": dict(tg=CK + "2025/11/CKVA_G4_TG_W2.pdf", sab=CK + "2025/11/CKVA_G4_SAB_W1.pdf", org=CK + "2025/11/CKVA_G4_ORG_W2.pdf",
           slides=CK + "2025/11/CKVA_G4_SlideDeck_W1.pptx", page="https://www.coreknowledge.org/free-resource/ck-visual-arts-grade-4/"),
 "7": dict(tg=CK + "2026/02/CKVA_G7_TG_W1.pdf", sab=CK + "2026/02/CKVA_G7_SAB_W1.pdf", org=CK + "2026/02/CKVA_G7_ORG_W1.pdf",
           slides=CK + "2026/02/CKVA_G7_SlideDeck_W1.pptx", page="https://www.coreknowledge.org/free-resource/ck-visual-arts-grade-7/"),
}
SAB_OFFSET = 6  # Student Activity Book: PDF page = printed page + 6 (both grades)
TG_OFFSET = {"4": 8, "7": 8}  # Teacher Guide: printed page = PDF page - 8

UNITS = {
 "4": {1: "Middle Ages in Europe", 2: "Islamic Art and Architecture", 3: "The Art of Africa", 4: "The Art of China", 5: "Early United States", "C": "Year in Review"},
 "7": {1: "Expressionism", 2: "Cubism", 3: "Surrealism", 4: "Abstract Expressionism", 5: "Abstraction", 6: "Twentieth-Century Architecture", "C": "Year in Review"},
}

# (unit, lesson, title, day, of, TG pdf page, what students do, SAB printed pages, artworks, supplies, objective)
D4 = [
 (1,1,"Introduction to Art of the Middle Ages in Europe",1,1,17,"Explore and summarize the defining features of art in the European Middle Ages",[3,4],[],[],"Summarize defining features and themes of art of the European Middle Ages."),
 (1,2,"The Madonna and Child in Medieval Art",1,1,20,"Learn about the Madonna as a main subject in medieval artwork",[5],["Madonna and Child on a Curved Throne"],[],"Analyze the style and symbolism of the Madonna in medieval artwork."),
 (1,3,"Illuminated Manuscripts",1,1,23,"Create an original two-page illuminated manuscript based on your initials",[6],["Chi Rho Page from the Book of Kells"],["markers or colored pencils (including gold)","white paper (2 sheets)","eraser","black ink pen (optional)"],"Describe the features and purposes of illuminated manuscripts."),
 (1,4,"Tapestries",1,1,26,"Learn how medieval tapestries were designed and used, then build a cardboard loom",[7],["The Unicorn in Captivity (Tapestry)"],["drawing paper","cardboard 8 x 12 in","ruler","scissors","tape","yarn (about 10 ft)"],"Identify the artistic, decorative and practical purposes of medieval tapestries."),
 (1,5,"Creating Art of the Middle Ages",1,1,30,"Review medieval art and create artwork that represents the Middle Ages",[8],[],["sketch paper","drawing paper","pencil and eraser","markers, colored pencils or watercolors"],"Represent the characteristics of medieval art in an original artwork."),
 (1,6,"Gothic Architecture",1,2,32,"Learn the elements of Gothic architecture",[9],["Notre Dame Cathedral"],["writing paper","pencil"],"Describe the features of Gothic architecture and explain their purpose."),
 (1,6,"Gothic Architecture",2,2,32,"Learn about gargoyles and sculpt your own gargoyle from clay",[10],[],["air-dry clay","sculpting tools (plastic knife, toothpicks)","small bowl of water","washable work surface"],"Describe the features of Gothic architecture and explain their purpose."),
 (1,7,"Unit 1 Assessment",1,1,37,"Make a rose window to show what you learned in Unit 1",[11],[],["black construction paper","white chalk","scissors","colored tissue paper or cellophane","glue stick"],"Show understanding of medieval art through a performance task."),
 (2,1,"Characteristics of Islamic Art",1,1,46,"Match pictures to the element of Islamic art they show",[12],[],[],"Recognize elements of religious and secular Islamic art."),
 (2,2,"Patterns and Illumination",1,2,48,"Create artwork from repeating geometric patterns",[13],["Illumination of the Qur'an"],["graph paper","ruler","pencil and eraser","colored pencils or markers"],"Analyze how and why geometric patterns were used in Islamic art."),
 (2,2,"Patterns and Illumination",2,2,48,"Complete your repeating geometric pattern artwork",[13],[],["graph paper","ruler","colored pencils or markers"],"Analyze how and why geometric patterns were used in Islamic art."),
 (2,3,"Intersection of Art and Architecture",1,2,52,"Identify elements of Islamic architecture",[14],["Court of the Lions","Dome of the Rock"],[],"Identify the structural and decorative features of Islamic architecture."),
 (2,3,"Intersection of Art and Architecture",2,2,52,"Design architectural plans for an Islamic building or monument",[15],["Taj Mahal"],["sketch paper (2 sheets)","pencil and eraser","ruler"],"Identify the structural and decorative features of Islamic architecture."),
 (2,4,"Unit 2 Assessment",1,1,58,"Answer questions about the Taj Mahal to review Unit 2",[16],["Taj Mahal"],["pencil"],"Show understanding of Islamic art and architecture."),
 (3,1,"Introduction to Art of Africa",1,1,64,"Learn that African art has practical and traditional purposes",[17],[],[],"Compare the purposes and functions of African art with art of other cultures."),
 (3,2,"Portraying Leaders",1,2,66,"Examine sculpted portrait heads that represent African leaders",[18],["Benin Bronze Head","Portrait Head of an Ife King"],[],"Analyze how leaders are portrayed in traditional African art."),
 (3,2,"Portraying Leaders",2,2,66,"Create a royal self-portrait that communicates a personal message",[19],[],["drawing paper","pencil and eraser","markers, colored pencils or watercolors"],"Analyze how leaders are portrayed in traditional African art."),
 (3,3,"Masks: Carvings and Sculptures",1,2,71,"Learn about African carvings, masks and headdresses",[],["Face Mask","Bamana Antelope Headdress of Mali"],[],"Analyze the form and function of traditional African masks and headdresses."),
 (3,3,"Masks: Carvings and Sculptures",2,2,71,"Create an animal mask inspired by traditional African art",[20],[],["construction paper","glue","clear tape","scissors","craft stick","natural decorations (feathers, leaves, seeds)"],"Analyze the form and function of traditional African masks and headdresses."),
 (3,4,"Contemporary and Ancient Connections",1,1,76,"Create a collage inspired by contemporary African collage artists",[21],[],["heavy drawing paper","magazines","scissors","glue","paints or markers (optional)"],"Compare contemporary African art with traditional African art."),
 (3,5,"Unit 3 Assessment",1,1,79,"Create a painting that shows characteristics of African art",[22],[],["canvas panel or heavy paper","acrylic paints","brushes and palette","cup of water","paper towels"],"Show understanding of the art of Africa."),
 (4,1,"Introduction to Art of China",1,1,85,"Read and answer questions about the Chinese invention of silk and paper",[23],[],[],"Identify Chinese artistic inventions and the art forms Chinese artists excelled in."),
 (4,2,"Calligraphy",1,1,87,"Practice writing Chinese calligraphy",[24],["Calligraphy"],["heavy drawing or watercolor paper","black calligraphy pen, marker, or pointed brush with black paint"],"Identify the purpose and techniques of traditional Chinese calligraphy."),
 (4,3,"Landscapes",1,2,91,"Reflect on the artistic qualities of a silk scroll painting",[25],["Lonely Retreat Overlooking a Misty Valley (Silk Scroll)"],[],"Describe how traditional Chinese artists painted landscapes on scrolls."),
 (4,3,"Landscapes",2,2,91,"Paint a landscape inspired by traditional Chinese art",[26],[],["watercolor paper","watercolor paints","brushes","cup of water","paper towels"],"Describe how traditional Chinese artists painted landscapes on scrolls."),
 (4,4,"Pottery",1,1,96,"Sculpt a vase or bowl from clay",[27],["Ming Dynasty Vase"],["air-dry porcelain clay (3-5 lb)","sculpting tools","rolling pin","cup of water","washable work surface"],"Identify the key features of traditional Chinese porcelain."),
 (4,5,"Unit 4 Assessment",1,1,99,"Paint your clay pottery with traditional Chinese imagery",[28],[],["your clay pot from last lesson","blue ceramic or acrylic paint","paintbrush","cup of water","paper towels"],"Show understanding of the art of China."),
 (5,1,"Introduction to Art and Architecture of a New Nation",1,1,106,"Read and answer questions about early American portraits",[29],["Paul Revere (John Singleton Copley)"],[],"Analyze the purpose of portraiture in colonial America."),
 (5,2,"History Through an Artist's Lens",1,1,109,"Analyze the painting Washington Crossing the Delaware",[30],["Washington Crossing the Delaware (Emanuel Leutze)"],["colored pencils"],"Analyze the purpose of history painting after the American Revolution."),
 (5,3,"Portrait of a Leader",1,2,113,"Analyze portraits of national heroes",[],["George Washington (Gilbert Stuart)","Profile Bust of Benjamin Franklin (Patience Wright)"],[],"Analyze portraits of national heroes from the colonial and revolutionary periods."),
 (5,3,"Portrait of a Leader",2,2,113,"Draw a portrait of an inspiring early American leader",[31],[],["drawing paper","pencil and eraser","colored pencils"],"Analyze portraits of national heroes from the colonial and revolutionary periods."),
 (5,4,"Architecture to Represent Us",1,1,117,"Design your own neoclassical building after learning about Monticello",[32],["Monticello (Thomas Jefferson)"],["sketch paper","drawing paper","pencil and eraser","colored pencils"],"Recognize the features of American neoclassical architecture."),
 (5,5,"Unit 5 Assessment",1,1,120,"Reflect on architectural designs and review Unit 5",[33],[],["pencil"],"Show understanding of early American art and architecture."),
 ("C",1,"Culminating Activity: A Year in Review",1,2,123,"Make a year-in-review booklet about the art you studied",[34],["Madonna and Child on a Curved Throne","Illumination of the Qur'an","Portrait Head of an Ife King","Washington Crossing the Delaware"],["blank booklet (folded paper)","markers or colored pencils","pencil and eraser"],"Summarize the features and purposes of the art studied this year."),
 ("C",1,"Culminating Activity: Gallery Show",2,2,123,"Set up a gallery of your artwork from the year and present it to the family",[],[],["your artwork from the year"],"Present and explain your own artwork to an audience."),
]
D7 = [
 (1,1,"What Is Expressionism?",1,1,16,"Explore expressionist art and create an expressionist sketch",[2,3],["The Scream (Edvard Munch)"],["heavy paper","pencil","kneaded and vinyl erasers","oil pastels"],"Learn the characteristics of the expressionist movement."),
 (1,2,"Fauvism",1,2,20,"Explore fauvism and begin a fauvist painting",[4,5],["The Dessert: Harmony in Red (Henri Matisse)"],["heavy paper","pencil and erasers","tempera or acrylic paints","brush, palette, cup of water"],"Learn the characteristics of fauvism."),
 (1,2,"Fauvism",2,2,20,"Compare impressionist and fauvist art and finish your fauvist painting",[5],[],["your painting from Day 1","charcoal pencil","paints, brush, palette, water"],"Learn the characteristics of fauvism."),
 (1,3,"Unit 1 Assessment",1,1,25,"Review Unit 1 and analyze another expressionist work (Indian Church)",[6],["Indian Church (Emily Carr)"],[],"Show understanding of expressionism and fauvism."),
 (2,1,"What Is Cubism?",1,1,31,"Learn the features of cubism and examine key works",[7],["Le verre sur la table (Georges Braque)"],[],"Learn the features of cubism."),
 (2,2,"Depicting a Scene",1,2,35,"Study Picasso's Guernica and draw a realistic scene in colored pencil",[8],["Guernica (Pablo Picasso)"],["drawing paper","pencil","colored pencils"],"Explore Guernica and create a cubist work."),
 (2,2,"Depicting a Scene",2,2,35,"Re-create your realistic scene in a cubist style",[9],[],["drawing paper","scrap paper (4 sheets)","erasers","scissors","glue"],"Explore Guernica and create a cubist work."),
 (2,3,"Unit 2 Assessment",1,1,39,"Review Unit 2 and analyze Nude Descending a Staircase (No. 2)",[10],["Le verre sur la table","Guernica"],[],"Show understanding of cubism."),
 (3,1,"What Is Surrealism?",1,1,45,"Learn the features of surrealism and draw like a surrealist",[11],["The Persistence of Memory (Salvador Dali)"],["drawing paper","pencil and vinyl eraser","colored pencils"],"Learn the features of surrealism."),
 (3,2,"Portraits",1,1,49,"Study surrealist portraits and make your own surrealist portrait",[12,13],["Creation of the Birds (Remedios Varo)","Self-Portrait (Leonora Carrington)"],["heavy paper","pencil and eraser","colored pencils","watercolors (optional)"],"Learn surrealist self-portraiture."),
 (3,3,"Max Ernst and Surrealist Techniques",1,2,52,"Explore Max Ernst's techniques and start a surrealist collage",[14],["The Forest (Max Ernst)"],["heavy drawing paper","newspapers and magazines","construction paper","scissors"],"Learn Max Ernst's techniques (collage, frottage, grattage)."),
 (3,3,"Max Ernst and Surrealist Techniques",2,2,52,"Finish your surrealist collage",[14],[],["your collage from Day 1","glue"],"Learn Max Ernst's techniques (collage, frottage, grattage)."),
 (3,4,"Unit 3 Assessment",1,1,55,"Present your collage and explain the surrealist techniques you used",[15],[],[],"Show understanding of surrealism."),
 (4,1,"What Is Abstract Expressionism?",1,1,61,"Explore the features of abstract expressionism and analyze a Pollock painting",[16],["Number 28, 1950 (Jackson Pollock)"],[],"Learn the features of abstract expressionism."),
 (4,2,"Drip Painting",1,1,65,"Make a drip painting in the style of Jackson Pollock",[17],[],["large heavy craft paper (24 in+)","acrylic paints","brushes, spoons, squeeze bottles","newspaper or drop cloth (work outside if possible)"],"Learn the technique of drip painting."),
 (4,3,"A Study in Texture",1,1,67,"Explore texture and create a thickly painted textured work",[18,19],["Night Light (Lee Krasner)"],["small canvas or heavy paper","acrylic paints","brush","palette knife (optional)"],"Learn how abstract expressionists used texture."),
 (4,4,"A Study in Color",1,1,70,"Explore color fields and create an abstract color painting",[20,21],["No. 9 (Mark Rothko)","John F. Kennedy (Elaine de Kooning)"],["heavy paper","acrylic paints","brushes"],"Learn how abstract expressionists used color."),
 (4,5,"Unit 4 Assessment",1,1,73,"Create an abstract work using the techniques from Unit 4",[22],[],["heavy paper or small canvas","acrylic paints","brushes"],"Show understanding of abstract expressionism."),
 (5,1,"What Is Abstraction?",1,1,79,"Explore abstraction through Mondrian and Kandinsky",[23],["Broadway Boogie Woogie (Piet Mondrian)","Points (Wassily Kandinsky)"],[],"Learn the characteristics of abstraction."),
 (5,2,"Create Abstract Style",1,2,83,"Paint an abstract work in the style of Mondrian or Kandinsky",[24],[],["heavy paper","pencil","markers","watercolors and brush"],"Create two scenes in the abstract style."),
 (5,2,"Create Abstract Style",2,2,83,"Paint a second abstract work with different materials",[25],[],["heavy paper","pencil","acrylic paints and brush"],"Create two scenes in the abstract style."),
 (5,3,"Abstract Portraiture",1,2,85,"Study abstract portraits by Klee and Lois Mailou Jones",[26],["Senecio (Paul Klee)","Les fetiches (Lois Mailou Jones)"],[],"Learn about abstract portraiture."),
 (5,3,"Abstract Portraiture",2,2,85,"Create an abstract portrait and compare it with your surrealist portrait",[27,28],[],["heavy paper","pencil","paints or markers"],"Learn about abstract portraiture."),
 (5,4,"Abstraction in Nature",1,2,89,"Explore abstraction in nature paintings (O'Keeffe and others)",[29],[],[],"Learn about abstraction in nature."),
 (5,4,"Abstraction in Nature",2,2,89,"Create an abstract nature scene",[30],[],["heavy paper","pencil","markers","watercolors and brush"],"Learn about abstraction in nature."),
 (5,5,"The Gutai Group",1,3,92,"Explore the Gutai Group's work and mission",[31],[],[],"Learn about the Gutai Group."),
 (5,5,"The Gutai Group",2,3,92,"Create artwork using Gutai principles",[32],[],["large heavy craft paper","acrylic paints","sponges or found tools","newspaper or drop cloth"],"Learn about the Gutai Group."),
 (5,5,"The Gutai Group",3,3,92,"Hold a gallery walk and compare your work with the Gutai Group",[33],[],[],"Learn about the Gutai Group."),
 (5,6,"Unit 5 Assessment",1,1,95,"Compare and contrast art from Unit 5",[34],[],[],"Show understanding of abstraction."),
 (6,1,"What Is Organic Architecture?",1,1,101,"Learn the features of organic architecture through four famous buildings",[35,36],["Tassel House (Victor Horta)","Guaranty Building (Sullivan and Adler)","Darwin Martin House (Frank Lloyd Wright)","Casa Batllo (Antoni Gaudi)"],[],"Learn the characteristics of organic architecture."),
 (6,2,"Architectural Design",1,2,106,"Design a building using organic architecture",[37],[],["paper or 1-inch graph paper","pencil, ruler, eraser"],"Design and model a building using organic architecture."),
 (6,2,"Architectural Design",2,2,106,"Build a cardboard model of your design",[38],[],["cardboard","construction paper","markers","scissors","masking tape"],"Design and model a building using organic architecture."),
 (6,3,"Unit 6 Assessment",1,1,109,"Review twentieth-century architecture",[39],[],[],"Show understanding of organic architecture."),
 ("C",1,"Culminating Activity: Reflection",1,2,112,"Reflect on each movement you studied this year",[40],[],[],"Summarize the art movements studied this year."),
 ("C",1,"Culminating Activity: Put It All Together",2,2,112,"Create a new work in one of the styles you studied",[41],[],["large paper","construction paper","markers","glue, tape, scissors","paints (optional)"],"Create a new work in a studied style and explain it."),
]
DAYS = {"4": D4, "7": D7}
assert len(D4) == 35 and len(D7) == 35

def merge(t, s):
    for k, v in s.items():
        if isinstance(v, list): t[k] = t.get(k, []) + v
        elif isinstance(v, dict): t[k] = merge(t.get(k, {}), v)
        else: t[k] = v
    return t
def load(name):
    d = json.load(open(name)); r = {}
    for p in d["_parts"]: merge(r, json.load(open("." + p)))
    return r

def rng(a): return f"{a[0]}" if len(a) == 1 or a[0] == a[-1] else f"{a[0]}-{a[-1]}"

daily = load("daily-packets.json")
weeks_order = {}  # grade -> list of (module, week, [dates])
for date in sorted(daily):
    for g in "47":
        r = daily[date].get(g)
        if r and "art" in (r.get("subjects") or []):
            lst = weeks_order.setdefault(g, [])
            if not lst or lst[-1][:2] != (r["module"], r["week"]): lst.append((r["module"], r["week"], []))
            lst[-1][2].append(date)
for g in "47":
    assert len(weeks_order[g]) == 35 and all(len(w[2]) == 2 for w in weeks_order[g]), "Art must be 35 weeks x 2 days"

REV = dict(reviewed="2026-10-23", review="Teacher Guide and Student Activity Book read page by page 2026-10-23")
resources, weeks, first_days = {}, {}, {}
for g in "47":
    f = FILES[g]
    resources[f"ckva{g}-sab"] = dict(title=f"Core Knowledge Visual Arts Grade {g} - Student Activity Book", url=f["sab"], provider="Core Knowledge Foundation", kind="Printable workbook", access="Free printable PDF (CC BY-NC-SA)", note="Print the pages listed for each lesson; the color art prints are at the back.", teacher_only=False, **REV)
    resources[f"ckva{g}-org"] = dict(title=f"Core Knowledge Visual Arts Grade {g} - Online Resources (virtual tours and extra art)", url=f["org"], provider="Core Knowledge Foundation", kind="Lesson / reading collection", access="Free", note="", teacher_only=False, **REV)
    resources[f"ckva{g}-tg"] = dict(title=f"Core Knowledge Visual Arts Grade {g} - Teacher Guide", url=f["tg"], provider="Core Knowledge Foundation", kind="Teacher guide", access="Free printable PDF (CC BY-NC-SA)", note="35 class days of 45 minutes; scripted discussion questions and answer key.", teacher_only=True, **REV)
    resources[f"ckva{g}-slides"] = dict(title=f"Core Knowledge Visual Arts Grade {g} - Slide Deck (artwork images)", url=f["slides"], provider="Core Knowledge Foundation", kind="Slide deck", access="Free PowerPoint", note="Show the artwork slide named in each lesson on a screen.", teacher_only=True, **REV)
    for i, (mod, wk, dates) in enumerate(weeks_order[g]):
        u, l, title, day, of, tgp, what, sab, art, sup, obj = DAYS[g][i]
        unit = UNITS[g][u]
        label = f"CKVA Day {i+1}: {title}" + (f" (day {day} of {of})" if of > 1 else "")
        key = f"{g}-{mod}-{wk}"
        first_days[(g, dates[0])] = (i, label, unit, DAYS[g][i])
        s = weeks.setdefault(key, {}).setdefault("art", {})
        s["resources"] = [f"ckva{g}-sab", f"ckva{g}-org"]
        s["teacher_resources"] = [f"ckva{g}-tg", f"ckva{g}-slides"]
        note = f"{what}." + (f" Artwork: {', '.join(art)}." if art else "") + (f" Supplies: {', '.join(sup)}." if sup else "")
        s["readings"] = ([dict(resource_id=f"ckva{g}-sab", section=f"{label} - Student Activity Book", pdf=[sab[0] + SAB_OFFSET, sab[-1] + SAB_OFFSET], printed=[sab[0], sab[-1]], session=1, note=note)] if sab else
                         [dict(resource_id=f"ckva{g}-org", section=f"{label} - view the artwork online", session=1, note=note)])
        s["teacher_readings"] = [dict(resource_id=f"ckva{g}-tg", section=f"{label} ({unit})", pdf=[tgp, tgp + 2], printed=[tgp - TG_OFFSET[g], tgp - TG_OFFSET[g] + 2], session=1, note=f"Objective: {obj}")]
        s["ckva"] = dict(day=i + 1, unit=unit, lesson=title, of=of, part=day)

json.dump(dict(resources=resources, weeks=weeks), open("curriculum-data/assigned-resources-017.json", "w"), ensure_ascii=False, indent=1)
man = json.load(open("planner-resources.json"))
if "/curriculum-data/assigned-resources-017.json" not in man["_parts"]:
    man["_parts"].append("/curriculum-data/assigned-resources-017.json"); json.dump(man, open("planner-resources.json", "w"))

# Existing Art readings move to the second art day (session 2); topics name both days.
changed = 0
for f in sorted(glob.glob("curriculum-data/assigned-resources-0*.json")):
    if f.endswith(("016.json", "017.json")): continue
    d = json.load(open(f)); touched = False
    for key, w in d.get("weeks", {}).items():
        a = w.get("art")
        if not a or not key[0] in "47": continue
        for r in a.get("readings", []) + a.get("teacher_readings", []):
            if r.get("session", 0) == 0: r["session"] = 2; touched = True
        ck = weeks.get(key, {}).get("art", {}).get("ckva")
        if ck and "topic" in a and not a["topic"].startswith("CK Art"):
            a["topic"] = f"CK Art: {ck['lesson']} · Studio: {a['topic']}"; touched = True
    if touched: json.dump(d, open(f, "w"), ensure_ascii=False, separators=(",", ":")); changed += 1

# First art day of each week: new task text and worksheet; teacher key gets look-fors.
def practice(i, label, unit, row, keys):
    u, l, title, day, of, tgp, what, sab, art, sup, obj = row
    look = "Look for accurate use of the lesson's vocabulary, specific details from the artwork, and a reason for each choice. Accept varied, well-supported answers; do not grade artistic talent."
    items = [
        dict(prompt=(f"Look closely at {art[0]}. Describe three details you notice (color, line, shape, subject) and what you think they mean." if art else f"In your own words, what is today's big idea about {unit}? Give one example from the lesson."), points=3, lines=4),
        dict(prompt=f"{what}." + (f" Use Student Activity Book p. {rng(sab)}." if sab else "") + (" Then write 2-3 sentences explaining one artistic choice you made." if sup else " Then write 2-3 sentences about the most interesting thing you learned."), points=4, lines=5),
    ]
    if keys:
        items[0]["answer"] = look; items[1]["answer"] = f"Objective: {obj} " + look
    return dict(title="Art", passage_title=f"Core Knowledge Visual Arts · {unit}", passage=f"{label}. Today's goal: {obj}" + (f" Supplies: {', '.join(sup)}." if sup else ""), items=items)

converted = 0
for kind in ("daily-packets", "daily-practice-keys"):
    for f in sorted(glob.glob(f"curriculum-data/{kind}-0*.json")):
        d = json.load(open(f)); touched = False
        for date, grades in d.items():
            for g, r in grades.items():
                hit = first_days.get((g, date))
                if not hit or "Core Knowledge Visual Arts" in r.get("tasks", ""): continue
                i, label, unit, row = hit
                u, l, title, day, of, tgp, what, sab, art, sup, obj = row
                task = f"Art: {label} ({unit}) — Core Knowledge Visual Arts. {what}." + (f" Student Activity Book p. {rng(sab)}." if sab else "") + (f" Supplies: {', '.join(sup)}." if sup else "")
                r["tasks"] = re.sub(r"Art: .*?(?= (?:Life|CS|Skills|Friday):|$)", lambda m: task, r["tasks"], count=1)
                r["goals"] = re.sub(r"Art: [^;]*", f"Art: {title} (CK Visual Arts)", r.get("goals", ""), count=1)
                r["practice"] = [practice(i, label, unit, row, kind == "daily-practice-keys") if p.get("title") == "Art" else p for p in r.get("practice", [])]
                touched = True; converted += 1
        if touched: json.dump(d, open(f, "w"), ensure_ascii=False, separators=(",", ":"))
# The second art day now carries the whole studio topic, so it starts with the reading.
for kind in ("daily-packets", "daily-practice-keys"):
    for f in sorted(glob.glob(f"curriculum-data/{kind}-0*.json")):
        d = json.load(open(f)); touched = False
        for date, grades in d.items():
            for g, r in grades.items():
                t = r.get("tasks", "")
                if "Art: " in t and "Revisit the chapter, complete the application" in t and (g, date) not in first_days:
                    r["tasks"] = t.replace("Revisit the chapter, complete the application", "Read the chapter with your parent, try the guided example, complete the application"); touched = True
        if touched: json.dump(d, open(f, "w"), ensure_ascii=False, separators=(",", ":"))
print(f"{len(resources)} resources; {len(weeks)} art weeks; {changed} plan files updated; {converted} first-art-day packets/keys converted")
