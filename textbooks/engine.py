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
pdfmetrics.registerFont(TTFont("Sym", os.path.join(F, "DejaVuSans.ttf")))   # fallback for symbols the brand fonts lack
registerFontFamily("Body", normal="Body", bold="BodySemi", italic="BodyMed", boldItalic="BodyBold")
registerFontFamily("Display", normal="Display", bold="Display", italic="DisplayIt", boldItalic="DisplayIt")
registerFontFamily("Mono", normal="Mono", bold="MonoSemi", italic="Mono", boldItalic="MonoSemi")

import re as _re
from reportlab.platypus import Paragraph as _Paragraph
from fontTools.ttLib import TTFont as _FT
_BODY_CMAP = set(_FT(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "Outfit-Regular.ttf")).getBestCmap())
_SYM = _re.compile("([\u0370-\u03ff\u2070-\u209f\u2190-\u21ff\u2200-\u22ff\u25a0-\u25ff\u2600-\u27bf])")


def _sym(m):
    ch = m.group(1)
    return ch if ord(ch) in _BODY_CMAP else f'<font name="Sym">{ch}</font>'


class Paragraph(_Paragraph):
    """Paragraph that draws symbols missing from the brand fonts (○ △ ☐ ✓ → ≈) with DejaVu Sans."""
    def __init__(self, text, *a, **k):
        super().__init__(text if text is None else _SYM.sub(_sym, text), *a, **k)


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

