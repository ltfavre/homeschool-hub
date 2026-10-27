"""Data Science & Psychometrics · Unit 1: Your Data Toolkit — the analysis workflow, reading data in SAS, Python, and R,
variables and levels of measurement, and reproducible habits (week of Nov 2, 2026)."""
from engine import *
from content.datakit import S, MC, OR, SA, DRAW, CODEX, mono, quiz, review, exam, weeks_for, NO_TE

# ================================================================= Week 1
L1 = Lesson("1.1", "Your Toolkit and the Analysis Workflow",
    "I can describe the steps of a data analysis and set up SAS, Python, and R so I can practice every day.", "Foundations · 30 min",
    [("workflow", "The repeatable sequence of steps in an analysis, from question to communication."), ("reproducible", "Able to be rerun by you or someone else and get the same result."),
     ("IDE", "Integrated development environment: the program where you write and run code (SAS Studio, RStudio, Jupyter, VS Code).")],
    "Think of the last report or analysis you were handed at work. Where did the numbers come from, and could you have recreated them yourself?",
    [Text("Every analysis, from a quick table for a meeting to a full technical report on a test, follows roughly the same path. Naming the steps helps you see where you are confident and where you want to grow."),
     Figure(lambda t: flow_fig(t, ["Question: what do we need to know?", "Import: get the data in", "Clean and tidy: fix and reshape", "Explore: summarize and visualize", "Model: test and estimate", "Communicate: report and decide"], height=60, size=8)),
     Text("This year you'll practice each step in three languages. <b>SAS</b> is your workplace's statistics engine. <b>Python</b> is what you already use a lot. <b>R</b> is the language most psychometricians use for reliability, factor analysis, and item response theory. Seeing one task three ways makes each language easier, because you learn the <i>idea</i> first and the syntax second."),
     Figure(lambda t: table(t, [["Tool", "Free way to use it", "What it's best at for you"], ["SAS", "SAS OnDemand for Academics (SAS Studio in a browser), or SAS at work", "your team's production statistics; PROC IRT, PROC FACTOR, PROC CORR"],
                                ["Python", "your current setup, or Anaconda / VS Code with Jupyter", "data wrangling, automation, machine learning"], ["R", "R plus RStudio Desktop (Posit), or Posit Cloud in a browser", "psychometrics packages: psych, mirt, lavaan"]],
                            [0.8 * inch, 2.6 * inch, 2.5 * inch], width=5.9 * inch, font_size=9)),
     Heading("Your resource plan"),
     Figure(lambda t: table(t, [["Resource", "Cost", "Use it for"], ["SAS OnDemand for Academics (SAS Studio)", "free", "running SAS anywhere; includes free e-learning: SAS Programming 1 and Statistics 1"],
                                ["R for Data Science (2e), r4ds.hadley.nz", "free online", "R and the tidyverse"], ["Python for Data Analysis (3E), wesmckinney.com/book", "free online", "pandas"],
                                ["StatQuest with Josh Starmer (YouTube)", "free", "short, clear statistics videos"], ["Introduction to Educational and Psychological Measurement Using R (Albano)", "free online, CC BY", "psychometrics in R (Units 6–8)"],
                                ["NCME ITEMS digital modules", "check access on ncme.org", "short modules on reliability, IRT, item analysis, standard setting"],
                                ["DataCamp Premium (optional)", "about $25–27/month billed yearly, or about $42 month to month (check current price)", "interactive R, Python, and SQL practice; Statistician (R) track; Factor Analysis in R; Structural Equation Modeling with lavaan in R"]],
                            [2.3 * inch, 1.3 * inch, 2.3 * inch], width=5.9 * inch, font_size=8.5)),
     Text("<b>Is DataCamp worth renewing?</b> It fits this course well for R, Python, and SQL practice, and the interactive format suits a 30-minute day. It has no SAS courses and only a few psychometrics courses, so this book carries the SAS and measurement content. A good approach: on Fridays, after your quiz, spend 15 minutes on the DataCamp chapter listed in that week's Watch and Explore box. If you'd use it at least twice a week, the annual plan is the better value; if not, the free resources above cover everything in this book."),
     Code("Hello, data", sas='''data _null_;
  put "Hello from SAS!";
  x = 17.67 * 2;
  put x=;
run;''', python='''print("Hello from Python!")
x = 17.67 * 2
print(x)''', r='''print("Hello from R!")
x <- 17.67 * 2
x''', output='''Hello from ...!
35.34          (SAS writes x=35.34 in the log; R prints [1] 35.34)''',
          note="In SAS, PUT writes to the <b>log</b>, not the results window. Reading the log is a core SAS skill: look for NOTE, WARNING, and ERROR."),
     Watch([("SAS Programming: Getting Started", "free e-learning at learn.sas.com", "start with the first module, about 30 minutes"),
            ("R for Data Science (2e), “Introduction” and “Workflow: basics”", "free online book at r4ds.hadley.nz", "15 minutes"),
            ("DataCamp (optional): Introduction to R, Chapter 1", "datacamp.com", "the first chapter of every course is free")]),
     OnTheJob("Write down one recurring task at work (a monthly score report, a survey summary, an item review). As you go through this year, you'll rebuild pieces of it in code."),
     KeyIdea("Question → import → clean → explore → model → communicate. You'll practice every step in SAS, Python, and R.")],
    [Problem("Name the six steps of the workflow.", "question, import, clean/tidy, explore, model, communicate"), Problem("Where does a SAS PUT statement write?", "the log"),
     Problem("Which language has the psychometrics packages psych, mirt, and lavaan?", "R")],
    [S("Warm-Up", [SA("What does IDE stand for?", "integrated development environment"), SA("Why does reproducible work matter?", "Others (or future you) can rerun it and get the same results.")], cols=1),
     S("Set Up", [OR("Check off each step and write where you'll work: (1) SAS Studio opened; (2) R and RStudio installed or Posit Cloud account; (3) Python with Jupyter ready; (4) data pack downloaded into a folder named data.",
                     "Answers vary. All four steps completed.", lines=4),
                  CODEX("Run the Hello, data example in all three languages. Record what each one printed.", "Each prints its hello message and 35.34 (SAS: x=35.34 in the log; R: [1] 35.34).", lines=3)]),
     S("Reflect", [OR("Which workflow step do you feel most and least confident about at work? Why?", "Answers vary.", lines=3),
                   OR("Write the recurring work task you'll rebuild in code this year.", "Answers vary.", lines=2)])],
    NO_TE, summary="Every analysis follows the same workflow; you'll practice it in SAS, Python, and R.")

