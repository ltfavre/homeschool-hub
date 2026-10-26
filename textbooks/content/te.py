"""Shorthand for teacher-edition lesson data."""


def TE(objective, standard_text, materials, flow, misconceptions=(), support=(), extend=(), prep=None, time=None):
    d = dict(objective=objective, standard_text=standard_text, materials=materials, flow=flow,
             misconceptions=list(misconceptions), support=list(support), extend=list(extend))
    if prep: d["prep"] = prep
    if time: d["time"] = time
    return d


def flow(warm, launch, teach, guided, independent="Workbook lesson pages: Warm-Up through Think Deeper.", exit_="Student completes the Exit Ticket alone. Check it before the next lesson."):
    """Standard 50-minute lesson flow. Each argument is a string or list of strings."""
    L = lambda x: x if isinstance(x, list) else [x]
    return [("Warm-Up", 5, L(warm)), ("Launch", 5, L(launch)), ("Teach", 15, L(teach)),
            ("Guided Practice", 10, L(guided)), ("Independent", 12, L(independent)), ("Exit Ticket", 3, L(exit_))]
