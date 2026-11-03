"""Exports what the Tutor needs to know from the VenvLearning textbooks and Readers, one file per grade:

    python tutor/export_knowledge.py OUT_DIR

OUT_DIR/grade4.json and grade7.json hold every lesson (explanations, worked examples, Your Turn and workbook
problems with their answers, teacher notes), every weekly check and unit test, and the text of every Reader section.
The files include answer keys, so OUT_DIR must be the Tutor's private data folder, never this repository (the whole
repository is published to the website)."""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "textbooks"))
from build import BOOKS  # noqa: E402
from books import workbook_sections, with_directions  # noqa: E402

KEYS = {4: ["math4", "ela4", "sci4", "ss4", "art4"], 7: ["math7", "ela7", "sci7", "ss7", "art7"]}
SUBJECT = {"science": "science", "social": "social", "math": "math", "ela": "ela", "art": "art"}


def plain(s):
    """Markup-free text."""
    s = re.sub(r"<br\s*/?>", "\n", str(s or ""))
    s = re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").replace("&amp;", "&").replace("\\n", "\n")
    return re.sub(r"[ \t]+", " ", s).strip()


def cell(v):
    if isinstance(v, (list, tuple)): return " ".join(cell(x) for x in v)
    if hasattr(v, "getPlainText"): return plain(v.getPlainText())
    if hasattr(v, "text"): return plain(v.text)
    return plain(v) if isinstance(v, (str, int, float)) else ""


def figure(fig, theme):
    """A figure as text when it is a table; drawings have no text."""
    try:
        f = fig.fn(theme)
    except Exception:
        return ""
    rows = getattr(f, "_cellvalues", None)
    if not rows: return "[diagram]"
    return "\n".join(" | ".join(cell(c) for c in row) for row in rows)


def problem(p):
    d = {"q": plain(p.prompt), "answer": plain(p.answer)}
    if p.choices: d["choices"] = [plain(c) for c in p.choices]
    if p.note: d["note"] = plain(p.note)
    return d


def passage(p):
    return {"title": plain(p.title), "text": "\n\n".join(plain(x.lstrip(">")) for x in p.paras), "source": plain(p.source or "")}


def block(b, theme):
    kind = type(b).__name__
    if kind in ("Text", "Heading", "WatchOut", "OnTheJob"): return plain(b.t)
    if kind == "KeyIdea": return f"KEY IDEA: {plain(b.t)}"
    if kind == "Callout": return f"{plain(b.label)}: {plain(b.t)}"
    if kind == "Bullets": return "\n".join("- " + plain(x) for x in b.items)
    if kind == "Figure": return figure(b, theme)
    if kind == "Example":
        return "\n".join([f"EXAMPLE: {plain(b.title)}", f"Problem: {plain(b.problem)}"] + [f"  {i}. {plain(s)}" for i, s in enumerate(b.steps, 1)] + [f"Answer: {plain(b.answer)}"])
    if kind == "Passage":
        p = passage(b); return f"PASSAGE: {p['title']}\n{p['text']}\n({p['source']})"
    if kind == "ReaderAssign": return f"READ IN YOUR READER: {plain(b.book)}, {plain(b.section)}. As you read: {plain(b.focus)}"
    if kind == "Vocab": return "\n".join(f"{plain(w)}: {plain(d)}" for w, d in b.items)
    if kind == "Investigate":
        return "\n".join([f"INVESTIGATION: {plain(b.title)}", f"Question: {plain(b.question)}", "Materials: " + ", ".join(plain(m) for m in b.materials)] + [f"  {i}. {plain(s)}" for i, s in enumerate(b.steps, 1)])
    if kind in ("Beside",): return "\n".join(plain(t) for t in b.texts)
    return ""


def section(s):
    d = {"title": plain(s.title), "items": [problem(p) for p in s.problems]}
    if s.intro: d["directions"] = plain(s.intro)
    if s.passage: d["passage"] = passage(s.passage)
    return d


def export_book(key):
    book = BOOKS[key](); out = {"lessons": [], "assessments": []}
    for U in book.units:
        for L in U.lessons:
            t = L.teacher or {}
            out["lessons"].append({
                "id": f"{book.subject}-{L.num}", "subject": book.subject, "book": book.title, "unit": U.num, "unit_title": plain(U.title),
                "num": L.num, "title": plain(L.title), "date": L.date, "i_can": plain(L.i_can), "standard": plain(L.standard),
                "vocab": [[plain(w), plain(d)] for w, d in (L.vocab or [])], "get_ready": plain(L.launch),
                "learn": "\n\n".join(x for x in (block(b, book.theme) for b in L.learn) if x),
                "your_turn": [problem(p) for p in L.try_it], "workbook": [section(s) for s in workbook_sections(book.theme, L)],
                "summary": plain(L.summary or ""),
                "teacher": {k: [plain(x) for x in t.get(k, [])] for k in ("misconceptions", "support", "extend")}})
        for C in list(U.checks) + [U.review, U.test]:
            out["assessments"].append({"subject": book.subject, "unit": U.num, "unit_title": plain(U.title), "kind": C.kind, "title": plain(C.title),
                                       "date": C.date, "sections": [section(s) for s in with_directions(book.theme, C.sections, "C", plain(C.title))]})
    return out


def reader_text(grade):
    """Every Reader section's text: A Christmas Carol from its source text, the other parts from the built Reader PDF."""
    import pypdfium2
    idx_path = os.path.join(ROOT, "downloads", "textbooks", f"grade{grade}-ela-reader.index.json")
    idx = json.load(open(idx_path, encoding="utf-8"))
    pdf = pypdfium2.PdfDocument(os.path.join(ROOT, "downloads", "textbooks", f"grade{grade}-ela-reader.pdf"))
    out = []
    for key, part in idx["parts"].items():
        if key == "carol":
            from readers.carol import INTRO, load
            out.append({"part": part["title"], "section": INTRO["title"], "printed": part["sections"][INTRO["title"]]["printed"], "text": "\n\n".join(plain(p) for p in INTRO["paras"])})
            for s in load():
                out.append({"part": part["title"], "section": s["name"], "printed": part["sections"][s["name"]]["printed"],
                            "words_to_know": s["words"], "text": "\n\n".join(s["paras"])})
            continue
        for name, sec in part["sections"].items():
            a, b = sec["pdf"]
            text = "\n".join(pdf[i - 1].get_textpage().get_text_range() for i in range(a, b + 1)).replace("\r", "")
            out.append({"part": part["title"], "section": name, "printed": sec["printed"], "text": re.sub(r"\n{3,}", "\n\n", text).strip()})
    pdf.close()
    return out


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for grade, keys in KEYS.items():
        data = {"grade": grade, "lessons": [], "assessments": [], "reader": reader_text(grade)}
        for k in keys:
            b = export_book(k); data["lessons"] += b["lessons"]; data["assessments"] += b["assessments"]
        json.dump(data, open(os.path.join(out_dir, f"grade{grade}.json"), "w", encoding="utf-8"), ensure_ascii=False)
        print(f"grade {grade}: {len(data['lessons'])} lessons, {len(data['assessments'])} checks/tests, {len(data['reader'])} Reader sections")


if __name__ == "__main__":
    main(sys.argv[1])
