"""Data Science & Psychometrics · Unit 2: Data Wrangling — filtering, scoring, grouped summaries, missing data, joins, reshaping,
cleaning, validation, SQL, functions, an end-to-end scoring pipeline, dates, text, and codebooks (Nov 9 – Dec 11, 2026)."""
from engine import *
from content.datakit import S, MC, OR, SA, DRAW, CODEX, mono, quiz, review, exam, weeks_for, NO_TE

KEYS = '"B" "A" "A" "D" "A" "B" "B" "A" "C" "C" "D" "A" "D" "A" "A" "C" "A" "D" "C" "A" "B" "D" "C" "A" "C" "A" "C" "A" "B" "B"'

# ================================================================= Week 2 · Core verbs
L1 = Lesson("2.1", "Selecting Columns and Filtering Rows",
    "I can keep the columns I need and the rows that meet one or more conditions.", "Wrangling · 30 min",
    [("filter", "Keep only the rows that meet a condition."), ("select", "Keep only certain columns."), ("Boolean condition", "A true/false test, such as hours_prep >= 30.")],
    "A program director asks, “How many Online examinees prepared at least 30 hours?” How would you answer in under a minute?",
    [Text("Almost every question starts by narrowing the data. Filtering keeps rows; selecting keeps columns. Combine conditions with <b>and</b> (both must be true) or <b>or</b> (either can be true)."),
     Code("Online examinees with 30+ hours of prep", sas='''data work.online_hi;
  set work.examinees(keep=id program hours_prep);
  where program = "Online" and hours_prep >= 30;
run;   /* log: WORK.ONLINE_HI has 27 observations */''', python='''online_hi = examinees.loc[
    (examinees["program"] == "Online") & (examinees["hours_prep"] >= 30),
    ["id", "program", "hours_prep"]]
print(len(online_hi))''', r='''library(dplyr)
online_hi <- examinees |>
  filter(program == "Online", hours_prep >= 30) |>
  select(id, program, hours_prep)
nrow(online_hi)''', output='''27''', note="In pandas, wrap each condition in parentheses and use &amp; (and) or | (or). In dplyr, commas inside filter() mean “and.”"),
     Figure(lambda t: table(t, [["Task", "SAS", "Python (pandas)", "R (dplyr)"], ["keep columns", "KEEP= or KEEP statement", "df[[cols]] or .loc", "select()"], ["keep rows", "WHERE", "boolean mask or .query()", "filter()"],
                                ["and / or / not", "and, or, not", "&amp;, |, ~", ", or &amp;, |, !"], ["in a list", "in (\"Day\", \"Online\")", ".isin([...])", "%in% c(...)"]],
                            [1.2 * inch, 1.5 * inch, 1.6 * inch, 1.5 * inch], width=5.8 * inch, font_size=8.5)),
     Watch([("R for Data Science (2e), “Data transformation,” rows and columns", "r4ds.hadley.nz", "20 minutes"), ("SAS Programming 1: Essentials, “Preparing Data”", "learn.sas.com (free)", None),
            ("DataCamp (optional): Data Manipulation with pandas, Ch. 1", "datacamp.com", None)]),
     KeyIdea("Filter rows with conditions, select the columns you need, and check the row count.")],
    [Problem("How many examinees are Online with 30+ hours?", "27"), Problem("pandas operator for “or”", "|"), Problem("dplyr function to keep rows", "filter()")],
    [S("Warm-Up", [SA("Keep only certain columns =", "select"), SA("SAS statement to keep rows", "WHERE")], cols=2),
     S("Practice", [CODEX("How many examinees are in the South region and the Evening program?", '''examinees |> filter(region == "South", program == "Evening") |> nrow()
# 49''', lines=3),
                    CODEX("How many examinees have prior_gpa of 3.5 or higher?", '''(examinees["prior_gpa"] >= 3.5).sum()   # 81''', lines=3),
                    CODEX("Keep Day or Online examinees (use “in a list”). How many rows?", '''data work.day_online; set work.examinees; where program in ("Day", "Online"); run;
/* 437 observations */''', lines=3)]),
     S("Exit Ticket", [OR("Why check the row count after every filter?", "To confirm the condition did what you meant; a wrong condition (or a typo in a category) silently returns the wrong rows.", lines=2)])],
    NO_TE, summary="Filter rows, select columns, and check the count.")

L2 = Lesson("2.2", "Creating Variables: Scoring a Test",
    "I can create new variables, including scoring multiple-choice responses against a key and computing a total score.", "Wrangling · Psychometrics · 30 min",
    [("scoring", "Turning responses into points, such as 1 for correct and 0 for incorrect."), ("array (SAS)", "A temporary name for a group of variables so you can loop over them."),
     ("vectorized", "Applied to a whole column at once instead of one value at a time.")],
    "Your exam data arrive as letters. Before any psychometric analysis, someone has to turn A, B, C, D into 1s and 0s. Who on your team does that, and how?",
    [Text("Scoring is the first transformation in almost every testing project. Each response is compared with the key: a match scores 1, anything else (wrong letter or omitted) scores 0. The <b>total score</b> is the sum of the item scores."),
     Code("Score 30 items against the key", sas=f'''data work.scored;
  set work.exam;
  array resp{{30}} $ i01-i30;
  array key{{30}} $ _temporary_ ({KEYS});
  array sc{{30}} s01-s30;
  do j = 1 to 30;
    sc{{j}} = (resp{{j}} = key{{j}});      /* 1 if match, else 0 */
  end;
  total = sum(of s01-s30);
  drop j;
run;''', python='''key = pd.read_csv("data/exam_key.csv")
items = key["item"].tolist()
key_map = dict(zip(key["item"], key["key"]))
scored = pd.DataFrame({it: (exam[it] == k).astype(int)
                       for it, k in key_map.items()})
scored["total"] = scored[items].sum(axis=1)
scored.insert(0, "id", exam["id"])''', r='''key <- read_csv("data/exam_key.csv")
items <- key$item
scored <- as.data.frame(mapply(
  function(x, k) as.integer(!is.na(x) & x == k),
  exam[items], key$key))
scored$total <- rowSums(scored[items])
scored$id <- exam$id''', output='''first three totals (E1001, E1002, E1003): 29, 22, 27
mean total = 17.67 out of 30'''),
     WatchOut("In R, comparing a missing value gives NA, not FALSE, so an omitted response would make the whole total NA. The <font name='Mono'>!is.na(x) &amp;</font> part scores omits as 0. SAS and pandas already treat a blank as “not a match.”"),
     OnTheJob("Ask how omitted responses are scored in your program. Treating omits as wrong, as missing, or as “not reached” changes item statistics, and it should be a documented decision."),
     Watch([("Python for Data Analysis (3E), “Data Cleaning and Preparation,” data transformation", "wesmckinney.com/book", None), ("SAS Programming 2 topics: arrays and DO loops (search “SAS arrays” in SAS documentation)", "documentation.sas.com", None)]),
     KeyIdea("Score by comparing each response with its key (1 = match, 0 = otherwise), then sum for a total.")],
    [Problem("What is E1001's total score?", "29"), Problem("How is an omitted response scored here?", "0 (not a match)"), Problem("Why add !is.na(x) in R?", "so missing responses score 0 instead of NA")],
    [S("Warm-Up", [SA("1 for a match, 0 otherwise is called…", "dichotomous scoring"), SA("Key for item i01", "B")], cols=2),
     S("Practice", [SA("What proportion of examinees answered i01 correctly?", "0.415"), SA("What proportion answered i05 correctly?", "0.96"),
                    CODEX("Score the test and report the mean, minimum, and maximum total.", '''scored["total"].describe()   # mean 17.67, min 3, max 29''', lines=4),
                    CODEX("Create pass = 1 if total >= 20, else 0. How many passed?", '''scored["pass"] = (scored["total"] >= 20).astype(int); scored["pass"].sum()   # 237''',
                          lines=3, note="237 of 600 pass.")]),
     S("Exit Ticket", [OR("Explain in plain words what the scoring code does.", "For each item, it compares each person's answer to the key, records 1 for a match and 0 otherwise, then adds the 30 item scores into a total.", lines=2)])],
    NO_TE, summary="Compare each response with the key, then sum the item scores.")

