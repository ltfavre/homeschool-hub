"""Renders a Book (see engine.py) into the student textbook, student workbook and teacher edition."""
import os
import re as _re
from engine import *


# ================================================================ shared pieces

def check_tag(C):
    """Eyebrow label for a check page."""
    if "Quiz" in C.title: return "WEEKLY QUIZ"
    if "Sketchbook" in C.title: return "SKETCHBOOK CHECK"
    if C.title.startswith("Prueba"): return "PRUEBA · WEEKLY QUIZ"
    if C.title.startswith("Examen"): return "EXAMEN · YEAR-END TEST" if "Final" in C.title else "EXAMEN · UNIT TEST"
    if C.title.startswith("Repaso"): return "REPASO · REVIEW"
    if "Portfolio" in C.title: return "YEAR-END PORTFOLIO REVIEW" if "Year-End" in C.title else "PORTFOLIO REVIEW"
    if "Final Exam" in C.title: return "FINAL EXAM" if C.kind == "test" else "FINAL REVIEW"
    if "Exam" in C.title: return "UNIT EXAM"
    if "Year-End" in C.title:
        return "YEAR-END TEST" if C.kind == "test" else "YEAR-END REVIEW"
    return {"test": "UNIT TEST", "review": "UNIT REVIEW"}.get(C.kind, "WEEKLY CHECK")

# ---------------------------------------------------------------- clarity kit
# Two visual languages, so a student always knows what she is looking at:
#   * Lesson information and instructions (goal, assignment, words to know, key ideas, examples, questions) are sans-serif
#     boxes, each opened by a solid colored LABEL CHIP that names what the box is.
#   * Reading content (stories, excerpts, articles, speeches) is set like a page from a book: warm paper, a brown
#     "READING" tab, and a book serif (see passage_box).

def chip(text, bg, fg=WHITE, size=8.5):
    """A solid rounded label, e.g. TODAY'S GOAL. Sized to its text and left-aligned."""
    st = ParagraphStyle("chip", fontName="BodyBold", fontSize=size, leading=size + 2, textColor=fg)
    # symbols the brand font lacks (★ ✎) are drawn with the fallback font, so measure them in it
    from engine import _BODY_CMAP
    w = sum(stringWidth(ch, "BodyBold" if ord(ch) in _BODY_CMAP else "Sym", size) for ch in text) + 18
    tb = Table([[P(text, st)]], colWidths=[w], rowHeights=[size + 9])
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("ROUNDEDCORNERS", [5, 5, 5, 5]), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                            ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    tb.hAlign = "LEFT"
    return tb


def boxed(t, label, flowables, bg, chip_bg=None, chip_fg=None, border=None, left_bar=None):
    """An information box opened by a label chip."""
    return panel([chip(label, chip_bg or t.main, chip_fg or t.on_main), Spacer(1, 5)] + list(flowables), bg, border=border, left_bar=left_bar)


class StepHeader(Flowable):
    """Numbered lesson step: a colored circle with the step number, the step name, and a rule to the margin."""
    def __init__(self, t, n, label, note=None):
        super().__init__(); self.t, self.n, self.label, self.note = t, n, label, note
    def wrap(self, aw, ah): self.aw = aw; return aw, 30
    def draw(self):
        c, t = self.canv, self.t
        c.setFillColor(t.main); c.circle(11, 13, 11, stroke=0, fill=1)
        text(c, 11, 9, str(self.n), "BodyBold", 11.5, t.on_main, "c")
        text(c, 30, 8.5, self.label, "BodySemi", 14, t.dark)
        x = 30 + stringWidth(self.label, "BodySemi", 14) + 10
        if self.note:
            text(c, x, 9, self.note, "Body", 9.5, MUTED); x += stringWidth(self.note, "Body", 9.5) + 10
        c.setStrokeColor(t.mid); c.setLineWidth(1); c.line(x, 13, self.aw, 13)


def step(t, n, label, note=None):
    return [Spacer(1, 6), StepHeader(t, n, label, note), Spacer(1, 4)]


class Target(Flowable):
    """Bullseye icon for the goal card."""
    def __init__(self, t, size=34): super().__init__(); self.t, self.s = t, size
    def wrap(self, aw, ah): return self.s, self.s
    def draw(self):
        c, r = self.canv, self.s / 2
        for k, col in enumerate([self.t.main, WHITE, self.t.main, WHITE, self.t.main]):
            c.setFillColor(col); c.circle(r, r, r * (1 - k * 0.2), stroke=0, fill=1)


class CheckBox(Flowable):
    """An empty checkbox to tick off an assignment step."""
    def __init__(self, t, size=12): super().__init__(); self.t, self.s = t, size
    def wrap(self, aw, ah): return self.s, self.s + 3
    def draw(self):
        c = self.canv; c.setStrokeColor(self.t.main); c.setLineWidth(1.3); c.setFillColor(WHITE)
        c.roundRect(0, 1, self.s, self.s, 2, stroke=1, fill=1)


def when(L):
    """'Tuesday, November 3' from the school calendar date pace() gives each lesson."""
    d = getattr(L, "_d", None)
    return f"{d:%A, %B} {d.day}" if d else (L.date or "")


def lesson_banner(t, L, U=None, tag=None):
    """Full-width colored bar: LESSON 1.5 and the planned day on the left, the unit on the right."""
    big = ParagraphStyle("bn", fontName="BodyBold", fontSize=13, leading=16, textColor=t.on_main)
    sm = ParagraphStyle("bs", fontName="BodyMed", fontSize=9.5, leading=12, textColor=t.on_main)
    right = ParagraphStyle("br", parent=sm, alignment=TA_RIGHT)
    left = [P(f"LESSON {L.num}" + (f"  ·  {tag}" if tag else ""), big)]
    if when(L): left.append(P(f"Planned for {when(L)}", sm))
    unit = f"Unit {U.num}: {U.title}" if U else f"Unit {L.num.split('.')[0]}"
    tb = Table([[left, P(unit, right)]], colWidths=[W * 0.5, W * 0.5])
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), t.main), ("ROUNDEDCORNERS", [6, 6, 6, 6]), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                            ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return tb


def lesson_header(t, L, U=None, tag=None, title_style=None):
    return [lesson_banner(t, L, U, tag), Spacer(1, 8),
            toc_heading(f"Lesson {L.num}: {L.title}", title_style or t.h1, 1, running=f"Lesson {L.num} · {L.title}")]


def goal_card(t, L, size=15):
    """TODAY'S GOAL: the I can statement, large, next to a bullseye. The standard is small reference text."""
    goal = ParagraphStyle("goal", fontName="BodySemi", fontSize=size, leading=size * 1.32, textColor=t.dark)
    inner = [chip("TODAY'S GOAL", t.main, t.on_main), Spacer(1, 5), P(L.i_can, goal)]
    if L.standard: inner.append(P(f"Standards: {L.standard}", ParagraphStyle("std", parent=t.tiny, spaceBefore=3)))
    tb = Table([[Target(t), inner]], colWidths=[48, W - 48])
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), t.wash), ("BOX", (0, 0), (-1, -1), 1.2, t.main), ("ROUNDEDCORNERS", [6, 6, 6, 6]),
                            ("VALIGN", (0, 0), (0, 0), "MIDDLE"), ("VALIGN", (1, 0), (1, 0), "TOP"),
                            ("LEFTPADDING", (0, 0), (0, 0), 12), ("LEFTPADDING", (1, 0), (1, 0), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                            ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))
    return tb


