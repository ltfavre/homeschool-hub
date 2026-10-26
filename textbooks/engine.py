"""VenvLearning textbook engine.

One content source (textbooks/content/<book>/unitNN.py) renders three books:
  textbook  - the student reading/teaching text (lessons, worked examples, Try It)
  workbook  - every question and activity, with space to write
  teacher   - plans, scripts, activity instructions, the student lessons, and all answer keys

Brand: DM Serif Display (headings), Outfit (body), IBM Plex Mono (numbers), ivory/hunter/gold
with the ink stripe signature. Subject colour: Math = red, ELA = blue.
"""
import math, os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily, stringWidth
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                Flowable, KeepTogether, PageBreak, CondPageBreak, NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, "fonts")
for name, file in [("Display", "DMSerifDisplay-Regular"), ("DisplayIt", "DMSerifDisplay-Italic"),
                   ("Body", "Outfit-Regular"), ("BodyMed", "Outfit-Medium"), ("BodySemi", "Outfit-SemiBold"),
                   ("BodyBold", "Outfit-Bold"), ("Mono", "IBMPlexMono-Regular"), ("MonoMed", "IBMPlexMono-Medium"),
                   ("MonoSemi", "IBMPlexMono-SemiBold")]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(F, file + ".ttf")))
registerFontFamily("Body", normal="Body", bold="BodySemi", italic="BodyMed", boldItalic="BodyBold")
registerFontFamily("Display", normal="Display", bold="Display", italic="DisplayIt", boldItalic="DisplayIt")
registerFontFamily("Mono", normal="Mono", bold="MonoSemi", italic="Mono", boldItalic="MonoSemi")

# ---------------------------------------------------------------- brand
HUNTER = colors.HexColor("#234638"); FOREST = colors.HexColor("#142B23"); INK = colors.HexColor("#171717")
IVORY = colors.HexColor("#FAF7F2"); GOLD = colors.HexColor("#D4AF37"); BLUSH = colors.HexColor("#E8BFC4")
SAGE = colors.HexColor("#A8B89F"); SAGE_WASH = colors.HexColor("#EEF2EA"); MUTED = colors.HexColor("#5F5B56")
LINE = colors.HexColor("#E6DFD2"); WHITE = colors.white; GRID = colors.HexColor("#E9E4DA")

SUBJECTS = {
    "math": dict(name="Mathematics", main=colors.HexColor("#A3322B"), dark=colors.HexColor("#6E1F1A"),
                 wash=colors.HexColor("#F8E9E6"), mid=colors.HexColor("#E2A39C")),
    "ela": dict(name="English Language Arts", main=colors.HexColor("#2C5A85"), dark=colors.HexColor("#1B3B59"),
                wash=colors.HexColor("#E7EEF6"), mid=colors.HexColor("#9DB8D4")),
}

PAGE_W, PAGE_H = letter
LM, RM, TM, BM = 1.0 * inch, 0.75 * inch, 0.85 * inch, 0.8 * inch   # wide left margin for 3-hole binders
W = PAGE_W - LM - RM


class Theme:
    def __init__(self, subject):
        s = SUBJECTS[subject]
        self.subject = subject; self.name = s["name"]
        self.main, self.dark, self.wash, self.mid = s["main"], s["dark"], s["wash"], s["mid"]
        base = dict(fontName="Body", textColor=INK)
        self.body = ParagraphStyle("body", fontSize=11.5, leading=17, spaceAfter=7, **base)
        self.small = ParagraphStyle("small", fontSize=9.5, leading=13, spaceAfter=3, fontName="Body", textColor=MUTED)
        self.tiny = ParagraphStyle("tiny", fontSize=8.5, leading=11, fontName="Body", textColor=MUTED)
        self.boxt = ParagraphStyle("boxt", fontSize=11, leading=16, spaceAfter=4, **base)
        self.cell = ParagraphStyle("cell", fontSize=10, leading=14, **base)
        self.cellb = ParagraphStyle("cellb", fontSize=10, leading=14, fontName="BodySemi", textColor=INK)
        self.prob = ParagraphStyle("prob", fontSize=11, leading=16, **base)
        self.eyebrow = ParagraphStyle("eyebrow", fontName="BodySemi", fontSize=8.5, leading=11, textColor=self.main, spaceAfter=3)
        self.h1 = ParagraphStyle("h1", fontName="Display", fontSize=30, leading=34, textColor=HUNTER, spaceAfter=6)
        self.h2 = ParagraphStyle("h2", fontName="Display", fontSize=20, leading=24, textColor=HUNTER, spaceBefore=8, spaceAfter=6)
        self.h3 = ParagraphStyle("h3", fontName="BodySemi", fontSize=13, leading=17, textColor=self.dark, spaceBefore=8, spaceAfter=4)
        self.h4 = ParagraphStyle("h4", fontName="BodySemi", fontSize=11, leading=15, textColor=HUNTER, spaceBefore=4, spaceAfter=2)
        self.ican = ParagraphStyle("ican", fontName="DisplayIt", fontSize=14, leading=19, textColor=self.dark, spaceAfter=8)
        self.bullet = ParagraphStyle("bullet", parent=self.body, leftIndent=16, bulletIndent=3, spaceAfter=3)
        self.say = ParagraphStyle("say", parent=self.cell, fontName="BodyMed", textColor=self.dark)
        self.answer = ParagraphStyle("answer", parent=self.cell, fontName="BodySemi", textColor=self.main)