L2 = Lesson("1.2", "Reading Data into SAS, Python, and R",
    "I can import a CSV file in all three languages and check its size and first rows.", "Import · 30 min",
    [("CSV", "Comma-separated values: a plain-text table where commas separate columns."), ("data frame", "A table of rows and columns in Python (pandas) or R; SAS calls it a data set."),
     ("working directory", "The folder your program looks in when you give a file name without a full path.")],
    "Most analyses fail at step one: the file won't load, columns come in as the wrong type, or the path is wrong. How do you usually check that data loaded correctly?",
    [Text("The data pack's <b>exam.csv</b> holds responses from 600 examinees to a 30-item multiple-choice test (Form A). Each row is one examinee; columns <font name='Mono'>i01</font> to <font name='Mono'>i30</font> hold the letter each person chose. A blank means the person skipped the item."),
     Code("Import exam.csv and look at it", sas='''%let path = ~/data;      /* the folder where you uploaded the data pack */
proc import datafile="&path/exam.csv" out=work.exam dbms=csv replace;
  getnames=yes;  guessingrows=max;
run;
proc contents data=work.exam varnum; run;
proc print data=work.exam(obs=5); var id form i01-i05; run;''', python='''import pandas as pd
exam = pd.read_csv("data/exam.csv")
print(exam.shape)                       # (rows, columns)
print(exam.loc[:, "id":"i05"].head())''', r='''library(readr)                          # part of the tidyverse
exam <- read_csv("data/exam.csv")
dim(exam)                               # rows, columns
head(exam[, 1:7], 5)''', output='''600 rows, 32 columns
     id form i01 i02 i03 i04 i05
  E1001    A   B   A   A   D   A
  E1002    A   B   A   A   A   A
  E1003    A   D   A   A   D   A
  E1004    A   B   A   D   D   A
  E1005    A   A   A   A   D   A''',
          note="If SAS can't find the file, right-click the data folder in SAS Studio, choose Properties, and copy the full path into %let path. In Python and R, a relative path like data/exam.csv is read from your working directory."),
     Text("<b>Always check three things after an import:</b> the number of rows and columns, the first few rows, and the type of each column. Those three checks catch most problems before they spread into your results."),
     WatchOut("Blank cells become missing values: SAS stores a blank character value, while pandas and R store NaN or NA. That will matter when you score the test in Unit 2."),
     Watch([("R for Data Science (2e), “Data import”", "r4ds.hadley.nz", "20 minutes"), ("Python for Data Analysis (3E), “Data Loading, Storage, and File Formats”, reading text files", "wesmckinney.com/book (free online)", "read the CSV section"),
            ("SAS Programming 1: Essentials, “Accessing Data” lesson", "free e-learning at learn.sas.com", None)]),
     KeyIdea("Import, then immediately check dimensions, the first rows, and column types.")],
    [Problem("How many examinees and columns are in exam.csv?", "600 rows and 32 columns"), Problem("What did examinee E1003 answer on item i01?", "D"),
     Problem("Which SAS option makes PROC IMPORT scan all rows before guessing column types?", "GUESSINGROWS=MAX")],
    [S("Warm-Up", [SA("CSV stands for…", "comma-separated values"), SA("SAS's name for a data frame", "data set")], cols=2),
     S("Practice", [CODEX("Import examinees.csv in the language of your choice. How many rows and columns does it have?", '''examinees <- read_csv("data/examinees.csv"); dim(examinees)
# 600 rows, 6 columns (id, gender, region, program, hours_prep, prior_gpa)''', lines=4),
                    SA("What are the gender, region, and program of examinee E1002?", "M, East, Evening"),
                    SA("How many blank (omitted) responses does exam.csv have on item i01?", "7"),
                    CODEX("Write the code in a second language to print the first 3 rows of examinees.", '''proc print data=work.examinees(obs=3); run;
print(examinees.head(3))
head(examinees, 3)''', lines=4)]),
     S("Exit Ticket", [OR("List the three checks you should do after every import.", "dimensions (rows/columns), first rows, column types", lines=2)])],
    NO_TE, summary="Import, then check dimensions, first rows, and types.")

