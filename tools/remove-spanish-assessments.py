#!/usr/bin/env python3
"""Takes Spanish out of the Friday gap quizzes and module tests dated on or after CUTOFF (Spanish is not taught for the rest of
the 2026-27 year). Safe to re-run.

    python3 tools/remove-spanish-assessments.py

* assessment-student.json parts: drops each "Spanish" section and the Spanish wording in coverage and standards.
* assessments/khan-*-student.pdf and -key.pdf: drops the last page, which holds only the Spanish section.
* The Khan_Primary_Grade_{4,7}_Gap_* year bundles: drops those quizzes' Spanish pages.

The PDF cover pages still mention Spanish in their printed coverage and standards lines; the generator for these PDFs is
not in this repository, so that text is left as printed."""
import json, os, re
import pikepdf, pypdfium2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUTOFF = "2026-11-02"
SPANISH_PAGE = re.compile(r"\| (?:STUDENT|TEACHER KEY)\r?\nSpanish - \d+ points")


def page_texts(path):
    pdf = pypdfium2.PdfDocument(path)
    out = [pdf[i].get_textpage().get_text_range() for i in range(len(pdf))]
    pdf.close()
    return out


def drop_pages(path, keep):
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    for i in reversed(range(len(pdf.pages))):
        if not keep(i): del pdf.pages[i]
    pdf.save(path)


def main():
    manifest = json.load(open(os.path.join(ROOT, "assessment-student.json")))
    titles, n_sections = {}, 0
    for part in manifest["_parts"]:
        path = os.path.join(ROOT, part.lstrip("/"))
        data = json.load(open(path, encoding="utf-8"))
        for a in data.values():
            if a.get("date", "") < CUTOFF: continue
            titles[a["title"]] = a["id"]
            before = len(a.get("sections", []))
            a["sections"] = [s for s in a.get("sections", []) if s.get("title") != "Spanish"]
            n_sections += before - len(a["sections"])
            if a.get("coverage"): a["coverage"] = a["coverage"].replace("social studies, and Spanish gap work", "and social studies gap work")
            if a.get("standards"): a["standards"] = re.sub(r"\s*\|\s*Spanish:[^|]*", "", a["standards"])
        json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    n_pdfs = 0
    for aid in titles.values():
        for kind in ("student", "key"):
            path = os.path.join(ROOT, "assessments", f"{aid}-{kind}.pdf")
            if not os.path.exists(path): continue
            texts = page_texts(path)
            if len(texts) > 1 and SPANISH_PAGE.search(texts[-1]):
                drop_pages(path, lambda i, n=len(texts): i < n - 1); n_pdfs += 1
    n_bundle = 0
    for g in ("4", "7"):
        for name in (f"Khan_Primary_Grade_{g}_Gap_Assessments_2026-2027.pdf", f"Khan_Primary_Grade_{g}_Gap_Answer_Keys_2026-2027.pdf"):
            path = os.path.join(ROOT, "assessments", name)
            texts = page_texts(path)
            drop = {i for i, t in enumerate(texts) if SPANISH_PAGE.search(t) and any(f"{title} |" in t for title in titles)}
            if drop: drop_pages(path, lambda i: i not in drop); n_bundle += len(drop)
    print(f"{n_sections} Spanish sections removed from {len(titles)} assessments; {n_pdfs} quiz PDFs and {n_bundle} bundle pages trimmed")


if __name__ == "__main__":
    main()
