"""Front and back covers for VenvLearning textbooks, workbooks, and teacher editions.

make_covers(book, kind, path) writes a two-page PDF (front, back); attach(book, kind, pdf_path) wraps an
existing book PDF with them, padding so the back cover lands on an even page for duplex printing."""
import math, os, io
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas as _canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from engine import (PAGE_W, PAGE_H, LM, RM, IVORY, INK, GOLD, BLUSH, HUNTER, MUTED, LINE, WHITE, Paragraph, text, KIND_LABEL)

M = 0.7 * inch   # cover margin


ART_RGB = [(1, 1, 1)]


def a(alpha, rgb=None):
    return colors.Color(*(rgb or ART_RGB[0]), alpha=alpha)


# Covers default to white type on the subject color; Data Science uses the signature blush with dark type.
def palette(book):
    t = book.theme
    if book.subject == "data":
        return dict(bg=BLUSH, ink=HUNTER, sub=HUNTER, art=(0.14, 0.27, 0.22), band=t.dark)
    if book.subject == "art":
        return dict(bg=t.main, ink=t.on_main, sub=t.dark, art=(0.17, 0.16, 0.13), band=t.dark)
    return dict(bg=t.main, ink=WHITE, sub=BLUSH, art=(1, 1, 1), band=t.dark)


def stripe(c, y, h=8, color=INK, step=6):
    c.setFillColor(color); x = 0
    while x < PAGE_W:
        c.rect(x, y, step / 2, h, fill=1, stroke=0); x += step


SHORT = {"spanish": "Spanish", "art": "Art", "math": "Mathematics", "ela": "English Language Arts", "science": "Science", "social": "Social Studies", "data": "Data Science & Psychometrics"}
TITLE_LINES = {"math": ["Mathematics"], "ela": ["English", "Language Arts"], "science": ["Science"], "social": ["Social", "Studies"],
               "data": ["Data Science &", "Psychometrics"], "art": ["Art"], "spanish": ["Spanish", "Español"]}

BLURB = {
    "math": "A full year of Grade {g} mathematics, taught one clear idea at a time. Every lesson opens with a question worth thinking about, "
            "walks through worked examples step by step, and builds from models and pictures to fluent, confident problem solving.",
    "ela": "A full year of Grade {g} reading, writing, and language. Lessons pair the Core Knowledge Readers with close reading, vocabulary, "
           "grammar, and writing instruction, so students learn to read carefully, think deeply, and write with purpose.",
    "science": "A full year of Grade {g} science built around questions, investigations, and evidence. Students observe, measure, model, "
               "and explain the natural world, then use what they learn to design solutions to real problems.",
    "spanish": "A full year of Grade {g} Spanish in short daily lessons. Students listen, speak, read, and write from the very first day, "
               "building real conversations step by step and exploring the people, places, and traditions of the Spanish-speaking world.",
    "art": "A full year of Grade {g} arts: drawing, painting, and design; music; art history; theater and dance; media arts; and sculpture. "
           "Every lesson pairs looking closely at real artwork with hands-on studio time, and the year ends with a portfolio and a show.",
    "data": "A year of professional learning in statistics, data science, and psychometrics, built for a working professional: about 30 minutes a day, "
            "Monday through Friday. Every lesson pairs a short reading with worked examples, a suggested video, and hands-on code in SAS, Python, and R, "
            "using realistic assessment and survey data.",
    "social": "A full year of Grade {g} social studies. Students read maps, weigh primary and secondary sources, build timelines, and "
              "connect geography, history, government, and economics to the people and places that shaped our world.",
}
KIND_BLURB_DATA = {
    "textbook": "This <b>Textbook</b> teaches every lesson: the big idea, key terms, worked examples, side-by-side code in SAS, Python, and R, "
                "suggested videos, and On the Job notes that connect each skill to real work. It pairs with the Workbook.",
    "workbook": "This <b>Workbook</b> holds the hands-on practice for every lesson, a quiz every Friday, unit exams, and a complete answer key "
                "with code solutions at the back.",
}
INSIDE_DATA = {
    "textbook": ["Four 30-minute lessons a week, Monday–Thursday", "Code It examples in SAS, Python, and R", "Watch lists: videos and free courses for each topic", "On the Job notes and a glossary"],
    "workbook": ["Practice and coding exercises for every lesson", "A quiz every Friday", "Unit exams", "Answer key with code solutions"],
}
KIND_BLURB = {
    "textbook": "This <b>Student Textbook</b> teaches every lesson: the big idea, key vocabulary, models and examples, and a short set of practice "
                "problems to check understanding. It pairs with the Student Workbook and the Teacher Edition.",
    "workbook": "This <b>Student Workbook</b> holds the daily practice pages for every lesson, plus each Friday's Weekly Check, the unit reviews, "
                "and the unit tests, with room to show thinking and write complete answers.",
    "teacher": "This <b>Teacher Edition</b> holds everything needed to teach: a pacing calendar, a guided lesson plan for every day with "
               "timing, discussion prompts, common misconceptions, support and extension ideas, and complete answer keys.",
}
INSIDE = {
    "textbook": ["Clear lesson goals: “I can…” statements", "Key vocabulary with student-friendly definitions", "Models, examples, and Key Idea summaries", "A study guide and glossary for every unit"],
    "workbook": ["Warm-ups, practice, and exit tickets for every lesson", "Weekly Checks every Friday", "Unit reviews and unit tests", "Space to show work and explain thinking"],
    "teacher": ["Day-by-day pacing calendar for the school year", "Guided lessons with timing and teaching moves", "Misconceptions, supports, and extensions", "Answer keys and scoring guides for every page"],
}