L3 = Lesson("1.3", "Variables, Data Types, and Levels of Measurement",
    "I can identify data types and levels of measurement and explain why they decide which analyses make sense.", "Foundations · 30 min",
    [("nominal", "Categories with no order (program, region)."), ("ordinal", "Ordered categories with uneven or unknown spacing (Likert agreement, ranks)."),
     ("interval", "Ordered numbers with equal spacing but no true zero (scaled test scores, °F)."), ("ratio", "Equal spacing and a true zero (hours, counts, dollars)."),
     ("tidy data", "Each variable is a column, each observation is a row, each value is a cell.")],
    "A colleague averages survey responses coded 1 = Strongly disagree to 5 = Strongly agree and reports a mean of 3.02. Is that a meaningful number?",
    [Text("Software stores data as <b>types</b>: numbers, text (character or string), logical (true/false), and dates. Statistics also cares about <b>levels of measurement</b>, which describe what the numbers mean."),
     Figure(lambda t: table(t, [["Level", "Examples in the data pack", "Sensible summaries"], ["nominal", "program, region, gender", "counts, percents, mode"], ["ordinal", "survey items e1–s4 (1–5 agreement)", "medians, percentiles, counts; means used with care"],
                                ["interval", "scaled scores (Unit 8), z-scores", "means, standard deviations, differences"], ["ratio", "hours_prep, study_hours", "everything above, plus ratios (“twice as many hours”)"]],
                            [0.9 * inch, 2.3 * inch, 2.7 * inch], width=5.9 * inch, font_size=9)),
     Text("Psychometrics lives on this boundary. Single Likert items are ordinal, but sums of several items often behave approximately like interval scales, which is why analysts routinely average scale scores. Being able to explain that choice is part of being confident in your role."),
     Code("Check column types", sas='''proc import datafile="&path/examinees.csv" out=work.examinees dbms=csv replace;
  getnames=yes;  guessingrows=max;
run;
proc contents data=work.examinees varnum; run;   /* Type: Num or Char */''', python='''examinees = pd.read_csv("data/examinees.csv")
print(examinees.dtypes)
examinees["program"] = examinees["program"].astype("category")''', r='''examinees <- read_csv("data/examinees.csv")
str(examinees)                         # or dplyr::glimpse(examinees)
examinees$program <- factor(examinees$program)''', output='''id, gender, region, program -> text (Char / object or str / chr)
hours_prep -> integer; prior_gpa -> decimal (Num / int64, float64 / dbl)'''),
     Text("<b>Tidy data</b> makes every analysis easier: one row per observation, one column per variable. Exam data are “wide” (one column per item); for some item analyses you'll reshape them “long” (one row per person-item) in Unit 2."),
     Watch([("StatQuest: “What is a statistical distribution?”", "StatQuest with Josh Starmer on YouTube", "about 5 minutes"), ("R for Data Science (2e), “Data tidying,” first section", "r4ds.hadley.nz", "10 minutes")]),
     OnTheJob("When someone hands you a number, ask what level of measurement it came from. It's one of the fastest ways to spot a summary that doesn't fit the data."),
     KeyIdea("Data types tell software how to store values; levels of measurement tell you which statistics are meaningful.")],
    [Problem("Level of measurement: region", "nominal"), Problem("Level: a 1–5 agreement item", "ordinal"), Problem("Level: hours_prep", "ratio")],
    [S("Warm-Up", [SA("Categories with no order", "nominal"), SA("Equal spacing and a true zero", "ratio")], cols=2),
     S("Classify", [SA(q, a) for q, a in [("prior_gpa", "interval (treated as a continuous number)"), ("left_next_year (0/1)", "nominal (binary)"),
                                          ("tenure_years", "ratio"), ("dept", "nominal"), ("intent_stay (1–10 rating)", "ordinal"), ("rank in class", "ordinal")]], cols=2),
     S("Code It", [CODEX("Load survey.csv and show each column's type. Which columns are numbers but really ordinal?", '''survey = pd.read_csv("data/survey.csv"); print(survey.dtypes)
# e1-e4, w1-w4, s1-s4 (1-5 agreement) and intent_stay are ordinal''', lines=4)]),
     S("Exit Ticket", [OR("Is a mean of 3.02 on one Likert item meaningful? Give one argument each way.", "For: with many responses it summarizes the center reasonably. Against: the item is ordinal, so spacing between options may not be equal; report the median or distribution too.", lines=3)])],
    NO_TE, summary="Know your types and levels of measurement before you summarize.")

