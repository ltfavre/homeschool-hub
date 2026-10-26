"""Renders a Book (see engine.py) into the student textbook, student workbook and teacher edition."""
from engine import *


# ================================================================ shared pieces
def lesson_header(t, L, kind_note=None):
    out = [P(f"UNIT {L.num.split('.')[0]}  ·  LESSON {L.num}  ·  {L.standard}" + (f"  ·  {kind_note}" if kind_note else ""), t.eyebrow),
           toc_heading(f"Lesson {L.num}: {L.title}", t.h1, 1, running=f"Lesson {L.num} · {L.title}")]
    return out


def vocab_panel(t, vocab, title="Words to Know"):
    rows = [[P(f"<b>{w}</b>", t.cellb), P(d, t.cell)] for w, d in vocab]
    tb = Table(rows, colWidths=[1.45 * inch, W - 1.45 * inch - 26])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    return panel([P(title.upper(), t.eyebrow), tb], SAGE_WASH, left_bar=HUNTER)


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
            out.append(Spacer(1, 2)); out.append(panel([P(b.title.upper(), t.eyebrow), P(b.t, t.boxt)], t.wash, left_bar=t.main)); out.append(Spacer(1, 8))
        elif isinstance(b, WatchOut):
            out.append(Spacer(1, 2)); out.append(panel([P("WATCH OUT", ParagraphStyle("wo", parent=t.eyebrow, textColor=FOREST)), P(b.t, t.boxt)],
                                                       colors.HexColor("#FBF3DC"), left_bar=GOLD)); out.append(Spacer(1, 8))
        elif isinstance(b, Example):
            out.append(Spacer(1, 4)); out.append(example_box(t, b)); out.append(Spacer(1, 8))
        elif isinstance(b, Vocab):
            out.append(vocab_panel(t, b.items)); out.append(Spacer(1, 8))
    return out


def example_box(t, ex):
    inner = [P(f"WORKED EXAMPLE  ·  {ex.title.upper()}", t.eyebrow), P(ex.problem, ParagraphStyle("exq", parent=t.boxt, fontName="BodySemi"))]
    if ex.fig: inner += [Spacer(1, 3), centered(ex.fig(t), W - 30), Spacer(1, 3)]
    num = ParagraphStyle("st", parent=t.boxt, leftIndent=22, bulletIndent=0)
    for i, s in enumerate(ex.steps, 1):
        inner.append(Paragraph(s, num, bulletText=f"{i}"))
    inner.append(P(f"<b>Answer:</b> {ex.answer}", ParagraphStyle("exa", parent=t.boxt, textColor=t.dark, spaceBefore=3)))
    # one row per paragraph so a long example can continue on the next page
    head = [inner[0], inner[1]]
    rows = [[head]] + [[f] for f in inner[2:]]
    tb = Table(rows, colWidths=[W])
    tb.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1, t.main), ("BACKGROUND", (0, 0), (-1, -1), WHITE),
                            ("LINEABOVE", (0, 0), (-1, 0), 4, t.main), ("LEFTPADDING", (0, 0), (-1, -1), 12),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                            ("TOPPADDING", (0, 0), (-1, 0), 8), ("BOTTOMPADDING", (0, -1), (-1, -1), 8)]))
    return tb


def try_it_box(t, L, with_answers=False):
    inner = [P("TRY IT", t.eyebrow), P("Work these in your notebook or on scrap paper. Then check with your teacher." if not with_answers
                                        else "Answers are shown in red.", t.small)]
    for i, pr in enumerate(L.try_it, 1):
        row = [P(f"<b>{i}.</b>  {pr.prompt}", t.boxt)]
        if pr.fig: row += [centered(pr.fig(t), W - 40)]
        if pr.choices: row.append(P("    ".join(f"<b>{chr(65 + k)}.</b> {c}" for k, c in enumerate(pr.choices)), t.boxt))
        if with_answers: row.append(P(f"Answer: {pr.answer}", t.answer))
        inner += row
    inner.append(P(f"More practice: <b>Workbook, Lesson {L.num}</b>.", t.small))
    return panel(inner, t.wash, border=t.mid)


# ================================================================ TEXTBOOK
def textbook_lesson(t, L, teacher=False):
    out = lesson_header(t, L)
    out.append(P(L.i_can, t.ican))
    if L.vocab: out += [vocab_panel(t, L.vocab), Spacer(1, 8)]
    out.append(panel([P("LET'S EXPLORE", t.eyebrow), P(L.launch, t.boxt)], IVORY, border=LINE)); out.append(Spacer(1, 8))
    out += render_blocks(t, L.learn, teacher)
    out.append(Spacer(1, 4)); out.append(try_it_box(t, L, with_answers=teacher))
    if L.summary:
        out += [Spacer(1, 8), panel([P("LESSON SUMMARY", t.eyebrow), P(L.summary, t.boxt)], SAGE_WASH, left_bar=HUNTER)]
    return out