# ---------------------------------------------------------------- subject art (white line work on the subject color)
def art_math(c, cx, cy, r):
    c.setStrokeColor(a(0.22)); c.setLineWidth(1.2)
    # coordinate grid
    for i in range(-6, 7):
        c.setStrokeColor(a(0.07)); c.line(cx + i * r / 6, cy - r * 1.05, cx + i * r / 6, cy + r * 1.05); c.line(cx - r * 1.05, cy + i * r / 6, cx + r * 1.05, cy + i * r / 6)
    c.setStrokeColor(a(0.30)); c.setLineWidth(2)
    c.circle(cx, cy, r, stroke=1, fill=0)
    # protractor ticks around the circle
    for d in range(0, 360, 10):
        t = math.radians(d); l = 14 if d % 30 == 0 else 7
        c.line(cx + r * math.cos(t), cy + r * math.sin(t), cx + (r - l) * math.cos(t), cy + (r - l) * math.sin(t))
    # inscribed triangle and a radius
    pts = [(cx + r * 0.82 * math.cos(math.radians(d)), cy + r * 0.82 * math.sin(math.radians(d))) for d in (90, 210, 330)]
    c.setStrokeColor(a(0.42)); c.setLineWidth(2.4)
    p = c.beginPath(); p.moveTo(*pts[0]); [p.lineTo(*q) for q in pts[1:]]; p.close(); c.drawPath(p, stroke=1, fill=0)
    c.setStrokeColor(a(0.30)); c.setLineWidth(1.5); c.circle(cx, cy, r * 0.41, stroke=1, fill=0)
    c.setFillColor(a(0.5)); c.circle(cx, cy, 4, fill=1, stroke=0)
    c.setFillColor(a(0.22)); c.setFont("Sym", 30)
    for s, dx, dy in (("π", -1.05, 0.95), ("÷", 1.0, 0.9), ("×", 1.08, -0.85), ("=", -1.1, -0.9), ("%", 0.0, -1.22), ("√", -1.25, 0.1)):
        c.drawCentredString(cx + dx * r, cy + dy * r, s)


def art_ela(c, cx, cy, r):
    # open book
    w, h = r * 1.1, r * 0.78
    c.setStrokeColor(a(0.45)); c.setLineWidth(2.2); c.setFillColor(a(0.08))
    for side in (-1, 1):
        p = c.beginPath(); p.moveTo(cx, cy - h * 0.55)
        p.curveTo(cx + side * w * 0.35, cy - h * 0.42, cx + side * w * 0.7, cy - h * 0.5, cx + side * w, cy - h * 0.45)
        p.lineTo(cx + side * w, cy + h * 0.55)
        p.curveTo(cx + side * w * 0.7, cy + h * 0.6, cx + side * w * 0.35, cy + h * 0.52, cx, cy + h * 0.42)
        p.close(); c.drawPath(p, stroke=1, fill=1)
        c.setStrokeColor(a(0.22)); c.setLineWidth(1.2)
        for k in range(7):
            y = cy + h * 0.32 - k * h * 0.12
            x0, x1 = (cx + side * w * 0.12, cx + side * w * 0.88)
            c.line(min(x0, x1), y, max(x0, x1) - (w * 0.25 if k == 6 and side == 1 else 0), y)
        c.setStrokeColor(a(0.45)); c.setLineWidth(2.2)
    # quill
    c.saveState(); c.translate(cx + r * 0.75, cy + r * 0.55); c.rotate(-35)
    c.setFillColor(a(0.20)); c.setStrokeColor(a(0.5)); c.setLineWidth(1.5)
    p = c.beginPath(); p.moveTo(0, -r * 0.55); p.curveTo(r * 0.16, -r * 0.2, r * 0.16, r * 0.25, 0, r * 0.55); p.curveTo(-r * 0.1, r * 0.2, -r * 0.1, -r * 0.2, 0, -r * 0.55)
    p.close(); c.drawPath(p, stroke=1, fill=1); c.line(0, -r * 0.7, 0, r * 0.5)
    for k in range(1, 8):
        y = -r * 0.45 + k * r * 0.11; c.setStrokeColor(a(0.28)); c.line(0, y, r * 0.09, y + r * 0.06)
    c.restoreState()
    c.setFillColor(a(0.20)); c.setFont("Display", 64); c.drawCentredString(cx - r * 0.95, cy + r * 0.75, "Aa")
    c.setFont("Display", 90); c.drawCentredString(cx + r * 0.95, cy - r * 1.05, "”")
    c.setFont("Display", 26); c.drawCentredString(cx - r * 1.05, cy - r * 0.95, "?  !  ;")