L3 = Lesson("2.3", "Sorting, Counting, and Grouped Summaries",
    "I can sort data, count categories, and summarize a variable for each group.", "Wrangling · 30 min",
    [("group by", "Split the data into groups, summarize each, and combine the results."), ("frequency table", "A table of how many rows fall in each category.")],
    "Leaders rarely want 600 rows; they want one line per program. How do you get from rows to that summary?",
    [Text("<b>Split–apply–combine</b> is the pattern behind most reports: split rows into groups, apply a summary to each group, and combine the results into a small table."),
     Code("Hours of preparation by program", sas='''proc freq data=work.examinees;
  tables program program*gender / nocol nopercent;
run;
proc means data=work.examinees n mean median maxdec=2;
  class program;
  var hours_prep;
run;''', python='''print(examinees["program"].value_counts())
print(examinees.groupby("program")["hours_prep"]
      .agg(["count", "mean", "median"]).round(2))''', r='''count(examinees, program)
examinees |>
  group_by(program) |>
  summarise(n = n(), mean = mean(hours_prep), median = median(hours_prep))''',
          output='''program   n    mean   median
Day       283  18.73  18
Evening   163  20.28  19
Online    154  19.84  18'''),
     Text("Sort with <font name='Mono'>proc sort</font> (SAS), <font name='Mono'>sort_values()</font> (pandas), or <font name='Mono'>arrange()</font> (dplyr). Sorting descending puts the largest values first: in SAS add <font name='Mono'>descending</font> before the variable; in pandas use <font name='Mono'>ascending=False</font>; in dplyr wrap the variable in <font name='Mono'>desc()</font>."),
     Watch([("R for Data Science (2e), “Data transformation,” groups", "r4ds.hadley.nz", None), ("Python for Data Analysis (3E), “Data Aggregation and Group Operations”", "wesmckinney.com/book", None),
            ("SAS Programming 1: Essentials, “Analyzing and Reporting on Data”", "learn.sas.com (free)", None)]),
     KeyIdea("Split–apply–combine turns rows into the summary tables leaders need.")],
    [Problem("How many Evening examinees are there?", "163"), Problem("Which program prepared the most hours on average?", "Evening (20.28)"), Problem("dplyr function for sorting", "arrange()")],
    [S("Warm-Up", [SA("Count of rows in each category", "frequency table"), SA("SAS procedure for counts", "PROC FREQ")], cols=2),
     S("Practice", [SA("How many Day examinees are female (F)?", "150"),
                    CODEX("Count examinees by region. Which region is largest?", '''examinees["region"].value_counts()   # South 186, East 169, West 129, North 116''', lines=3),
                    CODEX("Sort examinees by hours_prep, largest first. What is the maximum?", '''proc sort data=work.examinees out=work.sorted; by descending hours_prep; run;   /* 58 */''', lines=3)]),
     S("Exit Ticket", [OR("Describe split–apply–combine in your own words with a work example.", "Answers vary.", lines=2)])],
    NO_TE, summary="Count categories and summarize by group (split–apply–combine).")

L4 = Lesson("2.4", "Missing Data: Finding and Handling It",
    "I can count missing values, describe why they matter, and choose a reasonable first strategy.", "Wrangling · 30 min",
    [("listwise deletion", "Dropping any row with a missing value on the variables used."), ("pairwise deletion", "Using all available data for each statistic, so different statistics may use different rows."),
     ("missing completely at random (MCAR)", "Missingness unrelated to any data, observed or not.")],
    "A survey summary says “n = 800,” but a table inside uses only 536 people. Where did 264 respondents go?",
    [Text("Missing data are normal; ignoring them isn't. First <b>count</b> them (by variable and by row). Then ask <b>why</b> they're missing. Data that are missing completely at random cost you precision; data missing for a reason (for example, unhappy staff skipping workload questions) can bias results."),
     Code("Count missing values in survey.csv", sas='''proc import datafile="&path/survey.csv" out=work.survey dbms=csv replace;
  getnames=yes; guessingrows=max;
run;
proc means data=work.survey n nmiss;
  var e1-e4 w1-w4 s1-s4;
run;
data _null_;
  set work.survey end=last;
  complete + (cmiss(of e1-e4, of w1-w4, of s1-s4) = 0);
  if last then put complete=;
run;''', python='''survey = pd.read_csv("data/survey.csv")
item_cols = [f"{p}{k}" for p in "ews" for k in range(1, 5)]
print(survey[item_cols].isna().sum())
print(survey[item_cols].dropna().shape[0])   # complete rows''', r='''survey <- read_csv("data/survey.csv")
item_cols <- c(paste0("e", 1:4), paste0("w", 1:4), paste0("s", 1:4))
colSums(is.na(survey[item_cols]))
sum(complete.cases(survey[item_cols]))''', output='''missing per item: e1 23, w2 30, s1 31, ... (about 3% each)
complete rows: 536 of 800'''),
     Figure(lambda t: table(t, [["Strategy", "When it's reasonable", "Risk"], ["listwise deletion", "little missingness, plausibly random", "loses many rows when missingness is spread across items"],
                                ["pairwise / available-case", "descriptive statistics item by item", "statistics based on different people"], ["scale mean of answered items", "multi-item scales, e.g., at least 3 of 4 answered", "assumes skipped items resemble answered ones"],
                                ["multiple imputation / FIML", "modeling with meaningful missingness", "more complex; needs care"]], [1.6 * inch, 2.2 * inch, 2.1 * inch], width=5.9 * inch, font_size=8.5)),
     Text("Notice what happened above: each item is only about 3% missing, yet one third of respondents are missing <i>something</i>. Listwise deletion would throw away 264 people. That's why scale scores are often computed from the items each person answered."),
     Watch([("R for Data Science (2e), “Missing values”", "r4ds.hadley.nz", None), ("Python for Data Analysis (3E), “Handling Missing Data”", "wesmckinney.com/book", None)]),
     OnTheJob("When a report gives an n, ask whether it's everyone or complete cases only, and how missing data were handled. It's one of the most useful questions you can bring to a technical review."),
     KeyIdea("Count missingness by variable and by row, think about why it's missing, and document your strategy.")],
    [Problem("How many survey rows are complete on all 12 items?", "536"), Problem("How many responses are missing on w2?", "30"), Problem("What is listwise deletion?", "dropping any row with a missing value")],
    [S("Warm-Up", [SA("pandas: count missing per column", "df.isna().sum()"), SA("R: rows with no missing values", "complete.cases()")], cols=2),
     S("Practice", [SA("How many respondents are missing at least one item?", "264"), SA("Mean of e1 using all available responses", "3.017 (777 responses)"),
                    CODEX("Compute each person's mean on e1–e4, using answered items only. Then count people who answered fewer than 3 of the 4.", '''eng = ["e1", "e2", "e3", "e4"]
survey["eng_mean"] = survey[eng].mean(axis=1)          # skips NaN
(survey[eng].notna().sum(axis=1) < 3).sum()   # 3 people''', lines=5,
                          note="The rule “at least 3 of 4 answered” is common; record it in your codebook.")]),
     S("Exit Ticket", [OR("Why can 3% missing per item turn into 33% incomplete rows?", "Missing values fall on different items for different people, so the chance a row is missing something grows with the number of items.", lines=2)])],
    NO_TE, summary="Count missing data, ask why, choose and document a strategy.")

