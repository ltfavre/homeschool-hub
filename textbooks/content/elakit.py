"""Shared helpers for ELA unit files."""
from engine import Section, Problem
from content.te import TE, eflow


def S(title, problems, intro=None, cols=1, passage=None):
    return Section(title, problems, intro, cols, passage)


def MC(prompt, choices, correct, note=None):
    """Multiple choice. correct: index of the right choice."""
    return Problem(prompt, f"{chr(65 + correct)}. {choices[correct]}", choices=choices, space=0, note=note, wide=True)


def OR(prompt, answer, lines=2, note=None, points=1):
    """Open response written on lines."""
    return Problem(prompt, answer, lines=lines, space=0, wide=True, note=note, points=points)


def SA(prompt, answer, note=None):
    """Short answer on one answer line."""
    return Problem(prompt, answer, space=0, note=note)


def DRAW(prompt, answer, space=150, note=None):
    """Space to sketch or plan."""
    return Problem(prompt, answer, space=space, wide=True, note=note)


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


def rubric_for(total):
    """Standard 85% / 70% scoring bands for a test worth `total` points."""
    hi = -(-total * 85 // 100); mid = -(-total * 70 // 100)
    return [[f"{hi}–{total} (85%+)", "Mastered."], [f"{mid}–{hi - 1}", "Proficient; review missed skills."], [f"Below {mid}", "Reteach and retest."]]


def make_test(title, sections, minutes=45, labels=None):
    """Unit or year-end test with scoring bands computed from its point total."""
    from engine import Check
    total = sum(p.points for s in sections for p in s.problems)
    rb = rubric_for(total)
    if labels: rb = [[r[0], lab] for r, lab in zip(rb, labels)]
    return Check(title, sections, kind="test", minutes=minutes, rubric=rb)