def art_science(c, cx, cy, r):
    # atom
    c.setStrokeColor(a(0.35)); c.setLineWidth(2)
    for ang in (0, 60, 120):
        c.saveState(); c.translate(cx, cy); c.rotate(ang); c.ellipse(-r, -r * 0.36, r, r * 0.36, stroke=1, fill=0); c.restoreState()
    c.setFillColor(a(0.55)); c.circle(cx, cy, r * 0.11, fill=1, stroke=0)
    for ang, t in ((0, 30), (60, 150), (120, 260)):
        x, y = r * math.cos(math.radians(t)), r * 0.36 * math.sin(math.radians(t))
        ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        c.setFillColor(a(0.7)); c.circle(cx + x * ca - y * sa, cy + x * sa + y * ca, 6, fill=1, stroke=0)
    # flask (lower left)
    fx, fy, s = cx - r * 1.05, cy - r * 0.95, r * 0.42
    c.setStrokeColor(a(0.45)); c.setLineWidth(2); c.setFillColor(a(0.10))
    p = c.beginPath(); p.moveTo(fx - s * 0.18, fy + s); p.lineTo(fx - s * 0.18, fy + s * 0.4); p.lineTo(fx - s * 0.7, fy - s * 0.6)
    p.lineTo(fx + s * 0.7, fy - s * 0.6); p.lineTo(fx + s * 0.18, fy + s * 0.4); p.lineTo(fx + s * 0.18, fy + s); p.close(); c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(a(0.25)); c.circle(fx - s * 0.1, fy - s * 0.25, 5, fill=1, stroke=0); c.circle(fx + s * 0.2, fy - s * 0.05, 3.5, fill=1, stroke=0); c.circle(fx, fy + s * 0.2, 2.5, fill=1, stroke=0)
    # leaf (upper right)
    lx, ly, s = cx + r * 1.0, cy + r * 0.95, r * 0.5
    c.saveState(); c.translate(lx, ly); c.rotate(35); c.setStrokeColor(a(0.45)); c.setFillColor(a(0.12))
    p = c.beginPath(); p.moveTo(0, -s); p.curveTo(s * 0.7, -s * 0.4, s * 0.6, s * 0.5, 0, s); p.curveTo(-s * 0.6, s * 0.5, -s * 0.7, -s * 0.4, 0, -s); p.close()
    c.drawPath(p, stroke=1, fill=1); c.line(0, -s * 1.25, 0, s * 0.85)
    for k in range(-2, 3):
        c.setStrokeColor(a(0.28)); c.line(0, k * s * 0.3, s * 0.35, k * s * 0.3 + s * 0.22); c.line(0, k * s * 0.3, -s * 0.35, k * s * 0.3 + s * 0.22)
    c.restoreState()
    # DNA-ish wave (right)
    c.setStrokeColor(a(0.22)); c.setLineWidth(1.4)
    for ph in (0, math.pi):
        p = c.beginPath()
        for k in range(41):
            y = cy - r * 1.2 + k * r * 0.03 * 1.5; x = cx + r * 1.25 + math.sin(k / 4 + ph) * r * 0.14
            p.moveTo(x, y) if k == 0 else p.lineTo(x, y)
        c.drawPath(p, stroke=1, fill=0)