# ================================================================= Week 3 · Combining and reshaping
L5 = Lesson("2.5", "Joining Tables",
    "I can join two tables on a key and check that the join kept the rows I expected.", "Wrangling · 30 min",
    [("key", "A column that identifies matching rows across tables, such as id."), ("left join", "Keep every row of the left table and add matching columns from the right."),
     ("inner join", "Keep only rows with a match in both tables.")],
    "Scores live in one file and demographics in another. How do you get mean score by program?",
    [Text("Joins combine tables using a <b>key</b>. A <b>left join</b> keeps every row of your main table (here, the scored exam) and attaches matching information. Always compare row counts before and after: an unexpected change usually means duplicate or missing keys."),
     Code("Attach examinee information to scores", sas='''proc sql;
  create table work.scored_info as
  select s.id, s.total, e.program, e.gender, e.region, e.hours_prep
  from work.scored as s left join work.examinees as e
       on s.id = e.id;
quit;
proc means data=work.scored_info mean maxdec=2;
  class program;  var total;
run;''', python='''scored_info = scored[["id", "total"]].merge(
    examinees, on="id", how="left", validate="one_to_one")
print(len(scored_info))
print(scored_info.groupby("program")["total"].mean().round(2))''', r='''scored_info <- scored |>
  select(id, total) |>
  left_join(examinees, by = "id")
nrow(scored_info)
scored_info |> group_by(program) |> summarise(mean_total = mean(total))''',
          output='''600 rows
Day 17.64   Evening 17.92   Online 17.47'''),
     Text("pandas' <font name='Mono'>validate=\"one_to_one\"</font> stops with an error if either table has duplicate ids, a built-in safety check. In SAS, the classic alternative is a DATA step <font name='Mono'>MERGE</font> with a <font name='Mono'>BY id</font> statement after sorting both tables by id."),
     Watch([("R for Data Science (2e), “Joins”", "r4ds.hadley.nz", "25 minutes"), ("Python for Data Analysis (3E), “Data Wrangling: Join, Combine, and Reshape”", "wesmckinney.com/book", None),
            ("DataCamp (optional): Joining Data with pandas or Joining Data with dplyr", "datacamp.com", None)]),
     KeyIdea("Join on a key, choose the join type on purpose, and check row counts before and after.")],
    [Problem("After the left join, how many rows?", "600"), Problem("Mean total for Evening", "17.92"), Problem("Which join keeps only matches in both tables?", "inner join")],
    [S("Warm-Up", [SA("The column used to match rows", "key"), SA("Join that keeps every row of the main table", "left join")], cols=2),
     S("Practice", [SA("Mean total for females (F)", "17.75"), SA("Mean total for the South region", "18.08"),
                    CODEX("What is the correlation between hours_prep and total? (Join first.)", '''scored_info["hours_prep"].corr(scored_info["total"])   # 0.449''', lines=3),
                    OR("What would you suspect if a left join turned 600 rows into 612?", "Duplicate keys in the right table: some ids matched more than one row.", lines=2)]),
     S("Exit Ticket", [OR("Write the question you'd ask before choosing left vs inner join.", "Do I need to keep every row of my main table even if there's no match?", lines=2)])],
    NO_TE, summary="Join on a key and verify the row count.")

L6 = Lesson("2.6", "Reshaping Data: Wide and Long",
    "I can reshape item data from wide (one column per item) to long (one row per person-item) and back.", "Wrangling · Psychometrics · 30 min",
    [("wide format", "One row per person, one column per item."), ("long format", "One row per person-item combination."), ("pivot", "Reshape between wide and long.")],
    "To compute statistics for every item at once, which is easier: 30 columns or one column called item?",
    [Text("Exam data usually arrive <b>wide</b>. Many item-level analyses are easier <b>long</b>: one column says which item, one column holds the score, and a grouped summary gives every item's statistics in one step."),
     Code("Wide to long, then proportion correct by item", sas='''proc sort data=work.scored; by id; run;
proc transpose data=work.scored out=work.long(rename=(col1=score _name_=item));
  by id;
  var s01-s30;
run;
proc means data=work.long mean maxdec=3 nway;
  class item;  var score;
  output out=work.item_p mean=p;
run;''', python='''long = scored.melt(id_vars="id", value_vars=items,
                   var_name="item", value_name="score")
print(long.shape)                                   # (18000, 3)
item_p = long.groupby("item")["score"].mean().round(3)
print(item_p.sort_values().head(3))''', r='''library(tidyr)
long <- scored |>
  pivot_longer(all_of(items), names_to = "item", values_to = "score")
dim(long)
long |> group_by(item) |> summarise(p = mean(score)) |> arrange(p) |> head(3)''',
          output='''18000 rows (600 people x 30 items)
hardest: i17 0.307, i21 0.315, i13 0.328'''),
     Text("Going back to wide uses <font name='Mono'>proc transpose</font> without the rename, <font name='Mono'>pivot()</font> or <font name='Mono'>pivot_table()</font> in pandas, and <font name='Mono'>pivot_wider()</font> in R."),
     Watch([("R for Data Science (2e), “Data tidying,” pivoting", "r4ds.hadley.nz", "20 minutes"), ("Python for Data Analysis (3E), “Reshaping and Pivoting”", "wesmckinney.com/book", None)]),
     KeyIdea("Long format turns “do this for every item” into one grouped summary.")],
    [Problem("How many rows does the long table have?", "18,000"), Problem("Which item is hardest?", "i17 (0.307)"), Problem("pandas function for wide → long", "melt()")],
    [S("Warm-Up", [SA("One row per person, one column per item", "wide"), SA("R function for wide → long", "pivot_longer()")], cols=2),
     S("Practice", [SA("Which three items are easiest?", "i05 (0.96), i29 (0.918), i26 (0.875)"),
                    CODEX("Add each item's domain to the long data (join with exam_key) and compute mean proportion correct by domain.", '''long |> left_join(key, by = "item") |> group_by(domain) |> summarise(p = mean(score))
# Reasoning 0.638, Content 0.590, Application 0.539''', lines=4)]),
     S("Exit Ticket", [OR("Give one analysis that's easier in wide format and one that's easier in long.", "Wide: total scores, correlations between items. Long: statistics for every item by group, plots by item.", lines=2)])],
    NO_TE, summary="Pivot between wide and long to fit the analysis.")

