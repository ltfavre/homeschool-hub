"""Builds the Grade 4 and Grade 7 ELA Readers: one book per grade holding every story the ELA lessons read.

    python3 readers/build_readers.py SOURCE_DIR

SOURCE_DIR holds the Core Knowledge Readers (Creative Commons BY-NC-SA) downloaded from coreknowledge.org:
    venv-CKLA_G4U8_Treasure_Island_Reader.pdf, venv-CC_TheTempest_Reader.pdf,
    venv-CC_StrangeCaseOfDrJekyllAndMrHyde_Reader.pdf, venv-CC_TheTimeMachine_Reader.pdf
King Arthur (Grade 4) and the Harlem Renaissance anthology (Grade 7) are VenvLearning's own (readers/arthur_*.py, readers/harlem.py).

Writes downloads/textbooks/grade{4,7}-ela-reader.pdf and grade{4,7}-ela-reader.index.json. The index maps every Reader
assignment in the ELA lessons to its part, printed pages, and PDF pages. Each part keeps its own page numbers."""
import io, json, os, re, subprocess, sys, collections
from xml.sax.saxutils import escape
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, ROOT)
import pikepdf
from PIL import Image
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas as _canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Flowable
import engine
from engine import PAGE_W, PAGE_H, SUBJECTS, IVORY, INK, GOLD, MUTED, LINE, WHITE, Book, text
import covers

ELA = SUBJECTS["ela"]; MAIN, DARK, WASH, MID = ELA["main"], ELA["dark"], ELA["wash"], ELA["mid"]
OUT = os.path.join(ROOT, "..", "downloads", "textbooks")
M = 0.85 * inch

S = dict(
    eyebrow=ParagraphStyle("eb", fontName="BodyBold", fontSize=9, leading=12, textColor=MAIN, spaceAfter=4),
    h1=ParagraphStyle("h1", fontName="Display", fontSize=30, leading=34, textColor=DARK, spaceAfter=6),
    h2=ParagraphStyle("h2", fontName="Display", fontSize=19, leading=23, textColor=DARK, spaceBefore=14, spaceAfter=2),
    by=ParagraphStyle("by", fontName="BodyMed", fontSize=10, leading=14, textColor=MUTED, spaceAfter=10),
    body4=ParagraphStyle("b4", fontName="Body", fontSize=13.5, leading=21, textColor=INK, spaceAfter=9, firstLineIndent=18),
    body7=ParagraphStyle("b7", fontName="Body", fontSize=11.5, leading=17, textColor=INK, spaceAfter=8, firstLineIndent=16),
    sign=ParagraphStyle("sg", fontName="BodySemi", fontSize=13.5, leading=19, textColor=DARK, spaceAfter=10, spaceBefore=4, alignment=TA_CENTER),
    poem=ParagraphStyle("pm", fontName="Body", fontSize=11.5, leading=16.5, textColor=INK, leftIndent=36, firstLineIndent=-18),
    small=ParagraphStyle("sm", fontName="Body", fontSize=10, leading=14, textColor=INK, spaceAfter=6),
    wordh=ParagraphStyle("wh", fontName="BodyBold", fontSize=9, leading=12, textColor=MAIN),
    word=ParagraphStyle("wd", fontName="Body", fontSize=10.5, leading=14, textColor=INK),
    toc=ParagraphStyle("tc", fontName="Body", fontSize=11, leading=15, textColor=INK),
)


class Rule(Flowable):
    def __init__(self, w=54, color=GOLD, h=2.5): super().__init__(); self.w, self.color, self.h = w, color, h
    def wrap(self, *a): return self.w, self.h + 8
    def draw(self): self.canv.setFillColor(self.color); self.canv.rect(0, 4, self.w, self.h, fill=1, stroke=0)


class Mark(Flowable):
    """Zero-size marker that records the page it lands on."""
    def __init__(self, key, log): super().__init__(); self.key, self.log = key, log
    def wrap(self, *a): return 0, 0
    def draw(self): self.log.setdefault(self.key, self.canv.getPageNumber())


