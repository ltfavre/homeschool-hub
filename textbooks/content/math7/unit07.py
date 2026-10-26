"""Grade 7 Math · Unit 7: Statistics and Probability (Apr 26 – May 21, 2027)."""
from fractions import Fraction as Fr
from itertools import product
from engine import *
from content.mathkit import F, RD
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


# ---------- statistics helpers (all answers computed) ----------
def mean(v): return Fr(sum(v), len(v))
def med(v):
    s = sorted(v); n = len(s)
    return Fr(s[n // 2]) if n % 2 else Fr(s[n // 2 - 1] + s[n // 2], 2)
def mad(v):
    m = mean(v); return Fr(sum(abs(x - m) for x in v), len(v))
def five(v):
    s = sorted(v); n = len(s)
    return (s[0], med(s[:n // 2]), med(s), med(s[(n + 1) // 2:]), s[-1])
def iqr(v):
    f = five(v); return f[3] - f[1]
def N(x):
    """Number to at most 2 decimals; ≈ when rounded."""
    r = round(float(x), 2); s = RD(r if r != int(r) else int(r))
    return s if Fr(str(r)) == Fr(x) else "≈ " + s
def P(n, d):
    """Probability as a reduced fraction."""
    f = Fr(n, d)
    return "0" if f == 0 else ("1" if f == 1 else F(f.numerator, f.denominator))
def show(v): return ", ".join(str(x) for x in v)


DICE = [(a, b) for a, b in product(range(1, 7), repeat=2)]
def dice(cond): return P(sum(1 for a, b in DICE if cond(a, b)), 36)


# ---------- data sets ----------
A6 = [3, 4, 4, 5, 5, 5, 6, 6, 7]          # Lesson 7.6 class A (minutes)
B6 = [6, 7, 7, 8, 8, 8, 9, 9, 10]         # Lesson 7.6 class B
TALL_A = [52, 54, 55, 56, 58, 59, 60, 61, 62, 64, 66]   # Lesson 7.7 inches
TALL_B = [56, 58, 60, 61, 62, 63, 64, 65, 66, 68, 70]
DS5 = [2, 4, 6, 8, 10]
DS5b = [12, 15, 15, 18, 20]
SAMP = [6, 8, 5, 7, 9]                     # red candies in five samples of 20


L1 = Lesson("7.1", "Populations and Samples",
    "I can tell the difference between a population and a sample.", "7.SP.1",
    [("population", "The entire group you want to know about."), ("sample", "A part of the population that is actually studied."), ("census", "Data collected from every member of a population.")],
    "You want to know the favorite lunch of every 7th grader in your state. Could you ask all of them? What could you do instead?",
    [Text("A <b>population</b> is the whole group you are curious about. Studying everyone is usually too slow or expensive, so statisticians study a <b>sample</b>, a smaller part of the population, and use it to learn about the whole."),
     Example("Identify", "A library asks 80 of its 2,000 members how often they visit.", ["Population: all 2,000 members.", "Sample: the 80 members surveyed."], "Population: 2,000 members; sample: 80 members"),
     KeyIdea("A sample is useful only when it represents the population well.")],
    [Problem("A chef tastes one spoonful of soup. Population? Sample?", "Population: the whole pot; sample: the spoonful", wide=True),
     Problem("A factory tests 50 of 10,000 light bulbs. Population? Sample?", "Population: 10,000 bulbs; sample: 50 bulbs", wide=True),
     Problem("When is a census a better choice than a sample?", "When the population is small, e.g. one class of 20", wide=True)],
    [S("Warm-Up", [Problem("What fraction of 2,000 is 80?", P(80, 2000)), Problem("What percent of 2,000 is 80?", "4%")]),
     S("Name the population and the sample", [
         Problem("A city surveys 400 residents about a new park.", "Population: all city residents; sample: 400 surveyed", lines=1, space=0, wide=True),
         Problem("A coach times 6 of her 30 swimmers.", "Population: 30 swimmers; sample: 6 swimmers", lines=1, space=0, wide=True),
         Problem("A scientist tags 25 frogs in a pond.", "Population: all frogs in the pond; sample: 25 frogs", lines=1, space=0, wide=True),
         Problem("A teacher checks every student's homework.", "Census: the whole class is studied", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Describe a question you could answer with a sample. Name the population and the sample.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students distinguish populations and samples.", "Understand that statistics can be used to gain information about a population by examining a sample.", "Workbook Lesson 7.1",
       flow("Percent warm-up.", "Discuss Let's Explore: could you ask everyone?", ["Define population, sample, census.", "Say: A spoonful of soup is a sample of the pot."], "Try It 1–3."),
       ["Calling the sample the population."], ["Ask: Who do we want to know about? Who did we actually ask?"], ["Find a survey in the news and name its population and sample."]),
    summary="Study a sample to learn about a population.")

L2 = Lesson("7.2", "Random Samples and Bias",
    "I can tell whether a sample is random and representative, or biased.", "7.SP.1",
    [("random sample", "A sample in which every member of the population has an equal chance of being chosen."), ("biased sample", "A sample that over- or under-represents part of the population.")],
    "To find the town's favorite sport, Ellie surveys people leaving a soccer game. Is that fair?",
    [Text("Ellie's sample is <b>biased</b>: people at a soccer game probably like soccer more than the town as a whole. A <b>random sample</b>, such as drawing names from the whole town's list, gives everyone the same chance and tends to <b>represent</b> the population."),
     Figure(lambda t: table(t, [["Sampling method", "Random?", "Why"], ["Draw 50 names from a hat with every student's name", "Yes", "Everyone has an equal chance"], ["Ask the first 50 students who arrive", "No", "Early arrivers may differ"],
                                ["Ask volunteers to answer online", "No", "Only people who care respond"], ["Number students; use a random-number generator", "Yes", "Equal chance"]], [3.1 * inch, 0.8 * inch, 2.0 * inch], width=5.9 * inch)),
     WatchOut("A large sample is not automatically fair. 1,000 biased answers are still biased."),
     KeyIdea("Random samples tend to be representative; samples that leave out groups are biased.")],
    [Problem("Survey the basketball team about favorite sports.", "Biased"), Problem("Roll a die to pick one student from each table group of 6.", "Random"), Problem("Ask your friends whom they will vote for.", "Biased")],
    [S("Warm-Up", [Problem("Name a population for “favorite sport in town.”", "All town residents"), Problem("Name a sample of that population.", "e.g. 100 residents chosen at random")]),
     S("Random or biased? Explain.", [
         Problem("A school picks 40 student ID numbers by computer to survey about lunch.", "Random: every student has an equal chance", lines=1, space=0, wide=True),
         Problem("A pet store asks its customers whether people in the city prefer cats or dogs.", "Biased: only pet store customers", lines=1, space=0, wide=True),
         Problem("A magazine asks readers to mail in opinions about the magazine.", "Biased: only motivated readers reply", lines=1, space=0, wide=True),
         Problem("A farmer tests corn from 10 spots chosen at random across the field.", "Random", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Describe a random way to choose 10 students from a school of 300.", "e.g. number students 1–300 and use a random-number generator", lines=2, space=0, wide=True)], cols=1)],
    TE("Students identify random and biased samples.", "Random sampling tends to produce representative samples and support valid inferences.", "Names in a hat (optional), workbook Lesson 7.2",
       flow("Warm-up.", "Discuss Ellie's soccer survey.", ["Go through the table.", "Ask: Who is left out?"], "Try It 1–3."),
       ["Thinking a big sample is always fair."], ["Ask: Does everyone have the same chance?"], ["Design a fair survey for the family."]),
    summary="Random samples give everyone an equal chance; biased samples leave groups out.")

L3 = Lesson("7.3", "Making Inferences from Samples",
    "I can use data from a random sample to estimate something about a population.", "7.SP.2",
    [("inference", "A conclusion about a population based on sample data.")],
    "In a random sample of 50 students, 18 prefer pizza for lunch. The school has 600 students. About how many prefer pizza?",
    [Example("Use a proportion", "18 of 50 prefer pizza; 600 students in all", [f"Sample rate: {F(18, 50)} = 36%.", f"36% of 600 = 0.36 × 600 = {int(Fr(18, 50) * 600)}."], f"about {int(Fr(18, 50) * 600)} students"),
     Example("Defects", "4 of 200 sampled phones are defective. Estimate for 15,000 phones.", [f"{F(4, 200)} = 2%.", f"0.02 × 15,000 = {int(Fr(4, 200) * 15000)}."], f"about {int(Fr(4, 200) * 15000)} phones"),
     KeyIdea("Sample rate × population size = estimate. Estimates are approximate, not exact.")],
    [Problem("12 of 40 sampled students walk to school. School: 500. Estimate walkers.", f"about {int(Fr(12, 40) * 500)}"),
     Problem("3 of 60 sampled apples are bruised. Shipment: 2,400. Estimate bruised.", f"about {int(Fr(3, 60) * 2400)}"),
     Problem("45 of 75 sampled voters favor a plan. Percent?", f"{int(Fr(45, 75) * 100)}%")],
    [S("Warm-Up", [Problem("18 ÷ 50 as a percent", "36%"), Problem("0.36 × 600", "216")]),
     S("Estimate for the population", [Problem(f"{a} of {b} in the sample; population {c:,}", f"about {int(Fr(a, b) * c):,}") for a, b, c in [(9, 30, 450), (14, 70, 1500), (6, 25, 800), (33, 120, 2400)]]),
     S("Solve", [Problem("A random sample of 80 households found 52 own a pet. The town has 6,000 households. Estimate the number with pets.", f"about {int(Fr(52, 80) * 6000):,}", space=24, wide=True),
                 Problem("A survey of 25 random students found 7 play an instrument. Estimate for 350 students.", f"about {int(Fr(7, 25) * 350)}", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Why should the sample be random for this estimate to be trusted?", "A biased sample would not match the population rate.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students estimate population values from samples.", "Use data from a random sample to draw inferences about a population.", "Workbook Lesson 7.3",
       flow("Percent warm-up.", "Read Let's Explore.", ["Proportion method, then percent method."], "Try It 1–3."),
       ["Using the sample count as the population count."], ["Write the rate as a percent first."], ["Sample the family's pantry and estimate."]),
    summary="Multiply the sample rate by the population size.")

_m = mean(SAMP)
L4 = Lesson("7.4", "Variability in Samples",
    "I can use several samples to judge how much an estimate might vary.", "7.SP.2",
    [("sampling variability", "The natural differences between results from different samples.")],
    "Five students each scoop 20 candies from the same jar and count the red ones. Will they all get the same number?",
    [Text("No! Different random samples give different results. That is <b>sampling variability</b>. Looking at several samples helps you see how much an estimate might change."),
     Figure(lambda t: table(t, [["Sample", "1", "2", "3", "4", "5"], ["Red (of 20)"] + [str(v) for v in SAMP], ["Percent red"] + [f"{int(Fr(v, 20) * 100)}%" for v in SAMP]], width=W * 0.8)),
     Example("Combine samples", "Estimate the percent of red candies in the jar.", [f"Mean red per sample: ({' + '.join(map(str, SAMP))}) ÷ 5 = {N(_m)}.", f"{N(_m)} ÷ 20 = {int(_m / 20 * 100)}%."], f"about {int(_m / 20 * 100)}%"),
     Example("Use it", "The jar holds 500 candies. About how many are red?", [f"{int(_m / 20 * 100)}% of 500."], f"about {int(_m / 20 * 500)}"),
     KeyIdea("Estimates from samples vary. Larger samples and more samples give more reliable estimates.")],
    [Problem("What is the range of the five percents above?", f"{int(Fr(min(SAMP), 20) * 100)}% to {int(Fr(max(SAMP), 20) * 100)}%"),
     Problem("Which gives a more reliable estimate: one sample of 20 or five samples of 20?", "five samples of 20"),
     Problem("A sixth sample has 7 red. Does it change the estimate much?", "No; 7 of 20 is 35%, the same as the estimate")],
    [S("Warm-Up", [Problem("Mean of 6, 8, 5, 7, 9", "7"), Problem("7 out of 20 as a percent", "35%")]),
     S("Use the samples", [
         Problem("Four random samples of 50 voters show 28, 31, 25, and 30 supporting a plan. Find the mean percent.", f"{N(mean([28, 31, 25, 30]) / 50 * 100)}%", space=24, wide=True),
         Problem("Use your answer to estimate supporters among 8,000 voters.", f"about {int(mean([28, 31, 25, 30]) / 50 * 8000):,}", space=24, wide=True),
         Problem("Lillie's sample of 10 says 70% like a book. Ellie's sample of 100 says 52%. Whose estimate is more reliable? Why?", "Ellie's; the larger sample varies less", lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Why don't all random samples give the same result?", "Each sample includes different members by chance.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students explore sampling variability.", "Generate multiple samples to gauge variation in estimates.", "Bag of mixed candies or beads (optional), workbook Lesson 7.4",
       flow("Warm-up.", "Do Let's Explore with real beads if available.", ["Record several samples; compute the mean."], "Try It 1–3. Weekly Check tomorrow."),
       ["Expecting every sample to match."], ["Physically draw samples."], ["Compare samples of size 5 vs 20."]),
    summary="Samples vary; combine several or use larger samples for better estimates.")

L5 = Lesson("7.5", "Measures of Center and Variability",
    "I can find the mean, median, mean absolute deviation, range, and interquartile range of a data set.", "7.SP.4",
    [("mean", "The sum of the values divided by the number of values."), ("median", "The middle value when data are in order."),
     ("mean absolute deviation (MAD)", "The average distance of the values from the mean."), ("interquartile range (IQR)", "Q3 − Q1, the spread of the middle half of the data.")],
    f"Two quizzes have scores {show(DS5)} and {show(DS5b)}. Which set is more spread out?",
    [Text("<b>Center</b> (mean or median) describes a typical value. <b>Variability</b> (MAD, range, or IQR) describes how spread out the values are."),
     Example("Mean and MAD", show(DS5), [f"Mean: {sum(DS5)} ÷ {len(DS5)} = {N(mean(DS5))}.",
                                          f"Distances from {N(mean(DS5))}: " + ", ".join(str(abs(x - mean(DS5))) for x in DS5) + ".",
                                          f"MAD: {sum(abs(x - mean(DS5)) for x in DS5)} ÷ {len(DS5)} = {N(mad(DS5))}."], f"mean {N(mean(DS5))}, MAD {N(mad(DS5))}"),
     Example("Median and IQR", show(TALL_A), [f"Median (6th value): {N(med(TALL_A))}.", f"Q1 = median of lower half = {N(five(TALL_A)[1])}; Q3 = {N(five(TALL_A)[3])}.", f"IQR = {N(five(TALL_A)[3])} − {N(five(TALL_A)[1])} = {N(iqr(TALL_A))}."],
             f"median {N(med(TALL_A))}, IQR {N(iqr(TALL_A))}"),
     KeyIdea("Use mean and MAD for symmetric data; median and IQR when there are outliers or skew.")],
    [Problem(f"Mean and MAD of {show(DS5b)}", f"mean {N(mean(DS5b))}, MAD {N(mad(DS5b))}"), Problem(f"Median of {show([7, 3, 9, 4, 10, 6])}", N(med([7, 3, 9, 4, 10, 6]))),
     Problem(f"IQR of {show([1, 3, 4, 6, 7, 9, 12, 15])}", N(iqr([1, 3, 4, 6, 7, 9, 12, 15])))],
    [S("Warm-Up", [Problem("Order: 9, 2, 7, 4, 5", "2, 4, 5, 7, 9"), Problem("Median of 2, 4, 5, 7, 9", "5")]),
     S("Find the mean and MAD", [Problem(show(v), f"mean {N(mean(v))}, MAD {N(mad(v))}") for v in [[4, 6, 8, 10, 12], [5, 5, 7, 9, 9], [10, 12, 14, 16, 18, 20], [1, 4, 4, 5, 6]]]),
     S("Find the median and IQR", [Problem(show(v), f"median {N(med(v))}, IQR {N(iqr(v))}") for v in [[2, 3, 5, 6, 8, 9, 11], [10, 12, 13, 15, 18, 20, 21, 25]]]),
     S("Exit Ticket", [Problem(f"Which set has more variability: {show(DS5)} or {show(DS5b)}? Use MAD.", f"{show(DS5)} (MAD {N(mad(DS5))} vs {N(mad(DS5b))})", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compute measures of center and variability.", "Use measures of center and variability to describe and compare data.", "Workbook Lesson 7.5",
       flow("Ordering warm-up.", "Read Let's Explore.", ["Review mean and median.", "Compute MAD with a distance table.", "Review quartiles and IQR."], "Try It 1–3."),
       ["Forgetting to order data before finding the median.", "Using signed differences for MAD."], ["Number line distances."], ["Compute the MAD of family heights."]),
    summary="Center: mean or median. Variability: MAD, range, or IQR.")

d6 = mean(B6) - mean(A6)
L6 = Lesson("7.6", "Comparing Dot Plots",
    "I can compare two data sets using their centers and variability.", "7.SP.3",
    [],
    "Two classes record minutes of homework. Class B seems to do more. How much more, compared to the spread?",
    [Figure(lambda t: Table([[dot_plot(t, A6, 2, 11, width=W * 0.47, title="Class A (minutes)"), dot_plot(t, B6, 2, 11, width=W * 0.47, title="Class B (minutes)")]], colWidths=[W / 2] * 2)),
     Example("Compare", "Class A vs Class B", [f"Means: A = {N(mean(A6))}, B = {N(mean(B6))}; difference {N(d6)}.", f"MAD of each set: {N(mad(A6))}.", f"{N(d6)} ÷ {F(mad(A6).numerator, mad(A6).denominator)} {N(d6 / mad(A6))}."],
             f"The centers differ by about {round(float(d6 / mad(A6)), 1)} MADs: a big difference"),
     KeyIdea("Divide the difference in centers by the variability (MAD). A result above about 2 means the groups are clearly different.")],
    [Problem("Do the dot plots overlap?", "Yes, from 6 to 7"), Problem("Which class has more variability?", "Neither; same MAD"), Problem("Is a typical B student doing more homework?", "Yes, about 3 more minutes")],
    [S("Warm-Up", [Problem(f"Mean of {show(A6)}", N(mean(A6))), Problem(f"Mean of {show(B6)}", N(mean(B6)))]),
     S("Compare the data sets", [
         Problem(f"Team X jumps (ft): {show([10, 11, 12, 12, 13, 14])}. Team Y: {show([12, 13, 14, 14, 15, 16])}. Difference of means?", N(mean([12, 13, 14, 14, 15, 16]) - mean([10, 11, 12, 12, 13, 14])), wide=True),
         Problem("Find the MAD of either team.", N(mad([10, 11, 12, 12, 13, 14])), wide=True),
         Problem("How many MADs apart are the means?", N(Fr(2) / mad([10, 11, 12, 12, 13, 14])), wide=True),
         Problem("Is the difference large or small? Explain.", "Yes: about 2 MADs apart, a noticeable difference", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Two data sets have means 20 and 22 and MADs of 5. Are they very different? Why?", "No; 2 ÷ 5 = 0.4 MADs, lots of overlap", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare dot plots.", "Informally assess the degree of visual overlap of two distributions; express the difference in centers as a multiple of variability.", "Workbook Lesson 7.6",
       flow("Means warm-up.", "Look at the two dot plots.", ["Compute difference ÷ MAD."], "Try It 1–3."),
       ["Comparing only the highest values."], ["Shade overlap."], ["Compare two family members' reaction times."]),
    summary="Compare centers relative to the spread.")

fa, fb = five(TALL_A), five(TALL_B)
L7 = Lesson("7.7", "Comparing Box Plots",
    "I can compare two data sets displayed in box plots.", "7.SP.3, 7.SP.4",
    [("box plot", "A display of the five-number summary: minimum, Q1, median, Q3, maximum.")],
    "Two 7th-grade classes measured heights in inches. Which class tends to be taller?",
    [Figure(lambda t: box_plot(t, [float(v) for v in fa], 50, 72, step=2, label="Class A", second=[float(v) for v in fb], second_label="Class B")),
     Example("Read the plots", "Class A vs Class B", [f"Medians: A = {N(fa[2])}, B = {N(fb[2])}.", f"IQRs: A = {N(fa[3] - fa[1])}, B = {N(fb[3] - fb[1])}."],
             f"Class B's median is {N(fb[2] - fa[2])} in. greater; the spreads are similar"),
     KeyIdea("Compare medians for center and IQRs for spread.")],
    [Problem("Range of Class A", N(fa[4] - fa[0])), Problem("Range of Class B", N(fb[4] - fb[0])), Problem("About what percent of Class B is taller than Class A's median?", "more than 75% (B's Q1 = 60)")],
    [S("Warm-Up", [Problem("What does the line inside a box show?", "the median"), Problem("What does the box's length show?", "the IQR")]),
     S("Compare", [Problem(f"Data: {show(v)}. Five-number summary?", ", ".join(N(x) for x in five(v)), wide=True) for v in [[3, 5, 6, 8, 9, 11, 14], [20, 22, 25, 26, 28, 30, 31, 35]]]
                  + [Problem("Plot Set A {2, 4, 5, 7, 9} and Set B {5, 7, 8, 10, 12}. Which has the greater median?", "Set B (8 vs 5)", fig=lambda t: box_plot(t, None, 0, 14, step=1, width=W - 60), space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("When might you compare medians instead of means?", "When the data are skewed or have outliers", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare box plots.", "Use measures of center and variability to compare two populations.", "Workbook Lesson 7.7",
       flow("Warm-up.", "Read Let's Explore.", ["Read both box plots."], "Try It 1–3."),
       ["Thinking a longer whisker means more data points."], ["Each section holds about 25% of the data."], ["Box plot of family ages."]),
    summary="Compare medians for center and IQRs for spread.")

G7, G4 = [4, 5, 6, 6, 7, 8], [2, 3, 3, 4, 4, 5]
G7M, G4M = mean(G7), mean(G4)
L8 = Lesson("7.8", "Comparing Populations",
    "I can use random samples to compare two populations.", "7.SP.3, 7.SP.4",
    [],
    "Random samples of 7th and 4th graders report weekly reading hours. Do 7th graders read more?",
    [Figure(lambda t: table(t, [["Group", "Sample data (hours)", "Mean", "MAD"],
                                ["Grade 7", show([4, 5, 6, 6, 7, 8]), N(mean([4, 5, 6, 6, 7, 8])), N(mad([4, 5, 6, 6, 7, 8]))],
                                ["Grade 4", show([2, 3, 3, 4, 4, 5]), N(mean([2, 3, 3, 4, 4, 5])), N(mad([2, 3, 3, 4, 4, 5]))]], [1.0 * inch, 2.4 * inch, 0.9 * inch, 0.9 * inch], width=5.2 * inch)),
     Example("Compare", "Difference in means vs MAD", [f"Difference: {N(G7M)} − {N(G4M)} = {N(G7M - G4M)}.", f"Divide by the larger MAD: {N(G7M - G4M)} ÷ {N(mad(G7))} = {N((G7M - G4M) / mad(G7))}."],
             f"about {N((G7M - G4M) / mad(G7)).replace('≈ ', '')} MADs: 7th graders likely read more"),
     KeyIdea("If the samples are random and the difference is more than about 2 MADs, the populations probably differ.")],
    [Problem("If the difference were 0.5 MAD, what would you conclude?", "Not enough evidence of a difference", wide=True),
     Problem("Why do the samples need to be random?", "So they represent their populations", wide=True),
     Problem("Name one other way to compare these groups.", "Compare medians and IQRs", wide=True)],
    [S("Warm-Up", [Problem("Mean of 4, 5, 6, 6, 7, 8", "6"), Problem("Mean of 2, 3, 3, 4, 4, 5", N(mean([2, 3, 3, 4, 4, 5])))]),
     S("Compare the populations", [
         Problem("Random samples of tomato plants: Fertilizer A heights (cm) have mean 42, MAD 3. Fertilizer B: mean 36, MAD 3. How many MADs apart?", "2 MADs", space=24, wide=True),
         Problem("Is there a meaningful difference? Explain.", "Yes; about 2 MADs, so A plants tend to be taller", lines=2, space=0, wide=True),
         Problem("Samples of two dog breeds: mean weights 61 lb and 58 lb, each MAD 6 lb. Meaningful difference?", "No; 3 ÷ 6 = 0.5 MAD", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a question comparing two populations you could answer with random samples.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students compare populations from samples.", "Use measures of center and variability of random samples to draw informal comparative inferences.", "Workbook Lesson 7.8",
       flow("Warm-up.", "Read Let's Explore.", ["Compute difference ÷ MAD."], "Try It 1–3. Weekly Check tomorrow."),
       ["Concluding a difference from tiny gaps."], ["Use the 2-MAD rule of thumb."], ["Design a two-group study at home."]),
    summary="Random samples + difference in means ÷ MAD → is there a real difference?")


L9 = Lesson("7.9", "Probability and Likelihood",
    "I can describe the likelihood of an event with a number from 0 to 1.", "7.SP.5",
    [("probability", "A number from 0 to 1 that tells how likely an event is."), ("event", "A set of outcomes."), ("outcome", "One possible result of an experiment.")],
    "Is it likely, unlikely, certain, or impossible that the sun rises tomorrow? That you roll a 7 on a number cube?",
    [Text(f"Probability measures likelihood on a scale from 0 (impossible) to 1 (certain). A probability of {F(1, 2)} means equally likely to happen or not."),
     Figure(lambda t: table(t, [["0", "near 0", F(1, 2), "near 1", "1"], ["impossible", "unlikely", "equally likely", "likely", "certain"]], header=False, width=W * 0.85)),
     KeyIdea("Probabilities near 0 are unlikely; near 1 are likely.")],
    [Problem("Rolling a 7 on a standard number cube", "impossible (0)"), Problem("A coin landing heads", f"equally likely ({F(1, 2)})"), Problem("Drawing a red marble from a bag of 9 red, 1 blue", "likely")],
    [S("Warm-Up", [Problem(f"Is {F(3, 4)} closer to 0 or 1?", "1"), Problem("Write 0.2 as a fraction", F(1, 5))]),
     S("Describe the likelihood", [Problem(e, v) for e, v in [("Probability 0.95", "likely"), (f"Probability {F(1, 8)}", "unlikely"), ("Probability 0", "impossible"), ("Probability 0.5", "equally likely"),
                                                             ("Snow in July in Texas", "very unlikely"), ("Choosing a vowel from A, E, I", "certain")]]),
     S("Exit Ticket", [Problem("Describe an event that is likely but not certain. Estimate its probability.", "Answers vary.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students describe probability on a 0–1 scale.", "Understand probability as a number from 0 to 1 expressing likelihood.", "Workbook Lesson 7.9",
       flow("Fraction warm-up.", "Discuss Let's Explore.", ["Build the likelihood line."], "Try It 1–3."),
       ["Thinking probability can exceed 1."], ["Place events on a number line."], ["Ask family members to estimate probabilities of daily events."]),
    summary="Probability runs from 0 (impossible) to 1 (certain).")

L10 = Lesson("7.10", "Theoretical Probability",
    "I can find the theoretical probability of an event.", "7.SP.7a",
    [("theoretical probability", "Number of favorable outcomes ÷ number of equally likely outcomes."), ("sample space", "The set of all possible outcomes.")],
    "A bag holds 3 red, 5 blue, and 2 green marbles. What is the probability of drawing blue?",
    [Text("When all outcomes are equally likely, P(event) = favorable outcomes ÷ total outcomes."),
     Example("Marbles", "3 red, 5 blue, 2 green", ["Total: 10. Blue: 5."], f"P(blue) = {P(5, 10)}"),
     Example("Number cube", "P(number greater than 4)", ["Favorable: 5, 6. Total: 6."], f"P = {P(2, 6)}"),
     Example("Complement", "P(not green)", [f"P(green) = {P(2, 10)}, so P(not green) = 1 − {P(2, 10)}."], f"{P(8, 10)}"),
     KeyIdea("P(not A) = 1 − P(A).")],
    [Problem("P(red)", P(3, 10)), Problem("P(even) on a number cube", P(3, 6)), Problem("P(not 6) on a number cube", P(5, 6))],
    [S("Warm-Up", [Problem(f"Simplify {F(5, 10)}", P(5, 10)), Problem("1 − 0.3", "0.7")]),
     S("A spinner has 8 equal parts numbered 1–8. Find each probability.", [Problem(e, v) for e, v in [("P(3)", P(1, 8)), ("P(even)", P(4, 8)), ("P(less than 4)", P(3, 8)), ("P(9)", "0"), ("P(not 8)", P(7, 8)), ("P(multiple of 3)", P(2, 8))]]),
     S("Solve", [Problem("A class has 12 boys and 16 girls. A name is drawn at random. P(girl)?", P(16, 28), space=24, wide=True),
                 Problem("The probability of rain is 0.35. What is the probability of no rain?", "0.65", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Letters of MISSISSIPPI are on cards. P(S)?", P(4, 11), wide=True)], cols=1)],
    TE("Students find theoretical probabilities.", "Develop a uniform probability model and use it to find probabilities.", "Spinner or number cube, workbook Lesson 7.10",
       flow("Warm-up.", "Read Let's Explore.", ["Favorable ÷ total.", "Complement."], "Try It 1–3."),
       ["Using favorable ÷ unfavorable."], ["List the sample space."], ["Probabilities with a deck of cards."]),
    summary="P(event) = favorable ÷ total equally likely outcomes.")

ROLLS = {1: 7, 2: 9, 3: 11, 4: 8, 5: 10, 6: 15}
NR = sum(ROLLS.values())
L11 = Lesson("7.11", "Experimental Probability",
    "I can find experimental probability and compare it to theoretical probability.", "7.SP.6, 7.SP.7b",
    [("experimental probability", "Number of times an event happens ÷ number of trials."), ("trial", "One repetition of an experiment.")],
    f"Ellie rolled a number cube {NR} times. She got a 6 fifteen times. Is the cube fair?",
    [Figure(lambda t: table(t, [["Result", "1", "2", "3", "4", "5", "6"], ["Frequency"] + [str(ROLLS[k]) for k in range(1, 7)]], width=W * 0.75)),
     Example("Experimental", "P(6) from the data", [f"6 occurred 15 times in {NR} rolls."], f"{P(15, NR)} = 25%"),
     Example("Compare", "Theoretical P(6)", [f"{F(1, 6)} ≈ 17%.", "25% is higher, but 60 rolls is a small number of trials."], "Roll many more times before deciding the cube is unfair"),
     KeyIdea("As the number of trials grows, experimental probability tends to get closer to theoretical probability.")],
    [Problem("Experimental P(3)", P(11, NR)), Problem("Experimental P(odd)", P(7 + 11 + 10, NR)), Problem(f"Predict how many 6s in 600 rolls of a fair cube", "about 100")],
    [S("Warm-Up", [Problem("15 ÷ 60 as a percent", "25%"), Problem(f"{F(1, 6)} of 600", "100")]),
     S("A coin is flipped 50 times: 29 heads.", [Problem("Experimental P(heads)", P(29, 50)), Problem("Theoretical P(heads)", F(1, 2)), Problem("Experimental P(tails)", P(21, 50)), Problem("Predict heads in 1,000 flips of a fair coin", "about 500")]),
     S("Predict", [Problem("A player made 18 of 24 free throws. Predict makes in 40 attempts.", f"about {int(Fr(18, 24) * 40)}", space=24, wide=True),
                   Problem("A spinner landed on blue 12 times in 80 spins. Predict blues in 200 spins.", f"about {int(Fr(12, 80) * 200)}", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Why might experimental and theoretical probability differ?", "Chance; small number of trials", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compute experimental probability.", "Approximate probability by collecting data; predict relative frequency.", "Number cube or coin, workbook Lesson 7.11",
       flow("Warm-up.", "Roll a cube 30 times and record.", ["Compare experimental and theoretical."], "Try It 1–3."),
       ["Expecting exact matches with few trials."], ["Pool data from several experiments."], ["Graph running proportion of heads."]),
    summary="Experimental: occurrences ÷ trials. It approaches theoretical with more trials.")

L12 = Lesson("7.12", "Probability Models",
    "I can build uniform and non-uniform probability models.", "7.SP.7a, 7.SP.7b",
    [("probability model", "A list of outcomes and their probabilities, which add to 1."), ("uniform model", "All outcomes are equally likely.")],
    "A spinner has 4 equal sections: red, red, blue, yellow. Are all colors equally likely?",
    [Figure(lambda t: spinner(t, ["Red", "Red", "Blue", "Yellow"], width=110)),
     Example("Non-uniform model", "Spinner above", [f"P(red) = {F(2, 4)} = {F(1, 2)}, P(blue) = {F(1, 4)}, P(yellow) = {F(1, 4)}.", f"Sum: {F(1, 2)} + {F(1, 4)} + {F(1, 4)} = 1 ✓."], "Not uniform: red is twice as likely"),
     Example("Model from data", "A survey of 40: 18 dogs, 14 cats, 8 fish (favorite pet)", [f"P(dog) = {P(18, 40)}, P(cat) = {P(14, 40)}, P(fish) = {P(8, 40)}."], "probabilities add to 1"),
     KeyIdea("In every probability model, the probabilities add up to 1.")],
    [Problem("Uniform model for a coin", f"H: {F(1, 2)}, T: {F(1, 2)}"), Problem("Spinner P(not red)", F(1, 2)), Problem("A model lists 0.3, 0.5, and ? Find ?", "0.2")],
    [S("Warm-Up", [Problem(f"{F(1, 2)} + {F(1, 4)} + {F(1, 4)}", "1"), Problem("1 − 0.3 − 0.5", "0.2")]),
     S("Build or check the model", [
         Problem("Spinner with sections 1, 2, 2, 3, 3, 3. Give P(1), P(2), P(3).", f"{P(1, 6)}, {P(2, 6)}, {P(3, 6)}", fig=lambda t: spinner(t, [1, 2, 2, 3, 3, 3], width=90), space=0, wide=True),
         Problem("Is the model P(A) = 0.4, P(B) = 0.4, P(C) = 0.3 valid? Why?", "No; the sum is 1.1", lines=1, space=0, wide=True),
         Problem("Of 50 cars, 20 were white, 15 black, 10 silver, and 5 red. Write a model.", f"white {P(20, 50)}, black {P(15, 50)}, silver {P(10, 50)}, red {P(5, 50)}", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Design a spinner where P(green) = 0.5 and P(red) = 0.25.", "e.g. 4 sections: green, green, red, any other color", lines=2, space=0, wide=True)], cols=1)],
    TE("Students develop probability models.", "Develop uniform and non-uniform probability models.", "Paper spinner, workbook Lesson 7.12",
       flow("Warm-up.", "Discuss Let's Explore.", ["Build models; check the sum is 1."], "Try It 1–3. Weekly Check tomorrow."),
       ["Assuming every outcome is equally likely."], ["Count sections."], ["Design a fair game."]),
    summary="A probability model lists every outcome; the probabilities sum to 1.")

SHIRTS, PANTS = ["Red", "Blue", "Green"], ["Jeans", "Khakis"]
L13 = Lesson("7.13", "Sample Spaces for Compound Events",
    "I can list the sample space of a compound event using lists and tables.", "7.SP.8b",
    [("compound event", "An event made of two or more simple events.")],
    "You roll two number cubes. How many outcomes are possible?",
    [Figure(lambda t: table(t, [["+", "1", "2", "3", "4", "5", "6"]] + [[str(a)] + [str(a + b) for b in range(1, 7)] for a in range(1, 7)], width=W * 0.6, font_size=9)),
     Example("Count outcomes", "Two number cubes", ["6 × 6 = 36 outcomes."], "36"),
     Example("Use the table", "P(sum is 7)", ["Count 7s in the table: 6."], f"{dice(lambda a, b: a + b == 7)}"),
     KeyIdea("Organized lists and tables make sure you count every outcome once.")],
    [Problem("P(sum is 2)", dice(lambda a, b: a + b == 2)), Problem("P(sum is 10)", dice(lambda a, b: a + b == 10)), Problem("P(doubles)", dice(lambda a, b: a == b))],
    [S("Warm-Up", [Problem("6 × 6", "36"), Problem(f"Simplify {F(6, 36)}", P(6, 36))]),
     S("Use the sum table", [Problem(e, dice(cnd)) for e, cnd in [("P(sum is 8)", lambda a, b: a + b == 8), ("P(sum greater than 9)", lambda a, b: a + b > 9), ("P(sum is even)", lambda a, b: (a + b) % 2 == 0),
                                                                ("P(sum less than 5)", lambda a, b: a + b < 5), ("P(sum is 12)", lambda a, b: a + b == 12), ("P(sum is 1)", lambda a, b: a + b == 1)]]),
     S("List the sample space", [Problem("Flip a coin and spin a 3-color spinner (R, B, Y). List all outcomes.", "HR, HB, HY, TR, TB, TY (6)", lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which sum of two number cubes is most likely? Why?", "7; it occurs 6 ways, more than any other", lines=2, space=0, wide=True)], cols=1)],
    TE("Students list sample spaces.", "Represent sample spaces for compound events using organized lists and tables.", "Two number cubes, workbook Lesson 7.13",
       flow("Warm-up.", "Discuss Let's Explore.", ["Build the sum table together."], "Try It 1–3."),
       ["Counting 3+4 and 4+3 as one outcome."], ["Color-code the table."], ["Play a sum-guessing game."]),
    summary="Lists and tables organize every outcome of a compound event.")

L14 = Lesson("7.14", "Tree Diagrams",
    "I can use a tree diagram to find the sample space of a compound event.", "7.SP.8b",
    [("tree diagram", "A branching diagram that shows every outcome of a multi-step experiment.")],
    "Lillie has a red, blue, or green shirt and jeans or khakis. How many outfits can she make?",
    [Figure(lambda t: tree_diagram(t, SHIRTS, PANTS, width=W * 0.8)),
     Example("Count", "3 shirts, 2 pants", [f"Each of {len(SHIRTS)} shirts branches to {len(PANTS)} pants."], f"{len(SHIRTS) * len(PANTS)} outfits"),
     Example("Probability", "Outfit chosen at random: P(blue shirt with jeans)", [f"1 favorable outcome of {len(SHIRTS) * len(PANTS)}."], P(1, 6)),
     KeyIdea("Multiply the number of choices at each stage to count outcomes (the counting principle).")],
    [Problem("P(outfit with khakis)", P(3, 6)), Problem("Add a yellow shirt. How many outfits?", "8"), Problem("Coin flipped 3 times: how many outcomes?", "8")],
    [S("Warm-Up", [Problem("3 × 2", "6"), Problem("2 × 2 × 2", "8")]),
     S("Tree diagrams", [Problem("Draw a tree: flip a coin twice. List outcomes.", "HH, HT, TH, TT", space=80, wide=True),
                         Problem("P(exactly one head)", P(2, 4)), Problem("P(at least one tail)", P(3, 4))]),
     S("Count", [Problem(e, v) for e, v in [("4 sandwiches, 3 drinks: combos", "12"), ("2 sizes, 5 flavors: cones", "10"), ("Coin and number cube: outcomes", "12"), ("3 coins: P(all heads)", P(1, 8))]]),
     S("Exit Ticket", [Problem("A café offers 3 breads, 4 fillings, and 2 sauces. How many sandwiches?", "24", wide=True)], cols=1)],
    TE("Students use tree diagrams.", "Represent sample spaces for compound events with tree diagrams.", "Workbook Lesson 7.14",
       flow("Warm-up.", "Read Let's Explore.", ["Draw the outfit tree."], "Try It 1–3."),
       ["Missing branches."], ["Draw every branch at each stage."], ["Plan outfits for the week with a tree."]),
    summary="Tree diagrams and the counting principle show every outcome.")


L15 = Lesson("7.15", "Probability of Compound Events",
    "I can find the probability of a compound event using the sample space.", "7.SP.8a, 7.SP.8c",
    [],
    "Flip a coin and roll a number cube. What is P(heads and an even number)?",
    [Figure(lambda t: tree_diagram(t, ["H", "T"], [str(k) for k in range(1, 7)], width=W * 0.6)),
     Example("Count", "P(heads and even)", ["Sample space: 2 × 6 = 12.", "Favorable: H2, H4, H6 = 3."], P(3, 12)),
     Example("Multiply (independent events)", "Same event", [f"P(H) × P(even) = {F(1, 2)} × {F(1, 2)}."], F(1, 4)),
     KeyIdea("Probability of a compound event = favorable outcomes ÷ sample space size. For independent events you can also multiply.")],
    [Problem("P(tails and 5)", P(1, 12)), Problem("P(heads and greater than 2)", P(4, 12)), Problem("P(tails or 6)", P(7, 12))],
    [S("Warm-Up", [Problem(f"{F(1, 2)} × {F(1, 3)}", F(1, 6)), Problem("2 × 6", "12")]),
     S("Find each probability", [Problem(e, v) for e, v in [("Two coins: P(HH)", P(1, 4)), ("Two number cubes: P(both 6)", dice(lambda a, b: a == 6 and b == 6)), ("Two cubes: P(both even)", dice(lambda a, b: a % 2 == 0 and b % 2 == 0)),
                                                             ("Coin + cube: P(T and 1 or 2)", P(2, 12)), ("Spinner 1–4 twice: P(sum 5)", P(sum(1 for a, b in product(range(1, 5), repeat=2) if a + b == 5), 16)), ("Three coins: P(exactly 2 heads)", P(3, 8))]]),
     S("Solve", [Problem(f"Ellie guesses on 2 true/false questions. P(both correct)?", F(1, 4), space=24, wide=True),
                 Problem("A family has 3 children. Assuming boy and girl are equally likely, P(at least one girl)?", P(7, 8), space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Roll two number cubes. P(sum is 4)?", dice(lambda a, b: a + b == 4), wide=True)], cols=1)],
    TE("Students compute compound probabilities.", "Find probabilities of compound events using lists, tables, tree diagrams, and simulation.", "Workbook Lesson 7.15",
       flow("Warm-up.", "Read Let's Explore.", ["Count from the tree; then multiply."], "Try It 1–3."),
       ["Adding probabilities instead of multiplying for “and.”"], ["Use the sample space."], ["Find P(at least one 6) in two rolls: 11/36."]),
    summary="Count favorable outcomes in the sample space, or multiply for independent events.")

L16 = Lesson("7.16", "Simulations",
    "I can design and use a simulation to estimate the probability of a compound event.", "7.SP.8c",
    [("simulation", "An experiment that models a real situation using random tools.")],
    "A cereal box holds one of 4 equally likely prizes. About how many boxes must you buy to get all 4?",
    [Text("Instead of buying cereal, <b>simulate</b>: roll a 4-sided die (or spin a 4-part spinner) where each number stands for a prize. Count rolls until all four appear. Repeat many times."),
     Figure(lambda t: table(t, [["Trial", "Rolls", "Boxes needed"], ["1", "2, 1, 2, 4, 1, 3", "6"], ["2", "3, 3, 1, 4, 2", "5"], ["3", "1, 4, 4, 2, 4, 1, 3", "7"], ["4", "4, 2, 2, 1, 3", "5"], ["5", "2, 2, 3, 2, 1, 1, 4", "7"]],
                            [0.7 * inch, 2.6 * inch, 1.3 * inch], width=4.6 * inch)),
     Example("Estimate", "Mean of the five trials", [f"(6 + 5 + 7 + 5 + 7) ÷ 5 = {N(mean([6, 5, 7, 5, 7]))}."], f"about {N(mean([6, 5, 7, 5, 7]))} boxes (more trials improve the estimate)"),
     KeyIdea("A simulation matches each real outcome to a random-tool outcome with the same probability.")],
    [Problem("Experimental P(needing more than 6 boxes) from the table", P(2, 5)), Problem("Which tool simulates a 50% event?", "a coin"), Problem("Which tool simulates a 1-in-6 event?", "a number cube")],
    [S("Warm-Up", [Problem("Mean of 6, 5, 7, 5, 7", N(mean([6, 5, 7, 5, 7]))), Problem("What tool has 4 equal outcomes?", "4-section spinner")]),
     S("Design a simulation", [
         Problem("A player makes 50% of shots. Design a simulation for P(making 3 in a row).", "Flip 3 coins; heads = make; repeat many times", lines=2, space=0, wide=True),
         Problem("Rain is forecast at 30% each day. Design a simulation for P(rain on at least 1 of 2 days).", "Use digits 0–9; 0–2 = rain; draw 2 digits per trial", lines=2, space=0, wide=True),
         Problem("In 20 trials of the shot simulation, 3 had three heads. Experimental probability?", P(3, 20), wide=True),
         Problem("What is the theoretical probability of three heads?", F(1, 8), wide=True)], cols=1),
     S("Exit Ticket", [Problem("Why do more trials give a better estimate?", "Results settle closer to the true probability", lines=2, space=0, wide=True)], cols=1)],
    TE("Students design and run simulations.", "Design and use a simulation to generate frequencies for compound events.", "Coins, number cubes, spinners, workbook Lesson 7.16, Unit 7 Review",
       flow("Warm-up.", "Run the cereal-prize simulation 5 times.", ["Pool results; compute the mean."], "Try It 1–3.", "Workbook Lesson 7.16 and the Unit 7 Review.", "Check. Tomorrow: Unit 7 Test."),
       ["Choosing a tool with the wrong probability."], ["Match probabilities first."], ["Run 50 trials and compare."]),
    summary="Simulations use random tools to estimate real probabilities.")

C1 = Check("Weekly Check 19: Sampling", [S("Show what you know", [
    Problem("A school surveys 60 of its 900 students. Name the population.", "all 900 students"), Problem("Surveying only the chess club about favorite games: random or biased?", "Biased"),
    Problem("15 of 60 sampled students bike. Estimate bikers in 900.", f"{int(Fr(15, 60) * 900)}"), Problem("Samples show 40%, 46%, 43%, 39%. Mean percent?", f"{N(mean([40, 46, 43, 39]))}%"),
    Problem("Use that mean to estimate for 2,000 people.", f"about {int(mean([40, 46, 43, 39]) / 100 * 2000)}"), Problem("Which is more reliable: a sample of 30 or of 300?", "300")])], minutes=15)
C2 = Check("Weekly Check 20: Comparing Data", [S("Show what you know", [
    Problem(f"Mean of {show([6, 8, 10, 12, 14])}", N(mean([6, 8, 10, 12, 14]))), Problem(f"MAD of {show([6, 8, 10, 12, 14])}", N(mad([6, 8, 10, 12, 14]))),
    Problem(f"Median of {show([3, 7, 8, 12, 15, 20])}", N(med([3, 7, 8, 12, 15, 20]))), Problem(f"IQR of {show([2, 4, 5, 7, 8, 10, 13, 14])}", N(iqr([2, 4, 5, 7, 8, 10, 13, 14]))),
    Problem("Means 30 and 36, MAD 3. How many MADs apart?", "2"), Problem("Is that a meaningful difference?", "Yes (about 2 MADs)")])], minutes=15)
C3 = Check("Weekly Check 21: Probability", [S("Show what you know", [
    Problem("Bag: 4 red, 6 blue. P(red)", P(4, 10)), Problem("P(not 2) on a number cube", P(5, 6)), Problem("Probability 0.9 is…", "likely"),
    Problem("32 heads in 50 flips: experimental P(heads)", P(32, 50)), Problem("Model: 0.25, 0.45, ? Find ?", "0.3"), Problem("Coin landed heads 12 of 40 times. Predict heads in 200 flips with that rate.", "60")])], minutes=15)

REVIEW = Check("Unit 7 Review", [
    S("Statistics", [Problem("Random or biased: surveying shoppers at a bookstore about reading habits", "Biased"), Problem("24 of 80 sampled like a show. Estimate for 5,000.", f"{int(Fr(24, 80) * 5000):,}"),
                     Problem(f"Mean and MAD of {show([5, 7, 9, 11, 13])}", f"mean {N(mean([5, 7, 9, 11, 13]))}, MAD {N(mad([5, 7, 9, 11, 13]))}"), Problem(f"Five-number summary of {show([1, 4, 6, 7, 9, 12, 14])}", ", ".join(N(x) for x in five([1, 4, 6, 7, 9, 12, 14])))]),
    S("Probability", [Problem("Spinner 1–10: P(prime)", P(4, 10)), Problem("Two coins: P(no heads)", F(1, 4)), Problem("Two cubes: P(sum is 6)", dice(lambda a, b: a + b == 6)),
                      Problem("3 shirts, 4 pants, 2 shoes: outfits", "24"), Problem("Design a simulation for a 25% event.", "e.g. 4-section spinner; 1 section = success", lines=1, space=0, wide=True)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 7 Test", [
    S("Part A · Sampling (1 point each)", [Problem("A factory tests 100 of 20,000 parts. Name the sample.", "the 100 parts tested"), Problem("Asking the first 20 people in line for a roller coaster about favorite rides: random or biased?", "Biased"),
        Problem("9 of 45 sampled students have a summer job. Estimate for 1,200 students.", f"{int(Fr(9, 45) * 1200)}"), Problem("Samples: 12, 15, 9, 14 successes out of 30 each. Mean count?", N(mean([12, 15, 9, 14])))]),
    S("Part B · Comparing data (1 point each)", [Problem(f"Mean of {show([8, 10, 11, 13, 18])}", N(mean([8, 10, 11, 13, 18]))), Problem(f"MAD of {show([8, 10, 11, 13, 18])}", N(mad([8, 10, 11, 13, 18]))),
        Problem(f"IQR of {show([5, 6, 9, 10, 12, 15, 16, 20])}", N(iqr([5, 6, 9, 10, 12, 15, 16, 20]))), Problem("Means 52 and 60, MADs 4. MADs apart?", "2")]),
    S("Part C · Probability (1 point each)", [Problem("Bag: 2 red, 3 green, 5 yellow. P(green)", P(3, 10)), Problem("P(not yellow)", P(5, 10)), Problem("Coin + cube: P(H and 3)", P(1, 12)),
        Problem("Two cubes: P(sum is 9)", dice(lambda a, b: a + b == 9)), Problem("Three coins: P(at least one head)", P(7, 8)), Problem("18 of 30 spins landed on red. Experimental P(red)?", P(18, 30))]),
    S("Part D · Problem solving (3 points each)", [
        Problem("Random samples of two orchards: Orchard A apples mean 150 g, MAD 10 g; Orchard B mean 175 g, MAD 10 g. Compare the orchards. Is the difference meaningful? Explain.", "Difference 25 g = 2.5 MADs; yes, B's apples tend to be heavier", space=60, wide=True, points=3),
        Problem("Design a simulation to estimate the probability that a family with 4 children has at least 3 girls. Describe the tool, one trial, and what you record.", f"Flip 4 coins (H = girl) per trial; record whether ≥ 3 heads; repeat many times; theoretical {F(5, 16)}", space=60, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["17–20 (85%+)", "Mastered."], ["14–16", "Proficient; correct missed items."], ["Below 14", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-04-26", "2027-05-03", "2027-05-10", "2027-05-17"], CHECKS, REVIEW, TEST)

UNIT = Unit(7, "Statistics and Probability", "Sampling, comparing populations, probability models, and compound events.",
    "How can a survey of 100 people tell us about a whole city? How likely is it to roll doubles? In this unit you will learn to sample fairly, compare groups with data, and measure chance with probability.",
    ["Use random samples to make inferences about populations.", "Compare two data sets using center and variability.", "Find theoretical and experimental probabilities.", "Build probability models.", "Find probabilities of compound events with lists, tables, trees, and simulations."],
    [("7.SP.1–2", "Use random sampling to draw inferences about a population."), ("7.SP.3–4", "Draw informal comparative inferences about two populations."),
     ("7.SP.5–7", "Investigate chance processes and develop probability models."), ("7.SP.8", "Find probabilities of compound events.")],
    [("population", "The whole group."), ("sample", "Part of the population."), ("MAD", "Average distance from the mean."), ("probability", "A number 0–1 for likelihood."), ("sample space", "All possible outcomes.")],
    ["Mean, median, and dot plots (Grade 6).", "Fractions, decimals, and percents (Units 2–5)."], ["Coins, number cubes, paper spinners", "Bag of beads or candies"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Election polls, weather forecasts, quality control in factories, and sports statistics all use sampling and probability.",
    family_note="Play board games together and ask your student to estimate the chance of a roll or draw before it happens.",
    weeks=WEEKS)
