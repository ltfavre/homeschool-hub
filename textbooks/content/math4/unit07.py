"""Grade 4 Math · Unit 7: Decimals (Mar 29 – Apr 23, 2027)."""
from decimal import Decimal as Dc
from engine import *
from content.mathkit import c, F, MX
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def dcmp(a, b):
    a, b = Dc(a), Dc(b)
    return ">" if a > b else "<" if a < b else "="


def grid(n, size=70):
    return lambda t: decimal_grid(t, n, size=size)


def money_s(x):
    return f"${Dc(x):,.2f}"


O = "&nbsp;◯&nbsp;"

L1 = Lesson("7.1", "Tenths",
    f"I can write tenths as fractions and as decimals, like {F(3, 10)} = 0.3.", "4.NF.6",
    [("decimal", "A number with a decimal point, used to show parts of a whole in tenths, hundredths, and so on."),
     ("tenth", f"One of 10 equal parts of a whole: {F(1, 10)} or 0.1."), ("decimal point", "The dot that separates the whole number from the parts of a whole.")],
    "A candy bar is split into 10 equal pieces. You eat 3 pieces. How can you write the amount you ate without a fraction bar?",
    [Text(f"When a whole is split into 10 equal parts, each part is one <b>tenth</b>. Three tenths can be written as the fraction {F(3, 10)} or the <b>decimal</b> 0.3."),
     Figure(lambda t: fraction_bar(t, 3, 10, unit_labels=True)),
     Figure(lambda t: decimal_chart(t, "0.3", places=("Ones", "Tenths"), width=200), "0.3: 0 ones and 3 tenths"),
     Text("The <b>decimal point</b> separates whole numbers from parts of a whole. The first place after the decimal point is the tenths place. We read 0.3 as “three tenths.”"),
     Example("Write as a decimal", f"Write {F(7, 10)} as a decimal.", ["7 tenths.", "Write 7 in the tenths place."], "0.7"),
     KeyIdea(f"{F('n', 10)} = 0.n. The tenths place is the first place to the right of the decimal point.")],
    [Problem(f"Write {F(9, 10)} as a decimal.", "0.9"), Problem("Write 0.4 as a fraction.", F(4, 10)), Problem("How do you read 0.6?", "six tenths")],
    [S("Warm-Up", [Problem(f"Simplify {F(5, 10)}", F(1, 2)), Problem("How many tenths make 1 whole?", "10")]),
     S("Write the shaded part as a fraction and a decimal", [Problem("", f"{F(n, 10)} = 0.{n}", fig=(lambda n=n: (lambda t: fraction_bar(t, n, 10, width=CW, label=False)))(), space=0) for n in [2, 5, 8, 1]]),
     S("Write as a decimal", [Problem(F(n, 10), f"0.{n}") for n in [6, 3, 9, 4]]),
     S("Write as a fraction", [Problem(f"0.{n}", F(n, 10)) for n in [1, 7, 2, 5]]),
     S("Exit Ticket", [Problem("Write “eight tenths” as a fraction and as a decimal.", f"{F(8, 10)} = 0.8", wide=True)], cols=1)],
    TE("Students write tenths as fractions and decimals.", "Use decimal notation for fractions with denominators 10 or 100.", "Paper strips cut into 10 parts, workbook Lesson 7.1",
       flow("Simplify 5/10.", "Read Let's Explore.", ["Shade tenths on a strip. Write fraction and decimal side by side.", "Say: The decimal point separates wholes from parts."], "Try It 1–3."),
       ["Writing 3/10 as 3.10 or 0.03."], ["Always say ‘tenths’ aloud."], ["Write 10/10 as a decimal (1.0)."]),
    summary="Tenths are 10 equal parts of a whole: 3/10 = 0.3.".replace("3/10", F(3, 10)))