# ---------------------------------------------------------------- helpers
def P(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return [Paragraph(t, style, bulletText="•") for t in items]


def panel(flowables, bg, border=None, pad=11, width=W, left_bar=None):
    t = Table([[flowables]], colWidths=[width])
    st = [("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), pad + (4 if left_bar else 0)),
          ("RIGHTPADDING", (0, 0), (-1, -1), pad), ("TOPPADDING", (0, 0), (-1, -1), pad - 3),
          ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 5)]
    if border: st.append(("BOX", (0, 0), (-1, -1), 0.8, border))
    if left_bar: st.append(("LINEBEFORE", (0, 0), (0, -1), 4, left_bar))
    t.setStyle(TableStyle(st))
    return t


class Draw(Flowable):
    """A flowable that calls fn(canvas, w, h)."""
    def __init__(self, w, h, fn):
        super().__init__(); self.w, self.h, self.fn = w, h, fn

    def wrap(self, aw, ah):
        return self.w, self.h

    def draw(self):
        self.canv.saveState(); self.fn(self.canv, self.w, self.h); self.canv.restoreState()


def centered(flow, width=W):
    t = Table([[flow]], colWidths=[width]); t.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"),
                                                                    ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return t


def text(c, x, y, s, font="Body", size=10, color=INK, align="l"):
    c.setFont(font, size); c.setFillColor(color)
    {"l": c.drawString, "c": c.drawCentredString, "r": c.drawRightString}[align](x, y, s)


def fmt(n):
    return f"{n:,}"


# ---------------------------------------------------------------- math figures
PLACES = ["Ones", "Tens", "Hundreds", "Thousands", "Ten Thousands", "Hundred Thousands", "Millions"]


def place_value_chart(theme, number=None, places=6, highlight=None, digits=None, width=W, label_periods=True):
    """Place-value chart. digits: optional explicit list (highest place first); highlight: place index from ones=0."""
    cols = places; cw = min(width / cols, 78); tw = cw * cols; h = 86 if label_periods else 66
    ds = list(str(number).rjust(cols)) if number is not None else (digits or [""] * cols)

    def fn(c, w, hh):
        x0 = (w - tw) / 2
        if label_periods:
            groups = [("ONES PERIOD", 0, min(3, cols)), ("THOUSANDS PERIOD", 3, min(6, cols)), ("MILLIONS", 6, cols)]
            for lab, a, b in groups:
                if a >= b: continue
                xa = x0 + (cols - b) * cw; xb = x0 + (cols - a) * cw
                c.setFillColor(theme.dark); c.rect(xa + 1, hh - 16, xb - xa - 2, 14, fill=1, stroke=0)
                text(c, (xa + xb) / 2, hh - 12.5, lab, "BodySemi", 7.5, WHITE, "c")
        top = hh - (20 if label_periods else 0)
        for i in range(cols):
            place = cols - 1 - i; x = x0 + i * cw
            hl = highlight is not None and place == highlight
            c.setFillColor(theme.wash if not hl else theme.mid); c.setStrokeColor(theme.main); c.setLineWidth(0.8)
            c.rect(x, top - 26, cw, 26, fill=1, stroke=1)
            words = PLACES[place].split(" ")
            if len(words) == 2:
                text(c, x + cw / 2, top - 11, words[0], "BodySemi", 7.6, theme.dark, "c")
                text(c, x + cw / 2, top - 21, words[1], "BodySemi", 7.6, theme.dark, "c")
            else:
                text(c, x + cw / 2, top - 16, words[0], "BodySemi", 8, theme.dark, "c")
            c.setFillColor(WHITE if not hl else theme.wash); c.rect(x, top - 64, cw, 38, fill=1, stroke=1)
            d = ds[i].strip() if i < len(ds) else ""
            text(c, x + cw / 2, top - 54, d, "MonoSemi", 22, theme.main if hl else INK, "c")
        # heavier period dividers
        c.setStrokeColor(INK); c.setLineWidth(1.6)
        for k in (3, 6):
            if k < cols:
                x = x0 + (cols - k) * cw; c.line(x, top, x, top - 64)
    return Draw(width, h, fn)


def base_ten_blocks(theme, th=0, hu=0, te=0, on=0, width=W, scale=1.0, labels=True):
    u = 4.2 * scale
    hh = 10 * u + 40

    def cube(c, x, y):
        s = 10 * u * 0.62; d = s * 0.35
        c.setStrokeColor(theme.dark); c.setLineWidth(0.6)
        c.setFillColor(theme.mid); c.rect(x, y, s, s, fill=1, stroke=1)
        p = c.beginPath(); p.moveTo(x, y + s); p.lineTo(x + d, y + s + d); p.lineTo(x + s + d, y + s + d); p.lineTo(x + s, y + s); p.close()
        c.setFillColor(theme.wash); c.drawPath(p, fill=1, stroke=1)
        p = c.beginPath(); p.moveTo(x + s, y); p.lineTo(x + s + d, y + d); p.lineTo(x + s + d, y + s + d); p.lineTo(x + s, y + s); p.close()
        c.setFillColor(theme.main); c.drawPath(p, fill=1, stroke=1)
        c.setStrokeColor(colors.Color(1, 1, 1, 0.5)); c.setLineWidth(0.3)
        for k in range(1, 10):
            c.line(x + k * s / 10, y, x + k * s / 10, y + s); c.line(x, y + k * s / 10, x + s, y + k * s / 10)
        return s + d

    def flat(c, x, y):
        c.setStrokeColor(theme.dark); c.setLineWidth(0.4); c.setFillColor(theme.wash)
        c.rect(x, y, 10 * u, 10 * u, fill=1, stroke=1)
        for k in range(1, 10):
            c.line(x + k * u, y, x + k * u, y + 10 * u); c.line(x, y + k * u, x + 10 * u, y + k * u)
        return 10 * u

    def rod(c, x, y):
        c.setStrokeColor(theme.dark); c.setLineWidth(0.4); c.setFillColor(theme.mid)
        c.rect(x, y, u, 10 * u, fill=1, stroke=1)
        for k in range(1, 10): c.line(x, y + k * u, x + u, y + k * u)
        return u

    def unit(c, x, y):
        c.setStrokeColor(theme.dark); c.setLineWidth(0.4); c.setFillColor(theme.main); c.rect(x, y, u, u, fill=1, stroke=1)

    def fn(c, w, h):
        y = 22; x = 4; groups = []
        if th:
            gx = x
            for i in range(th): x += cube(c, x, y) + 6
            groups.append((gx, x - 6, f"{th} thousand" + ("s" if th != 1 else "")))
            x += 14
        if hu:
            gx = x
            for i in range(hu):
                flat(c, x, y); x += 10 * u * 0.42
            x += 10 * u * 0.58
            groups.append((gx, x - 4, f"{hu} hundred" + ("s" if hu != 1 else "")))
            x += 12
        if te:
            gx = x
            for i in range(te): rod(c, x, y); x += u + 3
            groups.append((gx, x - 3, f"{te} ten" + ("s" if te != 1 else "")))
            x += 14
        if on:
            gx = x; yy = y
            for i in range(on):
                unit(c, x + (i % 3) * (u + 2.5), yy + (i // 3) * (u + 2.5))
            x += 3 * (u + 2.5)
            groups.append((gx, x, f"{on} one" + ("s" if on != 1 else "")))
        if labels:
            for a, b, lab in groups:
                text(c, (a + b) / 2, 6, lab, "BodyMed", 8.5, theme.dark, "c")
    return Draw(width, hh, fn)


def number_line(theme, start, end, step, label_step=None, points=(), width=W, height=70, mid_mark=None,
                hops=(), fmt_fn=fmt, tick_labels=True):
    """points: (value, label, color?) ; hops: (from, to, label) arcs above the line."""
    label_step = label_step or step

    def X(v, w):
        return 18 + (v - start) / (end - start) * (w - 36)

    def fn(c, w, h):
        y = 30
        c.setStrokeColor(INK); c.setLineWidth(1.2); c.line(8, y, w - 8, y)
        for s in (-1, 1):  # arrows
            xx = 8 if s < 0 else w - 8
            p = c.beginPath(); p.moveTo(xx, y); p.lineTo(xx - s * -6, y + 3.5); p.lineTo(xx - s * -6, y - 3.5); p.close()
            c.setFillColor(INK); c.drawPath(p, fill=1, stroke=0)
        n = round((end - start) / step)
        for k in range(n + 1):
            v = start + k * step; x = X(v, w)
            major = abs(((v - start) / label_step) - round((v - start) / label_step)) < 1e-9
            c.setLineWidth(1 if major else 0.6); c.line(x, y - (6 if major else 4), x, y + (6 if major else 4))
            if major and tick_labels: text(c, x, y - 17, fmt_fn(v), "Mono", 8.5, INK, "c")
        if mid_mark is not None:
            x = X(mid_mark, w); c.setStrokeColor(theme.main); c.setDash(2, 2); c.line(x, y - 10, x, y + 22); c.setDash()
            text(c, x, y + 25, "halfway " + fmt_fn(mid_mark), "BodySemi", 7.5, theme.main, "c")
        for a, b, lab in hops:
            xa, xb = X(a, w), X(b, w); c.setStrokeColor(theme.main); c.setLineWidth(1)
            p = c.beginPath(); p.moveTo(xa, y + 6); p.curveTo(xa, y + 30, xb, y + 30, xb, y + 6); c.drawPath(p, stroke=1, fill=0)
            text(c, (xa + xb) / 2, y + 27, lab, "BodySemi", 8, theme.main, "c")
        for pt in points:
            v, lab = pt[0], pt[1]; col = pt[2] if len(pt) > 2 else theme.main
            x = X(v, w); c.setFillColor(col); c.circle(x, y, 4, fill=1, stroke=0)
            if lab: text(c, x, y + 10, lab, "MonoSemi", 9, col, "c")
    return Draw(width, height, fn)


def column_arith(theme, a, b, op="+", show_answer=True, carries=None, size=17, width=None, answer_color=None):
    """Vertical algorithm with optional carry/borrow marks: carries = {column_from_right: 'text'}"""
    rows = [fmt(a), fmt(b)]
    res = a + b if op == "+" else a - b
    ans = fmt(res)
    n = max(len(r) for r in rows + [ans]) + 1
    cw = stringWidth("0", "Mono", size)
    wd = (n + 1) * cw + 10; hh = size * 4.3 + (10 if carries else 0)

    def fn(c, w, h):
        x_right = w - 4
        y = h - (size + (12 if carries else 4))
        if carries:
            for col, t in carries.items():
                x = x_right - (col + 0.5) * cw
                text(c, x, h - 10, t, "MonoMed", size * 0.55, theme.main, "c")
        for r in rows:
            text(c, x_right, y, r, "Mono", size, INK, "r"); y -= size * 1.15
        text(c, x_right - n * cw, y + size * 1.15, op, "Mono", size, INK, "l")
        c.setStrokeColor(INK); c.setLineWidth(1.2); c.line(x_right - n * cw, y + size * 0.85, x_right, y + size * 0.85)
        y -= size * 0.2
        if show_answer: text(c, x_right, y, ans, "MonoSemi", size, answer_color or theme.main, "r")
    return Draw(width or wd, hh, fn)


def bar_model(theme, parts, total_label=None, width=W * 0.8, height=62, unknown_part=None):
    """parts: list of (label, relative_size). total_label shown with a brace above."""
    tot = sum(p[1] for p in parts)

    def fn(c, w, h):
        x = 4; y = 8; bh = 24; inner = w - 8
        for i, (lab, size) in enumerate(parts):
            pw = inner * size / tot
            fill = theme.wash if i != unknown_part else WHITE
            c.setFillColor(fill); c.setStrokeColor(theme.dark); c.setLineWidth(1)
            if i == unknown_part: c.setDash(3, 2)
            c.rect(x, y, pw, bh, fill=1, stroke=1); c.setDash()
            text(c, x + pw / 2, y + 8, lab, "MonoSemi", 10, INK if i != unknown_part else theme.main, "c")
            x += pw
        if total_label:
            ty = y + bh + 8; c.setStrokeColor(theme.main); c.setLineWidth(1)
            c.line(4, ty, 4, ty + 6); c.line(w - 4, ty, w - 4, ty + 6); c.line(4, ty + 6, w - 4, ty + 6)
            text(c, w / 2, ty + 11, total_label, "MonoSemi", 10, theme.main, "c")
    return Draw(width, height, fn)


def ten_times_diagram(theme, width=W):
    def fn(c, w, h):
        labels = ["1", "10", "100", "1,000", "10,000", "100,000"]
        n = len(labels); bw = 66; gap = (w - n * bw) / (n - 1) if n > 1 else 0
        y = 12
        for i, lab in enumerate(labels):
            x = w - (i + 1) * bw - i * gap
            c.setFillColor(theme.wash); c.setStrokeColor(theme.main); c.roundRect(x, y, bw, 30, 5, fill=1, stroke=1)
            text(c, x + bw / 2, y + 10, lab, "MonoSemi", 12, INK, "c")
            if i < n - 1:
                xa = x - gap + 2; xb = x - 2
                c.setStrokeColor(theme.main); c.setLineWidth(1)
                p = c.beginPath(); p.moveTo(xb, y + 34); p.curveTo(xb - 4, y + 52, xa + 4, y + 52, xa, y + 34); c.drawPath(p)
                c.setFillColor(theme.main)
                p = c.beginPath(); p.moveTo(xa, y + 32); p.lineTo(xa - 3, y + 38); p.lineTo(xa + 4, y + 37); p.close(); c.drawPath(p, fill=1, stroke=0)
                text(c, (xa + xb) / 2, y + 50, "×10", "BodySemi", 8.5, theme.main, "c")
    return Draw(width, 70, fn)


def table(theme, rows, col_widths=None, header=True, width=W, zebra=True, styles=None, font_size=10):
    st = ParagraphStyle("t", fontName="Body", fontSize=font_size, leading=font_size * 1.4, textColor=INK)
    sth = ParagraphStyle("th", parent=st, fontName="BodySemi", textColor=WHITE)
    data = [[c if isinstance(c, Flowable) else Paragraph(str(c), sth if (header and r == 0) else st) for c in row]
            for r, row in enumerate(rows)]
    cw = col_widths or [width / len(rows[0])] * len(rows[0])
    t = Table(data, colWidths=cw, repeatRows=1 if header else 0)
    s = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (-1, -1), 0.8, theme.main),
         ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE), ("LEFTPADDING", (0, 0), (-1, -1), 6),
         ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]
    if header: s.append(("BACKGROUND", (0, 0), (-1, 0), theme.main))
    if zebra: s.append(("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [WHITE, theme.wash]))
    t.setStyle(TableStyle(s + (styles or [])))
    return t


# ---------------------------------------------------------------- content model
class Problem:
    """A question. answer: text shown in keys. space: writing room in points (workbook).
    choices: list for multiple choice. fig: callable(theme)->Flowable shown under the prompt.
    note: teacher note shown in the key. wide: take the full row in the workbook."""
    def __init__(self, prompt, answer, space=28, choices=None, fig=None, note=None, wide=False, lines=0, points=1):
        self.prompt, self.answer, self.space, self.choices = prompt, answer, space, choices
        self.fig, self.note, self.wide, self.lines, self.points = fig, note, wide, lines, points


class Section:
    def __init__(self, title, problems, intro=None, cols=2):
        self.title, self.problems, self.intro, self.cols = title, problems, intro, cols


# Learn blocks
class Text:
    def __init__(self, t): self.t = t
class Heading:
    def __init__(self, t): self.t = t
class Figure:
    def __init__(self, fn, caption=None): self.fn, self.caption = fn, caption
class KeyIdea:
    def __init__(self, t, title="Key Idea"): self.t, self.title = t, title
class WatchOut:
    def __init__(self, t): self.t = t
class Example:
    def __init__(self, title, problem, steps, answer, fig=None):
        self.title, self.problem, self.steps, self.answer, self.fig = title, problem, steps, answer, fig
class Bullets:
    def __init__(self, items): self.items = items
class Vocab:
    def __init__(self, items): self.items = items


class Lesson:
    def __init__(self, num, title, i_can, standard, vocab, launch, learn, try_it, practice, teacher,
                 date=None, summary=None):
        self.num, self.title, self.i_can, self.standard, self.vocab = num, title, i_can, standard, vocab
        self.launch, self.learn, self.try_it, self.practice, self.teacher = launch, learn, try_it, practice, teacher
        self.date, self.summary = date, summary


class Check:
    """Friday weekly check or unit test."""
    def __init__(self, title, sections, date=None, minutes=20, kind="check", rubric=None, teacher_note=None, after=None):
        self.title, self.sections, self.date, self.minutes, self.kind = title, sections, date, minutes, kind
        self.rubric, self.teacher_note, self.after = rubric, teacher_note, after


class Unit:
    def __init__(self, num, title, subtitle, overview, big_ideas, standards, vocab, prior, materials,
                 lessons, checks, review, test, real_world=None, family_note=None, weeks=None):
        self.__dict__.update(locals()); del self.__dict__["self"]


class Book:
    def __init__(self, subject, grade, title, units, year="2026–2027"):
        self.subject, self.grade, self.title, self.units, self.year = subject, grade, title, units, year
        self.theme = Theme(subject)


# ---------------------------------------------------------------- document
KIND_LABEL = {"textbook": "Student Textbook", "workbook": "Student Workbook", "teacher": "Teacher Edition"}


class Doc(BaseDocTemplate):
    def __init__(self, path, book, kind, **kw):
        super().__init__(path, pagesize=letter, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
                         title=f"{book.title} · {KIND_LABEL[kind]}", author="VenvLearning", **kw)
        self.book, self.kind, self.theme = book, kind, book.theme
        self.running = ""
        frame = Frame(LM, BM, W, PAGE_H - TM - BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cover", frames=[frame], onPage=self.cover_page),
                               PageTemplate(id="body", frames=[frame], onPage=self.body_page, onPageEnd=self.footer),
                               PageTemplate(id="opener", frames=[frame], onPage=self.opener_page, onPageEnd=self.footer)])

    def footer(self, c, doc):
        c.saveState(); text(c, LM, BM - 30, self.running, "Body", 8, MUTED); c.restoreState()

    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and getattr(f, "_toc", None) is not None:
            self.notify("TOCEntry", (f._toc[0], f._toc[1], self.page))
        if getattr(f, "_running", None) is not None:
            self.running = f._running

    def stripe(self, c, y, h=6):
        c.setFillColor(INK); x = 0
        while x < PAGE_W:
            c.rect(x, y, 3, h, fill=1, stroke=0); x += 6

    def body_page(self, c, doc):
        t = self.theme; c.saveState()
        c.setFillColor(t.main); c.rect(0, PAGE_H - 22, PAGE_W, 22, fill=1, stroke=0)
        self.stripe(c, PAGE_H - 28, 6)
        text(c, LM, PAGE_H - 15, f"VENVLEARNING  ·  GRADE {self.book.grade} {t.name.upper()}", "BodySemi", 7.5, WHITE)
        text(c, PAGE_W - RM, PAGE_H - 15, KIND_LABEL[self.kind].upper(), "BodySemi", 7.5, WHITE, "r")
        c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(LM, BM - 16, PAGE_W - RM, BM - 16)
        text(c, PAGE_W - RM, BM - 30, str(doc.page), "MonoSemi", 9, t.main, "r")
        if self.kind == "teacher":
            c.setFillColor(GOLD); c.rect(PAGE_W - 10, BM, 10, PAGE_H - TM - BM, fill=1, stroke=0)
        c.restoreState()

    def opener_page(self, c, doc):
        t = self.theme; c.saveState()
        c.setFillColor(t.main); c.rect(0, PAGE_H - 3.3 * inch, PAGE_W, 3.3 * inch, fill=1, stroke=0)
        c.setFillColor(t.dark); c.rect(0, PAGE_H - 3.3 * inch, PAGE_W, 0.18 * inch, fill=1, stroke=0)
        self.stripe(c, PAGE_H - 3.3 * inch - 8, 8)
        # faint big unit numeral
        c.setFillColor(colors.Color(1, 1, 1, 0.12)); c.setFont("Display", 250)
        c.drawRightString(PAGE_W - 0.4 * inch, PAGE_H - 3.05 * inch, str(getattr(self, "opener_num", "")))
        text(c, PAGE_W - RM, BM - 30, str(doc.page), "MonoSemi", 9, t.main, "r")
        c.restoreState()

    def cover_page(self, c, doc):
        t = self.theme; b = self.book; c.saveState()
        c.setFillColor(IVORY); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        c.setFillColor(t.main); c.rect(0, PAGE_H * 0.42, PAGE_W, PAGE_H * 0.58, fill=1, stroke=0)
        c.setFillColor(t.dark); c.rect(0, PAGE_H * 0.42, PAGE_W, 10, fill=1, stroke=0)
        self.stripe(c, PAGE_H * 0.42 - 10, 10)
        # decorative pattern: subject motif
        c.setStrokeColor(colors.Color(1, 1, 1, 0.13)); c.setLineWidth(1)
        if b.subject == "math":
            for i in range(14):
                for j in range(9):
                    x = 40 + i * 44; y = PAGE_H * 0.46 + j * 44
                    s = "+−×÷=%"[(i + j) % 6]
                    c.setFillColor(colors.Color(1, 1, 1, 0.10)); c.setFont("Display", 20); c.drawCentredString(x, y, s)
        else:
            for j in range(16):
                y = PAGE_H * 0.45 + j * 24
                c.line(30, y, PAGE_W - 30, y)
        text(c, LM, PAGE_H - 1.25 * inch, "VENVLEARNING", "BodySemi", 11, WHITE)
        c.setFillColor(GOLD); c.rect(LM, PAGE_H - 1.38 * inch, 54, 3, fill=1, stroke=0)
        text(c, LM, PAGE_H - 2.6 * inch, f"Grade {b.grade}", "Display", 34, BLUSH)
        text(c, LM, PAGE_H - 3.45 * inch, t.name if b.subject == "math" else "English", "Display", 64, WHITE)
        if b.subject == "ela": text(c, LM, PAGE_H - 4.25 * inch, "Language Arts", "Display", 64, WHITE)
        # kind badge
        lab = KIND_LABEL[self.kind].upper()
        bw = stringWidth(lab, "BodyBold", 12) + 34
        c.setFillColor(INK if self.kind != "teacher" else GOLD); c.roundRect(LM, PAGE_H * 0.42 + 34, bw, 30, 15, fill=1, stroke=0)
        text(c, LM + bw / 2, PAGE_H * 0.42 + 44.5, lab, "BodyBold", 12, WHITE if self.kind != "teacher" else INK, "c")
        # lower area
        text(c, LM, PAGE_H * 0.42 - 0.75 * inch, b.year + " School Year", "BodySemi", 13, HUNTER)
        y = PAGE_H * 0.42 - 1.15 * inch
        for u in b.units:
            text(c, LM, y, f"Unit {u.num}", "MonoSemi", 10, t.main); text(c, LM + 52, y, u.title, "Body", 11, INK); y -= 18
        if self.kind != "teacher":
            text(c, LM, 1.35 * inch, "This book belongs to", "Body", 10, MUTED)
            c.setStrokeColor(INK); c.setLineWidth(0.8); c.line(LM + 110, 1.33 * inch, LM + 330, 1.33 * inch)
        text(c, LM, 0.75 * inch, "A VenvLearning family homeschool curriculum", "Body", 9, MUTED)
        c.restoreState()


def toc_flowable(theme):
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc0", fontName="Display", fontSize=15, leading=20, textColor=HUNTER, spaceBefore=10, leftIndent=0),
        ParagraphStyle("toc1", fontName="Body", fontSize=10.5, leading=15, textColor=INK, leftIndent=18),
    ]
    toc.dotsMinLevel = 0
    return toc