def art_social(c, cx, cy, r):
    # globe
    c.setStrokeColor(a(0.40)); c.setLineWidth(2.2); c.setFillColor(a(0.07)); c.circle(cx, cy, r, stroke=1, fill=1)
    c.setLineWidth(1.2); c.setStrokeColor(a(0.25))
    for k in (-0.66, -0.33, 0, 0.33, 0.66):
        y = cy + k * r; hw = math.sqrt(1 - k * k) * r; c.ellipse(cx - hw, y - r * 0.05 * (1 - abs(k)), cx + hw, y + r * 0.05 * (1 - abs(k)), stroke=1, fill=0)
    for f in (0.3, 0.65, 0.92):
        c.ellipse(cx - r * f, cy - r, cx + r * f, cy + r, stroke=1, fill=0)
    c.line(cx, cy - r, cx, cy + r)
    # compass rose (upper left)
    rx, ry, s = cx - r * 1.05, cy + r * 0.9, r * 0.32
    c.setFillColor(a(0.32))
    for d in range(0, 360, 90):
        c.saveState(); c.translate(rx, ry); c.rotate(d)
        p = c.beginPath(); p.moveTo(0, s); p.lineTo(s * 0.18, 0); p.lineTo(0, -s * 0.05); p.lineTo(-s * 0.18, 0); p.close(); c.drawPath(p, stroke=0, fill=1)
        c.restoreState()
    for d in range(45, 360, 90):
        c.saveState(); c.translate(rx, ry); c.rotate(d); c.setFillColor(a(0.18))
        p = c.beginPath(); p.moveTo(0, s * 0.6); p.lineTo(s * 0.12, 0); p.lineTo(-s * 0.12, 0); p.close(); c.drawPath(p, stroke=0, fill=1)
        c.restoreState()
    c.setFillColor(a(0.5)); c.setFont("BodySemi", 13); c.drawCentredString(rx, ry + s + 6, "N")
    # mountains (lower right)
    mx, my, s = cx + r * 0.75, cy - r * 1.1, r * 0.55
    c.setStrokeColor(a(0.45)); c.setFillColor(a(0.12)); c.setLineWidth(2)
    p = c.beginPath(); p.moveTo(mx - s, my); p.lineTo(mx - s * 0.35, my + s * 0.8); p.lineTo(mx, my + s * 0.35); p.lineTo(mx + s * 0.35, my + s * 0.95); p.lineTo(mx + s, my); p.close()
    c.drawPath(p, stroke=1, fill=1)
    # dotted route
    c.setStrokeColor(a(0.4)); c.setLineWidth(2); c.setDash(2, 6)
    p = c.beginPath(); p.moveTo(cx - r * 0.55, cy + r * 0.35); p.curveTo(cx - r * 0.1, cy + r * 0.75, cx + r * 0.2, cy - r * 0.1, cx + r * 0.55, cy - r * 0.3); c.drawPath(p, stroke=1, fill=0)
    c.setDash(); c.setFillColor(a(0.6)); c.circle(cx - r * 0.55, cy + r * 0.35, 5, fill=1, stroke=0)
    c.setStrokeColor(a(0.6)); c.setLineWidth(2.4); x, y = cx + r * 0.55, cy - r * 0.3
    c.line(x - 6, y - 6, x + 6, y + 6); c.line(x - 6, y + 6, x + 6, y - 6)


def art_spanish(c, cx, cy, r):
    # overlapping speech bubbles with greetings, plus accented letters
    def bubble(x, y, w, h, tail_left, txt, size, alpha):
        c.setStrokeColor(a(0.6)); c.setLineWidth(2.2); c.setFillColor(a(alpha))
        c.roundRect(x, y, w, h, 18, fill=1, stroke=1)
        p = c.beginPath(); tx = x + (w * 0.22 if tail_left else w * 0.78)
        p.moveTo(tx - 10, y + 1); p.lineTo(tx + (-18 if tail_left else 18), y - 22); p.lineTo(tx + 10, y + 1); c.drawPath(p, fill=1, stroke=0)
        c.setFillColor(a(0.85)); c.setFont("Display", size); c.drawCentredString(x + w / 2, y + h / 2 - size * 0.33, txt)
    bubble(cx - r * 1.25, cy + r * 0.25, r * 1.5, r * 0.75, True, "¡Hola!", 34, 0.12)
    bubble(cx + r * 0.05, cy - r * 0.55, r * 1.35, r * 0.68, False, "¿Qué tal?", 26, 0.18)
    c.setFillColor(a(0.28)); c.setFont("Display", 54)
    c.drawCentredString(cx + r * 1.05, cy + r * 0.95, "ñ"); c.drawCentredString(cx - r * 1.0, cy - r * 0.85, "¿")
    c.setFont("Display", 38); c.drawCentredString(cx + r * 1.35, cy + r * 0.2, "é"); c.drawCentredString(cx - r * 0.4, cy + r * 1.35, "¡")


