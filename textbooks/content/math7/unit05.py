"""Grade 7 Math · Unit 5: Multiplying and Dividing Rational Numbers (Feb 22 – Mar 26, 2027)."""
from fractions import Fraction as Fr
from decimal import Decimal as D
from engine import *
from content.mathkit import F, MX, RF, RD
from content.te import TE, flow
from content.sched import schedule

CW = 205
s = sgn
H = Fr


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def pi_(n):
    return f"({s(n)})" if n < 0 else s(n)


def pf(x):
    return f"({RF(x)})" if Fr(x) < 0 else RF(x)


def pdc(x):
    return f"({RD(x)})" if D(str(x)) < 0 else RD(x)


def imul(a, b):
    return Problem(f"{pi_(a)} × {pi_(b)}", s(a * b))


def idiv(a, b):
    return Problem(f"{s(a)} ÷ {pi_(b)}", s(a // b) if a % b == 0 else RF(Fr(a, b)))


def fmul(a, b):
    return Problem(f"{pf(a)} × {pf(b)}", RF(Fr(a) * Fr(b)))


def fdiv(a, b):
    return Problem(f"{pf(a)} ÷ {pf(b)}", RF(Fr(a) / Fr(b)))


def dmul(a, b):
    return Problem(f"{pdc(a)} × {pdc(b)}", RD(D(a) * D(b)))


def ddiv(a, b):
    return Problem(f"{pdc(a)} ÷ {pdc(b)}", RD(D(a) / D(b)))


L1 = Lesson("5.1", "Multiplying Integers: Patterns",
    "I can use patterns to discover how to multiply positive and negative integers.", "7.NS.2a",
    [("product", "The result of multiplication.")],
    "A pool drains 3 inches of water each hour. What is the change in water level after 4 hours?",
    [Text("Draining means the level <b>changes by −3</b> each hour. Four hours: 4 × (−3) = −3 + (−3) + (−3) + (−3) = −12. The level drops 12 inches."),
     Figure(lambda t: table(t, [["Pattern", "Product"], ["3 × (−2)", "−6"], ["2 × (−2)", "−4"], ["1 × (−2)", "−2"], ["0 × (−2)", "0"], ["−1 × (−2)", "2"], ["−2 × (−2)", "4"]],
                            [1.8 * inch, 1.2 * inch], width=3.0 * inch)),
     Text("Look at the pattern: each time the first factor goes down by 1, the product goes <b>up</b> by 2. Continue past 0 and the products become positive. So a negative times a negative is positive."),
     KeyIdea("Positive × negative = negative. Negative × negative = positive.")],
    [imul(5, -6), imul(-7, -3), imul(-9, 4)],
    [S("Warm-Up", [Problem("−3 + (−3) + (−3) + (−3)", "−12"), Problem("6 × 7", "42")]),
     S("Multiply", [imul(a, b) for a, b in [(3, -8), (-5, 7), (-6, -6), (-11, 2), (-4, -9), (12, -3), (-1, -15), (0, -23)]]),
     S("Complete the pattern", [Problem("3 × (−5) = −15, 2 × (−5) = ___, 1 × (−5) = ___, 0 × (−5) = ___, −1 × (−5) = ___", "−10, −5, 0, 5", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Use a pattern to explain why −3 × (−4) is positive.", "Each time the first factor drops by 1, the product rises by 4: 0 × (−4) = 0, −1 × (−4) = 4, −2 × (−4) = 8, −3 × (−4) = 12.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students discover integer multiplication rules through patterns.", "Understand that multiplication extends from fractions to rational numbers by requiring that operations continue to satisfy the properties.", "Workbook Lesson 5.1",
       flow("Repeated addition.", "Read Let's Explore.", ["Build the pattern table together and predict the next rows.", "Say: The pattern forces negative × negative to be positive."], "Try It 1–3."),
       ["Applying addition rules (sign of larger absolute value) to multiplication."], ["Repeated addition for pos × neg."], ["Why must (−1)(−1) = 1? Use the distributive property: (−1)(1 + (−1)) = 0."]),
    summary="Same signs → positive product. Different signs → negative product.")

L2 = Lesson("5.2", "Multiplying Integers: Rules and Reasons",
    "I can multiply integers, including more than two factors, and explain the sign rules.", "7.NS.2a, 7.NS.2c",
    [],
    "What is (−2) × (−3) × (−5)? How can you tell the sign before multiplying?",
    [Text("Multiply the absolute values, then decide the sign. Each pair of negatives makes a positive. So an <b>even</b> number of negative factors gives a positive product, and an <b>odd</b> number gives a negative product."),
     Example("Three factors", "(−2)(−3)(−5)", ["Three negative factors: odd → negative.", "2 × 3 × 5 = 30."], "−30"),
     Example("Using the distributive property", "Why is (−1)(−1) = 1?", ["(−1)(1 + (−1)) = (−1)(0) = 0.", "So (−1)(1) + (−1)(−1) = 0, which means −1 + (−1)(−1) = 0.", "(−1)(−1) must be 1."], "The rules keep the properties true."),
     KeyIdea("Count the negative factors: even → positive, odd → negative.")],
    [Problem("(−4)(5)(−2)", "40"), Problem("(−1)(−1)(−1)(−1)(−1)", "−1"), Problem("(−3)²", "9")],
    [S("Warm-Up", [imul(-4, 5), imul(-20, -2)]),
     S("Multiply", [Problem(e, v) for e, v in [("(−2)(6)(−3)", "36"), ("(−5)(−2)(−4)", "−40"), ("(7)(−1)(3)", "−21"), ("(−3)(−3)(−3)", "−27"), ("(−10)(−10)", "100"), ("(−2)(−2)(−2)(−2)", "16")]]),
     S("Sign only", [Problem("Is the product of 9 negative numbers positive or negative?", "negative"), Problem("Is (−8)(−7)(−6)(−5) positive or negative?", "positive")]),
     S("Exit Ticket", [Problem("Explain why (−4)² and −4² are different.", "(−4)² = 16; −4² = −(4²) = −16.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students multiply integers with several factors.", "Interpret products of rational numbers; understand (−1)(−1) = 1.", "Workbook Lesson 5.2", flow("Warm-up.", "Read Let's Explore.", ["Count negatives; work examples."], "Try It 1–3."),
       ["(−3)² = −9."], ["Parentheses mean the sign is included."], ["Prove (−a)(−b) = ab with the distributive property."]),
    summary="Even number of negative factors → positive; odd → negative.")

L3 = Lesson("5.3", "Dividing Integers",
    "I can divide integers using the related multiplication fact.", "7.NS.2b",
    [("quotient", "The result of division.")],
    "A diver descends 60 feet in 5 minutes at a steady rate. What is the change in depth per minute?",
    [Text("−60 ÷ 5 = ? asks: 5 × ? = −60. Since 5 × (−12) = −60, the answer is −12 feet per minute."),
     Figure(lambda t: table(t, [["Division", "Because", "Quotient"], ["−60 ÷ 5", "5 × (−12) = −60", "−12"], ["60 ÷ (−5)", "−5 × (−12) = 60", "−12"], ["−60 ÷ (−5)", "−5 × 12 = −60", "12"]],
                            [1.5 * inch, 2.0 * inch, 1.1 * inch], width=4.6 * inch)),
     KeyIdea("Division sign rules match multiplication: same signs → positive; different signs → negative. You can never divide by 0.")],
    [idiv(-42, 6), idiv(56, -8), idiv(-81, -9)],
    [S("Warm-Up", [imul(5, -12), imul(-5, 12)]),
     S("Divide", [idiv(a, b) for a, b in [(-36, 4), (45, -9), (-72, -8), (100, -25), (-90, 10), (-64, -16), (0, -7), (-150, 30)]]),
     S("Solve", [Problem("The temperature dropped 18°F in 6 hours at a steady rate. Change per hour?", "−3°F per hour", space=24), Problem("A stock lost $48 over 4 days, the same each day. Daily change?", "−$12", space=24)]),
     S("Exit Ticket", [Problem("Why is −5 ÷ 0 undefined?", "No number times 0 equals −5.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students divide integers.", "Understand that integers can be divided, provided the divisor is not zero; quotients follow sign rules.", "Workbook Lesson 5.3", flow("Warm-up.", "Read Let's Explore.", ["Use fact families to justify each row."], "Try It 1–3."),
       ["Dividing by 0."], ["Fact families."], ["Find the average daily temperature change for a week."]),
    summary="Divide absolute values; same signs → positive, different signs → negative.")

L4 = Lesson("5.4", "Negative Fractions and Signs of Quotients",
    f"I can explain why −({F('p', 'q')}) = {F('−p', 'q')} = {F('p', '−q')}.", "7.NS.2b",
    [],
    f"Are −{F(3, 4)}, {F('−3', 4)}, and {F(3, '−4')} the same number?",
    [Text(f"Yes. A fraction is a division: {F('−3', 4)} = −3 ÷ 4 = −0.75 and {F(3, '−4')} = 3 ÷ (−4) = −0.75. Both equal −{F(3, 4)}."),
     Example("Where the sign goes", f"{F('−12', '−3')}", ["−12 ÷ (−3) = 4."], "4 (two negatives make a positive)"),
     KeyIdea(f"−({F('p', 'q')}) = {F('−p', 'q')} = {F('p', '−q')}. A fraction with one negative sign is negative.")],
    [Problem(f"Simplify {F('−18', 6)}", "−3"), Problem(f"Simplify {F(20, '−5')}", "−4"), Problem(f"Simplify {F('−7', '−14')}", F(1, 2))],
    [S("Warm-Up", [idiv(-18, 6), idiv(20, -5)]),
     S("Simplify", [Problem(F(a, b), RF(Fr(int(a.replace('−', '-')), int(b.replace('−', '-'))))) for a, b in [("−24", "8"), ("35", "−7"), ("−9", "−3"), ("−5", "10"), ("6", "−8"), ("−15", "−20")]]),
     S("Same or different?", [Problem(f"−{F(2, 5)} and {F('−2', 5)}", "same", choices=["same", "different"]), Problem(f"{F('−4', '−9')} and −{F(4, 9)}", "different", choices=["same", "different"])]),
     S("Exit Ticket", [Problem(f"Write −{F(5, 6)} two other ways.", f"{F('−5', 6)} and {F(5, '−6')}", wide=True)], cols=1)],
    TE("Students interpret signs in fractions.", "If p and q are integers, −(p/q) = (−p)/q = p/(−q).", "Workbook Lesson 5.4", flow("Warm-up.", "Read Let's Explore.", ["Evaluate each form as division."], "Try It 1–3. Weekly Check tomorrow."),
       ["Thinking −3/−4 is negative."], ["Treat the fraction bar as division."], ["Explain to a sibling with money owed shared among friends."]),
    summary="One negative sign anywhere makes the fraction negative; two make it positive.")

L5 = Lesson("5.5", "Multiplying Signed Fractions",
    "I can multiply positive and negative fractions and mixed numbers.", "7.NS.2a, 7.NS.2c",
    [],
    f"A recipe needs {F(3, 4)} cup of sugar, but you're making {F(2, 3)} of the recipe. A water tank loses {F(1, 2)} gallon per minute for {F(3, 4)} minute. What are the products?",
    [Example("Fractions", f"{F(2, 3)} × {F(3, 4)}", [f"Multiply numerators and denominators: {F(6, 12)} = {F(1, 2)}."], F(1, 2) + " cup"),
     Example("With a negative", f"(−{F(1, 2)}) × {F(3, 4)}", ["Different signs → negative.", f"{F(1, 2)} × {F(3, 4)} = {F(3, 8)}."], f"−{F(3, 8)} gallon"),
     Example("Mixed numbers", f"(−{MX(1, 1, 2)}) × (−{MX(2, 2, 3)})", [f"= {F(3, 2)} × {F(8, 3)} (two negatives → positive).", f"= {F(24, 6)} = 4."], "4"),
     KeyIdea("Decide the sign, multiply the absolute values, and simplify. Change mixed numbers to improper fractions.")],
    [fmul(H(-2, 5), H(3, 4)), fmul(H(-5, 6), H(-3, 10)), fmul(H(-9, 4), H(2, 3))],
    [S("Warm-Up", [Problem(f"{F(2, 3)} × {F(3, 4)}", F(1, 2)), imul(-2, 3)]),
     S("Multiply", [fmul(a, b) for a, b in [(H(-1, 3), H(6, 7)), (H(4, 5), H(-5, 8)), (H(-3, 4), H(-2, 9)), (H(-7, 2), H(4, 7)), (H(-5, 2), H(-5, 2)), (H(10, 3), H(-9, 20))]]),
     S("Solve", [Problem(f"A diver descends at {MX(2, 1, 4)} ft per second for {F(4, 3)} seconds. Change in depth?", "−3 ft", space=24, wide=True)], cols=1),
     S("Exit Ticket", [fmul(H(-15, 4), H(-8, 5))], cols=1)],
    TE("Students multiply signed fractions.", "Multiply rational numbers.", "Workbook Lesson 5.5", flow("Warm-up.", "Read Let's Explore.", ["Sign first, then multiply and simplify."], "Try It 1–3."),
       ["Using common denominators for multiplication."], ["Cross-simplify before multiplying."], ["Scale a recipe by −? (Why doesn't that make sense?)"]),
    summary="Sign first; then multiply numerators and denominators.")

L6 = Lesson("5.6", "Dividing Signed Fractions",
    "I can divide positive and negative fractions.", "7.NS.2b, 7.NS.2c",
    [("reciprocal", f"Two numbers whose product is 1, like {F(2, 3)} and {F(3, 2)}.")],
    f"A tank's level fell {F(3, 4)} ft over {F(3, 8)} hour. What is the change per hour?",
    [Example("Divide", f"(−{F(3, 4)}) ÷ {F(3, 8)}", ["Different signs → negative.", f"{F(3, 4)} × {F(8, 3)} = {F(24, 12)} = 2."], "−2 ft per hour"),
     Example("Two negatives", f"(−{F(5, 6)}) ÷ (−{F(5, 12)})", [f"Positive. {F(5, 6)} × {F(12, 5)} = 2."], "2"),
     KeyIdea("To divide, multiply by the reciprocal of the divisor. Sign rules are the same.")],
    [fdiv(H(-2, 3), H(4, 9)), fdiv(H(7, 8), H(-7, 16)), fdiv(H(-5, 2), H(-3, 4))],
    [S("Warm-Up", [Problem(f"Reciprocal of −{F(3, 8)}", f"−{F(8, 3)}"), Problem(f"{F(3, 4)} × {F(8, 3)}", "2")]),
     S("Divide", [fdiv(a, b) for a, b in [(H(-1, 2), H(1, 4)), (H(3, 5), H(-9, 10)), (H(-4, 7), H(-2, 7)), (H(-6), H(3, 4)), (H(5, 4), H(-5, 2)), (H(-9, 2), H(-3, 8))]]),
     S("Solve", [Problem(f"A hiker descends {MX(4, 1, 2)} miles in {F(3, 4)} hour. Change in elevation per hour (in miles)?", "−6 miles per hour", space=24, wide=True)], cols=1),
     S("Exit Ticket", [fdiv(H(-10, 3), H(5, 6))], cols=1)],
    TE("Students divide signed fractions.", "Divide rational numbers.", "Workbook Lesson 5.6", flow("Warm-up.", "Read Let's Explore.", ["Multiply by reciprocal; sign rules."], "Try It 1–3."),
       ["Flipping the dividend."], ["Keep-change-flip with signs."], ["Write a story for −2 ÷ 1/4."]),
    summary="Multiply by the reciprocal; use the same sign rules.")

L7 = Lesson("5.7", "Multiplying and Dividing Signed Decimals",
    "I can multiply and divide positive and negative decimals.", "7.NS.2",
    [],
    "A stock fell $1.25 per share. Ellie owns 8 shares. What is the total change? Over 4 days, what was the average daily change?",
    [Example("Multiply", "8 × (−1.25)", ["8 × 1.25 = 10. Different signs → negative."], "−$10"),
     Example("Divide", "−10 ÷ 4", ["10 ÷ 4 = 2.5. Negative."], "−$2.50 per day"),
     KeyIdea("Multiply or divide the decimals, then apply the sign rules.")],
    [dmul("-0.6", "4.5"), ddiv("-7.2", "-0.9"), dmul("-2.5", "-0.4")],
    [S("Warm-Up", [Problem("8 × 1.25", "10"), Problem("10 ÷ 4", "2.5")]),
     S("Compute", [dmul(a, b) for a, b in [("-3.2", "5"), ("-0.25", "-12"), ("1.5", "-0.6")]] + [ddiv(a, b) for a, b in [("-8.4", "4"), ("6.3", "-0.7"), ("-0.48", "-0.06")]]),
     S("Solve", [Problem("A submarine changes depth by −12.5 m per minute. Change in 3.2 minutes?", "−40 m", space=24), Problem("A temperature fell 7.2°F in 1.5 hours. Change per hour?", "−4.8°F", space=24)]),
     S("Exit Ticket", [ddiv("-13.5", "0.45")], cols=1)],
    TE("Students multiply and divide signed decimals.", "Multiply and divide rational numbers.", "Workbook Lesson 5.7", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."),
       ["Decimal placement errors."], ["Estimate first."], ["Compute real stock changes."]),
    summary="Compute with decimals, then apply sign rules.")

L8 = Lesson("5.8", "Rational Number Operations Practice",
    "I can multiply and divide any rational numbers fluently.", "7.NS.2",
    [],
    f"Which is greater: (−{F(3, 4)})(−0.8) or (−1.2) ÷ (−{F(3, 2)})?",
    [Example("Compare", "Both products/quotients", [f"(−{F(3, 4)})(−0.8) = 0.75 × 0.8 = 0.6.", f"(−1.2) ÷ (−1.5) = 0.8."], "the second (0.8 > 0.6)"),
     KeyIdea("Convert to one form (all fractions or all decimals) when operations mix.")],
    [Problem(f"(−0.5) × {F(4, 5)}", "−0.4"), Problem(f"{F(9, 10)} ÷ (−0.3)", "−3"), Problem(f"(−{MX(1, 1, 4)})(−0.8)", "1")],
    [S("Warm-Up", [dmul("0.75", "0.8"), ddiv("1.2", "1.5")]),
     S("Compute", [Problem(e, v) for e, v in [(f"(−0.25)(−{F(4, 5)})", "0.2"), (f"−{F(3, 8)} ÷ 0.75", "−0.5"), (f"(−2.4)({F(5, 6)})", "−2"), (f"−{MX(2, 1, 2)} ÷ (−0.5)", "5"), ("(−1.5)(−1.5)", "2.25"), (f"{F(1, 3)} ÷ (−{F(1, 9)})", "−3")]]),
     S("Exit Ticket", [Problem(f"Evaluate (−{F(2, 5)})(1.5) ÷ (−0.3).", "2", wide=True)], cols=1)],
    TE("Students compute fluently with rational numbers.", "Apply properties of operations to multiply and divide rational numbers.", "Workbook Lesson 5.8", flow("Warm-up.", "Read Let's Explore.", ["Convert; compute."], "Try It 1–3. Weekly Check tomorrow."),
       ["Sign errors in multi-step products."], ["Sign first."], ["Rational-number bingo."]),
    summary="Convert to one form, decide the sign, then compute.")

L9 = Lesson("5.9", "Order of Operations with Rational Numbers",
    "I can use the order of operations with positive and negative numbers.", "7.NS.3, 7.EE.3",
    [("order of operations", "Parentheses, exponents, multiplication and division (left to right), addition and subtraction (left to right).")],
    "Evaluate −3 + 4 × (−2)² ÷ 8.",
    [Example("Order", "−3 + 4 × (−2)² ÷ 8", ["Exponent: (−2)² = 4.", "Multiply/divide left to right: 4 × 4 = 16; 16 ÷ 8 = 2.", "Add: −3 + 2 = −1."], "−1"),
     Example("Parentheses with negatives", "(−6 − 4) ÷ (−5) + 3", ["(−10) ÷ (−5) = 2.", "2 + 3 = 5."], "5"),
     KeyIdea("Same order of operations as always; keep track of every sign.")],
    [Problem("−8 + 3 × (−2)", "−14"), Problem("(−4)² − 10", "6"), Problem("12 ÷ (−3) × (−2)", "8")],
    [S("Warm-Up", [Problem("(−2)²", "4"), Problem("−3 + 2", "−1")]),
     S("Evaluate", [Problem(e, v) for e, v in [("5 − 2 × (−4)", "13"), ("−18 ÷ 3 + (−2)", "−8"), ("(−3)² − (−3)", "12"), ("−2(5 − 9)", "8"), ("(1 − 7)(−2) ÷ 4", "3"), ("−4² + (−4)²", "0")]]),
     S("Exit Ticket", [Problem("Evaluate −0.5(6 − 10) + 1.5².", "4.25", space=24, wide=True)], cols=1)],
    TE("Students apply order of operations with rational numbers.", "Solve problems with the four operations on rational numbers.", "Workbook Lesson 5.9", flow("Warm-up.", "Read Let's Explore.", ["Work both examples step by step."], "Try It 1–3."),
       ["−4² = 16."], ["Write each step on a new line."], ["Create an expression equal to −10 using 4 operations."]),
    summary="Follow the order of operations and track signs at each step.")

L10 = Lesson("5.10", "The Distributive Property with Rational Numbers",
    "I can use the distributive property with negative numbers.", "7.NS.2a, 7.EE.1",
    [("distributive property", "a(b + c) = ab + ac")],
    "How could you compute −4 × 2.75 in your head?",
    [Example("Mental math", "−4 × 2.75", ["2.75 = 3 − 0.25.", "−4(3 − 0.25) = −12 + 1 = −11."], "−11"),
     Example("Distribute a negative", "−3(x − 5)", ["−3 · x + (−3)(−5) = −3x + 15."], "−3x + 15"),
     KeyIdea("Distribute the sign too: −a(b − c) = −ab + ac.")],
    [Problem("−5(2 + 0.4)", "−12"), Problem("−2(y − 7)", "−2y + 14"), Problem(f"−{F(1, 2)}(8 − 6)", "−1")],
    [S("Warm-Up", [imul(-4, 3), Problem("(−4)(−0.25)", "1")]),
     S("Use the distributive property", [Problem(e, v) for e, v in [("−6 × 1.5 (think 6 × (1 + 0.5))", "−9"), ("−8(10 − 0.5)", "−76"), ("−3(4x + 2)", "−12x − 6"), ("−(a − 9)", "−a + 9"),
                                                                     (f"{F(2, 3)}(9 − 12)", "−2"), ("−0.5(4n − 10)", "−2n + 5")]]),
     S("Exit Ticket", [Problem("Show two ways to evaluate −7(5 − 2).", "−7(3) = −21; −35 + 14 = −21", lines=2, space=0, wide=True)], cols=1)],
    TE("Students apply the distributive property with negatives.", "Apply properties of operations as strategies to multiply rational numbers and to expand linear expressions.", "Workbook Lesson 5.10", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."),
       ["−3(x − 5) = −3x − 15."], ["Arrows from the factor to each term."], ["Mental math with distribution."]),
    summary="Distribute the factor (with its sign) to every term.")

L11 = Lesson("5.11", "Repeated Change: Rate × Time",
    "I can model repeated change with multiplication of signed numbers.", "7.NS.2a, 7.NS.3",
    [],
    "A balloon descends 4.5 meters per minute. Where was it 3 minutes ago, compared to now? Where will it be 3 minutes from now?",
    [Text("Use (rate) × (time). Descending is a negative rate: −4.5 m/min. Future time is positive; past time is negative."),
     Example("Future", "(−4.5)(3)", ["Different signs → negative."], "−13.5 m (13.5 m lower)"),
     Example("Past", "(−4.5)(−3)", ["Same signs → positive."], "+13.5 m (it was 13.5 m higher)"),
     KeyIdea("Negative × negative = positive makes sense: going back in time while descending means you were higher.")],
    [Problem("Rate −2°F/hour; 5 hours later", "−10°F"), Problem("Rate −2°F/hour; 5 hours ago", "+10°F"), Problem("Rate +3 cm/day; 4 days ago", "−12 cm")],
    [S("Warm-Up", [dmul("-4.5", "3"), dmul("-4.5", "-3")]),
     S("Solve", [Problem("A tank drains 1.5 gallons per minute. Change after 8 minutes?", "−12 gallons", space=24), Problem("Same tank: change compared to 8 minutes ago?", "It had 12 gallons more", space=24),
                 Problem("Temperature rises 1.2° per hour. Compared to now, what was it 6 hours ago?", "7.2° lower (−7.2)", space=24), Problem("A diver ascends 0.75 m/s. Change in 20 s?", "+15 m", space=24)]),
     S("Exit Ticket", [Problem("Explain (−3)(−4) = 12 using a temperature that drops 3° per hour.", "4 hours ago it was 12° warmer.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students model repeated change with signed multiplication.", "Interpret products of rational numbers by describing real-world contexts.", "Workbook Lesson 5.11", flow("Warm-up.", "Read Let's Explore.", ["Timeline with past (negative) and future (positive)."], "Try It 1–3."),
       ["Confusing direction."], ["Timeline diagram."], ["Make a ‘time machine’ story for (−5)(−2)."]),
    summary="Rate × time; negative times negative means going back in time while decreasing.")

L12 = Lesson("5.12", "Choosing the Operation",
    "I can decide which operation fits a situation with rational numbers.", "7.NS.3",
    [],
    "A hiker's elevation changed by −1,240 ft over 4 hours. Is the average change per hour found by multiplying or dividing?",
    [Figure(lambda t: table(t, [["Situation", "Operation"], ["combine changes", "add"], ["difference / change between", "subtract"], ["repeated equal change", "multiply"], ["equal share / average rate", "divide"]],
                            [2.6 * inch, 1.6 * inch], width=4.2 * inch)),
     Example("Average change", "−1,240 ft over 4 hours", ["Equal share per hour → divide: −1,240 ÷ 4."], "−310 ft per hour"),
     KeyIdea("Think about what is happening, not just key words.")],
    [Problem("Lost 3.5 lb a week for 6 weeks: total change?", "−21 lb (multiply)"), Problem("From −8°F to 5°F: change?", "13°F (subtract)"), Problem("−$84 over 7 days: average daily change?", "−$12 (divide)")],
    [S("Warm-Up", [idiv(-1240, 4), dmul("-3.5", "6")]),
     S("Which operation? Then solve.", [Problem("A balance of −$45 gets a $60 deposit.", "add; $15"), Problem("A plane descends 300 ft/min for 12 min.", "multiply; −3,600 ft"),
                                         Problem("Temperatures −6° and 9°: how far apart?", "subtract; 15°"), Problem("A stock drops $36.60 over 6 days. Average?", "divide; −$6.10/day")]),
     S("Exit Ticket", [Problem("Write a situation for each operation using negative numbers.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students choose operations for rational-number situations.", "Solve real-world problems with the four operations on rational numbers.", "Workbook Lesson 5.12", flow("Warm-up.", "Read Let's Explore.", ["Sort situation cards by operation."], "Try It 1–3. Weekly Check tomorrow."),
       ["Key-word guessing."], ["Act out or draw."], ["Write a 4-operation story."]),
    summary="Combine → add; compare → subtract; repeat → multiply; share or average → divide.")

L13 = Lesson("5.13", "Average Change",
    "I can find the mean of positive and negative numbers.", "7.NS.3",
    [("mean (average)", "The sum of the values divided by how many values there are.")],
    "Daily temperature changes: −4°, +2°, −7°, +1°, −2°. What was the average daily change?",
    [Example("Mean", "−4, 2, −7, 1, −2", ["Sum: −4 + 2 − 7 + 1 − 2 = −10.", "Divide by 5: −10 ÷ 5 = −2."], "−2° per day"),
     KeyIdea("Mean = sum ÷ count. A negative mean means a typical decrease.")],
    [Problem("Mean of −3, 5, −8, 2", "−1"), Problem("Mean of −1.5, −2.5, 1", "−1"), Problem("Golf scores −2, 0, −3, +1: mean", "−1")],
    [S("Warm-Up", [Problem("−4 + 2 − 7 + 1 − 2", "−10"), idiv(-10, 5)]),
     S("Find the mean", [Problem(", ".join(s(v) for v in vals), RF(Fr(sum(vals), len(vals)))) for vals in [[-6, 4, -2, 0], [-10, -15, -5], [3, -9, 6, -12, 2], [-1, -1, -1, 7]]]),
     S("Solve", [Problem("A stock changed −$1.20, +$0.60, −$0.90, +$0.30 over 4 days. Mean daily change?", "−$0.30", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Find 4 numbers with a mean of −3.", "e.g. −3, −3, −3, −3 or −10, 2, −5, 1", lines=1, space=0, wide=True)], cols=1)],
    TE("Students compute means of signed data.", "Solve real-world problems with rational numbers.", "Workbook Lesson 5.13", flow("Warm-up.", "Read Let's Explore.", ["Compute mean."], "Try It 1–3."), ["Ignoring signs when summing."], ["Group positives and negatives."], ["Mean of a week's real temperature changes."]),
    summary="Mean = sum ÷ count; signs matter in the sum.")

L14 = Lesson("5.14", "Rate Problems with Negatives",
    "I can solve rate problems that involve decreases.", "7.NS.3, 7.RP.1",
    [],
    "A cold front drops the temperature from 18°F to −6°F in 8 hours. What is the rate of change per hour?",
    [Example("Rate of change", "18 → −6 in 8 hours", ["Change: −6 − 18 = −24.", "Rate: −24 ÷ 8 = −3."], "−3°F per hour"),
     Example("Predict", "At −3°F per hour, when will it reach −15°F from −6°F?", ["Change needed: −15 − (−6) = −9.", "−9 ÷ (−3) = 3 hours."], "3 hours later"),
     KeyIdea("Rate of change = change ÷ time. Change = end − start.")],
    [Problem("A pool level drops from 60 in. to 48 in. in 4 days. Rate?", "−3 in. per day"), Problem("A balance goes from $50 to −$25 in 5 weeks. Rate?", "−$15 per week"), Problem("Elevation 2,400 ft to 600 ft in 3 hours. Rate?", "−600 ft per hour")],
    [S("Warm-Up", [Problem("−6 − 18", "−24"), idiv(-24, 8)]),
     S("Solve", [Problem("A submarine goes from −40 m to −220 m in 12 minutes. Rate?", "−15 m per minute", space=24), Problem("At that rate, how long from −220 m to −400 m?", "12 minutes", space=24),
                 Problem("A plant's height changes from 14.5 cm to 11.3 cm in 4 days (drought). Rate?", "−0.8 cm per day", space=24), Problem("−$2.40 per day. After how many days is the change −$16.80?", "7 days", space=24)]),
     S("Exit Ticket", [Problem("Temperature drops 2.5° per hour from 10°. What is it after 6 hours?", "−5°", space=24, wide=True)], cols=1)],
    TE("Students solve rate problems with negative rates.", "Compute unit rates; solve real-world problems with rational numbers.", "Workbook Lesson 5.14", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."), ["Start − end instead of end − start."], ["Label start/end."], ["Track a real cold front."]),
    summary="Rate of change = (end − start) ÷ time.")

L15 = Lesson("5.15", "Multi-Step Rational Number Problems",
    "I can solve multi-step problems using all four operations with rational numbers.", "7.EE.3, 7.NS.3",
    [],
    "A business lost $1,250 per month for 3 months, then earned $2,400 per month for 2 months. What is the average monthly result?",
    [Example("All operations", "3 months at −$1,250, 2 months at +$2,400", ["Total: 3(−1,250) + 2(2,400) = −3,750 + 4,800 = 1,050.", "Average: 1,050 ÷ 5 = 210."], "+$210 per month"),
     KeyIdea("Organize the steps; estimate to check the sign and size.")],
    [Problem("4(−2.5) + 3(1.5)", "−5.5"), Problem(f"(−{F(3, 4)} + {F(1, 2)}) × 8", "−2"), Problem("(−12 − 6) ÷ (−3) + 2", "8")],
    [S("Warm-Up", [imul(3, -1250), imul(2, 2400)]),
     S("Solve", [Problem("A diver descends 2.4 m every 10 seconds for 50 seconds, then rises 3 m. Final change?", "−9 m", space=30, wide=True),
                 Problem(f"Ellie's savings change by −$12.50 a week for 4 weeks, then +$20 a week for 3 weeks. Net change?", "+$10", space=30, wide=True),
                 Problem("The temperature was 4°C. It fell 1.5°C per hour for 6 hours, then rose 2°C. Final temperature?", "−3°C", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a problem whose answer is −8 using all four operations.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve multi-step rational problems.", "Solve multi-step real-life problems with rational numbers in any form; assess reasonableness.", "Workbook Lesson 5.15", flow("Warm-up.", "Read Let's Explore.", ["Work the example."], "Try It 1–3."), ["Skipping steps."], ["Table of steps."], ["Plan a budget with gains and losses."]),
    summary="Break the problem into steps, use the right operation for each, and check.")

L16 = Lesson("5.16", "Rational Number Operations Problem Solving",
    "I can use all four operations with rational numbers to solve problems.", "7.NS.1–3",
    [],
    "Design a ‘temperature challenge’: start at 5°F, apply four changes so that the final temperature is −7°F and the average change is −3°F.",
    [Example("Work backward", "Average −3 over 4 changes", ["Total change = 4 × (−3) = −12.", "5 + (−12) = −7 ✓. Any 4 changes summing to −12 work, e.g., −5, +2, −6, −3."], "−5, +2, −6, −3"),
     KeyIdea("Use multiplication and division to plan totals and averages.")],
    [Problem("(−2.5)(−4) ÷ (−5)", "−2"), Problem(f"−{F(2, 3)} ÷ {F(4, 9)}", f"−{MX(1, 1, 2)}"), Problem("Mean of −4.2, 1.8, −3", "−1.8")],
    [S("Warm-Up", [imul(4, -3), Problem("5 + (−12)", "−7")]),
     S("Mixed practice", [imul(-8, 7), idiv(-96, -12), fmul(H(-5, 6), H(9, 10)), fdiv(H(-7, 4), H(7, 2)), dmul("-0.4", "-2.75"), Problem("−3 + (−2)³", "−11")]),
     S("Solve", [Problem("A stock's price changes −$0.85 per day for 6 days, then +$1.20 per day for 4 days. Net change? Average per day?", "−$0.30 net; −$0.03 per day", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain how you decide the sign of a product of five numbers.", "Count negatives; odd → negative.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students solve mixed rational-number problems.", "7.NS review.", "Workbook Lesson 5.16, Unit 5 Review", flow("Warm-up.", "Read Let's Explore.", ["Work backward example."], "Try It 1–3.", "Workbook Lesson 5.16 and the Unit 5 Review.", "Check. Tomorrow: Unit 5 Test."),
       ["Sign errors."], ["Sign first."], ["Design your own challenge."]),
    summary="Plan totals with multiplication, find averages with division, and track signs.")

C1 = Check("Weekly Check 13: Multiplying and Dividing Integers", [S("Show what you know", [imul(-7, 8), imul(-6, -9), Problem("(−2)(−3)(−4)", "−24"), idiv(-63, 7), idiv(-48, -6), Problem(f"Simplify {F(14, '−21')}", f"−{F(2, 3)}")])], minutes=15)
C2 = Check("Weekly Check 14: Rational Products and Quotients", [S("Show what you know", [fmul(H(-3, 8), H(4, 9)), fmul(H(-5, 2), H(-6, 5)), fdiv(H(-4, 5), H(2, 15)), fdiv(H(7, 3), H(-14, 9)), dmul("-1.6", "0.5"), ddiv("-2.7", "-0.09")])], minutes=20)
C3 = Check("Weekly Check 15: Operations and Models", [S("Show what you know", [Problem("−4 + 6 × (−2)", "−16"), Problem("(−5)² − 3(−4)", "37"), Problem("−3(2x − 7)", "−6x + 21"), Problem("Rate −1.5°/hr; 4 hours ago?", "6° warmer (+6)"),
    Problem("A $45 loss over 5 days: average daily change", "−$9"), Problem("From 30 to −10 in 8 hours: rate", "−5 per hour")])], minutes=20)

REVIEW = Check("Unit 5 Review", [
    S("Compute", [imul(-12, -5), idiv(84, -7), fmul(H(-2, 3), H(-9, 14)), fdiv(H(-5, 8), H(15, 16)), dmul("3.5", "-0.6"), ddiv("-4.5", "1.5"), Problem("(−1)⁶", "1"), Problem("10 − 3(−2)²", "−2")]),
    S("Apply", [Problem("Mean of −8, 3, −5, −2", "−3"), Problem("Temp falls from 12° to −9° in 7 hours. Rate?", "−3° per hour"), Problem("−0.5(8x − 6)", "−4x + 3"),
                Problem("A pool drains 2.5 in./hour. Change after 3.5 hours?", "−8.75 in.")])], kind="review", minutes=35, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 5 Test", [
    S("Part A · Integers (1 point each)", [imul(-9, 6), imul(-11, -4), Problem("(−1)(−2)(−3)(−4)", "24"), idiv(-108, 9), idiv(-75, -15), Problem(f"Simplify {F('−16', 24)}", f"−{F(2, 3)}")]),
    S("Part B · Rational numbers (1 point each)", [fmul(H(-4, 7), H(21, 8)), fdiv(H(-3, 5), H(-9, 20)), dmul("-2.4", "1.25"), ddiv("6.4", "-0.8"), Problem("−8 + 12 ÷ (−4)", "−11"), Problem("−4(3 − 2.5)", "−2")]),
    S("Part C · Applications (2 points each)", [Problem("The temperature fell from 15°F to −9°F in 6 hours. Find the rate of change.", "−4°F per hour", space=30, points=2),
        Problem("Mean of −3.5, 2, −4.5, 1, −5", "−2", space=30, points=2), Problem("A submarine changes depth by −8.5 m per minute. Where was it, relative to now, 4 minutes ago?", "34 m higher (+34 m)", space=30, points=2)]),
    S("Part D · Explain (3 points)", [Problem("Use a pattern or the distributive property to explain why (−2)(−5) = 10.", "Pattern: 2(−5) = −10, 1(−5) = −5, 0(−5) = 0, −1(−5) = 5, −2(−5) = 10; or −2(5 + (−5)) = 0 ⇒ −10 + (−2)(−5) = 0.", lines=4, space=0, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["18–21 (85%+)", "Mastered."], ["15–17", "Proficient; correct missed items."], ["Below 15", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-02-22", "2027-03-01", "2027-03-08", "2027-03-22"], CHECKS, REVIEW, TEST)

UNIT = Unit(5, "Multiplying and Dividing Rational Numbers", "Sign rules and why they work, signed fractions and decimals, order of operations, rates, and averages.",
    "You can add and subtract any rational number. Now you will multiply and divide them, discover why the sign rules work, and use them to model repeated change, rates, and averages.",
    ["Multiply and divide integers and explain the sign rules.", "Multiply and divide signed fractions and decimals.", "Use order of operations and the distributive property with negatives.", "Model repeated change and rates with signed numbers.", "Solve multi-step problems with all four operations."],
    [("7.NS.2", "Apply and extend understandings of multiplication and division to rational numbers."), ("7.NS.3", "Solve real-world problems with the four operations on rational numbers."),
     ("7.EE.3", "Solve multi-step real-life problems with rational numbers.")],
    [("product", "Result of multiplication."), ("quotient", "Result of division."), ("reciprocal", "Number whose product with another is 1."), ("mean", "Sum ÷ count.")],
    ["Integer and rational addition/subtraction (Units 3–4).", "Fraction multiplication and division (Grade 6)."], ["Two-color counters", "Number lines", "Calculator for checking"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Weather forecasters, divers, pilots, and investors all use rates of change that can be negative.",
    family_note="Spring break (Mar 15–19) falls between Weeks 3 and 4 of this unit.",
    weeks=WEEKS)
