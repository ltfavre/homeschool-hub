"""Grade 7 Math · Unit 4: Adding and Subtracting Rational Numbers (Jan 25 – Feb 19, 2027)."""
from fractions import Fraction as Fr
from decimal import Decimal as D
from engine import *
from content.mathkit import F, MX, RF, RD
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def pf(x):
    """Fraction in an expression, parenthesized when negative."""
    return f"({RF(x)})" if Fr(x) < 0 else RF(x)


def pdc(x):
    return f"({RD(x)})" if D(str(x)) < 0 else RD(x)


def fadd(a, b):
    return Problem(f"{RF(a)} + {pf(b)}", RF(Fr(a) + Fr(b)))


def fsub(a, b):
    return Problem(f"{RF(a)} − {pf(b)}", RF(Fr(a) - Fr(b)))


def dadd(a, b):
    return Problem(f"{RD(a)} + {pdc(b)}", RD(D(a) + D(b)))


def dsub(a, b):
    return Problem(f"{RD(a)} − {pdc(b)}", RD(D(a) - D(b)))


H = Fr


L1 = Lesson("4.1", "Rational Numbers on the Number Line",
    "I can place positive and negative fractions and decimals on a number line.", "7.NS.1",
    [("rational number", f"A number that can be written as a fraction of integers, like {F(3, 4)}, −2.5, or 7.")],
    "The temperature is −2.5°C. Is that warmer or colder than −2°C?",
    [Text(f"<b>Rational numbers</b> include integers, fractions, and decimals, positive and negative. −2.5 is halfway between −3 and −2, so it is farther from 0 and colder than −2."),
     Figure(lambda t: number_line(t, -3, 3, D("0.5"), 1, points=[(D("-2.5"), "−2.5"), (D("-0.75"), "−0.75"), (D("1.5"), "1.5")], fmt_fn=lambda v: RD(v))),
     Example("Compare", f"−{F(3, 4)} and −{F(2, 3)}", [f"{F(3, 4)} = {F(9, 12)} and {F(2, 3)} = {F(8, 12)}.", f"−{F(9, 12)} is farther left."], f"−{F(3, 4)} &lt; −{F(2, 3)}"),
     KeyIdea("For negative numbers, the one farther from 0 is less.")],
    [Problem("Which is less: −1.2 or −1.02?", "−1.2"), Problem(f"Opposite of −{MX(3, 1, 2)}", MX(3, 1, 2)), Problem("|−4.75|", "4.75")],
    [S("Warm-Up", [Problem("Which is less: −5 or −2?", "−5"), Problem(f"{F(3, 4)} as a decimal", "0.75")]),
     S("Compare (write <, >, or =)", [Problem(f"{a} ◯ {b}", c_) for a, b, c_ in [("−0.6", "−0.06", "<"), (f"−{F(1, 2)}", "−0.5", "="), (f"−{F(2, 5)}", f"−{F(1, 3)}", "<"), ("−3.4", "−3.45", ">"),
                                                                                  (f"{F(5, 8)}", f"−{F(7, 8)}", ">"), ("−1.75", f"−{MX(1, 3, 4)}", "=")]]),
     S("Order from least to greatest", [Problem(f"0.5, −{F(3, 4)}, −0.7, {F(1, 4)}, −1", f"−1, −{F(3, 4)}, −0.7, {F(1, 4)}, 0.5", wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain why −2.1 is less than −2.", "It is farther left (farther from 0 in the negative direction).", lines=2, space=0, wide=True)], cols=1)],
    TE("Students locate and compare rational numbers.", "Represent addition and subtraction on a number line; understand rational numbers.", "Number line −3 to 3 in halves and quarters, workbook Lesson 4.1",
       flow("Compare integers.", "Read Let's Explore.", ["Place fractions and decimals on a number line.", "Say: For negatives, farther from 0 is smaller."], "Try It 1–3."),
       ["Thinking −1.02 < −1.2 because it has more digits."], ["Number line."], ["Find negative decimals in real data (stocks, temperatures)."]),
    summary="Rational numbers include signed fractions and decimals. For negatives, farther from 0 is less.")

L2 = Lesson("4.2", "Adding Signed Fractions",
    "I can add positive and negative fractions.", "7.NS.1b, 7.NS.1d",
    [],
    f"A stock rose {F(3, 8)} of a point on Monday and fell {F(5, 8)} of a point on Tuesday. What was the total change?",
    [Text("The integer rules work for fractions too. Same signs: add absolute values, keep the sign. Different signs: subtract absolute values, use the sign of the one farther from 0."),
     Example("Different signs", f"{F(3, 8)} + (−{F(5, 8)})", [f"|−{F(5, 8)}| is larger, so the answer is negative.", f"{F(5, 8)} − {F(3, 8)} = {F(2, 8)} = {F(1, 4)}."], f"−{F(1, 4)}"),
     Example("Unlike denominators", f"−{F(1, 2)} + (−{F(1, 3)})", [f"Common denominator 6: −{F(3, 6)} + (−{F(2, 6)}).", f"Same signs: −{F(5, 6)}."], f"−{F(5, 6)}"),
     KeyIdea("Use common denominators, then apply the integer sign rules to the numerators.")],
    [fadd(H(-2, 5), H(4, 5)), fadd(H(3, 4), H(-5, 6)), fadd(H(-1, 6), H(-2, 3))],
    [S("Warm-Up", [Problem("−5 + 3", "−2"), Problem(f"{F(1, 2)} + {F(1, 3)}", F(5, 6))]),
     S("Add", [fadd(a, b) for a, b in [(H(-3, 7), H(1, 7)), (H(5, 9), H(-8, 9)), (H(-1, 4), H(-3, 8)), (H(2, 3), H(-1, 6)), (H(-7, 10), H(2, 5)), (H(-5, 12), H(-1, 3)), (H(4, 5), H(-1, 2)), (H(-3, 4), H(3, 4))]]),
     S("Solve", [Problem(f"A water level was −{F(3, 4)} ft (below normal). It rose {F(1, 2)} ft. New level?", f"−{F(1, 4)} ft", space=24, wide=True)], cols=1),
     S("Exit Ticket", [fadd(H(-5, 6), H(3, 4))], cols=1)],
    TE("Students add signed fractions.", "Apply properties of operations to add rational numbers.", "Workbook Lesson 4.2", flow("Warm-up.", "Read Let's Explore.", ["Work both examples. Say: Same rules as integers."], "Try It 1–3."),
       ["Adding denominators.", "Losing the negative sign."], ["Write the sign decision first."], ["Add three signed fractions."]),
    summary="Find a common denominator, then follow the integer sign rules.")

L3 = Lesson("4.3", "Subtracting Signed Fractions",
    "I can subtract positive and negative fractions by adding the opposite.", "7.NS.1c",
    [],
    f"At 6 a.m. a pond's ice was −{F(1, 4)} inch below a mark. At noon it was {F(5, 8)} inch above. How much did it rise?",
    [Example("Add the opposite", f"{F(5, 8)} − (−{F(1, 4)})", [f"= {F(5, 8)} + {F(1, 4)} = {F(5, 8)} + {F(2, 8)}."], F(7, 8) + " inch"),
     Example("Negative minus positive", f"−{F(2, 3)} − {F(1, 2)}", [f"= −{F(2, 3)} + (−{F(1, 2)}) = −{F(4, 6)} + (−{F(3, 6)})."], f"−{F(7, 6)} = −{MX(1, 1, 6)}"),
     KeyIdea("a − b = a + (−b), for fractions too.")],
    [fsub(H(1, 3), H(2, 3)), fsub(H(-3, 4), H(-1, 8)), fsub(H(-1, 2), H(3, 10))],
    [S("Warm-Up", [Problem("2 − (−5)", "7"), Problem(f"Opposite of −{F(3, 8)}", F(3, 8))]),
     S("Subtract", [fsub(a, b) for a, b in [(H(1, 5), H(4, 5)), (H(-2, 9), H(5, 9)), (H(3, 8), H(-1, 4)), (H(-5, 6), H(-1, 3)), (H(-1, 2), H(1, 4)), (H(2, 3), H(3, 4)), (H(-7, 12), H(-3, 4)), (H(0), H(-5, 8))]]),
     S("Exit Ticket", [Problem(f"Explain why {F(1, 2)} − (−{F(1, 2)}) = 1.", "Subtracting a negative adds: 1/2 + 1/2.".replace("1/2", F(1, 2)), lines=2, space=0, wide=True)], cols=1)],
    TE("Students subtract signed fractions.", "Understand subtraction as adding the additive inverse for rational numbers.", "Workbook Lesson 4.3", flow("Warm-up.", "Read Let's Explore.", ["Rewrite each subtraction as addition."], "Try It 1–3."),
       ["Forgetting to change the second sign."], ["Keep-change-opposite."], ["Write a real story for −3/4 − 1/2."]),
    summary="Subtract fractions by adding the opposite.")

L4 = Lesson("4.4", "Adding and Subtracting Signed Mixed Numbers",
    f"I can add and subtract signed mixed numbers like −{MX(2, 1, 3)} + {MX(1, 1, 2)}.", "7.NS.1",
    [],
    f"A hiker is at −{MX(3, 1, 2)} m (in a trench). She climbs {MX(5, 3, 4)} m. Where is she now?",
    [Text("Change mixed numbers to improper fractions, or work with whole and fraction parts carefully."),
     Example("Improper fractions", f"−{MX(3, 1, 2)} + {MX(5, 3, 4)}", [f"= −{F(14, 4)} + {F(23, 4)} = {F(9, 4)}."], MX(2, 1, 4) + " m"),
     Example("Subtract", f"−{MX(1, 2, 3)} − {MX(2, 1, 6)}", [f"= −{F(10, 6)} + (−{F(13, 6)}) = −{F(23, 6)}."], f"−{MX(3, 5, 6)}"),
     KeyIdea("Improper fractions make signed mixed-number problems safer.")],
    [fadd(H(-9, 4), H(7, 2)), fsub(H(5, 3), H(13, 4)), fadd(H(-11, 5), H(-3, 2))],
    [S("Warm-Up", [Problem(f"{MX(2, 1, 3)} as an improper fraction", F(7, 3)), Problem(f"{F(17, 6)} as a mixed number", MX(2, 5, 6))]),
     S("Compute", [fadd(a, b) for a, b in [(H(-5, 2), H(17, 4)), (H(10, 3), H(-23, 6)), (H(-13, 8), H(-3, 4))]] + [fsub(a, b) for a, b in [(H(-7, 2), H(5, 4)), (H(9, 4), H(-11, 3)), (H(-16, 5), H(-21, 10))]]),
     S("Solve", [Problem(f"A lake was {MX(1, 1, 4)} ft below normal. It dropped {MX(2, 2, 3)} ft more. New level?", f"−{MX(3, 11, 12)} ft", space=30, wide=True)], cols=1),
     S("Exit Ticket", [fsub(H(-5, 2), H(-23, 4))], cols=1)],
    TE("Students add and subtract signed mixed numbers.", "Add and subtract rational numbers.", "Workbook Lesson 4.4", flow("Conversions.", "Read Let's Explore.", ["Work both examples with improper fractions."], "Try It 1–3. Weekly Check tomorrow."),
       ["Making only the whole part negative: −3½ treated as −3 + ½."], ["Improper fractions."], ["Solve with both methods and compare."]),
    summary=f"Change signed mixed numbers to improper fractions, then use the sign rules. Remember −{MX(3, 1, 2)} = −3 − {F(1, 2)}.")

L5 = Lesson("4.5", "Fractions as Decimals",
    "I can write fractions as terminating or repeating decimals using long division.", "7.NS.2d",
    [("terminating decimal", "A decimal that ends, like 0.375."), ("repeating decimal", "A decimal with a digit or digits that repeat forever, like 0.333… written 0.3̄.")],
    f"Is {F(1, 3)} closer to 0.33 or 0.34? Does it ever end?",
    [Text(f"Divide the numerator by the denominator. {F(3, 8)} = 3 ÷ 8 = 0.375: it <b>terminates</b>. {F(1, 3)} = 0.3333…: it <b>repeats</b> forever. We write 0.3 with a bar over the 3."),
     Figure(lambda t: table(t, [["Fraction", "Decimal", "Type"], [P(F(1, 4), t.cell), "0.25", "terminating"], [P(F(3, 8), t.cell), "0.375", "terminating"], [P(F(2, 3), t.cell), "0.666…", "repeating"],
                                [P(F(5, 11), t.cell), "0.4545…", "repeating"], [P(F(7, 20), t.cell), "0.35", "terminating"]], [1.3 * inch, 1.5 * inch, 1.5 * inch], width=4.3 * inch)),
     Example("Long division", f"{F(5, 6)}", ["5 ÷ 6: 50 ÷ 6 = 8 R2; 20 ÷ 6 = 3 R2; 20 ÷ 6 = 3 R2…", "The 3 repeats."], "0.8333… (0.83 with a bar over the 3)"),
     KeyIdea("Every fraction is a terminating or repeating decimal. That's what makes it rational.")],
    [Problem(f"{F(5, 8)} as a decimal", "0.625"), Problem(f"{F(4, 9)} as a decimal", "0.444…"), Problem(f"−{F(7, 4)} as a decimal", "−1.75")],
    [S("Warm-Up", [Problem("3 ÷ 8", "0.375"), Problem("1 ÷ 3", "0.333…")]),
     S("Write as a decimal. Terminating or repeating?", [Problem(F(n, d), a) for n, d, a in [(3, 5, "0.6; terminating"), (1, 6, "0.1666…; repeating"), (7, 8, "0.875; terminating"), (2, 9, "0.222…; repeating"),
                                                                                             (9, 20, "0.45; terminating"), (4, 11, "0.3636…; repeating")]]),
     S("Exit Ticket", [Problem(f"Write −{MX(2, 1, 3)} as a decimal.", "−2.333…", wide=True)], cols=1)],
    TE("Students convert fractions to decimals with long division.", "Convert a rational number to a decimal using long division; know that the decimal form terminates or eventually repeats.", "Workbook Lesson 4.5",
       flow("Division warm-up.", "Read Let's Explore.", ["Long division for 5/6 showing the repeating remainder."], "Try It 1–3."), ["Stopping too early to see the repeat."], ["Watch for repeating remainders."], ["Which denominators give terminating decimals? (factors of 2 and 5 only)"]),
    summary="Divide numerator by denominator; the decimal terminates or repeats.")

L6 = Lesson("4.6", "Comparing and Ordering Rational Numbers",
    "I can compare and order signed fractions and decimals.", "7.NS.1, 7.NS.2d",
    [],
    f"Order these golf scores (relative to par) from best (lowest) to worst: −2.5, −{MX(2, 3, 4)}, 1.25, −{F(1, 2)}.",
    [Example("Order", f"−2.5, −{MX(2, 3, 4)}, 1.25, −{F(1, 2)}", [f"Decimals: −2.5, −2.75, 1.25, −0.5.", "Least to greatest: −2.75, −2.5, −0.5, 1.25."], f"−{MX(2, 3, 4)}, −2.5, −{F(1, 2)}, 1.25"),
     KeyIdea("Change all numbers to decimals, then compare on a number line.")],
    [Problem(f"−{F(5, 8)} ◯ −0.6", "<"), Problem(f"Order: −1.3, −{F(4, 3)}, −1.25", f"−{F(4, 3)}, −1.3, −1.25"), Problem("Greatest: −0.09, −0.9, −0.19", "−0.09")],
    [S("Warm-Up", [Problem(f"{F(5, 8)} as a decimal", "0.625"), Problem(f"{F(4, 3)} as a decimal", "1.333…")]),
     S("Order from least to greatest", [Problem(t_, a, wide=True) for t_, a in [(f"−0.4, −{F(3, 8)}, 0.3, −{F(1, 2)}", f"−{F(1, 2)}, −0.4, −{F(3, 8)}, 0.3"),
                                                                                (f"{MX(1, 1, 3)}, −1.3, 1.3, −{MX(1, 1, 3)}", f"−{MX(1, 1, 3)}, −1.3, 1.3, {MX(1, 1, 3)}"),
                                                                                (f"−2.05, −2.5, −{MX(2, 1, 5)}, −2", f"−2.5, −{MX(2, 1, 5)}, −2.05, −2")]], cols=1),
     S("Exit Ticket", [Problem(f"Which is greater, −{F(2, 3)} or −0.67? Explain.", "−2/3 (−0.666…) is greater than −0.67.".replace("2/3", F(2, 3)), lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare and order rational numbers.", "Understand ordering of rational numbers.", "Workbook Lesson 4.6", flow("Conversions.", "Read Let's Explore.", ["Convert to decimals; place on a number line."], "Try It 1–3."),
       ["Ordering negatives like positives."], ["Number line."], ["Order real golf scores or stock changes."]),
    summary="Convert to decimals and compare on a number line.")

L7 = Lesson("4.7", "Adding Signed Decimals",
    "I can add positive and negative decimals.", "7.NS.1",
    [],
    "A bank account has −$12.50 (overdrawn). A deposit of $40.75 is made. What is the new balance?",
    [Example("Different signs", "−12.50 + 40.75", ["Subtract absolute values: 40.75 − 12.50 = 28.25.", "40.75 is farther from 0, so positive."], "$28.25"),
     Example("Same signs", "−3.6 + (−0.85)", ["Add: 3.6 + 0.85 = 4.45. Keep negative."], "−4.45"),
     KeyIdea("Line up decimal points and use the integer sign rules.")],
    [dadd("-7.2", "3.5"), dadd("-0.45", "-1.8"), dadd("12.06", "-12.6")],
    [S("Warm-Up", [Problem("40.75 − 12.50", "28.25"), Problem("3.6 + 0.85", "4.45")]),
     S("Add", [dadd(a, b) for a, b in [("-4.3", "2.1"), ("6.75", "-9.5"), ("-0.8", "-0.15"), ("-15.2", "15.2"), ("3.05", "-0.7"), ("-22.4", "-7.65")]]),
     S("Solve", [Problem("A temperature of −3.8°C rises 5.6°C. New temperature?", "1.8°C", space=24), Problem("A stock changed −1.35, +0.80, and −0.25 dollars. Total change?", "−$0.80", space=24)]),
     S("Exit Ticket", [dadd("-8.06", "5.9")], cols=1)],
    TE("Students add signed decimals.", "Add rational numbers.", "Workbook Lesson 4.7", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."), ["Misaligned decimals."], ["Write zeros to equal length."], ["Track a stock for a week."]),
    summary="Line up decimals and apply the sign rules.")

L8 = Lesson("4.8", "Subtracting Signed Decimals",
    "I can subtract positive and negative decimals.", "7.NS.1c",
    [],
    "The lowest point in Louisiana is about −2.4 m (in New Orleans). Driskill Mountain is about 163.1 m. What is the difference in elevation?",
    [Example("Subtract a negative", "163.1 − (−2.4)", ["= 163.1 + 2.4."], "165.5 m"),
     Example("Negative minus positive", "−0.75 − 1.6", ["= −0.75 + (−1.6) = −2.35."], "−2.35"),
     KeyIdea("Subtract decimals by adding the opposite.")],
    [dsub("4.2", "6.5"), dsub("-3.8", "-1.25"), dsub("-0.9", "0.45")],
    [S("Warm-Up", [dadd("163.1", "2.4"), dadd("-0.75", "-1.6")]),
     S("Subtract", [dsub(a, b) for a, b in [("2.5", "7.1"), ("-6.3", "2.4"), ("1.75", "-0.5"), ("-8.2", "-8.2"), ("-0.05", "0.5"), ("10", "-3.75")]]),
     S("Solve", [Problem("From −12.5°F to 4.3°F: change?", "16.8°F", space=24), Problem("A submarine at −85.4 m dives to −112.9 m. Change?", "−27.5 m", space=24)]),
     S("Exit Ticket", [dsub("-5.08", "-7.3")], cols=1)],
    TE("Students subtract signed decimals.", "Subtract rational numbers.", "Workbook Lesson 4.8", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3. Weekly Check tomorrow."), ["Sign errors."], ["Rewrite as addition."], ["Find elevation ranges for Gulf states."]),
    summary="Subtract decimals by adding the opposite.")

L9 = Lesson("4.9", "Rational Numbers and Money",
    "I can solve money problems with positive and negative decimals.", "7.NS.3, 7.EE.3",
    [],
    "Lillie's account starts at $24.60. She buys a book for $18.95 and a snack for $7.40. Then she deposits $15. What is her balance?",
    [Example("Running balance", "24.60 − 18.95 − 7.40 + 15", ["24.60 − 18.95 = 5.65.", "5.65 − 7.40 = −1.75.", "−1.75 + 15 = 13.25."], "$13.25"),
     KeyIdea("Write each transaction as a signed number and keep a running balance.")],
    [Problem("$5.20 − $9.85", "−$4.65"), Problem("−$32.10 + $50", "$17.90"), Problem("Profits: $12.40, −$20.15, $6.80", "−$0.95")],
    [S("Warm-Up", [dsub("24.60", "18.95"), dsub("5.65", "7.40")]),
     S("Solve", [Problem("Start at −$8.25. Deposit $30, spend $14.60.", "$7.15", space=24), Problem("A lemonade stand: +$18.50, −$6.75 (supplies), +$12.25, −$4.30. Total?", "$19.70", space=24),
                 Problem("A stock is at $45.20. It changes −2.85, +1.10, −0.65. New price?", "$42.80", space=24), Problem("Ellie owes $12.40 and pays $7.95. How much does she owe now?", "$4.45 (−$4.45)", space=24)]),
     S("Exit Ticket", [Problem("Create a 4-transaction account record that ends below $0.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve money problems with signed decimals.", "Solve real-world problems with rational numbers.", "Workbook Lesson 4.9", flow("Warm-up.", "Read Let's Explore.", ["Running balance table."], "Try It 1–3."), ["Treating purchases as positive."], ["Table."], ["Track a real allowance budget."]),
    summary="Use signed decimals for deposits and purchases and keep a running balance.")

L10 = Lesson("4.10", "Rational Numbers in Measurement",
    "I can solve elevation, temperature, and measurement problems with signed fractions and decimals.", "7.NS.3",
    [],
    f"A carpenter needs a board {MX(4, 3, 8)} ft long. Hers is {MX(5, 1, 4)} ft. How much must she cut off?",
    [Example("Fractions", f"{MX(5, 1, 4)} − {MX(4, 3, 8)}", [f"= {F(42, 8)} − {F(35, 8)} = {F(7, 8)}."], F(7, 8) + " ft"),
     Example("Temperature", "−4.5°C at night, 7.2°C at noon", ["7.2 − (−4.5) = 11.7."], "11.7°C warmer"),
     KeyIdea("Choose fractions or decimals, whichever makes the computation easier.")],
    [Problem(f"A plant {MX(3, 1, 2)} in. tall shrinks {F(3, 4)} in. New height?", MX(2, 3, 4) + " in."), Problem("−1.8°F to 6.5°F: change", "8.3°F"), Problem(f"Water level −{F(2, 3)} ft then rises {MX(1, 1, 6)} ft", F(1, 2) + " ft")],
    [S("Warm-Up", [fsub(H(21, 4), H(35, 8)), dsub("7.2", "-4.5")]),
     S("Solve", [Problem(f"A diver at −{MX(10, 1, 2)} ft rises {MX(4, 3, 4)} ft. Depth?", f"−{MX(5, 3, 4)} ft", space=24), Problem("A runner's times: 12.45 s and 11.9 s. Improvement?", "0.55 s", space=24),
                 Problem("−6.25°F drops 3.8°F. New temperature?", "−10.05°F", space=24), Problem(f"Rope {MX(12, 1, 3)} m; cut {MX(4, 5, 6)} m. Left?", MX(7, 1, 2) + " m", space=24)]),
     S("Exit Ticket", [Problem(f"Write a measurement story for {MX(2, 1, 2)} − {MX(3, 3, 4)}. Solve.", f"−{MX(1, 1, 4)}", lines=2, space=0, wide=True)], cols=1)],
    TE("Students solve measurement problems with rational numbers.", "Solve real-world problems with rational numbers.", "Workbook Lesson 4.10", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."), ["Sign errors with mixed numbers."], ["Improper fractions."], ["Measure and compare real objects."]),
    summary="Use signed fractions and decimals for real measurements.")

L11 = Lesson("4.11", "Properties for Rational Number Sums",
    "I can use properties to add and subtract rational numbers efficiently.", "7.NS.1d",
    [],
    f"Find −{F(3, 4)} + 2.6 + {F(3, 4)} + (−0.6) in your head.",
    [Example("Rearrange", f"−{F(3, 4)} + 2.6 + {F(3, 4)} + (−0.6)", [f"(−{F(3, 4)} + {F(3, 4)}) + (2.6 + (−0.6)).", "0 + 2 = 2."], "2"),
     KeyIdea("Group opposites and friendly decimals; rewrite subtraction as addition first.")],
    [Problem("−3.7 + 8.25 + 3.7", "8.25"), Problem(f"{F(2, 5)} − 1.5 − {F(2, 5)} + 0.5", "−1"), Problem("−0.25 + 6 + (−0.75)", "5")],
    [S("Warm-Up", [Problem(f"−{F(3, 4)} + {F(3, 4)}", "0"), Problem("2.6 − 0.6", "2")]),
     S("Compute mentally", [Problem(e, a) for e, a in [("4.8 + (−2.3) + (−4.8)", "−2.3"), (f"−{F(5, 6)} + 3 + {F(5, 6)}", "3"), ("−1.25 + 7 + (−0.75)", "5"), (f"{MX(2, 1, 2)} − 4 + {F(1, 2)}", "−1"),
                                                     ("−9.9 + 5 + 9.9 + (−5)", "0"), (f"0.75 + (−{F(1, 4)}) + (−2)", "−1.5")]]),
     S("Exit Ticket", [Problem("Show how grouping helps evaluate −6.4 + 3.3 + 6.4 − 1.3.", "(−6.4 + 6.4) + (3.3 − 1.3) = 2", lines=2, space=0, wide=True)], cols=1)],
    TE("Students use properties to compute with rational numbers.", "Apply properties of operations as strategies to add and subtract rational numbers.", "Workbook Lesson 4.11", flow("Warm-up.", "Read Let's Explore.", ["Look for opposites and friendly sums."], "Try It 1–3."), ["Moving numbers without their signs."], ["Circle each term with its sign."], ["Mental-math race."]),
    summary="Regroup opposites and friendly numbers to compute mentally.")

L12 = Lesson("4.12", "Multi-Step Rational Number Problems",
    "I can solve multi-step problems with signed fractions and decimals.", "7.EE.3",
    [],
    f"A tide chart shows changes of −{MX(1, 1, 4)} ft, +{MX(2, 1, 2)} ft, −{F(3, 4)} ft from a starting level of {F(1, 2)} ft. Final level?",
    [Example("Tide", f"{F(1, 2)} − {MX(1, 1, 4)} + {MX(2, 1, 2)} − {F(3, 4)}", ["In fourths: 2 − 5 + 10 − 3 = 4 fourths."], "1 ft"),
     KeyIdea("Convert to one form (all fourths, or all decimals) and combine in order.")],
    [Problem("−2.4 + 5.1 − 3.25", "−0.55"), Problem(f"{F(2, 3)} − {F(5, 6)} + (−{F(1, 2)})", f"−{F(2, 3)}"), Problem("A hiker at −15.5 m climbs 40.25 m then descends 8.75 m.", "16 m")],
    [S("Warm-Up", [Problem("2 − 5 + 10 − 3", "4"), Problem(f"{F(4, 4)}", "1")]),
     S("Solve", [Problem("Temperatures: −2.4°C, then +6.8°C, then −5.1°C. Final?", "−0.7°C", space=30, wide=True),
                 Problem(f"A stock: start $18.40. Changes: −{F(3, 4)}, +$1.20, −$0.55. Final price? (Use 0.75 for {F(3, 4)}.)", "$18.30", space=30, wide=True),
                 Problem(f"Lillie's garden bed is {MX(8, 1, 2)} ft. She uses {MX(2, 3, 4)} ft for tomatoes and {MX(3, 1, 3)} ft for peppers. Space left?", MX(2, 5, 12) + " ft", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write and solve a three-step problem with negative decimals.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve multi-step rational problems.", "Solve multi-step real-life problems with positive and negative rational numbers.", "Workbook Lesson 4.12", flow("Warm-up.", "Read Let's Explore.", ["Convert to one form."], "Try It 1–3. Weekly Check tomorrow."), ["Mixing fractions and decimals carelessly."], ["Convert first."], ["Analyze real tide data."]),
    summary="Convert to one form and combine step by step.")

L13 = Lesson("4.13", "Distance Between Rational Numbers",
    "I can find the distance between two rational numbers using absolute value.", "7.NS.1c",
    [],
    f"How far apart are −{MX(2, 1, 2)} and {MX(1, 3, 4)} on a number line?",
    [Example("Distance", f"|{MX(1, 3, 4)} − (−{MX(2, 1, 2)})|", [f"= |{F(7, 4)} + {F(10, 4)}| = {F(17, 4)}."], MX(4, 1, 4)),
     KeyIdea("Distance = |a − b|, for fractions and decimals too.")],
    [Problem("Distance between −3.2 and 1.5", "4.7"), Problem(f"Distance between −{F(5, 6)} and −{F(1, 3)}", F(1, 2)), Problem("|−0.8 − 2.45|", "3.25")],
    [S("Warm-Up", [Problem("|−7.5|", "7.5"), fadd(H(7, 4), H(10, 4))]),
     S("Find the distance", [Problem(f"{a} and {b}", v) for a, b, v in [("−4.6", "2.9", "7.5"), (f"−{F(2, 3)}", F(1, 6), F(5, 6)), ("−10.25", "−3.5", "6.75"), (f"{MX(3, 1, 2)}", f"−{MX(1, 1, 4)}", MX(4, 3, 4))]]),
     S("Solve", [Problem("Death Valley: −86 m. Mount McKinley (Denali): 6,190 m. Distance?", "6,276 m", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain why the distance from −2.5 to 4 equals the distance from 4 to −2.5.", "|a − b| = |b − a|", lines=2, space=0, wide=True)], cols=1)],
    TE("Students find distance between rational numbers.", "Show that the distance between two rational numbers is the absolute value of their difference.", "Workbook Lesson 4.13", flow("Warm-up.", "Read Let's Explore.", ["Work the example."], "Try It 1–3."), ["Negative distances."], ["Number line."], ["Distances between record temperatures."]),
    summary="Distance between rational numbers is |a − b|.")

L14 = Lesson("4.14", "Expressions with Rational Numbers",
    "I can evaluate expressions with signed fractions and decimals.", "7.NS.1, 7.EE.1",
    [],
    "Evaluate x − y + 2.5 when x = −1.75 and y = −3.",
    [Example("Substitute", "x − y + 2.5", ["(−1.75) − (−3) + 2.5 = −1.75 + 3 + 2.5."], "3.75"),
     KeyIdea("Substitute with parentheses, rewrite subtraction, then combine.")],
    [Problem("a + b when a = −0.6, b = 2.35", "1.75"), Problem(f"x − {F(1, 2)} when x = −{F(3, 4)}", f"−{MX(1, 1, 4)}"), Problem("−m + n when m = −4.2, n = −1.8", "2.4")],
    [S("Warm-Up", [Problem("−1.75 + 3", "1.25"), Problem("−(−4.2)", "4.2")]),
     S("Evaluate when p = −2.5 and q = 1.25", [Problem(e, v) for e, v in [("p + q", "−1.25"), ("p − q", "−3.75"), ("q − p", "3.75"), ("−p − q", "1.25"), ("p + p + q", "−3.75"), ("|p| − |q|", "1.25")]]),
     S("Exit Ticket", [Problem(f"Evaluate r − s when r = {F(2, 3)} and s = −{F(5, 6)}.", MX(1, 1, 2), wide=True)], cols=1)],
    TE("Students evaluate expressions with rational numbers.", "Evaluate expressions.", "Workbook Lesson 4.14", flow("Warm-up.", "Read Let's Explore.", ["Substitute with parentheses."], "Try It 1–3."), ["Sign errors."], ["Parentheses."], ["Make a table for an expression."]),
    summary="Substitute in parentheses and follow the sign rules.")

L15 = Lesson("4.15", "Error Analysis with Rational Numbers",
    "I can find and fix errors in rational-number computations.", "7.NS.1",
    [],
    f"Sam says −{F(1, 2)} − {F(1, 3)} = −{F(1, 6)}. Is he right?",
    [Example("Fix it", f"−{F(1, 2)} − {F(1, 3)}", [f"Sam subtracted absolute values. It should be −{F(1, 2)} + (−{F(1, 3)}).", f"= −{F(3, 6)} + (−{F(2, 6)}) = −{F(5, 6)}."], f"−{F(5, 6)}"),
     Figure(lambda t: table(t, [["Error", "Fix"], ["−2.5 + 1.3 = −3.8", "Different signs: −1.2"], ["0.4 − (−0.6) = −0.2", "Add the opposite: 1.0"], [P(f"−{MX(1, 1, 2)} = −1 + {F(1, 2)}", t.cell), P(f"−{MX(1, 1, 2)} = −1 − {F(1, 2)} = −1.5", t.cell)]],
                            [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     KeyIdea("Estimate the sign and size first; then check the computed answer.")],
    [Problem("Fix: −3.2 − 1.5 = −1.7", "−4.7"), Problem(f"Fix: {F(1, 4)} − (−{F(3, 4)}) = −{F(1, 2)}", "1"), Problem("Fix: −0.8 + 0.25 = −1.05", "−0.55")],
    [S("Warm-Up", [fsub(H(-1, 2), H(1, 3)), dadd("-2.5", "1.3")]),
     S("Find and fix", [Problem(e, v) for e, v in [("−6.1 + 2.4 = −8.5", "−3.7"), (f"{F(2, 3)} − {F(5, 6)} = {F(1, 6)}", f"−{F(1, 6)}"), ("−4 − (−1.25) = −5.25", "−2.75"), ("0.3 − 0.45 = 0.15", "−0.15")]]),
     S("Exit Ticket", [Problem("Describe how estimating first can catch a sign error.", "Predict positive/negative and size; compare.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students analyze rational-number errors.", "Apply properties to add and subtract rational numbers.", "Workbook Lesson 4.15", flow("Warm-up.", "Read Let's Explore.", ["Discuss each error in the table."], "Try It 1–3."), ["Same as listed."], ["Estimate first."], ["Write tricky problems for a sibling."]),
    summary="Estimate sign and size first, then check.")

L16 = Lesson("4.16", "Rational Number Problem Solving",
    "I can solve problems with signed fractions and decimals.", "7.NS.1, 7.NS.3, 7.EE.3",
    [],
    "A science class recorded temperature changes every hour: −1.5°, −2.25°, +0.75°, +3.5°. Starting at −4°C, what is the final temperature? What was the lowest?",
    [Example("Track", "Start −4", ["−4 − 1.5 = −5.5.", "−5.5 − 2.25 = −7.75 (lowest).", "−7.75 + 0.75 = −7.", "−7 + 3.5 = −3.5."], "final −3.5°C; lowest −7.75°C"),
     KeyIdea("Organize with a table; check the reasonableness of every step.")],
    [Problem(f"−{F(3, 8)} + {F(5, 6)}", F(11, 24)), Problem("−7.05 − (−2.6)", "−4.45"), Problem(f"Distance between −{F(3, 4)} and 2.5", "3.25")],
    [S("Warm-Up", [dsub("-4", "1.5"), dadd("-7.75", "0.75")]),
     S("Mixed practice", [fadd(H(-7, 8), H(1, 4)), fsub(H(2, 5), H(-1, 2)), dadd("-12.4", "8.75"), dsub("0.6", "2.15"), Problem(f"Order: −0.3, −{F(1, 3)}, −0.33", f"−{F(1, 3)}, −0.33, −0.3"), Problem(f"{F(7, 12)} as a decimal", "0.58333…")]),
     S("Solve", [Problem("A business had monthly results of −$1,250.50, +$3,400.75, and −$875.25. Total?", "$1,275", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which is harder for you: signed fractions or signed decimals? Make up and solve one of each.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve mixed rational-number problems.", "7.NS.1–3 review.", "Workbook Lesson 4.16, Unit 4 Review", flow("Warm-up.", "Read Let's Explore.", ["Work the table example."], "Try It 1–3.", "Workbook Lesson 4.16 and the Unit 4 Review.", "Check. Tomorrow: Unit 4 Test."),
       ["Sign errors."], ["Tables."], ["Analyze a week of real temperature data."]),
    summary="Organize, convert, compute with the sign rules, and check.")

C1 = Check("Weekly Check 10: Signed Fractions", [S("Show what you know", [fadd(H(-3, 5), H(1, 5)), fadd(H(-1, 4), H(-2, 3)), fsub(H(1, 6), H(5, 6)), fsub(H(-3, 8), H(-1, 2)),
    fadd(H(-7, 2), H(9, 4)), Problem(f"Order: −{F(2, 3)}, −0.6, {F(1, 2)}", f"−{F(2, 3)}, −0.6, {F(1, 2)}")])], minutes=20)
C2 = Check("Weekly Check 11: Signed Decimals", [S("Show what you know", [Problem(f"{F(7, 8)} as a decimal", "0.875"), Problem(f"{F(5, 9)} as a decimal", "0.555…"), dadd("-6.4", "2.75"), dadd("-0.35", "-1.2"),
    dsub("3.1", "5.85"), dsub("-2.5", "-7.25")])], minutes=20)
C3 = Check("Weekly Check 12: Rational Number Applications", [S("Show what you know", [Problem("Start −$6.40, deposit $25, spend $11.85", "$6.75"), Problem("−3.2°C to 5.9°C: change", "9.1°C"),
    Problem(f"Board {MX(6, 1, 4)} ft, cut {MX(2, 7, 8)} ft. Left?", MX(3, 3, 8) + " ft"), Problem("−4.5 + 2.75 + 4.5 (mentally)", "2.75"), Problem("−1.6 + 3.25 − 0.9", "0.75"), Problem(f"{F(1, 2)} − {F(3, 4)} − {F(1, 8)}", f"−{F(3, 8)}")])], minutes=20)

REVIEW = Check("Unit 4 Review", [
    S("Compute", [fadd(H(-5, 6), H(1, 3)), fsub(H(-3, 4), H(5, 8)), fadd(H(-11, 4), H(-3, 2)), dadd("-9.6", "4.35"), dsub("-1.2", "-3.05"), Problem(f"{F(3, 11)} as a decimal", "0.2727…")]),
    S("Apply", [Problem(f"Order: −1.5, −{MX(1, 2, 3)}, −1.6", f"−{MX(1, 2, 3)}, −1.6, −1.5"), Problem("Distance between −2.75 and 4.1", "6.85"), Problem("x − y when x = −0.4, y = 1.35", "−1.75"),
                Problem("A balance of −$15.60 gets a $40 deposit and a $9.25 charge.", "$15.15")])], kind="review", minutes=35, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 4 Test", [
    S("Part A · Rational numbers (1 point each)", [Problem(f"{F(9, 16)} as a decimal", "0.5625"), Problem(f"{F(2, 3)} as a decimal", "0.666…"), Problem(f"Order: −0.8, −{F(3, 4)}, −{F(5, 6)}", f"−{F(5, 6)}, −0.8, −{F(3, 4)}"), Problem("|−6.05|", "6.05")]),
    S("Part B · Compute (1 point each)", [fadd(H(-4, 9), H(-2, 3)), fadd(H(7, 10), H(-6, 5)), fsub(H(3, 8), H(-5, 12)), fsub(H(-17, 4), H(11, 6)), dadd("-14.25", "6.8"), dsub("0.45", "2.6"), dsub("-8.3", "-12.05"),
        Problem("−3.75 + 9.2 + 3.75 (mentally)", "9.2")]),
    S("Part C · Applications (2 points each)", [Problem("Temperatures change −2.6°, +4.15°, −0.8° from −1.5°C. Final temperature?", "−0.75°C", space=30, points=2),
        Problem(f"A diver at −{MX(12, 1, 2)} ft rises {MX(7, 3, 4)} ft. Depth now?", f"−{MX(4, 3, 4)} ft", space=30, points=2),
        Problem("Distance between −18.4 m and 22.75 m", "41.15 m", space=30, points=2)]),
    S("Part D · Explain (3 points)", [Problem(f"Ellie says −{MX(2, 1, 4)} + {MX(1, 3, 4)} = −{MX(3, 2, 4)}. Explain her mistake and give the correct answer.", f"She added absolute values; signs differ, so subtract: −{F(2, 4)} = −{F(1, 2)}.", lines=4, space=0, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["18–21 (85%+)", "Mastered."], ["15–17", "Proficient; correct missed items."], ["Below 15", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-01-25", "2027-02-01", "2027-02-08", "2027-02-15"], CHECKS, REVIEW, TEST)

UNIT = Unit(4, "Adding and Subtracting Rational Numbers", "Signed fractions and decimals, converting fractions to decimals, and real-world problems.",
    "The integer rules from Unit 3 work for every rational number. In this unit you will add and subtract signed fractions, mixed numbers, and decimals, and use them to solve problems about money, temperature, and measurement.",
    ["Place and compare signed fractions and decimals.", "Add and subtract signed fractions and mixed numbers.", "Convert fractions to terminating or repeating decimals.", "Add and subtract signed decimals.", "Solve multi-step rational-number problems."],
    [("7.NS.1", "Add and subtract rational numbers; represent on a number line; apply properties."), ("7.NS.2d", "Convert a rational number to a decimal using long division."),
     ("7.NS.3", "Solve real-world problems with the four operations on rational numbers."), ("7.EE.3", "Solve multi-step real-life problems with rational numbers in any form.")],
    [("rational number", "A number that can be written as a fraction of integers."), ("terminating decimal", "A decimal that ends."), ("repeating decimal", "A decimal with a repeating pattern.")],
    ["Integer operations (Unit 3).", "Fraction and decimal operations (Grades 5–6)."], ["Number lines with fractions and decimals", "Two-color counters"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Bank balances, stock prices, tide levels, golf scores, and temperatures use signed fractions and decimals.",
    family_note="Look at a bank statement or a weather report together and talk about the negative numbers you see.",
    weeks=WEEKS)