def art_art(c, cx, cy, r):
    # painter's palette with paint wells, a brush, music notes, and a frame corner
    c.setStrokeColor(a(0.55)); c.setLineWidth(2.4); c.setFillColor(a(0.07))
    p = c.beginPath(); p.moveTo(cx - r, cy)
    p.curveTo(cx - r, cy + r * 0.85, cx + r * 0.6, cy + r * 0.95, cx + r * 0.95, cy + r * 0.3)
    p.curveTo(cx + r * 1.15, cy - r * 0.2, cx + r * 0.65, cy - r * 0.35, cx + r * 0.4, cy - r * 0.2)
    p.curveTo(cx + r * 0.1, cy - r * 0.05, cx + r * 0.25, cy - r * 0.75, cx - r * 0.2, cy - r * 0.8)
    p.curveTo(cx - r * 0.7, cy - r * 0.85, cx - r, cy - r * 0.45, cx - r, cy); p.close(); c.drawPath(p, fill=1, stroke=1)
    c.setFillColor(a(0)); c.circle(cx + r * 0.25, cy - r * 0.42, r * 0.13, fill=0, stroke=1)
    for i, (dx, dy) in enumerate([(-0.65, 0.2), (-0.35, 0.55), (0.05, 0.65), (0.45, 0.5), (0.7, 0.15), (-0.6, -0.35)]):
        c.setFillColor(a(0.18 + 0.08 * (i % 3))); c.circle(cx + dx * r, cy + dy * r, r * 0.12, fill=1, stroke=0)
    # brush
    c.saveState(); c.translate(cx + r * 0.2, cy - r * 1.05); c.rotate(28)
    c.setFillColor(a(0.35)); c.roundRect(-4, 0, 8, r * 1.2, 3, fill=1, stroke=0)
    c.setFillColor(a(0.5)); c.rect(-5, r * 1.2, 10, 12, fill=1, stroke=0)
    p = c.beginPath(); p.moveTo(-5, r * 1.2 + 12); p.curveTo(-6, r * 1.2 + 30, 0, r * 1.2 + 40, 0, r * 1.2 + 44); p.curveTo(0, r * 1.2 + 40, 6, r * 1.2 + 30, 5, r * 1.2 + 12); p.close()
    c.setFillColor(a(0.6)); c.drawPath(p, fill=1, stroke=0); c.restoreState()
    # music notes
    c.setFillColor(a(0.4)); c.setStrokeColor(a(0.4)); c.setLineWidth(2)
    for nx, ny in ((cx + r * 1.05, cy + r * 1.0), (cx + r * 1.4, cy + r * 1.15)):
        c.ellipse(nx - 7, ny - 5, nx + 7, ny + 5, fill=1, stroke=0); c.line(nx + 6, ny, nx + 6, ny + 30)
    c.line(cx + r * 1.05 + 6, cy + r * 1.0 + 30, cx + r * 1.4 + 6, cy + r * 1.15 + 30)
    # frame corner
    c.setStrokeColor(a(0.3)); c.setLineWidth(5); c.line(cx - r * 1.3, cy + r * 1.3, cx - r * 0.6, cy + r * 1.3); c.line(cx - r * 1.3, cy + r * 1.3, cx - r * 1.3, cy + r * 0.6)


def art_data(c, cx, cy, r):
    # scatter with regression line, an item characteristic curve, a bell curve, and code brackets
    import random
    rnd = random.Random(7)
    c.setStrokeColor(a(0.18)); c.setLineWidth(1)
    x0, y0, w, h = cx - r * 1.15, cy - r * 0.9, r * 2.3, r * 1.8
    for i in range(7): c.line(x0, y0 + i * h / 6, x0 + w, y0 + i * h / 6)
    c.setStrokeColor(a(0.5)); c.setLineWidth(2); c.line(x0, y0, x0, y0 + h); c.line(x0, y0, x0 + w, y0)
    c.setFillColor(a(0.42))
    for _ in range(46):
        u = rnd.random(); v = 0.15 + 0.7 * u + rnd.gauss(0, 0.09)
        c.circle(x0 + u * w, y0 + max(0.03, min(0.97, v)) * h, 3.2, fill=1, stroke=0)
    c.setStrokeColor(a(0.7)); c.setLineWidth(2.6); c.line(x0, y0 + 0.15 * h, x0 + w, y0 + 0.85 * h)
    # ICC (logistic) curve
    c.setStrokeColor(a(0.55)); c.setLineWidth(2.2); p = c.beginPath()
    for i in range(61):
        t = -3 + 6 * i / 60; px = x0 + (t + 3) / 6 * w; py = y0 + h * (0.05 + 0.9 / (1 + math.exp(-1.7 * t)))
        (p.moveTo if i == 0 else p.lineTo)(px, py)
    c.setDash(5, 4); c.drawPath(p, stroke=1, fill=0); c.setDash()
    # bell curve above
    c.setStrokeColor(a(0.45)); c.setLineWidth(1.8); p = c.beginPath()
    for i in range(61):
        t = -3 + 6 * i / 60; px = cx - r * 0.9 + (t + 3) / 6 * r * 1.8; py = cy + r * 1.05 + r * 0.55 * math.exp(-t * t / 2)
        (p.moveTo if i == 0 else p.lineTo)(px, py)
    c.drawPath(p, stroke=1, fill=0)
    c.setFillColor(a(0.32)); c.setFont("MonoSemi", 30); c.drawCentredString(cx + r * 1.2, cy + r * 1.25, "</>")
    c.setFont("MonoSemi", 15); c.drawString(x0 - r * 0.35, y0 - 26, "proc means;   df.describe()   summary(x)")


