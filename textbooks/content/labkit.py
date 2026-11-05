"""Building blocks for workbook Lab Sheets (science), Activity Sheets (social studies), and Studio Sheets (art).

Each block is a workbook Problem whose figure is a ready-made recording space, so students follow the steps and
record results on the same page instead of on scrap paper. Used by content/sheets/<book>.py.
"""
from engine import Problem, W, inch, colors, Table, TableStyle, ParagraphStyle, P, LINE, WHITE, TA_CENTER

VARIES = "Answers vary. Check that every part is filled in and matches what the student did."
FIG_W = W - 40


class Take:
    """Move a workbook section that already holds this activity's recording space (or its follow-up questions) onto the sheet."""
    def __init__(self, *titles): self.titles = titles


def _grid(t, header, first, rows, row_h, widths=None, label_w=None):
    n = len(header)
    hs = ParagraphStyle("lth", fontName="BodySemi", fontSize=9, leading=11, textColor=t.on_main, alignment=TA_CENTER)
    ls = ParagraphStyle("ltl", fontName="BodyMed", fontSize=9, leading=11, textColor=t.dark)
    data = [[P(h, hs) for h in header]]
    for i in range(rows):
        lab = first[i] if first and i < len(first) else ""
        data.append([P(lab, ls) if lab else ""] + [""] * (n - 1))
    if widths is None:
        lw = label_w if label_w and first else None
        widths = [lw] + [(FIG_W - lw) / (n - 1)] * (n - 1) if lw else [FIG_W / n] * n
    tb = Table(data, colWidths=widths, rowHeights=[None] + [row_h] * rows)
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), t.main), ("BOX", (0, 0), (-1, -1), 0.9, t.main),
                            ("INNERGRID", (0, 0), (-1, -1), 0.5, t.mid), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("BACKGROUND", (0, 1), (0, -1), t.wash if first else WHITE),
                            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return tb


def T(*header, rows=None, first=None, label="Record your results in the table.", row_h=24, answer=VARIES, label_w=1.6 * inch):
    """A blank data table. first: labels printed down the first column (one per row)."""
    n = rows or (len(first) if first else 4)
    return Problem(label, answer, space=0, wide=True, fig=lambda t: _grid(t, header, first, n, row_h, label_w=label_w))


def CER(question=None, answer="Claim answers the question; evidence uses the student's own data; reasoning explains why the evidence supports the claim."):
    """Claim, Evidence, Reasoning frame."""
    lab = "Write a CER" + (f": {question}" if question else " about your results.")
    rows = [("Claim", "My answer to the question"), ("Evidence", "Data from my investigation"), ("Reasoning", "Why my evidence supports my claim")]
    def fig(t):
        ks = ParagraphStyle("ck", fontName="BodySemi", fontSize=10, leading=12, textColor=t.dark)
        ss = ParagraphStyle("cs", fontName="Body", fontSize=8, leading=10, textColor=colors.HexColor("#5F5B56"))
        data = [[[P(k, ks), P(s, ss)], ""] for k, s in rows]
        tb = Table(data, colWidths=[1.25 * inch, FIG_W - 1.25 * inch], rowHeights=[46, 58, 58])
        tb.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.9, t.main), ("INNERGRID", (0, 0), (-1, -1), 0.5, t.mid),
                                ("BACKGROUND", (0, 0), (0, -1), t.wash), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 5)]))
        return tb
    return Problem(lab, answer, space=0, wide=True, fig=fig)


def BOX(label, h=170, answer=VARIES):
    """A drawing or sketching space."""
    return Problem(label, answer, space=h, wide=True)


def LN(label, n=3, answer=VARIES):
    """Writing lines."""
    return Problem(label, answer, space=0, lines=n, wide=True)


def GRAPH(label, x, y, h=170, answer=VARIES):
    """A blank graph with labeled axes and a light grid."""
    from reportlab.graphics.shapes import Drawing, Line, String, Rect
    def fig(t):
        d = Drawing(FIG_W, h)
        ox, oy, gw, gh = 34, 22, FIG_W - 44, h - 30
        d.add(Rect(ox, oy, gw, gh, strokeColor=None, fillColor=WHITE))
        step = 14
        for i in range(1, int(gw // step) + 1): d.add(Line(ox + i * step, oy, ox + i * step, oy + gh, strokeColor=LINE, strokeWidth=0.4))
        for j in range(1, int(gh // step) + 1): d.add(Line(ox, oy + j * step, ox + gw, oy + j * step, strokeColor=LINE, strokeWidth=0.4))
        d.add(Line(ox, oy, ox + gw, oy, strokeColor=t.dark, strokeWidth=1.2)); d.add(Line(ox, oy, ox, oy + gh, strokeColor=t.dark, strokeWidth=1.2))
        d.add(String(ox + gw / 2, 6, x, fontName="BodyMed", fontSize=9, fillColor=t.dark, textAnchor="middle"))
        s = String(0, 0, y, fontName="BodyMed", fontSize=9, fillColor=t.dark, textAnchor="middle")
        from reportlab.graphics.shapes import Group
        g = Group(s); g.translate(14, oy + gh / 2); g.rotate(90); d.add(g)
        return d
    return Problem(label, answer, space=0, wide=True, fig=fig)

