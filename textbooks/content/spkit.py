"""Shared helpers for Spanish unit files (four short lessons a week plus a Friday prueba)."""
from engine import Check
from content.te import TE
from content.elakit import S, MC, OR, SA, DRAW, rubric_for, make_test
from content.sched import schedule, UNIT_MONDAYS

_L = lambda x: x if isinstance(x, list) else [x]


def spflow(warm, listen, learn, practice, speak="Partners (or parent and child) act out the dialogue, then swap in their own details."):
    return [("Calentamiento", 3, _L(warm)), ("Escucha y repite", 5, _L(listen)), ("Aprende", 6, _L(learn)), ("Practica", 6, _L(practice)), ("Habla", 3, _L(speak))]


def tsp(obj, std, mat, warm, listen, learn, practice, mis, sup, ext, minutes=20, **k):
    return TE(obj, std, mat, spflow(warm, listen, learn, practice, **k), mis, sup, ext, time=f"About {minutes} minutes")


def prueba(title, sections, minutes=15):
    return Check(title, sections, minutes=minutes)


def repaso(title, sections, minutes=20, note="Use Thursday evening or Friday morning before the examen."):
    return Check(title, sections, kind="review", minutes=minutes, teacher_note=note)


def examen(title, sections, minutes=25, labels=None):
    return make_test(title, sections, minutes=minutes, labels=labels or ["¡Excelente! Ready for the next unit.", "¡Bien! Review the missed vocabulary.", "Repeat the unit's dialogues and retake."])


def LISTEN(prompt, script, answer, choices=None, correct=None):
    """Listening item: the teacher reads the script aloud (it appears only in the answer key)."""
    from engine import Problem
    if choices:
        return Problem("(Listen) " + prompt, f"{chr(65 + correct)}. {choices[correct]}", choices=choices, space=0, wide=True, note=f"Teacher reads: “{script}”")
    return Problem("(Listen) " + prompt, answer, space=0, note=f"Teacher reads: “{script}”")


def weeks_for(unit, lessons, checks, rev, test):
    return schedule(lessons, UNIT_MONDAYS[unit], checks, rev, test)
