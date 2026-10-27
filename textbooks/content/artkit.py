"""Shared helpers for Art unit files (two lessons a week, Monday and Wednesday)."""
from engine import Check
from content.te import TE
from content.elakit import S, MC, OR, SA, DRAW, rubric_for, make_test
from content.sched import schedule2, UNIT_MONDAYS

_L = lambda x: x if isinstance(x, list) else [x]


def aflow(look, demo, create, reflect="Students share one success and one thing to try next time; store work in the portfolio folder."):
    return [("Look and Talk", 5, _L(look)), ("Learn and Demonstrate", 10, _L(demo)), ("Create", 25, _L(create)), ("Reflect", 5, _L(reflect))]


def tart(obj, std, mat, look, demo, create, mis, sup, ext, **k):
    return TE(obj, std, mat, aflow(look, demo, create, **k), mis, sup, ext, time="About 45 minutes")


def sketchbook(title, sections, minutes=15):
    return Check(title, sections, minutes=minutes)


def review(title, sections, minutes=30, note="Use as a study session or portfolio sort before the review."):
    return Check(title, sections, kind="review", minutes=minutes, teacher_note=note)


def portfolio(title, sections, minutes=45, labels=None):
    return make_test(title, sections, minutes=minutes, labels=labels or ["Excellent: skills and ideas shine.", "Solid: revisit one technique.", "Reteach and redo one project."])


def weeks_for(unit, lessons, checks, rev, test):
    return schedule2(lessons, UNIT_MONDAYS[unit], checks, rev, test, days=(0, 2))