ART = {"spanish": art_spanish, "art": art_art, "data": art_data, "math": art_math, "ela": art_ela, "science": art_science, "social": art_social}


# ---------------------------------------------------------------- pages
def kind_badge(c, x, y, kind, center=False):
    lab = KIND_LABEL[kind].upper(); bw = stringWidth(lab, "BodyBold", 11) + 34
    if center: x -= bw / 2
    teacher = kind == "teacher"
    c.setFillColor(GOLD if teacher else IVORY); c.roundRect(x, y, bw, 28, 14, fill=1, stroke=0)
    text(c, x + bw / 2, y + 10, lab, "BodyBold", 11, INK, "c")
    return bw


def front(c, book, kind):
    t = book.theme; g = book.grade; pal = palette(book); ART_RGB[0] = pal["art"]
    c.setFillColor(pal["bg"]); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # soft diagonal light
    c.setFillColor(a(0.05)); p = c.beginPath(); p.moveTo(PAGE_W * 0.35, PAGE_H); p.lineTo(PAGE_W, PAGE_H); p.lineTo(PAGE_W, PAGE_H * 0.25); p.close(); c.drawPath(p, fill=1, stroke=0)
    # teacher edition gets a gold spine band
    if kind == "teacher":
        c.setFillColor(GOLD); c.rect(0, 0, 0.32 * inch, PAGE_H, fill=1, stroke=0)
    else:
        c.setFillColor(t.dark); c.rect(0, 0, 0.32 * inch, PAGE_H, fill=1, stroke=0)
    # top: wordmark and badge
    text(c, M + 0.2 * inch, PAGE_H - 0.95 * inch, "VENVLEARNING", "BodySemi", 12, pal["ink"])
    c.setFillColor(GOLD); c.rect(M + 0.2 * inch, PAGE_H - 1.08 * inch, 60, 3, fill=1, stroke=0)
    lab = KIND_LABEL[kind].upper(); bw = stringWidth(lab, "BodyBold", 11) + 34
    kind_badge(c, PAGE_W - M - bw, PAGE_H - 1.08 * inch, kind)
    # art
    ART[book.subject](c, PAGE_W * 0.58, PAGE_H * 0.60, 1.55 * inch)
    # title block
    x = M + 0.2 * inch; y = PAGE_H * 0.33
    lines = TITLE_LINES[book.subject]
    mx, my, mr = PAGE_W - M - 0.95 * inch, PAGE_H * 0.33 - 0.15 * inch, 0.82 * inch
    maxw = mx - mr - 18 - x
    size = min(66 if len(lines) == 1 else 58, min(maxw / stringWidth(ln, "Display", 1) for ln in lines))
    for k, ln in enumerate(lines):
        text(c, x, y - k * size * 0.98, ln, "Display", size, pal["ink"])
    yb = y - (len(lines) - 1) * size * 0.98
    # grade medallion
    c.setFillColor(IVORY); c.circle(mx, my, mr, fill=1, stroke=0)
    c.setStrokeColor(GOLD); c.setLineWidth(3); c.circle(mx, my, mr - 7, fill=0, stroke=1)
    text(c, mx, my + 0.28 * inch, book.medal[0], "BodyBold", 11, t.dark, "c")
    text(c, mx, my - 0.5 * inch, book.medal[1], "Display", 72, t.accent, "c")
    # subtitle
    sub = {"textbook": "Lessons, examples, and practice for the whole year", "workbook": "Daily practice, weekly checks, and unit tests",
           "teacher": "Guided lessons, pacing, and complete answer keys", "reader": "Every story, play, and novel for the year in one book"}[kind]
    if book.subject == "data":
        sub = {"textbook": "Statistics, coding, and measurement in 30 minutes a day", "workbook": "Practice, coding exercises, weekly quizzes, and answers"}[kind]
    text(c, x, yb - 0.55 * inch, sub, "BodyMed", 14, pal["sub"])
    scope = f"{len(book.units)} units" if len(book.units) > 1 else f"Unit {book.units[0].num}: {book.units[0].title}"
    text(c, x, yb - 0.85 * inch, f"{book.year} {book.year_label}  ·  {scope}", "Body", 11, a(0.8, (1, 1, 1) if pal["ink"] == WHITE else (pal["ink"].red, pal["ink"].green, pal["ink"].blue)))
    # bottom band
    c.setFillColor(t.dark); c.rect(0, 0, PAGE_W, 0.95 * inch, fill=1, stroke=0)
    stripe(c, 0.95 * inch, 8, INK)
    text(c, M + 0.2 * inch, 0.42 * inch, book.tagline, "Body", 10, colors.Color(1, 1, 1, alpha=0.85))
    right = f"{book.audience.upper()}  ·  {SHORT[book.subject].upper()}" if book.subject != "data" else "SAS  ·  PYTHON  ·  R"
    text(c, PAGE_W - M, 0.42 * inch, right, "BodySemi", 9, GOLD, "r")
    ART_RGB[0] = (1, 1, 1)


