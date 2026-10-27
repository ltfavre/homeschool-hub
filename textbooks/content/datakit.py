"""Helpers for the Data Science & Psychometrics (professional learning) units."""
from engine import Section, Problem, Check
from content.elakit import S, MC, OR, SA, DRAW, rubric_for, make_test
from content.sched import schedule, UNIT_MONDAYS

NO_TE = {}   # this subject has no teacher edition; the workbook carries the answer key


def mono(code):
    """Show code in an answer key or prompt: monospace, line breaks and indentation kept."""
    esc = code.strip("\n").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    lines = [ln.replace("  ", "&nbsp;&nbsp;") for ln in esc.split("\n")]
    return "<font name='Mono' size='8.5'>" + "<br/>".join(lines) + "</font>"


def CODEX(prompt, solution, lines=6, note=None, points=1):
    """Coding exercise: write code (in the language of your choice) on lines; the key shows a solution."""
    return Problem(prompt, solution if solution.startswith("<") else mono(solution), lines=lines, space=0, wide=True, note=note, points=points)


def quiz(title, sections, minutes=15):
    return Check(title, sections, minutes=minutes)


def review(title, sections, minutes=30, note="Use this on Thursday evening or Friday morning before the exam."):
    return Check(title, sections, kind="review", minutes=minutes, teacher_note=note)


def exam(title, sections, minutes=30, labels=None):
    return make_test(title, sections, minutes=minutes, labels=labels or ["Strong. Move on with confidence.", "Solid. Redo the missed items' lessons.", "Revisit this unit's Code It examples before moving on."])


# The professional-learning year starts Monday, November 2, 2026; Units 2–9 follow the family school calendar.
DATA_MONDAYS = dict(UNIT_MONDAYS); DATA_MONDAYS[1] = ["2026-11-02"]


def weeks_for(unit, lessons, checks, rev, test):
    return schedule(lessons, DATA_MONDAYS[unit], checks, rev, test)