def words_box(words, width):
    rows = [[Paragraph("WORDS TO KNOW", S["wordh"]), ""]] + [[Paragraph(f"<b>{escape(w)}</b>", S["word"]), Paragraph(escape(d), S["word"])] for w, d in words]
    t = Table(rows, colWidths=[1.6 * inch, width - 1.6 * inch])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), WASH), ("SPAN", (0, 0), (1, 0)), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, 0), 9), ("BOTTOMPADDING", (0, -1), (-1, -1), 9),
                           ("LINEBEFORE", (0, 0), (0, -1), 4, MAIN)]))
    return t


def part_doc(path, running, story):
    """A part of the Reader on letter pages with its own page numbers and a running head."""
    def page(c, d):
        c.saveState(); c.setFillColor(IVORY); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        n = c.getPageNumber()
        if n > 1:
            text(c, M, PAGE_H - 0.55 * inch, running.upper(), "BodySemi", 8, MAIN)
            c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, PAGE_H - 0.64 * inch, PAGE_W - M, PAGE_H - 0.64 * inch)
        text(c, PAGE_W / 2, 0.5 * inch, str(n), "BodySemi", 10, DARK, "c")
        c.restoreState()
    doc = BaseDocTemplate(path, pagesize=(PAGE_W, PAGE_H), leftMargin=M, rightMargin=M, topMargin=0.95 * inch, bottomMargin=0.85 * inch,
                          title=running, author="VenvLearning")
    doc.addPageTemplates([PageTemplate("p", [Frame(M, 0.85 * inch, PAGE_W - 2 * M, PAGE_H - 1.8 * inch, id="f")], onPage=page)])
    doc.build(story)


def build_arthur(path):
    from readers.arthur_a import CHAPTERS
    import readers.arthur_b, readers.arthur_c, readers.arthur_d   # noqa: F401 (they append chapters 7-22)
    log, story, W = {}, [], PAGE_W - 2 * M
    for i, c in enumerate(CHAPTERS, 1):
        if i > 1: story.append(PageBreak())
        story += [Mark(i, log), Spacer(1, 30), Paragraph(f"CHAPTER {i}", S["eyebrow"]), Paragraph(escape(c["title"]), S["h1"]), Rule(), Spacer(1, 10),
                  words_box(c["words"], W), Spacer(1, 16)]
        for p in c["paras"]:
            st = S["sign"] if p.isupper() else S["body4"]
            story.append(Paragraph(escape(p), st))
    story += [PageBreak(), Mark("end", log), Spacer(1, 40), Paragraph("ABOUT THIS RETELLING", S["eyebrow"]), Rule(), Spacer(1, 6)] + [Paragraph(escape(p), S["small"]) for p in [
        "The legends of King Arthur were told and retold for hundreds of years in Britain and France. The most famous early collection is "
        "Le Morte d'Arthur (The Death of Arthur), written by Sir Thomas Malory and printed in 1485. Later writers, including Sidney Lanier, "
        "Howard Pyle, and Mary Macgregor, retold the stories for young readers.",
        "This VenvLearning retelling follows Malory's version of the legends, chapter by chapter, in language written for fourth-grade readers. "
        "Some events have been simplified or told gently. Names follow the older spellings (Guenevere, Gawaine) used in many classic retellings; "
        "you may also see Guinevere and Gawain in other books.",
        "Want to read more? Stories of King Arthur's Knights, Told to the Children by Mary Macgregor (1905) and The Boy's King Arthur by "
        "Sidney Lanier (1880) are free to read on Project Gutenberg."]]
    part_doc(path, "King Arthur and the Round Table", story)
    return log