def mini_cover(c, x, y, w, h, book, kind, here):
    t = book.theme; pal = palette(book)
    c.setFillColor(pal["bg"]); c.roundRect(x, y, w, h, 4, fill=1, stroke=0)
    c.setFillColor(GOLD if kind == "teacher" else t.dark); c.rect(x, y, 6, h, fill=1, stroke=0)
    c.setFillColor(t.dark); c.rect(x, y, w, h * 0.16, fill=1, stroke=0)
    c.setFillColor(IVORY); c.circle(x + w - 16, y + h * 0.42, 11, fill=1, stroke=0)
    text(c, x + w - 16, y + h * 0.42 - 5, book.medal[1], "Display", 14, t.accent, "c")
    words = TITLE_LINES[book.subject]
    fs = min(12, min((w - 40) / stringWidth(ln, "Display", 1) for ln in words))
    for k, ln in enumerate(words):
        text(c, x + 12, y + h * 0.62 - k * (fs + 1), ln, "Display", fs, pal["ink"])
    text(c, x + 12, y + h - 16, "VENVLEARNING", "BodySemi", 5.5, pal["ink"])
    lab = KIND_LABEL[kind].replace("Student ", "")
    text(c, x + w / 2, y - 14, lab, "BodySemi", 9, INK, "c")
    if here:
        c.setStrokeColor(GOLD); c.setLineWidth(2.5); c.roundRect(x - 5, y - 5, w + 10, h + 10, 6, fill=0, stroke=1)
        text(c, x + w / 2, y - 26, "You are holding this book", "Body", 7.5, MUTED, "c")


