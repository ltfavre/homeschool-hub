"""Grade 4 Math · Unit 5: Fraction Equivalence and Comparison (Jan 25 – Feb 19, 2027)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import c, F, MX
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def fcmp(a, b, c_, d):
    x, y = Fr(a, b), Fr(c_, d)
    return ">" if x > y else "<" if x < y else "="


def simp(n, d):
    f = Fr(n, d); return F(f.numerator, f.denominator)


def bar(n, d, w=CW, unit=False):
    return lambda t: fraction_bar(t, n, d, width=w, unit_labels=unit)


def bars(fr, w=W * 0.7, unit=True):
    return lambda t: fraction_bars(t, fr, width=w, unit_labels=unit)


L1 = Lesson("5.1", "Fractions and Unit Fractions",
    f"I can name a fraction as a number of equal parts of a whole, like {F(3, 4)} is 3 of 4 equal parts.",
    "4.NF.1 (review of 3.NF.1)",
    [("fraction", "A number that names part of a whole or part of a set."), ("numerator", "The top number: how many parts we are counting."),
     ("denominator", "The bottom number: how many equal parts make one whole."), ("unit fraction", f"A fraction with a numerator of 1, like {F(1, 5)}.")],
    "A pan of cornbread is cut into 8 equal pieces. You eat 3. What fraction of the pan did you eat?",
    [Text(f"A <b>fraction</b> names equal parts of a whole. The <b>denominator</b> tells how many equal parts the whole is cut into. The <b>numerator</b> tells how many parts we are counting."),
     Figure(lambda t: fraction_bar(t, 3, 8, unit_labels=True), f"3 of 8 equal parts: {F(3, 8)}"),
     Text(f"Each piece is {F(1, 8)} of the pan. {F(1, 8)} is a <b>unit fraction</b>. Three pieces are 3 copies of {F(1, 8)}, so you ate {F(3, 8)}."),
     Example("Name a fraction", "What fraction of the circle is shaded?", ["The circle has 5 equal parts, so the denominator is 5.", "2 parts are shaded, so the numerator is 2."], F(2, 5),
             fig=lambda t: fraction_circle(t, 2, 5)),
     WatchOut("The parts must be <b>equal</b>. A shape cut into 4 unequal pieces does not show fourths."),
     KeyIdea(f"A fraction {F('a', 'b')} means a copies of the unit fraction {F(1, 'b')}.")],
    [Problem("What fraction of a pizza is 1 slice if the pizza has 6 equal slices?", F(1, 6)), Problem(f"How many {F(1, 10)}s make {F(7, 10)}?", "7"),
     Problem("A bar is cut into 4 equal parts with 3 shaded. Name the fraction.", F(3, 4))],
    [S("Warm-Up", [Problem("12 ÷ 4", "3"), Problem("Which is a fraction: 3 or one-half?", "one-half")]),
     S("Write the fraction that is shaded", [Problem("", F(n, d), fig=bar(n, d), space=0) for n, d in [(1, 3), (5, 6), (2, 8), (7, 10)]]),
     S("Write the fraction", [Problem("4 of 5 equal parts", F(4, 5)), Problem("1 of 12 equal parts", F(1, 12)), Problem(f"6 copies of {F(1, 8)}", F(6, 8)), Problem(f"3 copies of {F(1, 4)}", F(3, 4))]),
     S("Exit Ticket", [Problem(f"Draw a bar and shade {F(2, 3)}. Label the unit fractions.", f"Bar in 3 equal parts, 2 shaded, each labeled {F(1, 3)}", space=50, wide=True)], cols=1)],
    TE("Students name fractions as counts of unit fractions.", "Review of fraction meaning; build toward 4.NF.1 equivalence.",
       "Paper strips, crayons, workbook Lesson 5.1",
       flow("12 ÷ 4.", "Read Let's Explore. Fold a strip into 8 equal parts and shade 3.", ["Say: The bottom number is how many equal parts; the top is how many we count.", "Work the example. Discuss the Watch Out with an unequal drawing."], "Try It 1–3."),
       ["Counting all the parts as the numerator.", "Accepting unequal parts."], ["Fold paper strips."], ["Is the same fraction always the same amount of pizza? (preview of Lesson 5.14)"]),
    summary="A fraction counts equal parts. The denominator names the size of the parts; the numerator counts them.")

L2 = Lesson("5.2", "Fractions on a Number Line",
    "I can place fractions on a number line.", "4.NF.1",
    [("number line (fractions)", "A line where the distance from 0 to 1 is split into equal parts.")],
    f"Where would {F(3, 4)} be on a number line from 0 to 1?",
    [Text(f"On a number line, the whole is the distance from 0 to 1. Split it into equal parts, and count parts from 0. To show {F(3, 4)}, split 0 to 1 into 4 equal parts and count 3."),
     Figure(lambda t: frac_number_line(t, 4, 1, points=[(3, None)])),
     Example("Name the point", "What fraction is at point P?", ["0 to 1 is split into 6 equal parts.", "P is 5 parts from 0."], F(5, 6),
             fig=lambda t: frac_number_line(t, 6, 1, points=[(5, "P")], label_all=False)),
     KeyIdea("Count the spaces between marks, not the marks, to find the denominator.")],
    [Problem("A line from 0 to 1 is split into 3 equal parts. What fraction is at the first mark after 0?", F(1, 3)),
     Problem("On a line split into 8 parts, how many parts from 0 is 5/8?".replace("5/8", F(5, 8)), "5"), Problem("What fraction is halfway between 0 and 1?", F(1, 2))],
    [S("Warm-Up", [Problem(f"How many {F(1, 5)}s in {F(4, 5)}?", "4"), Problem("Count by 2s to 12.", "2, 4, 6, 8, 10, 12")]),
     S("Name each point", [Problem("Point A", F(2, 3), fig=lambda t: frac_number_line(t, 3, 1, points=[(2, "A")], label_all=False, width=CW), space=0),
                           Problem("Point B", F(1, 4), fig=lambda t: frac_number_line(t, 4, 1, points=[(1, "B")], label_all=False, width=CW), space=0),
                           Problem("Point C", F(7, 8), fig=lambda t: frac_number_line(t, 8, 1, points=[(7, "C")], label_all=False, width=CW), space=0),
                           Problem("Point D", F(3, 5), fig=lambda t: frac_number_line(t, 5, 1, points=[(3, "D")], label_all=False, width=CW), space=0)]),
     S("Draw", [Problem(f"Draw a number line from 0 to 1. Mark {F(1, 6)}, {F(3, 6)}, and {F(5, 6)}.", "Line with 6 equal parts; points at 1st, 3rd, 5th marks", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Explain how to find {F(2, 5)} on a number line.", "Split 0–1 into 5 equal parts; count 2 parts from 0.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students locate fractions on a number line.", "Understand a fraction as a number on the number line.", "Ruler, workbook Lesson 5.2",
       flow(f"How many {F(1, 5)}s in {F(4, 5)}?", "Read Let's Explore.", ["Draw 0 to 1 and split into 4 equal parts with a ruler.", "Say: Count spaces, not marks.", "Work the example."], "Try It 1–3."),
       ["Counting tick marks (including 0) instead of spaces."], ["Use a paper strip laid along the line."], [f"Place {F(5, 4)} on a number line from 0 to 2."]),
    summary="Split 0 to 1 into equal parts (the denominator) and count parts from 0 (the numerator).")

L3 = Lesson("5.3", "Fractions Equal to and Greater Than 1",
    f"I can show fractions equal to 1 and greater than 1, like {F(4, 4)} and {F(5, 4)}.", "4.NF.1",
    [("improper fraction", f"A fraction with a numerator equal to or greater than its denominator, like {F(7, 4)}."),
     ("mixed number", f"A whole number and a fraction together, like {MX(1, 3, 4)}.")],
    f"Mom cut 2 pies into fourths. The family ate 5 pieces. Is that more or less than one whole pie?",
    [Text(f"When the numerator equals the denominator, the fraction equals 1 whole: {F(4, 4)} = 1. When the numerator is bigger, the fraction is greater than 1."),
     Figure(lambda t: fraction_bars(t, [(4, 4), (1, 4)], width=W * 0.6, unit_labels=True), f"{F(5, 4)} = 1 whole and {F(1, 4)} more = {MX(1, 1, 4)}"),
     Figure(lambda t: frac_number_line(t, 4, 2, points=[(5, None)])),
     Example("Write as a mixed number", f"Write {F(7, 3)} as a mixed number.", [f"3 thirds make 1 whole. 7 thirds = 3 + 3 + 1.", "That is 2 wholes and 1 third."], MX(2, 1, 3)),
     KeyIdea(f"Same numerator and denominator = 1 whole. To change an improper fraction to a mixed number, see how many wholes fit.")],
    [Problem(f"{F(6, 6)} = ___", "1"), Problem(f"Write {F(9, 4)} as a mixed number.", MX(2, 1, 4)), Problem(f"Write {MX(1, 2, 5)} as a fraction.", F(7, 5))],
    [S("Warm-Up", [Problem("13 ÷ 4", "3 R1"), Problem(f"Name the fraction: 3 of 3 equal parts", F(3, 3))]),
     S("Write as a mixed number", [Problem(F(n, d), MX(n // d, n % d, d)) for n, d in [(5, 3), (7, 2), (11, 4), (13, 5)]]),
     S("Write as a fraction", [Problem(MX(w, n, d), F(w * d + n, d)) for w, n, d in [(1, 1, 2), (2, 3, 4), (3, 1, 3), (1, 5, 8)]]),
     S("Exit Ticket", [Problem(f"Draw a model of {F(8, 3)}. Write it as a mixed number.", MX(2, 2, 3), space=50, wide=True)], cols=1)],
    TE("Students represent fractions equal to and greater than 1.", "Understand fractions greater than 1 and mixed numbers (foundation for 4.NF.3).", "Fraction strips, workbook Lesson 5.3",
       flow("13 ÷ 4.", "Read Let's Explore with paper ‘pies’.", ["Build 5/4 with strips: one whole and one fourth more.", "Say: How many wholes fit? What is left?", "Work the example."], "Try It 1–3."),
       ["Thinking a fraction can never be greater than 1."], ["Use strips and count wholes."], ["Which is greater, 11/4 or 3? Why?"]),
    summary=f"{F(4, 4)} = 1. Improper fractions can be written as mixed numbers by finding how many wholes fit.")

L4 = Lesson("5.4", "Fractions of a Set",
    "I can find a fraction of a group of objects.", "4.NF.4 (preview), 3.NF.1",
    [("set", "A group of objects.")],
    f"There are 12 eggs in a carton. {F(1, 3)} of them are brown. How many brown eggs are there?",
    [Text(f"A fraction can name part of a <b>set</b>. To find {F(1, 3)} of 12, split the 12 into 3 equal groups. One group is {F(1, 3)}."),
     Figure(lambda t: dot_groups(t, 3, 4, width=260), f"12 eggs in 3 equal groups: {F(1, 3)} of 12 = 4."),
     Example("More than one part", f"Find {F(2, 3)} of 12.", [f"{F(1, 3)} of 12 = 12 ÷ 3 = 4.", f"{F(2, 3)} is 2 of those groups: 2 × 4 = 8."], "8"),
     KeyIdea("To find a fraction of a set: divide by the denominator to find one part, then multiply by the numerator.")],
    [Problem(f"{F(1, 4)} of 20", "5"), Problem(f"{F(3, 5)} of 15", "9"), Problem(f"Lillie has 18 books. {F(2, 6)} are mysteries. How many mysteries?", "6")],
    [S("Warm-Up", [Problem("24 ÷ 6", "4"), Problem("3 × 7", "21")]),
     S("Find the fraction of the set", [Problem(f"{F(n, d)} of {s}", str(s // d * n)) for n, d, s in [(1, 2, 16), (1, 5, 30), (2, 3, 21), (3, 4, 24), (5, 6, 36), (4, 9, 27)]]),
     S("Solve", [Problem(f"A class of 28 students went on a trip. {F(3, 4)} of them rode the bus. How many rode the bus?", "21 students", space=40, wide=True),
                 Problem(f"Ellie picked 40 strawberries and ate {F(1, 8)} of them. How many are left?", "35 strawberries", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Draw a picture to find {F(2, 5)} of 10.", "4", space=50, wide=True)], cols=1)],
    TE("Students find fractions of sets.", "Understand fractions of a set (supports 4.NF.4).", "24 counters, workbook Lesson 5.4",
       flow("24 ÷ 6; 3 × 7.", "Read Let's Explore with 12 counters.", ["Divide counters into 3 equal groups.", "Say: Divide by the bottom, multiply by the top.", "Work the example."], "Try It 1–3."),
       ["Dividing by the numerator."], ["Use counters."], [f"If {F(3, 4)} of a number is 18, what is the number? (24)"]),
    summary="Divide by the denominator to find one part; multiply by the numerator.")

L5 = Lesson("5.5", "Equivalent Fractions with Models",
    "I can use models to show that two fractions are equivalent.", "4.NF.1",
    [("equivalent fractions", f"Fractions that name the same amount, like {F(1, 2)} and {F(2, 4)}.")],
    f"Ellie ate {F(1, 2)} of a sandwich. Lillie ate {F(2, 4)} of the same size sandwich. Who ate more?",
    [Text(f"Look at the bars. {F(1, 2)} and {F(2, 4)} cover the same length. They are <b>equivalent fractions</b>: different names for the same amount."),
     Figure(bars([(1, 2), (2, 4), (4, 8)])),
     Text(f"When you cut each part into 2 smaller parts, you get twice as many parts, and each part is half as big. The amount does not change."),
     Example("Find an equivalent fraction", f"Use a model to find a fraction equal to {F(2, 3)} with sixths.", ["Draw thirds. Cut each third in half.", "2 shaded thirds become 4 shaded sixths."], f"{F(2, 3)} = {F(4, 6)}",
             fig=bars([(2, 3), (4, 6)])),
     KeyIdea("Equivalent fractions cover the same amount of the same whole.")],
    [Problem(f"{F(1, 3)} = {F('?', 6)}", F(2, 6)), Problem(f"{F(3, 4)} = {F('?', 8)}", F(6, 8)), Problem(f"Are {F(2, 5)} and {F(4, 10)} equivalent?", "Yes")],
    [S("Warm-Up", [Problem("Shade half of a bar of 6 parts. How many parts?", "3"), Problem("2 × 4", "8")]),
     S("Write the equivalent fraction shown", [Problem("", f"{F(1, 2)} = {F(3, 6)}", fig=bars([(1, 2), (3, 6)], w=CW, unit=False), space=0),
                                               Problem("", f"{F(2, 4)} = {F(4, 8)}", fig=bars([(2, 4), (4, 8)], w=CW, unit=False), space=0),
                                               Problem("", f"{F(1, 5)} = {F(2, 10)}", fig=bars([(1, 5), (2, 10)], w=CW, unit=False), space=0),
                                               Problem("", f"{F(2, 3)} = {F(8, 12)}", fig=bars([(2, 3), (8, 12)], w=CW, unit=False), space=0)]),
     S("Draw a model to find the missing number", [Problem(f"{F(1, 4)} = {F('?', 8)}", "2"), Problem(f"{F(3, 5)} = {F('?', 10)}", "6"),
                                                    Problem(f"{F(1, 3)} = {F('?', 12)}", "4"), Problem(f"{F(5, 6)} = {F('?', 12)}", "10")]),
     S("Exit Ticket", [Problem(f"Draw models to show {F(3, 4)} = {F(6, 8)}.", "Two equal bars: 4 parts with 3 shaded; 8 parts with 6 shaded", space=50, wide=True)], cols=1)],
    TE("Students show equivalent fractions with area and bar models.", "Explain why a fraction a/b is equivalent to (n×a)/(n×b) using visual fraction models.", "Fraction strips (make from paper), workbook Lesson 5.5",
       flow("Shade half of 6 parts.", "Read Let's Explore.", ["Lay 1/2, 2/4, 4/8 strips under each other.", "Say: More pieces, smaller pieces, same amount.", "Work the example by cutting a strip."], "Try It 1–3."),
       ["Thinking bigger numbers mean a bigger fraction."], ["Fraction strips for every problem."], ["Find three fractions equivalent to 2/3."]),
    summary="Equivalent fractions name the same amount. Cutting each part into more equal parts makes an equivalent fraction.")

L6 = Lesson("5.6", "Equivalent Fractions by Multiplying",
    "I can multiply the numerator and denominator by the same number to make an equivalent fraction.", "4.NF.1",
    [],
    f"Is there a way to find a fraction equal to {F(3, 5)} with a denominator of 20 without drawing?",
    [Text(f"In the models, cutting every part into 4 pieces multiplies the number of parts by 4 <b>and</b> the number of shaded parts by 4."),
     Figure(lambda t: table(t, [[" ", "Numerator", "Denominator"], [P(F(3, 5), ParagraphStyle('x', fontName='Body', fontSize=13)), "3", "5"],
                                ["× 4", "× 4", "× 4"], [P(F(12, 20), ParagraphStyle('x', fontName='Body', fontSize=13)), "12", "20"]],
                            [1.2 * inch, 1.4 * inch, 1.4 * inch], width=4.0 * inch)),
     Example("Multiply", f"Find a fraction equal to {F(2, 3)} with denominator 12.", ["3 × 4 = 12, so multiply by 4.", "Multiply the numerator too: 2 × 4 = 8."], f"{F(2, 3)} = {F(8, 12)}"),
     WatchOut("Multiply the numerator <b>and</b> the denominator by the same number. Multiplying both by 4 is like multiplying by 4/4, which equals 1.".replace("4/4", F(4, 4))),
     KeyIdea(f"{F('a', 'b')} = {F('n × a', 'n × b')}")],
    [Problem(f"{F(1, 4)} = {F('?', 12)}", "3"), Problem(f"{F(5, 6)} = {F('?', 18)}", "15"), Problem(f"Write two fractions equivalent to {F(2, 5)}.", f"e.g. {F(4, 10)}, {F(6, 15)}")],
    [S("Warm-Up", [Problem("6 × 4", "24"), Problem(f"{F(1, 2)} = {F('?', 4)}", "2")]),
     S("Find the missing number", [Problem(f"{F(n, d)} = {F('?', d * k)}", str(n * k)) for n, d, k in [(1, 3, 2), (3, 4, 3), (2, 5, 4), (5, 8, 2), (1, 6, 5), (4, 7, 3)]]),
     S("Find the missing number", [Problem(f"{F(n, d)} = {F(n * k, '?')}", str(d * k)) for n, d, k in [(1, 2, 6), (3, 10, 10)]]),
     S("Write three equivalent fractions", [Problem(F(3, 4), f"e.g. {F(6, 8)}, {F(9, 12)}, {F(12, 16)}", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Is {F(3, 8)} = {F(9, 24)}? Explain.", "Yes. 3 × 3 = 9 and 8 × 3 = 24.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students generate equivalent fractions by multiplying.", "Explain why a/b = (n×a)/(n×b).", "Workbook Lesson 5.6",
       flow("6 × 4.", "Read Let's Explore.", ["Connect the model from 5.5 to the multiplication table.", "Say: What you do to the bottom, you do to the top."], "Try It 1–3."),
       ["Adding the same number to top and bottom."], ["Show with strips why adding fails (1/2 vs 2/3)."], ["Why is multiplying by 4/4 the same as multiplying by 1?"]),
    summary="Multiply the numerator and denominator by the same number to make an equivalent fraction.")

L7 = Lesson("5.7", "Simplest Form",
    "I can divide the numerator and denominator by a common factor to write a fraction in simplest form.", "4.NF.1",
    [("common factor", "A number that is a factor of two or more numbers."), ("simplest form", "A fraction whose numerator and denominator have no common factor except 1.")],
    f"A recipe calls for {F(6, 8)} of a cup of milk. Is there a simpler name for that amount?",
    [Text(f"You can also go the other way: <b>divide</b> the numerator and denominator by a <b>common factor</b>. 6 and 8 are both divisible by 2."),
     Example("Simplify", f"Write {F(6, 8)} in simplest form.", ["6 ÷ 2 = 3 and 8 ÷ 2 = 4.", "3 and 4 have no common factor but 1."], F(3, 4)),
     Example("Use the greatest common factor", f"Write {F(12, 18)} in simplest form.", ["Factors of 12: 1, 2, 3, 4, 6, 12. Factors of 18: 1, 2, 3, 6, 9, 18.", "The greatest common factor is 6.", "12 ÷ 6 = 2, 18 ÷ 6 = 3."], F(2, 3)),
     KeyIdea("Divide the numerator and denominator by a common factor. Keep going until 1 is the only common factor.")],
    [Problem(f"Simplify {F(4, 10)}", F(2, 5)), Problem(f"Simplify {F(9, 12)}", F(3, 4)), Problem(f"Simplify {F(8, 16)}", F(1, 2))],
    [S("Warm-Up", [Problem("Factors of 12", "1, 2, 3, 4, 6, 12"), Problem("Factors of 16", "1, 2, 4, 8, 16")]),
     S("Write in simplest form", [Problem(F(n, d), simp(n, d)) for n, d in [(2, 4), (3, 9), (5, 10), (6, 9), (8, 12), (10, 15), (14, 21), (15, 20)]]),
     S("Simplest form or not?", [Problem(f"Is {F(5, 7)} in simplest form?", "Yes", choices=["Yes", "No"]), Problem(f"Is {F(4, 6)} in simplest form?", "No (2/3)".replace("2/3", F(2, 3)), choices=["Yes", "No"])]),
     S("Exit Ticket", [Problem(f"Write {F(18, 24)} in simplest form. Show your steps.", F(3, 4), space=40, wide=True)], cols=1)],
    TE("Students write fractions in simplest form.", "Recognize and generate equivalent fractions.", "Workbook Lesson 5.7",
       flow("Factors of 12 and 16.", "Read Let's Explore.", ["Work both examples. Say: Divide top and bottom by the same factor."], "Try It 1–3."),
       ["Dividing only the numerator.", "Stopping before simplest form."], ["List factors of both numbers."], ["Simplify 36/48 in one step."]),
    summary="Divide the numerator and denominator by a common factor until only 1 is common.")

L8 = Lesson("5.8", "Equivalent Fractions on a Number Line",
    "I can show equivalent fractions at the same point on a number line.", "4.NF.1",
    [],
    f"On a ruler, the {F(1, 2)}-inch mark is the same mark as {F(2, 4)} and {F(4, 8)}. Why?",
    [Text("Equivalent fractions land on the same point of a number line, because they are the same distance from 0."),
     Figure(lambda t: frac_number_line(t, 2, 1, points=[(1, None)], height=50)),
     Figure(lambda t: frac_number_line(t, 4, 1, points=[(2, None)], height=50)),
     Figure(lambda t: frac_number_line(t, 8, 1, points=[(4, None)], height=50)),
     Example("Find the same point", f"Which eighths fraction is at the same point as {F(3, 4)}?", ["Each fourth is 2 eighths.", "3 fourths = 6 eighths."], F(6, 8)),
     KeyIdea("Equivalent fractions are the same number, so they are at the same point on a number line.")],
    [Problem(f"Which sixths fraction is at the same point as {F(1, 3)}?", F(2, 6)), Problem(f"Which tenths fraction is at the same point as {F(1, 2)}?", F(5, 10)),
     Problem(f"Is {F(2, 3)} at the same point as {F(4, 6)}?", "Yes")],
    [S("Warm-Up", [Problem(f"{F(2, 5)} = {F('?', 10)}", "4"), Problem(f"Simplify {F(6, 10)}", F(3, 5))]),
     S("Name the two equivalent fractions at the point", [Problem("", f"{F(1, 4)} = {F(2, 8)}", fig=lambda t: frac_number_line(t, 8, 1, points=[(2, None)], width=CW), space=0),
                                                         Problem("", f"{F(2, 3)} = {F(4, 6)}", fig=lambda t: frac_number_line(t, 6, 1, points=[(4, None)], width=CW), space=0)]),
     S("Draw", [Problem(f"Draw a number line from 0 to 1 in sixths. Circle the fractions equal to {F(1, 2)} and {F(1, 3)}.", f"{F(3, 6)} and {F(2, 6)}", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Explain why {F(3, 5)} and {F(6, 10)} are at the same point.", "Each fifth is 2 tenths, so 3 fifths = 6 tenths: same distance from 0.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students show equivalent fractions on number lines.", "Recognize equivalent fractions as the same point on a number line.", "Ruler, workbook Lesson 5.8",
       flow("2/5 = ?/10.", "Read Let's Explore with a ruler.", ["Draw three stacked number lines (halves, fourths, eighths) the same length.", "Say: Same point, same number."], "Try It 1–3."),
       ["Drawing number lines of different lengths."], ["Use a ruler marked in eighths."], ["Find all fractions with denominators up to 12 equal to 1/2."]),
    summary="Equivalent fractions are at the same point on a number line.")

L9 = Lesson("5.9", "Comparing: Same Denominator or Same Numerator",
    "I can compare fractions that have the same denominator or the same numerator.", "4.NF.2",
    [],
    f"Which is more, {F(3, 8)} of a pizza or {F(5, 8)} of the same pizza? Which is more, {F(3, 4)} or {F(3, 8)}?",
    [Heading("Same denominator"),
     Text(f"When the denominators are the same, the pieces are the same size. More pieces means more: {F(5, 8)} &gt; {F(3, 8)}."),
     Heading("Same numerator"),
     Text(f"When the numerators are the same, you have the same number of pieces. Compare the <b>size</b> of the pieces: fourths are bigger than eighths, so {F(3, 4)} &gt; {F(3, 8)}."),
     Figure(bars([(3, 4), (3, 8)])),
     WatchOut(f"A bigger denominator means <b>smaller</b> pieces. {F(1, 8)} is less than {F(1, 4)}, even though 8 &gt; 4."),
     KeyIdea("Same denominator: compare numerators. Same numerator: the smaller denominator is the bigger fraction.")],
    [Problem(f"{F(2, 6)} &nbsp;◯&nbsp; {F(5, 6)}", "<"), Problem(f"{F(4, 5)} &nbsp;◯&nbsp; {F(4, 10)}", ">"), Problem(f"{F(1, 3)} &nbsp;◯&nbsp; {F(1, 12)}", ">")],
    [S("Warm-Up", [Problem("Which is bigger, 1 of 3 equal pieces or 1 of 6 equal pieces of the same cake?", "1 of 3"), Problem(f"Simplify {F(4, 8)}", F(1, 2))]),
     S("Write >, <, or = in the circle", [Problem(f"{F(a, b)} &nbsp;◯&nbsp; {F(c_, d)}", fcmp(a, b, c_, d)) for a, b, c_, d in
                           [(3, 5, 4, 5), (7, 10, 3, 10), (2, 3, 2, 5), (5, 12, 5, 6), (1, 2, 1, 4), (6, 8, 6, 8), (9, 12, 7, 12), (3, 10, 3, 4)]]),
     S("Exit Ticket", [Problem(f"Explain why {F(2, 3)} &gt; {F(2, 5)}.", "Both have 2 pieces, but thirds are bigger than fifths.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare fractions with like numerators or denominators.", "Compare two fractions with different numerators and denominators; recognize comparisons are valid only for the same whole.",
       "Fraction strips, workbook Lesson 5.9",
       flow("Which piece is bigger?", "Read Let's Explore.", ["Compare with strips. Say: Same size pieces? Count them. Same number of pieces? Compare their size."], "Try It 1–3."),
       [f"Thinking {F(1, 8)} > {F(1, 4)} because 8 > 4."], ["Strips for every comparison."], ["Order 1/2, 1/3, 1/4, 1/5, 1/6."]),
    summary="Same denominator: more pieces is greater. Same numerator: bigger pieces (smaller denominator) is greater.")

L10 = Lesson("5.10", "Comparing with Benchmarks",
    f"I can compare fractions by thinking about 0, {F(1, 2)}, and 1.", "4.NF.2",
    [("benchmark fraction", f"A friendly fraction like 0, {F(1, 2)}, or 1 used to compare.")],
    f"Which is greater, {F(3, 8)} or {F(4, 6)}? They have different numerators and denominators!",
    [Text(f"Compare each fraction to {F(1, 2)}. {F(3, 8)} is less than {F(4, 8)}, which is half. {F(4, 6)} is more than {F(3, 6)}, which is half. So {F(3, 8)} &lt; {F(4, 6)}."),
     Figure(lambda t: table(t, [["Less than half", "Exactly half", "More than half"],
                                ["numerator less than half of denominator", "numerator is half of denominator", "numerator more than half of denominator"],
                                [P(f"{F(2, 5)}, {F(3, 8)}, {F(1, 4)}", ParagraphStyle('x', fontName='Body', fontSize=12, leading=16)),
                                 P(f"{F(3, 6)}, {F(5, 10)}", ParagraphStyle('x', fontName='Body', fontSize=12, leading=16)),
                                 P(f"{F(3, 5)}, {F(5, 8)}, {F(3, 4)}", ParagraphStyle('x', fontName='Body', fontSize=12, leading=16))]],
                            [2.0 * inch] * 3, width=6.0 * inch)),
     Example("Close to 1", f"Compare {F(7, 8)} and {F(9, 10)}.", [f"Both are one piece away from 1.", f"{F(7, 8)} is missing {F(1, 8)}; {F(9, 10)} is missing {F(1, 10)}.", f"{F(1, 10)} is the smaller gap, so {F(9, 10)} is closer to 1."],
             f"{F(7, 8)} &lt; {F(9, 10)}"),
     KeyIdea(f"Ask: Is each fraction less than, equal to, or more than {F(1, 2)}? Near 1, compare the missing pieces.")],
    [Problem(f"{F(2, 6)} &nbsp;◯&nbsp; {F(5, 8)}", "<"), Problem(f"{F(4, 7)} &nbsp;◯&nbsp; {F(1, 3)}", ">"), Problem(f"{F(5, 6)} &nbsp;◯&nbsp; {F(7, 8)}", "<")],
    [S("Warm-Up", [Problem("Half of 10", "5"), Problem("Half of 7", "3.5 (3 and a half)")]),
     S(f"Less than, equal to, or greater than {F(1, 2)}?", [Problem(F(n, d), "less" if Fr(n, d) < Fr(1, 2) else "equal" if Fr(n, d) == Fr(1, 2) else "greater") for n, d in [(3, 7), (5, 9), (6, 12), (2, 5), (7, 12), (4, 10)]]),
     S("Compare using benchmarks. Write >, <, or = in the circle.", [Problem(f"{F(a, b)} &nbsp;◯&nbsp; {F(c_, d)}", fcmp(a, b, c_, d)) for a, b, c_, d in [(3, 8, 2, 3), (5, 6, 2, 5), (1, 4, 4, 7), (11, 12, 9, 10)]]),
     S("Exit Ticket", [Problem(f"Compare {F(4, 9)} and {F(6, 10)}. Explain using {F(1, 2)}.", f"{F(4, 9)} &lt; {F(6, 10)}: 4/9 is less than half and 6/10 is more than half.".replace("4/9", F(4, 9)).replace("6/10", F(6, 10)), lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare fractions using benchmarks.", "Compare two fractions by comparing to a benchmark fraction such as 1/2.", "Workbook Lesson 5.10",
       flow("Half of 10, half of 7.", "Read Let's Explore.", ["Sort fractions into less than half, half, more than half.", "Work the ‘close to 1’ example."], "Try It 1–3."),
       ["Not knowing how to find half of an odd denominator."], ["Use strips folded in half."], ["Compare 13/25 and 12/23."]),
    summary="Compare each fraction to 1/2. Near 1, compare the missing pieces.".replace("1/2", F(1, 2)))

L11 = Lesson("5.11", "Comparing with Common Denominators",
    "I can compare fractions by renaming them with a common denominator.", "4.NF.2",
    [("common denominator", "A denominator that two fractions share.")],
    f"Compare {F(2, 3)} and {F(3, 4)}. Neither benchmarks nor matching numbers help much. What can we do?",
    [Text("Rename both fractions so they have the <b>same denominator</b>. Then the pieces are the same size and you can compare numerators."),
     Example("Common denominator", f"Compare {F(2, 3)} and {F(3, 4)}.", ["Multiples of 3: 3, 6, 9, 12. Multiples of 4: 4, 8, 12. Use 12.", f"{F(2, 3)} = {F(8, 12)} (× 4).", f"{F(3, 4)} = {F(9, 12)} (× 3).", "8 &lt; 9."],
             f"{F(2, 3)} &lt; {F(3, 4)}", fig=bars([(8, 12), (9, 12)])),
     Example("One denominator is a multiple of the other", f"Compare {F(3, 5)} and {F(7, 10)}.", [f"10 is a multiple of 5. {F(3, 5)} = {F(6, 10)}.", "6 &lt; 7."], f"{F(3, 5)} &lt; {F(7, 10)}"),
     KeyIdea("Find a common multiple of the denominators. Rename both fractions, then compare numerators.")],
    [Problem(f"{F(1, 2)} &nbsp;◯&nbsp; {F(3, 5)}", "<"), Problem(f"{F(5, 6)} &nbsp;◯&nbsp; {F(3, 4)}", ">"), Problem(f"{F(2, 4)} &nbsp;◯&nbsp; {F(5, 10)}", "=")],
    [S("Warm-Up", [Problem("Common multiple of 4 and 6", "12"), Problem(f"{F(1, 3)} = {F('?', 12)}", "4")]),
     S("Rename and compare", [Problem(f"{F(a, b)} &nbsp;◯&nbsp; {F(c_, d)}", fcmp(a, b, c_, d), space=36) for a, b, c_, d in
                             [(1, 3, 2, 6), (3, 4, 5, 8), (2, 5, 3, 10), (4, 6, 2, 3), (3, 8, 1, 3), (5, 12, 1, 2), (7, 10, 4, 5), (2, 3, 5, 9)]]),
     S("Exit Ticket", [Problem(f"Compare {F(5, 8)} and {F(2, 3)}. Show the common denominator.", f"{F(15, 24)} &lt; {F(16, 24)}, so {F(5, 8)} &lt; {F(2, 3)}", space=40, wide=True)], cols=1)],
    TE("Students compare fractions using common denominators.", "Compare two fractions by creating common denominators.", "Workbook Lesson 5.11",
       flow("Common multiple of 4 and 6.", "Read Let's Explore.", ["Work both examples. Say: Make the pieces the same size, then count."], "Try It 1–3."),
       ["Changing only the denominator."], ["Use the multiplication table to find common multiples."], ["Compare 5/7 and 7/9."]),
    summary="Rename both fractions with a common denominator, then compare numerators.")

L12 = Lesson("5.12", "Comparing with Common Numerators",
    "I can compare fractions by renaming them with a common numerator.", "4.NF.2",
    [("common numerator", "A numerator that two fractions share.")],
    f"Compare {F(2, 5)} and {F(4, 9)}. Is there a quick way?",
    [Text(f"Sometimes it is easier to make the <b>numerators</b> match. {F(2, 5)} = {F(4, 10)}. Now compare {F(4, 10)} and {F(4, 9)}: same number of pieces, and ninths are bigger than tenths."),
     Example("Common numerator", f"Compare {F(2, 5)} and {F(4, 9)}.", [f"{F(2, 5)} = {F(4, 10)}.", "4 tenths vs 4 ninths: ninths are bigger pieces."], f"{F(2, 5)} &lt; {F(4, 9)}"),
     KeyIdea("If the numerators are easy to match, rename to a common numerator. Then the smaller denominator is the greater fraction.")],
    [Problem(f"{F(1, 3)} &nbsp;◯&nbsp; {F(2, 7)}", ">"), Problem(f"{F(3, 4)} &nbsp;◯&nbsp; {F(6, 9)}", ">"), Problem(f"{F(2, 3)} &nbsp;◯&nbsp; {F(4, 5)}", "<")],
    [S("Warm-Up", [Problem(f"{F(3, 4)} = {F(6, '?')}", "8"), Problem(f"{F(4, 7)} &nbsp;◯&nbsp; {F(4, 9)}", ">")]),
     S("Rename to a common numerator and compare", [Problem(f"{F(a, b)} &nbsp;◯&nbsp; {F(c_, d)}", fcmp(a, b, c_, d), space=30) for a, b, c_, d in
                                                   [(1, 4, 2, 9), (2, 3, 4, 7), (3, 5, 6, 11), (1, 2, 3, 5), (2, 7, 4, 15), (3, 8, 6, 15)]]),
     S("Choose a strategy", [Problem(f"Compare {F(5, 6)} and {F(5, 8)}. Which strategy is fastest? Why?", "Same numerator: 5/6 > 5/8 because sixths are bigger.".replace("5/6", F(5, 6)).replace("5/8", F(5, 8)), lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Compare {F(3, 7)} and {F(6, 13)}.", f"{F(3, 7)} = {F(6, 14)} &lt; {F(6, 13)}", space=30, wide=True)], cols=1)],
    TE("Students compare fractions using common numerators.", "Compare two fractions by creating common numerators.", "Workbook Lesson 5.12",
       flow("3/4 = 6/?.", "Read Let's Explore.", ["Work the example.", "List all four strategies so far: same denominator, same numerator, benchmark, common denominator/numerator."], "Try It 1–3. Weekly Check tomorrow."),
       ["Forgetting that larger denominators mean smaller pieces."], ["Strips."], ["Make a strategy poster."]),
    summary="Match the numerators. With the same number of pieces, bigger pieces (smaller denominator) win.")

L13 = Lesson("5.13", "Ordering Fractions",
    "I can order three or more fractions from least to greatest.", "4.NF.2",
    [],
    f"Three friends ran {F(3, 4)} mile, {F(2, 3)} mile, and {F(5, 6)} mile. Who ran farthest? Who ran the least?",
    [Text("Ordering fractions is comparing again and again. A common denominator lets you compare all of them at once."),
     Example("Order", f"Order {F(3, 4)}, {F(2, 3)}, {F(5, 6)} from least to greatest.", ["Common denominator 12.", f"{F(3, 4)} = {F(9, 12)}, {F(2, 3)} = {F(8, 12)}, {F(5, 6)} = {F(10, 12)}.", "8 &lt; 9 &lt; 10."],
             f"{F(2, 3)}, {F(3, 4)}, {F(5, 6)}", fig=bars([(8, 12), (9, 12), (10, 12)])),
     Example("Use benchmarks", f"Order {F(1, 5)}, {F(7, 8)}, {F(1, 2)}.", [f"{F(1, 5)} is near 0, {F(1, 2)} is half, {F(7, 8)} is near 1."], f"{F(1, 5)}, {F(1, 2)}, {F(7, 8)}"),
     KeyIdea("Use the fastest strategy: benchmarks if the fractions are far apart, a common denominator if they are close.")],
    [Problem(f"Order least to greatest: {F(1, 2)}, {F(1, 3)}, {F(1, 6)}", f"{F(1, 6)}, {F(1, 3)}, {F(1, 2)}"),
     Problem(f"Order greatest to least: {F(3, 5)}, {F(7, 10)}, {F(1, 2)}", f"{F(7, 10)}, {F(3, 5)}, {F(1, 2)}"),
     Problem(f"Which is greatest: {F(5, 8)}, {F(3, 4)}, {F(2, 3)}?", F(3, 4))],
    [S("Warm-Up", [Problem(f"{F(2, 3)} &nbsp;◯&nbsp; {F(5, 8)}", ">"), Problem(f"{F(1, 2)} = {F('?', 12)}", "6")]),
     S("Order from least to greatest", [Problem(f"{F(a, b)}, {F(c_, d)}, {F(e, f)}", ", ".join(F(*p) for p in sorted([(a, b), (c_, d), (e, f)], key=lambda q: Fr(*q))), wide=True)
                                       for a, b, c_, d, e, f in [(1, 4, 3, 8, 1, 2), (2, 3, 1, 6, 5, 12), (4, 5, 7, 10, 1, 2), (3, 4, 5, 6, 7, 12)]], cols=1),
     S("Solve", [Problem(f"Lillie used {F(2, 3)} cup of flour, Ellie used {F(3, 4)} cup, and Mom used {F(5, 8)} cup. Who used the most? The least?", "Most: Ellie; least: Mom", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Order {F(3, 10)}, {F(1, 2)}, {F(2, 5)} from greatest to least.", f"{F(1, 2)}, {F(2, 5)}, {F(3, 10)}", space=30, wide=True)], cols=1)],
    TE("Students order three or more fractions.", "Compare fractions; record with symbols.", "Workbook Lesson 5.13",
       flow("2/3 vs 5/8.", "Read Let's Explore.", ["Work both examples. Discuss which strategy fits."], "Try It 1–3."),
       ["Ordering by numerator or denominator alone."], ["Rename all to a common denominator."], ["Order five fractions."]),
    summary="Order fractions by renaming to a common denominator or by using benchmarks.")

L14 = Lesson("5.14", "Comparing Fractions of the Same Whole",
    "I can explain why fractions can only be compared when they refer to the same whole.", "4.NF.2",
    [("whole", "The one complete thing or group a fraction is part of.")],
    f"Ellie ate {F(1, 2)} of a small pizza. Lillie ate {F(1, 3)} of a large pizza. Ellie says she ate more because {F(1, 2)} &gt; {F(1, 3)}. Is she right?",
    [Text(f"Not necessarily! {F(1, 2)} &gt; {F(1, 3)} is only true when both fractions are of the <b>same whole</b>. Half of a small pizza could be less than a third of a huge pizza."),
     KeyIdea("Comparisons are only valid when the two fractions refer to the same whole."),
     Example("Different wholes", f"Is {F(1, 2)} of 10 more or less than {F(1, 3)} of 30?", [f"{F(1, 2)} of 10 = 5.", f"{F(1, 3)} of 30 = 10."], f"Less: 5 &lt; 10")],
    [Problem(f"{F(1, 4)} of 40 or {F(1, 2)} of 12. Which is more?", f"{F(1, 4)} of 40 (10 &gt; 6)"), Problem("Can you say 2/3 > 1/2 for any two pizzas?".replace("2/3", F(2, 3)).replace("1/2", F(1, 2)), "Only if the pizzas are the same size."),
     Problem(f"{F(3, 4)} of 8 vs {F(3, 4)} of 20", f"{F(3, 4)} of 20 is more (15 &gt; 6)")],
    [S("Warm-Up", [Problem(f"{F(1, 3)} of 18", "6"), Problem(f"{F(1, 2)} of 18", "9")]),
     S("Which is more?", [Problem(f"{F(1, 2)} of 8 or {F(1, 4)} of 24", f"{F(1, 4)} of 24 (6 &gt; 4)"), Problem(f"{F(2, 3)} of 9 or {F(1, 2)} of 14", f"{F(1, 2)} of 14 (7 &gt; 6)"),
                          Problem(f"{F(3, 5)} of 10 or {F(1, 2)} of 10", f"{F(3, 5)} of 10 (6 &gt; 5)"), Problem(f"{F(1, 6)} of 60 or {F(5, 6)} of 6", f"{F(1, 6)} of 60 (10 &gt; 5)")]),
     S("Think Deeper", [Problem(f"Draw two different-size rectangles where {F(1, 4)} of one is bigger than {F(1, 2)} of the other.", "Drawings vary: a large rectangle's fourth vs a small rectangle's half.", space=70, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain why the size of the whole matters when comparing fractions.", "The same fraction of a bigger whole is a bigger amount.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students recognize that fraction comparisons require the same whole.", "Recognize that comparisons are valid only when the two fractions refer to the same whole.", "Two paper circles of different sizes, workbook Lesson 5.14",
       flow("1/3 of 18 and 1/2 of 18.", "Read Let's Explore with a big and small paper circle.", ["Cut half of the small circle and a third of the big circle; compare.", "Say: Same whole first, then compare."], "Try It 1–3."),
       ["Always trusting the symbol comparison regardless of the whole."], ["Use real objects of different sizes."], ["Create a tricky fraction riddle."]),
    summary="You can only compare fractions directly when they are parts of the same whole.")

L15 = Lesson("5.15", "Fraction Comparison Word Problems",
    "I can solve word problems by comparing fractions and explain my answer.", "4.NF.2",
    [],
    f"Ellie practiced piano {F(3, 4)} hour. Lillie practiced {F(5, 6)} hour. Who practiced longer?",
    [Text("Decide which strategy to use, compare, then answer in a sentence."),
     Example("Compare times", f"{F(3, 4)} hour vs {F(5, 6)} hour.", ["Common denominator 12: 9/12 vs 10/12.".replace("9/12", F(9, 12)).replace("10/12", F(10, 12))], "Lillie practiced longer."),
     Example("Missing piece", f"A recipe needs {F(2, 3)} cup of sugar. You have {F(3, 4)} cup. Do you have enough?", [f"{F(2, 3)} = {F(8, 12)}, {F(3, 4)} = {F(9, 12)}.", "9 &gt; 8."], "Yes, you have enough."),
     KeyIdea("Answer word problems with a complete sentence and make sure the wholes are the same.")],
    [Problem(f"A blue ribbon is {F(5, 8)} yard. A red ribbon is {F(1, 2)} yard. Which is longer?", "the blue ribbon"),
     Problem(f"Ellie ate {F(2, 6)} of her sandwich. Lillie ate {F(1, 3)} of hers (same size). Who ate more?", "They ate the same amount."),
     Problem(f"A trail is {F(7, 10)} mile. Another is {F(3, 5)} mile. Which is shorter?", f"the {F(3, 5)}-mile trail")],
    [S("Warm-Up", [Problem(f"{F(2, 5)} &nbsp;◯&nbsp; {F(1, 2)}", "<"), Problem(f"{F(4, 6)} &nbsp;◯&nbsp; {F(2, 3)}", "=")]),
     S("Solve. Answer in a sentence.", [
         Problem(f"Dad walked {F(4, 5)} mile. Mom walked {F(7, 10)} mile. Who walked farther?", "Dad walked farther.", space=40, wide=True),
         Problem(f"A plant grew {F(3, 8)} inch in week 1 and {F(1, 4)} inch in week 2. Which week did it grow more?", "Week 1.", space=40, wide=True),
         Problem(f"Lillie finished {F(5, 12)} of her project. Ellie finished {F(1, 2)} of hers. Who has more left to do?", "Lillie has more left.", space=40, wide=True),
         Problem(f"A jug has {F(2, 3)} gallon of tea. A recipe needs {F(5, 6)} gallon. Is there enough?", f"No. {F(2, 3)} = {F(4, 6)} &lt; {F(5, 6)}.", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Write a word problem comparing {F(3, 4)} and {F(2, 3)}. Solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve comparison word problems with fractions.", "Compare two fractions; justify conclusions.", "Workbook Lesson 5.15",
       flow("Two quick comparisons.", "Read Let's Explore.", ["Work both examples. Require a sentence answer."], "Try It 1–3."),
       ["Answering with just a symbol."], ["Underline the question."], ["Make a fraction comparison game with cards."]),
    summary="Pick a strategy, compare, and answer in a full sentence about the same whole.")

L16 = Lesson("5.16", "Explaining Fraction Reasoning",
    "I can explain and justify my thinking about equivalent fractions and comparisons.", "4.NF.1, 4.NF.2",
    [("justify", "To give reasons that show why something is true.")],
    f"Sam says {F(3, 6)} &gt; {F(1, 2)} because 3 &gt; 1. How would you convince Sam he is wrong?",
    [Text("Mathematicians explain their thinking with models, numbers, and words. A strong explanation uses at least two of these."),
     Example("Justify", f"Show that {F(3, 6)} = {F(1, 2)}.", ["Model: 3 of 6 equal parts covers the same length as 1 of 2 equal parts.", f"Numbers: {F(1, 2)} = {F('1 × 3', '2 × 3')} = {F(3, 6)}.",
                                                       "Words: The pieces are 3 times smaller, but there are 3 times as many."], "They are equal."),
     KeyIdea("Use a model, numbers, and words to justify your answer.")],
    [Problem(f"Explain why {F(2, 8)} = {F(1, 4)}.", "2 eighths cover the same length as 1 fourth; 1×2/4×2.", lines=2, space=0),
     Problem(f"Explain why {F(5, 6)} &lt; {F(7, 8)}.", "Each is one piece from 1; an eighth is a smaller gap.", lines=2, space=0),
     Problem(f"Is {F(4, 10)} &gt; {F(1, 2)}? Explain.", f"No; {F(5, 10)} = {F(1, 2)} and 4 &lt; 5.", lines=2, space=0)],
    [S("Warm-Up", [Problem(f"Simplify {F(10, 12)}", F(5, 6)), Problem(f"{F(3, 9)} &nbsp;◯&nbsp; {F(1, 3)}", "=")]),
     S("Justify with a model, numbers, and words", [
         Problem(f"Is {F(4, 6)} equivalent to {F(2, 3)}?", f"Yes; {F(2, 3)} = {F(4, 6)} (× 2); model shows same length.", lines=3, space=0, wide=True),
         Problem(f"Which is greater: {F(5, 8)} or {F(3, 5)}?", f"{F(5, 8)} (25/40 vs 24/40)".replace("25/40", F(25, 40)).replace("24/40", F(24, 40)), lines=3, space=0, wide=True),
         Problem(f"Maria says {F(1, 4)} of a pizza is always less than {F(1, 3)} of a pizza. When is she right? When could she be wrong?", "Right if the pizzas are the same size; wrong if the 1/4 pizza is much larger.".replace("1/4", F(1, 4)), lines=3, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which comparison strategy do you like best? Show it with an example.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students justify equivalence and comparisons with models, numbers, and words.", "Justify conclusions about equivalence and comparison.", "Workbook Lesson 5.16, Unit 5 Review",
       flow("Simplify 10/12.", "Read Let's Explore.", ["Work the example. Model a three-part explanation."], "Try It 1–3.", "Workbook Lesson 5.16 and the Unit 5 Review.", "Check. Tomorrow: Unit 5 Test."),
       ["Giving answers without reasons."], ["Sentence frames: ‘I know … because …’"], ["Teach a sibling one strategy."]),
    summary="Justify fraction ideas with a model, numbers, and words.")

C1 = Check("Weekly Check 9: Understanding Fractions", [S("Show what you know", [
    Problem("Name the shaded fraction.", F(5, 8), fig=bar(5, 8), space=0), Problem("Name point P.", F(3, 4), fig=lambda t: frac_number_line(t, 4, 1, points=[(3, "P")], label_all=False, width=CW), space=0),
    Problem(f"Write {F(11, 3)} as a mixed number.", MX(3, 2, 3)), Problem(f"Write {MX(2, 1, 4)} as a fraction.", F(9, 4)),
    Problem(f"{F(2, 3)} of 18", "12"), Problem(f"{F(3, 3)} = ___", "1")])], minutes=15)
C2 = Check("Weekly Check 10: Equivalent Fractions", [S("Show what you know", [
    Problem(f"{F(2, 3)} = {F('?', 9)}", "6"), Problem(f"{F(3, 5)} = {F('?', 20)}", "12"), Problem(f"Simplify {F(8, 10)}", F(4, 5)), Problem(f"Simplify {F(9, 15)}", F(3, 5)),
    Problem(f"Write two fractions equivalent to {F(1, 4)}.", f"e.g. {F(2, 8)}, {F(3, 12)}"), Problem(f"Are {F(3, 4)} and {F(9, 12)} equivalent? Explain.", "Yes; × 3", lines=2, space=0)])], minutes=15)
C3 = Check("Weekly Check 11: Comparing Fractions", [S("Write >, <, or = in the circle", [Problem(f"{F(a, b)} &nbsp;◯&nbsp; {F(c_, d)}", fcmp(a, b, c_, d)) for a, b, c_, d in
    [(3, 7, 5, 7), (2, 5, 2, 9), (3, 8, 4, 6), (5, 6, 7, 9), (2, 3, 8, 12), (4, 10, 1, 2)]])], minutes=15)

REVIEW = Check("Unit 5 Review", [
    S("Fraction meaning", [Problem(f"Write {F(13, 4)} as a mixed number.", MX(3, 1, 4)), Problem(f"{F(3, 5)} of 25", "15"),
                           Problem("Name point Q.", F(5, 6), fig=lambda t: frac_number_line(t, 6, 1, points=[(5, "Q")], label_all=False, width=CW), space=0)]),
    S("Equivalent fractions", [Problem(f"{F(3, 4)} = {F('?', 16)}", "12"), Problem(f"Simplify {F(12, 16)}", F(3, 4))]),
    S("Compare and order", [Problem(f"{F(5, 9)} &nbsp;◯&nbsp; {F(2, 5)}", fcmp(5, 9, 2, 5)), Problem(f"{F(3, 4)} &nbsp;◯&nbsp; {F(7, 10)}", fcmp(3, 4, 7, 10)),
                            Problem(f"Order least to greatest: {F(3, 5)}, {F(1, 2)}, {F(7, 10)}", f"{F(1, 2)}, {F(3, 5)}, {F(7, 10)}", wide=True),
                            Problem(f"Is {F(1, 2)} of a small cake always more than {F(1, 4)} of a big cake? Explain.", "No; the wholes are different sizes.", lines=2, space=0, wide=True)])],
    kind="review", minutes=35, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 5 Test", [
    S("Part A · Fraction meaning (1 point each)", [Problem("Name the shaded fraction.", F(3, 10), fig=bar(3, 10), space=0),
        Problem("Name point R.", F(2, 5), fig=lambda t: frac_number_line(t, 5, 1, points=[(2, "R")], label_all=False, width=CW), space=0),
        Problem(f"Write {F(17, 5)} as a mixed number.", MX(3, 2, 5)), Problem(f"{F(3, 4)} of 32", "24")]),
    S("Part B · Equivalent fractions (1 point each)", [Problem(f"{F(2, 5)} = {F('?', 15)}", "6"), Problem(f"{F(5, 6)} = {F(20, '?')}", "24"),
        Problem(f"Simplify {F(15, 25)}", F(3, 5)), Problem(f"Simplify {F(14, 20)}", F(7, 10))]),
    S("Part C · Compare (1 point each)", [Problem(f"{F(a, b)} &nbsp;◯&nbsp; {F(c_, d)}", fcmp(a, b, c_, d)) for a, b, c_, d in [(4, 9, 7, 9), (3, 4, 3, 7), (5, 8, 2, 6), (2, 3, 7, 10), (9, 12, 3, 4), (5, 6, 4, 5)]]),
    S("Part D · Explain and solve (3 points each)", [
        Problem(f"Order from least to greatest and explain your strategy: {F(2, 3)}, {F(5, 12)}, {F(3, 4)}", f"{F(5, 12)}, {F(2, 3)}, {F(3, 4)} (5/12, 8/12, 9/12)".replace("5/12", F(5, 12)).replace("8/12", F(8, 12)).replace("9/12", F(9, 12)), lines=3, space=0, wide=True, points=3),
        Problem(f"Ellie says {F(4, 8)} &gt; {F(1, 2)} because 4 &gt; 1. Use a model and numbers to show whether she is right.", f"She is wrong: {F(4, 8)} = {F(1, 2)}; model shows equal lengths.", space=70, wide=True, points=3)], cols=1)],
    kind="test", minutes=40, rubric=[["17–20 (85%+)", "Mastered."], ["14–16", "Proficient; correct missed items."], ["Below 14", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-01-25", "2027-02-01", "2027-02-08", "2027-02-15"], CHECKS, REVIEW, TEST)

UNIT = Unit(5, "Fraction Equivalence and Comparison", "Fractions on number lines, equivalent fractions, simplest form, and comparing and ordering fractions.",
    "Fractions are numbers that name parts of a whole. In this unit you will find different names for the same fraction, simplify fractions, and compare fractions with different numerators and denominators.",
    ["Explain fractions with models and number lines, including fractions greater than 1.", "Find fractions of a set.", "Make equivalent fractions by multiplying or dividing.",
     "Compare fractions with benchmarks, common denominators, and common numerators.", "Explain why comparisons need the same whole."],
    [("4.NF.1", "Explain why a/b is equivalent to (n×a)/(n×b) using visual models; generate equivalent fractions."),
     ("4.NF.2", "Compare two fractions with different numerators and denominators using common denominators, numerators, or benchmarks; same whole; record with >, =, <.")],
    [("fraction", "A number naming part of a whole."), ("numerator", "Top number: parts counted."), ("denominator", "Bottom number: equal parts in the whole."),
     ("equivalent fractions", "Fractions naming the same amount."), ("simplest form", "No common factor but 1."), ("benchmark fraction", "Friendly fraction like 0, 1/2, 1.")],
    ["Factors and multiples (Unit 4).", "Grade 3 fractions: unit fractions, fractions on a number line."],
    ["Paper strips for fraction strips (make a set: halves to twelfths)", "Paper circles", "Ruler marked in eighths", "Counters"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Fractions are in recipes, rulers, sports statistics, sale prices, and music. Comparing fractions tells you which recipe uses more sugar or which runner went farther.",
    family_note="Make a set of paper fraction strips together (halves through twelfths). Cook together and talk about measuring cups: which is more, one-third cup or one-fourth cup?",
    weeks=WEEKS)