def build_harlem(path):
    from readers.harlem import SECTIONS
    log, story, W = {}, [], PAGE_W - 2 * M
    for i, s in enumerate(SECTIONS, 1):
        if i > 1: story.append(PageBreak())
        story += [Mark(s["title"], log), Spacer(1, 18), Paragraph(f"SECTION {i}", S["eyebrow"]), Paragraph(escape(s["title"]), S["h1"]), Rule(), Spacer(1, 8)]
        if s["words"]: story += [words_box(s["words"], W), Spacer(1, 12)]
        story += [Paragraph(escape(p), S["body7"]) for p in s["paras"]]
        for x in s["selections"]:
            head = [Spacer(1, 6), Paragraph("EXCERPT" if x["kind"] == "prose" else "POEM", S["eyebrow"]), Paragraph(escape(x["title"]), S["h2"]),
                    Paragraph(f"{escape(x['author'])}  ·  {escape(x['source'])}", S["by"])]
            if x["kind"] == "poem":
                lines = []
                for ln in x["text"].split("\n"):
                    if not ln.strip(): lines.append(Spacer(1, 8)); continue
                    lead = len(ln) - len(ln.lstrip(" "))
                    lines.append(Paragraph("&nbsp;" * (lead * 3) + escape(ln.strip()), S["poem"]))
                story.append(KeepTogether(head + lines[:6])); story += lines[6:]
            else:
                story.append(KeepTogether(head + [Paragraph(escape(x["paras"][0]), S["body7"])]))
                story += [Paragraph(escape(p), S["body7"]) for p in x["paras"][1:]]
    story += [PageBreak(), Mark("end", log), Spacer(1, 30), Paragraph("SOURCES", S["eyebrow"]), Rule(), Spacer(1, 6)] + [Paragraph(escape(p), S["small"]) for p in [
        "The background sections in this anthology were written for VenvLearning. Every poem and essay excerpt was first published in 1930 or earlier "
        "and is in the public domain in the United States. The texts follow the first book editions as transcribed on Wikisource "
        "(en.wikisource.org): Paul Laurence Dunbar, Lyrics of Lowly Life (1896) and Lyrics of the Hearthside (1899); Claude McKay, Harlem Shadows (1922); "
        "Georgia Douglas Johnson, The Heart of a Woman (1918) and Bronze (1922); Langston Hughes, The Weary Blues (1926); Countee Cullen, Color (1925); "
        "Alain Locke, ed., The New Negro (1925), for the essays by Alain Locke and Arthur A. Schomburg.",
        "Excerpts are marked. Spelling and punctuation follow the original editions, including period spellings and dialect.",
        "To read more, The Genius of the Harlem Renaissance Reader from the Core Knowledge Foundation is free at coreknowledge.org, and the "
        "Schomburg Center for Research in Black Culture (New York Public Library) has extensive free online exhibits."]]
    part_doc(path, "Voices of the Harlem Renaissance", story)
    return log


