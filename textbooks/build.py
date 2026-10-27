"""Build VenvLearning textbooks.  python3 textbooks/build.py math4 [--out DIR]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from engine import Book
from books import build_textbook, build_workbook, build_teacher
from covers import attach

import importlib, glob


def units(key):
    """Every content/<key>/unitNN.py that defines UNIT, in order."""
    mods = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(HERE, "content", key, "unit[0-9][0-9].py")))
    return [importlib.import_module(f"content.{key}.{m}").UNIT for m in mods]


BOOKS = {
    "math4": lambda: Book("math", 4, "Grade 4 Mathematics", units("math4")),
    "math7": lambda: Book("math", 7, "Grade 7 Mathematics", units("math7")),
    "ela4": lambda: Book("ela", 4, "Grade 4 English Language Arts", units("ela4")),
    "ela7": lambda: Book("ela", 7, "Grade 7 English Language Arts", units("ela7")),
    "sci4": lambda: Book("science", 4, "Grade 4 Science", units("sci4")),
    "sci7": lambda: Book("science", 7, "Grade 7 Science", units("sci7")),
    "ss4": lambda: Book("social", 4, "Grade 4 Social Studies", units("ss4")),
    "ss7": lambda: Book("social", 7, "Grade 7 Social Studies", units("ss7")),
    "span4": lambda: Book("spanish", 4, "Grade 4 Spanish", units("span4")),
    "span7": lambda: Book("spanish", 7, "Grade 7 Spanish (Spanish 1A)", units("span7")),
    "art4": lambda: Book("art", 4, "Grade 4 Art", units("art4")),
    "art7": lambda: Book("art", 7, "Grade 7 Art", units("art7")),
    "data": lambda: Book("data", "pro", "Data Science & Psychometrics", units("data"), audience="Professional Learning", kinds=("textbook", "workbook"),
                         medal=("YEAR", "1"), tagline="A VenvLearning professional learning curriculum", year_label="Professional Learning"),
}

if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else "math4"
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(HERE, "..", "downloads", "textbooks", key)
    os.makedirs(out, exist_ok=True)
    book = BOOKS[key]()
    stem = f"grade{book.grade}-{book.subject}" if book.subject != "data" else "data-science-psychometrics"
    kinds = tuple(k for k in (("textbook", build_textbook), ("workbook", build_workbook), ("teacher", build_teacher)) if k[0] in book.kinds)
    if "--units" not in sys.argv or "--all" in sys.argv:
        for kind, fn in kinds:
            path = os.path.join(out, f"{stem}-{kind}.pdf"); fn(book, path); attach(book, kind, path); print("wrote", os.path.relpath(path))
    if "--units" in sys.argv:
        # one printable booklet per unit, for binders
        for U in book.units:
            part = Book(book.subject, book.grade, f"{book.title} · Unit {U.num}", [U], audience=book.audience, kinds=book.kinds, medal=book.medal,
                        tagline=book.tagline, year_label=book.year_label)
            for kind, fn in kinds:
                path = os.path.join(out, "units", f"{stem}-unit{U.num:02d}-{kind}.pdf"); os.makedirs(os.path.dirname(path), exist_ok=True)
                fn(part, path); attach(part, kind, path)
            print("wrote unit", U.num)
