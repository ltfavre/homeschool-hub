"""Build VenvLearning textbooks.  python3 textbooks/build.py math4 [--out DIR]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from engine import Book
from books import build_textbook, build_workbook, build_teacher

BOOKS = {
    "math4": lambda: Book("math", 4, "Grade 4 Mathematics", [__import__("content.math4.unit01", fromlist=["UNIT"]).UNIT]),
}

if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else "math4"
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(HERE, "..", "downloads", "textbooks", key)
    os.makedirs(out, exist_ok=True)
    book = BOOKS[key]()
    stem = f"grade{book.grade}-{book.subject}"
    for kind, fn in (("textbook", build_textbook), ("workbook", build_workbook), ("teacher", build_teacher)):
        path = os.path.join(out, f"{stem}-{kind}.pdf"); fn(book, path); print("wrote", os.path.relpath(path))
