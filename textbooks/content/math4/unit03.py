"""Grade 4 Math · Unit 3: Division (Dec 14, 2026 – Jan 8, 2027)."""
from engine import *
from content.mathkit import c
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def qr(a, b):
    q, r = divmod(a, b)
    return f"{c(q)}" + (f" R{r}" if r else "")


def D(a, b, space=80):
    return Problem(f"{c(a)} ÷ {b}", qr(a, b), space=space, fig=lambda t: long_div(t, a, b, show_answer=False))


def Dans(a, b):
    return lambda t: long_div(t, a, b, show_answer=True)


L1 = Lesson("3.1", "What Division Means",
    "I can explain division as sharing equally or making equal groups, and use multiplication facts to divide.",
    "4.OA.2, 4.NBT.6",
    [("dividend", "The number being divided."), ("divisor", "The number you divide by."), ("quotient", "The answer to a division problem."),
     ("fact family", "Related multiplication and division facts, like 6 × 4 = 24, 4 × 6 = 24, 24 ÷ 4 = 6, 24 ÷ 6 = 4.")],
    "Grandma baked 24 cookies for 4 grandchildren. How many cookies does each child get if she shares them fairly?",
    [Text("Division answers two kinds of questions. <b>Sharing:</b> 24 cookies shared by 4 children, how many each? "
          "<b>Grouping:</b> 24 cookies put in bags of 4, how many bags? Both are 24 ÷ 4 = 6."),
     Figure(lambda t: dot_groups(t, 4, 6, width=320), "24 shared into 4 equal groups: 6 in each group."),
     Text("Division is the opposite of multiplication. If you know 4 × 6 = 24, you know 24 ÷ 4 = 6 and 24 ÷ 6 = 4."),
     Figure(lambda t: table(t, [["Dividend", "÷", "Divisor", "=", "Quotient"], ["24", "÷", "4", "=", "6"]], [1.2 * inch, 0.4 * inch, 1.1 * inch, 0.4 * inch, 1.2 * inch], width=4.3 * inch)),
     Example("Use a fact family", "Find 56 ÷ 7.", ["Think: 7 × ? = 56.", "7 × 8 = 56."], "8"),
     KeyIdea("To divide, think of the related multiplication fact: 56 ÷ 7 = ? is the same as 7 × ? = 56.")],
    [Problem("36 ÷ 9", "4"), Problem("Write the fact family for 5, 8, and 40.", "5 × 8 = 40, 8 × 5 = 40, 40 ÷ 5 = 8, 40 ÷ 8 = 5"),
     Problem("42 apples go in bags of 6. How many bags?", "7 bags")],
    [S("Warm-Up", [Problem("6 × 9", "54"), Problem("7 × ___ = 49", "7")]),
     S("Divide", [Problem(f"{a} ÷ {b}", str(a // b)) for a, b in [(18, 3), (45, 5), (63, 9), (32, 4), (72, 8), (49, 7), (54, 6), (81, 9)]]),
     S("Fact families", [Problem("Write the fact family for 6, 7, 42.", "6 × 7 = 42, 7 × 6 = 42, 42 ÷ 6 = 7, 42 ÷ 7 = 6", lines=2, space=0),
                         Problem("Write the fact family for 3, 9, 27.", "3 × 9 = 27, 9 × 3 = 27, 27 ÷ 3 = 9, 27 ÷ 9 = 3", lines=2, space=0)]),
     S("Solve", [Problem("35 crayons are shared by 5 friends. How many crayons does each friend get?", "7 crayons", space=40),
                 Problem("48 chairs are put in rows of 8. How many rows?", "6 rows", space=40)]),
     S("Exit Ticket", [Problem("Write a sharing story and a grouping story for 30 ÷ 6.", "Answers vary; quotient 5.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students understand division as sharing and grouping and use fact families.", "Find whole-number quotients using strategies based on the relationship between multiplication and division.",
       "24 counters or cookies, cups or paper plates, workbook Lesson 3.1",
       flow("6 × 9 and 7 × ? = 49.", "Read Let's Explore; share 24 counters onto 4 plates.",
            ["Act out both meanings: sharing (4 plates) and grouping (bags of 4).", "Say: Division undoes multiplication.", "Introduce dividend, divisor, quotient."], "Try It 1–3."),
       ["Thinking division always means sharing.", "Mixing up the dividend and divisor."], ["Use counters for every problem."], ["Why can't you divide 24 cookies among 0 children?"]),
    summary="Division shares or groups equally. Use the related multiplication fact to divide.")

L2 = Lesson("3.2", "Dividing Multiples of 10, 100, and 1,000",
    "I can use basic facts and place value to divide numbers like 2,400 ÷ 6.",
    "4.NBT.6",
    [],
    "A school has 2,400 pencils to share equally among 6 classrooms. How many pencils does each room get?",
    [Text("Use a basic fact and think about the unit. 2,400 is 24 hundreds. 24 hundreds ÷ 6 = 4 hundreds = 400."),
     Figure(lambda t: table(t, [["Basic fact", "Tens", "Hundreds", "Thousands"], ["24 ÷ 6 = 4", "240 ÷ 6 = 40", "2,400 ÷ 6 = 400", "24,000 ÷ 6 = 4,000"]],
                            [1.4 * inch, 1.4 * inch, 1.6 * inch, 1.9 * inch], width=6.3 * inch)),
     Example("Think in units", "Find 3,500 ÷ 7.", ["3,500 = 35 hundreds.", "35 ÷ 7 = 5, so 35 hundreds ÷ 7 = 5 hundreds."], "500"),
     WatchOut("Check by multiplying: 7 × 500 = 3,500. If you get a different number, recount the zeros."),
     KeyIdea("Name the dividend in tens, hundreds, or thousands, use the basic fact, then rename the quotient.")],
    [Problem("320 ÷ 4", "80"), Problem("4,500 ÷ 9", "500"), Problem("6,000 ÷ 3", "2,000")],
    [S("Warm-Up", [Problem("48 ÷ 8", "6"), Problem("How many hundreds are in 3,600?", "36")]),
     S("Divide", [Problem(f"{c(a)} ÷ {b}", c(a // b)) for a, b in [(80, 4), (150, 5), (210, 7), (640, 8), (1200, 3), (2800, 4), (5400, 9), (3000, 5), (48000, 6), (35000, 7)]]),
     S("Solve", [Problem("A farm packs 1,800 eggs equally into 6 crates. How many eggs are in each crate?", "300 eggs", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain how 42 ÷ 7 helps you find 4,200 ÷ 7.", "4,200 is 42 hundreds; 42 ÷ 7 = 6, so 6 hundreds = 600.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students divide multiples of 10, 100, and 1,000 by one-digit numbers.", "Find quotients using strategies based on place value.",
       "Base-ten blocks, workbook Lesson 3.2",
       flow("48 ÷ 8; hundreds in 3,600.", "Read Let's Explore.", ["Show 24 flats shared into 6 groups (4 flats each).", "Say: Name the unit, divide the fact, name the unit again.", "Work the example."], "Try It 1–3."),
       ["Dropping or adding zeros."], ["Check every answer by multiplying."], ["Find 36,000 ÷ 40 (preview)."]),
    summary="Use the basic fact and the unit: 2,400 ÷ 6 = 24 hundreds ÷ 6 = 4 hundreds = 400.")

L3 = Lesson("3.3", "Dividing with Area Models",
    "I can use an area model to divide a two- or three-digit number by a one-digit number.",
    "4.NBT.6",
    [],
    "A rectangle has an area of 84 square feet. One side is 4 feet long. How long is the other side?",
    [Text("Division can be pictured as a rectangle where you know the <b>area</b> (the dividend) and one side (the divisor). The missing side is the quotient."),
     Figure(lambda t: area_model(t, 21, 4, width=300), "84 ÷ 4: 80 ÷ 4 = 20 and 4 ÷ 4 = 1, so the side is 20 + 1 = 21."),
     Example("Split the dividend into friendly parts", "Find 84 ÷ 4.", ["Split 84 into 80 + 4, numbers that are easy to divide by 4.", "80 ÷ 4 = 20.", "4 ÷ 4 = 1.", "Add: 20 + 1 = 21."], "21"),
     Example("Three digits", "Find 315 ÷ 5.", ["Split 315 into 300 + 15.", "300 ÷ 5 = 60.", "15 ÷ 5 = 3.", "60 + 3 = 63."], "63",
             fig=lambda t: area_model(t, 63, 5, width=300)),
     KeyIdea("Break the dividend into parts that are easy to divide (multiples of the divisor). Divide each part, then add the answers.")],
    [Problem("96 ÷ 3", "32"), Problem("78 ÷ 6", "13"), Problem("426 ÷ 6", "71")],
    [S("Warm-Up", [Problem("90 ÷ 3", "30"), Problem("6 × 40", "240")]),
     S("Use an area model to divide", [Problem(f"{a} ÷ {b}", str(a // b), space=60) for a, b in [(68, 2), (93, 3), (85, 5), (72, 4), (256, 8), (434, 7)]]),
     S("Solve", [Problem("A garden has an area of 96 square yards. It is 8 yards wide. How long is it?", "12 yards", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Use an area model to find 252 ÷ 6.", "42 (240 ÷ 6 = 40, 12 ÷ 6 = 2)", space=60, wide=True)], cols=1)],
    TE("Students divide using area models and the distributive property.", "Find whole-number quotients up to four-digit dividends and one-digit divisors using place value strategies and area models.",
       "Grid paper, workbook Lesson 3.3",
       flow("90 ÷ 3 and 6 × 40.", "Read Let's Explore. Draw the rectangle with the unknown side.",
            ["Work Example 1. Say: Find a big friendly piece of the dividend first.", "Work Example 2 (three digits)."], "Try It 1–3."),
       ["Splitting the dividend into parts that are not divisible by the divisor (e.g., 84 = 70 + 14 for ÷ 4)."], ["Use multiples tables (4, 8, 12, … 40, 80) as a reference."], ["Find 1,248 ÷ 4 with an area model."]),
    summary="Split the dividend into friendly parts, divide each part, and add the quotients.")

L4 = Lesson("3.4", "Partial Quotients",
    "I can divide using partial quotients and check my answer with multiplication.",
    "4.NBT.6",
    [("partial quotients", "A way to divide by subtracting easy multiples of the divisor and adding up how many groups you took away.")],
    "There are 156 students going on a field trip. Each van holds 6 students. How many vans are needed?",
    [Text("With <b>partial quotients</b>, you take away big, easy groups first, then smaller groups, until nothing (or a little) is left."),
     Example("Partial quotients", "Find 156 ÷ 6.",
             ["Take away 10 groups of 6: 156 − 60 = 96. (10)", "Take away 10 more groups: 96 − 60 = 36. (10)",
              "Take away 6 groups: 36 − 36 = 0. (6)", "Add the groups: 10 + 10 + 6 = 26.", "Check: 26 × 6 = 156. ✓"], "26 vans"),
     Figure(lambda t: table(t, [["Left to divide", "Subtract", "Groups of 6"], ["156", "− 60 (10 × 6)", "10"], ["96", "− 60 (10 × 6)", "10"], ["36", "− 36 (6 × 6)", "6"], ["0", "", "Total: 26"]],
                            [1.6 * inch, 2.0 * inch, 1.6 * inch], width=5.2 * inch)),
     KeyIdea("Any easy multiple works: 10 groups, 20 groups, 5 groups. Different students may take different steps and still get the same quotient.")],
    [Problem("144 ÷ 4", "36"), Problem("215 ÷ 5", "43"), Problem("738 ÷ 9", "82")],
    [S("Warm-Up", [Problem("10 × 7", "70"), Problem("20 × 8", "160")]),
     S("Divide using partial quotients", [Problem(f"{a} ÷ {b}", str(a // b), space=80) for a, b in [(84, 3), (132, 4), (195, 5), (378, 7), (504, 8), (846, 9)]]),
     S("Exit Ticket", [Problem("Divide 288 ÷ 6 with partial quotients. Check by multiplying.", "48; 48 × 6 = 288", space=70, wide=True)], cols=1)],
    TE("Students divide 3-digit numbers by 1-digit numbers using partial quotients.", "Find whole-number quotients using strategies based on place value and the relationship between multiplication and division.",
       "Workbook Lesson 3.4, a multiples chart (×10, ×20, ×5)",
       flow("10 × 7 and 20 × 8.", "Read Let's Explore.", ["Work the example in the table. Say: Take away big easy groups first.", "Show a second way (20 groups first) to get the same answer."], "Try It 1–3."),
       ["Subtracting a multiple bigger than what is left."], ["Write a ‘menu’ of easy multiples first (10×, 20×, 5×, 2×)."], ["Divide 1,512 ÷ 6 with partial quotients."]),
    summary="Subtract easy multiples of the divisor, keep track of the groups, and add them up. Check by multiplying.")

L5 = Lesson("3.5", "Understanding Remainders",
    "I can find a quotient with a remainder and explain what the remainder means.",
    "4.NBT.6",
    [("remainder", "The amount left over when a number cannot be divided evenly.")],
    "Ellie has 26 stickers to share equally among 4 friends. How many does each friend get? Are any left?",
    [Text("Sometimes the groups come out even and sometimes there are some left over. The leftover amount is the <b>remainder</b>."),
     Figure(lambda t: dot_groups(t, 4, 6, width=320), "26 ÷ 4: each friend gets 6 (24 stickers), and 2 are left."),
     Example("Write a remainder", "Find 26 ÷ 4.", ["4 × 6 = 24, the closest product that is not too big.", "26 − 24 = 2 left over.", "Write the answer as 6 R2."], "6 R2"),
     WatchOut("The remainder must always be <b>less than the divisor</b>. If you have 5 left when dividing by 4, you can make another group!"),
     Example("Check a remainder", "Check 47 ÷ 5 = 9 R2.", ["Multiply: 9 × 5 = 45.", "Add the remainder: 45 + 2 = 47. ✓"], "Correct"),
     KeyIdea("Quotient × divisor + remainder = dividend.")],
    [Problem("17 ÷ 3", "5 R2"), Problem("38 ÷ 6", "6 R2"), Problem("50 ÷ 7", "7 R1")],
    [S("Warm-Up", [Problem("7 × 6", "42"), Problem("45 − 42", "3")]),
     S("Divide. Write any remainder.", [Problem(f"{a} ÷ {b}", qr(a, b)) for a, b in [(13, 2), (23, 5), (31, 4), (44, 6), (58, 8), (67, 9), (40, 7), (29, 3)]]),
     S("Check the answer", [Problem("Is 53 ÷ 6 = 8 R5 correct? Show how you checked.", "Yes: 8 × 6 = 48, 48 + 5 = 53", lines=2, space=0),
                            Problem("Is 35 ÷ 4 = 7 R7 correct? Explain.", "No. The remainder 7 is bigger than 4. 35 ÷ 4 = 8 R3.", lines=2, space=0)]),
     S("Exit Ticket", [Problem("Find 61 ÷ 8 and check your answer.", "7 R5; 7 × 8 + 5 = 61", space=40, wide=True)], cols=1)],
    TE("Students find quotients with remainders and check them.", "Find whole-number quotients and remainders.", "Counters, workbook Lesson 3.5",
       flow("7 × 6; 45 − 42.", "Read Let's Explore. Act it out with 26 counters.", ["Work Example 1. Say: Make as many full groups as you can; what's left is the remainder.", "Read the Watch Out. Work Example 2."], "Try It 1–3."),
       ["A remainder that is bigger than the divisor."], ["Use counters."], ["Find a number that leaves remainder 1 when divided by 2, 3, and 4. (13, 25, …)"]),
    summary="The remainder is what is left over. It must be less than the divisor. Check: quotient × divisor + remainder = dividend.")

L6 = Lesson("3.6", "Dividing Larger Numbers",
    "I can divide up to four-digit numbers by one-digit numbers using place value, step by step.",
    "4.NBT.6",
    [("long division", "Dividing one place at a time from left to right: divide, multiply, subtract, bring down.")],
    "A charity has $1,236 to split equally among 4 families. How much does each family get?",
    [Text("<b>Long division</b> divides one place at a time, starting at the greatest place. Repeat four steps: <b>divide, multiply, subtract, bring down</b>."),
     Example("Long division", "Find 1,236 ÷ 4.",
             ["1 thousand ÷ 4: not enough. Use 12 hundreds instead. 12 ÷ 4 = 3. Write 3 over the hundreds. 3 × 4 = 12, 12 − 12 = 0.",
              "Bring down the 3 tens. 3 ÷ 4 = 0. Write 0 over the tens. 0 × 4 = 0, 3 − 0 = 3.",
              "Bring down the 6 ones: 36. 36 ÷ 4 = 9. Write 9 over the ones. 9 × 4 = 36, 36 − 36 = 0.",
              "Check: 309 × 4 = 1,236. ✓"], "$309", fig=Dans(1236, 4)),
     WatchOut("When a place cannot be divided (like 3 ÷ 4), write a <b>0</b> in the quotient. Skipping it would give 39, which is far too small."),
     KeyIdea("Divide, multiply, subtract, bring down. Repeat until every digit has been brought down.")],
    [Problem("846 ÷ 2", "423"), Problem("1,575 ÷ 5", "315"), Problem("2,418 ÷ 6", "403")],
    [S("Warm-Up", [Problem("36 ÷ 4", "9"), Problem("Is 2,400 ÷ 6 = 40 or 400?", "400")]),
     S("Divide", [D(a, b) for a, b in [(368, 2), (645, 3), (928, 4), (1715, 5), (3612, 6), (2856, 7), (4096, 8), (7254, 9)]]),
     S("Exit Ticket", [D(2128, 7)], cols=1)],
    TE("Students divide up to 4-digit numbers by 1-digit numbers with long division.", "Find whole-number quotients with up to four-digit dividends and one-digit divisors.",
       "Grid paper, workbook Lesson 3.6, “Divide, Multiply, Subtract, Bring down” card",
       flow("36 ÷ 4; 2,400 ÷ 6.", "Read Let's Explore; estimate first (1,200 ÷ 4 = 300).",
            ["Work the example on grid paper, one digit per box.", "Say: Divide, multiply, subtract, bring down.", "Point out the zero in the quotient."], "Try It 1–3."),
       ["Forgetting zeros in the quotient.", "Misaligning digits."], ["Grid paper; estimate first so a missing zero is noticed.", "Partial quotients are always allowed."], ["Divide 9,999 ÷ 9 and 9,990 ÷ 9."]),
    summary="Long division: divide, multiply, subtract, bring down. Write 0 when a place can't be divided.")

L7 = Lesson("3.7", "What Do I Do With the Remainder?",
    "I can decide what a remainder means in a word problem.",
    "4.OA.3",
    [("interpret", "To explain what something means.")],
    "27 people are going to the zoo. Each car holds 4 people. How many cars do they need?",
    [Text("27 ÷ 4 = 6 R3. But the answer is not “6 R3 cars”! The remainder means something different in different stories."),
     Figure(lambda t: table(t, [["What to do with the remainder", "Example (27 ÷ 4 = 6 R3)", "Answer"],
                                ["Round up: everyone needs a spot", "Cars for 27 people, 4 per car", "7 cars"],
                                ["Drop it: only full groups count", "Bags of 4 apples from 27 apples", "6 full bags"],
                                ["The remainder is the answer", "Apples left after making bags of 4", "3 apples"]],
                            [2.2 * inch, 2.4 * inch, 1.1 * inch], width=5.7 * inch)),
     Example("Round up", "A teacher has 75 students. Each table seats 8. How many tables?", ["75 ÷ 8 = 9 R3.", "3 students still need seats, so add a table."], "10 tables"),
     KeyIdea("Always ask: what does the remainder mean in this story?")],
    [Problem("50 photos go in an album, 6 per page. How many pages are needed?", "9 pages"),
     Problem("50 crayons go in boxes of 6. How many full boxes?", "8 full boxes"), Problem("50 crayons in boxes of 6. How many crayons are left over?", "2 crayons")],
    [S("Warm-Up", [Problem("38 ÷ 5", "7 R3"), Problem("62 ÷ 7", "8 R6")]),
     S("Solve. Explain what you did with the remainder.", [
         Problem("A boat holds 6 people. 39 people want to ride. How many trips?", "7 trips (39 ÷ 6 = 6 R3; round up)", space=50),
         Problem("Ribbons are cut into 8-inch pieces from 70 inches. How many full pieces?", "8 pieces (70 ÷ 8 = 8 R6; drop)", space=50),
         Problem("A baker fills boxes of 6 muffins from 100 muffins. How many muffins are left out of boxes?", "4 muffins (100 ÷ 6 = 16 R4; the remainder is the answer)", space=50),
         Problem("4 friends share $30 equally. How much does each get, and how much is left?", "$7 each, $2 left (30 ÷ 4 = 7 R2)", space=50)]),
     S("Exit Ticket", [Problem("Write a story for 45 ÷ 7 where the answer is 7.", "Example: 45 people, 7 per van; 7 vans needed.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students interpret remainders in context.", "Solve multistep word problems with whole-number answers, including problems in which remainders must be interpreted.",
       "Counters, workbook Lesson 3.7",
       flow("38 ÷ 5; 62 ÷ 7.", "Read Let's Explore. Ask: Can we have 6 R3 cars?", ["Discuss the three remainder cases using the table.", "Work the example (round up)."], "Try It 1–3."),
       ["Writing remainders in answers to story problems without thinking about them."], ["Act out each story with counters."], ["Write one story for each kind of remainder."]),
    summary="Round up, drop it, or use it as the answer: the story tells you what a remainder means.")

L8 = Lesson("3.8", "Division Problem Solving",
    "I can solve word problems with division and check my answers with multiplication.",
    "4.OA.3, 4.NBT.6",
    [],
    "A family drives 1,248 miles in 4 days, the same distance each day. How far do they drive each day?",
    [Text("Look for clues for division: <b>shared equally</b>, <b>each</b>, <b>per</b>, <b>how many groups</b>."),
     Example("Equal sharing", "1,248 miles in 4 equal days.", ["1,248 ÷ 4 = 312.", "Check: 312 × 4 = 1,248."], "312 miles each day"),
     Example("Two steps", "A class earns $96 at a bake sale and $120 at a car wash. They split the money equally among 6 field-trip groups. How much per group?",
             ["Add: 96 + 120 = 216.", "Divide: 216 ÷ 6 = 36."], "$36"),
     KeyIdea("Multiply to check every division answer.")],
    [Problem("A rope 96 feet long is cut into 8 equal pieces. How long is each piece?", "12 feet"),
     Problem("There are 365 days in a year. About how many weeks is that? (7 days in a week)", "52 weeks and 1 day (52 R1)"),
     Problem("Mom buys 3 packs of 12 water bottles and splits them among 4 coolers. How many per cooler?", "9 bottles")],
    [S("Warm-Up", [Problem("720 ÷ 8", "90"), Problem("91 ÷ 7", "13")]),
     S("Solve", [
         Problem("A school collected 1,530 cans and packed them equally into 5 boxes. How many cans in each box?", "306 cans", space=60, wide=True),
         Problem("Dad has 250 tomato plants. He plants them in rows of 9. How many full rows? How many plants are left?", "27 full rows, 7 left", space=60, wide=True),
         Problem("A pack of 8 juice boxes costs $4. How many packs are needed for 60 kids?", "8 packs (60 ÷ 8 = 7 R4; round up)", space=60, wide=True),
         Problem("Lillie read 156 pages in 6 days and Ellie read 112 pages in 4 days. Who read more pages each day?", "Ellie: 28 per day vs Lillie 26 per day", space=60, wide=True)], cols=1),
     S("Exit Ticket", [Problem("2,184 ÷ 6. Check with multiplication.", "364; 364 × 6 = 2,184", space=60, wide=True)], cols=1)],
    TE("Students solve one- and two-step division problems.", "Solve multistep word problems with whole numbers, including interpreting remainders.", "Workbook Lesson 3.8",
       flow("720 ÷ 8; 91 ÷ 7.", "Read Let's Explore.", ["Work both examples. Say: Check every division with multiplication."], "Try It 1–3.", "Workbook Lesson 3.8 and the Unit 3 Review.", "Check. Tomorrow: Unit 3 Test."),
       ["Choosing division when a problem needs multiplication."], ["Draw a bar model."], ["Plan equal shares for a real family trip budget."]),
    summary="Look for equal sharing or equal groups. Divide, interpret any remainder, and check by multiplying.")

CHECK1 = Check("Weekly Check 7: Dividing", [S("Show what you know", [
    Problem("63 ÷ 9", "7"), Problem("2,800 ÷ 7", "400"), Problem("Use an area model: 96 ÷ 4", "24", space=50),
    Problem("Partial quotients: 175 ÷ 5", "35", space=60), Problem("29 ÷ 6", "4 R5"), Problem("Is 42 ÷ 5 = 7 R7 correct? Explain.", "No; remainder must be < 5. 42 ÷ 5 = 8 R2.", lines=2, space=0)])], minutes=15)

REVIEW = Check("Unit 3 Review", [
    S("Facts and patterns", [Problem("54 ÷ 6", "9"), Problem("3,200 ÷ 8", "400"), Problem("Write the fact family for 4, 9, 36.", "4 × 9 = 36, 9 × 4 = 36, 36 ÷ 4 = 9, 36 ÷ 9 = 4", lines=2, space=0, wide=True)]),
    S("Divide", [D(84, 6), D(347, 5), D(1638, 7), D(4520, 8)]),
    S("Remainders in stories", [Problem("58 students ride in vans that hold 8. How many vans?", "8 vans", space=40),
                                Problem("58 cookies go in bags of 8. How many full bags?", "7 bags", space=40)])], kind="review", minutes=35,
    teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 3 Test", [
    S("Part A · Facts and patterns (1 point each)", [Problem("72 ÷ 8", "9"), Problem("4,500 ÷ 5", "900"), Problem("360 ÷ 6", "60"),
        Problem("Write a division fact related to 7 × 8 = 56.", "56 ÷ 7 = 8 or 56 ÷ 8 = 7")]),
    S("Part B · Divide (2 points each)", [D(96, 4), D(275, 6), D(1206, 3), D(3549, 7), D(5000, 8),
        Problem("Check 83 ÷ 9 = 9 R2 by multiplying. Is it correct?", "Yes: 9 × 9 = 81, 81 + 2 = 83", space=30, points=2)]),
    S("Part C · Word problems (3 points each)", [
        Problem("125 people are going to a game. Each van holds 9 people. How many vans are needed? Explain the remainder.", "14 vans (125 ÷ 9 = 13 R8; round up)", space=70, wide=True, points=3),
        Problem("A store has 3 boxes of 144 markers. It puts them into packs of 6. How many packs can it make?", "72 packs (432 ÷ 6)", space=70, wide=True, points=3)], cols=1)],
    kind="test", minutes=40, teacher_note="Allow about 40 minutes. Any correct method earns full credit if work is shown.",
    rubric=[["19–22 (85%+)", "Mastered."], ["16–18", "Proficient; correct missed items."], ["Below 16", "Reteach and retest."]])
for _p in TEST.sections[1].problems[:5]:
    _p.points = 2

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
CHECKS = [CHECK1]
WEEKS = schedule(LESSONS, ["2026-12-14", "2027-01-04"], CHECKS, REVIEW, TEST)

UNIT = Unit(3, "Division", "Sharing and grouping, dividing with place value, partial quotients, long division, and remainders.",
    "Division splits a total into equal groups. In this unit you will use multiplication facts and place value to divide numbers up to four digits by one-digit numbers, and decide what to do with leftovers.",
    ["Explain division as sharing and as grouping.", "Divide multiples of 10, 100, and 1,000.", "Divide with area models, partial quotients, and long division.",
     "Find and check remainders.", "Decide what a remainder means in a word problem."],
    [("4.NBT.6", "Find whole-number quotients and remainders with up to four-digit dividends and one-digit divisors, using strategies based on place value."),
     ("4.OA.2", "Multiply or divide to solve word problems involving multiplicative comparison."),
     ("4.OA.3", "Solve multistep word problems, including problems in which remainders must be interpreted.")],
    [("dividend", "The number being divided."), ("divisor", "The number you divide by."), ("quotient", "The answer to a division problem."), ("remainder", "The amount left over.")],
    ["Multiplication facts (fluent).", "Multiplying by one digit (Unit 2).", "Subtraction with regrouping (Unit 1)."],
    ["Counters (beans or buttons work)", "Paper plates or cups for sharing", "Grid paper", "Divide-Multiply-Subtract-Bring down card"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Division helps split a pizza fairly, plan how many cars a trip needs, and find how far to drive each day of a road trip.",
    family_note="Unit 3 spans winter break (Dec 21 – Jan 1). Over the break, practice division facts with cards for a few minutes on most days.",
    weeks=WEEKS)