L4 = Lesson("1.4", "Reproducible Work Habits",
    "I can organize a project, comment code, read a log, and save outputs so an analysis can be rerun.", "Foundations · 30 min",
    [("raw data", "The original data exactly as received; never edited by hand."), ("script", "A saved file of code that runs the analysis from start to finish."),
     ("version control", "A system (such as Git) that records every change to your files.")],
    "Have you ever reopened an old spreadsheet and had no idea how a number was calculated? What would have saved you?",
    [Text("Reproducible work is a habit, not a tool. A few rules make a big difference:"),
     Bullets(["Keep a project folder: <font name='Mono'>data/raw</font>, <font name='Mono'>data/clean</font>, <font name='Mono'>code</font>, <font name='Mono'>output</font>, <font name='Mono'>docs</font>.",
              "Never edit raw data by hand; fix problems in code so the fix is recorded.", "Write a comment for <i>why</i>, not just <i>what</i>.",
              "Rerun the whole script from the top before you share results.", "Name files so they sort: <font name='Mono'>2026-11-05_item-analysis.sas</font>.",
              "Save the log (SAS) or session information so you know which versions produced the results."]),
     Code("Comment, filter, and save a result", sas='''/* Why: the program office asked for Online examinees only */
data work.online;
  set work.examinees;
  where program = "Online";
run;
proc export data=work.online outfile="&path/online_examinees.csv"
            dbms=csv replace;
run;''', python='''# Why: the program office asked for Online examinees only
online = examinees[examinees["program"] == "Online"]
online.to_csv("output/online_examinees.csv", index=False)
print(len(online))''', r='''# Why: the program office asked for Online examinees only
online <- subset(examinees, program == "Online")
write_csv(online, "output/online_examinees.csv")
nrow(online)''', output='''154 rows written'''),
     Text("<b>Reading the SAS log:</b> NOTE lines report what happened (“The data set WORK.ONLINE has 154 observations”). WARNING lines mean SAS made an assumption you should check. ERROR lines mean a step did not run. Scan the log after every run, the way you'd check rows and columns after an import."),
     Watch([("R for Data Science (2e), “Workflow: scripts and projects”", "r4ds.hadley.nz", "15 minutes"), ("Happy Git and GitHub for the useR (optional)", "happygitwithr.com", "skim the introduction")]),
     OnTheJob("Pick one analysis you'll repeat this year. Create its project folder today, and put the raw file in data/raw with a note about where it came from."),
     KeyIdea("Raw data stay untouched; scripts do every change; comments explain why; rerun from the top before sharing.")],
    [Problem("Should you fix a typo directly in a raw data file?", "No; fix it in code so the change is documented."), Problem("What does a SAS ERROR in the log mean?", "A step did not run."), Problem("How many Online examinees are there?", "154")],
    [S("Warm-Up", [SA("Folder for the original data", "data/raw"), SA("A system that records every change to files", "version control (e.g., Git)")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Log line “WARNING: Variable X is uninitialized.” What should you do?", "Check the code: X was used before it was created (often a typo)."),
                                          ("Better file name: final_v2_NEW.sas or 2026-11-05_scoring.sas?", "2026-11-05_scoring.sas"), ("Why rerun a script from the top before sharing?", "to make sure results don't depend on steps run out of order or leftover objects")]] +
                   [CODEX("Write code to save only the Evening examinees to evening_examinees.csv. How many rows?", '''evening = examinees[examinees["program"] == "Evening"]
evening.to_csv("output/evening_examinees.csv", index=False)
# 163 rows''', lines=4)]),
     S("Exit Ticket", [OR("Describe the folder structure you created for your work project.", "Answers vary.", lines=2)])],
    NO_TE, summary="Organize projects, script every change, read the log, and rerun before sharing.")