def unit_opener(t, U, doc, kind):
    w = ParagraphStyle("ow", parent=t.h1, textColor=WHITE, fontSize=36, leading=40)
    e = ParagraphStyle("oe", parent=t.eyebrow, textColor=BLUSH, fontSize=10)
    s = ParagraphStyle("os", parent=t.body, textColor=IVORY, fontSize=13, leading=18)
    out = [NextPageTemplate("opener"), SetOpenerNum(doc, U.num), PageBreak(), Running(f"Unit {U.num} · {U.title}"),
           Spacer(1, 0.25 * inch), P(f"UNIT {U.num}" + ("  ·  TEACHER OVERVIEW" if kind == "teacher" else ""), e),
           toc_heading(U.title, w, 0), P(U.subtitle, s), SpaceTo(3.65 * inch), NextPageTemplate("body")]
    return out


def unit_intro_student(t, U):
    out = [P(U.overview, t.body), P("In this unit you will…", t.h3)] + bullets(U.big_ideas, t.bullet)
    if U.real_world: out += [Spacer(1, 6), panel([P("MATH IN REAL LIFE" if t.subject == "math" else "WHY IT MATTERS", t.eyebrow), P(U.real_world, t.boxt)], t.wash, left_bar=t.main)]
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


def front_matter(t, book, doc, kind):
    out = [NextPageTemplate("body"), PageBreak()]
    intro = {
        "textbook": ["How to use this book",
                     "Each lesson starts with an <b>I can</b> goal and a <b>Let's Explore</b> question. Read the lesson with your teacher, "
                     "study the <b>Worked Examples</b> step by step, and try the <b>Try It</b> problems. Your practice pages are in your "
                     "<b>Student Workbook</b>, labeled with the same lesson number.",
                     ["<b>Key Idea</b> boxes hold the most important rule or fact. Learn these.",
                      "<b>Watch Out</b> boxes warn you about common mistakes.",
                      "Every Friday there is a short <b>Weekly Check</b> in your workbook. The last Friday of a unit is the <b>Unit Test</b>."]],
        "workbook": ["How to use this workbook",
                     "Every lesson in your textbook has matching practice pages here. Show your thinking in the work space. "
                     "When a problem has an answer line, write your final answer there.",
                     ["<b>Warm-Up</b> reviews something you already know.",
                      "<b>Practice</b> uses today's lesson.", "<b>Think Deeper</b> problems ask you to explain or find a mistake.",
                      "<b>Exit Ticket</b> shows your teacher what you learned today."]],
        "teacher": ["How to use this Teacher Edition",
                    "This book holds everything needed to teach the course: unit overviews, a plan for every lesson with what to say "
                    "and do, the student lesson with Try It answers, and answer keys for every workbook page, weekly check and unit test.",
                    ["<b>Daily routine (about 45–55 minutes):</b> Warm-Up 5 · Teach 15 · Guided Practice 10 · Independent Practice 15 · Exit Ticket 5.",
                     "<b>Say:</b> lines are a suggested script. Use your own words.",
                     "Monday–Thursday are lessons. Friday is the <b>Weekly Check</b> (about 20 minutes), then corrections or a project.",
                     "Dates match the VenvLearning lesson plans for the 2026–2027 school year."]],
    }[kind]
    out += [P(intro[0], t.h2), P(intro[1], t.body)] + bullets(intro[2], t.bullet)
    out += [Spacer(1, 10), P("Contents", t.h2), toc_flowable(t)]
    return out


def build_textbook(book, path):
    t = book.theme; doc = Doc(path, book, "textbook")
    story = [Spacer(1, 1)] + front_matter(t, book, doc, "textbook")
    for U in book.units:
        story += unit_opener(t, U, doc, "textbook") + unit_intro_student(t, U)
        for L in U.lessons:
            story += [PageBreak()] + textbook_lesson(t, L)
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
        if grid and t.subject == "math":
            c.setStrokeColor(GRID); c.setLineWidth(0.35); s = 12
            x = s
            while x < ww: c.line(x, 1, x, hh - 1); x += s
            y = s
            while y < hh: c.line(1, y, ww - 1, y); y += s
        elif not grid or t.subject == "ela":
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
    badge = Table([[P(f"<b>{num}</b>", ParagraphStyle("bd", parent=t.cell, textColor=WHITE, alignment=TA_CENTER))]], colWidths=[18], rowHeights=[18])
    badge.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), t.main), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("ROUNDEDCORNERS", [9, 9, 9, 9])]))
    body = [P(pr.prompt, t.prob)]
    if pr.fig: body += [Spacer(1, 3), pr.fig(t), Spacer(1, 2)]
    if pr.choices:
        body.append(Spacer(1, 2))
        for k, ch in enumerate(pr.choices):
            body.append(P(f"<font name='BodySemi' color='#{t.main.hexval()[2:]}'>{chr(65 + k)}</font>   {ch}", t.prob))
    inner_w = w - 26
    if pr.lines: body += [Spacer(1, 2), write_lines(t, inner_w, pr.lines)]
    elif pr.space: body += [Spacer(1, 3), work_space(t, inner_w, max(pr.space, 26))]
    elif not pr.choices and not pr.fig: body += [Spacer(1, 2), answer_line(t, min(inner_w, 170))]
    if show_answer: body.append(P(f"Answer: {pr.answer}", t.answer))
    tb = Table([[badge, body]], colWidths=[24, w - 24])
    tb.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return tb