def checklist(t, label, items, bg=WHITE):
    """A labeled list of steps, each with a checkbox to tick off."""
    st = ParagraphStyle("cl", parent=t.boxt, fontSize=11.5, leading=15.5, spaceAfter=0)
    rows = [[CheckBox(t), P(x, st)] for x in items]
    tb = Table(rows, colWidths=[20, W - 20 - 30])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return panel([chip(label, HUNTER), Spacer(1, 4), tb], bg, border=LINE, left_bar=HUNTER)


_READER_INDEX = {}


def reader_pages(t, r):
    """Printed pages in the Grade Reader for a Read in Your Reader assignment, from the Reader's page index."""
    import json
    g = getattr(t, "grade", None)
    if g not in _READER_INDEX:
        f = os.path.join(HERE, "..", "downloads", "textbooks", f"grade{g}-ela-reader.index.json")
        _READER_INDEX[g] = json.load(open(f, encoding="utf-8")) if os.path.exists(f) else None
    idx = _READER_INDEX[g]
    if not idx: return None
    book, sec = r.book.lower(), r.section.lower()
    part = next((p for p in idx["parts"].values() if p["title"].lower() in book or p["short"].lower() in book), None)
    if not part: return None
    names = [n for n in part["sections"] if n.lower() in sec]
    m = _re.search(r"chapters? (\d+)(?:\s*(?:–|-|and|through)\s*(\d+))?", sec)
    if m:
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        names += [f"Chapter {n}" for n in range(a, b + 1) if f"Chapter {n}" in part["sections"]]
    if not names: return None
    lo = min(part["sections"][n]["printed"][0] for n in names); hi = max(part["sections"][n]["printed"][1] for n in names)
    return f"page {lo}" if lo == hi else f"pages {lo}–{hi}"


def assignment_items(t, L):
    """Today's steps for a lesson, in order: read the lesson, any Reader section, any hands-on activity, Your Turn, the workbook."""
    items = [f"Read <b>Lesson {L.num}</b> in this book with your teacher."]
    for b in L.learn:
        if isinstance(b, ReaderAssign):
            pages = reader_pages(t, b)
            items.append(f"Read in your <b>Reader</b>: {b.book.replace(' Reader', '')}, {b.section}" + (f" ({pages})" if pages else "") + ".")
        elif isinstance(b, Investigate):
            tag = {"science": "Investigate", "art": "Create"}.get(t.subject, "Activity")
            items.append(f"Do the <b>{tag}</b> activity: {b.title}.")
    if L.try_it: items.append(f"Answer the <b>{t.lab['try_'].title()}</b> questions in your notebook.")
    items.append(f"Complete <b>Workbook Lesson {L.num}</b>.")
    return items


def vocab_panel(t, vocab, title="Words to Know"):
    rows = [[P(f"<b>{w}</b>", t.cellb), P(d, t.cell)] for w, d in vocab]
    tb = Table(rows, colWidths=[1.45 * inch, W - 1.45 * inch - 30])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LINEBELOW", (0, 0), (-1, -2), 0.4, LINE)]))
    return boxed(t, title.upper(), [tb], SAGE_WASH, HUNTER, WHITE, left_bar=HUNTER)


def render_blocks(t, blocks, teacher=False):
    out = []
    for b in blocks:
        if isinstance(b, Text): out.append(P(b.t, t.body))
        elif isinstance(b, Heading): out.append(P(b.t, t.h3))
        elif isinstance(b, Bullets): out += bullets(b.items, t.bullet)
        elif isinstance(b, Figure):
            f = b.fn(t); items = [Spacer(1, 4), centered(f)]
            if b.caption: items.append(P(b.caption, ParagraphStyle("cap", parent=t.small, alignment=TA_CENTER)))
            items.append(Spacer(1, 6)); out.append(KeepTogether(items))
        elif isinstance(b, KeyIdea):
            out.append(Spacer(1, 2)); out.append(boxed(t, "★ " + b.title.upper(), [P(b.t, ParagraphStyle("ki", parent=t.boxt, fontName="BodyMed"))], t.wash, left_bar=t.main)); out.append(Spacer(1, 8))
        elif isinstance(b, WatchOut):
            out.append(Spacer(1, 2)); out.append(boxed(t, "! WATCH OUT", [P(b.t, t.boxt)], colors.HexColor("#FBF3DC"), GOLD, INK, left_bar=GOLD)); out.append(Spacer(1, 8))
        elif isinstance(b, Example):
            out.append(Spacer(1, 4)); out.append(example_box(t, b)); out.append(Spacer(1, 8))
        elif isinstance(b, Vocab):
            out.append(vocab_panel(t, b.items)); out.append(Spacer(1, 8))
        elif isinstance(b, Passage):
            out += [CondPageBreak(2.4 * inch), Spacer(1, 4), passage_box(t, b), Spacer(1, 10)]   # never strand a reading's title at a page bottom
        elif isinstance(b, ReaderAssign):
            out += [Spacer(1, 2), reader_box(t, b), Spacer(1, 8)]
        elif isinstance(b, Beside):
            fw = W * b.fig_w; tw = W - fw - 14
            fig = [b.fn(t)] + ([P(b.caption, ParagraphStyle("capb", parent=t.small, alignment=TA_CENTER))] if b.caption else [])
            txt = [P(x, t.body) for x in b.texts]
            cells = [fig, txt] if b.left else [txt, fig]
            tb = Table([cells], colWidths=[fw, tw] if b.left else [tw, fw])
            tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (0, 0), 14),
                                    ("RIGHTPADDING", (1, 0), (1, 0), 0), ("TOPPADDING", (0, 0), (-1, -1), 2)]))
            out += [tb, Spacer(1, 8)]
        elif isinstance(b, Investigate):
            out += [Spacer(1, 4), investigate_box(t, b), Spacer(1, 8)]
        elif isinstance(b, Code):
            out += [Spacer(1, 4)] + code_box(t, b) + [Spacer(1, 8)]
        elif isinstance(b, Watch):
            out += [Spacer(1, 2), watch_box(t, b), Spacer(1, 8)]
        elif isinstance(b, Callout):
            out += [Spacer(1, 2), boxed(t, b.label.upper(), [P(b.t, t.boxt)], SAGE_WASH, HUNTER, WHITE, left_bar=HUNTER), Spacer(1, 8)]
        elif isinstance(b, Dialogue):
            out += [Spacer(1, 2), dialogue_box(t, b), Spacer(1, 8)]
        elif isinstance(b, Phrases):
            rows = [["Español", "Sounds like", "English"]] + [list(r) for r in b.rows]
            out += [P(b.title, t.h4), table(t, rows, [2.2 * inch, 1.8 * inch, W - 4.0 * inch], font_size=10), Spacer(1, 8)]
        elif isinstance(b, OnTheJob):
            out += [Spacer(1, 2), boxed(t, "ON THE JOB", [P(b.t, t.boxt)], SAGE_WASH, HUNTER, WHITE, left_bar=HUNTER), Spacer(1, 8)]
    return out


