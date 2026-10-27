"""Builds the VenvLearning Data Science & Psychometrics data pack (synthetic, reproducible; seed 2026).

python3 textbooks/tools/make_datapack.py   ->  textbooks/data/*.csv  (+ README.txt)

All data are simulated. No real people are represented."""
import os, numpy as np, pandas as pd

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(2026)
LET = np.array(list("ABCD"))


# ---------------------------------------------------------------- examinees
N = 600
ids = [f"E{1001 + i}" for i in range(N)]
gender = rng.choice(["F", "M"], N, p=[0.55, 0.45])
region = rng.choice(["North", "South", "East", "West"], N, p=[0.22, 0.34, 0.24, 0.20])
program = rng.choice(["Day", "Evening", "Online"], N, p=[0.45, 0.30, 0.25])
hours = np.clip(np.round(rng.gamma(4, 5, N)), 0, 80).astype(int)
gpa = np.clip(np.round(rng.normal(3.0, 0.45, N), 2), 1.6, 4.0)
theta = 0.45 * (hours - hours.mean()) / hours.std() + 0.45 * (gpa - gpa.mean()) / gpa.std() + rng.normal(0, 0.78, N)
theta = (theta - theta.mean()) / theta.std()
examinees = pd.DataFrame(dict(id=ids, gender=gender, region=region, program=program, hours_prep=hours, prior_gpa=gpa))


def make_form(theta, focal, n_items, seed, anchor_params=None, flaws=True):
    r = np.random.default_rng(seed)
    a = np.round(r.uniform(0.7, 1.9, n_items), 2); b = np.round(r.normal(0, 0.9, n_items), 2); c = np.full(n_items, 0.2)
    if anchor_params is not None:
        k = len(anchor_params[0]); a[:k], b[:k] = anchor_params
    if flaws:
        b[4] = -2.8                          # i05: very easy
        b[22] = 0.1; a[22] = 1.2             # i23: DIF item (harder for focal group)
        a[11] = 0.25                         # i12: weak discrimination
        b[16] = 0.9; a[16] = 1.4             # i17: moderately hard (and miskeyed below)
    keys = r.choice(LET, n_items)
    P = c + (1 - c) / (1 + np.exp(-1.7 * a * (theta[:, None] - b[None, :])))
    if flaws:
        dif = 1 / (1 + np.exp(-1.7 * a[22] * (theta - (b[22] + 0.75))))
        P[:, 22] = np.where(focal, c[22] + (1 - c[22]) * dif, P[:, 22])
    correct = r.random(P.shape) < P
    resp = np.empty(P.shape, dtype=object)
    for j in range(n_items):
        others = [x for x in LET if x != keys[j]]
        strong = others[0]                   # one attractive distractor
        wrong = r.choice(others, size=len(theta), p=[0.55, 0.25, 0.20])
        resp[:, j] = np.where(correct[:, j], keys[j], wrong)
    if flaws:
        # i17 is miskeyed: the published key lists a wrong option, so high scorers (who choose the true answer) are marked wrong
        true17 = keys[16]; others = [x for x in LET if x != true17]; keys = keys.copy(); keys[16] = others[0]
    # a few omits (blank)
    omit = r.random(P.shape) < 0.008
    resp[omit] = ""
    return resp, keys, a, b


focal = gender == "F"
respA, keyA, aA, bA = make_form(theta, focal, 30, 11)
cols = [f"i{j + 1:02d}" for j in range(30)]
exam = pd.DataFrame(respA, columns=cols); exam.insert(0, "form", "A"); exam.insert(0, "id", ids)
domains = (["Reasoning"] * 10 + ["Content"] * 10 + ["Application"] * 10)
key = pd.DataFrame(dict(item=cols, key=keyA, domain=domains))

