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


def schedule2(unit_lessons, mondays, weekly_checks, review, test, days=(0, 2)):
    """Two lessons a week on the given weekday offsets (0 = Monday), a check on Friday, the unit test on the last Friday.
    Science meets Monday/Wednesday (0, 2); Social Studies meets Tuesday/Thursday (1, 3)."""
    weeks = []
    ms = [_dt.date.fromisoformat(m) for m in mondays]
    assert len(unit_lessons) == 2 * len(ms), "two lessons per week"
    assert len(weekly_checks) == len(ms) - 1
    for w, mon in enumerate(ms):
        items = []
        for k, off in enumerate(days):
            L = unit_lessons[w * 2 + k]; d = mon + _dt.timedelta(off); L.date = _lab(d)
            items.append((f"{d:%a} {d.month}/{d.day}", L.num, L.title))
        fri = mon + _dt.timedelta(4)
        if w < len(ms) - 1:
            C = weekly_checks[w]; C.date = _lab(fri); C.after = unit_lessons[w * 2 + 1].num
            items.append((f"Fri {fri.month}/{fri.day}", "Check", C.title))
        else:
            test.date = _lab(fri); review.date = _lab(fri - _dt.timedelta(1)) + " (homework) or as needed"
            items.append((f"Fri {fri.month}/{fri.day}", "Test", test.title))
        weeks.append((f"Week of {mon:%b} {mon.day}", items))
    return weeks


UNIT_MONDAYS = {
    1: ["2026-10-12", "2026-10-19", "2026-10-26", "2026-11-02"], 2: ["2026-11-09", "2026-11-16", "2026-11-30", "2026-12-07"],
    3: ["2026-12-14", "2027-01-04", "2027-01-11", "2027-01-18"], 4: ["2027-01-25", "2027-02-01", "2027-02-08", "2027-02-15"],
    5: ["2027-02-22", "2027-03-01", "2027-03-08", "2027-03-22"], 6: ["2027-03-29", "2027-04-05", "2027-04-12", "2027-04-19"],
    7: ["2027-04-26", "2027-05-03", "2027-05-10", "2027-05-17"], 8: ["2027-05-24", "2027-05-31", "2027-06-07", "2027-06-14"],
    9: ["2027-06-21", "2027-06-28", "2027-07-05", "2027-07-12"],
}
