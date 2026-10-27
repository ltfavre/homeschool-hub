VenvLearning Data Science & Psychometrics data pack
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