def toc_heading(txt, style, level, running=None):
    p = Paragraph(txt, style); p._toc = (level, txt.replace("&amp;", "&") if False else txt)
    if running is not None: p._running = running
    return p


class Running(Flowable):
    """Zero-size marker that sets the running footer text."""
    def __init__(self, t): super().__init__(); self._running = t
    def wrap(self, aw, ah): return 0, 0
    def draw(self): pass


class SetOpenerNum(Flowable):
    def __init__(self, doc_ref, n): super().__init__(); self.doc_ref, self.n = doc_ref, n
    def wrap(self, aw, ah): self.doc_ref.opener_num = self.n; return 0, 0
    def draw(self): pass


# ---------------------------------------------------------------- multiplication / division figures
def parts_of(n):
    s = str(n); return [int(d) * 10 ** (len(s) - 1 - i) for i, d in enumerate(s) if d != "0"]


def area_model(theme, a, b, width=None, show_products=True, height=None):
    """Rectangle for a × b, split by the place-value parts of each factor (a across the top, b down the side)."""
    pa, pb = parts_of(a), parts_of(b)
    width = width or min(W, 120 + 110 * len(pa)); height = height or (40 + 46 * len(pb))

    def fn(c, w, h):
        x0, y_top = 40, h - 22; cw = (w - x0 - 6) / len(pa); rh = (y_top - 4) / len(pb)
        for i, x in enumerate(pa):
            text(c, x0 + (i + 0.5) * cw, y_top + 7, fmt(x), "MonoSemi", 10, theme.dark, "c")
        for j, y in enumerate(pb):
            text(c, x0 - 6, y_top - (j + 0.5) * rh - 4, fmt(y), "MonoSemi", 10, theme.dark, "r")
            for i, x in enumerate(pa):
                c.setFillColor(theme.wash if (i + j) % 2 == 0 else WHITE); c.setStrokeColor(theme.main); c.setLineWidth(1)
                c.rect(x0 + i * cw, y_top - (j + 1) * rh, cw, rh, fill=1, stroke=1)
                if show_products:
                    text(c, x0 + (i + 0.5) * cw, y_top - (j + 0.5) * rh - 4, fmt(x * y), "MonoSemi", 11, INK, "c")
    return Draw(width, height, fn)