CODE_BG = colors.HexColor("#FBF4F5")
LANG = [("sas", "SAS", colors.HexColor("#234638")), ("python", "PYTHON", colors.HexColor("#5C7A5F")), ("r", "R", colors.HexColor("#8C7330"))]


def _code_para(src, size=8.4):
    from reportlab.platypus import XPreformatted
    esc = src.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return XPreformatted(esc, ParagraphStyle("code", fontName="Mono", fontSize=size, leading=size * 1.32, textColor=INK))


def code_box(t, cb):
    """Header row, then one row per language (label pill + code) so a long block can continue onto the next page."""
    rows = [[P(f"CODE IT  ·  {cb.title.upper()}", t.eyebrow), ""]]
    styles = [("SPAN", (0, 0), (1, 0))]
    for key, lab, col in LANG:
        src = getattr(cb, key)
        if not src: continue
        pill = Table([[P(f"<b>{lab}</b>", ParagraphStyle("pl", parent=t.small, textColor=WHITE, alignment=TA_CENTER, fontSize=7.5, leading=9))]], colWidths=[46], rowHeights=[14])
        pill.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), col), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("ROUNDEDCORNERS", [4, 4, 4, 4])]))
        rows.append([pill, _code_para(src.strip("\n"))])
    if cb.output:
        rows.append([P("<b>OUTPUT</b>", ParagraphStyle("ol", parent=t.small, fontSize=7.5, textColor=MUTED)), _code_para(cb.output.strip("\n"), 8)])
    if cb.note:
        rows.append([P("", t.small), P(cb.note, ParagraphStyle("cn", parent=t.small, textColor=INK))]); 
    tb = Table(rows, colWidths=[58, W - 58])
    tb.setStyle(TableStyle(styles + [("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (-1, -1), 0.8, t.mid), ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
                                     ("LINEABOVE", (0, 0), (-1, 0), 4, t.main), ("LINEBELOW", (0, 1), (-1, -2), 0.4, LINE),
                                     ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return [tb]


def dialogue_box(t, d):
    sp = ParagraphStyle("dsp", parent=t.boxt, fontName="BodySemi", textColor=t.accent)
    ln = ParagraphStyle("dln", parent=t.boxt, fontSize=12, leading=16)
    en = ParagraphStyle("den", parent=t.small, fontName="BodyMed")
    rows = [[P("DIÁLOGO  ·  " + d.title.upper(), t.eyebrow), ""]]
    for who, line, eng in d.lines:
        rows.append([P(who, sp), [P(line, ln)] + ([P(eng, en)] if eng else [])])
    if d.note: rows.append(["", P(d.note, t.small)])
    tb = Table(rows, colWidths=[0.95 * inch, W - 0.95 * inch])
    tb.setStyle(TableStyle([("SPAN", (0, 0), (1, 0)), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, -1), IVORY), ("BOX", (0, 0), (-1, -1), 0.8, t.mid),
                            ("LINEABOVE", (0, 0), (-1, 0), 4, t.main), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return tb


def watch_box(t, wb):
    inner = [P(wb.label, t.eyebrow)]
    for title, src, extra in wb.items:
        inner.append(Paragraph(f"<b>{title}</b> · {src}" + (f" <font color='#5F5B56'>({extra})</font>" if extra else ""), ParagraphStyle("wi", parent=t.boxt, leftIndent=14, bulletIndent=2), bulletText="•"))
    if wb.note: inner.append(P(wb.note, t.small))
    return panel(inner, IVORY, border=LINE, left_bar=t.mid)


def investigate_box(t, iv):
    """Hands-on investigation or activity: question, materials, numbered steps, what to record, safety."""
    tag = {"science": "INVESTIGATE", "art": "CREATE"}.get(t.subject, "ACTIVITY")
    inner = [[chip(f"{tag}  ·  {iv.title.upper()}", t.main, t.on_main), Spacer(1, 5)], P(iv.question, ParagraphStyle("ivq", parent=t.boxt, fontName="BodySemi"))]
    if iv.materials: inner.append(P("<b>You need:</b> " + "; ".join(iv.materials) + ".", t.boxt))
    num = ParagraphStyle("ivs", parent=t.boxt, leftIndent=22, bulletIndent=0)
    for i, st in enumerate(iv.steps, 1): inner.append(Paragraph(st, num, bulletText=f"{i}"))
    if iv.record: inner.append(P(f"<b>Record:</b> {iv.record}", ParagraphStyle("ivr", parent=t.boxt, textColor=t.dark, spaceBefore=3)))
    if iv.safety: inner.append(P(f"<b>Safety:</b> {iv.safety}", ParagraphStyle("ivx", parent=t.boxt, textColor=colors.HexColor("#8A5A00"))))
    rows = [[inner[:2]]] + [[f] for f in inner[2:]]
    tb = Table(rows, colWidths=[W])
    tb.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1, t.main), ("BACKGROUND", (0, 0), (-1, -1), IVORY),
                            ("LINEBEFORE", (0, 0), (0, -1), 5, t.main), ("LEFTPADDING", (0, 0), (-1, -1), 14),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                            ("TOPPADDING", (0, 0), (-1, 0), 8), ("BOTTOMPADDING", (0, -1), (-1, -1), 8)]))
    return tb


def passage_box(t, ps):
    """Reading content set like a page from a book: warm paper, a brown READING tab, a book serif, and paragraph
    numbers in the margin. One row per paragraph so a long reading can run across pages."""
    rf = READ_FONT
    num = ParagraphStyle("pn", parent=t.small, alignment=TA_RIGHT, textColor=BOOK, fontName="Mono", fontSize=8, leading=18.5)
    body = ParagraphStyle("pb", fontName=rf, fontSize=12, leading=18.5, textColor=READ_INK, spaceAfter=0, firstLineIndent=0)
    verse = ParagraphStyle("pv", parent=body, leftIndent=18, leading=17, fontName=rf if rf != "Read" else "ReadIt")
    tab = chip("READING" + (f"  ·  {ps.genre.upper()}" if ps.genre else ""), BOOK, WHITE, 8)
    head = [tab, Spacer(1, 6), P(ps.title, ParagraphStyle("pt", parent=t.h2, fontSize=18, leading=22, textColor=READ_INK, spaceBefore=0, spaceAfter=2))]
    if ps.source: head.append(P(ps.source, ParagraphStyle("ps", fontName=rf if rf != "Read" else "ReadIt", fontSize=9.5, leading=13, textColor=BOOK, spaceAfter=6)))
    rows = [["", head]]; n = 0
    for para in ps.paras:
        if para.startswith("<b>") and para.endswith("</b>") and len(para) < 70:
            rows.append(["", P(para[3:-4], ParagraphStyle("psh", parent=body, fontName=rf if rf != "Read" else "ReadBold", fontSize=12.5, spaceBefore=2))])
        elif para.startswith(">"):
            rows.append(["", P(para[1:].strip().replace("\\n", "<br/>").replace("\n", "<br/>"), verse)])
        else:
            n += 1
            rows.append([P(str(n) if ps.numbered else "", num), P(stage(para), body)])
    tb = Table(rows, colWidths=[28, W - 28])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, -1), PAPER),
                            ("BOX", (0, 0), (-1, -1), 0.8, PAPER_EDGE), ("LINEBEFORE", (0, 0), (0, -1), 3, PAPER_EDGE),
                            ("LEFTPADDING", (0, 0), (0, -1), 2), ("RIGHTPADDING", (0, 0), (0, -1), 9),
                            ("LEFTPADDING", (1, 0), (1, -1), 2), ("RIGHTPADDING", (1, 0), (1, -1), 18),
                            ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                            ("TOPPADDING", (0, 0), (-1, 0), 12), ("BOTTOMPADDING", (0, -1), (-1, -1), 14)]))
    return tb