LABELS = {
    "math": dict(explore="LET'S EXPLORE", example="WORKED EXAMPLE", answer="Answer", try_="TRY IT",
                 try_note="Work these in your notebook or on scrap paper. Then check with your teacher.", real="MATH IN REAL LIFE",
                 study="Study the <b>Worked Examples</b> step by step, and try the <b>Try It</b> problems."),
    "ela": dict(explore="GET READY", example="MODEL", answer="Model answer", try_="YOUR TURN",
                try_note="Answer in your notebook in complete sentences. Then check with your teacher.", real="WHY IT MATTERS",
                study="Read the <b>Model</b> boxes to see how a strong reader thinks, then answer the <b>Your Turn</b> questions."),
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
        self.lab = LABELS[subject]


# ---------------------------------------------------------------- helpers
def P(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return [Paragraph(t, style, bulletText="•") for t in items]


def panel(flowables, bg, border=None, pad=11, width=W, left_bar=None):
    """Shaded box. Long boxes are built one row per item so they can continue onto the next page."""
    if isinstance(flowables, list) and len(flowables) > 3:
        rows = [[flowables[:2]]] + [[f] for f in flowables[2:]]
        t = Table(rows, colWidths=[width])
        st = [("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), pad + (4 if left_bar else 0)),
              ("RIGHTPADDING", (0, 0), (-1, -1), pad), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
              ("TOPPADDING", (0, 0), (-1, 0), pad - 3), ("BOTTOMPADDING", (0, -1), (-1, -1), pad - 5)]
        if border: st.append(("BOX", (0, 0), (-1, -1), 0.8, border))
        if left_bar: st.append(("LINEBEFORE", (0, 0), (0, -1), 4, left_bar))
        t.setStyle(TableStyle(st))
        return t
    t = Table([[flowables]], colWidths=[width])
    st = [("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), pad + (4 if left_bar else 0)),
          ("RIGHTPADDING", (0, 0), (-1, -1), pad), ("TOPPADDING", (0, 0), (-1, -1), pad - 3),
          ("BOTTOMPADDING", (0, -1), (-1, -1), pad - 5)]
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
    if hops: height = max(height, 52 + 16 * len(hops))

    def X(v, w):
        return 18 + float(v - start) / float(end - start) * (w - 36)

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
        for i, (a, b, lab) in enumerate(hops):
            xa, xb = X(a, w), X(b, w); c.setStrokeColor(theme.main); c.setLineWidth(1); top = 30 + 16 * i
            p = c.beginPath(); p.moveTo(xa, y + 6); p.curveTo(xa, y + top, xb, y + top, xb, y + 6); c.drawPath(p, stroke=1, fill=0)
            _arrow(c, xb, y + 6, -math.pi / 2, s=5, color=theme.main)
            text(c, (xa + xb) / 2, y + top * 0.75 + 3, lab, "BodySemi", 8, theme.main, "c")
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
    def __init__(self, title, problems, intro=None, cols=2, passage=None):
        self.title, self.problems, self.intro, self.cols, self.passage = title, problems, intro, cols, passage


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
class Passage:
    """A reading passage printed with numbered paragraphs. paras: list of strings (a string starting with '>' is a
    poem/verse line block kept unnumbered)."""
    def __init__(self, title, paras, source=None, genre=None, numbered=True):
        self.title, self.paras, self.source, self.genre, self.numbered = title, paras, source, genre, numbered
class ReaderAssign:
    """'Read in your Reader' assignment: book, section (chapter), and what to notice while reading."""
    def __init__(self, book, section, focus=None, pages=None):
        self.book, self.section, self.focus, self.pages = book, section, focus, pages
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

    def beforeDocument(self):
        self.running = ""   # multiBuild runs several passes; don't carry the last footer into the front matter

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


def hundred_chart(theme, marked=(), circled=(), width=None, start=1, rows=10, cols=10, blank=False):
    width = width or 300; cell = width / cols; height = rows * cell + 4
    marked, circled = set(marked), set(circled)

    def fn(c, w, h):
        for i in range(rows):
            for j in range(cols):
                n = start + i * cols + j; x = j * cell; y = h - (i + 1) * cell - 2
                c.setFillColor(theme.mid if n in marked else WHITE); c.setStrokeColor(LINE); c.setLineWidth(0.6)
                c.rect(x, y, cell, cell, fill=1, stroke=1)
                if not blank: text(c, x + cell / 2, y + cell * 0.32, str(n), "Mono", cell * 0.36, INK, "c")
                if n in circled:
                    c.setStrokeColor(theme.dark); c.setLineWidth(1.2); c.circle(x + cell / 2, y + cell / 2, cell * 0.42, fill=0, stroke=1)
    return Draw(width, height, fn)


def shape_pattern(theme, shapes, width=None, size=26):
    """shapes: list of 'circle', 'square', 'triangle', 'star' or '?'"""
    width = width or len(shapes) * (size + 12) + 10; height = size + 12

    def fn(c, w, h):
        for i, s in enumerate(shapes):
            x = 6 + i * (size + 12); y = 6
            c.setStrokeColor(theme.dark); c.setFillColor(theme.mid); c.setLineWidth(1)
            if s == "circle": c.circle(x + size / 2, y + size / 2, size / 2, fill=1)
            elif s == "square": c.rect(x, y, size, size, fill=1)
            elif s == "triangle":
                p = c.beginPath(); p.moveTo(x, y); p.lineTo(x + size, y); p.lineTo(x + size / 2, y + size); p.close(); c.drawPath(p, fill=1)
            elif s == "star":
                p = c.beginPath()
                for k in range(10):
                    r = size / 2 if k % 2 == 0 else size / 5; a = math.pi / 2 + k * math.pi / 5
                    px, py = x + size / 2 + r * math.cos(a), y + size / 2 + r * math.sin(a)
                    p.moveTo(px, py) if k == 0 else p.lineTo(px, py)
                p.close(); c.setFillColor(GOLD); c.drawPath(p, fill=1)
            elif s == "?":
                c.setFillColor(WHITE); c.setDash(3, 2); c.rect(x, y, size, size, fill=1); c.setDash()
                text(c, x + size / 2, y + size * 0.3, "?", "BodySemi", size * 0.55, theme.main, "c")
    return Draw(width, height, fn)


# ---------------------------------------------------------------- fraction figures
def frac_label(c, x, y, n, d, size=10, color=INK, font="MonoSemi"):
    """Stacked fraction centred at x with its bar at y."""
    text(c, x, y + 2.5, str(n), font, size, color, "c")
    wbar = max(stringWidth(str(n), font, size), stringWidth(str(d), font, size)) + 3
    c.setStrokeColor(color); c.setLineWidth(0.8); c.line(x - wbar / 2, y, x + wbar / 2, y)
    text(c, x, y - size - 0.5, str(d), font, size, color, "c")


def fraction_bar(theme, n, d, width=None, height=26, label=True, shade_color=None, unit_labels=False):
    width = width or W * 0.75

    def fn(c, w, h):
        lw = 36 if label else 0; bw = w - lw - 4; pw = bw / d; y = (h - height) / 2
        for k in range(d):
            c.setFillColor((shade_color or theme.mid) if k < n else WHITE); c.setStrokeColor(theme.dark); c.setLineWidth(0.9)
            c.rect(2 + k * pw, y, pw, height, fill=1, stroke=1)
            if unit_labels and pw > 16: frac_label(c, 2 + (k + 0.5) * pw, y + height / 2 - 1, 1, d, 7.5, INK)
        if label: frac_label(c, w - lw / 2, y + height / 2 - 1, n, d, 11, theme.dark)
    return Draw(width, height + 8, fn)


def fraction_bars(theme, fracs, width=None, bar_h=22, gap=6, unit_labels=False):
    """A stack of bars of equal length to compare fractions. fracs: list of (n, d)."""
    width = width or W * 0.75; height = len(fracs) * (bar_h + gap) + 4

    def fn(c, w, h):
        lw = 36; bw = w - lw - 4
        for i, (n, d) in enumerate(fracs):
            y = h - (i + 1) * (bar_h + gap); pw = bw / d
            for k in range(d):
                c.setFillColor(theme.mid if k < n else WHITE); c.setStrokeColor(theme.dark); c.setLineWidth(0.8)
                c.rect(2 + k * pw, y, pw, bar_h, fill=1, stroke=1)
                if unit_labels and pw > 16: frac_label(c, 2 + (k + 0.5) * pw, y + bar_h / 2 - 1, 1, d, 7, INK)
            frac_label(c, w - lw / 2, y + bar_h / 2 - 1, n, d, 10.5, theme.dark)
    return Draw(width, height, fn)


def fraction_circle(theme, n, d, r=30, width=None):
    width = width or 2 * r + 10

    def fn(c, w, h):
        cx, cy = w / 2, h / 2
        for k in range(d):
            c.setFillColor(theme.mid if k < n else WHITE); c.setStrokeColor(theme.dark); c.setLineWidth(0.9)
            c.wedge(cx - r, cy - r, cx + r, cy + r, 90 - (k + 1) * 360 / d, 360 / d, fill=1, stroke=1)
    return Draw(width, 2 * r + 8, fn)


def frac_number_line(theme, d, whole_end=1, points=(), width=None, height=62, label_all=True, mixed=False):
    """Number line from 0 to whole_end split into d parts per whole. points: (n, label_or_None)."""
    width = width or W * 0.85

    def fn(c, w, h):
        y = 32; x0, x1 = 14, w - 14; c.setStrokeColor(INK); c.setLineWidth(1.2); c.line(x0, y, x1, y)
        total = d * whole_end
        for k in range(total + 1):
            x = x0 + (x1 - x0) * k / total; whole = k % d == 0
            c.setLineWidth(1.2 if whole else 0.7); c.line(x, y - (7 if whole else 5), x, y + (7 if whole else 5))
            if whole: text(c, x, y - 20, str(k // d), "MonoSemi", 10, INK, "c")
            elif label_all:
                if mixed and k > d: frac_label(c, x, y - 15, k, d, 7.5, MUTED)
                else: frac_label(c, x, y - 15, k, d, 7.5, MUTED)
        for p in points:
            k, lab = p[0], p[1]; x = x0 + (x1 - x0) * k / total
            c.setFillColor(theme.main); c.circle(x, y, 4, fill=1, stroke=0)
            if lab: text(c, x, y + 10, lab, "MonoSemi", 9, theme.main, "c")
    return Draw(width, height, fn)


def decimal_grid(theme, hundredths, size=110, tenths_only=False):
    """10×10 grid with `hundredths` squares shaded (or columns if tenths_only)."""
    def fn(c, w, h):
        s = size / 10; x0, y0 = 2, 2
        for i in range(10):
            for j in range(10):
                k = j * 10 + i
                c.setFillColor(theme.mid if k < hundredths else WHITE); c.setStrokeColor(theme.dark if tenths_only and False else LINE); c.setLineWidth(0.4)
                c.rect(x0 + j * s, y0 + (9 - i) * s, s, s, fill=1, stroke=1)
        c.setStrokeColor(theme.dark); c.setLineWidth(1); c.rect(x0, y0, size, size, fill=0, stroke=1)
        if tenths_only:
            for j in range(1, 10): c.line(x0 + j * s, y0, x0 + j * s, y0 + size)
    return Draw(size + 4, size + 4, fn)


def decimal_chart(theme, value=None, width=None, places=("Tens", "Ones", "Tenths", "Hundredths"), highlight=None):
    """Place-value chart with a decimal point column. value as string like '3.45' (digits fill from the point)."""
    width = width or 330
    whole_cols = [p for p in places if p in ("Thousands", "Hundreds", "Tens", "Ones")]
    frac_cols = [p for p in places if p in ("Tenths", "Hundredths")]
    w_digits, f_digits = ("", "")
    if value is not None:
        a, _, b = str(value).partition("."); w_digits, f_digits = a, b

    def fn(c, w, h):
        dot_w = 16; cw = (w - dot_w) / (len(whole_cols) + len(frac_cols)); top = h - 2; x = 0
        cols = [(p, "w", i) for i, p in enumerate(whole_cols)] + [(".", "dot", 0)] + [(p, "f", i) for i, p in enumerate(frac_cols)]
        for p, kind, i in cols:
            if kind == "dot":
                text(c, x + dot_w / 2, top - 52, ".", "MonoSemi", 26, theme.main, "c"); x += dot_w; continue
            hl = highlight == p
            c.setFillColor(theme.mid if hl else theme.wash); c.setStrokeColor(theme.main); c.setLineWidth(0.8)
            c.rect(x, top - 24, cw, 24, fill=1, stroke=1)
            text(c, x + cw / 2, top - 15.5, p, "BodySemi", 8, theme.dark, "c")
            c.setFillColor(WHITE); c.rect(x, top - 62, cw, 38, fill=1, stroke=1)
            if kind == "w":
                d = w_digits.rjust(len(whole_cols))[i].strip() if w_digits else ""
            else:
                d = f_digits[i] if i < len(f_digits) else ""
            text(c, x + cw / 2, top - 52, d, "MonoSemi", 21, theme.main if hl else INK, "c")
            x += cw
    return Draw(width, 66, fn)


def money(theme, dollars=0, quarters=0, dimes=0, nickels=0, pennies=0, width=None):
    """Simple drawing of bills and coins."""
    items = [("$1", 1)] * dollars + [("25¢", 2)] * quarters + [("10¢", 3)] * dimes + [("5¢", 4)] * nickels + [("1¢", 5)] * pennies
    natural = 8 + sum(64 if k == 1 else 34 for _, k in items)
    width = width or min(W, natural)
    scale = min(1.0, width / natural)

    def fn(c, w, h):
        c.scale(scale, scale); x = 4
        for lab, k in items:
            if k == 1:
                c.setFillColor(colors.HexColor("#DCE8D5")); c.setStrokeColor(HUNTER); c.roundRect(x, 6, 58, 28, 3, fill=1, stroke=1)
                text(c, x + 29, 15, "$1", "BodySemi", 11, HUNTER, "c"); x += 64
            else:
                r = {2: 14, 3: 10.5, 4: 12, 5: 11}[k]
                c.setFillColor(colors.HexColor("#E9E6E0") if k != 5 else colors.HexColor("#E7C3A5")); c.setStrokeColor(MUTED)
                c.circle(x + 15, 20, r, fill=1, stroke=1); text(c, x + 15, 17, lab, "BodySemi", 7, INK, "c"); x += 34
    return Draw(width, 40 * scale + 2, fn)


# ---------------------------------------------------------------- geometry figures
def _arrow(c, x, y, ang, s=7, color=INK):
    c.setFillColor(color)
    p = c.beginPath(); p.moveTo(x, y)
    p.lineTo(x - s * math.cos(ang - 0.4), y - s * math.sin(ang - 0.4)); p.lineTo(x - s * math.cos(ang + 0.4), y - s * math.sin(ang + 0.4)); p.close()
    c.drawPath(p, fill=1, stroke=0)


def _dot(c, x, y, lab=None, color=INK, dx=0, dy=8):
    c.setFillColor(color); c.circle(x, y, 2.6, fill=1, stroke=0)
    if lab: text(c, x + dx, y + dy, lab, "BodySemi", 10, color, "c")


def line_kind(theme, kind, labels=("A", "B"), width=170, height=46):
    """kind: point, segment, ray, line."""
    def fn(c, w, h):
        y = h / 2 - 4; x1, x2 = 22, w - 22
        c.setStrokeColor(theme.dark); c.setLineWidth(1.6)
        if kind == "point": _dot(c, w / 2, y, labels[0], theme.dark); return
        c.line(x1, y, x2, y)
        if kind in ("ray", "line"): _arrow(c, x2 + 6, y, 0, color=theme.dark)
        if kind == "line": _arrow(c, x1 - 6, y, math.pi, color=theme.dark)
        _dot(c, x1 + (14 if kind == "line" else 0), y, labels[0], theme.dark)
        _dot(c, x2 - (14 if kind in ("ray", "line") else 0), y, labels[1], theme.dark)
    return Draw(width, height, fn)


def line_pair(theme, kind, width=170, height=80):
    """kind: parallel, perpendicular, intersecting."""
    def fn(c, w, h):
        c.setStrokeColor(theme.dark); c.setLineWidth(1.6); cx, cy = w / 2, h / 2
        def L(x1, y1, x2, y2):
            c.line(x1, y1, x2, y2); a = math.atan2(y2 - y1, x2 - x1)
            _arrow(c, x2 + 5 * math.cos(a), y2 + 5 * math.sin(a), a, color=theme.dark); _arrow(c, x1 - 5 * math.cos(a), y1 - 5 * math.sin(a), a + math.pi, color=theme.dark)
        if kind == "parallel": L(16, cy + 16, w - 16, cy + 16); L(16, cy - 16, w - 16, cy - 16)
        elif kind == "perpendicular":
            L(16, cy, w - 16, cy); L(cx, 10, cx, h - 10)
            c.setLineWidth(1); c.rect(cx, cy, 9, 9, fill=0, stroke=1)
        else: L(20, 12, w - 20, h - 12); L(20, h - 22, w - 20, 22)
    return Draw(width, height, fn)


def angle_fig(theme, deg, width=170, height=None, label=None, show=True, arm=None, start=0, ray_labels=None):
    height = height or (60 if deg <= 90 else 80 if deg < 180 else 60)
    arm = arm or 70

    def fn(c, w, h):
        vx = w / 2 - (arm / 2 if deg <= 90 else 0); vy = 14 if deg <= 180 else h / 2
        a0 = math.radians(start); a1 = math.radians(start + deg)
        c.setStrokeColor(theme.dark); c.setLineWidth(1.8)
        for a in (a0, a1):
            x2, y2 = vx + arm * math.cos(a), vy + arm * math.sin(a); c.line(vx, vy, x2, y2); _arrow(c, x2 + 4 * math.cos(a), y2 + 4 * math.sin(a), a, color=theme.dark)
        _dot(c, vx, vy, None, theme.dark)
        if deg == 90:
            c.setLineWidth(1); s = 10
            p = c.beginPath(); p.moveTo(vx + s * math.cos(a0), vy + s * math.sin(a0)); p.lineTo(vx + s * math.cos(a0) + s * math.cos(a1), vy + s * math.sin(a0) + s * math.sin(a1)); p.lineTo(vx + s * math.cos(a1), vy + s * math.sin(a1)); c.drawPath(p)
        elif deg > 0:
            c.setStrokeColor(theme.main); c.setLineWidth(1.2); r = 18
            c.arc(vx - r, vy - r, vx + r, vy + r, start, deg)
        if show:
            am = math.radians(start + deg / 2); text(c, vx + 34 * math.cos(am), vy + 34 * math.sin(am) - 3, label if label is not None else f"{deg}°", "MonoSemi", 9.5, theme.main, "c")
    return Draw(width, height, fn)


def polygon_fig(theme, pts, width=150, height=110, labels=None, right_angles=(), sym=None, ticks=None, fill=True, edge_labels=None):
    """pts: list of (x, y) in 0..1 coordinates. right_angles: vertex indexes. sym: ((x1,y1),(x2,y2)) dashed symmetry line.
    ticks: list of (edge_index, count) for equal-side marks."""
    def fn(c, w, h):
        P_ = [(10 + x * (w - 20), 10 + y * (h - 20)) for x, y in pts]
        p = c.beginPath(); p.moveTo(*P_[0])
        for q in P_[1:]: p.lineTo(*q)
        p.close(); c.setStrokeColor(theme.dark); c.setLineWidth(1.6); c.setFillColor(theme.wash); c.drawPath(p, fill=1 if fill else 0, stroke=1)
        for i in right_angles:
            a, b, d = P_[i], P_[i - 1], P_[(i + 1) % len(P_)]
            u = [(b[0] - a[0]), (b[1] - a[1])]; v = [(d[0] - a[0]), (d[1] - a[1])]
            nu = math.hypot(*u); nv = math.hypot(*v); s = 9
            u = [u[0] / nu * s, u[1] / nu * s]; v = [v[0] / nv * s, v[1] / nv * s]
            c.setLineWidth(0.9); q = c.beginPath(); q.moveTo(a[0] + u[0], a[1] + u[1]); q.lineTo(a[0] + u[0] + v[0], a[1] + u[1] + v[1]); q.lineTo(a[0] + v[0], a[1] + v[1]); c.drawPath(q)
        for e, n in (ticks or []):
            a, b = P_[e], P_[(e + 1) % len(P_)]; mx_, my_ = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            ang = math.atan2(b[1] - a[1], b[0] - a[0]) + math.pi / 2
            for k in range(n):
                off = (k - (n - 1) / 2) * 4; ux, uy = math.cos(ang - math.pi / 2) * off, math.sin(ang - math.pi / 2) * off
                c.setLineWidth(1); c.line(mx_ + ux - 4 * math.cos(ang), my_ + uy - 4 * math.sin(ang), mx_ + ux + 4 * math.cos(ang), my_ + uy + 4 * math.sin(ang))
        if sym:
            (x1, y1), (x2, y2) = sym; c.setStrokeColor(theme.main); c.setDash(4, 3); c.setLineWidth(1.3)
            c.line(10 + x1 * (w - 20), 10 + y1 * (h - 20), 10 + x2 * (w - 20), 10 + y2 * (h - 20)); c.setDash()
        if labels:
            cx = sum(x for x, _ in P_) / len(P_); cy = sum(y for _, y in P_) / len(P_)
            for (x, y), lab in zip(P_, labels):
                dx, dy = x - cx, y - cy; d = math.hypot(dx, dy) or 1
                text(c, x + dx / d * 9, y + dy / d * 9 - 3, lab, "BodySemi", 9, theme.dark, "c")
        if edge_labels:
            cx = sum(x for x, _ in P_) / len(P_); cy = sum(y for _, y in P_) / len(P_)
            for i, lab in enumerate(edge_labels):
                if not lab: continue
                a, b = P_[i], P_[(i + 1) % len(P_)]; mx_, my_ = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
                nx, ny = -(b[1] - a[1]), b[0] - a[0]; d = math.hypot(nx, ny) or 1; nx, ny = nx / d, ny / d
                if (mx_ - cx) * nx + (my_ - cy) * ny < 0: nx, ny = -nx, -ny
                text(c, mx_ + nx * 10, my_ + ny * 10 - 3, lab, "Mono", 8.5, INK, "c")
    return Draw(width, height, fn)


def protractor_fig(theme, deg, width=260):
    """A protractor reading an angle of `deg` from the right-hand zero."""
    R = width / 2 - 16

    def fn(c, w, h):
        cx, cy = w / 2, 14
        c.setFillColor(colors.Color(theme.wash.red, theme.wash.green, theme.wash.blue, 0.7)); c.setStrokeColor(theme.dark); c.setLineWidth(1)
        c.wedge(cx - R, cy - R, cx + R, cy + R, 0, 180, fill=1, stroke=1)
        for k in range(0, 181, 5):
            a = math.radians(k); L = 10 if k % 10 == 0 else 5
            c.setLineWidth(0.8 if k % 10 == 0 else 0.5); c.line(cx + R * math.cos(a), cy + R * math.sin(a), cx + (R - L) * math.cos(a), cy + (R - L) * math.sin(a))
            if k % 30 == 0:
                text(c, cx + (R - 20) * math.cos(a), cy + (R - 20) * math.sin(a) - 3, str(k), "Mono", 7.5, INK, "c")
        c.setStrokeColor(theme.main); c.setLineWidth(2)
        c.line(cx, cy, cx + (R + 10), cy); a = math.radians(deg); c.line(cx, cy, cx + (R + 10) * math.cos(a), cy + (R + 10) * math.sin(a))
        _dot(c, cx, cy, None, theme.main)
    return Draw(width, R + 30, fn)


def line_plot(theme, values, lo, hi, d, width=None, title=None, unit=""):
    """values: list of Fractions; axis from lo to hi in steps of 1/d."""
    from fractions import Fraction as _F
    width = width or W * 0.8
    counts = {}
    for v in values: counts[_F(v)] = counts.get(_F(v), 0) + 1
    tallest = max(counts.values()) if counts else 1
    height = 46 + tallest * 13 + (14 if title else 0)

    def fn(c, w, h):
        y = 30; x0, x1 = 18, w - 18; c.setStrokeColor(INK); c.setLineWidth(1.2); c.line(x0, y, x1, y)
        n = int((_F(hi) - _F(lo)) * d)
        for k in range(n + 1):
            v = _F(lo) + _F(k, d); x = x0 + (x1 - x0) * k / n; c.setLineWidth(1); c.line(x, y - 5, x, y + 5)
            if v.denominator == 1: text(c, x, y - 18, str(v.numerator), "MonoSemi", 9, INK, "c")
            else:
                whole = v.numerator // v.denominator; num = v.numerator % v.denominator
                lab_x = x
                if whole: text(c, x - 6, y - 21, str(whole), "MonoSemi", 8.5, INK, "c"); lab_x = x + 4
                frac_label(c, lab_x, y - 14, num, v.denominator, 6.8, MUTED)
            for j in range(counts.get(v, 0)):
                text(c, x, y + 9 + j * 13, "×", "BodySemi", 13, theme.main, "c")
        if title: text(c, w / 2, h - 10, title, "BodySemi", 9, theme.dark, "c")
    return Draw(width, height, fn)


def rect_fig(theme, l, w, unit="", grid=False, width=None, height=None, label_l=None, label_w=None, max_w=None):
    """Rectangle l × w with side labels; grid draws unit squares (only for small sizes)."""
    max_w = max_w or 200
    s = min(max_w / l, 90 / w, 26)
    rw, rh = l * s, w * s
    width = width or rw + 70; height = height or rh + 40

    def fn(c, ww, hh):
        x0 = (ww - rw) / 2; y0 = 18
        c.setFillColor(theme.wash); c.setStrokeColor(theme.dark); c.setLineWidth(1.4); c.rect(x0, y0, rw, rh, fill=1, stroke=1)
        if grid:
            c.setStrokeColor(theme.mid); c.setLineWidth(0.5)
            for i in range(1, int(l)): c.line(x0 + i * s, y0, x0 + i * s, y0 + rh)
            for j in range(1, int(w)): c.line(x0, y0 + j * s, x0 + rw, y0 + j * s)
        lt = label_l if label_l is not None else f"{l} {unit}".strip(); wt = label_w if label_w is not None else f"{w} {unit}".strip()
        text(c, x0 + rw / 2, y0 - 13, lt, "MonoSemi", 9.5, theme.dark, "c")
        text(c, x0 + rw + 5, y0 + rh / 2 - 3, wt, "MonoSemi", 9.5, theme.dark, "l")
    return Draw(width, height, fn)


def l_shape(theme, a, b, cdim, d, unit="", width=220, height=120):
    """L-shaped figure: full width a, full height b; top part width cdim, bottom part height d."""
    def draw(c, ww, hh):
        s = min((ww - 70) / a, (hh - 36) / b); x0 = 20; y0 = 18
        pts = [(0, 0), (a, 0), (a, d), (cdim, d), (cdim, b), (0, b)]
        p = c.beginPath(); p.moveTo(x0, y0)
        for x, y in pts[1:]: p.lineTo(x0 + x * s, y0 + y * s)
        p.close(); c.setFillColor(theme.wash); c.setStrokeColor(theme.dark); c.setLineWidth(1.4); c.drawPath(p, fill=1, stroke=1)
        def lab(x, y, t_, al="c"): text(c, x, y, t_, "MonoSemi", 9, theme.dark, al)
        lab(x0 + a * s / 2, y0 - 13, f"{a} {unit}".strip()); lab(x0 - 4, y0 + b * s / 2, f"{b} {unit}".strip(), "r")
        lab(x0 + cdim * s / 2, y0 + b * s + 4, f"{cdim} {unit}".strip()); lab(x0 + a * s + 4, y0 + d * s / 2 - 3, f"{d} {unit}".strip(), "l")
    return Draw(width, height, draw)


class SpaceTo(Flowable):
    """Vertical space that ends at a fixed distance from the top of the page."""
    def __init__(self, from_top):
        super().__init__(); self.from_top = from_top

    def wrap(self, aw, ah):
        self.h = max(0, ah - (PAGE_H - self.from_top - BM)); return aw, self.h

    def draw(self): pass


# ---------------------------------------------------------------- grade 7 figures
def sgn(n):
    """Format a number with a true minus sign."""
    s = f"{n:,}" if isinstance(n, int) else str(n)
    return s.replace("-", "−")


def coord_graph(theme, xmax, ymax, xstep=1, ystep=1, points=(), lines=(), width=220, height=200, xlabel="x", ylabel="y",
                xmin=0, ymin=0, label_every=None, ylabel_every=None, point_labels=True):
    """Coordinate grid. points: (x, y, label). lines: list of (slope, intercept) or [(x1,y1),(x2,y2)]."""
    def fn(c, w, h):
        L, B, R_, T = 30, 24, 10, 10
        gw, gh = w - L - R_, h - B - T
        X = lambda x: L + (x - xmin) / (xmax - xmin) * gw
        Y = lambda y: B + (y - ymin) / (ymax - ymin) * gh
        c.setStrokeColor(GRID); c.setLineWidth(0.5)
        k = xmin
        while k <= xmax + 1e-9: c.line(X(k), B, X(k), B + gh); k += xstep
        k = ymin
        while k <= ymax + 1e-9: c.line(L, Y(k), L + gw, Y(k)); k += ystep
        c.setStrokeColor(INK); c.setLineWidth(1.2)
        x0 = X(0) if xmin <= 0 <= xmax else L; y0 = Y(0) if ymin <= 0 <= ymax else B
        c.line(x0, B, x0, B + gh); c.line(L, y0, L + gw, y0)
        le = label_every or xstep; lye = ylabel_every or ystep
        k = xmin
        while k <= xmax + 1e-9:
            if abs(round(k / le) * le - k) < 1e-9: text(c, X(k), y0 - 11, sgn(int(k)) if float(k).is_integer() else str(k), "Mono", 7, INK, "c")
            k += xstep
        k = ymin
        while k <= ymax + 1e-9:
            if abs(round(k / lye) * lye - k) < 1e-9 and k != 0: text(c, x0 - 4, Y(k) - 2.5, sgn(int(k)) if float(k).is_integer() else str(k), "Mono", 7, INK, "r")
            k += ystep
        text(c, L + gw, y0 - 20, xlabel, "BodySemi", 8, theme.dark, "r")
        c.saveState(); c.translate(9, B + gh / 2); c.rotate(90); text(c, 0, 0, ylabel, "BodySemi", 8, theme.dark, "c"); c.restoreState()
        c.setStrokeColor(theme.main); c.setLineWidth(1.6)
        for ln in lines:
            if isinstance(ln, tuple) and len(ln) == 2 and not isinstance(ln[0], tuple):
                m, b = ln; xa, xb = xmin, xmax
                ya, yb = m * xa + b, m * xb + b
                if yb > ymax: xb = (ymax - b) / m; yb = ymax
                c.line(X(xa), Y(ya), X(xb), Y(yb))
            else:
                (x1, y1), (x2, y2) = ln; c.line(X(x1), Y(y1), X(x2), Y(y2))
        for pt in points:
            x, y = pt[0], pt[1]; c.setFillColor(theme.main); c.circle(X(x), Y(y), 3, fill=1, stroke=0)
            if point_labels and len(pt) > 2 and pt[2]: text(c, X(x) + 5, Y(y) + 4, pt[2], "MonoSemi", 7.5, theme.dark, "l")
    return Draw(width, height, fn)


def double_line(theme, top, bottom, top_label, bottom_label, width=None, blanks=()):
    """Double number line. top/bottom: lists of values (strings or numbers). blanks: indexes shown as '?' on the bottom."""
    width = width or W * 0.85

    def fn(c, w, h):
        n = len(top); x0, x1 = 70, w - 14
        for y, vals, lab in ((h - 18, top, top_label), (16, bottom, bottom_label)):
            c.setStrokeColor(INK); c.setLineWidth(1.2); c.line(x0, y, x1, y)
            text(c, 4, y - 3, lab, "BodySemi", 8.5, theme.dark, "l")
            for i, v in enumerate(vals):
                x = x0 + (x1 - x0) * i / (n - 1); c.line(x, y - 5, x, y + 5)
                s = "?" if (vals is bottom and i in blanks) else (sgn(v) if isinstance(v, int) else str(v))
                text(c, x, y + (8 if y > h / 2 else -15), s, "MonoSemi", 9, theme.main if s == "?" else INK, "c")
    return Draw(width, 62, fn)


def percent_bar(theme, pct, whole_label=None, part_label=None, width=None, marks=10):
    width = width or W * 0.8

    def fn(c, w, h):
        x0, x1, y = 6, w - 6, 16; bw = x1 - x0
        c.setFillColor(WHITE); c.setStrokeColor(theme.dark); c.setLineWidth(1); c.rect(x0, y, bw, 22, fill=1, stroke=1)
        c.setFillColor(theme.mid); c.rect(x0, y, bw * min(pct, 100) / 100, 22, fill=1, stroke=0)
        c.setStrokeColor(theme.dark); c.rect(x0, y, bw, 22, fill=0, stroke=1)
        for k in range(marks + 1):
            x = x0 + bw * k / marks; c.setLineWidth(0.5); c.line(x, y, x, y + 22)
            text(c, x, y - 11, f"{100 * k // marks}%", "Mono", 7, MUTED, "c")
        if part_label: text(c, x0 + bw * min(pct, 100) / 200, y + 7, part_label, "MonoSemi", 9, INK, "c")
        if whole_label: text(c, x1, y + 28, whole_label, "BodySemi", 8.5, theme.dark, "r")
    return Draw(width, 58, fn)


def chips(theme, pos, neg, zero_pairs=0, width=None, r=8):
    """Integer chips: pos (+) and neg (−); zero_pairs are circled together."""
    n = pos + neg; width = width or min(W, 20 + n * (2 * r + 6))

    def fn(c, w, h):
        x = 8; cy = h / 2
        def chip(x, s):
            c.setFillColor(theme.mid if s > 0 else colors.HexColor("#DCE6EF")); c.setStrokeColor(theme.dark if s > 0 else colors.HexColor("#2C5A85")); c.setLineWidth(1)
            c.circle(x + r, cy, r, fill=1, stroke=1); text(c, x + r, cy - 4, "+" if s > 0 else "−", "BodyBold", 11, INK, "c")
        for i in range(zero_pairs):
            chip(x, 1); chip(x + 2 * r + 2, -1)
            c.setStrokeColor(MUTED); c.setDash(2, 2); c.roundRect(x - 3, cy - r - 4, 4 * r + 8, 2 * r + 8, r, fill=0, stroke=1); c.setDash()
            x += 4 * r + 14
        for i in range(pos - zero_pairs): chip(x, 1); x += 2 * r + 5
        for i in range(neg - zero_pairs): chip(x, -1); x += 2 * r + 5
    return Draw(width, 2 * r + 16, fn)


def dot_plot(theme, values, lo, hi, step=1, width=None, title=None, label_every=1):
    width = width or W * 0.8
    counts = {}
    for v in values: counts[v] = counts.get(v, 0) + 1
    tallest = max(counts.values()) if counts else 1
    height = 40 + tallest * 11 + (14 if title else 0)

    def fn(c, w, h):
        y = 26; x0, x1 = 14, w - 14; c.setStrokeColor(INK); c.setLineWidth(1.1); c.line(x0, y, x1, y)
        n = round((hi - lo) / step)
        for k in range(n + 1):
            v = lo + k * step; x = x0 + (x1 - x0) * k / n; c.line(x, y - 4, x, y + 4)
            if k % label_every == 0: text(c, x, y - 14, sgn(v) if isinstance(v, int) else str(v), "Mono", 7.5, INK, "c")
            for j in range(counts.get(v, 0)):
                c.setFillColor(theme.main); c.circle(x, y + 10 + j * 11, 3.8, fill=1, stroke=0)
        if title: text(c, w / 2, h - 10, title, "BodySemi", 8.5, theme.dark, "c")
    return Draw(width, height, fn)


def box_plot(theme, five, lo, hi, step=1, width=None, label=None, second=None, second_label=None, label_every=1):
    """five = (min, q1, median, q3, max). Optional second box plot for comparison."""
    width = width or W * 0.85; height = 66 if not second else 104

    def fn(c, w, h):
        x0, x1 = 60, w - 14; y = 20
        X = lambda v: x0 + (x1 - x0) * (v - lo) / (hi - lo)
        c.setStrokeColor(INK); c.setLineWidth(1.1); c.line(x0, y, x1, y)
        k = lo; i = 0
        while k <= hi + 1e-9:
            c.line(X(k), y - 4, X(k), y + 4)
            if i % label_every == 0: text(c, X(k), y - 13, sgn(k) if isinstance(k, int) else str(k), "Mono", 7.5, INK, "c")
            k += step; i += 1
        for idx, (f, lab) in enumerate([(five, label), (second, second_label)]):
            if not f: continue
            by = y + 22 + idx * 38; mn, q1, md, q3, mx = f
            c.setStrokeColor(theme.dark); c.setLineWidth(1.2)
            c.line(X(mn), by + 8, X(q1), by + 8); c.line(X(q3), by + 8, X(mx), by + 8)
            c.line(X(mn), by + 3, X(mn), by + 13); c.line(X(mx), by + 3, X(mx), by + 13)
            c.setFillColor(theme.wash); c.rect(X(q1), by, X(q3) - X(q1), 16, fill=1, stroke=1)
            c.setStrokeColor(theme.main); c.setLineWidth(2); c.line(X(md), by, X(md), by + 16)
            if lab: text(c, 4, by + 5, lab, "BodySemi", 8, theme.dark, "l")
    return Draw(width, height, fn)


def tree_diagram(theme, first, second, width=None):
    """Two-stage tree: first = ['H','T'], second = ['1',...,'6']"""
    width = width or W * 0.8; n = len(first) * len(second); height = max(80, n * 13 + 10)

    def fn(c, w, h):
        x0, x1, x2 = 10, w * 0.32, w * 0.62
        rows = len(first) * len(second); gap = (h - 10) / rows
        for i, a in enumerate(first):
            ya = h - 5 - gap * (i * len(second) + len(second) / 2)
            c.setStrokeColor(theme.dark); c.setLineWidth(0.9); c.line(x0, h / 2, x1, ya)
            text(c, x1 + 4, ya - 3, a, "BodySemi", 9, theme.dark, "l")
            xs = x1 + 8 + stringWidth(a, "BodySemi", 9)
            for j, b in enumerate(second):
                yb = h - 5 - gap * (i * len(second) + j + 0.5)
                c.line(xs, ya, x2, yb); text(c, x2 + 4, yb - 3, b, "BodySemi", 8.5, INK, "l")
                combo = f"{a}{b}" if len(a) == 1 and len(b) == 1 else f"{a}, {b}"
                text(c, w - 6, yb - 3, combo, "Mono", 8, MUTED, "r")
        c.setFillColor(theme.main); c.circle(x0, h / 2, 2.5, fill=1, stroke=0)
    return Draw(width, height, fn)


def circle_fig(theme, r_label=None, d_label=None, width=140, show="r"):
    def fn(c, w, h):
        cx, cy, r = w / 2, h / 2, min(w, h) / 2 - 8
        c.setFillColor(theme.wash); c.setStrokeColor(theme.dark); c.setLineWidth(1.4); c.circle(cx, cy, r, fill=1, stroke=1)
        _dot(c, cx, cy, None, theme.dark)
        c.setStrokeColor(theme.main); c.setLineWidth(1.4)
        if show == "r":
            c.line(cx, cy, cx + r, cy)
            if r_label: text(c, cx + r / 2, cy + 4, r_label, "MonoSemi", 9, theme.dark, "c")
        else:
            c.line(cx - r, cy, cx + r, cy)
            if d_label: text(c, cx, cy + 4, d_label, "MonoSemi", 9, theme.dark, "c")
    return Draw(width, width * 0.9, fn)


def prism_fig(theme, l, w_, h_, unit="", width=200, height=130):
    """Oblique drawing of a rectangular prism with labeled edges."""
    def fn(c, ww, hh):
        s = min((ww - 70) / (l + w_ * 0.5), (hh - 40) / (h_ + w_ * 0.5))
        L, H, D = l * s, h_ * s, w_ * s * 0.5; x0, y0 = 16, 18
        c.setStrokeColor(theme.dark); c.setLineWidth(1.3)
        c.setFillColor(theme.wash); c.rect(x0, y0, L, H, fill=1, stroke=1)
        p = c.beginPath(); p.moveTo(x0, y0 + H); p.lineTo(x0 + D, y0 + H + D); p.lineTo(x0 + L + D, y0 + H + D); p.lineTo(x0 + L, y0 + H); p.close()
        c.setFillColor(theme.mid); c.drawPath(p, fill=1, stroke=1)
        p = c.beginPath(); p.moveTo(x0 + L, y0); p.lineTo(x0 + L + D, y0 + D); p.lineTo(x0 + L + D, y0 + H + D); p.lineTo(x0 + L, y0 + H); p.close()
        c.setFillColor(theme.main); c.drawPath(p, fill=1, stroke=1)
        text(c, x0 + L / 2, y0 - 12, f"{l} {unit}".strip(), "MonoSemi", 9, theme.dark, "c")
        text(c, x0 + L + D + 4, y0 + H / 2 + D / 2, f"{h_} {unit}".strip(), "MonoSemi", 9, theme.dark, "l")
        text(c, x0 + L + D / 2 + 4, y0 + D / 2 - 8, f"{w_} {unit}".strip(), "MonoSemi", 9, theme.dark, "l")
    return Draw(width, height, fn)


def grid_shape(theme, cells, cols, rows, size=12, width=None, color=None):
    """Shape drawn on a grid: cells is a list of (col, row) squares to shade (row 0 at bottom)."""
    width = width or cols * size + 6; height = rows * size + 6

    def fn(c, w, h):
        for i in range(cols):
            for j in range(rows):
                c.setFillColor((color or theme.mid) if (i, j) in cells else WHITE); c.setStrokeColor(GRID); c.setLineWidth(0.4)
                c.rect(3 + i * size, 3 + j * size, size, size, fill=1, stroke=1)
    return Draw(width, height, fn)


def ineq_line(theme, lo, hi, value, direction, closed, width=None, step=1, blank=False):
    """Graph of x < v, x <= v, x > v, x >= v on a number line. direction: 'left' or 'right'."""
    width = width or W * 0.75

    def fn(c, w, h):
        y = 26; x0, x1 = 14, w - 14
        X = lambda v: x0 + (x1 - x0) * (v - lo) / (hi - lo)
        c.setStrokeColor(INK); c.setLineWidth(1.1); c.line(x0 - 6, y, x1 + 6, y)
        _arrow(c, x1 + 8, y, 0, s=5); _arrow(c, x0 - 8, y, math.pi, s=5)
        k = lo
        while k <= hi + 1e-9:
            c.line(X(k), y - 4, X(k), y + 4); text(c, X(k), y - 14, sgn(int(k)) if float(k).is_integer() else str(k), "Mono", 7.5, INK, "c"); k += step
        if blank: return
        xv = X(value); c.setStrokeColor(theme.main); c.setLineWidth(3)
        end = x1 + 6 if direction == "right" else x0 - 6
        c.line(xv, y, end, y); _arrow(c, end + (4 if direction == "right" else -4), y, 0 if direction == "right" else math.pi, s=7, color=theme.main)
        c.setLineWidth(1.6); c.setFillColor(theme.main if closed else WHITE); c.circle(xv, y, 4.5, fill=1, stroke=1)
    return Draw(width, 46, fn)


def spinner(theme, labels, width=110, colors=None):
    """Spinner with equal sections, one label per section."""
    def fn(c, w, h):
        cx, cy, r = w / 2, h / 2, min(w, h) / 2 - 4
        n = len(labels); pal = colors or [theme.wash, WHITE]
        for i, lab in enumerate(labels):
            a0 = 90 - 360 * (i + 1) / n
            c.setFillColor(pal[i % len(pal)]); c.setStrokeColor(INK); c.setLineWidth(1)
            c.wedge(cx - r, cy - r, cx + r, cy + r, a0, 360 / n, fill=1, stroke=1)
            am = math.radians(a0 + 180 / n)
            text(c, cx + 0.62 * r * math.cos(am), cy + 0.62 * r * math.sin(am) - 3, str(lab), "BodyBold", 9, INK, "c")
        c.setStrokeColor(theme.main); c.setLineWidth(2); c.line(cx, cy, cx + 0.3 * r, cy + 0.3 * r)
        c.setFillColor(theme.main); c.circle(cx, cy, 3, fill=1, stroke=0)
    return Draw(width, width, fn)



def grid_poly(theme, pts, cols, rows, size=11, width=None, labels=None):
    """Polygon with integer grid vertices drawn over a square grid (for scaled copies)."""
    width = width or cols * size + 8; height = rows * size + 8

    def fn(c, w, h):
        c.setStrokeColor(colors.HexColor("#CFC7B8")); c.setLineWidth(0.5)
        for i in range(cols + 1): c.line(4 + i * size, 4, 4 + i * size, 4 + rows * size)
        for j in range(rows + 1): c.line(4, 4 + j * size, 4 + cols * size, 4 + j * size)
        if not pts: return
        p = c.beginPath(); p.moveTo(4 + pts[0][0] * size, 4 + pts[0][1] * size)
        for x, y in pts[1:]: p.lineTo(4 + x * size, 4 + y * size)
        p.close(); c.setFillColor(theme.wash); c.setStrokeColor(theme.dark); c.setLineWidth(1.6); c.drawPath(p, fill=1, stroke=1)
        if labels:
            cx = sum(x for x, _ in pts) / len(pts); cy = sum(y for _, y in pts) / len(pts)
            for (x, y), lab in zip(pts, labels):
                dx, dy = x - cx, y - cy; d = math.hypot(dx, dy) or 1
                text(c, 4 + x * size + dx / d * 8, 4 + y * size + dy / d * 8 - 3, lab, "BodySemi", 8.5, theme.dark, "c")
    return Draw(width, height, fn)


def solid_fig(theme, kind, cut=None, width=120, height=120):
    """Solid with an optional shaded cross section. kind: prism, pyramid, cylinder, cone. cut: 'h' (parallel to base) or 'v' (perpendicular to base)."""
    def fn(c, w, h):
        x0, y0 = 14, 14; a = w * 0.52; dx, dy = w * 0.26, h * 0.18; H = h * 0.55
        c.setLineWidth(1.3); c.setStrokeColor(theme.dark)

        def poly(pts, fill=None, dash=False):
            p = c.beginPath(); p.moveTo(*pts[0])
            for q in pts[1:]: p.lineTo(*q)
            p.close()
            if dash: c.setDash(3, 2)
            if fill is not None: c.setFillColor(fill)
            c.drawPath(p, fill=1 if fill is not None else 0, stroke=1); c.setDash()
        sec = theme.mid
        if kind == "prism":
            F_ = [(x0, y0), (x0 + a, y0), (x0 + a, y0 + H), (x0, y0 + H)]
            Bk = [(x + dx, y + dy) for x, y in F_]
            c.setDash(3, 2); c.line(*Bk[0], *Bk[1]); c.line(*Bk[0], *Bk[3]); c.line(*F_[0], *Bk[0]); c.setDash()
            if cut == "h":
                ym = y0 + H / 2; poly([(x0, ym), (x0 + a, ym), (x0 + a + dx, ym + dy), (x0 + dx, ym + dy)], sec)
            if cut == "v":
                poly([(x + dx / 2, y + dy / 2) for x, y in F_], sec)
            poly(F_); c.line(*F_[1], *Bk[1]); c.line(*F_[2], *Bk[2]); c.line(*F_[3], *Bk[3]); c.line(*Bk[1], *Bk[2]); c.line(*Bk[2], *Bk[3])
        elif kind == "pyramid":
            B = [(x0, y0), (x0 + a, y0), (x0 + a + dx, y0 + dy), (x0 + dx, y0 + dy)]
            A = (x0 + (a + dx) / 2, y0 + dy / 2 + H * 1.15)
            c.setDash(3, 2); c.line(*B[2], *B[3]); c.line(*B[3], *B[0]); c.line(*B[3], *A); c.setDash()
            if cut == "h":
                poly([(x + 0.5 * (A[0] - x), y + 0.5 * (A[1] - y)) for x, y in B], sec)
            if cut == "v":
                m03 = ((B[0][0] + B[3][0]) / 2, (B[0][1] + B[3][1]) / 2); m12 = ((B[1][0] + B[2][0]) / 2, (B[1][1] + B[2][1]) / 2)
                poly([m03, m12, A], sec)
            c.line(*B[0], *B[1]); c.line(*B[1], *B[2]); c.line(*B[0], *A); c.line(*B[1], *A); c.line(*B[2], *A)
        else:
            cx = w / 2; rx, ry = w * 0.32, h * 0.08; yb = y0 + ry; top = yb + H * 1.1
            if kind == "cylinder":
                if cut == "v": poly([(cx - rx, yb), (cx + rx, yb), (cx + rx, top), (cx - rx, top)], sec)
                c.setDash(3, 2); c.arc(cx - rx, yb - ry, cx + rx, yb + ry, 0, 180); c.setDash()
                c.arc(cx - rx, yb - ry, cx + rx, yb + ry, 180, 180)
                if cut == "h":
                    ym = (yb + top) / 2; c.setFillColor(sec); c.ellipse(cx - rx, ym - ry, cx + rx, ym + ry, fill=1, stroke=1)
                c.line(cx - rx, yb, cx - rx, top); c.line(cx + rx, yb, cx + rx, top)
                c.setFillColor(WHITE); c.ellipse(cx - rx, top - ry, cx + rx, top + ry, fill=0, stroke=1)
            else:
                if cut == "v": poly([(cx - rx, yb), (cx + rx, yb), (cx, top)], sec)
                c.setDash(3, 2); c.arc(cx - rx, yb - ry, cx + rx, yb + ry, 0, 180); c.setDash()
                c.arc(cx - rx, yb - ry, cx + rx, yb + ry, 180, 180)
                if cut == "h":
                    ym = (yb + top) / 2; c.setFillColor(sec); c.ellipse(cx - rx / 2, ym - ry / 2, cx + rx / 2, ym + ry / 2, fill=1, stroke=1)
                c.line(cx - rx, yb, cx, top); c.line(cx + rx, yb, cx, top)
    return Draw(width, height, fn)


def rays_fig(theme, dirs, labels, width=200, height=110, right=(), full=False):
    """Rays from one vertex at the given directions (degrees). labels[i] names the sector from dirs[i] to dirs[i+1]
    (wrapping around when full=True). right: sector indexes to mark as right angles."""
    def fn(c, w, h):
        vx, vy = w / 2, (h / 2 if full else 16); R = min(w / 2 - 12, h - 26) if not full else min(w, h) / 2 - 8
        c.setStrokeColor(theme.dark); c.setLineWidth(1.6)
        for d in dirs:
            a = math.radians(d); x2, y2 = vx + R * math.cos(a), vy + R * math.sin(a)
            c.line(vx, vy, x2, y2); _arrow(c, x2 + 4 * math.cos(a), y2 + 4 * math.sin(a), a, color=theme.dark)
        _dot(c, vx, vy, None, theme.dark)
        n = len(dirs) if full else len(dirs) - 1
        for i in range(n):
            d0 = dirs[i]; d1 = dirs[(i + 1) % len(dirs)] + (360 if full and i == len(dirs) - 1 else 0)
            if i in right:
                s = 10; a0, a1 = math.radians(d0), math.radians(d1); c.setStrokeColor(theme.main); c.setLineWidth(1)
                p = c.beginPath(); p.moveTo(vx + s * math.cos(a0), vy + s * math.sin(a0)); p.lineTo(vx + s * math.cos(a0) + s * math.cos(a1), vy + s * math.sin(a0) + s * math.sin(a1)); p.lineTo(vx + s * math.cos(a1), vy + s * math.sin(a1)); c.drawPath(p)
            else:
                r = 14 + 4 * (i % 2); c.setStrokeColor(theme.main); c.setLineWidth(1.1); c.arc(vx - r, vy - r, vx + r, vy + r, d0, d1 - d0)
            if i < len(labels) and labels[i]:
                am = math.radians((d0 + d1) / 2); rr = 34 if (d1 - d0) > 30 else 46
                text(c, vx + rr * math.cos(am), vy + rr * math.sin(am) - 3, labels[i], "MonoSemi", 9, theme.main, "c")
    return Draw(width, height, fn)


def tri_prism(theme, b, th, l, unit="", width=200, height=120, hyp=None):
    """Oblique triangular prism: right-triangle base (legs b, th) extruded by length l."""
    def fn(c, ww, hh):
        s = min((ww - 100) / (b + l * 0.6), (hh - 34) / (th + l * 0.35))
        B, T, Lx, Ly = b * s, th * s, l * s * 0.6, l * s * 0.35; x0, y0 = 44, 18
        c.setStrokeColor(theme.dark); c.setLineWidth(1.3)
        front = [(x0, y0), (x0 + B, y0), (x0, y0 + T)]; back = [(x + Lx, y + Ly) for x, y in front]
        c.setDash(3, 2); c.line(*back[0], *back[1]); c.line(*back[0], *back[2]); c.line(*front[0], *back[0]); c.setDash()
        p = c.beginPath(); p.moveTo(*front[1]); p.lineTo(*back[1]); p.lineTo(*back[2]); p.lineTo(*front[2]); p.close(); c.setFillColor(theme.mid); c.drawPath(p, fill=1, stroke=1)
        p = c.beginPath(); p.moveTo(*front[0]); p.lineTo(*front[1]); p.lineTo(*front[2]); p.close(); c.setFillColor(theme.wash); c.drawPath(p, fill=1, stroke=1)
        c.setLineWidth(0.9); q = 7; c.line(x0 + q, y0, x0 + q, y0 + q); c.line(x0, y0 + q, x0 + q, y0 + q)
        text(c, x0 + B / 2, y0 - 12, f"{b} {unit}".strip(), "MonoSemi", 9, theme.dark, "c")
        text(c, x0 - 4, y0 + T / 2, f"{th} {unit}".strip(), "MonoSemi", 9, theme.dark, "r")
        text(c, x0 + B + Lx / 2 + 6, y0 + Ly / 2 - 6, f"{l} {unit}".strip(), "MonoSemi", 9, theme.dark, "l")
    return Draw(width, height, fn)


def rect_semi(theme, l, w_, unit="", width=180, height=130):
    """Rectangle l (across) by w_ (up) with a semicircle on the top side."""
    def fn(c, ww, hh):
        s = min((ww - 40) / l, (hh - 30) / (w_ + l / 2)); L, H = l * s, w_ * s; x0, y0 = (ww - L) / 2, 16
        c.setStrokeColor(theme.dark); c.setLineWidth(1.4); c.setFillColor(theme.wash)
        p = c.beginPath(); p.moveTo(x0, y0); p.lineTo(x0 + L, y0); p.lineTo(x0 + L, y0 + H)
        p.arcTo(x0, y0 + H - L / 2, x0 + L, y0 + H + L / 2, 0, 180); p.lineTo(x0, y0); p.close(); c.drawPath(p, fill=1, stroke=1)
        c.setDash(3, 2); c.line(x0, y0 + H, x0 + L, y0 + H); c.setDash()
        text(c, x0 + L / 2, y0 - 12, f"{l} {unit}".strip(), "MonoSemi", 9, theme.dark, "c")
        text(c, x0 + L + 4, y0 + H / 2 - 3, f"{w_} {unit}".strip(), "MonoSemi", 9, theme.dark, "l")
    return Draw(width, height, fn)


def plot_arc(theme, labels, width=None, height=120):
    """Plot mountain: exposition, rising action, climax, falling action, resolution."""
    width = width or W * 0.85

    def fn(c, w, h):
        pts = [(10, 18), (w * 0.22, 18), (w * 0.6, h - 22), (w * 0.82, 40), (w - 10, 40)]
        c.setStrokeColor(theme.main); c.setLineWidth(2.4)
        p = c.beginPath(); p.moveTo(*pts[0])
        for q in pts[1:]: p.lineTo(*q)
        c.drawPath(p)
        spots = [((pts[0][0] + pts[1][0]) / 2, 6, "c"), ((pts[1][0] + pts[2][0]) / 2 - 18, (pts[1][1] + pts[2][1]) / 2 + 4, "r"), (pts[2][0], h - 14, "c"),
                 ((pts[2][0] + pts[3][0]) / 2 + 14, (pts[2][1] + pts[3][1]) / 2 + 4, "l"), ((pts[3][0] + pts[4][0]) / 2, 28, "c")]
        for (x, y, al), lab in zip(spots, labels):
            text(c, x, y, lab, "BodySemi", 8.5, theme.dark, al)
        c.setFillColor(theme.main); c.circle(*pts[2], 4, fill=1, stroke=0)
    return Draw(width, height, fn)


def timeline_fig(theme, events, width=None, height=70):
    """Horizontal timeline. events: list of (date label, description)."""
    width = width or W * 0.95

    def fn(c, w, h):
        y = h / 2 + 4; x0, x1 = 16, w - 16; n = len(events)
        c.setStrokeColor(theme.dark); c.setLineWidth(1.6); c.line(x0, y, x1, y)
        for i, (d, desc) in enumerate(events):
            x = x0 + (x1 - x0) * (i + 0.5) / n
            c.setFillColor(theme.main); c.circle(x, y, 4, fill=1, stroke=0)
            text(c, x, y + 10, d, "MonoSemi", 8, theme.dark, "c")
            words = desc.split(); half = (len(words) + 1) // 2
            text(c, x, y - 17, " ".join(words[:half]), "Body", 7.5, INK, "c")
            if words[half:]: text(c, x, y - 27, " ".join(words[half:]), "Body", 7.5, INK, "c")
    return Draw(width, height, fn)


def bar_graph(theme, labels, values, title=None, ylabel=None, step=None, width=None, height=170):
    """Vertical bar graph with gridlines and value axis."""
    width = width or W * 0.75
    top = max(values); step = step or max(1, round(top / 5))
    ymax = step * math.ceil(top / step)

    def fn(c, w, h):
        L, B, R, T = 44, 30, w - 10, h - (22 if title else 8)
        if title: text(c, (L + R) / 2, h - 12, title, "BodySemi", 9.5, theme.dark, "c")
        v = 0
        while v <= ymax + 1e-9:
            y = B + (T - B) * v / ymax
            c.setStrokeColor(GRID); c.setLineWidth(0.5); c.line(L, y, R, y)
            text(c, L - 5, y - 3, f"{v:,}", "Mono", 7.5, INK, "r"); v += step
        n = len(values); slot = (R - L) / n; bw = slot * 0.55
        for i, (lab, val) in enumerate(zip(labels, values)):
            x = L + slot * i + (slot - bw) / 2; y = B + (T - B) * val / ymax
            c.setFillColor(theme.main); c.rect(x, B, bw, y - B, fill=1, stroke=0)
            text(c, x + bw / 2, B - 12, lab, "Body", 8, INK, "c")
        c.setStrokeColor(INK); c.setLineWidth(1); c.line(L, B, R, B); c.line(L, B, L, T)
        if ylabel:
            c.saveState(); c.translate(10, (B + T) / 2); c.rotate(90); text(c, 0, 0, ylabel, "Body", 8, MUTED, "c"); c.restoreState()
    return Draw(width, height, fn)


def ship_diagram(theme, width=None, height=200):
    """Side view of a two-masted schooner with labeled parts."""
    width = width or W * 0.9

    def fn(c, w, h):
        wl = 46; x0, x1 = w * 0.16, w * 0.80
        c.setStrokeColor(theme.mid); c.setLineWidth(1)
        for k in range(4): c.line(10, wl - 6 - k * 7, w - 10, wl - 6 - k * 7)
        hull = c.beginPath(); hull.moveTo(x0 - 18, wl + 26); hull.lineTo(x1 + 30, wl + 26); hull.lineTo(x1, wl - 10); hull.lineTo(x0 + 10, wl - 10); hull.close()
        c.setFillColor(theme.dark); c.setStrokeColor(INK); c.drawPath(hull, fill=1, stroke=1)
        c.setStrokeColor(WHITE); c.setLineWidth(0.8); c.line(x0 - 12, wl + 20, x1 + 24, wl + 20)
        c.setFillColor(INK); c.rect(x0 - 26, wl - 12, 8, 30, fill=1, stroke=0)  # rudder at stern
        masts = [x0 + (x1 - x0) * 0.33, x0 + (x1 - x0) * 0.68]
        c.setStrokeColor(INK); c.setLineWidth(2.2)
        for m in masts: c.line(m, wl + 26, m, h - 14)
        c.setFillColor(theme.wash); c.setStrokeColor(theme.dark); c.setLineWidth(1)
        for m in masts:
            s = c.beginPath(); s.moveTo(m + 3, h - 20); s.lineTo(m + 3, wl + 34); s.lineTo(m - 52, wl + 34); s.close(); c.drawPath(s, fill=1, stroke=1)
        jib = c.beginPath(); jib.moveTo(masts[1] + 4, h - 22); jib.lineTo(x1 + 52, wl + 30); jib.lineTo(masts[1] + 4, wl + 34); jib.close(); c.drawPath(jib, fill=1, stroke=1)
        c.setStrokeColor(MUTED); c.setLineWidth(0.6); c.line(masts[1], h - 14, x1 + 52, wl + 28)  # rigging line
        labels = [((x1 + 40, wl + 2), "bow →", "l"), ((x0 - 30, wl + 30), "← stern", "r"), ((x0 - 30, wl - 4), "rudder", "r"), ((masts[0] + 6, h - 12), "mast", "l"),
                  ((masts[0] - 40, wl + 70), "sail", "c"), (((x0 + x1) / 2, wl + 4), "hull", "c"), ((x1 + 56, wl + 60), "jib", "l"), ((masts[0] + (masts[1] - 52 - masts[0]) / 2, wl + 30), "deck", "c"),
                  ((masts[1] + 46, h - 40), "rigging", "l")]
        for (x, y), lab, al in labels:
            text(c, x, y, lab, "BodySemi", 8.5, WHITE if lab == "hull" else theme.dark, al)
    return Draw(width, height, fn)


def island_map(theme, width=None, height=210):
    """A simple treasure-island style map with a compass rose, key, and scale."""
    width = width or W * 0.8

    def fn(c, w, h):
        c.setFillColor(theme.wash); c.setStrokeColor(theme.mid); c.rect(0, 0, w, h, fill=1, stroke=1)
        pts = [(0.18, 0.30), (0.30, 0.15), (0.55, 0.12), (0.75, 0.22), (0.82, 0.45), (0.72, 0.72), (0.50, 0.85), (0.28, 0.78), (0.15, 0.55)]
        p = c.beginPath(); p.moveTo(pts[0][0] * w, pts[0][1] * h)
        for x, y in pts[1:]: p.lineTo(x * w, y * h)
        p.close(); c.setFillColor(colors.HexColor("#F3E9D2")); c.setStrokeColor(INK); c.setLineWidth(1.4); c.drawPath(p, fill=1, stroke=1)
        # hill (triangles), stockade (square), swamp (dashes), anchorage (anchor letter)
        for hx in (0.48, 0.55):
            t = c.beginPath(); t.moveTo(hx * w, 0.62 * h); t.lineTo(hx * w + 10, 0.62 * h); t.lineTo(hx * w + 5, 0.62 * h + 12); t.close(); c.setFillColor(MUTED); c.drawPath(t, fill=1, stroke=0)
        c.setStrokeColor(theme.dark); c.setLineWidth(1.2); c.rect(0.30 * w, 0.40 * h, 12, 12, fill=0, stroke=1)
        c.setStrokeColor(colors.HexColor("#6B8E5A"))
        for k in range(4): c.line(0.62 * w, (0.33 + k * 0.03) * h, 0.62 * w + 16, (0.33 + k * 0.03) * h)
        text(c, 0.65 * w, 0.58 * h, "X", "BodyBold", 14, theme.main, "c")
        text(c, 0.12 * w, 0.18 * h, "⚓", "Sym", 12, theme.dark, "c")
        # compass rose
        cx, cy = w - 34, h - 40
        c.setStrokeColor(INK); c.setLineWidth(1); c.line(cx, cy - 18, cx, cy + 18); c.line(cx - 18, cy, cx + 18, cy)
        for lab, dx, dy in (("N", 0, 24), ("S", 0, -30), ("E", 26, -3), ("W", -26, -3)): text(c, cx + dx, cy + dy, lab, "BodySemi", 8, INK, "c")
        # key
        kx, ky = 10, h - 14
        text(c, kx, ky, "KEY", "BodySemi", 8, theme.dark, "l")
        for i, lab in enumerate(["▲ hills", "□ stockade", "≡ swamp", "X treasure", "⚓ anchorage"]):
            text(c, kx, ky - 11 * (i + 1), lab, "Sym", 7.5, INK, "l")
        # scale bar
        c.setStrokeColor(INK); c.line(w - 110, 14, w - 50, 14); c.line(w - 110, 11, w - 110, 17); c.line(w - 50, 11, w - 50, 17)
        text(c, w - 80, 20, "1 mile", "Body", 7.5, INK, "c")
    return Draw(width, height, fn)