def array_dots(theme, rows, cols, width=None, r=4.2, gap=13):
    width = width or cols * gap + 10; height = rows * gap + 8

    def fn(c, w, h):
        c.setFillColor(theme.main)
        for i in range(rows):
            for j in range(cols):
                c.circle(6 + j * gap, h - 6 - i * gap, r, fill=1, stroke=0)
    return Draw(width, height, fn)


def mult_layout(theme, a, b, mode="partial", show_answer=True, size=15, width=None):
    """Vertical multiplication. mode: 'partial' lists partial products with labels; 'standard' shows only the product;
    'blank' shows only the problem."""
    rows = []
    if mode == "partial":
        if b < 10:
            rows = [(b * p, f"{b} × {fmt(p)}") for p in reversed(parts_of(a))]
        else:
            for q in reversed(parts_of(b)):
                for p in reversed(parts_of(a)):
                    rows.append((q * p, f"{fmt(q)} × {fmt(p)}"))
    prod = a * b
    n = max(len(fmt(x)) for x in [a, b, prod] + [r[0] for r in rows]) + 1
    cw = stringWidth("0", "Mono", size)
    lab_w = 80 if rows else 0
    wd = width or (n + 1) * cw + 14 + lab_w
    line_h = size * 1.2
    hh = line_h * (2 + len(rows) + (1 if (show_answer and rows) or mode != "blank" else 1)) + 18

    def fn(c, w, h):
        xr = w - 4; y = h - size - 4
        text(c, xr, y, fmt(a), "Mono", size, INK, "r"); y -= line_h
        text(c, xr, y, fmt(b), "Mono", size, INK, "r"); text(c, xr - n * cw, y, "×", "Mono", size, INK, "l")
        c.setStrokeColor(INK); c.setLineWidth(1.1); c.line(xr - n * cw, y - size * 0.3, xr, y - size * 0.3); y -= line_h
        if mode == "blank": return
        for v, lab in rows:
            if show_answer:
                text(c, xr, y, fmt(v), "Mono", size, theme.dark, "r")
                text(c, xr - n * cw - 8, y + 1, lab, "Body", size * 0.55, MUTED, "r")
            y -= line_h
        if rows:
            c.line(xr - n * cw, y + size * 0.85, xr, y + size * 0.85)
        if show_answer: text(c, xr, y, fmt(prod), "MonoSemi", size, theme.main, "r")
    return Draw(wd, hh, fn)


