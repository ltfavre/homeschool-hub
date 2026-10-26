"""Build VenvLearning textbooks.  python3 textbooks/build.py math4 [--out DIR]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from engine import Book
from books import build_textbook, build_workbook, build_teacher

import importlib, glob


def units(key):
    """Every content/<key>/unitNN.py that defines UNIT, in order."""
    mods = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(HERE, "content", key, "unit[0-9][0-9].py")))
    return [importlib.import_module(f"content.{key}.{m}").UNIT for m in mods]


BOOKS = {
    "math4": lambda: Book("math", 4, "Grade 4 Mathematics", units("math4")),
}

if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else "math4"
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(HERE, "..", "downloads", "textbooks", key)
    os.makedirs(out, exist_ok=True)
    book = BOOKS[key]()
    stem = f"grade{book.grade}-{book.subject}"
    kinds = (("textbook", build_textbook), ("workbook", build_workbook), ("teacher", build_teacher))
    if "--units" not in sys.argv or "--all" in sys.argv:
        for kind, fn in kinds:
            path = os.path.join(out, f"{stem}-{kind}.pdf"); fn(book, path); print("wrote", os.path.relpath(path))
    if "--units" in sys.argv:
        # one printable booklet per unit, for binders
        for U in book.units:
            part = Book(book.subject, book.grade, f"{book.title} · Unit {U.num}", [U])
            for kind, fn in kinds:
                path = os.path.join(out, "units", f"{stem}-unit{U.num:02d}-{kind}.pdf"); os.makedirs(os.path.dirname(path), exist_ok=True)
                fn(part, path)
            print("wrote unit", U.num)
