"""Written directions for every Your Turn set and every workbook or check section whose questions don't say what to do.
One module per book. Keys:
  "Y|<lesson>"                       the lesson's Your Turn questions (also Part A of the workbook lesson)
  "S|<lesson>|<section title>"       a workbook practice section
  "C|<check title>|<section title>"  a section of a weekly check, unit review, or unit test
Each direction tells the student exactly what to do and where to write."""
import importlib

DIRECTIONS = {}
for _k in ("math4", "math7", "ela4", "ela7", "sci4", "sci7", "ss4", "ss7", "art4", "art7"):
    try:
        DIRECTIONS[_k] = importlib.import_module(f"content.directions.{_k}").D
    except ModuleNotFoundError:
        DIRECTIONS[_k] = {}