# ------------------------------------------------------------------ Core Knowledge parts
CK = {
    "treasure": dict(file="venv-CKLA_G4U8_Treasure_Island_Reader.pdf", title="Treasure Island", author="Robert Louis Stevenson",
                     source="Core Knowledge Language Arts, Grade 4, Unit 8: Treasure Island Reader", license="CC BY-NC-SA 3.0",
                     license_url="https://creativecommons.org/licenses/by-nc-sa/3.0/", year="Core Knowledge Foundation"),
    "tempest": dict(file="venv-CC_TheTempest_Reader.pdf", title="The Tempest", author="William Shakespeare",
                    source="Core Classics: The Tempest Reader (Core Knowledge Language Arts, Grade 7, Unit 2)", license="CC BY-NC-SA 4.0",
                    license_url="https://creativecommons.org/licenses/by-nc-sa/4.0/", year="Core Knowledge Foundation"),
    "jekyll": dict(file="venv-CC_StrangeCaseOfDrJekyllAndMrHyde_Reader.pdf", title="Strange Case of Dr. Jekyll and Mr. Hyde", author="Robert Louis Stevenson",
                   source="Core Classics: Strange Case of Dr. Jekyll and Mr. Hyde Reader (Core Knowledge Language Arts, Grade 7, Unit 3)", license="CC BY-NC-SA 4.0",
                   license_url="https://creativecommons.org/licenses/by-nc-sa/4.0/", year="Core Knowledge Foundation"),
    "timemachine": dict(file="venv-CC_TheTimeMachine_Reader.pdf", title="The Time Machine", author="H. G. Wells",
                        source="Core Classics: The Time Machine Reader (Core Knowledge Language Arts, Grade 7, Unit 4)", license="CC BY-NC-SA 4.0",
                        license_url="https://creativecommons.org/licenses/by-nc-sa/4.0/", year="Core Knowledge Foundation"),
}
# Sections each lesson reads, as PRINTED page ranges in the Core Knowledge readers (from their contents pages; scene breaks found in the text).
CK_SECTIONS = {
    "treasure": {"Chapter 1": (2, 9), "Chapter 2": (10, 21), "Chapter 3": (22, 33), "Chapter 4": (34, 43), "Chapter 5": (44, 51), "Chapter 6": (52, 61),
                 "Chapter 7": (62, 71), "Chapter 8": (72, 79), "Chapter 9": (80, 89), "The Voyage": (90, 98), "Blackbeard": (99, 110), "Glossary": (111, 120)},
    "tempest": {"Introduction": (1, 51), "Act 1, Scene 1": (52, 61), "Act 1, Scene 2 (first section)": (62, 73), "Act 1, Scene 2 (second section)": (74, 107),
                "Act 2": (108, 151), "Act 3": (152, 191), "Act 4": (192, 217), "Act 5": (218, 243), "Epilogue": (244, 246)},
    "jekyll": {"Introduction": (1, 14), "Chapter 1": (15, 28), "Chapter 2": (29, 49), "Chapter 3": (50, 55), "Chapter 4": (56, 66), "Chapter 5": (67, 76),
               "Chapter 6": (77, 85), "Chapter 7": (86, 89), "Chapter 8": (90, 112), "Chapter 9": (113, 128), "Chapter 10": (129, 167)},
    "timemachine": {"Introduction": (1, 14), "Chapter 1": (15, 26), "Chapter 2": (27, 35), "Chapter 3": (36, 45), "Chapter 4": (46, 57), "Chapter 5": (58, 66),
                    "Chapter 6": (67, 80), "Chapter 7": (81, 91), "Chapter 8": (92, 114), "Chapter 9": (115, 126), "Chapter 10": (127, 140),
                    "Chapter 11": (141, 150), "Chapter 12": (151, 163), "Chapter 13": (164, 169), "Chapter 14": (170, 181), "Chapter 15": (182, 184),
                    "After the Story": (185, 192), "Epilogue": (193, 194)},
}


def page_offset(path):
    """PDF page index (1-based) minus printed page number, by the most common value over pages that show a number."""
    n = len(pikepdf.open(path).pages); c = collections.Counter()
    for i in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", path, "-"], capture_output=True, text=True).stdout
        ls = [l.strip() for l in t.splitlines() if l.strip()]
        for l in ls[:1] + ls[-1:]:
            m = re.match(r"^(\d{1,3})\s{2,}", l) or re.search(r"\s{2,}(\d{1,3})$", l) or re.fullmatch(r"(\d{1,3})", l)
            if m: c[i - int(m.group(1))] += 1
    return c.most_common(1)[0][0]


def shrink_images(pdf):
    """Re-encode large lossless illustrations as JPEG so the combined Reader stays small enough to serve."""
    for page in pdf.pages:
        for name, raw in list(page.images.items()):
            try:
                if int(raw.get("/Length", 0)) < 250_000 or raw.get("/SMask") is not None or raw.get("/Filter") != pikepdf.Name("/FlateDecode"): continue
                im = pikepdf.PdfImage(raw).as_pil_image()
                if im.mode not in ("RGB", "L"): im = im.convert("RGB")
                im.thumbnail((1400, 1400))
                buf = io.BytesIO(); im.save(buf, "JPEG", quality=72, optimize=True)
                raw.write(buf.getvalue(), filter=pikepdf.Name("/DCTDecode"))
                raw.Width, raw.Height = im.width, im.height
                raw.ColorSpace = pikepdf.Name("/DeviceRGB" if im.mode == "RGB" else "/DeviceGray"); raw.BitsPerComponent = 8
                for k in ("/DecodeParms", "/Decode"):
                    if k in raw: del raw[k]
            except Exception:
                continue