# ================================================================= Friday
REVIEW = review("Unit 1 Review", [S("Review", [SA("Six workflow steps", "question, import, clean, explore, model, communicate"), SA("Level of measurement for program", "nominal"),
                                              SA("Three checks after import", "dimensions, first rows, column types"), SA("Where to fix a data error", "in code, not in the raw file")], cols=1)])

TEST = exam("Week 1 Quiz", [
    S("Concepts (1 point each)", [
        MC("Which comes right after importing data in the workflow?", ["modeling", "cleaning and tidying", "communicating"], 1),
        MC("A 1–5 agreement item is measured at which level?", ["nominal", "ordinal", "ratio"], 1),
        MC("Hours of study is measured at which level?", ["ordinal", "interval", "ratio"], 2),
        SA("In tidy data, what does each row represent?", "one observation"),
        SA("What should you never edit by hand?", "raw data")], cols=1),
    S("Read the code (1 point each)", [
        SA("What does this print? " + mono('x <- 17.67 * 2\nx'), "[1] 35.34"),
        SA("In pandas, what does exam.shape return for exam.csv?", "(600, 32)"),
        SA("What does proc contents show?", "the variables, their types, lengths, and other attributes of a data set")], cols=1),
    S("Apply It (2 points)", [OR("Name one recurring task at work, the level of measurement of its main variable, and one summary that fits it.", "Answers vary; level and summary must match (e.g., ordinal survey item → median and percent agree).", lines=3, points=2)])],
    minutes=15, labels=["Great start.", "Review the lessons you missed.", "Redo the Code It examples before Unit 2."])

LESSONS = [L1, L2, L3, L4]
CHECKS = []
WEEKS = weeks_for(1, LESSONS, CHECKS, REVIEW, TEST)

UNIT = Unit(1, "Your Data Toolkit", "The analysis workflow; reading data in SAS, Python, and R; types and levels of measurement; reproducible habits.",
    "A week to set up your tools and your habits. You'll open SAS Studio, RStudio, and Jupyter, read the same file in all three, learn how data types and levels of measurement shape every analysis, and set up a project the way experienced analysts do.",
    ["Describe the analysis workflow.", "Import data in SAS, Python, and R and check it.", "Identify data types and levels of measurement.", "Organize reproducible projects and read a SAS log."],
    [("Foundations", "Workflow, data types, measurement levels."), ("Import", "Reading CSV files in three languages.")],
    [("workflow", "Steps from question to communication."), ("data frame", "A table of rows and columns."), ("ordinal", "Ordered categories."), ("reproducible", "Can be rerun with the same result.")],
    ["Comfort with spreadsheets.", "Some Python experience."], ["SAS OnDemand for Academics or SAS at work", "R and RStudio (or Posit Cloud)", "Python with Jupyter", "The VenvLearning data pack"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Most of the time you spend on an analysis goes into getting data in and checking it. These habits make every later skill faster and more trustworthy.",
    weeks=WEEKS)
