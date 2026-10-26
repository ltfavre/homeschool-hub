"""Grade 7 Math · Unit 2: Percents (Nov 9 – Dec 11, 2026)."""
from engine import *
from content.mathkit import c, F, MX
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def m(v):
    return f"${v:,.2f}"


def pf(p):
    return f"{p:g}%"


L1 = Lesson("2.1", "What Is a Percent?",
    "I can explain a percent as a rate per 100.", "7.RP.3",
    [("percent", "A rate per 100. 35% means 35 out of 100, or 35 per 100.")],
    "A survey says 35% of students walk to school. What does that mean if a school has 100 students? 200 students?",
    [Text("<b>Percent</b> means “per hundred.” 35% is 35 per 100. If there are 100 students, 35 walk. If there are 200, twice as many walk: 70."),
     Figure(lambda t: decimal_grid(t, 35, 110), "35 out of 100 squares: 35%"),
     Figure(lambda t: double_line(t, ["0%", "35%", "70%", "100%"], [0, 35, 70, 100], "percent", "students")),
     Example("Per 100", "In a class, 18 out of 25 students got an A. What percent is that?", ["Scale to 100: 25 × 4 = 100.", "18 × 4 = 72."], "72%"),
     KeyIdea("Percent is a rate per 100. Scale the ratio so the whole is 100.")],
    [Problem("40 out of 100 = ___%", "40%"), Problem("7 out of 20 = ___%", "35%"), Problem("What percent is 3 out of 4?", "75%")],
    [S("Warm-Up", [Problem("25 × 4", "100"), Problem("18 × 4", "72")]),
     S("Write as a percent", [Problem(f"{a} out of {b}", f"{a * 100 // b}%") for a, b in [(13, 100), (9, 10), (12, 50), (3, 5), (7, 25), (1, 4), (20, 20), (11, 20)]]),
     S("Solve", [Problem("A basketball player made 17 of 20 free throws. What percent did she make?", "85%", space=30), Problem("Lillie answered 46 of 50 questions correctly. Her percent score?", "92%", space=30)]),
     S("Exit Ticket", [Problem("Explain why 50% of something is half of it.", "50 per 100 = 1/2".replace("1/2", F(1, 2)), lines=2, space=0, wide=True)], cols=1)],
    TE("Students understand percent as a rate per 100.", "Use proportional relationships to solve percent problems.", "Hundred grids, workbook Lesson 2.1",
       flow("25 × 4.", "Read Let's Explore.", ["Shade 35 on a hundred grid; show the double number line.", "Say: Percent means per hundred."], "Try It 1–3."),
       ["Treating 7 out of 20 as 7%."], ["Scale to 100 with a double number line."], ["Find percents in the news."]),
    summary="Percent means per 100. Scale a ratio to a whole of 100 to find the percent.")

