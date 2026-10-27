"""Shared helpers for Science and Social Studies unit files (two lessons a week)."""
from engine import Section, Problem, Check
from content.te import TE
from content.elakit import S, MC, OR, SA, DRAW, rubric_for, make_test
from content.sched import schedule2, UNIT_MONDAYS

_L = lambda x: x if isinstance(x, list) else [x]


def sflow(engage, investigate, explain, guided, independent="Workbook lesson pages: Warm-Up through Exit Ticket.",
          exit_="Student completes the Exit Ticket alone. Check it before the next lesson."):
    return [("Engage", 5, _L(engage)), ("Investigate", 15, _L(investigate)), ("Explain", 10, _L(explain)),
            ("Guided Practice", 7, _L(guided)), ("Independent", 10, _L(independent)), ("Exit Ticket", 3, _L(exit_))]


def ssflow(warm, read, analyze, guided, independent="Workbook lesson pages: Warm-Up through Exit Ticket.",
           exit_="Student completes the Exit Ticket alone. Check it before the next lesson."):
    return [("Warm-Up", 5, _L(warm)), ("Read and Discuss", 15, _L(read)), ("Analyze", 10, _L(analyze)),
            ("Guided Practice", 7, _L(guided)), ("Independent", 10, _L(independent)), ("Exit Ticket", 3, _L(exit_))]


def tsci(obj, std, mat, engage, investigate, explain, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, sflow(engage, investigate, explain, guided, **k), mis, sup, ext)


def tss(obj, std, mat, warm, read, analyze, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, ssflow(warm, read, analyze, guided, **k), mis, sup, ext)


def weeks_for(unit, lessons, checks, review, test, subject):
    return schedule2(lessons, UNIT_MONDAYS[unit], checks, review, test, days=(0, 2) if subject == "science" else (1, 3))


def check(title, sections, minutes=15):
    return Check(title, sections, minutes=minutes)


def review(title, sections, minutes=40, note="Homework or a study session before the test."):
    return Check(title, sections, kind="review", minutes=minutes, teacher_note=note)
