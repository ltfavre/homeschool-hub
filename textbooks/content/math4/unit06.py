"""Grade 4 Math · Unit 6: Fraction Operations (Feb 22 – Mar 26, 2027; spring break Mar 15–19)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import c, F, MX
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def fx(x, d=None, mixed=True):
    """Format a Fraction. d: keep this denominator (don't simplify). mixed: show as mixed number when > 1."""
    x = Fr(x)
    if d is None: d = x.denominator
    n = x * d
    assert n.denominator == 1
    n = int(n)
    if n % d == 0: return str(n // d)
    if mixed and n > d: return MX(n // d, n % d, d)
    return F(n, d)


def add_p(a, b, d):
    return Problem(f"{F(a, d)} + {F(b, d)}", fx(Fr(a + b, d), d))


def sub_p(a, b, d):
    return Problem(f"{F(a, d)} − {F(b, d)}", fx(Fr(a - b, d), d))


def mx(w, n, d):
    return Fr(w * d + n, d)


L1 = Lesson("6.1", "Decomposing Fractions",
    f"I can break a fraction into a sum of smaller fractions with the same denominator, like {F(3, 8)} = {F(1, 8)} + {F(2, 8)}.", "4.NF.3b",
    [("decompose", "To break a number into parts."), ("unit fraction", "A fraction with numerator 1.")],
    f"A pizza is cut into 8 slices. Ellie and Lillie together eat {F(5, 8)} of it. How might they have shared those slices?",
    [Text(f"{F(5, 8)} is 5 eighths. You can split 5 eighths into parts in many ways, just like you can split 5 into 2 + 3 or 1 + 4."),
     Figure(lambda t: fraction_bar(t, 5, 8, unit_labels=True)),
     Figure(lambda t: table(t, [["Ways to decompose 5/8".replace("5/8", "five-eighths")], [P(f"{F(5, 8)} = {F(1, 8)} + {F(1, 8)} + {F(1, 8)} + {F(1, 8)} + {F(1, 8)}", ParagraphStyle('x', fontName='Body', fontSize=12, leading=18))],
                                [P(f"{F(5, 8)} = {F(2, 8)} + {F(3, 8)}", ParagraphStyle('x', fontName='Body', fontSize=12, leading=18))],
                                [P(f"{F(5, 8)} = {F(1, 8)} + {F(4, 8)}", ParagraphStyle('x', fontName='Body', fontSize=12, leading=18))]], [4.6 * inch], width=4.6 * inch)),
     Example("Decompose a mixed number", f"Decompose {MX(1, 1, 4)} into fourths.", [f"1 whole = {F(4, 4)}.", f"{MX(1, 1, 4)} = {F(4, 4)} + {F(1, 4)} = {F(5, 4)}."], f"{F(1, 4)} + {F(1, 4)} + {F(1, 4)} + {F(1, 4)} + {F(1, 4)}"),
     KeyIdea("When you decompose a fraction, the denominator stays the same. The numerators add up to the original numerator.")],
    [Problem(f"Decompose {F(4, 6)} two ways.", f"e.g. {F(1, 6)} + {F(3, 6)}; {F(2, 6)} + {F(2, 6)}"), Problem(f"{F(7, 10)} = {F(3, 10)} + {F('?', 10)}", "4"),
     Problem(f"Write {F(3, 5)} as a sum of unit fractions.", f"{F(1, 5)} + {F(1, 5)} + {F(1, 5)}")],
    [S("Warm-Up", [Problem("5 = 2 + ___", "3"), Problem("Name 3 of 8 equal parts.", F(3, 8))]),
     S("Find the missing numerator", [Problem(f"{F(n, d)} = {F(a, d)} + {F('?', d)}", str(n - a)) for n, a, d in [(5, 2, 6), (7, 3, 8), (9, 4, 10), (4, 1, 5), (11, 6, 12), (11, 5, 12)]]),
     S("Decompose in two different ways", [Problem(F(n, d), "Answers vary, numerators must add to " + str(n), lines=2, space=0) for n, d in [(4, 5), (6, 8)]]),
     S("Decompose the mixed number", [Problem(f"{MX(1, 2, 3)} into thirds", f"{F(3, 3)} + {F(2, 3)} (= {F(5, 3)})", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Show {F(7, 12)} as a sum of two fractions.", "Answers vary, e.g. " + f"{F(3, 12)} + {F(4, 12)}", lines=1, space=0, wide=True)], cols=1)],
    TE("Students decompose fractions into sums with like denominators.", "Decompose a fraction into a sum of fractions with the same denominator in more than one way; justify with a model.",
       "Fraction strips, workbook Lesson 6.1",
       flow("5 = 2 + ?", "Read Let's Explore with 8 paper slices.", ["Split 5 eighths into groups several ways.", "Say: The size of the pieces stays the same; only how we group them changes."], "Try It 1–3."),
       ["Changing the denominator when decomposing (e.g., 5/8 = 2/4 + 3/4)."], ["Use strips."], ["How many ways can you decompose 6/8 into two parts?"]),
    summary="Decompose a fraction by splitting its numerator; the denominator stays the same.")

L2 = Lesson("6.2", "Adding Fractions with Like Denominators",
    "I can add fractions that have the same denominator.", "4.NF.3a, 4.NF.3d",
    [("like denominators", "Denominators that are the same.")],
    f"Ellie walked {F(2, 5)} mile to the park and {F(1, 5)} mile to the store. How far did she walk?",
    [Text(f"Fifths plus fifths makes fifths. Add the numerators: 2 fifths + 1 fifth = 3 fifths. The denominator tells the size of the pieces, so it does <b>not</b> change."),
     Figure(lambda t: frac_number_line(t, 5, 1, points=[(2, None), (3, None)])),
     Example("Add", f"{F(2, 5)} + {F(1, 5)}", ["Add the numerators: 2 + 1 = 3.", "Keep the denominator: fifths."], F(3, 5)),
     Example("Sum greater than 1", f"{F(5, 6)} + {F(4, 6)}", ["5 + 4 = 9 sixths.", f"{F(9, 6)} = {F(6, 6)} + {F(3, 6)} = {MX(1, 3, 6)}."], f"{F(9, 6)} = {MX(1, 3, 6)}"),
     WatchOut(f"Do not add the denominators! {F(1, 4)} + {F(1, 4)} is {F(2, 4)}, not {F(2, 8)}. Two quarters of a dollar are 2 fourths of a dollar, not 2 eighths."),
     KeyIdea("Add the numerators. Keep the denominator.")],
    [add_p(3, 4, 8), add_p(1, 2, 3), add_p(7, 5, 10)],
    [S("Warm-Up", [Problem(f"{F(3, 5)} = {F(1, 5)} + {F('?', 5)}", "2"), Problem("4 + 3", "7")]),
     S("Add", [add_p(a, b, d) for a, b, d in [(1, 2, 4), (2, 3, 6), (4, 3, 8), (5, 2, 9), (3, 4, 5), (7, 8, 12), (6, 4, 10), (2, 2, 3)]]),
     S("Solve", [Problem(f"Lillie poured {F(3, 8)} cup of milk and then {F(4, 8)} cup more. How much milk did she pour?", F(7, 8) + " cup", space=40, wide=True),
                 Problem(f"A board is painted {F(2, 6)} red and {F(3, 6)} blue. What fraction is painted?", F(5, 6), space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Explain why {F(2, 7)} + {F(3, 7)} is not {F(5, 14)}.", "The pieces stay sevenths; only the count changes: 5 sevenths.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students add fractions with like denominators.", "Understand addition of fractions as joining parts referring to the same whole.", "Fraction strips, workbook Lesson 6.2",
       flow("Decompose 3/5.", "Read Let's Explore.", ["Join strips: 2 fifths and 1 fifth.", "Say: Add the count, keep the size.", "Work both examples; read Watch Out."], "Try It 1–3."),
       ["Adding denominators."], ["Say it in words: “3 eighths plus 4 eighths.”"], ["Add three fractions: 1/8 + 3/8 + 5/8."]),
    summary="Add the numerators and keep the denominator. Rename sums greater than 1 as mixed numbers.")

L3 = Lesson("6.3", "Subtracting Fractions with Like Denominators",
    "I can subtract fractions that have the same denominator.", "4.NF.3a, 4.NF.3d",
    [],
    f"There was {F(7, 8)} of a pie left. The family ate {F(3, 8)} of the pie. How much pie is left now?",
    [Text("Subtracting works the same way: subtract the numerators and keep the denominator."),
     Figure(lambda t: fraction_bar(t, 7, 8, unit_labels=True)),
     Example("Subtract", f"{F(7, 8)} − {F(3, 8)}", ["7 − 3 = 4 eighths."], f"{F(4, 8)} = {F(1, 2)}"),
     Example("Subtract from 1", f"1 − {F(2, 5)}", [f"1 = {F(5, 5)}.", "5 − 2 = 3 fifths."], F(3, 5)),
     KeyIdea("Subtract the numerators. Keep the denominator. To subtract from 1, rename 1 as a fraction with the same denominator.")],
    [sub_p(5, 2, 6), sub_p(9, 4, 10), Problem(f"1 − {F(3, 4)}", F(1, 4))],
    [S("Warm-Up", [add_p(2, 3, 7), Problem("8 − 5", "3")]),
     S("Subtract", [sub_p(a, b, d) for a, b, d in [(3, 1, 4), (5, 3, 6), (7, 2, 8), (4, 4, 9), (9, 5, 10), (11, 6, 12)]]
                   + [Problem(f"1 − {F(1, 3)}", F(2, 3)), Problem(f"1 − {F(5, 8)}", F(3, 8))]),
     S("Solve", [Problem(f"A ribbon is {F(9, 10)} meter long. Ellie cuts off {F(4, 10)} meter. How much is left?", F(5, 10) + " meter", space=40, wide=True),
                 Problem(f"Lillie has 1 whole sandwich. She eats {F(3, 8)} of it. How much is left?", F(5, 8) + " of the sandwich", space=40, wide=True)], cols=1),
     S("Exit Ticket", [sub_p(11, 4, 12)], cols=1)],
    TE("Students subtract fractions with like denominators.", "Understand subtraction of fractions as separating parts of the same whole.", "Fraction strips, workbook Lesson 6.3",
       flow("2/7 + 3/7.", "Read Let's Explore.", ["Remove 3 eighth-strips from 7.", "Work both examples. Say: To take from 1, rename 1."], "Try It 1–3."),
       ["Subtracting denominators to get 0."], ["Strips."], ["What fraction plus 3/10 makes 1?"]),
    summary="Subtract numerators and keep the denominator. Rename 1 as d/d when subtracting from 1.")

L4 = Lesson("6.4", "Fraction Word Problems",
    "I can solve word problems by adding and subtracting fractions with like denominators.", "4.NF.3d",
    [],
    f"A recipe uses {F(3, 4)} cup of flour for the cookies and {F(2, 4)} cup for the frosting. How much flour is that? Is it more than 1 cup?",
    [Text("Use a bar model or number line, decide whether to add or subtract, then answer in a sentence."),
     Example("Add", "Flour for cookies and frosting.", [f"{F(3, 4)} + {F(2, 4)} = {F(5, 4)} = {MX(1, 1, 4)}."], f"{MX(1, 1, 4)} cups, more than 1 cup"),
     Example("Compare by subtracting", f"Lillie ran {F(7, 10)} mile. Ellie ran {F(4, 10)} mile. How much farther did Lillie run?", [f"{F(7, 10)} − {F(4, 10)} = {F(3, 10)}."], f"{F(3, 10)} mile farther"),
     KeyIdea("Joining → add. Taking away or “how much more” → subtract. The pieces must be the same size.")],
    [Problem(f"{F(2, 6)} of a garden is beans and {F(3, 6)} is corn. What fraction is beans and corn?", F(5, 6)),
     Problem(f"A jug had {F(7, 8)} gallon of juice. {F(5, 8)} gallon was poured out. How much is left?", F(2, 8) + " gallon"),
     Problem(f"Dad painted {F(3, 5)} of a fence. How much more to finish?", F(2, 5))],
    [S("Warm-Up", [add_p(4, 3, 6), sub_p(9, 2, 10)]),
     S("Solve. Draw a model.", [
         Problem(f"Ellie read {F(2, 8)} of her book on Monday and {F(3, 8)} on Tuesday. What fraction did she read?", F(5, 8), space=40),
         Problem(f"A cake was {F(5, 6)} left. Lillie ate {F(1, 6)}. What fraction is left?", F(4, 6), space=40),
         Problem(f"Mom bought {F(3, 4)} pound of grapes and {F(3, 4)} pound of cherries. How many pounds of fruit?", MX(1, 2, 4) + " pounds", space=40),
         Problem(f"A path is {F(9, 10)} mile. You walked {F(6, 10)} mile. How far is left?", F(3, 10) + " mile", space=40)]),
     S("Exit Ticket", [Problem(f"Write and solve a story for {F(5, 12)} + {F(4, 12)}.", F(9, 12), lines=2, space=0, wide=True)], cols=1)],
    TE("Students solve fraction word problems.", "Solve word problems involving addition and subtraction of fractions referring to the same whole and having like denominators.", "Workbook Lesson 6.4",
       flow("Two computations.", "Read Let's Explore.", ["Work both examples with bar models."], "Try It 1–3. Weekly Check tomorrow."),
       ["Choosing the wrong operation."], ["Draw the model first."], ["Write a two-step fraction story."]),
    summary="Join → add; take away or compare → subtract. Use the same whole and like denominators.")

L5 = Lesson("6.5", "Mixed Numbers and Improper Fractions",
    "I can rename mixed numbers as fractions and fractions as mixed numbers.", "4.NF.3b",
    [("mixed number", "A whole number and a fraction."), ("improper fraction", "A fraction greater than or equal to 1.")],
    f"A carpenter needs {MX(2, 3, 4)} feet of board. How many fourths of a foot is that?",
    [Text(f"Each whole is {F(4, 4)}. Two wholes are {F(8, 4)}. Add the {F(3, 4)}: {MX(2, 3, 4)} = {F(11, 4)}."),
     Figure(lambda t: fraction_bars(t, [(4, 4), (4, 4), (3, 4)], width=W * 0.55, unit_labels=True)),
     Example("Mixed number to fraction", f"Write {MX(3, 2, 5)} as a fraction.", ["3 wholes = 3 × 5 = 15 fifths.", "15 + 2 = 17 fifths."], F(17, 5)),
     Example("Fraction to mixed number", f"Write {F(23, 6)} as a mixed number.", ["How many 6s are in 23? 23 ÷ 6 = 3 R5.", "3 wholes and 5 sixths."], MX(3, 5, 6)),
     KeyIdea("Mixed → fraction: multiply the whole by the denominator, add the numerator. Fraction → mixed: divide the numerator by the denominator.")],
    [Problem(f"{MX(1, 3, 8)} = ?", F(11, 8)), Problem(f"{F(14, 3)} = ?", MX(4, 2, 3)), Problem(f"{MX(4, 1, 2)} = ?", F(9, 2))],
    [S("Warm-Up", [Problem("19 ÷ 4", "4 R3"), Problem("3 × 6 + 2", "20")]),
     S("Write as a fraction", [Problem(MX(w, n, d), F(w * d + n, d)) for w, n, d in [(1, 2, 3), (2, 1, 4), (3, 3, 5), (2, 5, 8), (4, 1, 6), (5, 2, 3)]]),
     S("Write as a mixed number", [Problem(F(n, d), MX(n // d, n % d, d)) for n, d in [(7, 4), (11, 3), (13, 5), (17, 6), (25, 8), (31, 10)]]),
     S("Exit Ticket", [Problem(f"Which is greater, {MX(2, 1, 3)} or {F(8, 3)}? Explain.", f"{F(8, 3)} = {MX(2, 2, 3)} &gt; {MX(2, 1, 3)}", lines=2, space=0, wide=True)], cols=1)],
    TE("Students convert between mixed numbers and fractions.", "Decompose and compose fractions greater than 1.", "Fraction strips, workbook Lesson 6.5",
       flow("19 ÷ 4.", "Read Let's Explore.", ["Build 2 3/4 with strips and count fourths.", "Work both examples."], "Try It 1–3."),
       ["Multiplying the numerator instead of the whole."], ["Draw wholes."], ["Write 4 7/8 as eighths in your head."]),
    summary="Mixed to fraction: whole × denominator + numerator. Fraction to mixed: divide.")

L6 = Lesson("6.6", "Adding Mixed Numbers",
    "I can add mixed numbers with like denominators.", "4.NF.3c",
    [],
    f"Ellie practiced piano {MX(1, 1, 4)} hours on Saturday and {MX(2, 2, 4)} hours on Sunday. How long did she practice?",
    [Text("Add the whole numbers. Add the fractions. If the fractions add to 1 or more, regroup."),
     Example("Add", f"{MX(1, 1, 4)} + {MX(2, 2, 4)}", ["Wholes: 1 + 2 = 3.", f"Fractions: {F(1, 4)} + {F(2, 4)} = {F(3, 4)}."], MX(3, 3, 4) + " hours"),
     Example("Regroup", f"{MX(2, 3, 5)} + {MX(1, 4, 5)}", ["Wholes: 2 + 1 = 3.", f"Fractions: {F(3, 5)} + {F(4, 5)} = {F(7, 5)} = {MX(1, 2, 5)}.", f"3 + {MX(1, 2, 5)} = {MX(4, 2, 5)}."], MX(4, 2, 5)),
     KeyIdea("Add wholes, add fractions, then regroup fractions that make a whole.")],
    [Problem(f"{MX(3, 1, 6)} + {MX(1, 4, 6)}", MX(4, 5, 6)), Problem(f"{MX(2, 5, 8)} + {MX(1, 6, 8)}", MX(4, 3, 8)), Problem(f"{MX(4, 1, 2)} + {MX(3, 1, 2)}", "8")],
    [S("Warm-Up", [Problem(f"{F(9, 8)} as a mixed number", MX(1, 1, 8)), add_p(3, 2, 5)]),
     S("Add", [Problem(f"{MX(a, b, d)} + {MX(e, g, d)}", fx(mx(a, b, d) + mx(e, g, d), d), space=30) for a, b, e, g, d in
               [(1, 1, 2, 1, 3), (2, 2, 1, 3, 6), (3, 3, 2, 4, 8), (1, 4, 1, 3, 5), (4, 7, 2, 5, 10), (5, 2, 3, 2, 4)]]),
     S("Solve", [Problem(f"A bean plant was {MX(4, 3, 8)} inches tall. It grew {MX(1, 6, 8)} inches. How tall is it now?", MX(6, 1, 8) + " inches", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"{MX(3, 5, 6)} + {MX(2, 4, 6)}", MX(6, 3, 6) + " (= " + MX(6, 1, 2) + ")", space=30, wide=True)], cols=1)],
    TE("Students add mixed numbers with like denominators.", "Add and subtract mixed numbers with like denominators.", "Fraction strips, workbook Lesson 6.6",
       flow("9/8 as a mixed number.", "Read Let's Explore.", ["Work both examples. Say: Wholes with wholes, fractions with fractions, then regroup."], "Try It 1–3."),
       ["Leaving answers like 3 7/5."], ["Strips."], ["Add three mixed numbers."]),
    summary="Add wholes and fractions separately, then regroup any extra whole.")

L7 = Lesson("6.7", "Subtracting Mixed Numbers",
    "I can subtract mixed numbers with like denominators when no regrouping is needed.", "4.NF.3c",
    [],
    f"A rope is {MX(5, 7, 8)} feet long. You cut off {MX(2, 3, 8)} feet. How much is left?",
    [Text("Subtract the fractions. Subtract the wholes."),
     Example("Subtract", f"{MX(5, 7, 8)} − {MX(2, 3, 8)}", [f"Fractions: {F(7, 8)} − {F(3, 8)} = {F(4, 8)}.", "Wholes: 5 − 2 = 3."], f"{MX(3, 4, 8)} = {MX(3, 1, 2)} feet"),
     Example("Use fractions", f"{F(15, 4)} − {F(6, 4)}", [f"{F(15, 4)} − {F(6, 4)} = {F(9, 4)}.", f"{F(9, 4)} = {MX(2, 1, 4)}."], MX(2, 1, 4)),
     KeyIdea("Subtract fractions, then wholes. You can also change both to fractions first.")],
    [Problem(f"{MX(4, 5, 6)} − {MX(1, 2, 6)}", MX(3, 3, 6)), Problem(f"{MX(7, 9, 10)} − {MX(3, 4, 10)}", MX(4, 5, 10)), Problem(f"{MX(3, 2, 3)} − 2", MX(1, 2, 3))],
    [S("Warm-Up", [sub_p(7, 4, 8), Problem("9 − 4", "5")]),
     S("Subtract", [Problem(f"{MX(a, b, d)} − {MX(e, g, d)}", fx(mx(a, b, d) - mx(e, g, d), d), space=30) for a, b, e, g, d in
                    [(3, 3, 1, 1, 4), (5, 4, 2, 1, 5), (6, 5, 3, 2, 6), (8, 7, 4, 3, 8), (4, 9, 2, 4, 10), (9, 2, 5, 1, 3)]]),
     S("Solve", [Problem(f"Lillie's backpack weighs {MX(8, 5, 6)} pounds. She takes out a {MX(2, 3, 6)}-pound book. How much does it weigh now?", MX(6, 2, 6) + " pounds", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"{MX(6, 7, 12)} − {MX(2, 5, 12)}", MX(4, 2, 12), space=30, wide=True)], cols=1)],
    TE("Students subtract mixed numbers without regrouping.", "Add and subtract mixed numbers with like denominators.", "Workbook Lesson 6.7",
       flow("7/8 − 4/8.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."), ["Subtracting fractions in the wrong order."], ["Strips."], ["Check by adding."]),
    summary="Subtract fractions, then wholes. Check by adding.")

L8 = Lesson("6.8", "Subtracting Mixed Numbers with Regrouping",
    f"I can regroup a whole to subtract mixed numbers, like {MX(3, 1, 4)} − {MX(1, 3, 4)}.", "4.NF.3c",
    [],
    f"There are {MX(3, 1, 4)} pizzas. The family eats {MX(1, 3, 4)} pizzas. How much is left? Can you take {F(3, 4)} from {F(1, 4)}?",
    [Text(f"You can't take {F(3, 4)} from {F(1, 4)}. Regroup one whole as {F(4, 4)}: {MX(3, 1, 4)} = {MX(2, 5, 4)}."),
     Example("Regroup", f"{MX(3, 1, 4)} − {MX(1, 3, 4)}", [f"Regroup: {MX(3, 1, 4)} = {MX(2, 5, 4)}.", f"Fractions: {F(5, 4)} − {F(3, 4)} = {F(2, 4)}.", "Wholes: 2 − 1 = 1."], f"{MX(1, 2, 4)} = {MX(1, 1, 2)} pizzas"),
     Example("Subtract from a whole number", f"4 − {MX(1, 2, 3)}", [f"Regroup: 4 = {MX(3, 3, 3)}.", f"{F(3, 3)} − {F(2, 3)} = {F(1, 3)}; 3 − 1 = 2."], MX(2, 1, 3)),
     KeyIdea(f"When the first fraction is too small, trade 1 whole for {F('d', 'd')} and add it to the fraction.")],
    [Problem(f"{MX(4, 1, 5)} − {MX(2, 3, 5)}", MX(1, 3, 5)), Problem(f"{MX(5, 2, 6)} − {MX(1, 5, 6)}", MX(3, 3, 6)), Problem(f"3 − {MX(1, 3, 8)}", MX(1, 5, 8))],
    [S("Warm-Up", [Problem(f"{MX(2, 1, 3)} = {MX(1, '?', 3)}", "4"), Problem(f"1 = {F('?', 6)}", "6")]),
     S("Subtract. Regroup when needed.", [Problem(f"{MX(a, b, d)} − {MX(e, g, d)}", fx(mx(a, b, d) - mx(e, g, d), d), space=36) for a, b, e, g, d in
                                          [(4, 1, 1, 2, 3), (5, 1, 2, 3, 4), (6, 2, 3, 4, 5), (3, 3, 1, 7, 8), (7, 1, 4, 5, 6), (8, 3, 2, 9, 10)]]
                                         + [Problem(f"5 − {MX(2, 1, 4)}", MX(2, 3, 4), space=36), Problem(f"2 − {F(5, 8)}", MX(1, 3, 8), space=36)]),
     S("Exit Ticket", [Problem(f"{MX(6, 2, 10)} − {MX(3, 7, 10)}", MX(2, 5, 10), space=36, wide=True)], cols=1)],
    TE("Students subtract mixed numbers with regrouping.", "Add and subtract mixed numbers with like denominators by replacing each with an equivalent fraction or using properties.", "Fraction strips, workbook Lesson 6.8",
       flow("Regroup 2 1/3.", "Read Let's Explore with paper pizzas.", ["Cut one whole into fourths to show regrouping.", "Work both examples. Alternative: change both to fractions (13/4 − 7/4)."], "Try It 1–3. Weekly Check tomorrow."),
       ["Subtracting the smaller fraction from the larger (3/4 − 1/4) instead of regrouping."], ["Change to improper fractions instead."], ["Explain two ways to solve 5 1/6 − 2 5/6."]),
    summary="If the fraction part is too small, regroup 1 whole into d/d, then subtract.")

L9 = Lesson("6.9", "Fractions as Multiples of Unit Fractions",
    f"I can write a fraction as a whole number times a unit fraction, like {F(5, 4)} = 5 × {F(1, 4)}.", "4.NF.4a",
    [],
    f"How many {F(1, 3)}-cup scoops make {F(5, 3)} cups?",
    [Text(f"{F(5, 3)} is 5 thirds: {F(1, 3)} + {F(1, 3)} + {F(1, 3)} + {F(1, 3)} + {F(1, 3)}. Repeated addition is multiplication, so {F(5, 3)} = 5 × {F(1, 3)}."),
     Figure(lambda t: frac_number_line(t, 3, 2, points=[(5, None)], label_all=True)),
     Example("Write as a multiple", f"Write {F(7, 8)} as a multiple of a unit fraction.", ["7 eighths = 7 copies of 1 eighth."], f"{F(7, 8)} = 7 × {F(1, 8)}"),
     KeyIdea(f"{F('a', 'b')} = a × {F(1, 'b')}")],
    [Problem(f"{F(4, 5)} = ___ × {F(1, 5)}", "4"), Problem(f"6 × {F(1, 10)} = ?", F(6, 10)), Problem(f"{F(9, 4)} = 9 × ?", F(1, 4))],
    [S("Warm-Up", [Problem("3 + 3 + 3 + 3 = ___ × 3", "4"), Problem(f"{F(1, 6)} + {F(1, 6)} + {F(1, 6)}", F(3, 6))]),
     S("Write as a whole number times a unit fraction", [Problem(F(n, d), f"{n} × {F(1, d)}") for n, d in [(3, 4), (5, 6), (2, 3), (7, 10), (9, 5), (11, 8)]]),
     S("Multiply", [Problem(f"{n} × {F(1, d)}", F(n, d)) for n, d in [(4, 7), (3, 12), (6, 5), (10, 3)]]),
     S("Exit Ticket", [Problem(f"Draw a number line to show {F(4, 3)} = 4 × {F(1, 3)}.", "Four jumps of 1/3 from 0 to 4/3".replace("1/3", F(1, 3)).replace("4/3", F(4, 3)), space=50, wide=True)], cols=1)],
    TE("Students express fractions as multiples of unit fractions.", "Understand a fraction a/b as a multiple of 1/b.", "Workbook Lesson 6.9, measuring cups",
       flow("Repeated addition.", "Read Let's Explore with a 1/3 cup scoop.", ["Jump by thirds on a number line.", "Say: Fractions are copies of unit fractions."], "Try It 1–3."),
       ["Multiplying the denominator by the whole number."], ["Number line jumps."], ["Write 12/4 as a multiple of 1/4 and as a whole number."]),
    summary=f"Every fraction is a number of copies of a unit fraction: {F(5, 4)} = 5 × {F(1, 4)}.")

L10 = Lesson("6.10", "Multiplying a Fraction by a Whole Number",
    f"I can multiply a whole number by a fraction, like 3 × {F(2, 5)}.", "4.NF.4b",
    [],
    f"Each batch of muffins uses {F(2, 3)} cup of oil. How much oil is needed for 4 batches?",
    [Text(f"4 × {F(2, 3)} means 4 groups of {F(2, 3)}. That is 4 × 2 thirds = 8 thirds."),
     Figure(lambda t: fraction_bars(t, [(2, 3)] * 4, width=W * 0.55, bar_h=18)),
     Example("Multiply", f"4 × {F(2, 3)}", [f"4 × {F(2, 3)} = 4 × 2 × {F(1, 3)} = 8 × {F(1, 3)}.", f"{F(8, 3)} = {MX(2, 2, 3)}."], f"{MX(2, 2, 3)} cups"),
     WatchOut("Multiply the whole number by the <b>numerator</b> only. The size of the pieces (the denominator) does not change."),
     KeyIdea(f"n × {F('a', 'b')} = {F('n × a', 'b')}")],
    [Problem(f"3 × {F(2, 5)}", F(6, 5) + " = " + MX(1, 1, 5)), Problem(f"5 × {F(3, 4)}", F(15, 4) + " = " + MX(3, 3, 4)), Problem(f"6 × {F(1, 2)}", "3")],
    [S("Warm-Up", [Problem(f"{F(7, 8)} = 7 × ___", F(1, 8)), Problem("4 × 3", "12")]),
     S("Multiply. Write as a mixed number if greater than 1.", [Problem(f"{w} × {F(n, d)}", fx(Fr(w * n, d), d)) for w, n, d in
                                                                [(2, 3, 8), (3, 2, 7), (4, 3, 5), (6, 2, 3), (5, 5, 6), (8, 3, 4), (7, 2, 10), (9, 1, 3)]]),
     S("Exit Ticket", [Problem(f"Draw a model for 3 × {F(3, 4)}. Find the product.", F(9, 4) + " = " + MX(2, 1, 4), space=50, wide=True)], cols=1)],
    TE("Students multiply a fraction by a whole number.", "Understand a multiple of a/b as a multiple of 1/b; multiply a fraction by a whole number.", "Fraction strips, workbook Lesson 6.10",
       flow("7/8 = 7 × ?", "Read Let's Explore.", ["Lay out 4 groups of 2/3 with strips and count thirds.", "Say: Multiply the count, keep the size."], "Try It 1–3."),
       ["Multiplying the denominator too."], ["Repeated addition first."], ["What is 12 × 3/4? (9)"]),
    summary="Multiply the whole number by the numerator; keep the denominator.")

L11 = Lesson("6.11", "Models for Fraction Multiplication",
    "I can use number lines and area models to multiply fractions by whole numbers.", "4.NF.4b",
    [],
    f"A frog jumps {F(3, 4)} meter each hop. Where is it after 5 hops?",
    [Text(f"Each hop is {F(3, 4)}. Five hops: 5 × {F(3, 4)} = {F(15, 4)} = {MX(3, 3, 4)} meters."),
     Figure(lambda t: frac_number_line(t, 4, 4, points=[(3 * k, None) for k in range(1, 6)], label_all=False, width=W)),
     Example("Two ways", f"6 × {F(2, 5)}", [f"Repeated addition: {F(2, 5)} + {F(2, 5)} + {F(2, 5)} + {F(2, 5)} + {F(2, 5)} + {F(2, 5)} = {F(12, 5)}.", f"Multiply: 6 × 2 = 12, so {F(12, 5)} = {MX(2, 2, 5)}."], MX(2, 2, 5)),
     KeyIdea("A number line shows equal jumps; the product is where you land.")],
    [Problem(f"4 × {F(3, 8)}", F(12, 8) + " = " + MX(1, 4, 8)), Problem(f"3 × {F(5, 6)}", F(15, 6) + " = " + MX(2, 3, 6)), Problem(f"A snail moves {F(2, 10)} meter per minute. How far in 7 minutes?", F(14, 10) + " meters")],
    [S("Warm-Up", [Problem(f"2 × {F(3, 4)}", F(6, 4)), Problem(f"{F(10, 4)} as a mixed number", MX(2, 2, 4))]),
     S("Multiply. Show a model.", [Problem(f"{w} × {F(n, d)}", fx(Fr(w * n, d), d), space=50) for w, n, d in [(3, 2, 6), (4, 2, 3), (5, 3, 10), (2, 7, 8)]]),
     S("Solve", [Problem(f"Each lap is {F(3, 8)} mile. Ellie runs 6 laps. How far does she run?", F(18, 8) + " = " + MX(2, 2, 8) + " miles", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Show 4 × {F(2, 5)} on a number line.", F(8, 5) + " = " + MX(1, 3, 5), space=50, wide=True)], cols=1)],
    TE("Students model fraction multiplication.", "Multiply a fraction by a whole number using visual models.", "Workbook Lesson 6.11",
       flow("2 × 3/4.", "Read Let's Explore.", ["Draw frog hops on a number line.", "Work the example two ways."], "Try It 1–3."), ["Counting tick marks instead of jumps."], ["Number line with labels."], ["Make your own hop story."]),
    summary="Equal jumps on a number line show multiplication: 5 hops of 3/4 lands at 15/4.".replace("3/4", F(3, 4)).replace("15/4", F(15, 4)))

L12 = Lesson("6.12", "Fraction Multiplication Word Problems",
    "I can solve word problems that multiply a fraction by a whole number.", "4.NF.4c",
    [],
    f"Each student needs {F(3, 8)} yard of ribbon for a project. There are 5 students. How much ribbon is needed? Between which two whole numbers is the answer?",
    [Example("Ribbon", f"5 × {F(3, 8)}", [f"5 × 3 = 15, so {F(15, 8)}.", f"{F(15, 8)} = {MX(1, 7, 8)}: between 1 and 2 yards."], f"{MX(1, 7, 8)} yards"),
     Example("Recipe", f"A recipe uses {F(2, 3)} cup of sugar. Mom triples the recipe. How much sugar?", [f"3 × {F(2, 3)} = {F(6, 3)} = 2."], "2 cups"),
     KeyIdea("Equal groups of a fraction → multiply. Then think: between which whole numbers does the answer lie?")],
    [Problem(f"A plant grows {F(3, 4)} inch a week. How much in 6 weeks?", F(18, 4) + " = " + MX(4, 2, 4) + " inches"), Problem(f"8 friends each eat {F(1, 4)} pizza. How much pizza?", "2 pizzas"),
     Problem(f"A bottle holds {F(5, 6)} liter. How much do 4 bottles hold?", F(20, 6) + " = " + MX(3, 2, 6) + " liters")],
    [S("Warm-Up", [Problem(f"3 × {F(3, 5)}", F(9, 5)), Problem(f"{F(9, 5)} as a mixed number", MX(1, 4, 5))]),
     S("Solve", [
         Problem(f"Ellie walks {F(5, 8)} mile each day. How far does she walk in 4 days?", F(20, 8) + " = " + MX(2, 4, 8) + " miles", space=40, wide=True),
         Problem(f"A dog eats {F(2, 3)} can of food a day. How many cans in a week?", F(14, 3) + " = " + MX(4, 2, 3) + " cans", space=40, wide=True),
         Problem(f"Lillie fills 9 cups with {F(3, 4)} cup of juice each. How much juice? Between which two whole numbers?", F(27, 4) + " = " + MX(6, 3, 4) + " cups; between 6 and 7", space=40, wide=True),
         Problem(f"A board is cut into 6 pieces, each {F(5, 12)} foot. How long was the board (no waste)?", F(30, 12) + " = " + MX(2, 6, 12) + " feet", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Write a word problem for 7 × {F(2, 5)}. Solve it.", F(14, 5) + " = " + MX(2, 4, 5), lines=2, space=0, wide=True)], cols=1)],
    TE("Students solve word problems multiplying fractions by whole numbers.", "Solve word problems involving multiplication of a fraction by a whole number.", "Workbook Lesson 6.12",
       flow("3 × 3/5.", "Read Let's Explore.", ["Work both examples. Ask: Between which whole numbers is the answer?"], "Try It 1–3. Weekly Check tomorrow."), ["Adding instead of multiplying."], ["Draw equal groups."], ["Double a real recipe."]),
    summary="Equal groups of a fraction mean multiply. Name the whole numbers the answer falls between.")

L13 = Lesson("6.13", "Fractions and Measurement",
    "I can measure lengths to the nearest half, fourth, and eighth inch and add or subtract the measurements.", "4.MD.2, 4.NF.3d",
    [("inch ruler", f"A ruler where each inch is split into halves, fourths, and eighths.")],
    "How long is your pencil? Can you measure it more exactly than “about 6 inches”?",
    [Text(f"An inch ruler splits each inch into halves, fourths, and eighths. The longest marks between inches are halves, then fourths, then eighths."),
     Figure(lambda t: frac_number_line(t, 8, 3, points=[(13, "pencil end")], label_all=False, width=W)),
     Text(f"The pencil ends at 13 eighths of an inch past 0: {F(13, 8)} = {MX(1, 5, 8)} inches."),
     Example("Add measurements", f"Two sticks are {MX(2, 3, 8)} in. and {MX(1, 7, 8)} in. Laid end to end, how long are they?", [f"{MX(2, 3, 8)} + {MX(1, 7, 8)} = {MX(3, 10, 8)} = {MX(4, 2, 8)}."], f"{MX(4, 2, 8)} = {MX(4, 1, 4)} inches"),
     KeyIdea(f"Read a ruler like a number line: count the wholes, then count the small parts.")],
    [Problem(f"How many eighths are in {F(1, 2)} inch?", "4"), Problem(f"{MX(3, 1, 4)} in. − {MX(1, 3, 4)} in.", MX(1, 2, 4) + " in."), Problem(f"Which is longer: {F(5, 8)} in. or {F(3, 4)} in.?", F(3, 4) + " in.")],
    [S("Warm-Up", [Problem(f"{F(1, 4)} = {F('?', 8)}", "2"), Problem(f"{F(6, 8)} = {F('?', 4)}", "3")]),
     S("Measure", [Problem("Use a ruler to measure your pencil to the nearest eighth inch.", "Answers vary", space=20),
                   Problem("Measure your thumb to the nearest fourth inch.", "Answers vary", space=20),
                   Problem("Measure a crayon to the nearest half inch.", "Answers vary", space=20),
                   Problem("Measure the width of this workbook to the nearest inch.", "about 8 1/2 in. (8.5 in.)".replace("8 1/2", MX(8, 1, 2)), space=20)]),
     S("Add or subtract the measurements", [Problem(f"{MX(1, 3, 4)} in. + {MX(2, 2, 4)} in.", MX(4, 1, 4) + " in."), Problem(f"{MX(5, 5, 8)} in. − {MX(2, 7, 8)} in.", MX(2, 6, 8) + " in.")]),
     S("Exit Ticket", [Problem(f"A ribbon is {MX(4, 1, 8)} in. long. Ellie cuts off {MX(1, 5, 8)} in. How much is left?", MX(2, 4, 8) + " in. = " + MX(2, 1, 2) + " in.", space=30, wide=True)], cols=1)],
    TE("Students measure to fractional inches and compute with measurements.", "Use the four operations to solve word problems involving distances and measurement with fractions.", "Inch rulers, small objects, workbook Lesson 6.13",
       flow("Equivalent fractions on a ruler.", "Read Let's Explore.", ["Find halves, fourths, eighths on a real ruler.", "Measure three objects together.", "Work the example."], "Try It 1–3."),
       ["Starting measurement at 1 instead of 0."], ["Color-code ruler marks."], ["Measure 5 objects and order them."]),
    summary="A ruler is a number line in inches split into halves, fourths, and eighths.")

L14 = Lesson("6.14", "Multi-Step Fraction Problems",
    "I can solve multi-step word problems with fractions.", "4.NF.3d, 4.NF.4c",
    [],
    f"Lillie needs 3 pieces of ribbon, each {F(3, 4)} foot long. She has a ribbon that is 3 feet long. How much will be left?",
    [Example("Multiply, then subtract", "Ribbon problem.", [f"Needed: 3 × {F(3, 4)} = {F(9, 4)} = {MX(2, 1, 4)} feet.", f"Left: 3 − {MX(2, 1, 4)} = {F(3, 4)} foot."], f"{F(3, 4)} foot"),
     Example("Add, then compare", f"Ellie ran {F(5, 8)} mile and walked {F(6, 8)} mile. Lillie ran {MX(1, 2, 8)} miles. Who went farther?", [f"Ellie: {F(5, 8)} + {F(6, 8)} = {F(11, 8)} = {MX(1, 3, 8)}.", f"{MX(1, 3, 8)} &gt; {MX(1, 2, 8)}."], "Ellie went farther."),
     KeyIdea("Find the hidden first step. Write each step as an equation.")],
    [Problem(f"A pitcher holds 2 quarts. Mom pours 4 cups of {F(1, 4)} quart each. How much is left in the pitcher?", "1 quart"),
     Problem(f"Dad hiked {MX(2, 3, 10)} miles in the morning and {MX(1, 9, 10)} in the afternoon. How far in all?", MX(4, 2, 10) + " miles"),
     Problem(f"6 kids each eat {F(2, 8)} of a pie. Is 1 pie enough?", f"No; they need {F(12, 8)} = {MX(1, 4, 8)} pies.")],
    [S("Warm-Up", [Problem(f"4 × {F(3, 5)}", F(12, 5)), Problem(f"3 − {MX(1, 2, 5)}", MX(1, 3, 5))]),
     S("Solve", [
         Problem(f"A baker uses {F(3, 4)} cup of butter in each of 3 cakes. She had 4 cups. How much is left?", MX(1, 3, 4) + " cups", space=50, wide=True),
         Problem(f"Ellie read {MX(1, 1, 4)} hours on Saturday and {MX(2, 2, 4)} on Sunday. Lillie read 4 hours. Who read more, and by how much?", f"Lillie, by {F(1, 4)} hour", space=50, wide=True),
         Problem(f"A garden row is 10 feet. Each pepper plant needs {MX(1, 1, 2)} feet. Can 6 plants fit? Explain.", f"Yes; 6 × {MX(1, 1, 2)} = 9 feet ≤ 10.", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Write a two-step fraction problem. Solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve multi-step fraction problems.", "Solve word problems with fraction addition, subtraction, and multiplication by whole numbers.", "Workbook Lesson 6.14",
       flow("4 × 3/5.", "Read Let's Explore.", ["Work both examples. Write an equation per step."], "Try It 1–3."), ["Stopping after the first step."], ["Underline each question."], ["Plan a recipe for 12 from a recipe for 4."]),
    summary="Find the hidden first step, write an equation for each step, and check if the answer makes sense.")

L15 = Lesson("6.15", "Estimating with Fractions",
    "I can estimate sums, differences, and products with fractions using benchmarks.", "4.NF.3d, 4.NF.4c",
    [],
    f"About how much is {MX(2, 7, 8)} + {MX(3, 1, 10)}? Do you need an exact answer to know it's about 6?",
    [Text(f"Round each fraction or mixed number to the nearest whole or half. {MX(2, 7, 8)} is about 3. {MX(3, 1, 10)} is about 3. So the sum is about 6."),
     Example("Estimate a product", f"About how much is 4 × {F(7, 8)}?", [f"{F(7, 8)} is close to 1.", "4 × 1 = 4, a little less."], "a little less than 4"),
     KeyIdea(f"Round fractions to 0, {F(1, 2)}, or 1 (and mixed numbers to the nearest whole or half) to estimate.")],
    [Problem(f"Estimate {MX(5, 1, 6)} − {MX(1, 5, 6)}", "about 5 − 2 = 3"), Problem(f"Estimate 6 × {F(4, 9)}", f"about 6 × {F(1, 2)} = 3"), Problem(f"Is {MX(1, 3, 8)} + {MX(2, 1, 8)} more or less than 4?", "less (exact 3 4/8)".replace("3 4/8", MX(3, 4, 8)))],
    [S("Warm-Up", [Problem(f"Is {F(5, 6)} closer to {F(1, 2)} or 1?", "1"), Problem(f"Is {F(1, 8)} closer to 0 or {F(1, 2)}?", "0")]),
     S("Estimate", [Problem(f"{MX(3, 4, 5)} + {MX(2, 1, 5)}", "about 4 + 2 = 6"), Problem(f"{MX(6, 1, 10)} − {MX(2, 9, 10)}", "about 6 − 3 = 3"),
                    Problem(f"8 × {F(5, 12)}", f"about 8 × {F(1, 2)} = 4"), Problem(f"{F(11, 12)} + {F(1, 12)} + {F(5, 6)}", "about 1 + 0 + 1 = 2 (exact 1 5/6)".replace("1 5/6", MX(1, 5, 6)))]),
     S("Reasonable?", [Problem(f"Sam says {MX(2, 1, 4)} + {MX(1, 3, 4)} = {MX(3, 4, 8)}. Use an estimate to decide if he is right.", f"No; about 2 + 2 = 4. Exact: 4.", lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Estimate 5 × {MX(1, 7, 8)}.", "about 5 × 2 = 10", wide=True)], cols=1)],
    TE("Students estimate with fractions and mixed numbers.", "Use benchmark fractions and estimation to assess reasonableness.", "Workbook Lesson 6.15",
       flow("Closer to 0, 1/2, or 1?", "Read Let's Explore.", ["Work the examples. Say: Round, compute, then check the exact answer."], "Try It 1–3."), ["Rounding the numerator only."], ["Number line from 0 to 1."], ["Estimate the total length of 3 objects."]),
    summary="Round to 0, 1/2, or 1 (or to the nearest whole) to estimate and to check answers.".replace("1/2", F(1, 2)))

L16 = Lesson("6.16", "Fraction Operations Problem Solving",
    "I can choose the right operation and solve fraction problems from start to finish.", "4.NF.3, 4.NF.4",
    [],
    "Plan a fruit salad: it needs fractions of cups of different fruits for a group. How much fruit do you need?",
    [Text("This lesson pulls together adding, subtracting, and multiplying fractions."),
     Example("Fruit salad", f"Each serving: {F(3, 4)} cup grapes and {F(2, 4)} cup berries. Make 4 servings. How much fruit?", [f"One serving: {F(3, 4)} + {F(2, 4)} = {F(5, 4)}.", f"Four servings: 4 × {F(5, 4)} = {F(20, 4)} = 5."], "5 cups"),
     KeyIdea("Read, plan, solve, check.")],
    [Problem(f"4 × {F(3, 4)} + 4 × {F(2, 4)}", "5"), Problem(f"{MX(3, 1, 3)} − {MX(1, 2, 3)}", MX(1, 2, 3)), Problem(f"{F(5, 6)} + {F(5, 6)} + {F(5, 6)}", MX(2, 3, 6))],
    [S("Warm-Up", [Problem(f"{MX(1, 3, 5)} + {MX(2, 4, 5)}", MX(4, 2, 5)), Problem(f"3 × {F(4, 5)}", MX(2, 2, 5))]),
     S("Mixed practice", [add_p(5, 6, 8), sub_p(11, 7, 12), Problem(f"{MX(4, 2, 6)} − {MX(1, 5, 6)}", MX(2, 3, 6)), Problem(f"6 × {F(3, 10)}", MX(1, 8, 10)),
                          Problem(f"Write {F(19, 4)} as a mixed number.", MX(4, 3, 4)), Problem(f"Decompose {F(5, 6)} two ways.", "Answers vary", lines=1, space=0)]),
     S("Solve", [Problem(f"A class makes 6 posters. Each poster uses {F(2, 3)} yard of paper. The roll has 5 yards. How much paper is left?", "1 yard", space=60, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which fraction operation was hardest for you? Make up and solve one problem of that type.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students apply fraction operations in problem solving.", "4.NF.3 and 4.NF.4 review.", "Workbook Lesson 6.16, Unit 6 Review",
       flow("Two warm-ups.", "Read Let's Explore.", ["Work the example."], "Try It 1–3.", "Workbook Lesson 6.16 and the Unit 6 Review.", "Check. Tomorrow: Unit 6 Test."), ["Mixing up operations."], ["Bar models."], ["Make a real fruit salad!"]),
    summary="Add and subtract like fractions, regroup mixed numbers, and multiply fractions by whole numbers to solve problems.")

C1 = Check("Weekly Check 12: Adding and Subtracting Fractions", [S("Show what you know", [add_p(3, 4, 9), sub_p(7, 3, 10), Problem(f"1 − {F(3, 8)}", F(5, 8)), add_p(5, 4, 6),
    Problem(f"Decompose {F(4, 5)} as a sum of two fractions.", "Answers vary"), Problem(f"Mom had {F(7, 8)} yard of fabric and used {F(4, 8)}. How much is left?", F(3, 8) + " yard", space=30)])], minutes=15)
C2 = Check("Weekly Check 13: Mixed Numbers", [S("Show what you know", [Problem(f"Write {MX(3, 2, 5)} as a fraction.", F(17, 5)), Problem(f"Write {F(22, 4)} as a mixed number.", MX(5, 2, 4)),
    Problem(f"{MX(2, 3, 8)} + {MX(1, 7, 8)}", MX(4, 2, 8)), Problem(f"{MX(5, 4, 6)} − {MX(2, 1, 6)}", MX(3, 3, 6)), Problem(f"{MX(4, 1, 3)} − {MX(1, 2, 3)}", MX(2, 2, 3)), Problem(f"3 − {MX(1, 3, 4)}", MX(1, 1, 4))])], minutes=15)
C3 = Check("Weekly Check 14: Multiplying Fractions", [S("Show what you know", [Problem(f"{F(7, 9)} = ___ × {F(1, 9)}", "7"), Problem(f"3 × {F(2, 7)}", F(6, 7)), Problem(f"5 × {F(3, 4)}", MX(3, 3, 4)),
    Problem(f"8 × {F(1, 2)}", "4"), Problem(f"A cat eats {F(1, 3)} can of food a day. How much in 5 days?", MX(1, 2, 3) + " cans", space=30), Problem(f"Between which two whole numbers is 7 × {F(3, 5)}?", f"4 and 5 ({MX(4, 1, 5)})")])], minutes=15)

REVIEW = Check("Unit 6 Review", [
    S("Add and subtract", [add_p(4, 5, 7), sub_p(9, 6, 10), Problem(f"{MX(3, 5, 8)} + {MX(2, 6, 8)}", MX(6, 3, 8)), Problem(f"{MX(6, 1, 4)} − {MX(2, 3, 4)}", MX(3, 2, 4))]),
    S("Multiply", [Problem(f"4 × {F(5, 6)}", MX(3, 2, 6)), Problem(f"{F(9, 10)} = 9 × ___", F(1, 10))]),
    S("Solve", [Problem(f"Lillie runs {F(3, 4)} mile each day for 5 days. Ellie runs {MX(3, 1, 4)} miles in all. Who runs farther, and by how much?", f"Lillie, by {F(2, 4)} mile ({MX(3, 3, 4)} vs {MX(3, 1, 4)})", space=60, wide=True),
                Problem(f"A board is {MX(6, 2, 8)} feet. Dad cuts off {MX(2, 5, 8)} feet. How much is left?", MX(3, 5, 8) + " feet", space=40, wide=True)], cols=1)],
    kind="review", minutes=35, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 6 Test", [
    S("Part A · Add and subtract (1 point each)", [add_p(2, 5, 8), sub_p(11, 4, 12), Problem(f"1 − {F(2, 9)}", F(7, 9)), add_p(4, 4, 5),
        Problem(f"Decompose {F(5, 8)} in two different ways.", "Answers vary", lines=1, space=0)]),
    S("Part B · Mixed numbers (1 point each)", [Problem(f"Write {MX(4, 3, 4)} as a fraction.", F(19, 4)), Problem(f"Write {F(17, 3)} as a mixed number.", MX(5, 2, 3)),
        Problem(f"{MX(2, 4, 6)} + {MX(3, 5, 6)}", MX(6, 3, 6)), Problem(f"{MX(7, 2, 5)} − {MX(3, 4, 5)}", MX(3, 3, 5)), Problem(f"4 − {MX(2, 1, 3)}", MX(1, 2, 3))]),
    S("Part C · Multiply (1 point each)", [Problem(f"{F(8, 3)} = 8 × ___", F(1, 3)), Problem(f"6 × {F(2, 5)}", MX(2, 2, 5)), Problem(f"9 × {F(2, 3)}", "6"), Problem(f"Between which two whole numbers is 5 × {F(5, 6)}?", f"4 and 5 ({MX(4, 1, 6)})")]),
    S("Part D · Problem solving (3 points each)", [
        Problem(f"Ellie needs 4 pieces of string, each {F(5, 8)} yard. She has 3 yards. How much will be left?", F(4, 8) + " yard (= " + F(1, 2) + ")", space=70, wide=True, points=3),
        Problem(f"Lillie hiked {MX(2, 3, 4)} miles Saturday and {MX(1, 3, 4)} miles Sunday. Her goal was 5 miles. Did she reach it? Explain.", f"No; {MX(4, 2, 4)} miles, {F(2, 4)} mile short.", space=70, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["17–20 (85%+)", "Mastered."], ["14–16", "Proficient; correct missed items."], ["Below 14", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-02-22", "2027-03-01", "2027-03-08", "2027-03-22"], CHECKS, REVIEW, TEST)

UNIT = Unit(6, "Fraction Operations", "Adding and subtracting fractions and mixed numbers, and multiplying fractions by whole numbers.",
    "Now that you can compare fractions, you will compute with them. You will add and subtract fractions and mixed numbers with like denominators, regroup wholes, multiply fractions by whole numbers, and solve real problems with measurements and recipes.",
    ["Decompose fractions in more than one way.", "Add and subtract fractions with like denominators.", "Add and subtract mixed numbers, regrouping when needed.",
     "Multiply a fraction by a whole number.", "Solve multi-step word problems with fractions and measurements."],
    [("4.NF.3", "Understand a fraction a/b with a > 1 as a sum of fractions 1/b; add and subtract fractions and mixed numbers with like denominators; solve word problems."),
     ("4.NF.4", "Apply and extend previous understandings of multiplication to multiply a fraction by a whole number."),
     ("4.MD.2", "Solve word problems involving distances and measurements with fractions.")],
    [("decompose", "Break a number into parts."), ("mixed number", "A whole number and a fraction."), ("improper fraction", "A fraction ≥ 1."), ("like denominators", "Same denominators.")],
    ["Equivalent fractions and comparing (Unit 5).", "Multiplication (Unit 2)."], ["Fraction strips", "Inch rulers (marked to eighths)", "Measuring cups", "Paper ‘pizzas’"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Cooks add fractions of cups, carpenters subtract fractions of inches, and runners add fractions of miles. Doubling a recipe is multiplying fractions by whole numbers.",
    family_note="Spring break falls between Weeks 3 and 4 of this unit (Mar 15–19). Cooking together is the best fraction practice there is.",
    weeks=WEEKS)