def back(c, book, kind):
    t = book.theme; g = book.grade
    c.setFillColor(IVORY); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pal = palette(book)
    c.setFillColor(pal["bg"]); c.rect(0, PAGE_H - 1.55 * inch, PAGE_W, 1.55 * inch, fill=1, stroke=0)
    stripe(c, PAGE_H - 1.55 * inch - 8, 8, INK)
    c.setFillColor(GOLD if kind == "teacher" else t.dark); c.rect(PAGE_W - 0.32 * inch, 0, 0.32 * inch, PAGE_H, fill=1, stroke=0)
    head = f"Grade {g} {SHORT[book.subject]}" if book.subject != "data" else SHORT["data"]
    text(c, M, PAGE_H - 0.75 * inch, head, "Display", 32, pal["ink"])
    text(c, M, PAGE_H - 1.12 * inch, KIND_LABEL[kind] + "  ·  " + book.year + ("  ·  " + book.audience if book.subject == "data" else ""), "BodyMed", 12, pal["sub"])

    body = ParagraphStyle("b", fontName="Body", fontSize=11.5, leading=17, textColor=INK)
    y = PAGE_H - 2.05 * inch; wcol = PAGE_W - 2 * M - 0.3 * inch
    for html in (BLURB[book.subject].format(g=g), (KIND_BLURB_DATA if book.subject == "data" else KIND_BLURB)[kind]):
        para = Paragraph(html, body); _, h = para.wrap(wcol, 400); para.drawOn(c, M, y - h); y -= h + 10

    # two columns: units | what's inside
    y -= 14
    text(c, M, y, "INSIDE THIS YEAR", "BodyBold", 9, t.accent)
    inside = (INSIDE_DATA if book.subject == "data" else INSIDE)[kind]
    colx = M + wcol * 0.56
    text(c, colx, y, "IN THIS BOOK", "BodyBold", 9, t.accent)
    c.setFillColor(GOLD); c.rect(M, y - 7, 40, 2, fill=1, stroke=0); c.rect(colx, y - 7, 40, 2, fill=1, stroke=0)
    yy = y - 26
    us = ParagraphStyle("u", fontName="Body", fontSize=10, leading=13, textColor=INK)
    for u in book.units:
        text(c, M, yy, f"{u.num:02d}", "MonoSemi", 9.5, t.accent)
        para = Paragraph(u.title, us); _, h = para.wrap(wcol * 0.5 - 28, 100); para.drawOn(c, M + 26, yy - h + 10); yy -= max(h, 13) + 5
    yi = y - 26
    for item in inside:
        c.setFillColor(t.accent); c.circle(colx + 4, yi + 3.5, 3, fill=1, stroke=0)
        para = Paragraph(item, us); _, h = para.wrap(wcol * 0.44 - 16, 100); para.drawOn(c, colx + 14, yi - h + 10); yi -= h + 7

    # the complete set
    ys = min(yy, yi) - 30
    w, h = 1.05 * inch, 1.4 * inch
    if ys - h - 40 < 1.3 * inch:   # keep clear of the footer
        ys = 1.3 * inch + h + 40
    text(c, M, ys, "THE COMPLETE SET", "BodyBold", 9, t.accent)
    c.setFillColor(GOLD); c.rect(M, ys - 7, 40, 2, fill=1, stroke=0)
    gap = 0.45 * inch if len(book.kinds) < 4 else 0.3 * inch
    for k, kd in enumerate(book.kinds):
        mini_cover(c, M + k * (w + gap), ys - 20 - h, w, h, book, kd, kd == kind)
    note = ParagraphStyle("n", fontName="Body", fontSize=9.5, leading=13, textColor=MUTED)
    n = {2: "both", 3: "all three", 4: "all four"}[len(book.kinds)]
    para = Paragraph(f"Each lesson has the same number in {n} books, and every day of the year is mapped to its lesson in the "
                     "VenvLearning planner." if "reader" not in book.kinds else
                     "Every ELA lesson names the Reader part and pages to read, and every day of the year is mapped to its lesson in the VenvLearning planner.", note)
    sx = M + len(book.kinds) * (w + gap); _, ph = para.wrap(PAGE_W - sx - M - 0.3 * inch, 200); para.drawOn(c, sx, ys - 20 - h / 2 - ph / 2)

    # footer band
    c.setFillColor(t.dark); c.rect(0, 0, PAGE_W - 0.32 * inch, 0.95 * inch, fill=1, stroke=0)
    stripe(c, 0.95 * inch, 8, INK)
    text(c, M, 0.48 * inch, "VENVLEARNING", "BodySemi", 12, WHITE)
    c.setFillColor(GOLD); c.rect(M, 0.38 * inch, 54, 2.5, fill=1, stroke=0)
    text(c, PAGE_W - M - 0.3 * inch, 0.48 * inch, f"{book.audience}  ·  {SHORT[book.subject]}  ·  {KIND_LABEL[kind]}", "Body", 9.5, colors.Color(1, 1, 1, alpha=0.85), "r")


def make_covers(book, kind, path=None):
    buf = path or io.BytesIO()
    c = _canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))
    c.setTitle(f"{book.audience} {SHORT[book.subject]} · {KIND_LABEL[kind]} · Covers"); c.setAuthor("VenvLearning")
    front(c, book, kind); c.showPage(); back(c, book, kind); c.showPage(); c.save()
    return buf


def attach(book, kind, pdf_path):
    """Wrap pdf_path in place: front cover, blank inside cover, book, blank padding, back cover."""
    from pypdf import PdfReader, PdfWriter
    cov = PdfReader(make_covers(book, kind)); body = PdfReader(pdf_path)
    w = PdfWriter()
    w.add_page(cov.pages[0]); w.add_blank_page(PAGE_W, PAGE_H)
    for pg in body.pages: w.add_page(pg)
    while (len(w.pages) + 1) % 2: w.add_blank_page(PAGE_W, PAGE_H)   # back cover on an even page
    w.add_page(cov.pages[1])
    if body.metadata: w.add_metadata({k: v for k, v in body.metadata.items() if isinstance(v, str)})
    tmp = pdf_path + ".tmp"
    with open(tmp, "wb") as f: w.write(f)
    os.replace(tmp, pdf_path)
