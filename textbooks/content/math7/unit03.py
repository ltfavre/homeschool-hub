"""Grade 7 Math · Unit 3: Adding and Subtracting Integers (Dec 14, 2026 – Jan 22, 2027)."""
from engine import *
from content.te import TE, flow
from content.sched import schedule

CW = 205
s = sgn


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def par(n):
    """Integer shown in an expression, parenthesized when negative."""
    return f"({s(n)})" if n < 0 else s(n)


def addp(a, b):
    return Problem(f"{s(a)} + {par(b)}", s(a + b))


def subp(a, b):
    return Problem(f"{s(a)} − {par(b)}", s(a - b))


def nl(lo, hi, pts=(), hops=(), w=None, h=62):
    return lambda t: number_line(t, lo, hi, 1, 1 if hi - lo <= 12 else 2, points=pts, hops=hops, fmt_fn=lambda v: s(int(v)), width=w or W * 0.9, height=h)


L1 = Lesson("3.1", "Integers, Opposites, and Absolute Value",
    "I can use integers to describe real situations and find opposites and absolute values.", "7.NS.1 (review of 6.NS.5–7)",
    [("integer", "A whole number or its opposite: …, −3, −2, −1, 0, 1, 2, 3, …"), ("opposites", "Two numbers the same distance from 0 on opposite sides, like 4 and −4."),
     ("absolute value", "A number's distance from 0, written |a|. |−7| = 7.")],
    "The temperature in Jackson is 5°F. In Fairbanks, Alaska, it is 5 degrees below zero. How would you write both temperatures?",
    [Text("<b>Integers</b> include negative numbers. Negative numbers describe values below zero: temperatures, elevations below sea level, money owed."),
     Figure(nl(-6, 6, pts=[(-5, "−5"), (5, "5")])),
     Text("5 and −5 are <b>opposites</b>: the same distance from 0 in opposite directions. Both have an <b>absolute value</b> of 5."),
     Example("Absolute value", "Find |−12| and |9|.", ["−12 is 12 units from 0.", "9 is 9 units from 0."], "12 and 9"),
     KeyIdea("Opposites have the same absolute value. Absolute value is a distance, so it is never negative.")],
    [Problem("Write an integer: a loss of 8 yards", "−8"), Problem("Opposite of −15", "15"), Problem("|−23|", "23")],
    [S("Warm-Up", [Problem("Which is colder: −3°F or −8°F?", "−8°F"), Problem("Name a number between −2 and 0.", "−1")]),
     S("Write an integer", [Problem("a deposit of $40", "40"), Problem("20 feet below sea level", "−20"), Problem("a temperature drop of 6 degrees", "−6"), Problem("a gain of 3 yards", "3")]),
     S("Find", [Problem("opposite of 31", "−31"), Problem("opposite of −4", "4"), Problem("|−18|", "18"), Problem("|0|", "0"), Problem("−|−6|", "−6"), Problem("|14| − |−5|", "9")]),
     S("Order from least to greatest", [Problem("3, −7, 0, −2, 5", "−7, −2, 0, 3, 5", wide=True)], cols=1),
     S("Exit Ticket", [Problem("Can absolute value be negative? Explain.", "No; it is a distance from 0.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students represent quantities with integers and find opposites and absolute values.", "Apply understanding of addition and subtraction to rational numbers; represent on a number line.", "Thermometer picture, workbook Lesson 3.1",
       flow("Colder temperature.", "Read Let's Explore.", ["Draw a vertical number line like a thermometer.", "Say: Opposites are mirror images across 0."], "Try It 1–3."),
       ["Thinking −8 > −3 because 8 > 3."], ["Vertical number line."], ["Find the lowest and highest places in Mississippi (elevation)."]),
    summary="Integers include negatives. Opposites are the same distance from 0; absolute value is that distance.")

L2 = Lesson("3.2", "Adding Integers with the Same Sign",
    "I can add two integers that have the same sign.", "7.NS.1b",
    [],
    "You owe your sister $4. Then you borrow $3 more. How much do you owe in all?",
    [Text("Owing $4 is −4. Owing $3 more is −3. Together: −4 + (−3) = −7. You owe $7."),
     Figure(lambda t: chips(t, 0, 7), "Seven negative chips: −7"),
     Figure(nl(-8, 2, pts=[(-7, "−7")], hops=[(0, -4, "−4"), (-4, -7, "−3")])),
     Example("Same sign", "−9 + (−6)", ["Both negative: add the absolute values, 9 + 6 = 15.", "Keep the sign: negative."], "−15"),
     KeyIdea("Same signs: add the absolute values and keep the common sign.")],
    [addp(-5, -8), addp(12, 9), addp(-20, -15)],
    [S("Warm-Up", [Problem("|−9| + |−6|", "15"), Problem("4 + 3", "7")]),
     S("Add", [addp(a, b) for a, b in [(-3, -4), (-11, -2), (6, 8), (-7, -7), (-15, -9), (-24, -36), (13, 27), (-50, -50)]]),
     S("Solve", [Problem("A diver is at −12 m and dives 8 m deeper. Where is she now?", "−20 m", space=24), Problem("The temperature is −5°F and drops 9 more degrees. New temperature?", "−14°F", space=24)]),
     S("Exit Ticket", [Problem("Use chips to show −4 + (−5). What is the sum?", "−9", space=40, wide=True)], cols=1)],
    TE("Students add integers with the same sign.", "Understand p + q as the number |q| from p in the direction indicated by the sign of q.", "Two-color counters (or paper chips), workbook Lesson 3.2",
       flow("Warm-up.", "Read Let's Explore.", ["Model with chips, then a number line.", "Say: Same sign? Add and keep the sign."], "Try It 1–3."),
       ["Making the sum of two negatives positive."], ["Chips."], ["Write a real story for −15 + (−25)."]),
    summary="Same signs: add absolute values, keep the sign.")

L3 = Lesson("3.3", "Adding Integers with Different Signs",
    "I can add two integers with different signs.", "7.NS.1b",
    [("zero pair", "A positive and a negative chip together; they cancel to 0.")],
    "You have $8. You spend $11. What is your balance?",
    [Text("Model 8 + (−11) with chips. Each positive cancels a negative to make a <b>zero pair</b>. After 8 zero pairs, 3 negative chips are left: −3."),
     Figure(lambda t: chips(t, 8, 11, zero_pairs=8, r=7), "8 zero pairs cancel; 3 negatives remain."),
     Figure(nl(-4, 9, pts=[(-3, "−3")], hops=[(0, 8, "+8"), (8, -3, "−11")])),
     Example("Different signs", "−14 + 9", ["Subtract absolute values: 14 − 9 = 5.", "Use the sign of the number with the larger absolute value: −14."], "−5"),
     KeyIdea("Different signs: subtract the absolute values and use the sign of the number farther from 0.")],
    [addp(7, -10), addp(-6, 15), addp(-25, 18)],
    [S("Warm-Up", [addp(-4, -5), Problem("14 − 9", "5")]),
     S("Add", [addp(a, b) for a, b in [(5, -2), (-5, 2), (9, -13), (-12, 20), (30, -45), (-17, 17), (-8, 3), (21, -6)]]),
     S("Solve", [Problem("Your account has $35. You buy a $52 game with an overdraft. Balance?", "−$17", space=24), Problem("A football team gains 6 yards, then loses 9. Total?", "−3 yards", space=24)]),
     S("Exit Ticket", [Problem("Explain why −7 + 7 = 0 using zero pairs.", "7 positives cancel 7 negatives; nothing is left.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students add integers with different signs.", "Understand p + q; describe situations in which opposite quantities combine to make 0.", "Two-color counters, workbook Lesson 3.3",
       flow("−4 + (−5).", "Read Let's Explore.", ["Chips with zero pairs; then number line.", "Say: Cancel, then see what's left."], "Try It 1–3."),
       ["Adding absolute values when signs differ."], ["Chips until confident."], ["Why does the bigger absolute value win the sign?"]),
    summary="Different signs: subtract absolute values; the sign of the farther-from-zero number wins.")

L4 = Lesson("3.4", "Additive Inverses",
    "I can explain why a number plus its opposite equals 0.", "7.NS.1a, 7.NS.1b",
    [("additive inverse", "A number's opposite. A number plus its additive inverse equals 0.")],
    "A hydrogen atom has 1 proton (+1 charge) and 1 electron (−1 charge). What is its total charge?",
    [Text("+1 + (−1) = 0. Opposites always add to 0. The opposite of a number is called its <b>additive inverse</b>."),
     Example("Use inverses", "−13 + 8 + 13", ["−13 and 13 are opposites: they make 0.", "0 + 8 = 8."], "8"),
     Example("Find the missing number", "−35 + ___ = 0", ["The additive inverse of −35 is 35."], "35"),
     KeyIdea("a + (−a) = 0 for every number a. Look for opposites to make 0 and simplify.")],
    [Problem("−42 + 42", "0"), Problem("6 + (−9) + 9", "6"), Problem("___ + 17 = 0", "−17")],
    [S("Warm-Up", [addp(-6, 6), addp(15, -15)]),
     S("Find the sum using inverses", [Problem("−7 + 12 + 7", "12"), Problem("25 + (−18) + (−25)", "−18"), Problem("−3 + 9 + (−9) + 3", "0"), Problem("40 + (−11) + (−40)", "−11")]),
     S("Missing number", [Problem("−8 + ___ = 0", "8"), Problem("___ + (−26) = 0", "26"), Problem("−5 + ___ = 2", "7"), Problem("14 + ___ = −1", "−15")]),
     S("Exit Ticket", [Problem("Describe a real situation where two opposite quantities combine to make 0.", "e.g. earn $20, spend $20", lines=2, space=0, wide=True)], cols=1)],
    TE("Students use additive inverses.", "Describe situations in which opposite quantities combine to make 0.", "Counters, workbook Lesson 3.4",
       flow("Warm-up.", "Read Let's Explore.", ["Work examples; look for opposite pairs."], "Try It 1–3. Weekly Check tomorrow."), ["Missing that −35 needs +35 (not −35)."], ["Chips."], ["Build a ‘zero’ from 5 different integers."]),
    summary="A number plus its opposite is 0.")

L5 = Lesson("3.5", "Adding Integers on a Number Line",
    "I can use a number line to add integers.", "7.NS.1b",
    [],
    "A hiker starts at 3 m above a lake, climbs down 7 m, then up 2 m. Where does she end?",
    [Text("Start at the first number. Move right for a positive addend and left for a negative addend."),
     Figure(nl(-5, 5, pts=[(-2, "−2")], hops=[(0, 3, "+3"), (3, -4, "−7"), (-4, -2, "+2")])),
     Example("Number line", "3 + (−7) + 2", ["Start at 0, move right 3 to 3.", "Move left 7 to −4.", "Move right 2 to −2."], "−2"),
     KeyIdea("Positive → right. Negative → left. The landing point is the sum.")],
    [Problem("−4 + 6 (use a number line)", "2"), Problem("2 + (−5) + (−1)", "−4"), Problem("−3 + (−3) + 8", "2")],
    [S("Warm-Up", [addp(-7, 4), addp(-2, -6)]),
     S("Use the number line", [Problem("−5 + 8", "3", fig=nl(-6, 6, w=CW, h=50), space=0), Problem("4 + (−9)", "−5", fig=nl(-6, 6, w=CW, h=50), space=0),
                               Problem("−1 + (−4) + 3", "−2", fig=nl(-6, 6, w=CW, h=50), space=0), Problem("6 + (−2) + (−7)", "−3", fig=nl(-6, 6, w=CW, h=50), space=0)]),
     S("Exit Ticket", [Problem("Draw a number line for −6 + 10 and give the sum.", "4", space=50, wide=True)], cols=1)],
    TE("Students add integers on a number line.", "Represent addition on a horizontal or vertical number line diagram.", "Floor number line (−10 to 10), workbook Lesson 3.5",
       flow("Warm-up.", "Read Let's Explore. Walk it on a floor number line.", ["Model hops; say ‘positive right, negative left’."], "Try It 1–3."), ["Starting at 0 for the second addend."], ["Floor walking."], ["Vertical number line problems (elevation)."]),
    summary="On a number line, positive moves right and negative moves left.")

L6 = Lesson("3.6", "Subtracting Integers",
    "I can subtract integers by adding the opposite.", "7.NS.1c",
    [],
    "What is 3 − (−5)? How can subtracting make a number bigger?",
    [Text("Subtracting a number is the same as <b>adding its opposite</b>: a − b = a + (−b). So 3 − (−5) = 3 + 5 = 8."),
     Text("With chips: start with 3 positives. To take away 5 negatives, first add 5 zero pairs (which doesn't change the value). Then remove the 5 negatives. 8 positives are left."),
     Figure(lambda t: chips(t, 8, 5, zero_pairs=5, r=7), "3 positives plus 5 zero pairs; remove the 5 negatives → 8."),
     Example("Add the opposite", "−6 − 4", ["−6 − 4 = −6 + (−4).", "Same signs: −10."], "−10"),
     Example("Subtract a negative", "−2 − (−9)", ["−2 − (−9) = −2 + 9 = 7."], "7"),
     KeyIdea("a − b = a + (−b). Keep the first number, change subtraction to addition, use the opposite of the second number.")],
    [subp(5, 12), subp(-8, -3), subp(-4, 10)],
    [S("Warm-Up", [Problem("Opposite of −9", "9"), addp(-6, -4)]),
     S("Subtract", [subp(a, b) for a, b in [(7, 10), (-3, 5), (4, -6), (-9, -2), (-1, -8), (0, -15), (12, -12), (-20, 13)]]),
     S("Rewrite as addition, then solve", [Problem("15 − (−7)", "15 + 7 = 22"), Problem("−11 − 4", "−11 + (−4) = −15")]),
     S("Exit Ticket", [Problem("Explain why 6 − (−2) is greater than 6.", "Subtracting −2 adds 2: 8.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students subtract integers by adding the additive inverse.", "Understand subtraction of rational numbers as adding the additive inverse, p − q = p + (−q).", "Two-color counters, workbook Lesson 3.6",
       flow("Opposites.", "Read Let's Explore.", ["Chip model with zero pairs for 3 − (−5).", "Say: Keep, change, opposite."], "Try It 1–3."), ["Changing the sign of the first number."], ["Write the addition form every time."], ["Prove a − b = a + (−b) with chips for 3 cases."]),
    summary="Subtracting means adding the opposite: a − b = a + (−b).")

L7 = Lesson("3.7", "Subtraction as Distance",
    "I can use a number line to show subtraction as the change from one number to another.", "7.NS.1c",
    [],
    "At 6 a.m. it was −4°F. At noon it was 11°F. How much did the temperature rise?",
    [Text("Change = end − start. 11 − (−4) = 11 + 4 = 15. On a number line, from −4 to 11 is 15 units to the right."),
     Figure(nl(-6, 12, pts=[(-4, "−4"), (11, "11")], hops=[(-4, 11, "+15")])),
     Example("Elevation", "A bird at 25 ft dives to a fish at −8 ft. Change in elevation?", ["−8 − 25 = −33."], "−33 ft (33 ft down)"),
     KeyIdea("End − start tells the change. Positive means up or right; negative means down or left.")],
    [Problem("From −3 to 9: change?", "12"), Problem("From 5 to −7: change?", "−12"), Problem("From −10 to −2: change?", "8")],
    [S("Warm-Up", [subp(11, -4), subp(-8, 25)]),
     S("Find the change (end − start)", [Problem(f"from {s(a)} to {s(b)}", s(b - a)) for a, b in [(-2, 6), (8, -1), (-15, -5), (0, -9), (-7, -20), (14, -3)]]),
     S("Solve", [Problem("A submarine at −120 m rises to −45 m. Change?", "75 m up (+75)", space=24), Problem("A company's profit goes from $3 million to −$2 million. What is the change?", "−$5 million", space=24)]),
     S("Exit Ticket", [Problem("Explain how a number line shows 4 − (−3) = 7.", "The distance from −3 to 4 is 7.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students interpret subtraction as change/distance.", "Show that the distance between two rational numbers is the absolute value of their difference.", "Number line, workbook Lesson 3.7",
       flow("Warm-up.", "Read Let's Explore.", ["Model end − start on the number line."], "Try It 1–3."), ["Doing start − end."], ["Label start and end."], ["Track a week of temperature changes."]),
    summary="Change = end − start; on a number line it is the jump from start to end.")

L8 = Lesson("3.8", "Distance Between Two Numbers",
    "I can find the distance between two numbers using absolute value.", "7.NS.1c",
    [("distance", "How far apart two numbers are; always positive: |a − b|.")],
    "Death Valley is 282 ft below sea level. Mount Whitney is 14,505 ft above. How far apart are their elevations?",
    [Example("Distance", "|14,505 − (−282)|", ["14,505 + 282 = 14,787."], "14,787 ft"),
     Example("Order doesn't matter", "|−5 − 3| and |3 − (−5)|", ["|−8| = 8 and |8| = 8."], "8 both ways"),
     KeyIdea("Distance between a and b = |a − b|. It is never negative.")],
    [Problem("Distance between −7 and 2", "9"), Problem("Distance between −12 and −4", "8"), Problem("|−6 − 9|", "15")],
    [S("Warm-Up", [Problem("|−8|", "8"), subp(3, -5)]),
     S("Find the distance", [Problem(f"{s(a)} and {s(b)}", s(abs(a - b))) for a, b in [(-3, 4), (10, -10), (-25, -9), (0, -14), (-6, 6), (-100, 35)]]),
     S("Solve", [Problem("Highest Mississippi point: Woodall Mountain, 807 ft. Lowest: sea level on the Gulf, 0 ft. Difference?", "807 ft", space=24), Problem("Low of −11°F and high of 23°F. Temperature range?", "34°F", space=24)]),
     S("Exit Ticket", [Problem("Why do we use absolute value for distance?", "Distance is never negative; |a − b| works in either order.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students find distance between rational numbers.", "Show that the distance between two rational numbers on the number line is the absolute value of their difference.", "Workbook Lesson 3.8",
       flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3. Weekly Check tomorrow."), ["Giving a negative distance."], ["Count units on a number line."], ["Find temperature ranges in a weather report."]),
    summary="Distance between a and b is |a − b|.")

L9 = Lesson("3.9", "Integers: Temperature and Elevation",
    "I can solve temperature and elevation problems with integers.", "7.NS.1, 7.NS.3",
    [("sea level", "Elevation 0; above is positive and below is negative.")],
    "New Orleans sits about 6 feet below sea level in places. A levee rises 23 feet above that ground. How high above sea level is the top of the levee?",
    [Example("Elevation", "Ground at −6 ft, levee 23 ft higher", ["−6 + 23 = 17."], "17 ft above sea level"),
     Example("Temperature", "It is −3°F at 6 a.m. It rises 4° per hour for 3 hours, then drops 5°.", ["−3 + 12 = 9.", "9 − 5 = 4."], "4°F"),
     KeyIdea("Choose a direction for positive (up, warmer) and use negatives for the opposite.")],
    [Problem("A diver at −30 ft rises 12 ft.", "−18 ft"), Problem("8°F drops 15°.", "−7°F"), Problem("A balloon at 400 ft descends 650 ft into a canyon. New elevation?", "−250 ft")],
    [S("Warm-Up", [addp(-6, 23), subp(9, 5)]),
     S("Solve", [Problem("The temperature was −12°F and rose 19°. New temperature?", "7°F", space=24), Problem("A plane at 2,500 ft descends 3,100 ft over the Dead Sea basin. New elevation?", "−600 ft", space=24),
                 Problem("A miner is 450 ft underground and goes up 120 ft. Elevation?", "−330 ft", space=24), Problem("Morning −5°F, afternoon 14°F. How much warmer?", "19°F", space=24)]),
     S("Exit Ticket", [Problem("Write a temperature story for −8 + 13 and solve it.", "Answers vary; 5.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students solve real-world integer problems.", "Solve real-world problems involving the four operations with rational numbers.", "Workbook Lesson 3.9", flow("Warm-up.", "Read Let's Explore.", ["Work both examples on a vertical number line."], "Try It 1–3."),
       ["Losing track of the sign of the starting value."], ["Vertical number line."], ["Find the elevation of 5 world cities."]),
    summary="Use positive for up or warmer and negative for down or colder.")

L10 = Lesson("3.10", "Integers and Money",
    "I can use integers to track money: deposits, withdrawals, profits, and debts.", "7.NS.1, 7.NS.3",
    [("balance", "The amount of money in an account; it can be negative if more is owed than saved.")],
    "Lillie's account has $25. She spends $40, then deposits $30. What is her balance after each step?",
    [Figure(lambda t: table(t, [["Transaction", "Integer", "Balance"], ["start", "", "$25"], ["spend $40", "−40", "−$15"], ["deposit $30", "+30", "$15"]], [1.7 * inch, 1.2 * inch, 1.2 * inch], width=4.1 * inch)),
     Example("Profit and loss", "A lemonade stand earns $18, $−7 (a loss), and $12 on three days.", ["18 + (−7) + 12 = 23."], "$23 profit"),
     KeyIdea("Deposits and profits are positive; withdrawals, purchases, and losses are negative.")],
    [Problem("$10 balance, buy a $14 item", "−$4"), Problem("−$20 balance, deposit $35", "$15"), Problem("Profits: $50, −$65, $20. Total?", "$5")],
    [S("Warm-Up", [addp(25, -40), addp(-15, 30)]),
     S("Track the balance", [Problem("Start $0. Earn $45, spend $28, spend $30, earn $20.", "$7", lines=1, space=0, wide=True),
                             Problem("Start −$12. Deposit $50, withdraw $65.", "−$27", lines=1, space=0, wide=True)], cols=1),
     S("Solve", [Problem("A business lost $1,200 in January and earned $2,050 in February. Total?", "$850 profit", space=24), Problem("You owe $35 and pay back $22. How much do you owe now?", "$13 (balance −$13)", space=24)]),
     S("Exit Ticket", [Problem("Make a 4-transaction account record that ends at −$5.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students model money situations with integers.", "Solve real-world problems with rational numbers.", "Bank statement example, workbook Lesson 3.10", flow("Warm-up.", "Read Let's Explore.", ["Fill the transaction table."], "Try It 1–3."),
       ["Treating debt as positive."], ["Running balance table."], ["Plan a pretend budget for a month."]),
    summary="Money in is positive; money out or owed is negative. Keep a running balance.")

L11 = Lesson("3.11", "Multi-Step Integer Problems",
    "I can solve multi-step problems with integer addition and subtraction.", "7.NS.3, 7.EE.3",
    [],
    "A football team starts on its own 30-yard line. It loses 7 yards, gains 12, loses 3, and gains 25. Where is it now?",
    [Example("Combine", "30 − 7 + 12 − 3 + 25", ["Gains: 12 + 25 = 37. Losses: −7 + (−3) = −10.", "30 + 37 − 10 = 57."], "the 57-yard line (in plain terms, 27 yards net gain)"),
     KeyIdea("Group the positives and the negatives, then combine.")],
    [Problem("−8 + 15 − 6 + 4", "5"), Problem("A temperature of 3°F drops 10°, rises 4°, drops 2°.", "−5°F"), Problem("Elevation −20 m: up 35, down 12, up 6", "9 m")],
    [S("Warm-Up", [Problem("12 + 25", "37"), Problem("−7 + (−3)", "−10")]),
     S("Evaluate", [Problem(e, s(eval(e.replace("−", "-")))) for e in ["−6 + 9 − 4", "15 − 22 + 3", "−10 − 5 + 18", "7 − (−3) − 12", "−4 + (−8) − (−6)", "20 − 35 + 10 − 5"]]),
     S("Solve", [Problem("A hiker starts at −40 ft (in a valley), climbs 125 ft, descends 60 ft, climbs 15 ft. Elevation?", "40 ft", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a 3-step temperature story and solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve multi-step integer problems.", "Solve multi-step real-life problems with rational numbers.", "Workbook Lesson 3.11", flow("Warm-up.", "Read Let's Explore.", ["Group gains and losses."], "Try It 1–3."),
       ["Sign errors in long expressions."], ["Circle each number with its sign."], ["Track a real football drive."]),
    summary="Group positives and negatives, then combine.")

L12 = Lesson("3.12", "Properties and Mental Math with Integers",
    "I can use properties of addition to add integers mentally.", "7.NS.1d",
    [("commutative property", "Changing the order of addends doesn't change the sum: a + b = b + a."), ("associative property", "Changing the grouping doesn't change the sum: (a + b) + c = a + (b + c).")],
    "How would you quickly find −17 + 45 + 17 + (−5)?",
    [Example("Rearrange", "−17 + 45 + 17 + (−5)", ["Reorder: (−17 + 17) + (45 + (−5)).", "0 + 40 = 40."], "40"),
     KeyIdea("Rewrite subtraction as addition, then reorder and regroup to make zeros or tens.")],
    [Problem("−25 + 38 + 25", "38"), Problem("14 + (−9) + (−14) + 9", "0"), Problem("−36 + 50 + (−14)", "0")],
    [S("Warm-Up", [addp(-17, 17), addp(45, -5)]),
     S("Use properties to evaluate mentally", [Problem(e, s(eval(e.replace("−", "-").replace("(", "(").replace(")", ")")))) for e in ["−8 + 27 + 8", "45 + (−19) + (−45)", "−13 + (−7) + 50", "64 − 30 − 34", "−99 + 50 + 99 + (−50)", "125 + (−75) + (−25)"]]),
     S("Exit Ticket", [Problem("Show two ways to group −6 + 16 + (−4).", "(−6 + −4) + 16 = 6; −6 + (16 + −4) = 6", lines=2, space=0, wide=True)], cols=1)],
    TE("Students apply properties to integer addition.", "Apply properties of operations as strategies to add and subtract rational numbers.", "Workbook Lesson 3.12", flow("Warm-up.", "Read Let's Explore.", ["Reorder to make zero pairs and tens."], "Try It 1–3. Weekly Check tomorrow."),
       ["Moving a number without its sign."], ["Rewrite subtraction as adding the opposite first."], ["Speed challenge with mental integer sums."]),
    summary="Reorder and regroup addends (with their signs) to simplify.")

L13 = Lesson("3.13", "Integer Expressions",
    "I can evaluate expressions with integers and variables.", "7.NS.1, 7.EE.1",
    [("evaluate", "To find the value of an expression by substituting numbers.")],
    "If x = −4, what is x + 9 − x?",
    [Example("Substitute", "x + 9 − x when x = −4", ["(−4) + 9 − (−4) = −4 + 9 + 4 = 9."], "9"),
     Example("Two variables", "a − b when a = −6, b = −11", ["−6 − (−11) = −6 + 11 = 5."], "5"),
     KeyIdea("Substitute with parentheses around negative values, then add the opposite to subtract.")],
    [Problem("x − 7 when x = −3", "−10"), Problem("−y + 5 when y = −2", "7"), Problem("a + b − c when a = 4, b = −9, c = −2", "−3")],
    [S("Warm-Up", [subp(-6, -11), Problem("−(−4)", "4")]),
     S("Evaluate when x = −5 and y = 3", [Problem(e, s(v)) for e, v in [("x + y", -2), ("x − y", -8), ("y − x", 8), ("−x", 5), ("x + x + y", -7), ("|x| − y", 2)]]),
     S("Exit Ticket", [Problem("Find a value of x so that x − 8 is negative and x + 8 is positive.", "Any x between −8 and 8, e.g. 0", lines=2, space=0, wide=True)], cols=1)],
    TE("Students evaluate integer expressions.", "Apply properties to add and subtract; evaluate expressions.", "Workbook Lesson 3.13", flow("Warm-up.", "Read Let's Explore.", ["Substitute with parentheses."], "Try It 1–3."),
       ["Writing x − y as −5 − 3 = −2."], ["Parentheses always."], ["Make a table of x − 8 for x from −10 to 10."]),
    summary="Substitute negatives in parentheses; subtract by adding the opposite.")

L14 = Lesson("3.14", "Explaining Integer Rules with Models",
    "I can explain integer addition and subtraction rules using chips and number lines.", "7.NS.1",
    [],
    "Why does subtracting a negative make a number bigger? Can you prove it with a model?",
    [Text("Rules are easier to remember when you know <b>why</b> they work. Here are both models side by side."),
     Figure(lambda t: table(t, [["Problem", "Chip model", "Number line"], ["−3 + 5", "3 zero pairs cancel; 2 positives left", "start at −3, move right 5 → 2"],
                                ["4 − (−2)", "add 2 zero pairs, remove 2 negatives → 6", "the distance from −2 to 4 is 6"], ["−2 − 5", "add 5 zero pairs, remove 5 positives → −7", "start at −2, move left 5 → −7"]],
                            [1.1 * inch, 2.6 * inch, 2.6 * inch], width=6.3 * inch)),
     KeyIdea("Every rule can be shown with a model. Use a model to check a rule you're unsure of.")],
    [Problem("Explain −6 + 6 = 0 with chips.", "6 zero pairs, nothing left", lines=1, space=0), Problem("Explain 2 − 7 = −5 on a number line.", "Start at 2, move left 7 → −5", lines=1, space=0),
     Problem("Explain −1 − (−4) = 3 with chips.", "Start with 1 negative, add 3 zero pairs, remove 4 negatives → 3 positives", lines=2, space=0)],
    [S("Warm-Up", [subp(4, -2), addp(-3, 5)]),
     S("Explain with a model and solve", [Problem(f"{e}", f"{v}; model explanation", lines=2, space=0, wide=True) for e, v in [("−5 + 2", "−3"), ("3 − 8", "−5"), ("−4 − (−6)", "2"), ("0 − (−3)", "3")]], cols=1),
     S("Exit Ticket", [Problem("Which model do you prefer and why?", "Answers vary.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students justify integer rules with models.", "Understand addition and subtraction of rational numbers with models.", "Counters, number lines, workbook Lesson 3.14", flow("Warm-up.", "Read Let's Explore.", ["Model each table row with chips and number lines."], "Try It 1–3."),
       ["Memorizing rules without meaning."], ["Use chips."], ["Teach the rules to a younger sibling."]),
    summary="Chips and number lines show why integer rules work.")

L15 = Lesson("3.15", "Finding and Fixing Integer Errors",
    "I can find and fix mistakes in integer calculations.", "7.NS.1",
    [],
    "Sam says −8 − 3 = −5. Is he right?",
    [Example("Error", "−8 − 3 = −5?", ["Sam subtracted 8 − 3 and kept a negative sign.", "Correct: −8 − 3 = −8 + (−3) = −11."], "−11"),
     Figure(lambda t: table(t, [["Common error", "Fix"], ["−8 − 3 = −5", "Rewrite: −8 + (−3) = −11"], ["5 − (−2) = 3", "Subtracting a negative adds: 5 + 2 = 7"], ["−4 + 9 = −5", "Different signs: 9 − 4 = 5, sign of 9: +5"], ["|−6| = −6", "Absolute value is a distance: 6"]],
                            [2.4 * inch, 3.4 * inch], width=5.8 * inch)),
     KeyIdea("Rewrite subtraction as addition and check signs with a model.")],
    [Problem("Fix: −7 + (−2) = −5", "−9"), Problem("Fix: 3 − 10 = 7", "−7"), Problem("Fix: −6 − (−6) = −12", "0")],
    [S("Warm-Up", [subp(-8, 3), subp(5, -2)]),
     S("Find and fix the error", [Problem(f"{e}", f"{v}") for e, v in [("−12 + 5 = −17", "−7"), ("9 − (−4) = 5", "13"), ("−3 − 3 = 0", "−6"), ("−10 + 15 = −5", "5"), ("0 − 8 = 8", "−8"), ("|−2| + |−3| = −5", "5")]]),
     S("Exit Ticket", [Problem("What is the most common integer mistake you make? How will you avoid it?", "Answers vary.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students analyze and correct integer errors.", "Apply properties of operations to add and subtract rational numbers.", "Workbook Lesson 3.15", flow("Warm-up.", "Read Let's Explore.", ["Go through the table; student explains each fix."], "Try It 1–3."),
       ["Same errors as listed."], ["Model-check every answer."], ["Create error cards for a sibling."]),
    summary="Rewrite, check signs, and use a model to catch errors.")

L16 = Lesson("3.16", "Integer Problem Solving",
    "I can solve problems with integer addition and subtraction from start to finish.", "7.NS.1, 7.NS.3",
    [],
    "A week of low temperatures: −4, 2, −7, −1, 3, −5, 0. What is the range? What is the sum?",
    [Example("Range and sum", "−4, 2, −7, −1, 3, −5, 0", ["Range: 3 − (−7) = 10.", "Sum: positives 5, negatives −17 → −12."], "range 10°; sum −12"),
     KeyIdea("Organize the numbers, group signs, and check with a model.")],
    [Problem("Range of −15 and 22", "37"), Problem("−9 + 14 − 20", "−15"), Problem("Distance from −6 to −18", "12")],
    [S("Warm-Up", [Problem("3 − (−7)", "10"), Problem("5 + (−17)", "−12")]),
     S("Mixed practice", [addp(-23, 15), subp(-23, 15), subp(15, -23), Problem("|−9 − 4|", "13"), Problem("−6 + 13 − (−5) − 20", "−8"), Problem("x − y when x = −2, y = −9", "7")]),
     S("Solve", [Problem("A submarine at −250 ft rises 90 ft, dives 145 ft, then rises 60 ft. Final depth?", "−245 ft", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write and solve a problem that uses both addition and subtraction of negatives.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve mixed integer problems.", "7.NS.1 review.", "Workbook Lesson 3.16, Unit 3 Review", flow("Warm-up.", "Read Let's Explore.", ["Work the example."], "Try It 1–3.", "Workbook Lesson 3.16 and the Unit 3 Review.", "Check. Tomorrow: Unit 3 Test."),
       ["Sign errors."], ["Models."], ["Analyze real weather data."]),
    summary="Organize, group signs, and check with models.")

C1 = Check("Weekly Check 7: Adding Integers", [S("Show what you know", [addp(-9, -14), addp(-9, 14), addp(21, -30), Problem("|−17|", "17"), Problem("−13 + ___ = 0", "13"),
    Problem("−6 + 11 + 6", "11")])], minutes=15)
C2 = Check("Weekly Check 8: Subtracting Integers", [S("Show what you know", [subp(4, 11), subp(-7, -3), subp(-5, 8), subp(10, -6), Problem("Distance between −8 and 5", "13"),
    Problem("From −6°F to 9°F: change?", "15°F")])], minutes=15)
C3 = Check("Weekly Check 9: Integer Applications", [S("Show what you know", [Problem("−15 m diver rises 9 m", "−6 m"), Problem("$20 balance, spend $32", "−$12"), Problem("−4 + 10 − 9 + 2", "−1"),
    Problem("−29 + 46 + 29 (mentally)", "46"), Problem("Temp 6°F, drops 11°, rises 3°", "−2°F"), Problem("Profits $40, −$55, $30: total", "$15")])], minutes=15)

REVIEW = Check("Unit 3 Review", [
    S("Add and subtract", [addp(-18, -7), addp(25, -40), subp(-12, 9), subp(6, -14), subp(-3, -10), Problem("|−5 − 12|", "17")]),
    S("Applications", [Problem("−8°F rises 21°", "13°F"), Problem("Elevation −45 ft to 30 ft: change", "75 ft"), Problem("x − y + 3 when x = −1, y = −6", "8"), Problem("Fix: −9 − (−4) = −13", "−5")])],
    kind="review", minutes=35, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 3 Test", [
    S("Part A · Integers (1 point each)", [Problem("Opposite of −21", "21"), Problem("|−34|", "34"), Problem("Order: 4, −9, 0, −3", "−9, −3, 0, 4"), Problem("−17 + ___ = 0", "17")]),
    S("Part B · Compute (1 point each)", [addp(-15, -26), addp(-38, 22), addp(44, -19), subp(9, 25), subp(-14, -30), subp(-6, 18), Problem("|−11 − 7|", "18"),
        Problem("−8 + 20 − (−5) − 13", "4")]),
    S("Part C · Applications (2 points each)", [Problem("At 5 a.m. it was −9°F. By 2 p.m. it was 16°F. How much did it rise?", "25°F", space=30, points=2),
        Problem("A diver at −42 ft rises 15 ft, then dives 28 ft. Where is she?", "−55 ft", space=30, points=2),
        Problem("Evaluate a − b + c for a = −3, b = −10, c = −8.", "−1", space=30, points=2)]),
    S("Part D · Explain (3 points)", [Problem("Use a chip model or number line to explain why 2 − (−6) = 8.", "Add 6 zero pairs to 2 positives, remove 6 negatives → 8 positives; or distance from −6 to 2 is 8.", lines=4, space=0, wide=True, points=3)], cols=1)],
    kind="test", minutes=40, rubric=[["18–21 (85%+)", "Mastered."], ["15–17", "Proficient; correct missed items."], ["Below 15", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-12-14", "2027-01-04", "2027-01-11", "2027-01-18"], CHECKS, REVIEW, TEST)

UNIT = Unit(3, "Adding and Subtracting Integers", "Opposites, absolute value, adding and subtracting integers with chips and number lines, and real-world applications.",
    "Negative numbers let us describe temperatures below zero, elevations below sea level, and money owed. In this unit you will add and subtract integers and explain why the rules work.",
    ["Find opposites and absolute values.", "Add integers with the same and different signs.", "Subtract integers by adding the opposite.", "Find distances between numbers.", "Solve real-world integer problems."],
    [("7.NS.1", "Apply and extend previous understandings of addition and subtraction to add and subtract rational numbers; represent on a number line."),
     ("7.NS.3", "Solve real-world and mathematical problems involving the four operations with rational numbers."), ("7.EE.3", "Solve multi-step real-life problems with positive and negative numbers.")],
    [("integer", "Whole numbers and their opposites."), ("opposites", "Same distance from 0, opposite sides."), ("absolute value", "Distance from 0."), ("additive inverse", "A number's opposite; sums to 0.")],
    ["Number lines with negatives (Grade 6).", "Operations with whole numbers."], ["Two-color counters (or paper chips)", "Number lines from −20 to 20", "Thermometer picture"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Temperatures, elevations, bank balances, football yardage, and golf scores all use integers.",
    family_note="Unit 3 spans winter break. Talk about temperatures and bank balances during the break: “If it's 5° and drops 9°, what is it?”",
    weeks=WEEKS)