def stage(text):
    """Stage directions in drama, written as <i>(...)</i>, are set in the serif italic and muted."""
    return text.replace("<i>(", "<font name='DisplayIt' color='#5F5B56'>(").replace(")</i>", ")</font>")


def reader_box(t, r):
    """An assignment to read in the Reader (an instruction, so it uses the information style, with the pages)."""
    pages = r.pages or reader_pages(t, r)
    st = ParagraphStyle("rb", parent=t.boxt, fontSize=11.5, leading=16)
    lines = [P(f"<b>{r.book.replace(' Reader', '')}</b>  ·  {r.section}" + (f"  ·  <b>{pages}</b>" if pages else ""), st)]
    if r.focus: lines.append(P(f"<b>As you read, think about:</b> {r.focus}", st))
    return boxed(t, "READ IN YOUR READER", lines, colors.HexColor("#FBF3DC"), BOOK, WHITE, left_bar=BOOK)


def example_box(t, ex):
    inner = [chip(f"{t.lab['example']}  ·  {ex.title.upper()}", t.main, t.on_main), Spacer(1, 5), P(ex.problem, ParagraphStyle("exq", parent=t.boxt, fontName="BodySemi"))]
    if ex.fig: inner += [Spacer(1, 3), centered(ex.fig(t), W - 30), Spacer(1, 3)]
    num = ParagraphStyle("st", parent=t.boxt, leftIndent=22, bulletIndent=0)
    for i, s in enumerate(ex.steps, 1):
        inner.append(Paragraph(s, num, bulletText=f"{i}"))
    inner.append(P(f"<b>{t.lab['answer']}:</b> {ex.answer}", ParagraphStyle("exa", parent=t.boxt, textColor=t.dark, spaceBefore=3)))
    # one row per paragraph so a long example can continue on the next page
    head = inner[:3]
    rows = [[head]] + [[f] for f in inner[3:]]
    tb = Table(rows, colWidths=[W])
    tb.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1, t.main), ("BACKGROUND", (0, 0), (-1, -1), WHITE),
                            ("LINEABOVE", (0, 0), (-1, 0), 4, t.main), ("LEFTPADDING", (0, 0), (-1, -1), 12),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                            ("TOPPADDING", (0, 0), (-1, 0), 8), ("BOTTOMPADDING", (0, -1), (-1, -1), 8)]))
    return tb


def try_it_box(t, L, with_answers=False):
    directions = ParagraphStyle("dir", parent=t.boxt, fontName="BodyMed", textColor=t.dark)
    inner = [chip("✎ " + t.lab["try_"], t.main, t.on_main), Spacer(1, 5),
             P(("<b>Directions:</b> " + t.lab["try_note"]) if not with_answers else "Answers are shown in color.", directions)]
    for i, pr in enumerate(L.try_it, 1):
        row = [P(f"<b>{i}.</b>  {pr.prompt}", t.boxt)]
        if pr.fig: row += [centered(pr.fig(t), W - 40)]
        if pr.choices: row.append(P("    ".join(f"<b>{chr(65 + k)}.</b> {c}" for k, c in enumerate(pr.choices)), t.boxt))
        if with_answers: row.append(P(f"Answer: {pr.answer}", t.answer))
        inner += row
    inner.append(P(f"Next: <b>Workbook Lesson {L.num}</b>.", t.small))
    return panel(inner, t.wash, border=t.mid)


def summary_box(t, L):
    return boxed(t, "✓ REMEMBER", [P(L.summary, ParagraphStyle("sm2", parent=t.boxt, fontName="BodyMed"))], SAGE_WASH, HUNTER, WHITE, left_bar=HUNTER)


# ================================================================ TEXTBOOK
def textbook_lesson(t, L, U=None, teacher=False):
    """Lesson banner and title; Today's Goal and Today's Assignment; then numbered steps:
    1 Get Ready (words to know, warm-up question), 2 Learn, 3 Your Turn, 4 Wrap Up."""
    out = lesson_header(t, L, U)
    out += [goal_card(t, L), Spacer(1, 8), checklist(t, "TODAY'S ASSIGNMENT", assignment_items(t, L), IVORY)]
    out += step(t, 1, "Get Ready")
    if L.vocab: out += [vocab_panel(t, L.vocab), Spacer(1, 8)]
    out.append(boxed(t, t.lab["explore"], [P(L.launch, ParagraphStyle("gr", parent=t.boxt, fontSize=12, leading=17))], WHITE, border=t.mid))
    out += step(t, 2, "Learn")
    out += render_blocks(t, L.learn, teacher)
    out += [KeepTogether(step(t, 3, t.lab["try_"].title()) + [try_it_box(t, L, with_answers=teacher)])]
    if L.summary:
        out += [KeepTogether(step(t, 4, "Wrap Up") + [summary_box(t, L)])]
    return out


def unit_opener(t, U, doc, kind):
    light = t.on_main != WHITE
    w = ParagraphStyle("ow", parent=t.h1, textColor=t.on_main, fontSize=36, leading=40)
    e = ParagraphStyle("oe", parent=t.eyebrow, textColor=t.on_main if light else BLUSH, fontSize=10)
    s = ParagraphStyle("os", parent=t.body, textColor=t.on_main if light else IVORY, fontSize=13, leading=18)
    out = [NextPageTemplate("opener"), SetOpenerNum(doc, U.num), PageBreak(), Running(f"Unit {U.num} · {U.title}"),
           Spacer(1, 0.25 * inch), P(f"UNIT {U.num}" + ("  ·  TEACHER OVERVIEW" if kind == "teacher" else ""), e),
           toc_heading(U.title, w, 0), P(U.subtitle, s), SpaceTo(3.65 * inch), NextPageTemplate("body")]
    return out