L2 = Lesson("2.2", "Percents, Fractions, and Decimals",
    "I can write percents as fractions and decimals, and fractions and decimals as percents.", "7.RP.3, 7.NS.2d",
    [],
    f"Which is greater: {F(3, 8)}, 0.4, or 37%?",
    [Figure(lambda t: table(t, [["Percent", "Fraction", "Decimal"], ["50%", P(F(1, 2), t.cell), "0.5"], ["25%", P(F(1, 4), t.cell), "0.25"], ["20%", P(F(1, 5), t.cell), "0.2"],
                                ["10%", P(F(1, 10), t.cell), "0.1"], ["75%", P(F(3, 4), t.cell), "0.75"], ["12.5%", P(F(1, 8), t.cell), "0.125"]], [1.4 * inch, 1.4 * inch, 1.4 * inch], width=4.2 * inch)),
     Bullets(["Percent → decimal: divide by 100 (move the decimal point 2 places left). 37% = 0.37.",
              "Decimal → percent: multiply by 100. 0.4 = 40%.",
              f"Fraction → percent: divide, then multiply by 100. {F(3, 8)} = 3 ÷ 8 = 0.375 = 37.5%."]),
     Example("Compare", f"{F(3, 8)}, 0.4, 37%", [f"{F(3, 8)} = 37.5%; 0.4 = 40%; 37%."], "0.4 is greatest; 37% is least"),
     KeyIdea("Change everything to the same form to compare.")],
    [Problem("0.06 as a percent", "6%"), Problem("145% as a decimal", "1.45"), Problem(f"{F(7, 20)} as a percent", "35%")],
    [S("Warm-Up", [Problem("3 ÷ 8", "0.375"), Problem("0.4 × 100", "40")]),
     S("Complete", [Problem("62% = ___ (decimal)", "0.62"), Problem("8% = ___ (decimal)", "0.08"), Problem("0.9 = ___%", "90%"), Problem("1.25 = ___%", "125%"),
                    Problem(f"{F(2, 5)} = ___%", "40%"), Problem(f"{F(5, 8)} = ___%", "62.5%"), Problem(f"30% = ___ (fraction, simplest)", F(3, 10)), Problem(f"64% = ___ (fraction)", F(16, 25))]),
     S("Order from least to greatest", [Problem(f"{F(2, 3)}, 0.65, 64%", f"64%, 0.65, {F(2, 3)}", wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain why 0.05 is 5%, not 50%.", "0.05 = 5 hundredths = 5 per 100.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students convert among percents, fractions, and decimals.", "Convert a rational number to a decimal using long division; use percents.", "Workbook Lesson 2.2",
       flow("3 ÷ 8.", "Read Let's Explore.", ["Fill in the benchmark table from memory together.", "Model each conversion."], "Try It 1–3."), ["Writing 0.05 as 50%."], ["Place-value chart."], ["Memorize the benchmark table."]),
    summary="Percent ↔ decimal: ×100 or ÷100. Fraction → percent: divide, then ×100.")

L3 = Lesson("2.3", "Finding a Percent of a Number",
    "I can find a percent of a number using models and multiplication.", "7.RP.3",
    [],
    "A $60 jacket is 30% off. How many dollars do you save?",
    [Figure(lambda t: percent_bar(t, 30, "$60 is 100%", "30%")),
     Text("10% of 60 is 6, so 30% is 3 × 6 = 18. Or multiply: 0.30 × 60 = 18."),
     Example("Use 10%", "30% of $60", ["10% of 60 = 6.", "30% = 3 × 6 = 18."], "$18"),
     Example("Multiply by the decimal", "15% of 240", ["0.15 × 240 = 36."], "36"),
     KeyIdea("Percent of a number = percent (as a decimal) × number. 10% and 1% are quick building blocks.")],
    [Problem("20% of 85", "17"), Problem("7% of 300", "21"), Problem("120% of 50", "60")],
    [S("Warm-Up", [Problem("10% of 60", "6"), Problem("0.15 × 240", "36")]),
     S("Find", [Problem(f"{p}% of {n}", f"{p * n / 100:g}") for p, n in [(10, 90), (25, 64), (40, 35), (5, 180), (75, 48), (12, 250), (150, 30), (1, 600)]]),
     S("Solve", [Problem("A school has 450 students. 22% play an instrument. How many?", "99 students", space=30), Problem("A $25 meal plus an 18% tip. How much is the tip?", "$4.50", space=30)]),
     S("Exit Ticket", [Problem("Find 35% of 80 two different ways.", "28 (3.5 × 8; 0.35 × 80)", lines=2, space=0, wide=True)], cols=1)],
    TE("Students find a percent of a quantity.", "Use proportional relationships to solve percent problems.", "Workbook Lesson 2.3",
       flow("10% of 60.", "Read Let's Explore.", ["Use the percent bar, then multiplication."], "Try It 1–3."), ["Multiplying by 30 instead of 0.30."], ["Use 10% and 1% building blocks."], ["Compute tips at a restaurant."]),
    summary="Multiply the number by the percent as a decimal, or build from 10% and 1%.")

L4 = Lesson("2.4", "Finding What Percent",
    "I can find what percent one number is of another.", "7.RP.3",
    [],
    "Ellie scored 42 points out of 48 on a test. What percent is that?",
    [Text("Divide the part by the whole, then write the decimal as a percent."),
     Example("Part ÷ whole", "42 out of 48", ["42 ÷ 48 = 0.875.", "0.875 = 87.5%."], "87.5%"),
     Example("More than 100%", "This year's garden produced 90 tomatoes. Last year it produced 60. This year is what percent of last year?", ["90 ÷ 60 = 1.5 = 150%."], "150%"),
     KeyIdea("Percent = part ÷ whole × 100%.")],
    [Problem("What percent of 80 is 20?", "25%"), Problem("What percent of 50 is 7?", "14%"), Problem("What percent of 40 is 52?", "130%")],
    [S("Warm-Up", [Problem("42 ÷ 48", "0.875"), Problem("0.875 = ___%", "87.5%")]),
     S("What percent?", [Problem(f"{a} of {b}", f"{a / b * 100:g}%") for a, b in [(9, 36), (24, 30), (13, 52), (45, 60), (3, 12), (66, 55)]]),
     S("Solve", [Problem("A team won 27 of 36 games. What percent did it win?", "75%", space=30), Problem("A store sold 340 of its 400 jackets. What percent are left?", "15%", space=30)]),
     S("Exit Ticket", [Problem("A shirt costs $12. A sweater costs $30. The shirt's price is what percent of the sweater's?", "40%", space=30, wide=True)], cols=1)],
    TE("Students find what percent one number is of another.", "Solve percent problems.", "Workbook Lesson 2.4", flow("42 ÷ 48.", "Read Let's Explore.", ["Work both examples. Identify part and whole first."], "Try It 1–3. Weekly Check tomorrow."),
       ["Dividing whole by part."], ["Label part and whole."], ["Track your free throws and compute your percent."]),
    summary="Percent = part ÷ whole, then × 100%.")

L5 = Lesson("2.5", "Finding the Whole",
    "I can find the whole when I know a part and its percent.", "7.RP.3",
    [],
    "Lillie has saved $45, which is 30% of the cost of a bike. How much does the bike cost?",
    [Figure(lambda t: double_line(t, ["0%", "10%", "30%", "100%"], [0, "$15", "$45", "?"], "percent", "dollars", blanks=(3,))),
     Example("Use 10%", "30% is $45", ["10% is 45 ÷ 3 = 15.", "100% is 15 × 10 = 150."], "$150"),
     Example("Divide by the percent", "30% of the whole is 45", ["0.30 × w = 45.", "w = 45 ÷ 0.30 = 150."], "$150"),
     KeyIdea("Whole = part ÷ percent (as a decimal).")],
    [Problem("20% of what number is 14?", "70"), Problem("75% of what number is 60?", "80"), Problem("8 is 40% of what?", "20")],
    [S("Warm-Up", [Problem("45 ÷ 0.30", "150"), Problem("If 10% is 7, 100% is ___", "70")]),
     S("Find the whole", [Problem(f"{p}% of ___ is {part}", f"{part * 100 / p:g}") for p, part in [(10, 12), (25, 9), (50, 37), (60, 42), (5, 3), (125, 50)]]),
     S("Solve", [Problem("A player scored 24 points, which was 40% of the team's points. How many points did the team score?", "60 points", space=30),
                 Problem("Ellie paid a $6 deposit, which is 15% of the price. What is the price?", "$40", space=30)]),
     S("Exit Ticket", [Problem("18 students walk to school. That is 12% of the school. How many students attend?", "150 students", space=30, wide=True)], cols=1)],
    TE("Students find the whole given a part and a percent.", "Solve percent problems.", "Workbook Lesson 2.5", flow("Warm-up.", "Read Let's Explore.", ["Double number line, then equation."], "Try It 1–3."),
       ["Multiplying the part by the percent."], ["Ask: is the whole bigger or smaller than the part?"], ["Find the original price from a discount amount."]),
    summary="Whole = part ÷ percent. Check: the whole should be larger than the part when the percent is under 100%.")

L6 = Lesson("2.6", "The Percent Equation",
    "I can use part = percent × whole to solve any percent problem.", "7.RP.3, 7.EE.4",
    [("percent equation", "part = percent × whole")],
    "All percent problems have three numbers: a part, a percent, and a whole. If you know two, you can find the third.",
    [Figure(lambda t: table(t, [["Unknown", "Equation", "Example"], ["part", "p = 0.25 × 80", "20"], ["percent", "20 = r × 80", "r = 0.25 = 25%"], ["whole", "20 = 0.25 × w", "w = 80"]],
                            [1.2 * inch, 2.0 * inch, 2.0 * inch], width=5.2 * inch)),
     Example("Find the whole", "36 is 45% of what number?", ["36 = 0.45 × w.", "w = 36 ÷ 0.45 = 80."], "80"),
     KeyIdea("part = percent × whole. Substitute what you know, then solve.")],
    [Problem("What is 64% of 75?", "48"), Problem("27 is what percent of 90?", "30%"), Problem("33 is 55% of what?", "60")],
    [S("Warm-Up", [Problem("36 ÷ 0.45", "80"), Problem("0.64 × 75", "48")]),
     S("Write an equation and solve", [Problem("What is 18% of 350?", "63"), Problem("42 is what percent of 168?", "25%"), Problem("91 is 70% of what?", "130"),
                                       Problem("What is 2.5% of 400?", "10"), Problem("60 is what percent of 48?", "125%"), Problem("15 is 6% of what?", "250")]),
     S("Exit Ticket", [Problem("Write and solve: 14 is 35% of what number?", "14 = 0.35w; w = 40", space=30, wide=True)], cols=1)],
    TE("Students use the percent equation.", "Solve problems using equations; use proportional relationships for percent problems.", "Workbook Lesson 2.6", flow("Warm-up.", "Read Let's Explore.", ["Teach part = percent × whole with the three cases."], "Try It 1–3."),
       ["Using the percent as a whole number in the equation."], ["Convert percent to decimal first."], ["Solve with a proportion too and compare."]),
    summary="Use part = percent × whole to find any missing value.")

L7 = Lesson("2.7", "Percents Greater Than 100% and Less Than 1%",
    "I can work with percents greater than 100% and less than 1%.", "7.RP.3",
    [],
    "A town's population grew to 250% of what it was. A bank pays 0.5% interest. What do these mean?",
    [Text("250% means 2.5 times the whole. 0.5% means half of 1 percent: 0.005 times the whole."),
     Example("Greater than 100%", "250% of 80", ["2.5 × 80 = 200."], "200"),
     Example("Less than 1%", "0.5% of $2,000", ["0.005 × 2,000 = 10."], "$10"),
     WatchOut("0.5% is not 0.5. As a decimal, 0.5% = 0.005."),
     KeyIdea("Percent → decimal: divide by 100, even for 250% (2.5) or 0.5% (0.005).")],
    [Problem("300% of 15", "45"), Problem("0.2% of 5,000", "10"), Problem("125% as a decimal", "1.25")],
    [S("Warm-Up", [Problem("2.5 × 80", "200"), Problem("0.005 × 2,000", "10")]),
     S("Find", [Problem("200% of 34", "68"), Problem("110% of 60", "66"), Problem("0.1% of 9,000", "9"), Problem("0.75% of 400", "3"), Problem("175% of 20", "35"), Problem("0.4% as a decimal", "0.004")]),
     S("Solve", [Problem("A puppy's weight is now 300% of its birth weight of 2.5 lb. How much does it weigh?", "7.5 lb", space=30), Problem("A savings account earns 0.6% per year on $1,500. How much interest in 1 year?", "$9", space=30)]),
     S("Exit Ticket", [Problem("Is 150% of a number more or less than the number? Explain.", "More; it is 1.5 times the number.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students work with very large and very small percents.", "Solve percent problems.", "Workbook Lesson 2.7", flow("Warm-up.", "Read Let's Explore.", ["Work examples; stress the Watch Out."], "Try It 1–3."),
       ["0.5% = 0.5."], ["Use a place-value chart."], ["Find a real example of a percent over 100%."]),
    summary="Percents over 100% mean more than the whole; under 1% means less than a hundredth.")

L8 = Lesson("2.8", "Estimating with Percents",
    "I can estimate percents using benchmarks like 10%, 25%, and 50%.", "7.RP.3, 7.EE.3",
    [],
    "A $39.95 shirt is 25% off. About how much will it cost?",
    [Example("Benchmark", "25% off $39.95", ["Round to $40.", "25% of 40 = 10.", "40 − 10 = 30."], "about $30"),
     Example("Tip estimate", "A 20% tip on $47.80", ["Round to $48. 10% = $4.80, so 20% ≈ $9.60."], "about $10"),
     KeyIdea("10%: move the decimal point one place left. 5% is half of 10%. 25% is a quarter. 50% is half.")],
    [Problem("Estimate 10% of $83.20", "about $8.30"), Problem("Estimate 15% of $59", "about $9"), Problem("Estimate 48% of 202", "about 100")],
    [S("Warm-Up", [Problem("10% of 47.80", "4.78"), Problem("Half of 4.80", "2.40")]),
     S("Estimate", [Problem("20% of $31.75", "about $6.40"), Problem("25% of 397", "about 100"), Problem("5% of $198", "about $10"), Problem("33% of 61", "about 20"),
                    Problem("Tip of 18% on $52", "about $9–10"), Problem("75% of 81", "about 60")]),
     S("Exit Ticket", [Problem("Explain how to find 15% of a restaurant bill in your head.", "Find 10%, take half of it for 5%, and add.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students estimate percents with benchmarks.", "Use mental computation and estimation strategies to assess reasonableness.", "Workbook Lesson 2.8, restaurant receipts", flow("Warm-up.", "Read Let's Explore.", ["Teach 10%, 5%, 25%, 50% shortcuts."], "Try It 1–3. Weekly Check tomorrow."),
       ["Moving the decimal the wrong way for 10%."], ["Use money examples."], ["Estimate tips on real receipts."]),
    summary="Use 10%, 5%, 25%, and 50% benchmarks to estimate quickly.")

L9 = Lesson("2.9", "Discounts and Sale Prices",
    "I can find the sale price after a percent discount.", "7.RP.3",
    [("discount", "An amount taken off the original price."), ("sale price", "The price after the discount.")],
    "A $80 pair of shoes is 25% off. What is the sale price?",
    [Example("Subtract the discount", "25% off $80", ["Discount: 0.25 × 80 = 20.", "Sale price: 80 − 20 = 60."], "$60"),
     Example("Multiply by what's left", "25% off means you pay 75%", ["0.75 × 80 = 60."], "$60"),
     KeyIdea("Sale price = original × (100% − discount%).")],
    [Problem("40% off $45", "$27"), Problem("15% off $120", "$102"), Problem("A $90 coat is on sale for $63. What percent off?", "30%")],
    [S("Warm-Up", [Problem("0.25 × 80", "20"), Problem("100% − 15%", "85%")]),
     S("Find the sale price", [Problem(f"{p}% off {m(v)}", m(v * (100 - p) / 100)) for p, v in [(20, 35), (30, 50), (10, 89.90), (35, 60), (50, 27.80), (12, 250)]]),
     S("Solve", [Problem("A video game costs $59.99. It is 30% off. What is the sale price?", "$41.99", space=30), Problem("A $150 bike is on sale for $105. What is the percent discount?", "30%", space=30)]),
     S("Exit Ticket", [Problem("Is 20% off and then another 20% off the same as 40% off? Try it with $100.", "No: $100 → $80 → $64 (36% off).", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compute discounts and sale prices.", "Use proportional relationships to solve multistep percent problems: discounts.", "Store ads, workbook Lesson 2.9", flow("Warm-up.", "Read Let's Explore.", ["Two methods."], "Try It 1–3."),
       ["Adding the discount."], ["Write ‘you pay ___%’."], ["Compare real sale ads."]),
    summary="Sale price = original × (100% − discount).")

L10 = Lesson("2.10", "Markups and Sales Tax",
    "I can find prices after a markup or sales tax.", "7.RP.3",
    [("markup", "An amount added to the cost to set the selling price."), ("sales tax", "A percent of the price added at the register.")],
    "Mississippi's state sales tax is 7%. What is the total for a $40 purchase?",
    [Example("Sales tax", "7% tax on $40", ["Tax: 0.07 × 40 = 2.80.", "Total: 40 + 2.80 = 42.80."], "$42.80"),
     Example("Markup", "A store buys a lamp for $25 and marks it up 60%.", ["Markup: 0.60 × 25 = 15.", "Price: 25 + 15 = 40. Or 1.60 × 25 = 40."], "$40"),
     KeyIdea("Total with tax or markup = original × (100% + percent).")],
    [Problem("7% tax on $15", "$1.05 tax; $16.05 total"), Problem("Markup 40% on $30", "$42"), Problem("Total with 8% tax on $62.50", "$67.50")],
    [S("Warm-Up", [Problem("0.07 × 40", "2.80"), Problem("1.6 × 25", "40")]),
     S("Find the total", [Problem(f"{p}% tax on {m(v)}", m(round(v * (100 + p) / 100, 2))) for p, v in [(7, 20), (7, 64), (5, 38)]] + [Problem(f"{p}% markup on {m(v)}", m(v * (100 + p) / 100)) for p, v in [(50, 18), (25, 64), (120, 15)]]),
     S("Solve", [Problem("A bookstore buys a book for $12 and sells it for $18. What is the percent markup?", "50%", space=30), Problem("Lillie buys $28.50 of supplies with 7% tax. What does she pay?", "$30.50 (30.495 rounds to 30.50)", space=30)]),
     S("Exit Ticket", [Problem("A $50 item has a 20% markup, then a 20% discount. What is the final price?", "$48", space=30, wide=True)], cols=1)],
    TE("Students compute markups and sales tax.", "Solve multistep percent problems: tax, markups.", "Receipts, workbook Lesson 2.10", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."),
       ["Subtracting tax."], ["Write ‘you pay ___%’ (e.g., 107%)."], ["Check tax on a real receipt."]),
    summary="Add the percent: total = original × (100% + percent).")

L11 = Lesson("2.11", "Percent Increase and Decrease",
    "I can find the percent of increase or decrease.", "7.RP.3",
    [("percent change", "The amount of change divided by the original amount, as a percent.")],
    "A puppy weighed 8 pounds in March and 14 pounds in June. By what percent did its weight increase?",
    [Example("Increase", "8 lb → 14 lb", ["Change: 14 − 8 = 6.", "6 ÷ 8 = 0.75 = 75%."], "75% increase"),
     Example("Decrease", "A town had 2,500 people and now has 2,200.", ["Change: 300.", "300 ÷ 2,500 = 0.12 = 12%."], "12% decrease"),
     WatchOut("Always divide by the <b>original</b> amount, not the new amount."),
     KeyIdea("Percent change = change ÷ original × 100%.")],
    [Problem("$40 → $50", "25% increase"), Problem("80 → 60", "25% decrease"), Problem("150 → 165", "10% increase")],
    [S("Warm-Up", [Problem("6 ÷ 8", "0.75"), Problem("300 ÷ 2,500", "0.12")]),
     S("Find the percent change", [Problem(f"{a} → {b}", f"{abs(b - a) / a * 100:g}% {'increase' if b > a else 'decrease'}") for a, b in [(20, 25), (50, 35), (12, 18), (200, 170), (64, 80), (90, 63)]]),
     S("Solve", [Problem("A gallon of milk went from $3.20 to $3.60. Percent increase?", "12.5%", space=30), Problem("A plant was 15 cm tall and is now 24 cm. Percent increase?", "60%", space=30)]),
     S("Exit Ticket", [Problem("A price goes from $50 to $100, then back to $50. Are the percent changes the same? Explain.", "No: +100%, then −50% (different originals).", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compute percent increase and decrease.", "Solve multistep percent problems: percent increase and decrease.", "Workbook Lesson 2.11", flow("Warm-up.", "Read Let's Explore.", ["Work both examples; stress dividing by the original."], "Try It 1–3."),
       ["Dividing by the new amount."], ["Label original and new."], ["Track a price over months."]),
    summary="Percent change = change ÷ original.")

L12 = Lesson("2.12", "Tips, Commissions, and Fees",
    "I can solve problems with tips, commissions, and fees.", "7.RP.3",
    [("tip (gratuity)", "Money paid for a service, often a percent of the bill."), ("commission", "Pay earned as a percent of sales.")],
    "A salesperson earns 6% commission. She sells a $1,250 sofa. How much does she earn?",
    [Example("Commission", "6% of $1,250", ["0.06 × 1,250 = 75."], "$75"),
     Example("Tip", "18% tip on a $42 meal", ["0.18 × 42 = 7.56.", "Total: 42 + 7.56 = 49.56."], "$7.56 tip; $49.56 total"),
     KeyIdea("Tips, commissions, and fees are all “percent of” problems.")],
    [Problem("15% tip on $36", "$5.40"), Problem("4% commission on $8,500", "$340"), Problem("3% card fee on $120", "$3.60")],
    [S("Warm-Up", [Problem("0.06 × 1,250", "75"), Problem("0.18 × 42", "7.56")]),
     S("Solve", [Problem("20% tip on a $55 dinner. Total?", "$66"), Problem("5% commission on a $24,000 car", "$1,200"), Problem("A $2 fee plus 10% on a $30 ticket. Total?", "$35"),
                 Problem("Lillie earns $8 per hour plus 10% of her sales. She works 5 hours and sells $300. Pay?", "$70"), Problem("15% tip on a $28.40 haircut", "$4.26"), Problem("A real estate agent earns 3% on a $180,000 house", "$5,400")]),
     S("Exit Ticket", [Problem("Which earns more: 8% commission on $2,500 or a flat $175?", "8% commission ($200)", space=30, wide=True)], cols=1)],
    TE("Students solve tip, commission, and fee problems.", "Solve multistep percent problems: tips, commissions, fees.", "Workbook Lesson 2.12", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3. Weekly Check tomorrow."),
       ["Forgetting to add the tip to the total when asked."], ["Underline what the question asks."], ["Research how commissions work in a job you like."]),
    summary="Tips, commissions, and fees are percents of an amount.")

L13 = Lesson("2.13", "Simple Interest",
    "I can find simple interest and the total amount in an account or loan.", "7.RP.3, 7.EE.3",
    [("interest", "Money paid for using money: earned on savings or paid on loans."), ("principal", "The original amount saved or borrowed."),
     ("simple interest", "I = P × r × t: principal × yearly rate × years.")],
    "Grandpa puts $500 in a savings account that pays 3% simple interest each year. How much interest after 4 years?",
    [Example("Simple interest", "P = $500, r = 3%, t = 4 years", ["I = 500 × 0.03 × 4 = 60.", "Total: 500 + 60 = 560."], "$60 interest; $560 total"),
     Example("A loan", "Borrow $1,200 at 6% simple interest for 2 years.", ["I = 1,200 × 0.06 × 2 = 144.", "Total to repay: $1,344."], "$1,344"),
     KeyIdea("I = P × r × t. Use r as a decimal and t in years.")],
    [Problem("$800 at 5% for 3 years", "$120 interest"), Problem("$2,000 at 4.5% for 2 years. Total?", "$2,180"), Problem("$300 at 2% for 6 months (0.5 year)", "$3 interest")],
    [S("Warm-Up", [Problem("500 × 0.03", "15"), Problem("15 × 4", "60")]),
     S("Find the interest and total", [Problem(f"{m(Pp)} at {r}% for {tt} years", f"I = {m(Pp * r / 100 * tt)}; total {m(Pp + Pp * r / 100 * tt)}") for Pp, r, tt in [(400, 5, 2), (1500, 3, 4), (250, 8, 1), (6000, 2.5, 3)]]),
     S("Solve", [Problem("Which earns more: $1,000 at 4% for 3 years or $1,200 at 3% for 3 years?", "$1,000 at 4% ($120 vs $108)", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain why borrowing money costs more than the amount borrowed.", "You pay back the principal plus interest.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compute simple interest.", "Solve multistep percent problems: simple interest.", "Workbook Lesson 2.13", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."),
       ["Using r = 3 instead of 0.03."], ["Formula card."], ["Compare a real bank's savings rate."]),
    summary="Simple interest I = P × r × t.")

L14 = Lesson("2.14", "Percent Error",
    "I can find the percent error of an estimate or measurement.", "7.RP.3",
    [("percent error", "How far off an estimate is, as a percent of the actual value: |estimate − actual| ÷ actual × 100%.")],
    "Ellie guessed there were 120 jelly beans in a jar. There were actually 150. How far off was she, as a percent?",
    [Example("Percent error", "Guess 120, actual 150", ["Error: |120 − 150| = 30.", "30 ÷ 150 = 0.2 = 20%."], "20% error"),
     KeyIdea("Percent error = |estimate − actual| ÷ actual × 100%. Always divide by the actual value.")],
    [Problem("Estimate 45, actual 50", "10%"), Problem("Measured 8.4 cm, actual 8 cm", "5%"), Problem("Guessed 300, actual 240", "25%")],
    [S("Warm-Up", [Problem("|120 − 150|", "30"), Problem("30 ÷ 150", "0.2")]),
     S("Find the percent error", [Problem(f"Estimate {e}, actual {a}", f"{abs(e - a) / a * 100:g}%") for e, a in [(90, 100), (55, 50), (18, 24), (420, 400), (3.6, 4), (130, 125)]]),
     S("Exit Ticket", [Problem("Lillie estimated a room was 12 ft long. It was 15 ft. Find the percent error.", "20%", space=30, wide=True)], cols=1)],
    TE("Students compute percent error.", "Solve multistep percent problems, including percent error.", "Jar of objects for estimating, workbook Lesson 2.14", flow("Warm-up.", "Read Let's Explore. Estimate a jar count.", ["Work the example."], "Try It 1–3."),
       ["Dividing by the estimate."], ["Absolute value bars mean ‘distance’."], ["Estimation contest at home."]),
    summary="Percent error = |estimate − actual| ÷ actual.")

L15 = Lesson("2.15", "Multi-Step Percent Problems",
    "I can solve problems that combine discounts, tax, tips, and percent change.", "7.RP.3",
    [],
    "A $60 game is 25% off, and then 7% tax is added. What is the total?",
    [Example("Discount, then tax", "$60, 25% off, 7% tax", ["Sale: 0.75 × 60 = 45.", "Total: 1.07 × 45 = 48.15."], "$48.15"),
     Example("Two changes", "A price rises 10%, then falls 10%. Start at $100.", ["100 × 1.10 = 110.", "110 × 0.90 = 99."], "$99, not $100!"),
     KeyIdea("Apply each percent in order to the current amount.")],
    [Problem("$40 shirt, 20% off, then 7% tax", "$34.24"), Problem("$25 meal, 8% tax, then 20% tip on the pre-tax amount. Total?", "$32"), Problem("$200 rises 25%, then falls 20%", "$200")],
    [S("Warm-Up", [Problem("0.75 × 60", "45"), Problem("1.07 × 45", "48.15")]),
     S("Solve", [Problem("A $120 jacket is 30% off. Tax is 7%. Total?", "$89.88", space=40, wide=True), Problem("A family's dinner is $64. Tax is 7% and they tip 18% of $64. Total?", "$80.00 ($64 + $4.48 + $11.52)", space=40, wide=True),
                 Problem("A stock worth $50 rises 20% and then falls 15%. What is it worth?", "$51", space=40, wide=True), Problem("A store marks up a $30 item 50%, then puts it on sale for 20% off. Sale price?", "$36", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Does the order of a 10% discount and 7% tax matter for the final price? Test with $100.", "No: 100 × 0.9 × 1.07 = 100 × 1.07 × 0.9 = 96.30", lines=2, space=0, wide=True)], cols=1)],
    TE("Students solve multi-step percent problems.", "Use proportional relationships to solve multistep ratio and percent problems.", "Workbook Lesson 2.15", flow("Warm-up.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."),
       ["Adding percents (25% off + 7% tax = 18% off)."], ["Step-by-step table."], ["Plan a shopping trip with a budget."]),
    summary="Apply percents one step at a time to the current amount.")

L16 = Lesson("2.16", "Percent Problem Solving",
    "I can choose and use the right percent strategy to solve real problems.", "7.RP.3",
    [],
    "Plan a back-to-school shopping trip: a $35 backpack (20% off), $48 shoes (25% off), 7% tax. You have $75. Is it enough?",
    [Example("Plan", "Backpack and shoes", ["Backpack: 0.8 × 35 = 28.", "Shoes: 0.75 × 48 = 36.", "Subtotal 64; tax 1.07 × 64 = 68.48."], "Yes, $68.48 ≤ $75, with $6.52 left"),
     KeyIdea("Read carefully, decide what is the whole, and apply each percent in order.")],
    [Problem("What percent of 64 is 16?", "25%"), Problem("12% of what is 9?", "75"), Problem("$75 → $90 percent change", "20% increase")],
    [S("Warm-Up", [Problem("0.8 × 35", "28"), Problem("1.07 × 64", "68.48")]),
     S("Mixed practice", [Problem("35% of 260", "91"), Problem("54 is what percent of 72?", "75%"), Problem("27 is 45% of what?", "60"), Problem("Sale price: 15% off $86", "$73.10"),
                          Problem("I for $900 at 4% for 5 years", "$180"), Problem("Percent error: estimate 38, actual 40", "5%")]),
     S("Exit Ticket", [Problem("Write a multi-step percent problem about something you want to buy. Solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve mixed percent problems.", "7.RP.3 review.", "Workbook Lesson 2.16, Unit 2 Review", flow("Warm-up.", "Read Let's Explore.", ["Work the plan example."], "Try It 1–3.", "Workbook Lesson 2.16 and the Unit 2 Review.", "Check. Tomorrow: Unit 2 Test."),
       ["Using the wrong whole."], ["Identify part, percent, whole."], ["Budget a real purchase."]),
    summary="Identify the part, percent, and whole; apply percents step by step.")

C1 = Check("Weekly Check 4: Percent Basics", [S("Show what you know", [Problem("9 out of 20 = ___%", "45%"), Problem(f"{F(3, 8)} = ___%", "37.5%"), Problem("0.07 = ___%", "7%"),
    Problem("30% of 70", "21"), Problem("What percent of 60 is 45?", "75%"), Problem("A team won 14 of 16 games. Percent won?", "87.5%")])], minutes=15)
C2 = Check("Weekly Check 5: Percent Equations", [S("Show what you know", [Problem("40% of what is 26?", "65"), Problem("18 is what percent of 24?", "75%"), Problem("250% of 18", "45"),
    Problem("0.3% of 2,000", "6"), Problem("Estimate 15% of $79.", "about $12"), Problem("Write and solve: 63 is 35% of n.", "63 = 0.35n; n = 180", lines=1, space=0)])], minutes=20)
C3 = Check("Weekly Check 6: Discounts, Tax, and Change", [S("Show what you know", [Problem("35% off $80", "$52"), Problem("7% tax on $45", "$48.15 total"), Problem("$30 → $36 percent change", "20% increase"),
    Problem("$250 → $200 percent change", "20% decrease"), Problem("18% tip on $50", "$9"), Problem("6% commission on $3,500", "$210")])], minutes=20)

REVIEW = Check("Unit 2 Review", [
    S("Percent basics", [Problem("0.45 = ___%", "45%"), Problem(f"{F(7, 8)} = ___%", "87.5%"), Problem("24% of 150", "36"), Problem("What percent of 80 is 68?", "85%"), Problem("15 is 60% of what?", "25")]),
    S("Applications", [Problem("25% off $64, then 7% tax", "$51.36"), Problem("Percent change: 40 → 52", "30% increase"), Problem("I = ? for $2,500 at 3% for 4 years", "$300"), Problem("Percent error: guess 90, actual 75", "20%")])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 2 Test", [
    S("Part A · Percent basics (1 point each)", [Problem("13 out of 25 = ___%", "52%"), Problem("1.8 = ___%", "180%"), Problem(f"{F(5, 8)} = ___%", "62.5%"), Problem("0.4% as a decimal", "0.004")]),
    S("Part B · Percent equations (1 point each)", [Problem("16% of 75", "12"), Problem("What percent of 120 is 42?", "35%"), Problem("51 is 85% of what?", "60"), Problem("150% of 46", "69"), Problem("Estimate 18% of $41", "about $8")]),
    S("Part C · Applications (2 points each)", [Problem("A $72 jacket is 35% off. Sale price?", "$46.80", space=30, points=2), Problem("A $36 meal with 7% tax and a 20% tip on $36. Total?", "$45.72", space=30, points=2),
        Problem("A town grew from 4,800 to 5,520 people. Percent increase?", "15%", space=30, points=2), Problem("$1,800 at 3.5% simple interest for 3 years. Interest?", "$189", space=30, points=2)]),
    S("Part D · Problem solving (3 points each)", [
        Problem("Store A sells a $90 bike at 30% off. Store B sells the same bike for $70 with a $5 coupon. Which is cheaper, and by how much?", "Store A: $63 (0.70 × 90). Store B: $65. Store A is $2 cheaper.", space=60, wide=True, points=3),
        Problem("Lillie guessed a pumpkin weighed 12 lb. It weighed 15 lb. Ellie guessed 17 lb. Who had the smaller percent error?", "Ellie (13.3%) vs Lillie (20%): Ellie", space=60, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["20–23 (85%+)", "Mastered."], ["17–19", "Proficient; correct missed items."], ["Below 17", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-11-09", "2026-11-16", "2026-11-30", "2026-12-07"], CHECKS, REVIEW, TEST)

UNIT = Unit(2, "Percents", "Percent as a rate per 100, percent equations, discounts, tax, tips, percent change, interest, and percent error.",
    "Percents are rates per 100, and they are everywhere: sales, taxes, grades, interest, and statistics. You will use proportional reasoning and the percent equation to solve real percent problems.",
    ["Understand percent as a rate per 100.", "Convert among percents, fractions, and decimals.", "Find a part, a percent, or a whole.",
     "Solve discount, markup, tax, tip, and commission problems.", "Find percent change, simple interest, and percent error."],
    [("7.RP.3", "Use proportional relationships to solve multistep ratio and percent problems: simple interest, tax, markups and markdowns, gratuities and commissions, fees, percent increase and decrease, percent error."),
     ("7.EE.3", "Solve multi-step real-life problems with positive and negative rational numbers; assess reasonableness using estimation.")],
    [("percent", "A rate per 100."), ("discount", "Amount off a price."), ("markup", "Amount added to cost."), ("percent change", "Change ÷ original."), ("simple interest", "I = P × r × t."), ("percent error", "|estimate − actual| ÷ actual.")],
    ["Proportional relationships (Unit 1).", "Decimal multiplication and division."], ["Calculator for checking", "Store ads and receipts", "Hundred grids"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Percents decide sale prices, sales tax, tips, test grades, loan costs, and savings growth.",
    family_note="Let your student calculate the tip and tax at a restaurant or the sale price at a store this unit.",
    weeks=WEEKS)