# Form B: new group of 600, 10 anchor items identical to Form A items 1-10
NB = 600
idsB = [f"E{3001 + i}" for i in range(NB)]
thetaB = rng.normal(0.25, 1.0, NB)            # Form B group is a bit more able
gB = rng.choice(["F", "M"], NB, p=[0.55, 0.45])
respB, keyB, aB, bB = make_form(thetaB, gB == "F", 30, 12, anchor_params=(aA[:10], bA[:10]), flaws=False)
keyB[:10] = keyA[:10]
# regenerate anchor responses with Form A keys so anchors truly match
rB = np.random.default_rng(14)
PB = 0.2 + 0.8 / (1 + np.exp(-1.7 * aA[:10] * (thetaB[:, None] - bA[None, :10])))
corrB = rB.random(PB.shape) < PB
for j in range(10):
    others = [x for x in LET if x != keyA[j]]
    respB[:, j] = np.where(corrB[:, j], keyA[j], rB.choice(others, NB, p=[0.55, 0.25, 0.20]))
examB = pd.DataFrame(respB, columns=cols); examB.insert(0, "form", "B"); examB.insert(0, "id", idsB)
keyBdf = pd.DataFrame(dict(item=cols, key=keyB, domain=domains, anchor=["yes"] * 10 + ["no"] * 20))
examineesB = pd.DataFrame(dict(id=idsB, gender=gB))

# ---------------------------------------------------------------- survey (3 factors, 12 Likert items)
NS = 800
F = rng.multivariate_normal([0, 0, 0], [[1, -0.35, 0.5], [-0.35, 1, -0.3], [0.5, -0.3, 1]], NS)
load = {"eng": [0.8, 0.75, 0.7, 0.65], "wl": [0.75, 0.7, 0.6, 0.7], "sup": [0.8, 0.7, 0.75, 0.6]}
items = {}
names = {"eng": "e", "wl": "w", "sup": "s"}
for f_i, (fac, ls) in enumerate(load.items()):
    for k, l in enumerate(ls):
        z = l * F[:, f_i] + np.sqrt(1 - l ** 2) * rng.normal(0, 1, NS)
        likert = np.digitize(z, [-1.5, -0.5, 0.5, 1.5]) + 1
        items[f"{names[fac]}{k + 1}"] = likert
items["w3"] = 6 - items["w3"]                      # w3 is reverse-worded ("I have enough time to finish my work")
survey = pd.DataFrame(items)
survey.insert(0, "dept", rng.choice(["Assessment", "Research", "Operations", "Client Services"], NS, p=[0.3, 0.2, 0.3, 0.2]))
survey.insert(0, "resp_id", [f"S{5001 + i}" for i in range(NS)])
survey["tenure_years"] = np.clip(np.round(rng.gamma(2, 2.5, NS), 1), 0.1, 30)
stay = 5.5 + 1.3 * F[:, 0] - 0.9 * F[:, 1] + 0.8 * F[:, 2] + rng.normal(0, 1.3, NS)
survey["intent_stay"] = np.clip(np.round(stay), 1, 10).astype(int)
logit = -1.4 - 0.9 * F[:, 0] + 0.7 * F[:, 1] - 0.5 * F[:, 2] - 0.06 * survey["tenure_years"]
survey["left_next_year"] = (rng.random(NS) < 1 / (1 + np.exp(-logit))).astype(int)
item_cols = [c for c in survey.columns if c[0] in "ews" and c[1:].isdigit()]
mask = rng.random((NS, len(item_cols))) < 0.03
for j, c in enumerate(item_cols):
    survey.loc[mask[:, j], c] = np.nan
for c in item_cols: survey[c] = survey[c].astype("Int64")

