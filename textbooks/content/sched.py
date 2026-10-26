"""Assigns lesson and check dates: four lessons Monday–Thursday, a check on Friday, the unit test on the last Friday."""
import datetime as _dt
from engine import Check


def _lab(d):
    return f"{d:%a} {d:%b} {d.day}"


def schedule(unit_lessons, mondays, weekly_checks, review, test):
    """mondays: ISO dates of the Mondays the unit spans. weekly_checks: list for every week except the last."""
    weeks = []
    ms = [_dt.date.fromisoformat(m) for m in mondays]
    assert len(unit_lessons) == 4 * len(ms), "four lessons per week"
    assert len(weekly_checks) == len(ms) - 1
    for w, mon in enumerate(ms):
        items = []
        for k in range(4):
            L = unit_lessons[w * 4 + k]; d = mon + _dt.timedelta(k); L.date = _lab(d)
            items.append((f"{d:%a} {d.month}/{d.day}", L.num, L.title))
        fri = mon + _dt.timedelta(4)
        if w < len(ms) - 1:
            C = weekly_checks[w]; C.date = _lab(fri); C.after = unit_lessons[w * 4 + 3].num
            items.append((f"Fri {fri.month}/{fri.day}", "Check", C.title))
        else:
            test.date = _lab(fri); review.date = _lab(fri - _dt.timedelta(1)) + " (homework) or as needed"
            items.append((f"Fri {fri.month}/{fri.day}", "Test", test.title))
        end = fri
        weeks.append((f"Week of {mon:%b} {mon.day}", items))
    return weeks