def unit_intro_student(t, U):
    out = [P(U.overview, t.body), P("In this unit you will…", t.h3)] + bullets(U.big_ideas, t.bullet)
    if U.real_world: out += [Spacer(1, 6), panel([P(t.lab["real"], t.eyebrow), P(U.real_world, t.boxt)], t.wash, left_bar=t.main)]
    out += [Spacer(1, 8), vocab_panel(t, U.vocab, "Unit Vocabulary"), Spacer(1, 8), P("Lessons in this unit", t.h3)]
    rows = [["Lesson", "Title"]] + [[L.num, L.title] for L in U.lessons]
    out.append(table(t, rows, [0.8 * inch, W - 0.8 * inch]))
    return out


def study_guide(t, U):
    out = [PageBreak(), P(f"UNIT {U.num} REVIEW", t.eyebrow), toc_heading(f"Unit {U.num} Study Guide", t.h1, 1, running=f"Unit {U.num} Study Guide"),
           P("Use this page to get ready for the unit test. Read each big idea, then try the review pages in your workbook.", t.body)]
    rows = [["Lesson", "Remember…"]] + [[L.num, L.summary or ""] for L in U.lessons]
    out.append(table(t, rows, [0.8 * inch, W - 0.8 * inch]))
    return out


PREP = {"math": "Read the student lesson and work the Try It problems.",
        "ela": "Read the student lesson and any assigned Reader chapter; answer the Your Turn questions.",
        "science": "Read the student lesson, gather and test the investigation materials, and answer the Check Your Understanding questions.",
        "social": "Read the student lesson and its sources, preview the maps, and answer the Check Your Understanding questions.",
        "data": "Read the lesson and run the Code It examples.",
        "art": "Read the lesson, gather the studio materials, and try the Create activity yourself first so you can model it.",
        "spanish": "Read the lesson aloud once, play the pronunciation audio for any word you're unsure of, and practice the dialogue."}
ROUTINE = {"math": "Warm-Up 5 · Teach 15 · Guided Practice 10 · Independent Practice 15 · Exit Ticket 5",
           "ela": "Warm-Up 5 · Read 15 · Mini-Lesson 10 · Guided Practice 7 · Independent 10 · Exit Ticket 3",
           "science": "Engage 5 · Investigate 15 · Explain 10 · Guided Practice 7 · Independent 10 · Exit Ticket 3",
           "social": "Warm-Up 5 · Read and Discuss 15 · Analyze 10 · Guided Practice 7 · Independent 10 · Exit Ticket 3",
           "data": "Read 10 · Watch or Code 15 · Quick Check 5",
           "art": "Look and Talk 5 · Learn and Demonstrate 10 · Create 25 · Reflect 5",
           "spanish": "Calentamiento 3 · Escucha y repite 5 · Aprende 6 · Practica 6 · Habla 3 (about 20–25 minutes)"}
DAYS = {"math": "Monday–Thursday", "ela": "Monday–Thursday", "science": "Monday and Wednesday", "social": "Tuesday and Thursday", "data": "Monday–Thursday", "art": "Monday and Wednesday", "spanish": "Monday–Thursday"}


DATA_INTRO = {
    "textbook": ["How to use this book",
                 "This is a year of professional learning built to fit inside a workday: about 30 minutes, Monday through Friday. "
                 "Monday through Thursday is a lesson. Friday is a short quiz plus time to use the week's skill on real work.",
                 ["<b>A 30-minute day:</b> Read 10 · Watch or Code 15 · Quick Check 5. If a day gets away from you, the Quick Check alone keeps you moving.",
                  "<b>Code It</b> boxes show the same task in <b>SAS</b>, <b>Python</b>, and <b>R</b>. Run at least one language every day, and rotate so you build all three.",
                  "<b>Watch and Explore</b> boxes suggest free videos and courses, plus optional DataCamp courses if you subscribe.",
                  "<b>On the Job</b> boxes connect each skill to assessment, research, and reporting work.",
                  "Every exercise uses the VenvLearning data pack (exam.csv, survey.csv, and more), so your results match the answer key.",
                  "Your practice pages, Friday quizzes, unit exams, and answer key are in your <b>Workbook</b>."]],
    "workbook": ["How to use this workbook",
                 "Every lesson in your textbook has matching practice here: a warm-up, practice problems, a coding exercise, and an exit question. "
                 "Fridays have a 15-minute quiz; the last Friday of each unit is the unit exam.",
                 ["Work a problem before checking the <b>Answer Key</b> at the back.", "For coding exercises, write your code in SAS Studio, RStudio, or Jupyter, then record the key output here.",
                  "If an answer doesn't match, compare your code with the solution line by line. Finding the difference is the fastest way to learn.",
                  "Use the <b>Apply It</b> prompts on Fridays to try the week's skill on your own work data."]],
}


def front_matter(t, book, doc, kind):
    out = [NextPageTemplate("body"), PageBreak()]
    intro = {
        "textbook": ["How to use this book",
                     "Every lesson starts on a new page with the same parts, so you always know where to look. "
                     f"{t.lab['study']} Your practice pages are in your <b>Student Workbook</b>, labeled with the same lesson number.",
                     ["<b>Today's Goal</b> (the box with the target) says what you will be able to do by the end of the lesson.",
                      "<b>Today's Assignment</b> is your checklist for the day. Tick each box as you finish it"
                      + (", including the pages to read in your <b>Grade " + str(getattr(t, "grade", "")) + " Reader</b>." if t.subject == "ela" else "."),
                      f"The lesson then goes in numbered steps: <b>1 Get Ready</b>, <b>2 Learn</b>, <b>3 {t.lab['try_'].title()}</b>, and <b>4 Wrap Up</b>.",
                      "Boxes with a <b>colored label</b> are lesson information: <b>Words to Know</b>, <b>Key Idea</b> (the most important rule or fact; learn these), "
                      "worked examples, and <b>Watch Out</b> warnings about common mistakes.",
                      "Pages that look like <b>a page from a book</b>, on cream paper with a brown <b>READING</b> tab, are things to read: stories, excerpts, and articles."]
                     + (["<b>Investigate</b> boxes are hands-on experiments. Do them with your teacher and record what you observe."] if t.subject == "science" else [])
                     + (["<b>Activity</b> boxes are hands-on map, source, and timeline work. Do them with your teacher."] if t.subject == "social" else [])
                     + (["<b>Create</b> boxes are studio activities. Keep everything you make in your portfolio folder."] if t.subject == "art" else [])
                     + (["<b>Sounds like</b> columns show how to say each word; the CAPITAL syllable gets the stress. Hear any word at SpanishDict.com.",
                         "<b>Diálogo</b> boxes are conversations. Read them aloud with a partner, then change the details to talk about yourself."] if t.subject == "spanish" else [])
                     + [
                      ("Every Friday there is a short <b>Sketchbook Check</b> in your workbook. The last Friday of a unit is the <b>Portfolio Review</b>." if t.subject == "art" else
                       "Every Friday there is a short <b>Weekly Check</b> in your workbook. The last Friday of a unit is the <b>Unit Test</b>.")]],
        "workbook": ["How to use this workbook",
                     "Every lesson in your textbook has matching practice pages here. Show your thinking in the work space. "
                     "When a problem has an answer line, write your final answer there.",
                     ["<b>Warm-Up</b> reviews something you already know.",
                      "<b>Practice</b> uses today's lesson.", "<b>Think Deeper</b> problems ask you to explain or find a mistake.",
                      "<b>Exit Ticket</b> shows your teacher what you learned today."]],
        "teacher": ["How to use this Teacher Edition",
                    "This book holds everything needed to teach the course: unit overviews, a plan for every lesson with what to say "
                    "and do, the student lesson with Try It answers, and answer keys for every workbook page, weekly check and unit test.",
                    [(f"<b>Daily routine:</b> {ROUTINE[t.subject]}." if t.subject == "spanish" else f"<b>Daily routine (about 45–55 minutes):</b> {ROUTINE[t.subject]}."),
                     "<b>Say:</b> lines are a suggested script. Use your own words.",
                     f"{DAYS[t.subject]} are lessons. Friday is the <b>{'Sketchbook Check' if t.subject == 'art' else 'Weekly Check'}</b> (about {15 if t.subject in ('science', 'social', 'art') else 20} minutes), then corrections or a project.",
                     "Dates match the VenvLearning lesson plans for the 2026–2027 school year."]],
    }[kind]
    if t.subject == "data":
        intro = DATA_INTRO[kind]
    out += [P(intro[0], t.h2), P(intro[1], t.body)] + bullets(intro[2], t.bullet)
    out += [Spacer(1, 10), P("Contents", t.h2), toc_flowable(t)]
    return out


