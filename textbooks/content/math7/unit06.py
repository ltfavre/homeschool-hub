"""Grade 7 Math · Unit 6: Expressions, Equations, and Inequalities (Mar 29 – Apr 23, 2027)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import F, MX, RF
from content.te import TE, flow
from content.sched import schedule

CW = 205
x, y, n = "<i>x</i>", "<i>y</i>", "<i>n</i>"


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def eq(p, q, r):
    """Problem for p x + q = r with computed solution."""
    sol = Fr(r - q, p)
    qs = f" + {q}" if q >= 0 else f" − {-q}"
    ps = "" if p == 1 else ("−" if p == -1 else sgn(p))
    return Problem(f"{ps}x{qs} = {sgn(r)}", f"x = {RF(sol)}")


def IL(v, d, closed, lo=-6, hi=6, w=CW):
    return lambda t: ineq_line(t, lo, hi, v, d, closed, width=w)


L1 = Lesson("6.1", "Writing Expressions",
    "I can write algebraic expressions from words and real situations.", "7.EE.2, 7.EE.4",
    [("variable", "A letter that stands for a number."), ("expression", "Numbers, variables, and operations without an equals sign, like 3x + 5."),
     ("coefficient", "The number multiplied by a variable. In 3x, the coefficient is 3."), ("term", "A part of an expression separated by + or −.")],
    "A movie ticket costs $9 and popcorn costs $6. Write an expression for the cost of t tickets and one popcorn.",
    [Text(f"An <b>expression</b> uses a variable for an unknown or changing number. The cost is 9 for each ticket, so 9t, plus 6: <b>9t + 6</b>."),
     Figure(lambda t: table(t, [["Words", "Expression"], ["5 more than a number n", "n + 5"], ["3 less than twice a number", "2n − 3"], ["the product of −4 and x", "−4x"],
                                ["a number divided by 6", "n ÷ 6"], ["half of the sum of a number and 8", P(f"{F(1, 2)}(n + 8)", t.cell)]], [3.0 * inch, 2.2 * inch], width=5.2 * inch)),
     WatchOut("“3 less than x” is x − 3, not 3 − x. The order matters for subtraction and division."),
     KeyIdea("Read the words carefully. Use a variable for the unknown and write operations in the correct order.")],
    [Problem("7 less than a number m", "m − 7"), Problem("the quotient of a number and −3", "n ÷ (−3)"), Problem("A $25 bill split among k friends", "25 ÷ k")],
    [S("Warm-Up", [Problem("9 × 4 + 6", "42"), Problem("Name the coefficient in −5y", "−5")]),
     S("Write an expression", [Problem(w, e) for w, e in [("a number increased by 12", "n + 12"), ("8 times a number, minus 4", "8n − 4"), ("the difference of a number and −2", "n − (−2) or n + 2"),
                                                        ("one-third of a number", "n/3"), ("6 less than 5 times a number", "5n − 6"), ("twice the sum of a number and 3", "2(n + 3)")]]),
     S("Write an expression for the situation", [Problem("A phone plan costs $20 plus $0.10 per text t.", "20 + 0.10t", wide=True), Problem("Lillie has d dollars and spends $7.50.", "d − 7.50", wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a real situation for the expression 12h + 15.", "Answers vary, e.g. $12 per hour plus a $15 fee", lines=2, space=0, wide=True)], cols=1)],
    TE("Students write algebraic expressions.", "Rewrite expressions in different forms; write expressions for real situations.", "Workbook Lesson 6.1",
       flow("Arithmetic warm-up.", "Read Let's Explore.", ["Translate the table phrases together.", "Say: Order matters for subtraction and division."], "Try It 1–3."),
       ["Writing 3 − x for “3 less than x.”"], ["Test with a number: 3 less than 10 is 7."], ["Write expressions for family costs."]),
    summary="Use a variable for the unknown and translate words in the correct order.")

L2 = Lesson("6.2", "Evaluating Expressions",
    "I can evaluate expressions for given values, including negative and fractional values.", "7.EE.3",
    [("evaluate", "Substitute values for variables and compute.")],
    "The expression 1.8C + 32 converts Celsius to Fahrenheit. What is −10°C in Fahrenheit?",
    [Example("Substitute", "1.8C + 32 when C = −10", ["1.8(−10) + 32 = −18 + 32."], "14°F"),
     Example("Two variables", "3a − 2b when a = −4, b = 1.5", ["3(−4) − 2(1.5) = −12 − 3."], "−15"),
     KeyIdea("Substitute with parentheses, then follow the order of operations.")],
    [Problem("4x − 7 when x = −2", "−15"), Problem(f"{F(1, 2)}n + 3 when n = −8", "−1"), Problem("a² − b when a = −3, b = 4", "5")],
    [S("Warm-Up", [Problem("1.8 × (−10)", "−18"), Problem("−18 + 32", "14")]),
     S("Evaluate when x = −3, y = 4, z = 0.5", [Problem(e, v) for e, v in [("2x + y", "−2"), ("y − 5x", "19"), ("10z − x", "8"), ("xy", "−12"), ("x² + y²", "25"), ("(y − x) ÷ z", "14")]]),
     S("Solve", [Problem("A taxi costs 2.5m + 3 dollars for m miles. Cost for 12 miles?", "$33", space=24), Problem("Convert 25°C to Fahrenheit with 1.8C + 32.", "77°F", space=24)]),
     S("Exit Ticket", [Problem("Evaluate −2(x − 6) when x = −1.", "14", wide=True)], cols=1)],
    TE("Students evaluate expressions with rational values.", "Solve problems using expressions with rational numbers.", "Workbook Lesson 6.2", flow("Warm-up.", "Read Let's Explore.", ["Substitute with parentheses."], "Try It 1–3."),
       ["x² with x = −3 written as −9."], ["Parentheses first."], ["Convert this week's temperatures."]),
    summary="Substitute in parentheses and follow the order of operations.")

L3 = Lesson("6.3", "Combining Like Terms",
    "I can simplify expressions by combining like terms, including rational coefficients.", "7.EE.1",
    [("like terms", "Terms with the same variable part, like 3x and −5x."), ("constant", "A term without a variable.")],
    "Simplify 4x + 7 − 6x + 2.",
    [Text("<b>Like terms</b> have the same variable part. Add their coefficients. Constants combine with constants."),
     Example("Combine", "4x + 7 − 6x + 2", ["x-terms: 4x − 6x = −2x.", "Constants: 7 + 2 = 9."], "−2x + 9"),
     Example("Rational coefficients", f"{F(1, 2)}a − 0.75a + 3", [f"{F(1, 2)} − 0.75 = 0.5 − 0.75 = −0.25."], "−0.25a + 3"),
     KeyIdea("Only like terms combine. 3x + 2 is already simplified.")],
    [Problem("5y − 8y + 3", "−3y + 3"), Problem("−2m + 6 + 7m − 10", "5m − 4"), Problem("1.5x − 2 + 0.5x", "2x − 2")],
    [S("Warm-Up", [Problem("4 − 6", "−2"), Problem("0.5 − 0.75", "−0.25")]),
     S("Simplify", [Problem(e, v) for e, v in [("9x + 4x", "13x"), ("3a − 8 + 5a", "8a − 8"), ("−6n + 2 − n + 9", "−7n + 11"), ("2.4p − 1.4p + 6", "p + 6"),
                                             (f"{F(2, 3)}k + {F(1, 3)}k − 5", "k − 5"), ("4x + 3y − x − 5y", "3x − 2y")]]),
     S("Exit Ticket", [Problem("Is 5x + 3 equal to 8x? Explain.", "No. They are not like terms. Test x = 2: 5(2) + 3 = 13, but 8(2) = 16.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students combine like terms.", "Apply properties to add, subtract, factor, and expand linear expressions with rational coefficients.", "Algebra tiles (optional), workbook Lesson 6.3",
       flow("Warm-up.", "Read Let's Explore.", ["Color like terms the same color."], "Try It 1–3."), ["Combining x and constants."], ["Highlight like terms."], ["Write 3 expressions that simplify to 2x − 1."]),
    summary="Add the coefficients of like terms; combine constants.")

L4 = Lesson("6.4", "Expressions in Context",
    "I can rewrite an expression to show what it means in a situation.", "7.EE.2",
    [],
    "A store raises a price p by 5%. Two students write p + 0.05p and 1.05p. Are both right?",
    [Text("Both are right! p + 0.05p shows “the price plus 5% of the price.” 1.05p shows “105% of the price.” Rewriting an expression can reveal a new way of seeing the problem."),
     Example("Discount", "A 20% discount on price p", ["p − 0.2p = 0.8p.", "0.8p means you pay 80% of the price."], "0.8p"),
     Example("Perimeter", "A rectangle has length L and width 3. Perimeter?", ["L + 3 + L + 3 = 2L + 6 = 2(L + 3)."], "2(L + 3): twice the sum of length and width"),
     KeyIdea("Equivalent expressions can show different meanings of the same quantity.")],
    [Problem("A 15% tip on bill b, two ways", "b + 0.15b; 1.15b"), Problem("A 30% markdown on price m", "0.7m"), Problem("Equal sides: s + s + s", "3s")],
    [S("Warm-Up", [Problem("1 + 0.05", "1.05"), Problem("1 − 0.2", "0.8")]),
     S("Rewrite and explain", [Problem("p − 0.35p", "0.65p: pay 65%", lines=1, space=0, wide=True), Problem("c + 0.07c", "1.07c: price with 7% tax", lines=1, space=0, wide=True),
                               Problem("2w + 2(w + 4)", "4w + 8: perimeter of a rectangle w by w + 4", lines=1, space=0, wide=True), Problem("x + x + 0.5x", "2.5x", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write two expressions for the price p after a 10% increase. Explain each.", "p + 0.1p (price plus 10%); 1.1p (110% of price)", lines=2, space=0, wide=True)], cols=1)],
    TE("Students interpret equivalent expressions in context.", "Understand that rewriting an expression in different forms can shed light on the problem.", "Workbook Lesson 6.4", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3. Weekly Check tomorrow."),
       ["Writing p + 0.05 instead of p + 0.05p."], ["Plug in p = 100."], ["Rewrite a real sale ad as an expression."]),
    summary="Rewriting expressions reveals different meanings of the same quantity.")

L5 = Lesson("6.5", "The Distributive Property: Expanding",
    "I can expand expressions using the distributive property.", "7.EE.1",
    [("expand", "Rewrite a product as a sum: 3(x + 4) = 3x + 12.")],
    "Expand −2(3x − 5).",
    [Example("Expand", "−2(3x − 5)", ["−2 · 3x = −6x.", "−2 · (−5) = 10."], "−6x + 10"),
     Example("Fractions", f"{F(3, 4)}(8y + 12)", [f"{F(3, 4)} · 8y = 6y; {F(3, 4)} · 12 = 9."], "6y + 9"),
     Example("Expand and combine", "4(x + 2) − 3(x − 1)", ["4x + 8 − 3x + 3."], "x + 11"),
     KeyIdea("Multiply the outside factor (with its sign) by every term inside.")],
    [Problem("5(2a − 3)", "10a − 15"), Problem("−(4m + 1)", "−4m − 1"), Problem(f"−{F(1, 2)}(6n − 10)", "−3n + 5")],
    [S("Warm-Up", [Problem("−2 · (−5)", "10"), Problem(f"{F(3, 4)} · 12", "9")]),
     S("Expand", [Problem(e, v) for e, v in [("3(x + 7)", "3x + 21"), ("−4(2y − 1)", "−8y + 4"), ("0.5(6k + 8)", "3k + 4"), ("−(−3 + p)", "3 − p"), (f"{F(2, 3)}(9x − 3)", "6x − 2"), ("−1.5(4 − 2w)", "−6 + 3w")]]),
     S("Expand and simplify", [Problem("2(x − 4) + 3x", "5x − 8"), Problem("6 − 2(n + 5)", "−2n − 4"), Problem("3(a + 1) − (a − 4)", "2a + 7"), Problem("−5(2 − y) + 4y", "9y − 10")]),
     S("Exit Ticket", [Problem("Expand and simplify: −3(2x + 4) + 7x", "x − 12", wide=True)], cols=1)],
    TE("Students expand expressions.", "Apply properties to expand linear expressions with rational coefficients.", "Workbook Lesson 6.5", flow("Warm-up.", "Read Let's Explore.", ["Draw arrows from the factor to each term."], "Try It 1–3."),
       ["Multiplying only the first term."], ["Arrows."], ["Use area models to show 3(x + 4)."]),
    summary="Multiply the factor by every term inside, keeping signs.")

L6 = Lesson("6.6", "Factoring Expressions",
    "I can factor an expression by finding a common factor.", "7.EE.1",
    [("factor (an expression)", "Rewrite a sum as a product: 6x + 9 = 3(2x + 3)."), ("greatest common factor (GCF)", "The largest number that divides every term.")],
    "A rectangle has area 6x + 9. One side is 3. What is the other side?",
    [Example("Factor out the GCF", "6x + 9", ["GCF of 6 and 9 is 3.", "6x = 3 · 2x; 9 = 3 · 3."], "3(2x + 3)"),
     Example("Negative factor", "−4y + 12", ["Factor −4: −4(y − 3). Check: −4y + 12 ✓."], "−4(y − 3)"),
     KeyIdea("Factoring undoes the distributive property. Always check by expanding.")],
    [Problem("10a + 15", "5(2a + 3)"), Problem("8m − 12", "4(2m − 3)"), Problem("−7n − 21", "−7(n + 3)")],
    [S("Warm-Up", [Problem("GCF of 6 and 9", "3"), Problem("Expand 3(2x + 3)", "6x + 9")]),
     S("Factor", [Problem(e, v) for e, v in [("4x + 20", "4(x + 5)"), ("18y − 24", "6(3y − 4)"), ("9k + 9", "9(k + 1)"), ("−5p + 30", "−5(p − 6)"), ("12 − 16w", "4(3 − 4w)"), ("2.5x + 5", "2.5(x + 2)")]]),
     S("Exit Ticket", [Problem("A rectangle's area is 8x + 32 and one side is 8. Find the other side.", "x + 4", wide=True)], cols=1)],
    TE("Students factor linear expressions.", "Apply properties to factor linear expressions with rational coefficients.", "Workbook Lesson 6.6", flow("Warm-up.", "Read Let's Explore.", ["Area model in reverse."], "Try It 1–3."),
       ["Not factoring from every term."], ["Check by expanding."], ["Factor with fractional GCFs."]),
    summary="Find the GCF, write it outside, and divide each term by it.")

L7 = Lesson("6.7", "Simplifying with Rational Coefficients",
    "I can simplify expressions with fraction and decimal coefficients.", "7.EE.1",
    [],
    f"Simplify {F(1, 2)}(4x − 6) − {F(1, 3)}(3x + 9).",
    [Example("Expand then combine", f"{F(1, 2)}(4x − 6) − {F(1, 3)}(3x + 9)", ["2x − 3 − x − 3."], "x − 6"),
     Example("Decimals", "0.4(5n + 10) − 1.5n", ["2n + 4 − 1.5n."], "0.5n + 4"),
     KeyIdea("Distribute carefully, then combine like terms.")],
    [Problem(f"{F(1, 4)}(8a + 4) + a", "3a + 1"), Problem("0.2(10y − 5) − y", "y − 1"), Problem(f"{F(2, 5)}(10 − 5m) + 3m", "4 + m")],
    [S("Warm-Up", [Problem(f"{F(1, 2)} · 4x", "2x"), Problem("0.4 · 5n", "2n")]),
     S("Simplify", [Problem(e, v) for e, v in [(f"{F(1, 3)}(6x + 3) − x", "x + 1"), ("0.5(4k − 8) + 3k", "5k − 4"), (f"−{F(3, 4)}(4p − 8) + p", "−2p + 6"), ("1.2(5 + 10w) − 2w", "6 + 10w"),
                                             (f"{F(1, 2)}x + {F(1, 4)}x − {F(3, 4)}x", "0"), (f"{F(2, 3)}(3n − 6) − {F(1, 2)}(2n + 4)", "n − 6")]]),
     S("Exit Ticket", [Problem(f"Simplify {F(3, 5)}(10x − 5) − 0.5(2x + 4)", "5x − 5", wide=True)], cols=1)],
    TE("Students simplify expressions with rational coefficients.", "Add, subtract, factor, and expand linear expressions with rational coefficients.", "Workbook Lesson 6.7", flow("Warm-up.", "Read Let's Explore.", ["Distribute then combine."], "Try It 1–3."),
       ["Distributing a negative incorrectly."], ["Rewrite subtraction of a group as + (−)."], ["Write a challenge expression."]),
    summary="Distribute rational factors, then combine like terms.")

L8 = Lesson("6.8", "Equivalent Expressions",
    "I can tell whether two expressions are equivalent and justify my answer.", "7.EE.1, 7.EE.2",
    [("equivalent expressions", "Expressions that are equal for every value of the variable.")],
    "Are 2(x + 3) + x and 3x + 6 equivalent? What about 3(x + 2) and 3x + 2?",
    [Example("Simplify both", "2(x + 3) + x vs 3x + 6", ["2x + 6 + x = 3x + 6.", "Same."], "Equivalent"),
     Example("Test a value", "3(x + 2) vs 3x + 2", ["x = 1: 9 vs 5.", "Different for x = 1."], "Not equivalent"),
     KeyIdea("Simplify both to prove equivalence. One counterexample proves they are not equivalent.")],
    [Problem("4(x − 1) and 4x − 4", "equivalent"), Problem("5 − 2x and 2x − 5", "not equivalent"), Problem("x + x + x + 2 and 3(x + 1) − 1", "equivalent")],
    [S("Warm-Up", [Problem("Expand 2(x + 3)", "2x + 6"), Problem("3(1) + 2", "5")]),
     S("Equivalent? Justify.", [Problem(f"{a} and {b}", v, lines=1, space=0, wide=True) for a, b, v in [("6x − 9", "3(2x − 3)", "Yes (expand)"), ("−(x − 4)", "−x − 4", "No (x = 0: 4 vs −4)"),
                                                                                              ("0.5(4n + 2)", "2n + 1", "Yes"), ("3(a + 2) − a", "2a + 2", "No (= 2a + 6)")]], cols=1),
     S("Exit Ticket", [Problem("Write three expressions equivalent to 4x + 8.", "e.g. 4(x + 2), 2(2x + 4), 5x + 8 − x", lines=2, space=0, wide=True)], cols=1)],
    TE("Students determine and justify equivalence.", "Understand equivalent expressions.", "Workbook Lesson 6.8", flow("Warm-up.", "Read Let's Explore.", ["Simplify vs counterexample."], "Try It 1–3. Weekly Check tomorrow."),
       ["Testing only one value to prove equivalence."], ["Simplify fully."], ["Find a value where 3x + 2 and 3(x + 2) agree? (None.)"]),
    summary="Simplify both to show equivalence; a counterexample shows they're not.")

L9 = Lesson("6.9", "One-Step Equations",
    "I can solve one-step equations with rational numbers.", "7.EE.4a",
    [("equation", "A statement that two expressions are equal."), ("solution", "A value that makes an equation true."), ("inverse operations", "Operations that undo each other.")],
    "x − 4.5 = −2. What number is x?",
    [Text("Use <b>inverse operations</b> to get the variable alone. Do the same thing to both sides to keep the equation balanced."),
     Example("Add", "x − 4.5 = −2", ["Add 4.5 to both sides: x = −2 + 4.5."], "x = 2.5"),
     Example("Divide", "−3y = 18", ["Divide both sides by −3."], "y = −6"),
     Example("Multiply", f"{F(n, 4)} = −5", ["Multiply both sides by 4."], "n = −20"),
     KeyIdea("Undo the operation on the variable. Check by substituting.")],
    [Problem("x + 7 = −3", "x = −10"), Problem("−5m = −35", "m = 7"), Problem(f"{F(2, 3)}k = 8", "k = 12")],
    [S("Warm-Up", [Problem("−2 + 4.5", "2.5"), Problem("18 ÷ (−3)", "−6")]),
     S("Solve", [Problem(e, v) for e, v in [("a + 12 = 5", "a = −7"), ("b − 3.2 = −1.8", "b = 1.4"), ("6c = −45", "c = −7.5"), ("−d = 9", "d = −9"), ("p ÷ (−2) = 11", "p = −22"), (f"{F(3, 4)}w = −9", "w = −12")]]),
     S("Exit Ticket", [Problem(f"Solve and check: −{F(1, 2)}x = 7.", f"x = −14; −{F(1, 2)} · (−14) = 7", lines=1, space=0, wide=True)], cols=1)],
    TE("Students solve one-step equations.", "Solve word problems leading to equations of the form px + q = r.", "Balance picture, workbook Lesson 6.9", flow("Warm-up.", "Read Let's Explore.", ["Balance model; inverse operations."], "Try It 1–3."),
       ["Doing an operation to only one side."], ["Balance scale picture."], ["Write equations for real puzzles."]),
    summary="Use inverse operations on both sides; check by substituting.")

L10 = Lesson("6.10", "Two-Step Equations",
    "I can solve equations of the form px + q = r.", "7.EE.4a",
    [],
    "A gym charges a $25 sign-up fee plus $15 per month. Ellie paid $115. How many months?",
    [Text("15m + 25 = 115. Undo the operations in reverse order: subtract 25 first, then divide by 15."),
     Figure(lambda t: bar_model(t, [("m", 1), ("m", 1), ("…", 1), ("m", 1), ("25", 1.6)], total_label="115", width=W * 0.7)),
     Example("Solve", "15m + 25 = 115", ["Subtract 25: 15m = 90.", "Divide by 15: m = 6.", "Check: 15(6) + 25 = 115 ✓."], "6 months"),
     Example("Negative coefficient", "−4x + 7 = 31", ["−4x = 24.", "x = −6."], "x = −6"),
     KeyIdea("Undo addition/subtraction first, then multiplication/division.")],
    [eq(3, 5, 20), eq(-2, 9, -7), eq(5, -12, 13)],
    [S("Warm-Up", [Problem("115 − 25", "90"), Problem("90 ÷ 15", "6")]),
     S("Solve", [eq(p, q, r) for p, q, r in [(2, 7, 19), (6, -4, 32), (-3, 10, 1), (4, 15, 3), (-7, -2, 26), (8, 5, 9)]]),
     S("Fraction and decimal coefficients", [Problem(f"{F(1, 2)}x + 4 = 10", "x = 12"), Problem("0.25x − 3 = 2", "x = 20"), Problem(f"{F(2, 3)}x − 5 = −1", "x = 6"), Problem("1.5x + 2.5 = −5.5", f"x = −{MX(5, 1, 3)}")]),
     S("Exit Ticket", [Problem("Write and solve: a taxi charges $3 plus $2.50 per mile. The fare was $20.50. How many miles?", "2.5m + 3 = 20.5; m = 7", space=30, wide=True)], cols=1)],
    TE("Students solve two-step equations.", "Solve equations of the form px + q = r fluently.", "Workbook Lesson 6.10", flow("Warm-up.", "Read Let's Explore.", ["Tape diagram, then algebra."], "Try It 1–3."),
       ["Dividing before subtracting."], ["Undo in reverse order."], ["Write a two-step equation for a real cost."]),
    summary="Undo addition or subtraction first, then multiplication or division.")

L11 = Lesson("6.11", "Equations with Parentheses",
    "I can solve equations of the form p(x + q) = r.", "7.EE.4a",
    [],
    "Three friends each buy a $6 ticket plus the same snack. They spend $33 total. How much was each snack?",
    [Text("3(s + 6) = 33. You can divide first or distribute first."),
     Example("Divide first", "3(s + 6) = 33", ["Divide by 3: s + 6 = 11.", "Subtract 6: s = 5."], "$5"),
     Example("Distribute first", "3(s + 6) = 33", ["3s + 18 = 33.", "3s = 15; s = 5."], "$5"),
     KeyIdea("For p(x + q) = r: divide by p first, or distribute and solve. Both work.")],
    [Problem("2(x − 4) = 10", "x = 9"), Problem("−5(y + 1) = 20", "y = −5"), Problem(f"{F(1, 2)}(n + 6) = −3", "n = −12")],
    [S("Warm-Up", [Problem("33 ÷ 3", "11"), Problem("11 − 6", "5")]),
     S("Solve", [Problem(e, v) for e, v in [("4(x + 3) = 28", "x = 4"), ("−2(y − 7) = 6", "y = 4"), ("6(k − 1.5) = 21", "k = 5"), ("−3(m + 4) = −3", "m = −3"), (f"{F(2, 3)}(p − 9) = 4", "p = 15"), ("0.5(w + 8) = −1", "w = −10")]]),
     S("Exit Ticket", [Problem("The perimeter of a rectangle is 2(L + 7) = 46. Find L.", "L = 16", wide=True)], cols=1)],
    TE("Students solve p(x + q) = r equations.", "Solve equations of the form p(x + q) = r fluently.", "Workbook Lesson 6.11", flow("Warm-up.", "Read Let's Explore.", ["Show both methods."], "Try It 1–3."),
       ["Distributing to only the first term."], ["Divide first when it's easy."], ["Which method is faster for 0.5(w + 8) = −1?"]),
    summary="Divide first or distribute first; both give the same solution.")

L12 = Lesson("6.12", "Equation Word Problems",
    "I can write and solve equations for word problems and compare to an arithmetic solution.", "7.EE.4a",
    [],
    "The perimeter of a rectangle is 54 cm. Its length is 6 cm. What is its width?",
    [Example("Algebraic", "2(6) + 2w = 54", ["12 + 2w = 54.", "2w = 42; w = 21."], "21 cm"),
     Example("Arithmetic", "Same problem without a variable", ["54 − 12 = 42 for both widths.", "42 ÷ 2 = 21."], "21 cm (same steps!)"),
     KeyIdea("Equation steps match arithmetic steps. Writing the equation helps organize harder problems.")],
    [Problem("A plumber charges $60 plus $45 per hour. The bill is $240. Hours?", "4 hours"), Problem("Lillie has $18 and saves $7.50 a week. When will she have $63?", "6 weeks"), Problem("The sum of three consecutive integers is 57. The smallest?", "18")],
    [S("Warm-Up", [eq(2, 12, 54), Problem("54 − 12", "42")]),
     S("Write an equation and solve", [
         Problem("A family pays $28 for 4 movie tickets and a $4 snack. Price per ticket?", "4t + 4 = 28; $6", space=30, wide=True),
         Problem("A water tank has 120 gallons and drains 7.5 gallons per minute. When will it have 30 gallons left?", "120 − 7.5m = 30; 12 minutes", space=30, wide=True),
         Problem("Ellie's age times 3, minus 4, is 32. How old is she?", "3a − 4 = 32; 12", space=30, wide=True),
         Problem("A temperature of −8°F rises 2.5° per hour. When will it reach 7°F?", "−8 + 2.5h = 7; 6 hours", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write your own equation word problem with answer x = −3.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve equation word problems.", "Solve word problems leading to px + q = r and p(x + q) = r; compare algebraic and arithmetic solutions.", "Workbook Lesson 6.12", flow("Warm-up.", "Read Let's Explore.", ["Compare the two solution paths."], "Try It 1–3. Weekly Check tomorrow."),
       ["Setting up equations with the wrong operation."], ["Define the variable in words first."], ["Write equations for real family situations."]),
    summary="Define the variable, write the equation, solve, and check in the story.")

L13 = Lesson("6.13", "Writing and Graphing Inequalities",
    "I can write inequalities for situations and graph them on a number line.", "7.EE.4b",
    [("inequality", "A statement that compares with <, >, ≤, or ≥."), ("solution set", "All values that make an inequality true.")],
    "You must be at least 48 inches tall to ride a roller coaster. Write and graph an inequality.",
    [Text("“At least 48” means 48 or more: <b>h ≥ 48</b>. A closed circle means the number is included; an open circle means it is not."),
     Figure(lambda t: Table([[ineq_line(t, 44, 52, 48, "right", True, width=W * 0.45), ineq_line(t, -4, 4, 1, "left", False, width=W * 0.45)],
                             [P("h ≥ 48 (closed circle)", t.small), P("x &lt; 1 (open circle)", t.small)]], colWidths=[W / 2] * 2)),
     Figure(lambda t: table(t, [["Words", "Symbol"], ["at least, no less than", "≥"], ["at most, no more than", "≤"], ["more than, greater than", ">"], ["fewer than, less than", "<"]],
                            [3.0 * inch, 1.2 * inch], width=4.2 * inch)),
     KeyIdea("≤ and ≥ use closed circles; < and > use open circles. The arrow points toward the solutions.")],
    [Problem("No more than 30 students: write it", "s ≤ 30"), Problem("Temperature below −5", "t < −5"), Problem("Graph x ≥ −2: open or closed circle?", "closed")],
    [S("Warm-Up", [Problem("Is 48 ≥ 48 true?", "Yes"), Problem("Is 48 > 48 true?", "No")]),
     S("Write an inequality", [Problem(w, e) for w, e in [("a speed limit of 65 mph", "s ≤ 65"), ("more than 12 players", "p > 12"), ("at least $20", "d ≥ 20"), ("colder than −10°", "t < −10")]]),
     S("Write the inequality shown", [Problem("", "x > 2", fig=IL(2, "right", False), space=0), Problem("", "x ≤ −1", fig=IL(-1, "left", True), space=0),
                                      Problem("", "x ≥ −4", fig=IL(-4, "right", True), space=0), Problem("", "x < 0", fig=IL(0, "left", False), space=0)]),
     S("Exit Ticket", [Problem("Graph t ≤ 3 on a number line.", "closed circle at 3, arrow left", fig=lambda t: ineq_line(t, -5, 5, 0, "left", True, width=W - 60, blank=True), space=0, wide=True)], cols=1)],
    TE("Students write and graph inequalities.", "Write and graph inequalities; interpret solutions in context.", "Workbook Lesson 6.13", flow("Inequality truth checks.", "Read Let's Explore.", ["Teach the word/symbol table and circle rules."], "Try It 1–3."),
       ["Open vs closed circle confusion."], ["‘Or equal’ fills the circle."], ["Find inequalities in signs: speed limits, height limits."]),
    summary="Translate words to <, >, ≤, ≥; graph with open or closed circles.")

L14 = Lesson("6.14", "Solving One-Step Inequalities",
    "I can solve one-step inequalities, including multiplying or dividing by a negative.", "7.EE.4b",
    [],
    "Solve −3x < 12. Is x = −5 a solution? Is x = 0?",
    [Text("Solve inequalities like equations, with one big difference: when you multiply or divide both sides by a <b>negative</b> number, <b>reverse</b> the inequality symbol."),
     Example("Why reverse?", "2 < 5. Multiply both sides by −1.", ["−2 and −5: now −2 > −5.", "Multiplying by a negative flips the order on the number line."], "the symbol must flip"),
     Example("Solve", "−3x < 12", ["Divide by −3 and flip: x > −4.", "Check x = 0: −3(0) = 0 < 12 ✓. Check x = −5: 15 < 12 ✗."], "x > −4"),
     KeyIdea("Flip the inequality symbol when multiplying or dividing by a negative number.")],
    [Problem("x + 6 ≥ 2", "x ≥ −4"), Problem("−5y ≤ 30", "y ≥ −6"), Problem(f"{F(n, '−2')} > 3", "n < −6")],
    [S("Warm-Up", [Problem("Is −2 > −5?", "Yes"), Problem("12 ÷ (−3)", "−4")]),
     S("Solve", [Problem(e, v) for e, v in [("x − 4 < 7", "x < 11"), ("4k ≥ −20", "k ≥ −5"), ("−6m > 18", "m < −3"), ("−p ≤ 2.5", "p ≥ −2.5"), (f"{F(1, 3)}w < −2", "w < −6"), ("−0.5z ≥ −4", "z ≤ 8")]]),
     S("Exit Ticket", [Problem("Solve −2x ≥ 10 and graph it.", "x ≤ −5", fig=lambda t: ineq_line(t, -8, 2, 0, "left", True, width=W - 60, blank=True), space=0, wide=True)], cols=1)],
    TE("Students solve one-step inequalities.", "Solve inequalities; graph the solution set.", "Workbook Lesson 6.14", flow("Warm-up.", "Read Let's Explore.", ["Show why the symbol flips with a number line."], "Try It 1–3."),
       ["Forgetting to flip."], ["Test a value from the answer."], ["Explain the flip rule to a sibling."]),
    summary="Solve like equations, but flip the symbol when multiplying or dividing by a negative.")

L15 = Lesson("6.15", "Two-Step Inequalities",
    "I can solve inequalities of the form px + q > r and graph the solutions.", "7.EE.4b",
    [],
    "Lillie has $20 and earns $8 per hour. How many hours must she work to have at least $100?",
    [Example("Solve", "8h + 20 ≥ 100", ["Subtract 20: 8h ≥ 80.", "Divide by 8: h ≥ 10."], "at least 10 hours"),
     Example("Negative coefficient", "−2x + 5 > 11", ["−2x > 6.", "Divide by −2 and flip: x < −3."], "x < −3"),
     KeyIdea("Use the same steps as two-step equations; flip when dividing by a negative.")],
    [Problem("3x − 4 ≤ 11", "x ≤ 5"), Problem("−4y + 2 > 14", "y < −3"), Problem(f"{F(1, 2)}n + 3 ≥ −1", "n ≥ −8")],
    [S("Warm-Up", [Problem("100 − 20", "80"), Problem("80 ÷ 8", "10")]),
     S("Solve", [Problem(e, v) for e, v in [("2x + 7 > 15", "x > 4"), ("5y − 3 ≤ −18", "y ≤ −3"), ("−3k + 1 ≥ 10", "k ≤ −3"), ("9 − 2m < 1", "m > 4"), ("0.5p + 4 > 1", "p > −6"), ("−x − 6 ≤ −2", "x ≥ −4")]]),
     S("Exit Ticket", [Problem("Solve 6 − 3x ≤ 12 and graph it.", "x ≥ −2", fig=lambda t: ineq_line(t, -6, 4, 0, "right", True, width=W - 60, blank=True), space=0, wide=True)], cols=1)],
    TE("Students solve two-step inequalities.", "Solve word problems leading to inequalities px + q > r or px + q < r; graph and interpret.", "Workbook Lesson 6.15", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."),
       ["Flipping when subtracting a negative constant."], ["Flip only for × or ÷ by a negative."], ["Budget inequality for a purchase."]),
    summary="Two-step inequalities: undo +/− then ×/÷; flip for negatives.")

L16 = Lesson("6.16", "Inequality Word Problems",
    "I can write, solve, and interpret inequalities for real situations.", "7.EE.4b",
    [],
    "A school club has $150 for a pizza party. Each pizza costs $12.50 and delivery is $10. How many pizzas can they buy?",
    [Example("Write, solve, interpret", "12.5p + 10 ≤ 150", ["12.5p ≤ 140.", "p ≤ 11.2."], "at most 11 pizzas (you can't buy part of a pizza)"),
     KeyIdea("Interpret the solution in context: whole numbers only? Must be positive?")],
    [Problem("A phone plan costs $30 + $5 per GB. Budget $60. Max GB?", "6 GB"), Problem("Ellie needs at least 85 points. She has 62. Each task is worth 4 points. How many tasks?", "at least 6 tasks"),
     Problem("An elevator holds at most 2,000 lb. A 180-lb operator rides with boxes of 65 lb. Max boxes?", "28 boxes")],
    [S("Warm-Up", [Problem("150 − 10", "140"), Problem("140 ÷ 12.5", "11.2")]),
     S("Write, solve, and interpret", [
         Problem("A taxi charges $3 plus $2 per mile. You have $25. How far can you ride?", "3 + 2m ≤ 25; at most 11 miles", space=30, wide=True),
         Problem("To keep a B, Lillie needs an average of at least 80 on 4 tests. Her first three scores are 76, 84, 78. What score does she need on test 4?", "(238 + s)/4 ≥ 80 → s ≥ 82", space=30, wide=True),
         Problem("A freezer is at 5°F and cools 3° per hour. When will it be below −10°F?", "5 − 3h < −10; after more than 5 hours", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write an inequality problem where the answer must be a whole number. Solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve inequality word problems.", "Solve word problems leading to inequalities; interpret solutions in context.", "Workbook Lesson 6.16, Unit 6 Review", flow("Warm-up.", "Read Let's Explore.", ["Work the example; discuss interpretation."], "Try It 1–3.", "Workbook Lesson 6.16 and the Unit 6 Review.", "Check. Tomorrow: Unit 6 Test."),
       ["Answering 11.2 pizzas."], ["Ask: does a decimal make sense?"], ["Plan a party budget."]),
    summary="Write, solve, then interpret the solution in context.")

C1 = Check("Weekly Check 16: Expressions", [S("Show what you know", [Problem("Write: 4 less than 3 times a number", "3n − 4"), Problem("Evaluate 5x − 2y when x = −2, y = 3", "−16"),
    Problem("Simplify 7a − 3 − 9a + 8", "−2a + 5"), Problem("Simplify 0.6k + 1.4k − 2", "2k − 2"), Problem("Rewrite p − 0.25p", "0.75p"), Problem("Evaluate x² − x when x = −4", "20")])], minutes=15)
C2 = Check("Weekly Check 17: Equivalent Expressions", [S("Show what you know", [Problem("Expand −3(4x − 2)", "−12x + 6"), Problem("Factor 12y + 18", "6(2y + 3)"), Problem(f"Simplify {F(1, 2)}(6n + 4) − n", "2n + 2"),
    Problem("Simplify 5(x − 2) − 2(x + 1)", "3x − 12"), Problem("Equivalent? 2(x + 5) and 2x + 5", "No"), Problem("Factor −8m + 24", "−8(m − 3)")])], minutes=15)
C3 = Check("Weekly Check 18: Equations", [S("Show what you know", [Problem("x − 6.5 = −2", "x = 4.5"), Problem("−7y = 56", "y = −8"), eq(3, -8, 13), eq(-5, 4, 29), Problem("4(n − 2) = −20", "n = −3"),
    Problem("A $15 fee plus $9 per hour; total $78. Hours?", "7 hours")])], minutes=20)

REVIEW = Check("Unit 6 Review", [
    S("Expressions", [Problem("Evaluate −2a + b² when a = 3, b = −4", "10"), Problem("Simplify 3(2x − 1) − (x + 5)", "5x − 8"), Problem("Factor 15k − 25", "5(3k − 5)"), Problem("Rewrite 1.08c in words", "price plus 8% tax")]),
    S("Equations and inequalities", [eq(4, 9, -11), Problem(f"{F(2, 5)}(x + 10) = 6", "x = 5"), Problem("−3x + 4 > 19", "x < −5"), Problem("7 + 2y ≤ 1", "y ≤ −3"),
        Problem("A pool has 900 gal and drains 25 gal/min. When is it below 400 gal?", "after more than 20 minutes", space=24, wide=True)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 6 Test", [
    S("Part A · Expressions (1 point each)", [Problem("Write: twice the difference of a number and 5", "2(n − 5)"), Problem("Evaluate 3x − y when x = −2, y = −7", "1"), Problem("Simplify −4m + 9 + 6m − 12", "2m − 3"),
        Problem("Expand −5(2 − 3k)", "−10 + 15k"), Problem("Factor 21a + 14", "7(3a + 2)"), Problem(f"Simplify {F(3, 4)}(8x − 4) − 2x", "4x − 3")]),
    S("Part B · Equations (1 point each)", [Problem("y + 8.25 = 3", "y = −5.25"), eq(-6, 0, 39), eq(2, 11, -5), Problem("−3(p + 4) = 9", "p = −7"), Problem(f"{F(1, 3)}n − 2 = 5", "n = 21")]),
    S("Part C · Inequalities (1 point each)", [Problem("x − 3 ≥ −8", "x ≥ −5"), Problem("−4y < 28", "y > −7"), Problem("5 − 2k ≤ 17", "k ≥ −6"), Problem("Graph the answer to the previous problem.", "closed circle at −6, arrow right", fig=lambda t: ineq_line(t, -8, 2, 0, "right", True, width=CW, blank=True), space=0)]),
    S("Part D · Problem solving (3 points each)", [
        Problem("A plumber charges $55 plus $40 per hour. The bill was $235. Write and solve an equation to find the hours.", "55 + 40h = 235; h = 4.5 hours", space=60, wide=True, points=3),
        Problem("Ellie has $35 and wants to buy shirts at $8.50 each with a $3 shipping fee. Write and solve an inequality for the number of shirts. Interpret.", "8.5s + 3 ≤ 35; s ≤ 3.76…, so at most 3 shirts", space=60, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["18–21 (85%+)", "Mastered."], ["15–17", "Proficient; correct missed items."], ["Below 15", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-03-29", "2027-04-05", "2027-04-12", "2027-04-19"], CHECKS, REVIEW, TEST)

UNIT = Unit(6, "Expressions, Equations, and Inequalities", "Writing and simplifying expressions, solving two-step equations, and solving and graphing inequalities.",
    "Algebra lets you describe real situations with symbols and solve for unknowns. You will write and simplify expressions, solve equations like 3x + 5 = 20 and 2(x − 4) = 10, and solve and graph inequalities.",
    ["Write and evaluate expressions with rational numbers.", "Combine like terms, expand, and factor.", "Solve equations of the forms px + q = r and p(x + q) = r.", "Write, solve, and graph inequalities.", "Interpret solutions in real situations."],
    [("7.EE.1", "Apply properties of operations to add, subtract, factor, and expand linear expressions with rational coefficients."), ("7.EE.2", "Understand that rewriting an expression can shed light on a problem."),
     ("7.EE.3", "Solve multi-step real-life problems; assess reasonableness."), ("7.EE.4", "Use variables to construct and solve equations and inequalities to solve problems.")],
    [("variable", "A letter for a number."), ("expression", "No equals sign."), ("equation", "Two expressions are equal."), ("inequality", "Comparison with <, >, ≤, ≥."), ("like terms", "Same variable part.")],
    ["Rational-number operations (Units 3–5).", "One-step equations (Grade 6)."], ["Algebra tiles (optional)", "Balance-scale picture", "Number lines"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Phone plans, taxi fares, savings goals, and grade averages can all be written as equations and inequalities.",
    family_note="When a cost has a fixed fee plus a rate (gym, taxi, phone), ask your student to write and solve an equation for it.",
    weeks=WEEKS)