L7 = Lesson("2.7", "Cleaning Messy Data",
    "I can standardize text categories, convert numbers stored as text, and parse dates in mixed formats.", "Wrangling · 30 min",
    [("standardize", "Make values that mean the same thing look the same."), ("coerce", "Convert to another type, turning values that can't convert into missing."),
     ("whitespace", "Invisible spaces or tabs, often at the ends of text values.")],
    "Open messy_enrollment.csv. How many different ways is “Online” written?",
    [Text("Real files are messy: <i>Day</i>, <i>day</i>, and <i>DAY&nbsp;</i> (with a trailing space) are the same program; fees appear as <i>336</i>, <i>$328.00</i>, <i>N/A</i>, or blank; dates arrive as <i>2026-09-06</i>, <i>09/04/2026</i>, or <i>Aug 12, 2026</i>. Fix them in code, one column at a time, and check counts after each fix."),
     Code("Clean program, status, fee, and date", sas='''data work.clean;
  set work.messy;          /* imported with all columns as text */
  length program_c status_c $10;
  program_c = propcase(strip(program));
  if lowcase(program_c) = "on-line" then program_c = "Online";
  status_c = propcase(strip(status));
  fee_c = input(compress(fee, "$,"), ?? best12.);   /* N/A, blank -> . */
  if index(enroll_date, "/") then date_c = input(enroll_date, mmddyy10.);
  else if anydigit(substr(enroll_date, 1, 1)) then date_c = input(enroll_date, yymmdd10.);
  else date_c = input(cats(scan(enroll_date, 2, " ,"), scan(enroll_date, 1, " "),
                           scan(enroll_date, 3, " ,")), date9.);
  format date_c yymmdd10.;
run;
proc freq data=work.clean; tables program_c status_c; run;''', python='''messy = pd.read_csv("data/messy_enrollment.csv", dtype=str, keep_default_na=False)
messy["program_c"] = (messy["program"].str.strip().str.lower()
                      .replace({"on-line": "online"}).str.title())
messy["status_c"] = messy["status"].str.strip().str.title()
messy["fee_c"] = pd.to_numeric(messy["fee"].str.replace(r"[$,]", "", regex=True),
                               errors="coerce")
messy["date_c"] = pd.to_datetime(messy["enroll_date"], format="mixed")
print(messy["program_c"].value_counts())''', r='''library(stringr); library(lubridate)
messy <- read_csv("data/messy_enrollment.csv", col_types = cols(.default = "c"))
messy <- messy |> mutate(
  program_c = str_to_title(str_trim(str_replace(str_to_lower(program), "on-line", "online"))),
  status_c  = str_to_title(str_trim(status)),
  fee_c     = suppressWarnings(as.numeric(str_remove_all(fee, "[$,]"))),
  date_c    = as_date(parse_date_time(enroll_date, orders = c("Ymd", "mdY", "bdY"))))
count(messy, program_c)''', output='''program_c: Online 23, Day 21, Evening 19   (63 rows, before removing duplicates)
status_c:  Active 48, Withdrawn 15
fee_c:     10 missing (N/A or blank)'''),
     WatchOut("Read messy files with every column as text first (dtype=str, cols(.default = \"c\")). Letting software guess types can silently turn “N/A” or “$328.00” into missing values before you see them."),
     Watch([("R for Data Science (2e), “Strings” and “Dates and times”", "r4ds.hadley.nz", None), ("DataCamp (optional): Cleaning Data in Python or Cleaning Data in R", "datacamp.com", None)]),
     KeyIdea("Standardize text, coerce numbers and dates on purpose, and recount after each fix.")],
    [Problem("How many rows are Online after cleaning (before de-duplicating)?", "23"), Problem("How many fees are missing?", "10"), Problem("Why read every column as text first?", "to see and fix problem values before automatic type guessing hides them")],
    [S("Warm-Up", [SA("Remove spaces at the ends of text", "strip / trim"), SA("Convert, turning failures into missing", "coerce")], cols=2),
     S("Practice", [SA("How many distinct raw spellings does program have?", "8"), SA("Status counts after cleaning", "Active 48, Withdrawn 15"),
                    CODEX("What is the mean cleaned fee (all 63 rows, ignoring missing)?", '''messy["fee_c"].mean().round(2)   # 280.28''', lines=3),
                    SA("In which month did most enrollments occur?", "August")]),
     S("Exit Ticket", [OR("Why fix data in code rather than in Excel?", "The fix is documented, repeatable, and can be reapplied when new data arrive.", lines=2)])],
    NO_TE, summary="Standardize, coerce, parse, and recount.")

L8 = Lesson("2.8", "Duplicates and Validation Checks",
    "I can find and remove duplicate records and write checks that catch impossible values.", "Wrangling · 30 min",
    [("duplicate", "A record that appears more than once."), ("validation check", "A rule the data must satisfy, such as scores between 0 and 30."),
     ("assertion", "A line of code that stops the program if a condition is false.")],
    "If a score file has a duplicated person, what happens to item statistics and pass rates?",
    [Text("Duplicates inflate counts and distort statistics. Exact duplicates (every column identical) are usually copy errors; duplicate <b>ids</b> with different values need investigation. After de-duplicating, write <b>validation checks</b>: rules the clean data must satisfy."),
     Code("Remove exact duplicates and validate", sas='''proc sort data=work.clean out=work.dedup nodupkey;
  by _all_;
run;                     /* log: 3 duplicate observations deleted; 60 remain */
data _null_;
  set work.dedup;
  if program_c not in ("Day", "Evening", "Online") then
    put "CHECK: unexpected program " id= program_c=;
  if not missing(fee_c) and (fee_c < 0 or fee_c > 1000) then
    put "CHECK: fee out of range " id= fee_c=;
run;''', python='''dedup = messy.drop_duplicates()
print(len(messy) - len(dedup), "duplicates removed;", len(dedup), "rows")
assert dedup["id"].is_unique, "duplicate ids remain"
assert dedup["program_c"].isin(["Day", "Evening", "Online"]).all()
assert dedup["fee_c"].dropna().between(0, 1000).all()''', r='''dedup <- distinct(messy)
nrow(messy) - nrow(dedup)          # duplicates removed
stopifnot(!anyDuplicated(dedup$id),
          all(dedup$program_c %in% c("Day", "Evening", "Online")),
          all(between(na.omit(dedup$fee_c), 0, 1000)))''', output='''3 duplicates removed; 60 rows remain (E1004, E1018, E1042 were duplicated)
all checks pass'''),
     OnTheJob("Write three validation rules for your next score file: valid ids, scores in range, and one rule only your team would know (for example, Form B examinees must have anchor items)."),
     Watch([("SAS Programming 1: Essentials, “Exploring and Validating Data”", "learn.sas.com (free)", None)]),
     KeyIdea("De-duplicate, then let code check the rules your data must follow.")],
    [Problem("How many exact duplicates were in messy_enrollment?", "3"), Problem("How many rows remain?", "60"), Problem("What does an assertion do when its condition is false?", "stops the program with an error")],
    [S("Warm-Up", [SA("pandas: remove exact duplicates", "drop_duplicates()"), SA("R: stop if a condition fails", "stopifnot()")], cols=2),
     S("Practice", [SA("After de-duplicating, how many Active enrollments?", "45"), SA("Withdrawn by program (Day, Evening, Online)", "9, 4, 2"),
                    CODEX("Write a validation check that every total score in your scored data is between 0 and 30.", '''assert scored["total"].between(0, 30).all()
stopifnot(all(scored$total >= 0 & scored$total <= 30))''', lines=3)]),
     S("Exit Ticket", [OR("What's the difference between an exact duplicate and a duplicate id with different values?", "Exact duplicates are copies and can be dropped; duplicate ids with different values are conflicting records that need investigation.", lines=2)])],
    NO_TE, summary="Remove duplicates and automate validation rules.")