def section_grid(t, sec, start, show_answer=False):
    head = [P(sec.title, t.h3)]
    if sec.intro: head.append(P(sec.intro, t.body))
    out = []
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


def workbook_lesson(t, L):
    out = [P(f"UNIT {L.num.split('.')[0]}  ·  LESSON {L.num}  ·  PRACTICE", t.eyebrow),
           toc_heading(f"Lesson {L.num}: {L.title}", ParagraphStyle("wh", parent=t.h2, spaceBefore=0), 1, running=f"Lesson {L.num} Practice · {L.title}"),
           name_date(t), Spacer(1, 6), P(L.i_can, ParagraphStyle("ic2", parent=t.ican, fontSize=12, leading=16))]
    n = 1
    for sec in L.practice:
        part, n = section_grid(t, sec, n)
        out += part
    return out


def check_pages(t, C, show_answer=False, teacher=False):
    tag = "UNIT TEST" if C.kind == "test" else ("UNIT REVIEW" if C.kind == "review" else "WEEKLY CHECK")
    out = [P(f"{tag}" + (f"  ·  {C.date}" if C.date else "") + (f"  ·  ABOUT {C.minutes} MINUTES" if C.minutes else ""), t.eyebrow),
           toc_heading(C.title + (" — Answer Key" if teacher else ""), ParagraphStyle("ch", parent=t.h2, spaceBefore=0), 1, running=C.title)]
    if not teacher: out += [name_date(t), Spacer(1, 6)]
    if C.kind == "test" and not teacher:
        total = sum(p.points for s in C.sections for p in s.problems)
        out.append(P(f"Show your work. This test has {total} points.", t.body))
    n = 1
    for sec in C.sections:
        part, n = section_grid(t, sec, n, show_answer)
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
            story += [PageBreak()] + workbook_lesson(t, L)
            if L.num in week_checks:
                story += [PageBreak()] + check_pages(t, week_checks[L.num])
        story += [PageBreak()] + check_pages(t, U.review)
        story += [PageBreak()] + check_pages(t, U.test)
    doc.multiBuild(story)


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
        a = f"<font name='BodySemi' color='#{t.main.hexval()[2:]}'>{ans}</font>" + (f"<br/><font size='8.5' color='#5F5B56'>{note}</font>" if note else "")
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


def teacher_lesson(t, L):
    T = L.teacher
    out = lesson_header(t, L, kind_note=f"{L.date}" if L.date else None)
    out.append(P(L.i_can, t.ican))
    out.append(info_table(t, [("Objective", T["objective"]), ("Standard", L.standard + " — " + T.get("standard_text", "")),
                              ("Date", L.date or "—"), ("Time", T.get("time", "About 50 minutes")),
                              ("Materials", T["materials"]), ("Get ready", T.get("prep", "Read the student lesson and work the Try It problems."))]))
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
    out += [PageBreak(), P(f"STUDENT LESSON {L.num} · WITH ANSWERS", t.eyebrow)]
    out += textbook_lesson_compact(t, L)
    out += [Spacer(1, 8)] + problems_key(t, L.practice, f"Workbook Answer Key · Lesson {L.num}")
    return out


def textbook_lesson_compact(t, L):
    out = [P(f"Lesson {L.num}: {L.title}", t.h2)]
    out.append(panel([P("LET'S EXPLORE", t.eyebrow), P(L.launch, t.boxt)], IVORY, border=LINE)); out.append(Spacer(1, 6))
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
            story += [PageBreak()] + teacher_lesson(t, L)
            if L.num in week_checks:
                C = week_checks[L.num]
                story += [PageBreak()] + check_teacher(t, C)
        story += [PageBreak()] + check_teacher(t, U.review)
        story += [PageBreak()] + check_teacher(t, U.test)
    doc.multiBuild(story)


def check_teacher(t, C):
    tag = {"test": "UNIT TEST", "review": "UNIT REVIEW"}.get(C.kind, "WEEKLY CHECK")
    out = [P(tag + (f"  ·  {C.date}" if C.date else ""), t.eyebrow),
           toc_heading(C.title + " — Answer Key", ParagraphStyle("ch", parent=t.h2, spaceBefore=0), 1, running=C.title + " Key")]
    if C.teacher_note: out.append(P(C.teacher_note, t.body))
    out += problems_key(t, C.sections, "Answers")
    if C.rubric:
        out += [P("Scoring", t.h3), table(t, [["Score", "What it means / next step"]] + C.rubric, [1.2 * inch, W - 1.2 * inch])]
    return out
