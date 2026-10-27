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


# ---------------------------------------------------------------------------------------------------------------
# School-year pacing. The children started Lesson 1.1 in every textbook on Tuesday, October 27, 2026, so every
# student book is dated from that day on the family's school calendar. Each subject's lessons fill its class days in
# order with no gaps; each weekly check goes on the first Friday after the last lesson it covers, and the unit test on
# the first Friday after the unit's last lesson (with the review as homework the day before).
START = _dt.date(2026, 10, 27)
LAST_DAY = _dt.date(2027, 8, 6)             # the school year runs into August (summer extension Jul 19 – Aug 6)
import json as _json, os as _os
# Pacing adjustments for catch-up or working ahead: {"math4": {"2.5": "2026-12-01"}} means Lesson 2.5 of Grade 4 Math is
# taught on Dec 1, 2026, and every later lesson follows on the next class days. Two lessons may share a date (doubling up).
PACING_FILE = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "pacing.json")
BREAKS = [("2026-11-23", "2026-11-27"), ("2026-12-21", "2027-01-01"), ("2027-03-15", "2027-03-19")]
CLASS_DAYS = {"math": (0, 1, 2, 3), "ela": (0, 1, 2, 3), "spanish": (0, 1, 2, 3), "science": (0, 2), "art": (0, 2), "social": (1, 3)}


def _off(d):
    return any(_dt.date.fromisoformat(a) <= d <= _dt.date.fromisoformat(b) for a, b in BREAKS)


def school_days(weekdays, start=None):
    """Dates from START (or `start`) on that fall on the given weekdays (0 = Monday) and are not breaks; runs past LAST_DAY if needed.
    An anchor date is always included, then only the subject's own class days follow."""
    d = start or START
    if start and not _off(d): yield d; d += _dt.timedelta(1)
    while True:
        if d.weekday() in weekdays and not _off(d): yield d
        d += _dt.timedelta(1)


def _next_friday(d):
    return next(x for x in school_days((4,)) if x > d)


def pace(book, key=None):
    """Date every lesson, check, review, and test in a student book, and rebuild each unit's pacing table."""
    anchors = (_json.load(open(PACING_FILE)) if _os.path.exists(PACING_FILE) else {}).get(key, {})
    slots = school_days(CLASS_DAYS[book.subject])
    for U in book.units:
        rows = []
        for L in U.lessons:
            if L.num in anchors:
                a = _dt.date.fromisoformat(anchors[L.num])
                slots = school_days(CLASS_DAYS[book.subject], a)
            d = next(slots); L.date = _lab(d); L._d = d; rows.append((d, L.num, L.title))
        by_num = {L.num: L for L in U.lessons}
        for C in U.checks:
            fri = _next_friday(by_num[C.after]._d); C.date = _lab(fri); rows.append((fri, "Check", C.title))
        fri = _next_friday(U.lessons[-1]._d)
        U.test.date = _lab(fri); U.review.date = _lab(fri - _dt.timedelta(1)) + " (homework) or as needed"; rows.append((fri, "Test", U.test.title))
        weeks = {}
        for d, num, title in sorted(rows, key=lambda r: (r[0], r[1] in ("Check", "Test"))):
            mon = d - _dt.timedelta(d.weekday())
            weeks.setdefault(mon, []).append((f"{d:%a} {d.month}/{d.day}", num, title))
        U.weeks = [(f"Week of {m:%b} {m.day}", items) for m, items in weeks.items()]
    return book