# ================================================================= Week 4 · SQL, functions, pipeline
L9 = Lesson("2.9", "SQL for Analysts I: SELECT, WHERE, GROUP BY",
    "I can write SQL queries that filter and summarize a table, and run them from SAS, Python, and R.", "SQL · 30 min",
    [("SQL", "Structured Query Language, the standard language for databases."), ("query", "A request for data written in SQL."), ("aggregate", "A summary such as COUNT, AVG, or SUM.")],
    "Much of your organization's data probably lives in a database. What would it change if you could pull exactly what you need yourself?",
    [Text("SQL reads almost like English. The same query runs in SAS (<font name='Mono'>PROC SQL</font>), in Python (here with the built-in sqlite3 module), and in R (with DBI). Learn SQL once and you can use it everywhere."),
     Code("Count and average by program", sas='''proc sql;
  select program, count(*) as n, avg(hours_prep) as mean_hours format=6.2
  from work.examinees
  where prior_gpa >= 3.0
  group by program
  order by mean_hours desc;
quit;''', python='''import sqlite3
con = sqlite3.connect(":memory:")
examinees.to_sql("examinees", con, index=False)
q = """
SELECT program, COUNT(*) AS n, ROUND(AVG(hours_prep), 2) AS mean_hours
FROM examinees
WHERE prior_gpa >= 3.0
GROUP BY program
ORDER BY mean_hours DESC"""
print(pd.read_sql(q, con))''', r='''library(DBI)
con <- dbConnect(RSQLite::SQLite(), ":memory:")
dbWriteTable(con, "examinees", examinees)
dbGetQuery(con, "
  SELECT program, COUNT(*) AS n, ROUND(AVG(hours_prep), 2) AS mean_hours
  FROM examinees WHERE prior_gpa >= 3.0
  GROUP BY program ORDER BY mean_hours DESC")''', output='''program   n    mean_hours
Evening   86   20.06
Online    78   19.78
Day      150   18.78'''),
     Figure(lambda t: table(t, [["Clause", "Job", "Order SQL runs it"], ["SELECT", "columns and summaries to return", "5"], ["FROM", "which table", "1"], ["WHERE", "filter rows before grouping", "2"],
                                ["GROUP BY", "form groups", "3"], ["HAVING", "filter groups after summarizing", "4"], ["ORDER BY", "sort the result", "6"]], [1.2 * inch, 3.2 * inch, 1.4 * inch], width=5.8 * inch, font_size=9)),
     Watch([("SAS Programming 1: Essentials, “Using SQL in SAS”", "learn.sas.com (free)", None), ("DataCamp (optional): Introduction to SQL", "datacamp.com", None)]),
     KeyIdea("SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY: one language for every database and all three of your tools.")],
    [Problem("Which clause filters rows before grouping?", "WHERE"), Problem("Which clause filters groups after summarizing?", "HAVING"), Problem("SAS procedure that runs SQL", "PROC SQL")],
    [S("Warm-Up", [SA("SQL clause that names the table", "FROM"), SA("SQL function that counts rows", "COUNT(*)")], cols=2),
     S("Practice", [CODEX("Change the query to prior_gpa >= 3.5. How many examinees qualify in total?", '''SELECT COUNT(*) FROM examinees WHERE prior_gpa >= 3.5;   -- 81''', lines=4),
                    CODEX("Write a query: number of examinees by region, only regions with more than 150 people.", '''SELECT region, COUNT(*) AS n FROM examinees GROUP BY region HAVING COUNT(*) > 150;
-- South 186, East 169''', lines=4)]),
     S("Exit Ticket", [OR("Why can't you use WHERE COUNT(*) > 150?", "WHERE runs before grouping, so counts don't exist yet; use HAVING.", lines=2)])],
    NO_TE, summary="SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY.")

L10 = Lesson("2.10", "SQL for Analysts II: Joins and Subqueries",
    "I can join tables and use a subquery in SQL.", "SQL · 30 min",
    [("subquery", "A query inside another query."), ("alias", "A short temporary name for a table or column.")],
    "Which examinees scored above the overall average, and what programs are they in?",
    [Text("SQL joins work like the joins in Lesson 2.5. A <b>subquery</b> lets one query use the result of another, such as the overall mean score."),
     Code("Examinees above the mean, with their program", sas='''proc sql;
  create table work.above as
  select s.id, s.total, e.program
  from work.scored as s inner join work.examinees as e on s.id = e.id
  where s.total > (select avg(total) from work.scored);
  select program, count(*) as n from work.above group by program;
quit;''', python='''scored[["id", "total"]].to_sql("scored", con, index=False)
q = """
SELECT e.program, COUNT(*) AS n
FROM scored AS s JOIN examinees AS e ON s.id = e.id
WHERE s.total > (SELECT AVG(total) FROM scored)
GROUP BY e.program"""
print(pd.read_sql(q, con))''', r='''dbWriteTable(con, "scored", scored[, c("id", "total")])
dbGetQuery(con, "
  SELECT e.program, COUNT(*) AS n
  FROM scored AS s JOIN examinees AS e ON s.id = e.id
  WHERE s.total > (SELECT AVG(total) FROM scored)
  GROUP BY e.program")''', output='''program   n
Day       147
Evening    91
Online     77'''),
     KeyIdea("Join with ON; nest a query in parentheses when one result depends on another.")],
    [Problem("What does (SELECT AVG(total) FROM scored) return?", "the overall mean total, 17.67"), Problem("What is an alias?", "a short temporary name, like s for scored"), Problem("Which join keeps only matching rows?", "inner join (JOIN)")],
    [S("Warm-Up", [SA("A query inside a query", "subquery"), SA("Keyword for a table alias", "AS")], cols=2),
     S("Practice", [CODEX("Write a query that counts all examinees above the mean, without grouping.", '''SELECT COUNT(*) FROM scored WHERE total > (SELECT AVG(total) FROM scored);
-- 315 (147 + 91 + 77)''', lines=4),
                    CODEX("Write a query for mean total by gender, using a join.", '''SELECT e.gender, ROUND(AVG(s.total), 2) AS mean_total
FROM scored s JOIN examinees e ON s.id = e.id GROUP BY e.gender;
-- F 17.75, M 17.57''', lines=4)]),
     S("Exit Ticket", [OR("Translate the subquery example into a plain-English sentence.", "For each program, count examinees whose total is above the overall average total.", lines=2)])],
    NO_TE, summary="Join with ON; use subqueries for “compared with the overall” questions.")