def build_textbook(book, path):
    t = book.theme; doc = Doc(path, book, "textbook")
    story = [Spacer(1, 1)] + front_matter(t, book, doc, "textbook")
    for U in book.units:
        story += unit_opener(t, U, doc, "textbook") + unit_intro_student(t, U)
        for L in U.lessons:
            story += [PageBreak()] + textbook_lesson(t, L, U)       # every lesson starts on a fresh page
        story += study_guide(t, U)
    story += glossary(t, book)
    doc.multiBuild(story)


def glossary(t, book):
    words = {}
    for U in book.units:
        for w, d in U.vocab: words.setdefault(w, d)
        for L in U.lessons:
            for w, d in L.vocab: words.setdefault(w, d)
    out = [PageBreak(), Running("Glossary"), toc_heading("Glossary", t.h1, 0)]
    rows = [[P(f"<b>{w}</b>", t.cellb), P(d, t.cell)] for w, d in sorted(words.items(), key=lambda x: x[0].lower())]
    tb = Table(rows, colWidths=[1.7 * inch, W - 1.7 * inch])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE),
                            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    out.append(tb)
    return out


# ================================================================ WORKBOOK
def name_date(t):
    tb = Table([[P("Name", t.small), "", P("Date", t.small), ""]], colWidths=[0.45 * inch, 2.9 * inch, 0.4 * inch, 1.6 * inch])
    tb.setStyle(TableStyle([("LINEBELOW", (1, 0), (1, 0), 0.8, INK), ("LINEBELOW", (3, 0), (3, 0), 0.8, INK),
                            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    return tb


def work_space(t, w, h, grid=True):
    def fn(c, ww, hh):
        c.setStrokeColor(LINE); c.setLineWidth(0.6); c.roundRect(0, 0, ww, hh, 4, stroke=1, fill=0)
        if t.subject == "art":
            pass                                  # blank sketch box
        elif grid and t.subject == "math":
            c.setStrokeColor(GRID); c.setLineWidth(0.35); s = 12
            x = s
            while x < ww: c.line(x, 1, x, hh - 1); x += s
            y = s
            while y < hh: c.line(1, y, ww - 1, y); y += s
        elif not grid or t.subject != "math":
            c.setStrokeColor(GRID); y = hh - 22
            while y > 4: c.line(6, y, ww - 6, y); y -= 22
    return Draw(w, h, fn)


def answer_line(t, w):
    def fn(c, ww, hh):
        c.setStrokeColor(colors.HexColor("#CFC8BB")); c.setLineWidth(0.7); c.line(0, 4, ww, 4)
    return Draw(w, 22, fn)


def write_lines(t, w, n):
    def fn(c, ww, hh):
        c.setStrokeColor(colors.HexColor("#CFC8BB")); c.setLineWidth(0.6)
        for k in range(n): c.line(0, hh - 22 - k * 24, ww, hh - 22 - k * 24)
    return Draw(w, n * 24 + 4, fn)


def problem_cell(t, pr, num, w, show_answer=False):
    badge = Table([[P(f"<b>{num}</b>", ParagraphStyle("bd", parent=t.cell, textColor=t.on_main, alignment=TA_CENTER))]], colWidths=[18], rowHeights=[18])
    badge.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), t.main), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("ROUNDEDCORNERS", [9, 9, 9, 9])]))
    body = [P(pr.prompt, t.prob)]
    if pr.fig: body += [Spacer(1, 3), pr.fig(t), Spacer(1, 2)]
    if pr.choices:
        body.append(Spacer(1, 2))
        for k, ch in enumerate(pr.choices):
            body.append(P(f"<font name='BodySemi' color='#{t.accent.hexval()[2:]}'>{chr(65 + k)}</font>   {ch}", t.prob))
    inner_w = w - 26
    if pr.lines: body += [Spacer(1, 2), write_lines(t, inner_w, pr.lines)]
    elif pr.space: body += [Spacer(1, 3), work_space(t, inner_w, max(pr.space, 26))]
    elif not pr.choices and not pr.fig: body += [Spacer(1, 2), answer_line(t, inner_w if t.subject != "math" else min(inner_w, 170))]
    if show_answer: body.append(P(f"Answer: {pr.answer}", t.answer))
    tb = Table([[badge, body]], colWidths=[24, w - 24])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return tb


def section_head(t, title, letter=None):
    """Workbook section title with a colored part tab: [A] Warm-Up."""
    tag = chip(f"PART {letter}", t.main, t.on_main, 8) if letter else None
    h = P(title, ParagraphStyle("sh", parent=t.h3, spaceBefore=0, spaceAfter=0))
    if not tag: return h
    tb = Table([[tag, h]], colWidths=[tag._colWidths[0] + 8, W - tag._colWidths[0] - 8])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LINEBELOW", (0, 0), (-1, -1), 0.8, t.mid)]))
    return tb


