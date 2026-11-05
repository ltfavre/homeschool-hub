"""Recording layouts for each lesson's hands-on activity, by book ("sci4", "ss7", "art4", ...) and lesson number.
Each value is a list of content.labkit blocks (T, CER, BOX, LN, GRAPH, Take). See books.lab_section."""
import importlib


def sheet_for(book, num):
    try:
        mod = importlib.import_module(f"content.sheets.{book}")
    except ModuleNotFoundError:
        return None
    return mod.SHEETS.get(num)