def long_div(theme, dividend, divisor, show_answer=True, size=16, width=None):
    """Division bracket layout: quotient (and remainder) above dividend."""
    q, r = divmod(dividend, divisor)
    cw = stringWidth("0", "Mono", size); n = len(str(dividend))
    wd = width or (n + len(str(divisor)) + 6) * cw + 20; hh = size * 3.4

    def fn(c, w, h):
        x0 = 8 + len(str(divisor)) * cw + 8; y = h - size * 2.2
        text(c, x0 - 6, y, str(divisor), "Mono", size, INK, "r")
        c.setStrokeColor(INK); c.setLineWidth(1.2)
        p = c.beginPath(); p.moveTo(x0 - 3, y - size * 0.35); p.curveTo(x0 + 2, y, x0 + 2, y + size * 0.6, x0 - 1, y + size * 1.05); c.drawPath(p)
        c.line(x0 - 1, y + size * 1.05, x0 + (n + 0.6) * cw, y + size * 1.05)
        text(c, x0 + 3, y, str(dividend), "Mono", size, INK, "l")
        if show_answer:
            qs = str(q); text(c, x0 + 3 + (n - len(qs)) * cw, y + size * 1.3, qs + (f" R{r}" if r else ""), "MonoSemi", size, theme.main, "l")
    return Draw(wd, hh, fn)


def dot_groups(theme, groups, per, width=None):
    """Equal groups drawn as circles holding dots."""
    width = width or min(W, groups * 70 + 10); height = 66

    def fn(c, w, h):
        gw = (w - 10) / groups
        for g in range(groups):
            cx = 5 + gw * (g + 0.5); cy = h / 2
            c.setStrokeColor(theme.main); c.setFillColor(theme.wash); c.circle(cx, cy, min(gw / 2 - 4, 28), fill=1, stroke=1)
            for k in range(per):
                ang = 2 * math.pi * k / max(per, 1); rr = 0 if per == 1 else min(gw / 2 - 14, 16)
                c.setFillColor(theme.main); c.circle(cx + rr * math.cos(ang), cy + rr * math.sin(ang), 3.6, fill=1, stroke=0)
    return Draw(width, height, fn)