L11 = Lesson("2.11", "Don't Repeat Yourself: Functions and Macros",
    "I can write a reusable function (Python, R) or macro (SAS) for a task I'd otherwise copy and paste.", "Programming · 30 min",
    [("function", "Named, reusable code that takes inputs (arguments) and returns a result."), ("macro (SAS)", "Reusable SAS code with parameters that are filled in before the code runs."),
     ("argument", "A value you pass into a function.")],
    "How many times have you copied a block of code and changed one name? What happens when you find a bug in the original?",
    [Text("When you copy code more than twice, write a function. A function puts the logic in one place, so a fix happens once. In SAS, the macro language plays this role."),
     Code("Proportion correct for any item", sas='''%macro pcorrect(item);
  proc means data=work.scored mean maxdec=3;
    var &item;
    title "Proportion correct: &item";
  run;
  title;
%mend pcorrect;
%pcorrect(s17)
%pcorrect(s05)''', python='''def p_correct(df, item):
    """Proportion of examinees who answered an item correctly."""
    return round(df[item].mean(), 3)

print(p_correct(scored, "i17"), p_correct(scored, "i05"))
print({it: p_correct(scored, it) for it in items[:3]})''', r='''p_correct <- function(df, item) {
  round(mean(df[[item]]), 3)
}
p_correct(scored, "i17"); p_correct(scored, "i05")
sapply(items[1:3], function(it) p_correct(scored, it))''', output='''i17: 0.307   i05: 0.960
i01 0.415, i02 0.660, i03 0.767'''),
     Text("The SAS macro writes code for you: <font name='Mono'>&amp;item</font> is replaced by whatever you pass in, then the PROC MEANS step runs. Python and R functions receive values and return results directly."),
     Watch([("R for Data Science (2e), “Functions”", "r4ds.hadley.nz", "20 minutes"), ("SAS Macro Language: search “SAS macro tutorial getting started” in SAS documentation", "documentation.sas.com", None)]),
     KeyIdea("Copy twice, then write a function or macro.")],
    [Problem("p_correct(scored, \"i17\") returns…", "0.307"), Problem("In SAS, what replaces &amp;item?", "the value passed to the macro, e.g., s17"), Problem("Why write functions?", "to avoid repeated code and fix bugs in one place")],
    [S("Warm-Up", [SA("A value passed into a function", "argument"), SA("SAS statement that ends a macro definition", "%mend")], cols=2),
     S("Practice", [CODEX("Write a function that returns the mean total for one program, given scored_info and a program name. Test it on Online.", '''mean_total <- function(df, prog) mean(df$total[df$program == prog])
mean_total(scored_info, "Online")   # 17.47''', lines=4),
                    CODEX("Use a loop or comprehension to get the proportion correct for all 30 items, and report the lowest.", '''ps = {it: p_correct(scored, it) for it in items}; min(ps, key=ps.get)   # i17, 0.307''', lines=3)]),
     S("Exit Ticket", [OR("Name a task at work you'd turn into a function or macro.", "Answers vary.", lines=2)])],
    NO_TE, summary="Write functions and macros instead of copying code.")

L12 = Lesson("2.12", "Putting It Together: A Scoring Pipeline",
    "I can build an end-to-end script that imports, scores, computes subscores, joins demographics, and exports a clean file.", "Wrangling · Psychometrics · 30 min",
    [("pipeline", "A script that runs every step, in order, from raw data to final output."), ("subscore", "A score on part of a test, such as one content domain.")],
    "Imagine new Form A data arrive next month. Could you produce the score file by running one script?",
    [Text("A pipeline strings together everything from this unit. Today's version computes three domain subscores (10 items each) and writes a file ready for analysis."),
     Code("Domain subscores and export", sas='''data work.final;
  merge work.scored(keep=id s01-s30 total) work.examinees;
  by id;
  reasoning   = sum(of s01-s10);
  content     = sum(of s11-s20);
  application = sum(of s21-s30);
run;
proc means data=work.final mean std maxdec=2;
  var reasoning content application total;
run;
proc export data=work.final outfile="&path/scored_formA.csv" dbms=csv replace; run;''', python='''domains = key.groupby("domain")["item"].apply(list)
for d, cols in domains.items():
    scored[d.lower()] = scored[cols].sum(axis=1)
final = scored.merge(examinees, on="id", how="left", validate="one_to_one")
print(final[["reasoning", "content", "application", "total"]].agg(["mean", "std"]).round(2))
final.to_csv("output/scored_formA.csv", index=False)''', r='''for (d in unique(key$domain)) {
  scored[[tolower(d)]] <- rowSums(scored[key$item[key$domain == d]])
}
final <- left_join(scored, examinees, by = "id")
final |> summarise(across(c(reasoning, content, application, total), list(mean = mean, sd = sd)))
write_csv(final, "output/scored_formA.csv")''', output='''            mean   sd
reasoning   6.38  2.32
content     5.90  2.11
application 5.39  2.33
total      17.67  5.88'''),
     OnTheJob("Compare this pipeline with how scoring works on your team. Which steps are automated, and which depend on someone remembering? Those are good places to suggest a script."),
     KeyIdea("One script, top to bottom: import, score, subscore, join, validate, export.")],
    [Problem("Mean Reasoning subscore", "6.38"), Problem("Which domain has the lowest mean?", "Application (5.39)"), Problem("What does validate=\"one_to_one\" protect against?", "duplicate ids in either table")],
    [S("Warm-Up", [SA("A score on part of a test", "subscore"), SA("Items in each domain", "10")], cols=2),
     S("Practice", [CODEX("Build the pipeline in the language you use least. Record the subscore means.", '''Reasoning 6.38, Content 5.90, Application 5.39, Total 17.67''', lines=5),
                    CODEX("Add a validation check that reasoning + content + application equals total for every row.", '''assert (final[["reasoning", "content", "application"]].sum(axis=1) == final["total"]).all()''', lines=3)]),
     S("Exit Ticket", [OR("Why is a subscore based on 10 items less reliable than the total?", "Fewer items means more measurement error relative to the true score (you'll quantify this in Unit 6).", lines=2)])],
    NO_TE, summary="Build one script from raw responses to an analysis-ready file.")

# ================================================================= Week 5 · Dates, text, documentation, project
L13 = Lesson("2.13", "Working with Dates",
    "I can compute differences between dates and summarize by month.", "Wrangling · 30 min",
    [("date value", "A date stored as a number (days since a reference date) so it can be compared and subtracted."), ("format (SAS)", "How a value is displayed, separate from how it is stored.")],
    "How many days before the October 1 test date did each person enroll?",
    [Text("Software stores dates as numbers: SAS counts days from January 1, 1960; R counts from January 1, 1970; pandas stores timestamps. Because they're numbers, you can subtract them to get days between events."),
     Code("Days from enrollment to the test date", sas='''data work.dates;
  set work.dedup;
  days_before = '01OCT2026'd - date_c;
  month = month(date_c);
run;
proc means data=work.dates mean min max maxdec=1; var days_before; run;
proc freq data=work.dates; tables month; run;''', python='''dedup["days_before"] = (pd.Timestamp("2026-10-01") - dedup["date_c"]).dt.days
print(dedup["days_before"].describe().round(1))
print(dedup["date_c"].dt.month.value_counts())''', r='''dedup <- dedup |> mutate(days_before = as.numeric(as_date("2026-10-01") - date_c),
                        month = month(date_c))
summary(dedup$days_before)
count(dedup, month)''', output='''E1001 enrolled 2026-09-04: 27 days before the test
month 8 (August): 40 enrollments   month 9 (September): 20'''),
     KeyIdea("Dates are numbers underneath, so you can subtract, compare, and group them.")],
    [Problem("How many days before Oct 1 did E1001 enroll?", "27"), Problem("Earliest enrollment date", "2026-08-03"), Problem("SAS date constant for Oct 1, 2026", "'01OCT2026'd")],
    [S("Warm-Up", [SA("SAS counts days from…", "January 1, 1960"), SA("pandas: extract the month", ".dt.month")], cols=2),
     S("Practice", [SA("Latest enrollment date", "2026-09-11"), SA("Enrollments in September", "20"),
                    CODEX("Compute days_before for every row and report the mean.", '''dedup["days_before"].mean()   # 39.0 days (range 20 to 59)''', lines=3)]),
     S("Exit Ticket", [OR("Why separate a date's stored value from its format?", "So calculations use the number while people see a readable date in any style.", lines=2)])],
    NO_TE, summary="Subtract dates for durations; extract parts to group.")

