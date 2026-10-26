"""Small math helpers so answer keys are computed, not typed."""
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
PLACE_NAMES = ["ones", "tens", "hundreds", "thousands", "ten thousands", "hundred thousands", "millions"]
PLACE_VALUES = {"ones": 1, "tens": 10, "hundreds": 100, "thousands": 1000, "ten thousands": 10000,
                "hundred thousands": 100000, "millions": 1000000}


def _under_1000(n):
    out = []
    if n >= 100:
        out.append(ONES[n // 100] + " hundred"); n %= 100
    if n >= 20:
        out.append(TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else ""))
    elif n > 0:
        out.append(ONES[n])
    return " ".join(out)


def words(n):
    if n == 0: return "zero"
    parts = []
    for div, name in ((1000000, "million"), (1000, "thousand"), (1, "")):
        if n >= div:
            q = n // div; n %= div
            parts.append((_under_1000(q) + (" " + name if name else "")).strip())
    return " ".join(parts)


def c(n):
    return f"{n:,}"


def expanded(n):
    s = str(n); terms = []
    for i, d in enumerate(s):
        if d != "0": terms.append(c(int(d) * 10 ** (len(s) - 1 - i)))
    return " + ".join(terms)


def digit_place(n, digit_index_from_left):
    s = str(n); k = len(s) - 1 - digit_index_from_left
    return PLACE_NAMES[k], int(s[digit_index_from_left]) * 10 ** k


def value_of(n, place):
    k = PLACE_NAMES.index(place); return (n // 10 ** k) % 10 * 10 ** k


def digit_in(n, place):
    k = PLACE_NAMES.index(place); return (n // 10 ** k) % 10


def round_to(n, place):
    v = PLACE_VALUES[place] if isinstance(place, str) else place
    return (n + v // 2) // v * v


def F(n, d):
    """Inline fraction for Paragraph text."""
    return f"<super>{n}</super>⁄<sub>{d}</sub>"


def MX(w, n, d):
    return f"{w}&nbsp;{F(n, d)}"


def cmp(a, b):
    return ">" if a > b else "<" if a < b else "="