# ---------------------------------------------------------------- learners (program evaluation)
NL = 360
prog = rng.choice(["Standard", "Tutoring", "Online Modules"], NL, p=[0.4, 0.3, 0.3])
pre = np.clip(np.round(rng.normal(62, 10, NL)), 25, 95)
hrs = np.clip(np.round(rng.gamma(3, 4, NL), 1), 0, 60)
att = np.clip(np.round(rng.normal(88, 8, NL)), 40, 100)
eff = np.select([prog == "Standard", prog == "Tutoring", prog == "Online Modules"], [4, 9, 6])
post = np.clip(np.round(0.7 * pre + 18 + eff + 0.25 * hrs + 0.08 * (att - 88) + rng.normal(0, 6, NL)), 20, 100)
learners = pd.DataFrame(dict(learner_id=[f"L{701 + i}" for i in range(NL)], program=prog, pre_score=pre.astype(int), post_score=post.astype(int),
                             study_hours=hrs, attendance_pct=att.astype(int)))
learners["passed"] = (learners.post_score >= 75).astype(int)

# ---------------------------------------------------------------- essay ratings (inter-rater reliability)
NR = 150
true = rng.normal(3.5, 1.1, NR)
r1 = np.clip(np.round(true + rng.normal(0, 0.55, NR)), 1, 6).astype(int)
r2 = np.clip(np.round(true + 0.25 + rng.normal(0, 0.6, NR)), 1, 6).astype(int)
ratings = pd.DataFrame(dict(essay_id=[f"W{201 + i}" for i in range(NR)], rater1=r1, rater2=r2))

# ---------------------------------------------------------------- messy enrollment data (cleaning practice)
rows = []
progs = ["Day", "day", "DAY ", "Evening", "evening", "Online", "online", "On-line"]
for i in range(60):
    d = pd.Timestamp("2026-08-03") + pd.Timedelta(days=int(rng.integers(0, 40)))
    fmt = rng.choice(["%Y-%m-%d", "%m/%d/%Y", "%b %d, %Y"], p=[0.5, 0.35, 0.15])
    fee = rng.choice([f"{rng.integers(150, 400)}", f"${rng.integers(150, 400)}.00", "N/A", ""], p=[0.6, 0.25, 0.1, 0.05])
    rows.append(dict(id=ids[i], program=rng.choice(progs), enroll_date=d.strftime(fmt), fee=fee,
                     status=rng.choice(["Active", "active", "Withdrawn", "ACTIVE", "withdrawn "], p=[0.5, 0.2, 0.15, 0.1, 0.05])))
messy = pd.DataFrame(rows)
messy = pd.concat([messy, messy.iloc[[3, 17, 41]]], ignore_index=True)   # three duplicate rows

# ---------------------------------------------------------------- write
files = {"exam.csv": exam, "exam_key.csv": key, "examinees.csv": examinees, "exam_formB.csv": examB, "exam_formB_key.csv": keyBdf,
         "examinees_formB.csv": examineesB, "survey.csv": survey, "learners.csv": learners, "ratings.csv": ratings, "messy_enrollment.csv": messy}
for name, df in files.items():
    df.to_csv(os.path.join(OUT, name), index=False)
open(os.path.join(OUT, "README.txt"), "w").write("""VenvLearning Data Science & Psychometrics data pack
All data are simulated (seed 2026). No real people are represented.

exam.csv              600 examinees x 30 multiple-choice items (letters A-D; blank = omitted), Form A
exam_key.csv          answer key and content domain for each Form A item
examinees.csv         background for Form A examinees: gender, region, program, hours_prep, prior_gpa
exam_formB.csv        600 different examinees, Form B; items i01-i10 are anchor items shared with Form A
exam_formB_key.csv    Form B key, domain, and anchor flag
examinees_formB.csv   gender for Form B examinees
survey.csv            800 staff survey responses: 12 Likert items (e1-e4 engagement, w1-w4 workload, s1-s4 support;
                      w3 is reverse-worded), department, tenure, intent_stay (1-10), left_next_year (0/1); about 3% missing
learners.csv          360 learners in three programs: pre/post scores, study hours, attendance, passed
ratings.csv           150 essays scored 1-6 by two raters
messy_enrollment.csv  60 enrollment records with realistic problems to clean (formats, case, duplicates, missing)
""")
print("wrote", len(files), "files to", os.path.abspath(OUT))