L14 = Lesson("2.14", "Working with Text",
    "I can extract, change, and search text values, including simple patterns.", "Wrangling · 30 min",
    [("string", "A text value."), ("substring", "Part of a string."), ("regular expression", "A pattern for matching text, such as \\d+ for one or more digits.")],
    "Ids like E1001 hide a number. Comment fields hide themes. How do you get at what's inside text?",
    [Code("Extract the number from an id and search text", sas='''data work.ids;
  set work.examinees(keep=id);
  id_num = input(substr(id, 2), 8.);
  is_formA = (char(id, 1) = "E" and id_num < 3000);
run;
data work.withdrew;
  set work.messy;
  if prxmatch("/withdr/i", status);    /* case-insensitive pattern */
run;''', python='''examinees["id_num"] = examinees["id"].str[1:].astype(int)
withdrew = messy[messy["status"].str.contains("withdr", case=False)]
print(examinees["id_num"].min(), examinees["id_num"].max(), len(withdrew))''', r='''examinees$id_num <- as.integer(str_sub(examinees$id, 2))
withdrew <- messy |> filter(str_detect(status, regex("withdr", ignore_case = TRUE)))
range(examinees$id_num); nrow(withdrew)''', output='''id numbers 1001 to 1600; 15 withdrawn rows (before removing duplicates)'''),
     Text("Regular expressions look cryptic but a few cover most needs: <font name='Mono'>\\d</font> a digit, <font name='Mono'>+</font> one or more, <font name='Mono'>^</font> start, <font name='Mono'>$</font> end, <font name='Mono'>[A-Z]</font> any capital letter."),
     Watch([("R for Data Science (2e), “Regular expressions”", "r4ds.hadley.nz", None)]),
     KeyIdea("Use substrings and patterns to pull meaning out of text, then convert to numbers when needed.")],
    [Problem("Number part of E1234", "1234"), Problem("What does \\d+ match?", "one or more digits"), Problem("Withdrawn rows (raw, with duplicates)", "15")],
    [S("Warm-Up", [SA("A text value", "string"), SA("Part of a string", "substring")], cols=2),
     S("Practice", [CODEX("Write a pattern that checks every id is E followed by exactly four digits. Do all 600 pass?", '''examinees["id"].str.fullmatch(r"E\\d{4}").all()   # True''', lines=3),
                    SA("Regex for text that starts with a capital letter", "^[A-Z]")]),
     S("Exit Ticket", [OR("Name one text field at work you could analyze with these tools.", "Answers vary.", lines=2)])],
    NO_TE, summary="Substrings and regular expressions unlock text.")

L15 = Lesson("2.15", "Codebooks and Data Documentation",
    "I can write a codebook that explains every variable in a data set.", "Documentation · 30 min",
    [("codebook", "A document listing each variable's name, meaning, type, allowed values, and how it was made."), ("label", "A longer, readable description attached to a variable."),
     ("value label / format", "Text shown in place of a code, such as 1 = Strongly disagree.")],
    "If you left your job tomorrow, could someone else understand your score file?",
    [Text("A codebook turns a data file into something others can trust and reuse. For each variable record: name, label, type, allowed values or range, missing-data codes, and how it was created (source or formula)."),
     Figure(lambda t: table(t, [["Variable", "Label", "Type", "Values", "Created from"], ["total", "Total raw score, Form A", "integer", "0–30", "sum of s01–s30; omits scored 0"],
                                ["reasoning", "Reasoning subscore", "integer", "0–10", "sum of s01–s10"], ["w3", "I have enough time to finish my work", "ordinal", "1–5; blank = missing", "reverse-worded; reverse before scoring"]],
                            [0.8 * inch, 1.6 * inch, 0.7 * inch, 1.1 * inch, 1.7 * inch], width=5.9 * inch, font_size=8.5)),
     Code("Attach labels and value formats", sas='''proc format;
  value agree 1="Strongly disagree" 2="Disagree" 3="Neutral" 4="Agree" 5="Strongly agree";
run;
data work.survey_lab;
  set work.survey;
  label e1 = "I feel energized by my work"  w3 = "I have enough time to finish my work";
  format e1-e4 w1-w4 s1-s4 agree.;
run;
proc contents data=work.survey_lab varnum; run;   /* a starter codebook */''', python='''codebook = pd.DataFrame({
    "variable": ["total", "reasoning", "w3"],
    "label": ["Total raw score, Form A", "Reasoning subscore", "I have enough time to finish my work"],
    "type": ["integer", "integer", "ordinal"],
    "values": ["0-30", "0-10", "1-5; blank = missing"]})
codebook.to_csv("docs/codebook.csv", index=False)''', r='''codebook <- tibble::tribble(
  ~variable,   ~label,                                  ~type,     ~values,
  "total",     "Total raw score, Form A",               "integer", "0-30",
  "reasoning", "Reasoning subscore",                    "integer", "0-10",
  "w3",        "I have enough time to finish my work",  "ordinal", "1-5; blank = missing")
write_csv(codebook, "docs/codebook.csv")''', output='''a codebook table saved to docs/codebook.csv (SAS: labels and formats appear in PROC CONTENTS)'''),
     OnTheJob("Start a codebook for one file you use at work. Even five well-documented variables will make your next analysis faster."),
     KeyIdea("Document every variable: name, label, type, values, missing codes, and origin.")],
    [Problem("Name four things a codebook records.", "name, label, type, allowed values (also missing codes, origin)"), Problem("What is a SAS format?", "a rule for how values are displayed"), Problem("Why note that w3 is reverse-worded?", "it must be reversed before computing scale scores")],
    [S("Warm-Up", [SA("A readable description of a variable", "label"), SA("Text shown in place of a code", "value label / format")], cols=2),
     S("Practice", [CODEX("Write codebook rows for content, application, and pass (from Lesson 2.2).", '''content: Content subscore, integer, 0-10, sum of s11-s20
application: Application subscore, integer, 0-10, sum of s21-s30
pass: Passed (total >= 20), 0/1, 1 = passed''', lines=5)]),
     S("Exit Ticket", [OR("Who benefits from a codebook besides you?", "Colleagues, reviewers, future analysts, auditors, and you in six months.", lines=2)])],
    NO_TE, summary="A codebook makes data understandable and reusable.")