# ------------------------------------------------------------------ front matter, dividers, covers
def draw_title_page(c, g, parts):
    c.setFillColor(IVORY); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(MAIN); c.rect(0, PAGE_H - 3.2 * inch, PAGE_W, 3.2 * inch, fill=1, stroke=0)
    covers.stripe(c, PAGE_H - 3.2 * inch - 8, 8, INK)
    text(c, M, PAGE_H - 1.1 * inch, "VENVLEARNING", "BodySemi", 12, WHITE)
    text(c, M, PAGE_H - 2.0 * inch, f"Grade {g} Reader", "Display", 44, WHITE)
    text(c, M, PAGE_H - 2.55 * inch, "English Language Arts  ·  2026–2027", "BodyMed", 14, covers.BLUSH)
    y = PAGE_H - 4.2 * inch
    text(c, M, y, "IN THIS READER", "BodyBold", 10, MAIN); c.setFillColor(GOLD); c.rect(M, y - 8, 46, 2.5, fill=1, stroke=0); y -= 40
    for k, p in enumerate(parts):
        text(c, M, y, f"PART {['ONE', 'TWO', 'THREE', 'FOUR'][k]}", "BodyBold", 9, MAIN)
        text(c, M + 1.1 * inch, y, p["title"], "Display", 20, DARK)
        text(c, M + 1.1 * inch, y - 18, p["author"], "Body", 11, MUTED); y -= 52