L2 = Lesson("7.2", "Decimals Greater Than 1",
    f"I can write mixed numbers with tenths as decimals, like {MX(2, 4, 10)} = 2.4.", "4.NF.6",
    [],
    "A recipe needs 2 and 4 tenths cups of flour. How can you write that as a decimal?",
    [Text(f"The whole number goes to the left of the decimal point. The tenths go to the right. {MX(2, 4, 10)} = 2.4, read “two and four tenths.” The word <b>and</b> stands for the decimal point."),
     Figure(lambda t: fraction_bars(t, [(10, 10), (10, 10), (4, 10)], width=W * 0.6)),
     Figure(lambda t: decimal_chart(t, "2.4", places=("Tens", "Ones", "Tenths"), width=240)),
     Example("Write as a decimal", f"Write {MX(13, 6, 10)} as a decimal.", ["13 wholes, 6 tenths."], "13.6"),
     KeyIdea("Say “and” only for the decimal point: 13.6 is “thirteen and six tenths.”")],
    [Problem(f"{MX(5, 9, 10)} as a decimal", "5.9"), Problem("4.3 as a mixed number", MX(4, 3, 10)), Problem("Read 20.7 aloud. Write the words.", "twenty and seven tenths")],
    [S("Warm-Up", [Problem("Write 0.6 as a fraction.", F(6, 10)), Problem(f"{F(17, 10)} as a mixed number", MX(1, 7, 10))]),
     S("Write as a decimal", [Problem(MX(w, n, 10), f"{w}.{n}") for w, n in [(1, 2), (3, 5), (6, 1), (12, 8)]]),
     S("Write as a mixed number", [Problem(f"{w}.{n}", MX(w, n, 10)) for w, n in [(2, 7), (9, 3), (15, 5), (4, 9)]]),
     S("Write in words", [Problem("7.4", "seven and four tenths", lines=1, space=0, wide=True), Problem("31.2", "thirty-one and two tenths", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Write {F(26, 10)} as a mixed number and a decimal.", f"{MX(2, 6, 10)} = 2.6", wide=True)], cols=1)],
    TE("Students write numbers greater than 1 with tenths as decimals.", "Use decimal notation for fractions with denominators 10.", "Fraction strips, workbook Lesson 7.2",
       flow("0.6 as a fraction.", "Read Let's Explore.", ["Model 2 4/10 with strips; write 2.4.", "Say: ‘and’ means the decimal point."], "Try It 1–3."),
       ["Saying ‘and’ in whole numbers.", "Writing 2.4 as 24."], ["Use the chart."], ["Write 105/10 as a decimal."]),
    summary="Wholes go left of the decimal point, tenths go right. Say “and” for the decimal point.")

L3 = Lesson("7.3", "Tenths on a Number Line",
    "I can place and name decimals in tenths on a number line.", "4.NF.6",
    [],
    "A walking trail has markers every tenth of a mile. Lillie stops at the 7th marker after the 1-mile sign. Where is she?",
    [Text("A number line from 0 to 1 split into 10 equal parts shows tenths. 1.7 is 7 tenths past 1."),
     Figure(lambda t: number_line(t, 0, 2, Dc("0.1"), 1, points=[(Dc("1.7"), "1.7")], fmt_fn=lambda v: str(v))),
     Example("Name the point", "What decimal is at point A?", ["Each jump is 0.1.", "A is 4 jumps past 3."], "3.4",
             fig=lambda t: number_line(t, 3, 4, Dc("0.1"), Dc("0.5"), points=[(Dc("3.4"), "A")], fmt_fn=lambda v: str(v), width=360)),
     KeyIdea("Count jumps of 0.1 from the whole number.")],
    [Problem("What decimal is halfway between 0 and 1?", "0.5"), Problem("What decimal is 3 tenths more than 2?", "2.3"), Problem("Which whole number is 6.8 closer to?", "7")],
    [S("Warm-Up", [Problem("Count by tenths from 0.6 to 1.2.", "0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2", lines=1, space=0, wide=True)], cols=1),
     S("Name each point", [Problem(f"Point {lab}", v, fig=(lambda a=a, b=b, v=v, lab=lab: (lambda t: number_line(t, a, b, Dc("0.1"), Dc("0.5"), points=[(Dc(v), lab)], fmt_fn=lambda q: str(q), width=CW, height=58)))(), space=0)
                           for a, b, v, lab in [(0, 1, "0.3", "A"), (1, 2, "1.8", "B"), (4, 5, "4.5", "C"), (7, 8, "7.1", "D")]]),
     S("Exit Ticket", [Problem("Draw a number line from 5 to 6 in tenths. Mark 5.4 and 5.9.", "Ten equal parts; points at the 4th and 9th marks", space=50, wide=True)], cols=1)],
    TE("Students locate tenths on number lines.", "Locate decimals on a number line.", "Workbook Lesson 7.3",
       flow("Count by tenths.", "Read Let's Explore.", ["Draw 0 to 2 in tenths. Say: Count jumps of one tenth."], "Try It 1–3."), ["Counting marks instead of jumps."], ["Label every mark."], ["Place 0.25 between 0.2 and 0.3."]),
    summary="Split each whole into 10 equal jumps; each jump is 0.1.")

L4 = Lesson("7.4", "Decimal Place Value",
    "I can tell the place and value of digits in a decimal.", "4.NF.6",
    [("tenths place", "The first place to the right of the decimal point."), ("hundredths place", "The second place to the right of the decimal point.")],
    "In 45.7, the 4, the 5, and the 7 all have different values. What is each worth?",
    [Text("Place value continues to the right of the decimal point. Each place is still 10 times the place to its right: 1 one = 10 tenths."),
     Figure(lambda t: decimal_chart(t, "45.7", places=("Tens", "Ones", "Tenths"), width=260)),
     Example("Value of a digit", "What is the value of each digit in 45.7?", ["4 is in the tens place: 40.", "5 is in the ones place: 5.", f"7 is in the tenths place: 0.7 ({F(7, 10)})."], "40 + 5 + 0.7"),
     KeyIdea("Ones, then the decimal point, then tenths, then hundredths. 10 tenths = 1 one.")],
    [Problem("Value of the 3 in 6.3", f"0.3 ({F(3, 10)})"), Problem("Value of the 6 in 6.3", "6"), Problem("Write 20 + 8 + 0.1 as a decimal.", "28.1")],
    [S("Warm-Up", [Problem("Value of the 4 in 345", "40"), Problem("How many tenths in 1?", "10")]),
     S("Write the value of the underlined digit", [Problem(s, v) for s, v in [("3.<u>8</u>", "0.8"), ("<u>2</u>5.1", "20"), ("1<u>7</u>.4", "7"), ("40.<u>6</u>", "0.6")]]),
     S("Write as a decimal", [Problem("30 + 2 + 0.9", "32.9"), Problem("5 + 0.4", "5.4"), Problem("60 + 0.3", "60.3"), Problem("8 ones and 2 tenths", "8.2")]),
     S("Exit Ticket", [Problem("Write 73.5 in expanded form.", "70 + 3 + 0.5", wide=True)], cols=1)],
    TE("Students identify place and value in decimals.", "Understand decimal place value to tenths.", "Workbook Lesson 7.4", flow("Value of 4 in 345.", "Read Let's Explore.", ["Extend the place-value chart to tenths."], "Try It 1–3. Weekly Check tomorrow."),
       ["Calling the tenths place ‘oneths’."], ["Use the chart."], ["What is 10 tenths + 10 tenths?"]), summary="Each place is 10 times the place to its right, even after the decimal point.")

L5 = Lesson("7.5", "Hundredths",
    f"I can write hundredths as fractions and decimals, like {F(37, 100)} = 0.37.", "4.NF.6",
    [("hundredth", f"One of 100 equal parts of a whole: {F(1, 100)} or 0.01.")],
    "A dollar is 100 cents. If you have 37 cents, what part of a dollar do you have?",
    [Text(f"Split a whole into 100 equal parts. Each part is one <b>hundredth</b>. 37 hundredths = {F(37, 100)} = 0.37."),
     Figure(grid(37, 110), "37 of 100 squares shaded: 0.37"),
     Figure(lambda t: decimal_chart(t, "0.37", places=("Ones", "Tenths", "Hundredths"), width=260)),
     Example("Hundredths with a zero", f"Write {F(5, 100)} as a decimal.", ["5 hundredths: 0 tenths and 5 hundredths.", "Write a 0 in the tenths place."], "0.05"),
     WatchOut("0.5 and 0.05 are different! 0.5 is 5 tenths (50 cents). 0.05 is 5 hundredths (5 cents)."),
     KeyIdea("Hundredths use two places after the decimal point.")],
    [Problem(f"{F(48, 100)} as a decimal", "0.48"), Problem("0.09 as a fraction", F(9, 100)), Problem(f"{F(3, 100)} as a decimal", "0.03")],
    [S("Warm-Up", [Problem("How many cents in a dollar?", "100"), Problem(f"{F(7, 10)} as a decimal", "0.7")]),
     S("Write the shaded part as a fraction and a decimal", [Problem("", f"{F(n, 100)} = {Dc(n) / 100:.2f}", fig=grid(n), space=0) for n in [25, 62, 8, 90]]),
     S("Write as a decimal", [Problem(F(n, 100), f"{Dc(n) / 100:.2f}") for n in [13, 70, 4, 99]]),
     S("Exit Ticket", [Problem("Explain the difference between 0.4 and 0.04.", "0.4 is 4 tenths (40 hundredths); 0.04 is 4 hundredths.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students write hundredths as fractions and decimals.", "Use decimal notation for fractions with denominator 100.", "Hundred grids, coins, workbook Lesson 7.5",
       flow("Cents in a dollar.", "Read Let's Explore with coins.", ["Shade 37 squares on a hundred grid.", "Work the example and Watch Out using pennies and dimes."], "Try It 1–3."),
       ["Writing 5/100 as 0.5."], ["Use money: dimes are tenths, pennies are hundredths."], ["Write 125 hundredths as a decimal."]),
    summary="Hundredths use two decimal places: 37/100 = 0.37; 5/100 = 0.05.".replace("37/100", F(37, 100)).replace("5/100", F(5, 100)))

L6 = Lesson("7.6", "Equivalent Tenths and Hundredths",
    f"I can show that tenths and hundredths can be equivalent, like {F(3, 10)} = {F(30, 100)} and 0.3 = 0.30.", "4.NF.5, 4.NF.6",
    [],
    "Is 3 dimes the same amount of money as 30 pennies?",
    [Text(f"Yes! 3 dimes = 30 cents = 30 pennies. In the same way, {F(3, 10)} = {F(30, 100)}: each tenth is 10 hundredths."),
     Figure(lambda t: Table([[decimal_grid(t, 30, 100, tenths_only=True), decimal_grid(t, 30, 100)]], colWidths=[130, 130]), "0.3 (3 columns) = 0.30 (30 squares)"),
     Example("Rename tenths as hundredths", f"{F(6, 10)} = {F('?', 100)}", ["Multiply top and bottom by 10."], f"{F(60, 100)}; 0.6 = 0.60"),
     KeyIdea("A zero at the end of a decimal does not change its value: 0.3 = 0.30.")],
    [Problem(f"{F(9, 10)} = {F('?', 100)}", "90"), Problem(f"{F(40, 100)} = {F('?', 10)}", "4"), Problem("0.5 = 0.___", "50")],
    [S("Warm-Up", [Problem(f"{F(1, 2)} = {F('?', 10)}", "5"), Problem("How many pennies equal 1 dime?", "10")]),
     S("Find the equivalent fraction", [Problem(f"{F(n, 10)} = {F('?', 100)}", str(n * 10)) for n in [2, 7, 1]] + [Problem(f"{F(n * 10, 100)} = {F('?', 10)}", str(n)) for n in [5, 8, 3]]),
     S("Equal or not?", [Problem("0.6 and 0.60", "equal", choices=["equal", "not equal"]), Problem("0.6 and 0.06", "not equal", choices=["equal", "not equal"]),
                         Problem("2.4 and 2.40", "equal", choices=["equal", "not equal"]), Problem("0.70 and 0.07", "not equal", choices=["equal", "not equal"])]),
     S("Exit Ticket", [Problem(f"Use money to explain why {F(5, 10)} = {F(50, 100)}.", "5 dimes = 50 cents = 50 pennies.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students show tenths/hundredths equivalence.", "Express a fraction with denominator 10 as an equivalent fraction with denominator 100.", "Dimes and pennies, hundred grids, workbook Lesson 7.6",
       flow("1/2 = ?/10.", "Read Let's Explore with real coins.", ["Shade 3 columns and count squares (30).", "Say: Each tenth is 10 hundredths."], "Try It 1–3."),
       ["Thinking 0.30 is greater than 0.3."], ["Coins."], ["Write 1.5 as hundredths (150/100)."]),
    summary="Each tenth equals 10 hundredths: 0.3 = 0.30.")

L7 = Lesson("7.7", "Adding Tenths and Hundredths",
    f"I can add a fraction in tenths to a fraction in hundredths, like {F(3, 10)} + {F(4, 100)}.", "4.NF.5",
    [],
    "You have 3 dimes and 4 pennies. What part of a dollar is that?",
    [Text(f"To add tenths and hundredths, first make the denominators the same. Change tenths to hundredths."),
     Example("Add", f"{F(3, 10)} + {F(4, 100)}", [f"{F(3, 10)} = {F(30, 100)}.", f"{F(30, 100)} + {F(4, 100)} = {F(34, 100)}."], f"{F(34, 100)} = 0.34"),
     Example("Add with regrouping", f"{F(7, 10)} + {F(45, 100)}", [f"{F(7, 10)} = {F(70, 100)}.", f"{F(70, 100)} + {F(45, 100)} = {F(115, 100)} = {MX(1, 15, 100)}."], "1.15"),
     KeyIdea("Rename tenths as hundredths, then add the numerators.")],
    [Problem(f"{F(2, 10)} + {F(5, 100)}", F(25, 100)), Problem(f"{F(6, 10)} + {F(30, 100)}", F(90, 100)), Problem(f"{F(8, 10)} + {F(35, 100)}", F(115, 100) + " = " + MX(1, 15, 100))],
    [S("Warm-Up", [Problem(f"{F(4, 10)} = {F('?', 100)}", "40"), Problem(f"{F(23, 100)} + {F(41, 100)}", F(64, 100))]),
     S("Add", [Problem(f"{F(a, 10)} + {F(b, 100)}", (F(10 * a + b, 100) if 10 * a + b < 100 else (MX(1, 10 * a + b - 100, 100) if 10 * a + b > 100 else "1"))) for a, b in
               [(1, 6), (4, 22), (5, 50), (7, 3), (9, 15), (6, 40)]]),
     S("Solve", [Problem(f"Ellie walked {F(5, 10)} mile. Then she walked {F(25, 100)} mile. How far did she walk? Write a fraction and a decimal.", f"{F(75, 100)} = 0.75 mile", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"{F(2, 10)} + {F(68, 100)}", f"{F(88, 100)} = 0.88", wide=True)], cols=1)],
    TE("Students add fractions with denominators 10 and 100.", "Add two fractions with respective denominators 10 and 100.", "Coins, workbook Lesson 7.7",
       flow("4/10 = ?/100.", "Read Let's Explore with coins.", ["Work both examples. Say: Make the pieces the same size first."], "Try It 1–3."),
       ["Adding 3/10 + 4/100 = 7/110."], ["Use money."], ["Add three: 3/10 + 4/100 + 1/10."]),
    summary="Rename tenths as hundredths, then add.")

L8 = Lesson("7.8", "Decimals in Different Forms",
    "I can write decimals in standard, word, fraction, and expanded form.", "4.NF.6",
    [],
    "The fastest 100-meter dash time at a school meet was 13.45 seconds. How do you say that number?",
    [Figure(lambda t: table(t, [["Form", "13.45"], ["Standard", "13.45"], ["Word", "thirteen and forty-five hundredths"],
                                ["Fraction / mixed number", P(MX(13, 45, 100), ParagraphStyle('x', fontName='Body', fontSize=11))], ["Expanded", "10 + 3 + 0.4 + 0.05"]],
                            [1.9 * inch, 3.6 * inch], width=5.5 * inch)),
     Example("Write in words", "Write 6.08 in words.", ["Whole number: six.", "“and” for the point.", "08 hundredths = eight hundredths."], "six and eight hundredths"),
     KeyIdea("Read the decimal part as a whole number, then say the last place: 0.45 is “forty-five hundredths.”")],
    [Problem("Write 2.7 in words.", "two and seven tenths"), Problem("Write “nine and twelve hundredths” as a decimal.", "9.12"), Problem("Write 5.36 in expanded form.", "5 + 0.3 + 0.06")],
    [S("Warm-Up", [Problem(f"{F(45, 100)} as a decimal", "0.45"), Problem("0.3 = 0.___", "30")]),
     S("Write as a decimal", [Problem("four and six tenths", "4.6"), Problem("twenty and three hundredths", "20.03"), Problem(MX(7, 81, 100), "7.81"), Problem("1 + 0.5 + 0.02", "1.52")]),
     S("Write in words", [Problem("0.29", "twenty-nine hundredths", lines=1, space=0, wide=True), Problem("14.6", "fourteen and six tenths", lines=1, space=0, wide=True)], cols=1),
     S("Write in expanded form", [Problem("38.04", "30 + 8 + 0.04"), Problem("6.75", "6 + 0.7 + 0.05")]),
     S("Exit Ticket", [Problem("Write 12.09 in words and as a mixed number.", f"twelve and nine hundredths; {MX(12, 9, 100)}", lines=2, space=0, wide=True)], cols=1)],
    TE("Students write decimals in multiple forms.", "Read and write decimals to hundredths.", "Workbook Lesson 7.8", flow("45/100 as a decimal.", "Read Let's Explore.", ["Fill the table together. Work the example."], "Try It 1–3. Weekly Check tomorrow."),
       ["Reading 6.08 as ‘six and eight tenths’."], ["Look at the last place to name the decimal."], ["Find a real decimal in a sports page."]), summary="Decimals can be written in standard, word, fraction, and expanded form.")

L9 = Lesson("7.9", "Comparing Decimals with Models",
    "I can compare two decimals using hundred grids and number lines.", "4.NF.7",
    [],
    "Is 0.4 or 0.35 greater? 35 is bigger than 4… but is 0.35 bigger than 0.4?",
    [Text("Models show the truth: 0.4 shades 40 squares, and 0.35 shades only 35 squares. So 0.4 &gt; 0.35."),
     Figure(lambda t: Table([[decimal_grid(t, 40, 100), decimal_grid(t, 35, 100)]], colWidths=[130, 130]), "0.4 (left) and 0.35 (right)"),
     WatchOut("Longer decimals are not always greater. Compare the same places."),
     KeyIdea("Decimals must refer to the same whole to be compared. Shade both on the same-size grid.")],
    [Problem(f"0.6 {O} 0.59", ">"), Problem(f"0.25 {O} 0.3", "<"), Problem(f"0.7 {O} 0.70", "=")],
    [S("Warm-Up", [Problem("0.4 = 0.___", "40"), Problem(f"{F(35, 100)} {O} {F(40, 100)}", "<")]),
     S("Shade and compare", [Problem(f"{a} {O} {b}", dcmp(a, b), fig=lambda t: Table([[decimal_grid(t, 0, 60), decimal_grid(t, 0, 60)]], colWidths=[70, 70]), space=0)
                             for a, b in [("0.5", "0.45"), ("0.2", "0.12"), ("0.8", "0.80"), ("0.33", "0.3")]]),
     S("Exit Ticket", [Problem("Lillie says 0.15 &gt; 0.5 because 15 &gt; 5. Is she right? Explain.", "No: 0.5 = 0.50 and 50 hundredths > 15 hundredths.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare decimals with models.", "Compare two decimals to hundredths by reasoning about their size; same whole.", "Hundred grids, workbook Lesson 7.9",
       flow("0.4 = 0.40.", "Read Let's Explore.", ["Shade 0.4 and 0.35 on grids."], "Try It 1–3."), ["Thinking more digits means greater."], ["Shade both."], ["Find a decimal between 0.4 and 0.5."]),
    summary="Shade both decimals on the same grid; more shaded is greater.")

L10 = Lesson("7.10", "Comparing Decimals with Place Value",
    "I can compare decimals by lining up place values.", "4.NF.7",
    [],
    "Two runners finished in 12.48 seconds and 12.5 seconds. Who was faster (less time)?",
    [Text("Line up the decimal points. Write a zero so both have hundredths. Compare from the left like whole numbers."),
     Figure(lambda t: table(t, [["", "Tens", "Ones", ".", "Tenths", "Hundredths"], ["12.48", "1", "2", ".", "4", "8"], ["12.50", "1", "2", ".", "5", "0"]],
                            [0.9 * inch, 0.6 * inch, 0.6 * inch, 0.3 * inch, 0.8 * inch, 1.0 * inch], width=4.2 * inch)),
     Example("Compare", "12.48 vs 12.5", ["Tens and ones are the same.", "Tenths: 4 &lt; 5."], "12.48 &lt; 12.5; the 12.48 runner was faster"),
     KeyIdea("Line up the decimal points, fill in zeros, compare from the left.")],
    [Problem(f"3.09 {O} 3.1", "<"), Problem(f"5.6 {O} 5.06", ">"), Problem(f"10.4 {O} 9.99", ">")],
    [S("Warm-Up", [Problem(f"0.5 {O} 0.45", ">"), Problem("Write 0.7 with hundredths.", "0.70")]),
     S("Write >, <, or = in the circle", [Problem(f"{a} {O} {b}", dcmp(a, b)) for a, b in [("2.4", "2.38"), ("7.05", "7.5"), ("0.9", "0.90"), ("13.2", "12.99"), ("4.67", "4.76"), ("8.1", "8.01")]]),
     S("Exit Ticket", [Problem("Which is greater, 6.7 or 6.68? Explain with place value.", "6.7 (6.70): 7 tenths > 6 tenths.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare decimals using place value.", "Compare decimals; record with >, =, <.", "Workbook Lesson 7.10", flow("0.5 vs 0.45.", "Read Let's Explore.", ["Line up decimal points in a chart.", "Say: Same places, from the left."], "Try It 1–3."),
       ["Comparing 3.09 and 3.1 as 309 vs 31."], ["Fill zeros."], ["Order sports times."]), summary="Line up decimal points, add zeros, and compare from the left.")

L11 = Lesson("7.11", "Ordering Decimals",
    "I can order three or more decimals.", "4.NF.7",
    [],
    "Three bean plants grew 2.35 in., 2.5 in., and 2.07 in. List them from shortest to tallest growth.",
    [Example("Order", "2.35, 2.5, 2.07 from least to greatest", ["Write with hundredths: 2.35, 2.50, 2.07.", "Compare tenths: 0 &lt; 3 &lt; 5."], "2.07, 2.35, 2.5"),
     KeyIdea("Write all decimals with the same number of places, then order like whole numbers.")],
    [Problem("Order least to greatest: 0.6, 0.06, 0.66", "0.06, 0.6, 0.66"), Problem("Order greatest to least: 1.2, 1.12, 1.21", "1.21, 1.2, 1.12"), Problem("Which is least: 4.4, 4.04, 4.40?", "4.04")],
    [S("Warm-Up", [Problem(f"3.5 {O} 3.45", ">"), Problem("Write 1.3 with hundredths.", "1.30")]),
     S("Order from least to greatest", [Problem(", ".join(xs), ", ".join(sorted(xs, key=Dc)), wide=True) for xs in [["0.8", "0.18", "0.81"], ["3.4", "3.04", "3.44"], ["12.1", "11.9", "12.01"]]], cols=1),
     S("Order from greatest to least", [Problem(", ".join(xs), ", ".join(sorted(xs, key=Dc, reverse=True)), wide=True) for xs in [["5.5", "5.05", "5.55"], ["0.7", "0.69", "0.77"]]], cols=1),
     S("Solve", [Problem("Long jumps: Ellie 2.48 m, Lillie 2.6 m, cousin 2.53 m. Who jumped farthest? Order the jumps.", "Lillie; 2.6, 2.53, 2.48", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Order 9.09, 9.9, 9.19 from least to greatest.", "9.09, 9.19, 9.9", wide=True)], cols=1)],
    TE("Students order decimals.", "Compare decimals to hundredths.", "Workbook Lesson 7.11", flow("3.5 vs 3.45.", "Read Let's Explore.", ["Work the example in a place-value chart."], "Try It 1–3."),
       ["Ordering by number of digits."], ["Fill zeros."], ["Order 5 decimals."]), summary="Write the same number of decimal places, then order like whole numbers.")

L12 = Lesson("7.12", "Decimals and Fractions on a Number Line",
    "I can place decimals and fractions on the same number line and compare them.", "4.NF.6, 4.NF.7",
    [],
    f"Which is greater, {F(3, 4)} or 0.7?",
    [Text(f"Write both in hundredths. {F(3, 4)} = {F(75, 100)} = 0.75. 0.75 &gt; 0.70, so {F(3, 4)} &gt; 0.7."),
     Figure(lambda t: number_line(t, 0, 1, Dc("0.05"), Dc("0.25"), points=[(Dc("0.7"), "0.7"), (Dc("0.75"), "3/4")], fmt_fn=lambda v: f"{v:.2f}")),
     Example("Common benchmark decimals", f"Write {F(1, 2)}, {F(1, 4)}, {F(1, 5)} as decimals.", [f"{F(1, 2)} = {F(50, 100)} = 0.5.", f"{F(1, 4)} = {F(25, 100)} = 0.25.", f"{F(1, 5)} = {F(2, 10)} = 0.2."], "0.5, 0.25, 0.2"),
     KeyIdea("Change fractions to tenths or hundredths, then compare them as decimals.")],
    [Problem(f"{F(1, 2)} {O} 0.45", ">"), Problem(f"{F(2, 5)} {O} 0.4", "="), Problem(f"0.8 {O} {F(3, 4)}", ">")],
    [S("Warm-Up", [Problem(f"{F(1, 4)} = {F('?', 100)}", "25"), Problem(f"{F(3, 5)} = {F('?', 10)}", "6")]),
     S("Write as a decimal", [Problem(F(1, 2), "0.5"), Problem(F(3, 4), "0.75"), Problem(F(4, 5), "0.8"), Problem(F(3, 10), "0.3")]),
     S("Compare", [Problem(f"{F(1, 4)} {O} 0.3", "<"), Problem(f"0.6 {O} {F(3, 5)}", "="), Problem(f"{F(7, 10)} {O} 0.07", ">"), Problem(f"0.5 {O} {F(2, 5)}", ">")]),
     S("Exit Ticket", [Problem(f"Order from least to greatest: 0.6, {F(1, 2)}, 0.55", f"{F(1, 2)}, 0.55, 0.6", wide=True)], cols=1)],
    TE("Students compare fractions and decimals.", "Use decimal notation for fractions; compare.", "Workbook Lesson 7.12", flow("1/4 = ?/100.", "Read Let's Explore.", ["Convert both to hundredths."], "Try It 1–3. Weekly Check tomorrow."),
       ["Treating 3/4 as 0.34."], ["Benchmark list: 1/2 = 0.5, 1/4 = 0.25, 3/4 = 0.75."], ["Convert 3/20 to hundredths."]), summary="Change fractions to tenths or hundredths to compare them with decimals.")

L13 = Lesson("7.13", "Money and Decimals",
    "I can write money amounts as decimals and connect dollars, dimes, and pennies to ones, tenths, and hundredths.", "4.NF.6, 4.MD.2",
    [("cent", "One hundredth of a dollar: $0.01.")],
    "You have 2 one-dollar bills, 3 dimes, and 4 pennies. How do you write that amount?",
    [Figure(lambda t: money(t, dollars=2, dimes=3, pennies=4)),
     Text("Dollars are ones, dimes are tenths of a dollar, and pennies are hundredths of a dollar. 2 dollars, 3 dimes, 4 pennies = <b>$2.34</b>."),
     Figure(lambda t: table(t, [["Coin or bill", "Value", "Decimal"], ["dollar", "100¢", "$1.00"], ["quarter", "25¢", "$0.25"], ["dime", "10¢", "$0.10"], ["nickel", "5¢", "$0.05"], ["penny", "1¢", "$0.01"]],
                            [1.6 * inch, 1.2 * inch, 1.3 * inch], width=4.1 * inch)),
     Example("Count money", "3 quarters and 2 dimes", ["Quarters: 75¢.", "Dimes: 20¢.", "Total: 95¢."], "$0.95"),
     KeyIdea("Write money with a dollar sign and two decimal places: $3.05, not $3.5 for three dollars and five cents.")],
    [Problem("4 dollars, 1 dime, 7 pennies", "$4.17"), Problem("2 quarters, 1 nickel", "$0.55"), Problem("What fraction of a dollar is 1 quarter?", F(25, 100) + " = " + F(1, 4))],
    [S("Warm-Up", [Problem("25 + 25 + 10", "60"), Problem("0.6 = 0.___", "60")]),
     S("Write the amount", [Problem("", money_s(v), fig=(lambda kw=kw: (lambda t: money(t, width=CW, **kw)))(), space=0) for kw, v in
                            [(dict(dollars=1, quarters=2), "1.50"), (dict(dimes=4, pennies=3), "0.43"), (dict(dollars=3, nickels=1, pennies=2), "3.07"), (dict(quarters=3, dimes=2, nickels=1), "1.00")]]),
     S("Write as a decimal amount", [Problem("eight dollars and nine cents", "$8.09"), Problem("47 cents", "$0.47"), Problem("12 dollars and 50 cents", "$12.50"), Problem("6 dimes", "$0.60")]),
     S("Exit Ticket", [Problem("Show $1.36 two different ways with coins and bills.", "Answers vary.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students relate money to decimal place value.", "Use decimal notation; solve money problems.", "Play or real money, workbook Lesson 7.13",
       flow("25 + 25 + 10.", "Read Let's Explore with money.", ["Build amounts with money and write each one.", "Say: Dimes are tenths; pennies are hundredths."], "Try It 1–3."),
       ["Writing $3.5 for $3.05."], ["Use real coins."], ["Fewest coins to make $0.87."]), summary="Dollars = ones, dimes = tenths, pennies = hundredths. Write money with two decimal places.")

L14 = Lesson("7.14", "Adding Money",
    "I can add money amounts by lining up the decimal points.", "4.MD.2",
    [],
    "A notebook costs $2.75 and a pack of pens costs $3.49. What is the total?",
    [Text("Add money like whole numbers: line up the decimal points (dollars under dollars, cents under cents), add from the right, regroup, and bring the decimal point straight down."),
     Example("Add money", "$2.75 + $3.49", ["Think in cents: 275 + 349 = 624 cents.", "Write the decimal point: $6.24."], "$6.24",
             fig=lambda t: column_arith(t, 275, 349, "+", carries={1: "1", 2: "1"})),
     WatchOut("Line up the <b>decimal points</b>, not the right edges, when one amount has no cents: $5 + $1.25 → $5.00 + $1.25."),
     KeyIdea("Line up the decimal points, add like whole numbers, then place the decimal point in the answer.")],
    [Problem("$4.20 + $3.65", "$7.85"), Problem("$1.89 + $2.47", "$4.36"), Problem("$10 + $3.75", "$13.75")],
    [S("Warm-Up", [Problem("275 + 125", "400"), Problem("$1.00 = ___ cents", "100")]),
     S("Add", [Problem(f"{money_s(a)} + {money_s(b)}", money_s(Dc(a) + Dc(b)), space=34) for a, b in [("3.25", "4.50"), ("6.48", "2.39"), ("12.95", "4.06"), ("0.89", "0.76"), ("15", "8.45"), ("23.60", "17.85")]]),
     S("Solve", [Problem("Ellie buys a book for $7.95 and a bookmark for $1.29. How much does she spend?", "$9.24", space=40, wide=True),
                 Problem("Lillie earns $4.50 on Monday, $5.25 on Tuesday, and $3.75 on Wednesday. How much does she earn?", "$13.50", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("$8.67 + $5.48", "$14.15", space=34, wide=True)], cols=1)],
    TE("Students add money amounts.", "Solve word problems involving money with decimals.", "Play money, workbook Lesson 7.14", flow("275 + 125.", "Read Let's Explore.", ["Work the example with money first, then on paper."], "Try It 1–3."),
       ["Misaligning when one amount is whole dollars."], ["Write .00 on whole dollars."], ["Plan a $20 shopping list."]), summary="Line up decimal points and add like whole numbers.")

L15 = Lesson("7.15", "Subtracting Money and Making Change",
    "I can subtract money amounts and make change.", "4.MD.2",
    [("change", "The money you get back when you pay more than the price.")],
    "A game costs $13.65. You pay with a $20 bill. How much change do you get?",
    [Example("Subtract", "$20.00 − $13.65", ["Write $20 as $20.00.", "2000 − 1365 = 635 cents."], "$6.35",
             fig=lambda t: column_arith(t, 2000, 1365, "-")),
     Example("Count up", "Make change for $13.65 from $20.", ["$13.65 + $0.35 = $14.00.", "$14.00 + $6.00 = $20.00.", "$0.35 + $6.00 = $6.35."], "$6.35"),
     KeyIdea("Subtract to find change, or count up from the price to the amount paid.")],
    [Problem("$9.50 − $4.25", "$5.25"), Problem("$10.00 − $6.79", "$3.21"), Problem("Change from $5 for a $2.38 snack", "$2.62")],
    [S("Warm-Up", [Problem("1000 − 365", "635"), Problem("$2.65 + ___ = $3.00", "$0.35")]),
     S("Subtract", [Problem(f"{money_s(a)} − {money_s(b)}", money_s(Dc(a) - Dc(b)), space=34) for a, b in [("8.75", "3.40"), ("6.20", "2.85"), ("15.00", "7.62"), ("20.00", "11.49"), ("5.05", "1.98"), ("50.00", "23.75")]]),
     S("Make change", [Problem("Price $4.70, paid $5.00", "$0.30"), Problem("Price $12.15, paid $20.00", "$7.85"), Problem("Price $0.68, paid $1.00", "$0.32"), Problem("Price $36.40, paid $40.00", "$3.60")]),
     S("Exit Ticket", [Problem("Mom pays for $27.83 of groceries with $50. How much change?", "$22.17", space=34, wide=True)], cols=1)],
    TE("Students subtract money and make change.", "Solve money word problems.", "Play money, workbook Lesson 7.15", flow("1000 − 365.", "Read Let's Explore. Play store.", ["Work both examples; practice counting up with coins."], "Try It 1–3."),
       ["Forgetting to write $20 as $20.00."], ["Count up with real money."], ["Run a pretend store for 10 minutes."]), summary="Subtract or count up to find change.")

L16 = Lesson("7.16", "Decimal and Money Problem Solving",
    "I can solve multi-step problems with decimals and money.", "4.MD.2, 4.NF.7",
    [],
    "You have $20 for the school book fair. Books cost $6.95, $4.50, and $7.25. Can you buy all three?",
    [Example("Add, then compare", "Book fair", ["$6.95 + $4.50 + $7.25 = $18.70.", "$18.70 &lt; $20.00."], "Yes, with $1.30 left"),
     KeyIdea("Estimate first ($7 + $5 + $7 = $19), then find the exact answer.")],
    [Problem("3 notebooks at $1.25 each. Total?", "$3.75"), Problem("$10 − ($3.49 + $2.75)", "$3.76"), Problem("Which costs less: 4 pens at $0.60 or a 4-pack for $2.25?", "the 4-pack ($2.25 < $2.40)")],
    [S("Warm-Up", [Problem("$4.50 + $7.25", "$11.75"), Problem("$20.00 − $18.70", "$1.30")]),
     S("Solve", [
         Problem("Ellie buys 2 smoothies at $3.75 each and a muffin for $2.40. She pays with $10. How much change?", "$0.10", space=50, wide=True),
         Problem("Lillie saves $2.50 each week for 6 weeks. Does she have enough for a $14.95 game? Explain.", "Yes; $15.00 ≥ $14.95, with $0.05 left.", space=50, wide=True),
         Problem("Gas costs $3.09 a gallon in one town and $2.98 in another. Which is cheaper, and by how much?", "$2.98, by $0.11", space=50, wide=True),
         Problem("A family's lunch costs $8.45, $6.90, $7.25, and $5.40. What is the total?", "$28.00", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Plan a snack order under $10 from: chips $1.25, juice $1.75, apple $0.80, sandwich $4.50. Show your total and change.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve multi-step decimal and money problems.", "Solve word problems involving money and decimals.", "Workbook Lesson 7.16, Unit 7 Review",
       flow("Two computations.", "Read Let's Explore.", ["Work the example: estimate, then compute."], "Try It 1–3.", "Workbook Lesson 7.16 and the Unit 7 Review.", "Check. Tomorrow: Unit 7 Test."),
       ["Skipping the estimate and missing errors."], ["Use play money."], ["Plan a real grocery list with a budget."]), summary="Estimate, then add and subtract money carefully, lining up decimal points.")

C1 = Check("Weekly Check 15: Tenths", [S("Show what you know", [Problem(f"{F(7, 10)} as a decimal", "0.7"), Problem("3.9 as a mixed number", MX(3, 9, 10)),
    Problem("Write 15.6 in words.", "fifteen and six tenths", lines=1, space=0), Problem("Value of the 4 in 2.4", "0.4"),
    Problem("Name point A.", "6.3", fig=lambda t: number_line(t, 6, 7, Dc("0.1"), Dc("0.5"), points=[(Dc("6.3"), "A")], fmt_fn=lambda v: str(v), width=CW, height=58), space=0),
    Problem("Write 40 + 2 + 0.8 as a decimal.", "42.8")])], minutes=15)
C2 = Check("Weekly Check 16: Hundredths", [S("Show what you know", [Problem(f"{F(29, 100)} as a decimal", "0.29"), Problem(f"{F(6, 100)} as a decimal", "0.06"),
    Problem(f"{F(4, 10)} = {F('?', 100)}", "40"), Problem(f"{F(3, 10)} + {F(52, 100)}", F(82, 100)), Problem("Write 7.08 in words.", "seven and eight hundredths", lines=1, space=0), Problem("Write 3.45 in expanded form.", "3 + 0.4 + 0.05")])], minutes=15)
C3 = Check("Weekly Check 17: Comparing Decimals", [S("Show what you know", [Problem(f"0.6 {O} 0.58", ">"), Problem(f"4.07 {O} 4.7", "<"), Problem(f"2.30 {O} 2.3", "="),
    Problem(f"{F(1, 4)} {O} 0.2", ">"), Problem("Order: 1.5, 1.05, 1.55", "1.05, 1.5, 1.55"), Problem("Which is greatest: 0.9, 0.89, 0.09?", "0.9")])], minutes=15)

REVIEW = Check("Unit 7 Review", [
    S("Decimals and fractions", [Problem(f"{F(8, 10)} as a decimal", "0.8"), Problem(f"{F(45, 100)} as a decimal", "0.45"), Problem("0.07 as a fraction", F(7, 100)),
                                 Problem(f"{F(6, 10)} + {F(25, 100)}", F(85, 100))]),
    S("Compare and order", [Problem(f"3.4 {O} 3.38", ">"), Problem(f"{F(3, 4)} {O} 0.8", "<"), Problem("Order: 2.2, 2.02, 2.12", "2.02, 2.12, 2.2", wide=True)]),
    S("Money", [Problem("$6.85 + $2.47", "$9.32", space=30), Problem("$20.00 − $14.36", "$5.64", space=30),
                Problem("3 tickets at $4.50 each. Pay with $20. Change?", "$6.50", space=40, wide=True)])], kind="review", minutes=35, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 7 Test", [
    S("Part A · Decimal meaning (1 point each)", [Problem(f"{F(3, 10)} as a decimal", "0.3"), Problem(f"{F(57, 100)} as a decimal", "0.57"), Problem(f"{MX(4, 9, 100)} as a decimal", "4.09"),
        Problem("Write 12.6 in words.", "twelve and six tenths", lines=1, space=0), Problem("Value of the 8 in 3.08", "0.08"), Problem(f"{F(7, 10)} = {F('?', 100)}", "70")]),
    S("Part B · Add fractions and compare (1 point each)", [Problem(f"{F(4, 10)} + {F(35, 100)}", F(75, 100)), Problem(f"0.5 {O} 0.45", ">"), Problem(f"6.09 {O} 6.9", "<"),
        Problem(f"{F(1, 2)} {O} 0.50", "="), Problem("Order least to greatest: 0.4, 0.04, 0.44", "0.04, 0.4, 0.44")]),
    S("Part C · Money (2 points each)", [Problem("$15.75 + $8.68", "$24.43", space=30, points=2), Problem("$30.00 − $17.46", "$12.54", space=30, points=2),
        Problem("Write the amount: 5 dollars, 3 quarters, 2 pennies", "$5.77", points=2)]),
    S("Part D · Problem solving (3 points each)", [
        Problem("Ellie buys 2 books at $5.95 each and a pen for $1.35. She pays with $20. How much change does she get?", "$6.75", space=70, wide=True, points=3),
        Problem("Lillie ran 3.45 km Monday and 3.5 km Tuesday. On which day did she run farther? Explain using place value.", "Tuesday: 3.50 > 3.45 (5 tenths > 4 tenths).", lines=3, space=0, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["20–23 (85%+)", "Mastered."], ["16–19", "Proficient; correct missed items."], ["Below 16", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-03-29", "2027-04-05", "2027-04-12", "2027-04-19"], CHECKS, REVIEW, TEST)

UNIT = Unit(7, "Decimals", "Tenths and hundredths, equivalent decimals, comparing decimals, and money.",
    "Decimals are another way to write fractions with denominators of 10 and 100. You will connect decimals to fractions, place value, number lines, and money.",
    ["Write tenths and hundredths as fractions and decimals.", "Show that tenths and hundredths can be equivalent.", "Add tenths and hundredths.",
     "Compare and order decimals.", "Add and subtract money amounts and make change."],
    [("4.NF.5", "Express a fraction with denominator 10 as an equivalent fraction with denominator 100; add fractions with denominators 10 and 100."),
     ("4.NF.6", "Use decimal notation for fractions with denominators 10 or 100."), ("4.NF.7", "Compare two decimals to hundredths; record with >, =, <."),
     ("4.MD.2", "Solve word problems involving money, including problems with decimals.")],
    [("decimal", "A number written with a decimal point."), ("tenth", "1 of 10 equal parts."), ("hundredth", "1 of 100 equal parts."), ("decimal point", "Separates wholes from parts.")],
    ["Fractions and equivalence (Units 5–6).", "Place value (Unit 1)."], ["Hundred grids", "Real or play money", "Place-value chart with a decimal point"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Decimals are in prices, gas pumps, sports times, and measurements. Every time you pay for something, you are using decimals.",
    family_note="Let your child handle money this unit: count change, read receipts, and compare prices per item at the store.",
    weeks=WEEKS)