L16 = Lesson("2.16", "Wrangling Project: Enrollment Meets Scores",
    "I can clean, de-duplicate, join, validate, document, and summarize a messy file from start to finish.", "Project · 30 min",
    [],
    "This is the kind of request that lands on your desk: “Can you tell us how withdrawn students were doing?”",
    [Text("Combine everything from Unit 2. Work in the language you're least comfortable with; then check your numbers in a second language."),
     Bullets(["Clean messy_enrollment.csv (program, status, fee, date) and remove exact duplicates (60 rows).", "Join the cleaned file to scored_formA.csv by id (left join; keep all 60).",
              "Validate: unique ids, valid programs, fees in range.", "Summarize mean total and mean hours_prep for Active vs Withdrawn.", "Write a three-row codebook for your new variables and a two-sentence summary for a non-technical reader."]),
     KeyIdea("Real projects use every wrangling verb. A clean, documented pipeline is the foundation for everything that follows.")],
    [Problem("How many rows after de-duplicating?", "60"), Problem("Which join keeps all enrollment rows?", "left join (enrollment on the left)"), Problem("Name one validation check.", "e.g. unique ids, valid programs, fees in range")],
    [S("Project", [CODEX("Paste or summarize your pipeline's key steps.", "Clean → de-duplicate → left join with scores → validate → summarize by status → document.", lines=8),
                   SA("Mean hours_prep for Active enrollees (after joining examinees)", "19.76"),
                   OR("Write your two-sentence summary for a program director.", "Answers vary; must state the comparison clearly without jargon.", lines=3)])],
    NO_TE, summary="One messy file, cleaned and joined, start to finish.")

# ================================================================= quizzes and exam
C1 = quiz("Week 2 Quiz", [S("Concepts and code (1 point each)", [
    MC("Which keeps rows?", ["select", "filter", "mutate"], 1), SA("pandas operator for “and” between conditions", "&amp;"),
    SA("What does this return? " + mono('(examinees["program"] == "Online").sum()'), "154"),
    SA("How is an omitted response scored in the Unit 2 scoring code?", "0"), SA("E1002's total score", "22"),
    MC("Which SAS procedure counts categories?", ["PROC MEANS", "PROC FREQ", "PROC SORT"], 1),
    SA("How many survey respondents have complete data on all 12 items?", "536"),
    OR("Why might listwise deletion bias a survey result?", "If people with missing data differ systematically (e.g., less engaged), dropping them changes the estimate.", lines=2)], cols=1)])
C2 = quiz("Week 3 Quiz", [S("Concepts and code (1 point each)", [
    MC("A left join of 600 scored rows to examinees returns 600 rows. What does that suggest?", ["duplicate keys", "one match per id", "missing ids"], 1),
    SA("Which item is hardest on Form A?", "i17"), SA("Long format has how many rows for 600 people × 30 items?", "18,000"),
    SA("R function for long → wide", "pivot_wider()"), SA("Number of distinct raw spellings of program in messy_enrollment", "8"),
    SA("How many exact duplicate rows did messy_enrollment have?", "3"),
    OR("Write a one-line check that every program value is Day, Evening, or Online (any language).", mono('assert dedup["program_c"].isin(["Day", "Evening", "Online"]).all()'), lines=2)], cols=1)])
C3 = quiz("Week 4 Quiz", [S("Concepts and code (1 point each)", [
    MC("Which clause filters groups after aggregation?", ["WHERE", "HAVING", "ORDER BY"], 1), SA("Order: SELECT, WHERE, FROM, GROUP BY (as written)", "SELECT, FROM, WHERE, GROUP BY"),
    SA("What does %mend do?", "ends a SAS macro definition"), SA("Mean Application subscore", "5.39"),
    SA("Output of p_correct(scored, \"i05\")", "0.96"),
    OR("Write a SQL query for mean hours_prep by gender.", mono("SELECT gender, AVG(hours_prep) FROM examinees GROUP BY gender;"), lines=2),
    OR("Apply It: Name one step of your team's scoring or reporting process you could script.", "Answers vary.", lines=2)], cols=1)])

REVIEW = review("Unit 2 Review", [S("Review", [
    SA("Filter vs select", "filter keeps rows; select keeps columns"), SA("Left vs inner join", "left keeps all rows of the left table; inner keeps only matches"),
    SA("Wide vs long", "wide: one column per item; long: one row per person-item"), SA("Three cleaning fixes for messy text categories", "trim spaces, standardize case, map variants (on-line → online)"),
    SA("WHERE vs HAVING", "WHERE filters rows before grouping; HAVING filters groups after"), SA("Why write functions?", "reuse logic; fix bugs once")], cols=1)])

TEST = exam("Unit 2 Exam", [
    S("Part A · Concepts (1 point each)", [
        MC("Which is a ratio-level variable?", ["program", "hours_prep", "a 1–5 agreement rating"], 1),
        MC("Which pandas method combines tables on a key?", ["melt", "merge", "pivot"], 1),
        MC("Which statement about missing data is true?", ["3% missing per item always means 3% incomplete rows", "listwise deletion can drop many more rows than any single item's missing rate", "missing values are always random"], 1),
        SA("What does validate=\"one_to_one\" check?", "that the key is unique in both tables"),
        SA("SAS: what does proc sort … nodupkey; by _all_; do?", "removes exact duplicate rows")], cols=1),
    S("Part B · Read the code (1 point each)", [
        SA("What does this compute? " + mono('long.groupby("item")["score"].mean()'), "proportion correct (p-value) for each item"),
        SA("What does this return for Form A? " + mono("SELECT COUNT(*) FROM examinees WHERE program = 'Day';"), "283"),
        SA("Result of " + mono("input(compress(\"$328.00\", \"$,\"), ?? best12.)"), "328")], cols=1),
    S("Part C · Write code (2 points each)", [
        CODEX("Score item i01 (key B) as 0/1 in any language, treating omits as 0.", '''s01 = (resp = "B");                         /* SAS */
exam["i01"].eq("B").astype(int)             # Python
as.integer(!is.na(exam$i01) & exam$i01 == "B")   # R''', lines=3, points=2),
        CODEX("Mean total by program, given a table scored_info with total and program.", '''scored_info.groupby("program")["total"].mean()''', lines=3, points=2)]),
    S("Part D · Apply (3 points)", [OR("Describe a reproducible pipeline for a score file you work with: the steps, two validation checks, and what you'd put in the codebook.",
                                       "Rubric: ordered steps from raw to output (1); two sensible validation checks (1); codebook contents named (1).", lines=8, points=3)])], minutes=30)

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = weeks_for(2, LESSONS, CHECKS, REVIEW, TEST)

UNIT = Unit(2, "Data Wrangling", "Filtering, scoring, grouped summaries, missing data, joins, reshaping, cleaning, validation, SQL, functions, dates, text, and codebooks.",
    "Experienced analysts often say most of the job is getting data ready. In this unit you'll score a 30-item test from raw letters, attach demographics, reshape item data, clean a messy file, query with SQL, and build a pipeline that produces an analysis-ready file with one run. Every step is shown in SAS, Python, and R.",
    ["Filter, select, create, sort, and summarize data by group.", "Score multiple-choice responses and compute totals and subscores.", "Handle missing data, join and reshape tables, and clean messy values.",
     "Write SQL queries, functions, and macros; validate and document data."],
    [("Wrangling", "Core data verbs in SAS, pandas, and dplyr."), ("SQL", "SELECT, joins, subqueries."), ("Psychometrics", "Dichotomous scoring, totals, subscores.")],
    [("filter", "Keep rows that meet a condition."), ("left join", "Keep all rows of the main table."), ("long format", "One row per person-item."), ("codebook", "Documentation of every variable."),
     ("subscore", "A score on part of a test."), ("validation check", "A rule the data must satisfy.")],
    ["Unit 1: importing data and checking it."], ["exam.csv, exam_key.csv, examinees.csv, survey.csv, messy_enrollment.csv"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Scoring, merging, and cleaning are where errors hide. A documented, validated pipeline is one of the most valuable things you can bring to an assessment team.",
    weeks=WEEKS)
