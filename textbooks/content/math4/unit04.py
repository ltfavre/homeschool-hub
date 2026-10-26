"""Grade 4 Math · Unit 4: Factors, Multiples, and Patterns (Jan 11 – Jan 22, 2027)."""
from engine import *
from content.mathkit import c
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def fstr(n):
    return ", ".join(map(str, factors(n)))


def pairs(n):
    return ", ".join(f"{d} × {n // d}" for d in factors(n) if d * d <= n)


def is_prime(n):
    return n > 1 and factors(n) == [1, n]


def pc(n):
    return "prime" if is_prime(n) else ("neither" if n == 1 else "composite")


L1 = Lesson("4.1", "Factors and Factor Pairs",
    "I can find all the factor pairs of a whole number from 1 to 100.",
    "4.OA.4",
    [("factor pair", "Two numbers that multiply to make a product, like 3 and 8 for 24."),
     ("factor", "A number that divides another number with no remainder.")],
    "Ellie wants to arrange 12 chairs in equal rows with no chairs left over. How many different ways can she do it?",
    [Text("Every rectangle you can make with 12 squares shows a <b>factor pair</b> of 12."),
     Figure(lambda t: table(t, [["Rows", "In each row", "Factor pair"], ["1", "12", "1 × 12"], ["2", "6", "2 × 6"], ["3", "4", "3 × 4"]],
                            [1.2 * inch, 1.4 * inch, 1.6 * inch], width=4.2 * inch)),
     Figure(lambda t: array_dots(t, 3, 4), "3 rows of 4 chairs"),
     Text("The factors of 12 are <b>1, 2, 3, 4, 6, and 12</b>. (4 rows of 3 is the same pair as 3 rows of 4, just turned.)"),
     Example("Find all factor pairs", "Find all the factor pairs of 36.",
             ["Start with 1: 1 × 36.", "Try 2: 2 × 18. Try 3: 3 × 12. Try 4: 4 × 9. Try 5: no. Try 6: 6 × 6.",
              "When the factors meet or start repeating, you are done."], pairs(36)),
     KeyIdea("Test 1, 2, 3, … in order. Stop when the pairs meet in the middle. List the factors from least to greatest.")],
    [Problem("List the factor pairs of 18.", pairs(18)), Problem("List all the factors of 20.", fstr(20)), Problem("Is 7 a factor of 42?", "Yes (6 × 7 = 42)")],
    [S("Warm-Up", [Problem("4 × 6", "24"), Problem("45 ÷ 5", "9")]),
     S("List all the factor pairs", [Problem(f"{n}", pairs(n), space=30) for n in [8, 15, 16, 24, 30, 48]]),
     S("Yes or no?", [Problem("Is 6 a factor of 54?", "Yes", choices=["Yes", "No"]), Problem("Is 8 a factor of 60?", "No", choices=["Yes", "No"]),
                      Problem("Is 9 a factor of 81?", "Yes", choices=["Yes", "No"]), Problem("Is 4 a factor of 98?", "No", choices=["Yes", "No"])]),
     S("Solve", [Problem("A gardener has 28 plants. What are all the ways she can plant them in equal rows?", "1 × 28, 2 × 14, 4 × 7 (and turned around)", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("List all the factors of 40.", fstr(40), wide=True)], cols=1)],
    TE("Students find factor pairs for whole numbers 1–100.", "Find all factor pairs for a whole number in the range 1–100; recognize that a whole number is a multiple of each of its factors.",
       "Square tiles or grid paper, workbook Lesson 4.1",
       flow("4 × 6; 45 ÷ 5.", "Read Let's Explore. Build arrays with 12 tiles.", ["Record each rectangle as a factor pair.", "Say: Test 1, 2, 3 in order and stop when the pairs meet.", "Work the 36 example."], "Try It 1–3."),
       ["Missing factor pairs by testing out of order.", "Listing a pair twice."], ["Use tiles to build every rectangle."], ["Which number under 50 has the most factors?"]),
    summary="Factor pairs multiply to make the number. Test numbers in order and stop when the pairs meet.")

L2 = Lesson("4.2", "Prime and Composite Numbers",
    "I can tell whether a number is prime or composite.",
    "4.OA.4",
    [("prime number", "A whole number greater than 1 with exactly two factors: 1 and itself."),
     ("composite number", "A whole number greater than 1 with more than two factors.")],
    "Try to make a rectangle with 7 tiles that is more than one row. Can you?",
    [Text("Some numbers can only make one rectangle: a single row. Those numbers are <b>prime</b>. Numbers that can make more than one rectangle are <b>composite</b>."),
     Figure(lambda t: table(t, [["Number", "Factors", "Prime or composite?"], ["7", fstr(7), "prime"], ["9", fstr(9), "composite"], ["13", fstr(13), "prime"], ["15", fstr(15), "composite"]],
                            [1.0 * inch, 2.0 * inch, 1.8 * inch], width=4.8 * inch)),
     Example("Prime or composite?", "Is 21 prime or composite?", ["21 = 3 × 7.", "21 has more than two factors: 1, 3, 7, 21."], "composite"),
     WatchOut("1 is neither prime nor composite. It has only one factor. 2 is the only even prime number."),
     KeyIdea("Exactly two factors → prime. More than two → composite.")],
    [Problem("Is 17 prime or composite?", pc(17)), Problem("Is 27 prime or composite?", pc(27)), Problem("List the prime numbers between 1 and 20.", "2, 3, 5, 7, 11, 13, 17, 19")],
    [S("Warm-Up", [Problem("Factors of 10", fstr(10)), Problem("Factors of 11", fstr(11))]),
     S("Write prime or composite", [Problem(f"{n}", pc(n)) for n in [5, 12, 19, 25, 29, 33, 41, 49, 51, 53]]),
     S("Think Deeper", [Problem("Mia says all odd numbers are prime. Give an example that shows she is wrong.", "Examples: 9, 15, 21, 25", lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Is 39 prime or composite? Explain.", "Composite: 3 × 13 = 39.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students classify numbers as prime or composite.", "Determine whether a given whole number in the range 1–100 is prime or composite.",
       "Square tiles, hundred chart, workbook Lesson 4.2",
       flow("Factors of 10 and 11.", "Read Let's Explore with 7 tiles.", ["Build rectangles for 7, 9, 13, 15.", "Say: Only one rectangle means prime."], "Try It 1–3."),
       ["Thinking 1 is prime.", "Thinking all odd numbers are prime."], ["Use tiles."], ["Sieve of Eratosthenes on a hundred chart: cross out multiples of 2, 3, 5, 7."]),
    summary="Prime numbers have exactly two factors. Composite numbers have more. 1 is neither.")

L3 = Lesson("4.3", "Multiples",
    "I can find multiples of a number and tell whether a number is a multiple of another number.",
    "4.OA.4",
    [("multiple", "The product of a number and a whole number. Multiples of 4 are 4, 8, 12, 16, …")],
    "A bus comes every 15 minutes, starting at 8:00. Will there be a bus at 9:00?",
    [Text("Skip counting gives <b>multiples</b>. The multiples of 15 are 15, 30, 45, 60, … A bus comes at 8:15, 8:30, 8:45, and 9:00."),
     Figure(lambda t: hundred_chart(t, marked=range(6, 101, 6), width=280), "Multiples of 6 on a hundred chart."),
     Example("Is it a multiple?", "Is 72 a multiple of 8?", ["Ask: 8 × ? = 72.", "8 × 9 = 72."], "Yes"),
     KeyIdea("A number is a multiple of each of its factors. 72 is a multiple of 8, and 8 is a factor of 72.")],
    [Problem("List the first 6 multiples of 7.", "7, 14, 21, 28, 35, 42"), Problem("Is 54 a multiple of 6?", "Yes"), Problem("Is 46 a multiple of 4?", "No")],
    [S("Warm-Up", [Problem("Count by 9s to 45.", "9, 18, 27, 36, 45"), Problem("Is 5 a factor of 35?", "Yes")]),
     S("List the first five multiples", [Problem(f"{n}", ", ".join(str(n * k) for k in range(1, 6))) for n in [3, 6, 8, 11, 12, 25]]),
     S("Multiple or not?", [Problem(f"Is {a} a multiple of {b}?", "Yes" if a % b == 0 else "No", choices=["Yes", "No"]) for a, b in [(36, 9), (50, 6), (84, 7), (90, 4)]]),
     S("Solve", [Problem("Ellie has art every 3 days and piano every 4 days. Both are on day 12. On what day are both on again?", "Day 24", space=40, wide=True,
                         note="Common multiples of 3 and 4: 12, 24, 36.")], cols=1),
     S("Exit Ticket", [Problem("Name a number that is a multiple of both 5 and 6.", "30 (or 60, 90, …)", wide=True)], cols=1)],
    TE("Students find multiples and decide whether one number is a multiple of another.", "Recognize that a whole number is a multiple of each of its factors; determine whether a whole number is a multiple of a given one-digit number.",
       "Hundred chart, crayons, workbook Lesson 4.3",
       flow("Skip-count by 9s.", "Read Let's Explore.", ["Color the multiples of 6 on a hundred chart; then circle the multiples of 4 to find common multiples.", "Say: Factor and multiple are two sides of one fact."], "Try It 1–3."),
       ["Confusing factors and multiples."], ["Use the phrase: factors are small, multiples are many."], ["Find the first three common multiples of 4 and 6."]),
    summary="Multiples come from skip counting. If a × b = c, then c is a multiple of a and of b.")

L4 = Lesson("4.4", "Divisibility Rules",
    "I can use divisibility rules for 2, 3, 5, 9, and 10 to find factors quickly.",
    "4.OA.4",
    [("divisible", "Can be divided with no remainder.")],
    "Is 348 divisible by 3? You could divide… or you could use a shortcut.",
    [Text("<b>Divisibility rules</b> let you test for factors without dividing."),
     Figure(lambda t: table(t, [["A number is divisible by…", "if…", "Example"], ["2", "its ones digit is even (0, 2, 4, 6, 8)", "348 ✓"],
                                ["3", "the sum of its digits is divisible by 3", "3 + 4 + 8 = 15 ✓"], ["5", "its ones digit is 0 or 5", "345 ✓"],
                                ["9", "the sum of its digits is divisible by 9", "3 + 4 + 2 = 9, so 342 ✓"], ["10", "its ones digit is 0", "340 ✓"]],
                            [1.6 * inch, 3.0 * inch, 1.7 * inch], width=6.3 * inch)),
     Example("Use the rules", "Which of 2, 3, 5, 9, 10 divide 135?", ["Ones digit 5: divisible by 5, not by 2 or 10.", "Digit sum 1 + 3 + 5 = 9: divisible by 3 and by 9."], "3, 5, and 9"),
     KeyIdea("Even ones digit → 2. Ends in 0 or 5 → 5. Ends in 0 → 10. Digit sum divisible by 3 or 9 → 3 or 9.")],
    [Problem("Is 726 divisible by 3?", "Yes (7 + 2 + 6 = 15)"), Problem("Is 415 divisible by 2?", "No"), Problem("Is 918 divisible by 9?", "Yes (9 + 1 + 8 = 18)")],
    [S("Warm-Up", [Problem("4 + 7 + 2", "13"), Problem("Is 36 even?", "Yes")]),
     S("Which of 2, 3, 5, 9, 10 divide each number?", [Problem(f"{n}", ", ".join(str(d) for d in [2, 3, 5, 9, 10] if n % d == 0) or "none") for n in [60, 81, 115, 222, 405, 1000]]),
     S("Solve", [Problem("A teacher has 234 stickers. Can she share them equally among 9 students with none left?", "Yes; 2 + 3 + 4 = 9, so 234 ÷ 9 = 26", lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a 3-digit number that is divisible by 2, 3, and 5.", "Any multiple of 30, e.g. 120, 330", wide=True)], cols=1)],
    TE("Students use divisibility rules to identify factors.", "Determine whether a whole number is a multiple of a one-digit number.", "Workbook Lesson 4.4, rule card",
       flow("Digit sums.", "Read Let's Explore.", ["Teach each rule with one example. Make a rule card.", "Work the 135 example."], "Try It 1–3."),
       ["Applying the digit-sum rule to 5 or 10."], ["Keep the rule card visible."], ["Why does the 9 rule work? (Each place value is one more than a multiple of 9.)"]),
    summary="Divisibility rules test for 2, 3, 5, 9, and 10 without dividing.")

L5 = Lesson("4.5", "Number Patterns",
    "I can make and extend a number pattern that follows a rule.",
    "4.OA.5",
    [("pattern", "Numbers or shapes that repeat or change in a predictable way."), ("rule", "Tells how to get the next term of a pattern."),
     ("term", "Each number or shape in a pattern.")],
    "A savings jar starts with $5. Each week $3 is added. How much will be in the jar after 6 weeks?",
    [Text("A <b>rule</b> tells how to get each <b>term</b> from the one before. Rule: start at 5, add 3."),
     Figure(lambda t: table(t, [["Week", "0", "1", "2", "3", "4", "5", "6"], ["Dollars", "5", "8", "11", "14", "17", "20", "23"]],
                            [0.9 * inch] + [0.55 * inch] * 7, width=4.8 * inch)),
     Example("Find the rule", "What is the rule? 4, 9, 14, 19, …", ["9 − 4 = 5, 14 − 9 = 5, 19 − 14 = 5."], "Start at 4, add 5. Next terms: 24, 29"),
     Example("Notice features", "Rule: start at 4, add 5. Which terms are odd?", ["4 (even), 9 (odd), 14 (even), 19 (odd).", "Even + odd = odd, odd + odd = even."], "Every other term is odd."),
     KeyIdea("Find the change between terms to find the rule. Then look for features the rule doesn't say out loud, like odd and even.")],
    [Problem("Rule: start at 7, add 4. Write the first 5 terms.", "7, 11, 15, 19, 23"), Problem("Find the rule: 50, 44, 38, 32", "Start at 50, subtract 6"),
     Problem("Next two terms: 3, 6, 12, 24, ___, ___", "48, 96 (multiply by 2)")],
    [S("Warm-Up", [Problem("Count by 4s from 3: 3, 7, ___, ___", "11, 15"), Problem("100 − 8", "92")]),
     S("Write the first six terms", [Problem("Start at 2, add 6", "2, 8, 14, 20, 26, 32", wide=True), Problem("Start at 90, subtract 7", "90, 83, 76, 69, 62, 55", wide=True),
                                    Problem("Start at 1, multiply by 3", "1, 3, 9, 27, 81, 243", wide=True)], cols=1),
     S("Find the rule and the next term", [Problem("5, 13, 21, 29", "add 8; 37"), Problem("100, 88, 76, 64", "subtract 12; 52"), Problem("2, 4, 8, 16", "multiply by 2; 32"), Problem("11, 22, 33, 44", "add 11; 55")]),
     S("Think Deeper", [Problem("Rule: start at 1, add 2. Will 50 ever be a term? Explain.", "No. All terms are odd (1, 3, 5, …).", lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Make your own pattern with a rule. Write 5 terms.", "Answers vary.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students generate and extend number patterns and identify features.", "Generate a number or shape pattern that follows a given rule; identify apparent features not explicit in the rule.",
       "Workbook Lesson 4.5", flow("Skip-count from 3 by 4s.", "Read Let's Explore. Fill the table.", ["Work both examples.", "Say: Find the change; then look for hidden features."], "Try It 1–3."),
       ["Finding the change only between the first two terms."], ["Write the change between each pair of terms."], ["Patterns that alternate: add 2, add 3, add 2, …"]),
    summary="A rule tells how to get each term. Find the change between terms, and look for hidden features like odd and even.")

L6 = Lesson("4.6", "Shape Patterns",
    "I can extend and describe a repeating or growing shape pattern.",
    "4.OA.5",
    [("repeating pattern", "A pattern with a part (the core) that repeats."), ("growing pattern", "A pattern that gets bigger by a rule.")],
    "A quilt border goes star, square, square, star, square, square, … What shape is 20th?",
    [Figure(lambda t: shape_pattern(t, ["star", "square", "square"] * 3 + ["?"])),
     Text("The <b>core</b> of this repeating pattern is star, square, square, 3 shapes long. Every 3rd shape is a square that ends the core."),
     Example("Use division", "What is the 20th shape?", ["The core has 3 shapes.", "20 ÷ 3 = 6 R2: 6 full cores, then 2 more shapes.", "The 2nd shape in the core is a square."], "square"),
     Example("Growing pattern", "Figure 1 has 1 square, Figure 2 has 3, Figure 3 has 5. How many in Figure 10?", ["The rule is add 2.", "Figure 10 = 1 + 9 × 2 = 19."], "19 squares"),
     KeyIdea("For repeating patterns, find the core and use division. For growing patterns, find the rule.")],
    [Problem("Core: circle, triangle. What is the 15th shape?", "circle (15 is odd)"), Problem("Core: A, B, C, D. What is the 22nd letter?", "B (22 ÷ 4 = 5 R2)"),
     Problem("Growing: 4, 8, 12, … squares. How many in Figure 7?", "28")],
    [S("Warm-Up", [Problem("17 ÷ 3", "5 R2"), Problem("Next: 6, 9, 12, ___", "15")]),
     S("Draw the next shape", [Problem("", "triangle", fig=lambda t: shape_pattern(t, ["circle", "triangle", "circle", "triangle", "circle", "?"], width=CW, size=20), space=0),
                               Problem("", "square", fig=lambda t: shape_pattern(t, ["star", "star", "square", "star", "star", "?"], width=CW, size=20), space=0)]),
     S("Solve", [Problem("Core: red, blue, blue, yellow. What color is the 30th bead?", "blue (30 ÷ 4 = 7 R2)", space=30),
                 Problem("Core: ☐ ☐ ○. How many circles are in the first 24 shapes?", "8 circles", space=30),
                 Problem("A tower adds 3 blocks each day. It has 5 blocks on day 1. How many blocks on day 8?", "26 blocks", space=30),
                 Problem("Toothpick squares in a row: 4, 7, 10, … toothpicks. How many for 6 squares?", "19 toothpicks", space=30)]),
     S("Exit Ticket", [Problem("Make a repeating pattern with a core of 3 shapes. What is the 12th shape?", "Answers vary; the 12th shape is the last shape of the core.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students extend repeating and growing shape patterns.", "Generate a shape pattern that follows a given rule; identify apparent features.", "Pattern blocks or colored paper shapes, workbook Lesson 4.6",
       flow("17 ÷ 3; next in 6, 9, 12.", "Read Let's Explore. Build the border with blocks.", ["Work both examples. Say: Find the core, then divide."], "Try It 1–3."),
       ["Counting the core wrong."], ["Circle each core with a pencil."], ["Find the 100th shape in a 7-shape core."]),
    summary="Repeating patterns: find the core and divide. Growing patterns: find the rule.")

L7 = Lesson("4.7", "Input-Output Tables",
    "I can find and use a rule for an input-output table.",
    "4.OA.5",
    [("input-output table", "A table that shows a rule changing each input number into an output number.")],
    "A machine turns 3 into 12, 5 into 20, and 8 into 32. What does it turn 10 into?",
    [Figure(lambda t: table(t, [["Input", "3", "5", "8", "10"], ["Output", "12", "20", "32", "?"]], [0.9 * inch] + [0.6 * inch] * 4, width=3.3 * inch)),
     Text("Each output is 4 times the input. The rule is <b>multiply by 4</b>, so 10 becomes 40."),
     Example("Find the rule", "Inputs 2, 4, 7 → outputs 9, 11, 14.", ["Each output is 7 more than its input.", "Check: 2 + 7 = 9, 4 + 7 = 11, 7 + 7 = 14."], "Add 7"),
     KeyIdea("Test your rule on every pair in the table, not just one.")],
    [Problem("Rule: × 6. Input 7 → ?", "42"), Problem("Inputs 10, 20, 30 → outputs 5, 15, 25. Rule?", "subtract 5"), Problem("Rule: ÷ 3. Output 9 → input?", "27")],
    [S("Warm-Up", [Problem("8 × 7", "56"), Problem("45 + 9", "54")]),
     S("Find the rule and complete", [
         Problem("In: 1, 2, 3, 4 → Out: 5, 10, 15, ___", "× 5; 20"), Problem("In: 6, 9, 12, 15 → Out: 2, 3, 4, ___", "÷ 3; 5"),
         Problem("In: 12, 20, 33 → Out: 21, 29, ___", "+ 9; 42"), Problem("In: 50, 40, 30 → Out: 38, 28, ___", "− 12; 18")]),
     S("Exit Ticket", [Problem("Make a table with the rule × 8. Use 4 inputs.", "Answers vary, e.g. 1→8, 2→16, 5→40, 9→72.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students find and apply rules for input-output tables.", "Generate a number pattern that follows a given rule.", "Workbook Lesson 4.7",
       flow("8 × 7; 45 + 9.", "Read Let's Explore. Play ‘guess my rule’.", ["Work the example. Say: Test the rule on every pair."], "Try It 1–3."),
       ["Checking only the first pair."], ["Write the operation between each input and output."], ["Two-step rules: × 2 then + 1."]),
    summary="An input-output rule changes each input into its output. Test it on every pair.")

L8 = Lesson("4.8", "Factors, Multiples, and Patterns in Problems",
    "I can use factors, multiples, and patterns to solve problems.",
    "4.OA.4, 4.OA.5",
    [],
    "Hot dogs come in packs of 10 and buns in packs of 8. What is the fewest of each you can buy to have the same number of hot dogs and buns?",
    [Text("Common multiples answer “at the same time” or “the same number” questions. Factors answer “equal rows” and “equal groups” questions."),
     Example("Common multiple", "Packs of 10 hot dogs and 8 buns.", ["Multiples of 10: 10, 20, 30, 40.", "Multiples of 8: 8, 16, 24, 32, 40.", "The first match is 40."],
             "4 packs of hot dogs and 5 packs of buns"),
     Example("Factors", "48 students need equal teams of more than 5 and fewer than 10 students. What team sizes work?", ["Factors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48.", "Between 5 and 10: 6 and 8."], "teams of 6 or 8"),
     KeyIdea("Same number or same time → common multiples. Equal rows or equal teams → factors.")],
    [Problem("Juice comes in packs of 6 and cups in packs of 9. Fewest of each to match?", "3 packs of juice, 2 packs of cups (18)"),
     Problem("Can 52 chairs be put in equal rows of 4? Of 5?", "Rows of 4: yes (13); rows of 5: no"), Problem("Is 91 prime?", "No (7 × 13)")],
    [S("Warm-Up", [Problem("Factors of 24", fstr(24)), Problem("Multiples of 6 to 36", "6, 12, 18, 24, 30, 36")]),
     S("Solve", [
         Problem("Two lighthouses flash every 6 and every 10 seconds. They flash together now. In how many seconds will they flash together again?", "30 seconds", space=50, wide=True),
         Problem("Grandpa has 36 tomato plants. List every way he can plant them in equal rows.", "1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6", space=50, wide=True),
         Problem("A pattern starts at 3 and adds 4. Is 50 in the pattern? Explain.", "No. Terms are 3, 7, 11, … always odd.", lines=2, space=0, wide=True),
         Problem("Name all prime numbers between 40 and 60.", "41, 43, 47, 53, 59", space=20, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a problem that uses common multiples. Solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students apply factors, multiples, and patterns to solve problems.", "Find factor pairs; recognize multiples; generate patterns.", "Workbook Lesson 4.8, Unit 4 Review",
       flow("Factors of 24; multiples of 6.", "Read Let's Explore.", ["Work both examples. Discuss: factors or multiples?"], "Try It 1–3.", "Workbook Lesson 4.8 and the Unit 4 Review.", "Check. Tomorrow: Unit 4 Test."),
       ["Using factors when the question needs multiples."], ["List both and look for matches."], ["Find the least common multiple of 4, 6, and 9."]),
    summary="Use common multiples for “the same number” or “at the same time.” Use factors for equal rows or teams.")

CHECK1 = Check("Weekly Check 8: Factors and Multiples", [S("Show what you know", [
    Problem("List the factor pairs of 32.", pairs(32), space=24), Problem("Is 23 prime or composite?", pc(23)), Problem("Is 57 prime or composite?", "composite (3 × 19)"),
    Problem("List the first five multiples of 9.", "9, 18, 27, 36, 45"), Problem("Is 96 a multiple of 8?", "Yes"),
    Problem("Which of 2, 3, 5, 9, 10 divide 270?", "2, 3, 5, 9, 10")])], minutes=15)

REVIEW = Check("Unit 4 Review", [S("Factors and multiples", [
        Problem("Factors of 42", fstr(42)), Problem("Prime or composite: 31", pc(31)), Problem("First 5 multiples of 12", "12, 24, 36, 48, 60"),
        Problem("Is 7 a factor of 84?", "Yes")]),
    S("Patterns", [Problem("Rule: start at 6, add 7. First five terms.", "6, 13, 20, 27, 34"), Problem("Core: ○ △ ☐. What is the 14th shape?", "△ (14 ÷ 3 = 4 R2)"),
                   Problem("In: 2, 5, 9 → Out: 16, 40, 72. Rule?", "× 8"), Problem("Is 100 in the pattern 1, 4, 7, 10, …? Explain.", "Yes: 100 = 1 + 33 × 3.", lines=2, space=0)])],
    kind="review", minutes=30, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 4 Test", [
    S("Part A · Factors and multiples (1 point each)", [Problem("List all factors of 28.", fstr(28)), Problem("List the factor pairs of 45.", pairs(45)),
        Problem("Prime or composite: 47", pc(47)), Problem("Prime or composite: 63", pc(63)), Problem("List the first six multiples of 7.", "7, 14, 21, 28, 35, 42"),
        Problem("Is 72 a multiple of 9?", "Yes"), Problem("Is 4 a factor of 54?", "No"), Problem("Which of 2, 3, 5, 9, 10 divide 135?", "3, 5, 9")]),
    S("Part B · Patterns (1 point each)", [Problem("Rule: start at 8, add 6. Write five terms.", "8, 14, 20, 26, 32"), Problem("Find the rule: 81, 72, 63, 54", "subtract 9"),
        Problem("Core: red, red, blue. What is the 17th color?", "red (17 ÷ 3 = 5 R2)"), Problem("In: 3, 6, 9 → Out: 1, 2, 3. Rule?", "÷ 3"),
        Problem("Rule: start at 2, add 4. Will the terms be odd or even? Why?", "Even: even + even = even.", lines=2, space=0)]),
    S("Part C · Problem solving (3 points each)", [
        Problem("Rolls come in packs of 12 and patties in packs of 8. What is the fewest of each pack to have the same number of rolls and patties?", "2 packs of rolls, 3 packs of patties (24)", space=60, wide=True, points=3),
        Problem("A class of 30 students needs equal teams with at least 3 students each. List all the possible team sizes.", "3, 5, 6, 10, 15, 30", space=60, wide=True, points=3)], cols=1)],
    kind="test", minutes=35, rubric=[["17–19 (85%+)", "Mastered."], ["14–16", "Proficient; correct missed items."], ["Below 14", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
CHECKS = [CHECK1]
WEEKS = schedule(LESSONS, ["2027-01-11", "2027-01-18"], CHECKS, REVIEW, TEST)

UNIT = Unit(4, "Factors, Multiples, and Patterns", "Factor pairs, prime and composite numbers, multiples, divisibility, and patterns.",
    "Factors and multiples show how numbers are built from other numbers. Patterns show how numbers grow and change by rules. These ideas prepare you for fractions in the next units.",
    ["Find all factor pairs of a number to 100.", "Tell whether a number is prime or composite.", "Find multiples and common multiples.", "Use divisibility rules.", "Extend number and shape patterns and find rules."],
    [("4.OA.4", "Find all factor pairs for a whole number 1–100; recognize multiples; determine prime or composite."),
     ("4.OA.5", "Generate a number or shape pattern that follows a given rule; identify apparent features of the pattern.")],
    [("factor", "A number that divides another with no remainder."), ("multiple", "The product of a number and a whole number."), ("prime number", "A number with exactly two factors."),
     ("composite number", "A number with more than two factors."), ("pattern", "A predictable arrangement of numbers or shapes.")],
    ["Multiplication and division facts.", "Dividing with remainders (Unit 3)."], ["Square tiles (or grid paper squares)", "Hundred chart", "Crayons", "Pattern blocks or paper shapes"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Factors help plan equal teams and rows; multiples help plan schedules that repeat, like buses, medicine doses, and practices.",
    family_note="Hunt for patterns at home: tiles, fabric, calendars, house numbers. Ask: what's the rule? What comes next?",
    weeks=WEEKS)