def section_grid(t, sec, start, show_answer=False, letter=None):
    head = [section_head(t, sec.title, letter), Spacer(1, 4)]
    if sec.intro: head.append(P(f"<b>Directions:</b> {sec.intro}", ParagraphStyle("sdi", parent=t.body, fontName="BodyMed", textColor=t.dark)))
    out = []
    if getattr(sec, "passage", None) and not show_answer:
        out += [KeepTogether(head[:2] + [P("<b>First, read this passage.</b> Then answer the questions below it.", ParagraphStyle("rf", parent=t.body, fontName="BodyMed", textColor=t.dark)), Spacer(1, 2)]),
                passage_box(t, sec.passage), Spacer(1, 10)]
        head = head[2:]
    n = start; row = []; rows = []
    cols = sec.cols; cw = W / cols
    for pr in sec.problems:
        if pr.wide or cols == 1:
            if row: rows.append(row + [""] * (cols - len(row))); row = []
            rows.append(("wide", problem_cell(t, pr, n, W - 8, show_answer)))
        else:
            row.append(problem_cell(t, pr, n, cw - 10, show_answer))
            if len(row) == cols: rows.append(row); row = []
        n += 1
    if row: rows.append(row + [""] * (cols - len(row)))
    for i, r in enumerate(rows):
        if isinstance(r, tuple):
            f = r[1]
        else:
            f = Table([r], colWidths=[cw] * cols)
            f.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        out.append(KeepTogether(head + [f, Spacer(1, 10)]) if i == 0 else f)
        if i: out.append(Spacer(1, 10))
    return out, n


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def workbook_lesson(t, L, U=None):
    """Practice pages: banner, title, name and date, Today's Goal, a short What To Do list, then lettered parts."""
    parts = [s.title for s in L.practice]
    todo = [f"Read <b>Textbook Lesson {L.num}</b> first.",
            f"Do every part on these pages: " + ", ".join(f"<b>Part {LETTERS[i]}</b> {p}" for i, p in enumerate(parts)) + ".",
            "Show your thinking. Write final answers on the lines." if t.subject == "math" else "Answer in complete sentences unless a line asks for one word.",
            "Check your work with your teacher and fix any mistakes."]
    out = lesson_header(t, L, U, tag="PRACTICE", title_style=ParagraphStyle("wh", parent=t.h2, spaceBefore=0))
    out[-1] = toc_heading(f"Lesson {L.num}: {L.title}", ParagraphStyle("wh", parent=t.h2, spaceBefore=0), 1, running=f"Lesson {L.num} Practice · {L.title}")
    out += [name_date(t), Spacer(1, 8), goal_card(t, L, size=13), Spacer(1, 6), checklist(t, "WHAT TO DO", todo, IVORY), Spacer(1, 4)]
    n = 1
    for i, sec in enumerate(L.practice):
        part, n = section_grid(t, sec, n, letter=LETTERS[i])
        out += part
    return out


def check_banner(t, C, teacher=False):
    big = ParagraphStyle("cbn", fontName="BodyBold", fontSize=13, leading=16, textColor=WHITE)
    sm = ParagraphStyle("cbs", fontName="BodyMed", fontSize=9.5, leading=12, textColor=WHITE)
    right = ParagraphStyle("cbr", parent=sm, alignment=TA_RIGHT)
    left = [P(check_tag(C) + ("  ·  ANSWER KEY" if teacher else ""), big)]
    if C.date: left.append(P(f"Planned for {C.date}", sm))
    tb = Table([[left, P(f"About {C.minutes} minutes" if C.minutes else "", right)]], colWidths=[W * 0.6, W * 0.4])
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), HUNTER), ("ROUNDEDCORNERS", [6, 6, 6, 6]), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                            ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return tb


def check_pages(t, C, show_answer=False, teacher=False):
    out = [check_banner(t, C, teacher), Spacer(1, 8),
           toc_heading(C.title + (" — Answer Key" if teacher else ""), ParagraphStyle("ch", parent=t.h2, spaceBefore=0), 1, running=C.title)]
    if not teacher:
        out += [name_date(t), Spacer(1, 8)]
        todo = ["Work on your own. Don't use your textbook unless your teacher says you may.",
                "Read each question carefully. Show your thinking." if t.subject == "math" else "Read each passage and question carefully. Answer in complete sentences.",
                "When you finish, check that every question has an answer."]
        if C.kind == "test":
            todo.insert(1, f"This test has <b>{sum(p.points for s in C.sections for p in s.problems)} points</b>.")
        out += [checklist(t, "DIRECTIONS", todo, IVORY), Spacer(1, 4)]
    n = 1
    for i, sec in enumerate(C.sections):
        part, n = section_grid(t, sec, n, show_answer, letter=LETTERS[i] if len(C.sections) > 1 else None)
        out += part
    return out


def build_workbook(book, path):
    t = book.theme; doc = Doc(path, book, "workbook")
    story = [Spacer(1, 1)] + front_matter(t, book, doc, "workbook")
    for U in book.units:
        story += unit_opener(t, U, doc, "workbook")
        story += [P(f"Your practice pages for Unit {U.num}. Each lesson matches the same lesson number in your textbook.", t.body)]
        story += [vocab_panel(t, U.vocab, "Unit Vocabulary")]
        week_checks = {c.after: c for c in U.checks}
        for L in U.lessons:
            story += [PageBreak()] + workbook_lesson(t, L, U)
            if L.num in week_checks:
                story += [PageBreak()] + check_pages(t, week_checks[L.num])
        story += [PageBreak()] + check_pages(t, U.review)
        story += [PageBreak()] + check_pages(t, U.test)
    if book.subject == "data":
        story += answer_key_section(t, book, doc)
    doc.multiBuild(story)


def answer_key_section(t, book, doc):
    """Self-study answer key at the back of the workbook."""
    out = [NextPageTemplate("opener"), SetOpenerNum(doc, ""), PageBreak(), Running("Answer Key"), Spacer(1, 0.25 * inch),
           P("ANSWERS AND CODE SOLUTIONS", ParagraphStyle("ake", parent=t.eyebrow, textColor=t.on_main, fontSize=10)),
           toc_heading("Answer Key", ParagraphStyle("akh", parent=t.h1, textColor=t.on_main, fontSize=36, leading=40), 0),
           P("Try every problem before you look. Code solutions show one good way; yours may differ and still be right if the output matches.",
             ParagraphStyle("aks", parent=t.body, textColor=t.on_main, fontSize=13, leading=18)), SpaceTo(3.65 * inch), NextPageTemplate("body")]
    for U in book.units:
        out += [P(f"Unit {U.num}: {U.title}", t.h2)]
        week_checks = {c.after: c for c in U.checks}
        for L in U.lessons:
            out += problems_key(t, L.practice, f"Lesson {L.num}: {L.title}")
            if L.num in week_checks:
                out += check_teacher(t, week_checks[L.num])[1:]
        out += check_teacher(t, U.review)[1:] + check_teacher(t, U.test)[1:]
    return out


# ================================================================ TEACHER EDITION
def info_table(t, rows):
    data = [[P(f"<b>{k}</b>", t.cellb), P(v, t.cell)] for k, v in rows]
    tb = Table(data, colWidths=[1.25 * inch, W - 1.25 * inch])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, -1), t.wash),
                            ("BOX", (0, 0), (-1, -1), 0.8, t.main), ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return tb


