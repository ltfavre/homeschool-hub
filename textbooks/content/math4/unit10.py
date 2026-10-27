"""Grade 4 Math · Unit 10: Year in Review (Jun 21 – Jul 16, 2027)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import c, F, MX, words, expanded, round_to
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def review_te(focus, materials="Workbook lesson pages; the unit's Study Guide in the textbook"):
    return TE(f"Students review and strengthen {focus}.", "Cumulative review of Grade 4 standards.", materials,
              flow("Quick mental-math warm-up from the workbook.", "Read Let's Explore and ask the student to explain a strategy from memory.",
                   ["Reread the Remember box together.", "Work the example. Ask the student to teach it back to you.", "Look back at the student's Unit Test: reteach any item that was missed."],
                   "Try It 1–3."),
              ["Old mistakes coming back — check the misconceptions listed in the original unit."], ["Use the textbook lesson from the original unit."], ["Have the student write and solve a challenge problem."])


def RL(num, title, i_can, std, launch, remember, example, try_it, practice, summary):
    return Lesson(num, title, i_can, std, [], launch, [KeyIdea(remember, "Remember"), example], try_it, practice, review_te(title.lower()), summary=summary)


L1 = RL("10.1", "Review: Place Value and Rounding", "I can read, write, compare, and round numbers to one million.", "4.NBT.1–3",
    "What is the greatest six-digit number you can write? Round it to the nearest hundred thousand.",
    "Each place is 10 times the place to its right. To round, look one place to the right: 5 or more rounds up.",
    Example("Round and compare", "Round 638,452 to the nearest ten thousand. Is it greater than 638,524?", ["Ten thousands digit 3; look right: 8 → round up.", "640,000.", "638,452 &lt; 638,524 (hundreds: 4 &lt; 5)."], "640,000; no"),
    [Problem("Write 407,019 in words.", words(407019)), Problem("Round 85,349 to the nearest thousand.", "85,000"), Problem("Value of the 6 in 961,000", "60,000")],
    [S("Warm-Up", [Problem("10 × 4,000", "40,000"), Problem("Round 96 to the nearest ten.", "100")]),
     S("Practice", [Problem("Write 230,506 in expanded form.", expanded(230506), wide=True), Problem("Write 76,000 + 900 + 3 in standard form.", "76,903"),
                    Problem("Compare 409,999 ◯ 410,001", "<"), Problem("Order: 52,110; 51,210; 52,101", "51,210; 52,101; 52,110"),
                    Problem("Round 472,815 to the nearest hundred thousand.", "500,000"), Problem("Round 7,449 to the nearest hundred.", "7,400"),
                    Problem("3,600 = ___ hundreds", "36")]),
     S("Exit Ticket", [Problem("Explain how 5,500 rounds to the nearest thousand.", "Hundreds digit is 5, so round up to 6,000.", lines=2, space=0, wide=True)], cols=1)],
    "Place value, comparing, and rounding work the same way for every size of number.")

L2 = RL("10.2", "Review: Adding and Subtracting", "I can add and subtract multi-digit numbers fluently and check with estimation.", "4.NBT.4",
    "A truck carried 12,486 pounds on Monday and 9,758 pounds on Tuesday. How much more on Monday? How much in all?",
    "Line up places. Add or subtract from right to left, regrouping as needed. Estimate to check.",
    Example("Both operations", "12,486 and 9,758", ["Sum: 12,486 + 9,758 = 22,244.", "Difference: 12,486 − 9,758 = 2,728.", "Check: 12,000 + 10,000 = 22,000; 12,000 − 10,000 = 2,000."], "22,244 in all; 2,728 more"),
    [Problem("46,327 + 38,895", c(46327 + 38895)), Problem("70,000 − 26,418", c(70000 - 26418)), Problem("Estimate 6,812 − 2,390.", "7,000 − 2,000 = 5,000")],
    [S("Warm-Up", [Problem("900 − 456", "444"), Problem("378 + 549", "927")]),
     S("Practice", [Problem(f"{c(a)} {o} {c(b)}", c(a + b if o == "+" else a - b), space=0, fig=(lambda a=a, b=b, o=o: (lambda t: column_arith(t, a, b, o, show_answer=False, size=15)))())
                    for a, b, o in [(28507, 46918, "+"), (63205, 17846, "-"), (400000, 152736, "-"), (19999, 80001, "+")]]),
     S("Solve", [Problem("A school raised $14,250. It spent $6,875 on books and $3,940 on computers. How much is left?", "$3,435", space=60, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Find 50,003 − 28,765 and check by adding.", "21,238; 21,238 + 28,765 = 50,003", space=50, wide=True)], cols=1)],
    "Line up places, regroup carefully, and estimate to check.")

L3 = RL("10.3", "Review: Multiplying", "I can multiply up to four digits by one digit and two digits by two digits.", "4.NBT.5",
    "A stadium has 48 sections with 50 seats each. How many seats is that? How could you find it quickly?",
    "Use area models, partial products, or the standard algorithm. Estimate to check.",
    Example("Two strategies", "Find 6 × 2,347 and 34 × 27.", ["6 × 2,347: 6 × 2,000 + 6 × 300 + 6 × 40 + 6 × 7 = 12,000 + 1,800 + 240 + 42 = 14,082.", "34 × 27: 600 + 80 + 210 + 28 = 918."], "14,082 and 918"),
    [Problem("7 × 3,058", c(7 * 3058)), Problem("45 × 23", c(45 * 23)), Problem("80 × 60", "4,800")],
    [S("Warm-Up", [Problem("9 × 700", "6,300"), Problem("40 × 50", "2,000")]),
     S("Practice", [Problem(f"{c(a)} × {b}", c(a * b), space=60) for a, b in [(486, 7), (2905, 6), (63, 48), (75, 32)]]),
     S("Solve", [Problem("A bakery makes 36 trays of 24 muffins each day. How many muffins in 5 days?", "4,320 muffins", space=60, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Show 27 × 14 with an area model.", "378", space=60, wide=True)], cols=1)],
    "Break factors into place-value parts, multiply each part, and add.")

L4 = RL("10.4", "Review: Dividing", "I can divide up to four digits by one digit and interpret remainders.", "4.NBT.6, 4.OA.3",
    "A farmer packs 1,350 eggs into cartons of 6. How many full cartons? Any left over?",
    "Divide, multiply, subtract, bring down. Check: quotient × divisor + remainder = dividend. Decide what the remainder means.",
    Example("Long division", "1,350 ÷ 6", ["13 ÷ 6 = 2 R1; 15 ÷ 6 = 2 R3; 30 ÷ 6 = 5.", "Check: 225 × 6 = 1,350."], "225 cartons, none left"),
    [Problem("2,184 ÷ 7", c(2184 // 7)), Problem("605 ÷ 4", "151 R1"), Problem("50 people, 8 per table. How many tables?", "7 tables")],
    [S("Warm-Up", [Problem("4,200 ÷ 6", "700"), Problem("58 ÷ 7", "8 R2")]),
     S("Practice", [Problem(f"{c(a)} ÷ {b}", (lambda q, r: c(q) + (f" R{r}" if r else ""))(*divmod(a, b)), space=70, fig=(lambda a=a, b=b: (lambda t: long_div(t, a, b, show_answer=False)))()) for a, b in [(936, 4), (1475, 5), (3209, 8), (6012, 9)]]),
     S("Solve", [Problem("A ribbon 250 inches long is cut into 9-inch pieces. How many full pieces? How much is left?", "27 pieces; 7 inches left", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a story for 100 ÷ 8 where the answer is 13.", "Example: 100 people, 8 per van → 13 vans", lines=2, space=0, wide=True)], cols=1)],
    "Divide step by step, check by multiplying, and interpret the remainder.")

L5 = RL("10.5", "Review: Factors and Multiples", "I can find factors, multiples, and tell prime from composite.", "4.OA.4",
    "Is 91 prime? (Many people think so!)",
    "Factor pairs multiply to the number. Prime: exactly 2 factors. Multiples come from skip counting.",
    Example("Prime or composite", "Is 91 prime?", ["Test small factors: 2 no, 3 no (9 + 1 = 10), 5 no, 7: 7 × 13 = 91."], "Composite"),
    [Problem("Factors of 36", "1, 2, 3, 4, 6, 9, 12, 18, 36"), Problem("Is 53 prime?", "Yes"), Problem("First common multiple of 6 and 8", "24")],
    [S("Warm-Up", [Problem("7 × 13", "91"), Problem("Is 2 prime?", "Yes")]),
     S("Practice", [Problem("Factor pairs of 60", "1×60, 2×30, 3×20, 4×15, 5×12, 6×10", wide=True), Problem("Prime or composite: 39", "composite"), Problem("Prime or composite: 61", "prime"),
                    Problem("First 5 multiples of 11", "11, 22, 33, 44, 55"), Problem("Is 126 divisible by 9?", "Yes (1 + 2 + 6 = 9)"), Problem("Is 7 a factor of 98?", "Yes")]),
     S("Exit Ticket", [Problem("Name two numbers that have exactly 3 factors.", "e.g. 4 (1, 2, 4), 9, 25, 49", lines=1, space=0, wide=True)], cols=1)],
    "Factors divide evenly; multiples come from skip counting; primes have exactly two factors.")

L6 = RL("10.6", "Review: Patterns", "I can extend number and shape patterns and describe their rules and features.", "4.OA.5",
    "Rule: start at 5, add 5. Will 101 be in the pattern?",
    "Find the change between terms. Look for features like odd/even. For repeating patterns, use division.",
    Example("Features", "Start at 5, add 5: 5, 10, 15, 20…", ["All terms are multiples of 5.", "They end in 5 or 0, alternating."], "101 is not a term"),
    [Problem("Rule: start at 3, multiply by 2. First 5 terms.", "3, 6, 12, 24, 48"), Problem("Next: 99, 88, 77, ___", "66"), Problem("Core: A B B C. 18th letter?", "B (18 ÷ 4 = 4 R2)")],
    [S("Warm-Up", [Problem("Count by 7s to 49", "7, 14, 21, 28, 35, 42, 49", lines=1, space=0, wide=True)], cols=1),
     S("Practice", [Problem("Find the rule: 4, 13, 22, 31", "add 9"), Problem("Input 3, 5, 8 → output 18, 30, 48. Rule?", "× 6"),
                    Problem("Start at 2, add 4. Odd or even terms?", "always even"), Problem("Shape core: ● ▲ ■. 25th shape?", "● (25 ÷ 3 = 8 R1)")]),
     S("Exit Ticket", [Problem("Make a pattern whose terms are all odd. Explain why.", "e.g. start 1, add 2: odd + even = odd", lines=2, space=0, wide=True)], cols=1)],
    "Find the rule, then look for hidden features.")

L7 = RL("10.7", "Review: Multi-Step Word Problems", "I can solve multi-step word problems with all four operations.", "4.OA.3",
    "A class of 28 students goes on a trip. Tickets are $9 each. Buses hold 12 students. How many buses, and how much do tickets cost?",
    "Find the hidden steps. Write an equation for each, with a letter for the unknown. Check reasonableness.",
    Example("Two questions", "28 students, $9 tickets, buses of 12", ["Tickets: 28 × 9 = 252.", "Buses: 28 ÷ 12 = 2 R4 → 3 buses."], "$252 and 3 buses"),
    [Problem("4 packs of 18 pencils shared by 6 students. Each gets?", "12"), Problem("$50 − 3 × $12", "$14"), Problem("A 6-week summer camp, 5 days a week, 3 hours a day. Hours?", "90 hours")],
    [S("Warm-Up", [Problem("28 × 9", "252"), Problem("28 ÷ 12", "2 R4")]),
     S("Solve", [Problem("Ellie earns $8 a week. After 9 weeks she buys a $45 game. How much is left?", "$27", space=50, wide=True),
                 Problem("A library has 6 shelves of 125 books. It gives away 230 books. How many remain?", "520 books", space=50, wide=True),
                 Problem("150 cupcakes go in boxes of 8. How many boxes are needed to hold all of them?", "19 boxes", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a two-step word problem using multiplication and subtraction. Solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    "Find the hidden steps, write equations, and check that your answer makes sense.")

L8 = RL("10.8", "Review: Whole-Number Challenge", "I can solve challenging whole-number problems and explain my strategies.", "4.NBT, 4.OA",
    "Use the digits 2, 4, 6, 8 once each to make the greatest product of a 2-digit × 2-digit problem.",
    "Try, check, and improve. Organized guessing is a real strategy.",
    Example("Organized guessing", "Greatest product with 2, 4, 6, 8", ["Put the big digits in the tens places: 8_ × 6_.", "Try 82 × 64 = 5,248 and 84 × 62 = 5,208.", "82 × 64 is greater."], "82 × 64 = 5,248"),
    [Problem("Least product with the same digits?", "26 × 48 = 1,248"), Problem("Greatest 4-digit number divisible by 5 using 1, 3, 5, 7 once each", "7,315"), Problem("Two numbers multiply to 96 and add to 20. What are they?", "8 and 12")],
    [S("Warm-Up", [Problem("82 × 64", "5,248"), Problem("84 × 62", "5,208")]),
     S("Challenges", [Problem("Find a 3-digit number that is a multiple of 2, 3, 5, and 9.", "e.g. 270, 360, 450", space=40, wide=True),
                      Problem("A number rounded to the nearest hundred is 4,500. What are the least and greatest whole numbers it could be?", "4,450 and 4,549", space=40, wide=True),
                      Problem("Place +, −, ×, ÷ to make it true: 8 ◯ 4 ◯ 2 = 16", "e.g. 8 × 4 ÷ 2 = 16 or 8 + 4 × 2 = 16", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which whole-number skill are you proudest of this year? Show it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    "Organized trying, checking, and improving solves challenging problems.")

L9 = RL("10.9", "Review: Equivalent Fractions", "I can find equivalent fractions and simplify.", "4.NF.1",
    f"Is {F(6, 9)} the same as {F(2, 3)}? How can you prove it?",
    f"Multiply or divide the numerator and denominator by the same number: {F('a', 'b')} = {F('n × a', 'n × b')}.",
    Example("Prove it", f"{F(6, 9)} and {F(2, 3)}", [f"{F(2, 3)} × {F(3, 3)} = {F(6, 9)}.", "A model shows the same amount."], "They are equivalent."),
    [Problem(f"{F(3, 5)} = {F('?', 20)}", "12"), Problem(f"Simplify {F(16, 20)}", F(4, 5)), Problem(f"Write two fractions equal to {F(1, 3)}.", f"e.g. {F(2, 6)}, {F(4, 12)}")],
    [S("Warm-Up", [Problem("Factors of 16", "1, 2, 4, 8, 16"), Problem(f"{F(1, 2)} = {F('?', 8)}", "4")]),
     S("Practice", [Problem(f"{F(n, d)} = {F('?', d * k)}", str(n * k)) for n, d, k in [(2, 3, 4), (5, 6, 2), (3, 8, 3)]] + [Problem(f"Simplify {F(n, d)}", F(Fr(n, d).numerator, Fr(n, d).denominator)) for n, d in [(10, 12), (9, 15), (12, 18)]]),
     S("Exit Ticket", [Problem(f"Draw a model to show {F(3, 4)} = {F(6, 8)}.", "Two equal bars: 3 of 4 and 6 of 8 shaded", space=50, wide=True)], cols=1)],
    "Equivalent fractions name the same amount; multiply or divide top and bottom by the same number.")

L10 = RL("10.10", "Review: Comparing Fractions", "I can compare and order fractions with different denominators.", "4.NF.2",
    f"Which is greater: {F(5, 8)} or {F(3, 5)}?",
    "Use benchmarks, common denominators, or common numerators. Compare only when the wholes are the same.",
    Example("Common denominator", f"{F(5, 8)} vs {F(3, 5)}", [f"{F(25, 40)} vs {F(24, 40)}."], f"{F(5, 8)} &gt; {F(3, 5)}"),
    [Problem(f"{F(4, 9)} ◯ {F(1, 2)}", "<"), Problem(f"{F(7, 10)} ◯ {F(2, 3)}", ">"), Problem(f"Order: {F(1, 2)}, {F(3, 8)}, {F(3, 4)}", f"{F(3, 8)}, {F(1, 2)}, {F(3, 4)}")],
    [S("Warm-Up", [Problem("Common multiple of 3 and 4", "12"), Problem(f"{F(2, 3)} = {F('?', 12)}", "8")]),
     S("Write >, <, or = in the circle", [Problem(f"{F(a, b)} ◯ {F(cc, d)}", ">" if Fr(a, b) > Fr(cc, d) else "<" if Fr(a, b) < Fr(cc, d) else "=") for a, b, cc, d in
                                          [(2, 5, 3, 8), (5, 6, 7, 8), (4, 12, 1, 3), (3, 4, 5, 7), (1, 6, 2, 9), (9, 10, 4, 5)]]),
     S("Exit Ticket", [Problem(f"Order from greatest to least: {F(2, 3)}, {F(5, 12)}, {F(3, 4)}", f"{F(3, 4)}, {F(2, 3)}, {F(5, 12)}", wide=True)], cols=1)],
    "Pick the fastest comparison strategy and make sure the wholes match.")

L11 = RL("10.11", "Review: Fraction Operations", "I can add and subtract fractions and mixed numbers and multiply fractions by whole numbers.", "4.NF.3, 4.NF.4",
    f"A recipe needs {MX(1, 3, 4)} cups of flour. You triple it. How much flour?",
    "Like denominators: add or subtract numerators. Mixed numbers: regroup when needed. n × a/b = (n × a)/b.".replace("a/b", F("a", "b")).replace("(n × a)/b", F("n × a", "b")),
    Example("Triple a mixed number", f"3 × {MX(1, 3, 4)}", [f"{MX(1, 3, 4)} = {F(7, 4)}.", f"3 × {F(7, 4)} = {F(21, 4)} = {MX(5, 1, 4)}."], MX(5, 1, 4) + " cups"),
    [Problem(f"{MX(2, 5, 8)} + {MX(1, 6, 8)}", MX(4, 3, 8)), Problem(f"{MX(5, 1, 3)} − {MX(2, 2, 3)}", MX(2, 2, 3)), Problem(f"4 × {F(5, 6)}", MX(3, 2, 6))],
    [S("Warm-Up", [Problem(f"{F(7, 4)} as a mixed number", MX(1, 3, 4)), Problem(f"{MX(2, 1, 5)} as a fraction", F(11, 5))]),
     S("Practice", [Problem(f"{F(5, 12)} + {F(9, 12)}", MX(1, 2, 12)), Problem(f"{F(9, 10)} − {F(4, 10)}", F(5, 10)), Problem(f"{MX(3, 2, 6)} + {MX(4, 5, 6)}", MX(8, 1, 6)),
                    Problem(f"{MX(6, 1, 4)} − {MX(3, 3, 4)}", MX(2, 2, 4)), Problem(f"5 × {F(2, 3)}", MX(3, 1, 3)), Problem(f"7 × {F(3, 10)}", MX(2, 1, 10))]),
     S("Exit Ticket", [Problem(f"Lillie runs {F(4, 5)} mile a day for 6 days. Ellie runs {MX(4, 3, 5)} miles. Who runs farther?", f"Lillie ({MX(4, 4, 5)} miles)", space=40, wide=True)], cols=1)],
    "Add and subtract like fractions, regroup mixed numbers, and multiply the numerator by the whole number.")

L12 = RL("10.12", "Review: Decimals", "I can write, compare, and add with tenths and hundredths, including money.", "4.NF.5–7",
    "Which is more money: $0.75 or $0.8?",
    "Tenths and hundredths: 0.8 = 0.80. Line up decimal points to compare and to add money.",
    Example("Compare", "$0.75 vs $0.8", ["$0.8 = $0.80.", "80 &gt; 75."], "$0.80 is more"),
    [Problem(f"{F(7, 100)} as a decimal", "0.07"), Problem(f"{F(4, 10)} + {F(35, 100)}", F(75, 100)), Problem("Order: 0.5, 0.45, 0.54", "0.45, 0.5, 0.54")],
    [S("Warm-Up", [Problem("0.6 = 0.___", "60"), Problem("$1.00 − $0.35", "$0.65")]),
     S("Practice", [Problem(f"{F(39, 100)} as a decimal", "0.39"), Problem("2.07 in words", "two and seven hundredths"), Problem("3.4 ◯ 3.38", ">"),
                    Problem(f"{F(1, 4)} ◯ 0.3", "<"), Problem("$12.48 + $7.75", "$20.23"), Problem("$20.00 − $13.86", "$6.14")]),
     S("Exit Ticket", [Problem("Ellie has $5. She buys 2 snacks at $1.35 each. How much is left?", "$2.30", space=30, wide=True)], cols=1)],
    "Decimals are fractions in tenths and hundredths; line up the decimal points.")

L13 = RL("10.13", "Review: Geometry and Angles", "I can classify shapes and measure, draw, and find angles.", "4.G.1–3, 4.MD.5–7",
    "A pizza is cut into 6 equal slices. What angle does each slice make at the center?",
    "A full turn is 360°. Angles are additive. Classify shapes by sides, angles, and symmetry.",
    Example("Angles in a circle", "6 equal slices", ["360 ÷ 6 = 60."], "60° each"),
    [Problem("Right angle split into 25° and x", "65°"), Problem("Lines of symmetry in a rectangle (not a square)", "2"), Problem("A triangle with one 90° angle is a ___ triangle.", "right")],
    [S("Warm-Up", [Problem("360 ÷ 4", "90"), Problem("180 − 35", "145")]),
     S("Practice", [Problem("Classify a 98° angle.", "obtuse"), Problem("Name a quadrilateral with 4 equal sides and no right angles.", "rhombus"),
                    Problem("Straight angle split into 120° and x", "60°"), Problem("How many endpoints does a ray have?", "1"),
                    Problem("Read the protractor.", "105°", fig=lambda t: protractor_fig(t, 105, width=CW), space=0), Problem("Draw two perpendicular line segments.", "drawing", space=40)]),
     S("Exit Ticket", [Problem("Draw a triangle with one obtuse angle. Label its angles with estimates.", "Answers vary; one angle > 90°.", space=60, wide=True)], cols=1)],
    "Use angle facts (90°, 180°, 360°) and shape attributes.")

L14 = RL("10.14", "Review: Area, Perimeter, and Conversions", "I can solve area, perimeter, and measurement conversion problems.", "4.MD.1–3",
    "A rectangular garden has an area of 72 square feet and a width of 6 feet. How much fence goes around it?",
    "A = l × w; P = 2 × l + 2 × w. Big unit to small unit: multiply.",
    Example("Two steps", "A = 72, w = 6. Find P.", ["l = 72 ÷ 6 = 12.", "P = 2 × 12 + 2 × 6 = 36."], "36 feet of fence"),
    [Problem("5 yd = ___ in.", "180"), Problem("Area of 14 m × 9 m", "126 sq m"), Problem("2 hr 45 min = ___ min", "165")],
    [S("Warm-Up", [Problem("72 ÷ 6", "12"), Problem("3 × 12", "36")]),
     S("Practice", [Problem("P and A of 15 cm × 8 cm", "P = 46 cm, A = 120 sq cm"), Problem("P = 44 ft, l = 14 ft. Find w.", "8 ft"), Problem("3 gal = ___ c", "48"),
                    Problem("4 kg 250 g = ___ g", "4,250"), Problem("8:50 a.m. to 11:25 a.m.", "2 hr 35 min"), Problem("6 lb = ___ oz", "96")]),
     S("Exit Ticket", [Problem("A room is 11 ft × 9 ft. Tiles are 1 sq ft and cost $4 each. Total cost?", "$396", space=30, wide=True)], cols=1)],
    "Use formulas and conversion facts; convert first, then compute.")

L15 = RL("10.15", "Review: Data and Line Plots", "I can make and use line plots with fractions.", "4.MD.4",
    "Five friends' jump distances in feet: 4½, 5, 4¾, 5, 4½. Make a line plot. What is the difference between the longest and shortest jumps?".replace("4½", MX(4, 1, 2)).replace("4¾", MX(4, 3, 4)),
    "Each X is one data value. Use fraction operations to answer questions.",
    Example("Read a line plot", "Longest − shortest", [f"5 − {MX(4, 1, 2)} = {F(1, 2)}."], F(1, 2) + " foot"),
    [Problem("How many jumps were 5 feet?", "2"), Problem(f"Total of the {MX(4, 1, 2)}-foot jumps", "9 feet"), Problem("Most common distance(s)?", f"{MX(4, 1, 2)} and 5 ft (tie)")],
    [S("Warm-Up", [Problem(f"2 × {MX(4, 1, 2)}", "9"), Problem(f"5 − {MX(4, 3, 4)}", F(1, 4))]),
     S("Use the line plot", [Problem("How many plants were measured?", "8", fig=lambda t: line_plot(t, [Fr(1, 4), Fr(1, 2), Fr(1, 2), Fr(3, 4), Fr(3, 4), Fr(3, 4), Fr(1), Fr(1)], 0, 1, 4, width=W - 40, title="Plant growth (inches)"), space=20, wide=True),
                             Problem("Difference between greatest and least growth?", F(3, 4) + " inch", space=24, wide=True),
                             Problem(f"Total growth of the {F(3, 4)}-inch plants?", MX(2, 1, 4) + " inches", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Collect 6 measurements at home (to the nearest ¼ inch) and make a line plot.".replace("¼", F(1, 4)), "Answers vary.", space=80, wide=True)], cols=1)],
    "Line plots show measurement data; use fraction operations to answer questions.")

L16 = RL("10.16", "Celebrating a Year of Math", "I can show what I learned in Grade 4 math and set goals for Grade 5.", "Grade 4 review",
    "Look back at Lesson 1.1. What can you do now that you couldn't do then?",
    "You learned place value to one million, all four operations with big numbers, fractions, decimals, geometry, and measurement.",
    Example("Teach it back", "Choose your favorite lesson and teach it to someone at home.", ["Pick a lesson.", "Explain the Key Idea.", "Work one example together."], "Answers vary"),
    [Problem("Name one thing you learned in each unit.", "Answers vary."), Problem("What was the hardest unit? What helped you?", "Answers vary."), Problem("Set one math goal for Grade 5.", "Answers vary.")],
    [S("My year in math", [Problem("The math I'm proudest of this year:", "Answers vary.", lines=3, space=0, wide=True), Problem("Something I still want to practice:", "Answers vary.", lines=2, space=0, wide=True),
                           Problem("My math goal for Grade 5:", "Answers vary.", lines=2, space=0, wide=True)], cols=1),
     S("Final challenge", [Problem("Create a math poster or game that uses at least three skills from this year.", "Project; use the rubric in the Teacher Edition.", space=100, wide=True)], cols=1)],
    "You can do a lot of math now. Keep practicing and keep asking “why?”")
L16.teacher = TE("Students reflect on the year and set goals.", "Cumulative review.", "Poster paper, markers, workbook Lesson 10.16",
    flow("Favorite math fact from the year.", "Read Let's Explore. Look at Lesson 1.1 together.", ["Student chooses a lesson to teach back to you or a sibling."], "Fill out ‘My year in math’.", "Final challenge project.", "Celebrate!"),
    [], ["Offer a list of unit titles to choose from."], ["Make a video teaching a lesson."])

C1 = Check("Weekly Check 24: Whole Numbers", [S("Show what you know", [Problem("Round 649,512 to the nearest ten thousand.", "650,000"), Problem("37,485 + 48,697", "86,182"),
    Problem("60,000 − 23,758", "36,242"), Problem("8 × 3,047", "24,376"), Problem("53 × 26", "1,378"), Problem("2,346 ÷ 6", "391")])], minutes=20)
C2 = Check("Weekly Check 25: Factors, Patterns, and Problems", [S("Show what you know", [Problem("Factors of 45", "1, 3, 5, 9, 15, 45"), Problem("Prime or composite: 87", "composite (3 × 29)"),
    Problem("Rule: start at 4, add 7. Fifth term?", "32"), Problem("Is 234 divisible by 9?", "Yes"),
    Problem("100 students ride buses of 24. How many buses?", "5 buses"), Problem("$100 − 4 × $18", "$28")])], minutes=20)
C3 = Check("Weekly Check 26: Fractions and Decimals", [S("Show what you know", [Problem(f"Simplify {F(12, 16)}", F(3, 4)), Problem(f"{F(3, 5)} ◯ {F(5, 8)}", "<"),
    Problem(f"{MX(3, 1, 4)} − {MX(1, 3, 4)}", MX(1, 2, 4)), Problem(f"6 × {F(3, 4)}", MX(4, 2, 4)), Problem(f"{F(6, 10)} + {F(25, 100)}", F(85, 100)), Problem("0.7 ◯ 0.65", ">")])], minutes=20)

REVIEW = Check("Year-End Review", [
    S("Numbers and operations", [Problem("Write 504,060 in words.", words(504060), lines=2, space=0, wide=True), Problem("Round 87,652 to the nearest thousand.", "88,000"),
                                 Problem("45,089 + 37,946", "83,035", space=30), Problem("7 × 4,086", "28,602", space=30), Problem("3,725 ÷ 5", "745", space=40)]),
    S("Fractions and decimals", [Problem(f"{F(2, 3)} = {F('?', 15)}", "10"), Problem(f"{MX(4, 2, 5)} + {MX(2, 4, 5)}", MX(7, 1, 5)), Problem(f"3 × {F(5, 8)}", MX(1, 7, 8)), Problem("Order: 0.6, 0.06, 0.66", "0.06, 0.6, 0.66")]),
    S("Geometry and measurement", [Problem("Right angle split into 38° and x", "52°"), Problem("P and A of 13 ft × 7 ft", "P = 40 ft, A = 91 sq ft"), Problem("4 ft 7 in. = ___ in.", "55"), Problem("9:25 a.m. to 1:10 p.m.", "3 hr 45 min")])],
    kind="review", minutes=45, teacher_note="Use over two days if needed. Any section with more than one mistake shows what to review before the Year-End Test.")

TEST = Check("Grade 4 Year-End Test", [
    S("Part A · Whole numbers (1 point each)", [Problem("Value of the 7 in 372,815", "70,000"), Problem("Round 465,382 to the nearest hundred thousand.", "500,000"),
        Problem("Compare: 81,409 ◯ 81,490", "<"), Problem("63,507 + 28,896", "92,403"), Problem("50,000 − 17,284", "32,716"), Problem("6 × 2,309", "13,854"),
        Problem("47 × 32", "1,504"), Problem("1,856 ÷ 8", "232"), Problem("703 ÷ 6", "117 R1"), Problem("Factors of 28", "1, 2, 4, 7, 14, 28")]),
    S("Part B · Fractions and decimals (1 point each)", [Problem(f"{F(3, 4)} = {F('?', 12)}", "9"), Problem(f"Simplify {F(15, 18)}", F(5, 6)), Problem(f"{F(5, 6)} ◯ {F(3, 4)}", ">"),
        Problem(f"{MX(2, 3, 8)} + {MX(3, 7, 8)}", MX(6, 2, 8)), Problem(f"{MX(5, 1, 3)} − {MX(2, 2, 3)}", MX(2, 2, 3)), Problem(f"4 × {F(2, 5)}", MX(1, 3, 5)),
        Problem(f"{F(43, 100)} as a decimal", "0.43"), Problem("0.8 ◯ 0.79", ">")]),
    S("Part C · Geometry and measurement (1 point each)", [Problem("Classify a 135° angle.", "obtuse"), Problem("Straight angle split into 72° and x", "108°"),
        Problem("Lines of symmetry in a square", "4"), Problem("P and A of 9 m × 6 m", "P = 30 m, A = 54 sq m"), Problem("5 lb = ___ oz", "80"), Problem("3 m = ___ cm", "300")]),
    S("Part D · Problem solving (3 points each)", [
        Problem("A school orders 24 boxes of 36 pencils. It gives 150 pencils to each of 5 classes. How many pencils are left?", "114 pencils (864 − 750)", space=80, wide=True, points=3),
        Problem(f"Ellie walks {F(3, 4)} mile each day for 5 days. Lillie walks {MX(3, 1, 2)} miles in all. Who walks farther, and by how much?", f"Ellie, by {F(1, 4)} mile ({MX(3, 3, 4)} vs {MX(3, 1, 2)})", space=80, wide=True, points=3),
        Problem("A rectangular pool is 18 ft by 12 ft. A fence goes around it 3 ft away on every side. How long is the fence?", "84 ft (the fence makes a 24 ft × 18 ft rectangle)", space=80, wide=True, points=3)], cols=1)],
    kind="test", minutes=60, teacher_note="Allow about 60 minutes (or split over two sittings). No calculator.",
    rubric=[["28–33 (85%+)", "Ready for Grade 5 math."], ["23–27", "Ready; review missed topics over the summer."], ["Below 23", "Spend a few weeks reviewing weak units before Grade 5."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-06-21", "2027-06-28", "2027-07-05", "2027-07-12"], CHECKS, REVIEW, TEST)

UNIT = Unit(10, "Year in Review", "Pulling the whole year together: numbers, operations, fractions, decimals, geometry, and measurement.",
    "In the last four weeks you will review every big idea from Grade 4, practice the skills that need it most, and show what you have learned on the Year-End Test.",
    ["Review place value and all four operations.", "Review factors, multiples, and patterns.", "Review fractions and decimals.", "Review geometry, measurement, and data.", "Show your learning on the Year-End Test."],
    [("4.OA, 4.NBT", "Operations and Algebraic Thinking; Number and Operations in Base Ten (review)."), ("4.NF", "Number and Operations—Fractions (review)."), ("4.MD, 4.G", "Measurement and Data; Geometry (review).")],
    [("review", "To study again so you remember."), ("strategy", "A plan for solving a problem.")],
    ["Units 1–9."], ["All materials from the year", "Unit Study Guides in the textbook"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Everything you learned this year is a tool you will use in Grade 5 and in real life.",
    family_note="Use each unit's test results to choose what to reteach during review weeks. Celebrate the year!",
    weeks=WEEKS)