def front_matter(path, g, parts, units):
    """Title page, how to use this Reader, contents, and credits."""
    buf = io.BytesIO()
    W = PAGE_W - 2 * M
    story = [Spacer(1, 10), Paragraph("HOW TO USE THIS READER", S["eyebrow"]), Paragraph("One book for the whole year", S["h1"]), Rule(), Spacer(1, 8)]
    for p in [
        f"This Reader holds every story, play, novel, and selection that your Grade {g} English Language Arts lessons ask you to read. "
        "When a lesson says <b>Read in your Reader</b>, find the part and the pages it names, then read with the lesson's question in mind.",
        "This book has " + {2: "two", 3: "three", 4: "four"}[len(parts)] + " parts. <b>Each part keeps its own page numbers</b>, so the pages in a lesson always "
        "go with the part named. For example, “Reader: " + parts[0]["short"] + ", pp. 3–9” means pages 3 to 9 of " + parts[0]["title"] + ".",
        "Reading on a screen? Use the bookmarks to jump to any part or chapter, or open the lesson links on VenvLearning, which go straight to the right page."]:
        story.append(Paragraph(p, S["body7"]))
    story += [Spacer(1, 10), Paragraph("WHICH UNITS READ WHAT", S["eyebrow"])]
    rows = [[Paragraph("<b>Units</b>", S["small"]), Paragraph("<b>Reading</b>", S["small"])]] + [[Paragraph(a, S["small"]), Paragraph(b, S["small"])] for a, b in units]
    t = Table(rows, colWidths=[1.3 * inch, W - 1.3 * inch]); t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [t, PageBreak(), Spacer(1, 10), Paragraph("CONTENTS", S["eyebrow"]), Rule(), Spacer(1, 6)]
    for k, p in enumerate(parts):
        story.append(Paragraph(f"<font name='BodyBold' color='#{MAIN.hexval()[2:]}'>PART {['ONE', 'TWO', 'THREE', 'FOUR'][k]}</font>&nbsp;&nbsp;"
                               f"<font name='Display' size='15' color='#{DARK.hexval()[2:]}'>{escape(p['title'])}</font>", ParagraphStyle("pt", parent=S["toc"], spaceBefore=10, spaceAfter=3)))
        rows = [[Paragraph(escape(n), S["toc"]), Paragraph(f"p. {a}", ParagraphStyle("r", parent=S["toc"], alignment=2))] for n, a in p["toc"]]
        tt = Table(rows, colWidths=[W - 0.8 * inch, 0.8 * inch]); tt.setStyle(TableStyle([("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
        story.append(tt)
    story += [PageBreak(), Spacer(1, 10), Paragraph("CREDITS AND LICENSES", S["eyebrow"]), Rule(), Spacer(1, 6)]
    for p in parts:
        if p.get("ck"):
            ck = p["ck"]
            story.append(Paragraph(f"<b>{escape(p['title'])}</b>, by {escape(p['author'])}. Reproduced in full from <i>{escape(ck['source'])}</i>, "
                                   f"© Core Knowledge Foundation (www.coreknowledge.org), licensed under the Creative Commons Attribution-NonCommercial-ShareAlike "
                                   f"License ({ck['license']}, {ck['license_url']}). The pages are unchanged except that printer's crop marks were trimmed and large "
                                   "illustrations were compressed. This part may be shared for non-commercial purposes under the same license.", S["small"]))
        else:
            story.append(Paragraph(f"<b>{escape(p['title'])}</b>. {escape(p['credit'])}", S["small"]))
    story.append(Paragraph("This Reader was assembled by VenvLearning for home use. It is not sold. The Core Knowledge Foundation does not endorse VenvLearning.", S["small"]))

    def first(c, d):
        c.saveState()
        if c.getPageNumber() == 1: draw_title_page(c, g, parts)
        else: c.setFillColor(IVORY); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        c.restoreState()
    doc = BaseDocTemplate(buf, pagesize=(PAGE_W, PAGE_H), leftMargin=M, rightMargin=M, topMargin=0.9 * inch, bottomMargin=0.8 * inch)
    doc.addPageTemplates([PageTemplate("p", [Frame(M, 0.8 * inch, PAGE_W - 2 * M, PAGE_H - 1.7 * inch)], onPage=first)])
    doc.build([PageBreak()] + story)
    open(path, "wb").write(buf.getvalue())


def divider(path, k, p, units):
    c = _canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H))
    c.setFillColor(MAIN); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(DARK); c.rect(0, 0, PAGE_W, 1.2 * inch, fill=1, stroke=0); covers.stripe(c, 1.2 * inch, 8, INK)
    text(c, M, PAGE_H - 2.4 * inch, f"PART {['ONE', 'TWO', 'THREE', 'FOUR'][k]}", "BodyBold", 13, covers.BLUSH)
    c.setFillColor(GOLD); c.rect(M, PAGE_H - 2.55 * inch, 54, 2.5, fill=1, stroke=0)
    y = PAGE_H - 3.4 * inch
    for line in p["title_lines"]:
        text(c, M, y, line, "Display", 46, WHITE); y -= 52
    text(c, M, y - 6, p["author"], "BodyMed", 16, covers.BLUSH)
    st = ParagraphStyle("d", fontName="Body", fontSize=12, leading=17, textColor=WHITE)
    para = Paragraph(escape(units), st); _, h = para.wrap(PAGE_W - 2 * M, 300); para.drawOn(c, M, 2.2 * inch)
    if p.get("ck"):
        para = Paragraph(escape(f"From the {p['ck']['source']}. © Core Knowledge Foundation. {p['ck']['license']}. "
                                "This part keeps its original page numbers."), ParagraphStyle("d2", parent=st, fontSize=9.5, leading=13, textColor=covers.BLUSH))
        _, h = para.wrap(PAGE_W - 2 * M, 300); para.drawOn(c, M, 1.45 * inch)
    text(c, M, 0.55 * inch, "VENVLEARNING  ·  ENGLISH LANGUAGE ARTS READER", "BodySemi", 9, WHITE)
    c.showPage(); c.save()


def reader_covers(g, path):
    """Front and back covers in the ELA series style; the back cover shows the four-book set."""
    covers.KIND_BLURB["reader"] = ("This <b>Student Reader</b> holds every story, play, novel, and anthology selection the year's lessons read, in one book. "
                                   "Each part keeps its own page numbers, and every ELA lesson names the part and pages to read.")
    covers.INSIDE["reader"] = {4: ["King Arthur and the Round Table: 22 chapters, retold by VenvLearning", "Treasure Island (Core Knowledge Reader)",
                                   "Words to Know for every chapter", "Lesson-by-lesson page references"],
                               7: ["The Tempest, by William Shakespeare", "Strange Case of Dr. Jekyll and Mr. Hyde", "The Time Machine, by H. G. Wells",
                                   "Voices of the Harlem Renaissance: an anthology"]}[g]
    engine.KIND_LABEL.setdefault("reader", "Student Reader"); covers.KIND_LABEL.setdefault("reader", "Student Reader")
    from build import BOOKS
    ela = BOOKS[f"ela{g}"]()
    book = Book("ela", g, f"Grade {g} English Language Arts", ela.units, kinds=("textbook", "workbook", "teacher", "reader"))
    covers.make_covers(book, "reader", path)


def assemble(g, parts, units_rows, out_pdf):
    tmp = os.path.join(OUT, f".reader{g}"); os.makedirs(tmp, exist_ok=True)
    reader_covers(g, os.path.join(tmp, "covers.pdf"))
    for k, p in enumerate(parts): divider(os.path.join(tmp, f"div{k}.pdf"), k, p, p["units"])
    # front matter is 4 pages: title page, how to use, contents, credits (checked below)
    front_matter(os.path.join(tmp, "front.pdf"), g, parts, units_rows)
    out = pikepdf.new(); outline = []
    cov = pikepdf.open(os.path.join(tmp, "covers.pdf")); front = pikepdf.open(os.path.join(tmp, "front.pdf"))
    out.pages.append(cov.pages[0]); out.add_blank_page(page_size=(PAGE_W, PAGE_H))
    out.pages.extend(front.pages)
    outline.append(("Contents", 2 + 3))                      # cover, inside cover, title page, how to use, contents
    index_parts = {}
    for k, p in enumerate(parts):
        dv = pikepdf.open(os.path.join(tmp, f"div{k}.pdf")); out.pages.extend(dv.pages)
        src = pikepdf.open(p["pdf"])
        if p.get("ck"): shrink_images(src)
        for pg in src.pages:
            if "/CropBox" in pg.obj: pg.obj.MediaBox = pg.obj.CropBox
        base = len(out.pages)                      # PDF page index (0-based) where this part's first page goes
        out.pages.extend(src.pages)
        p["pdf_start"] = base + 1                  # 1-based PDF page of the part's first page
        outline.append((f"Part {k + 1}: {p['title']}", base - 1 + 1))
        p["pdf_start"] = base + 1
        p["outline_children"] = [(n, p["pdf_start"] + p["offset"] + a - (0 if p.get("ck") else 1)) for n, a in p["toc"]]   # printed page a -> PDF page
        index_parts[p["key"]] = p
    while (len(out.pages) + 1) % 2: out.add_blank_page(page_size=(PAGE_W, PAGE_H))
    out.pages.append(cov.pages[1])
    with out.open_outline() as ol:
        for title, pg in outline:
            item = pikepdf.OutlineItem(title, pg - 1)
            for p in parts:
                if title.endswith(p["title"]):
                    item.children = [pikepdf.OutlineItem(n, pp - 1) for n, pp in p["outline_children"]]
            ol.root.append(item)
    out.docinfo["/Title"] = f"Grade {g} ELA Reader"; out.docinfo["/Author"] = "VenvLearning"
    out.save(out_pdf, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
    return index_parts


def main(src_dir):
    os.makedirs(OUT, exist_ok=True); tmp = os.path.join(OUT, ".readerparts"); os.makedirs(tmp, exist_ok=True)
    ka_pdf, hr_pdf = os.path.join(tmp, "arthur.pdf"), os.path.join(tmp, "harlem.pdf")
    ka, hr = build_arthur(ka_pdf), build_harlem(hr_pdf)
    from readers.arthur_a import CHAPTERS
    from readers.harlem import SECTIONS

    def ck_part(key, short, title_lines, units):
        ck = CK[key]; path = os.path.join(src_dir, ck["file"]); off = page_offset(path)
        toc = [(n, a) for n, (a, b) in CK_SECTIONS[key].items()]
        return dict(key=key, title=ck["title"], short=short, author=ck["author"], title_lines=title_lines, pdf=path, ck=ck, offset=off - 1,
                    toc=toc, sections={n: (a, b) for n, (a, b) in CK_SECTIONS[key].items()}, units=units)

    ka_secs = {f"Chapter {i}": (ka[i], (ka[i + 1] - 1) if i < len(CHAPTERS) else ka["end"] - 1) for i in range(1, len(CHAPTERS) + 1)}
    ka_part = dict(key="arthur", title="King Arthur and the Round Table", short="King Arthur", author="Retold by VenvLearning from the medieval legends",
                   title_lines=["King Arthur", "and the Round Table"], pdf=ka_pdf, offset=0,
                   toc=[(f"Chapter {i}: {c['title']}", ka[i]) for i, c in enumerate(CHAPTERS, 1)], sections=ka_secs,
                   credit="A VenvLearning retelling of the Arthurian legends (Sir Thomas Malory, Le Morte d'Arthur, 1485). © 2026 VenvLearning.",
                   units="Read in Units 1–3 and 7–9: one chapter each week, from the birth of Arthur to the end of the Round Table.")
    titles = [s["title"] for s in SECTIONS]
    hr_secs = {t: (hr[t], (hr[titles[i + 1]] - 1) if i + 1 < len(titles) else hr["end"] - 1) for i, t in enumerate(titles)}
    hr_part = dict(key="harlem", title="Voices of the Harlem Renaissance", short="Harlem Renaissance", author="An anthology, with background by VenvLearning",
                   title_lines=["Voices of the", "Harlem Renaissance"], pdf=hr_pdf, offset=0, toc=[(t, hr[t]) for t in titles], sections=hr_secs,
                   credit="Background sections © 2026 VenvLearning. All poems and essay excerpts were published in 1930 or earlier and are in the public domain in the United States; see Sources at the end of the part.",
                   units="Read in Units 7 and 9: history, background, and the poems and essays of the movement.")
    g4 = [ka_part, ck_part("treasure", "Treasure Island", ["Treasure Island"], "Read in Units 4–6: nine chapters of the adventure, plus “The Voyage” and “Blackbeard.”")]
    g7 = [ck_part("tempest", "The Tempest", ["The Tempest"], "Read in Units 1–2: the complete play, act by act."),
          ck_part("jekyll", "Jekyll and Hyde", ["Strange Case of", "Dr. Jekyll", "and Mr. Hyde"], "Read in Units 3–4: the complete novella, chapter by chapter."),
          ck_part("timemachine", "The Time Machine", ["The Time Machine"], "Read in Units 5–6 and 8: the novel from the Inventor to the Epilogue."), hr_part]
    rows4 = [("Units 1–3", "King Arthur and the Round Table, Chapters 1–12"), ("Units 4–6", "Treasure Island, Chapters 1–9, “The Voyage,” and “Blackbeard”"),
             ("Units 7–8", "King Arthur and the Round Table, Chapters 13–20"), ("Unit 9", "King Arthur, Chapters 21–22, and rereading")]
    rows7 = [("Units 1–2", "The Tempest, Introduction through Act 5"), ("Units 3–4", "Strange Case of Dr. Jekyll and Mr. Hyde, Chapters 1–10"),
             ("Units 5–6", "The Time Machine, Chapters 1–12"), ("Unit 7", "Voices of the Harlem Renaissance"), ("Unit 8", "The Time Machine, Chapters 13–15, After the Story, and Epilogue"),
             ("Unit 9", "Voices of the Harlem Renaissance (Hughes, Georgia Douglas Johnson, McDougald)")]
    for g, parts, rows in ((4, g4, rows4), (7, g7, rows7)):
        out_pdf = os.path.join(OUT, f"grade{g}-ela-reader.pdf")
        assemble(g, parts, rows, out_pdf)
        idx = {"cover_pages": 0, "parts": {}}
        for p in parts:
            idx["parts"][p["key"]] = {"title": p["title"], "short": p["short"], "pdf_start": p["pdf_start"], "offset": p["offset"],
                                      "sections": {n: {"printed": [a, b], "pdf": [p["pdf_start"] + p["offset"] + a - (0 if p.get("ck") else 1),
                                                                                  p["pdf_start"] + p["offset"] + b - (0 if p.get("ck") else 1)]}
                                                   for n, (a, b) in p["sections"].items()}}
        json.dump(idx, open(out_pdf[:-4] + ".index.json", "w"), ensure_ascii=False, indent=1)
        print(f"grade {g}: {len(pikepdf.open(out_pdf).pages)} pages, {os.path.getsize(out_pdf) / 1e6:.1f} MB")


if __name__ == "__main__":
    main(sys.argv[1])