def flow_table(t, flow):
    rows = [[P("Part", ParagraphStyle("fh", parent=t.cellb, textColor=WHITE)), P("Min", ParagraphStyle("fh2", parent=t.cellb, textColor=WHITE)),
             P("What to do and say", ParagraphStyle("fh3", parent=t.cellb, textColor=WHITE))]]
    for phase, mins, lines in flow:
        cell = []
        for ln in lines:
            if ln.startswith("Say:"):
                cell.append(P("<b>Say:</b> “" + ln[4:].strip() + "”", t.say))
            elif ln.startswith("Ask:"):
                cell.append(P("<b>Ask:</b> " + ln[4:].strip(), t.cell))
            elif ln.startswith("Listen for:"):
                cell.append(P("<i>Listen for:</i> " + ln[11:].strip(), t.cell))
            else:
                cell.append(P(ln, t.cell))
            cell.append(Spacer(1, 3))
        rows.append([P(f"<b>{phase}</b>", t.cellb), P(str(mins), t.cell), cell])
    tb = Table(rows, colWidths=[1.05 * inch, 0.4 * inch, W - 1.45 * inch], repeatRows=1)
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, 0), t.main),
                            ("BOX", (0, 0), (-1, -1), 0.8, t.main), ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
                            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, IVORY]),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return tb


def key_table(t, items, title):
    """items: list of (number, prompt, answer, note)"""
    out = [CondPageBreak(1.6 * inch), P(title, t.h3)]
    rows = [["#", "Question", "Answer"]]
    for num, prompt, ans, note in items:
        a = f"<font name='BodySemi' color='#{t.accent.hexval()[2:]}'>{ans}</font>" + (f"<br/><font size='8.5' color='#5F5B56'>{note}</font>" if note else "")
        rows.append([str(num), P(prompt, ParagraphStyle("kq", parent=t.cell, fontSize=9, leading=12.5)), P(a, t.cell)])
    out.append(table(t, rows, [0.35 * inch, W * 0.56, W - 0.35 * inch - W * 0.56], font_size=9))
    return out


def problems_key(t, sections, title):
    items = []; n = 1
    for s in sections:
        for pr in s.problems:
            prompt = pr.prompt + (" <i>(figure)</i>" if pr.fig else "")
            if pr.choices: prompt += "<br/>" + "  ".join(f"{chr(65 + k)}. {c}" for k, c in enumerate(pr.choices))
            items.append((n, prompt, pr.answer, pr.note)); n += 1
    return key_table(t, items, title)


def teacher_lesson(t, L, U=None):
    T = L.teacher
    out = lesson_header(t, L, U, tag="TEACHER PLAN", title_style=ParagraphStyle("th", parent=t.h1, fontSize=24, leading=28))
    out.append(info_table(t, [("Student goal", f"<b>{L.i_can}</b>"), ("Objective", T["objective"]), ("Standard", L.standard + " — " + T.get("standard_text", "")),
                              ("Date", L.date or "—"), ("Time", T.get("time", "About 50 minutes")),
                              ("Materials", T["materials"]), ("Get ready", T.get("prep", PREP[t.subject]))]))
    out += [Spacer(1, 8), P("Lesson Flow", t.h3), flow_table(t, T["flow"])]
    side = []
    if T.get("misconceptions"):
        side.append(panel([P("COMMON MISCONCEPTIONS", ParagraphStyle("mc", parent=t.eyebrow, textColor=FOREST))] + bullets(T["misconceptions"], t.bullet),
                          colors.HexColor("#FBF3DC"), left_bar=GOLD))
    if T.get("support") or T.get("extend"):
        dt = Table([[[P("SUPPORT", t.eyebrow)] + bullets(T.get("support", []), ParagraphStyle("b2", parent=t.bullet, fontSize=10, leading=14)),
                     [P("EXTEND", t.eyebrow)] + bullets(T.get("extend", []), ParagraphStyle("b3", parent=t.bullet, fontSize=10, leading=14))]],
                   colWidths=[W / 2, W / 2])
        dt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (0, 0), 0.6, LINE), ("BOX", (1, 0), (1, 0), 0.6, LINE),
                                ("BACKGROUND", (0, 0), (-1, -1), IVORY), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8)]))
        side.append(dt)
    for s in side: out += [Spacer(1, 8), s]
    # student lesson with answers
    out += [PageBreak(), chip(f"STUDENT LESSON {L.num}  ·  WITH ANSWERS", HUNTER), Spacer(1, 6)]
    out += textbook_lesson_compact(t, L)
    out += [Spacer(1, 8)] + problems_key(t, L.practice, f"Workbook Answer Key · Lesson {L.num}")
    return out


def textbook_lesson_compact(t, L):
    out = [P(f"Lesson {L.num}: {L.title}", t.h2), checklist(t, "STUDENT'S ASSIGNMENT", assignment_items(t, L), IVORY), Spacer(1, 6)]
    out.append(boxed(t, t.lab["explore"], [P(L.launch, t.boxt)], WHITE, border=t.mid)); out.append(Spacer(1, 6))
    out += render_blocks(t, L.learn, True)
    out.append(try_it_box(t, L, with_answers=True))
    return out


def unit_overview_teacher(t, U):
    out = [P(U.overview, t.body), P("Big ideas", t.h3)] + bullets(U.big_ideas, t.bullet)
    out += [P("Standards", t.h3), table(t, [["Code", "Standard"]] + [[a, b] for a, b in U.standards], [0.95 * inch, W - 0.95 * inch])]
    out += [P("What students should already know", t.h3)] + bullets(U.prior, t.bullet)
    out += [P("Materials for the unit", t.h3)] + bullets(U.materials, t.bullet)
    out += [P("Pacing calendar", t.h3)]
    rows = [["Week", "Day", "Lesson", "Title"]]
    for wk, items in U.weeks:
        for day, num, title in items: rows.append([wk, day, num, title])
    out.append(table(t, rows, [1.35 * inch, 0.95 * inch, 0.75 * inch, W - 3.05 * inch], font_size=9))
    if U.family_note: out += [Spacer(1, 8), panel([P("TEACHING THIS UNIT AT HOME", t.eyebrow), P(U.family_note, t.boxt)], SAGE_WASH, left_bar=HUNTER)]
    out += [Spacer(1, 8), vocab_panel(t, U.vocab, "Unit Vocabulary")]
    return out


def build_teacher(book, path):
    t = book.theme; doc = Doc(path, book, "teacher")
    story = [Spacer(1, 1)] + front_matter(t, book, doc, "teacher")
    for U in book.units:
        story += unit_opener(t, U, doc, "teacher") + unit_overview_teacher(t, U)
        week_checks = {c.after: c for c in U.checks}
        for L in U.lessons:
            story += [PageBreak()] + teacher_lesson(t, L, U)
            if L.num in week_checks:
                C = week_checks[L.num]
                story += [PageBreak()] + check_teacher(t, C)
        story += [PageBreak()] + check_teacher(t, U.review)
        story += [PageBreak()] + check_teacher(t, U.test)
    doc.multiBuild(story)


def check_teacher(t, C):
    out = [check_banner(t, C, teacher=True), Spacer(1, 8),
           toc_heading(C.title + " — Answer Key", ParagraphStyle("ch", parent=t.h2, spaceBefore=0), 1, running=C.title + " Key")]
    if C.teacher_note: out.append(P(C.teacher_note, t.body))
    out += problems_key(t, C.sections, "Answers")
    if C.rubric:
        out += [P("Scoring", t.h3), table(t, [["Score", "What it means / next step"]] + C.rubric, [1.2 * inch, W - 1.2 * inch])]
    return out
