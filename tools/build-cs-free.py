#!/usr/bin/env python3
"""Adds the free Computer Science materials to both computer electives (Grades 4 and 7).

Block 2, Computer Foundations & Digital Citizenship (Dec 14 - Feb 5, 6 weeks x Mon-Thu):
  - TypingClub, 10 minutes every day.
  - Common Sense Education "Digital Literacy & Well-Being" (free, 20-minute lessons): all 18 grade-level
    lessons, three per week (Tue/Wed/Thu), matched to that week's booklet topic. Monday stays the
    booklet introduction.
Block 6, Coding & Game Design (Jun 21 - Jul 16, 4 weeks x Mon-Thu):
  - Grade 4: Code.org CS Fundamentals Course E (2025) coding lessons 3-16 and the two-day End of Course Project.
  - Grade 7: Code.org CS Discoveries "Interactive Animations and Games" Chapter 1 (lessons 1-18), with
    Chapter 2 listed for the two continuation weeks.
Lesson lists were read from commonsense.org and studio.code.org on 2026-10-23. Re-runnable."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curriculum_pack import load, save

CS = "https://www.commonsense.org/education/digital-literacy/"
CE = "https://studio.code.org/courses/coursee-2025/units/1/lessons/"
GL = "https://studio.code.org/courses/interactive-games-animations-2026/units/1/lessons/"
TYPING = "https://www.typingclub.com/"

# Three Common Sense lessons per block-2 week (Tue, Wed, Thu), by grade: (number, title, slug)
DL = {
 "4": [
  [(18, "Healthy Tech Habits & Our Feelings", "healthy-tech-habits-our-feelings"), (10, "Spotting Thinking Traps", "spotting-thinking-traps"), (11, "Brain Battle Game", "brain-battle-game")],
  [(3, "Communicating Clearly Online", "communicating-clearly-online"), (9, "Group Chat Dynamics", "group-chat-dynamics"), (14, "Peer Pressure Online", "peer-pressure-online")],
  [(12, "Online Tracks: What Do We Control?", "online-tracks-what-do-we-control"), (17, "Online Reputations & Our Responsibilities", "online-reputations-our-responsibilities"), (7, "Understanding Influencers", "understanding-influencers")],
  [(1, "Personally Identifiable Information", "personally-identifiable-information"), (4, "PII: What's the Risk Factor?", "pii-whats-the-risk-factor"), (2, "Media & Our Emotions", "media-our-emotions")],
  [(8, "Gone Phishing", "gone-phishing"), (6, "S.I.F.T. for Sources", "sift-for-sources"), (13, "Slicing Up Media with P.I.E.", "slicing-up-media-with-pie")],
  [(5, "S.T.A.N.D. Up to Cyberbullying", "stand-up-to-cyberbullying"), (15, "How Online Meanness Escalates", "how-online-meanness-escalates"), (16, "M.E.N.D.ing Friendships", "mending-friendships")],
 ],
 "7": [
  [(1, "Tech & Values", "tech-values"), (7, "What Are Thinking Traps?", "what-are-thinking-traps"), (10, "What Are Design Tricks?", "what-are-design-tricks")],
  [(6, "Parasocial Relationships", "parasocial-relationships"), (8, "Friendships & Boundaries", "friendships-boundaries"), (12, "Boundaries & Consent", "boundaries-consent")],
  [(3, "Care to Share?", "care-to-share"), (11, "Permission to Post", "permission-to-post"), (16, "The Assumptions We Make", "the-assumptions-we-make")],
  [(4, "Data for Sale", "data-for-sale"), (5, "Your Data, Your Choices", "your-data-your-choices"), (18, "Location Sharing & Your Privacy", "location-sharing-your-privacy")],
  [(2, "Choosing Sources", "choosing-sources"), (13, "Evaluating Information Online", "evaluating-information-online"), (14, "Bursting the Filter Bubble", "bursting-the-filter-bubble")],
  [(9, "The Ripple Effects of Conflict", "the-ripple-effects-of-conflict"), (15, "Being an Upstander", "being-an-upstander"), (17, "How to Re-A.C.T. to Cyberbullying", "how-to-re-act-to-cyberbullying")],
 ],
}
# Block 6: one entry per coding day (16), as (lesson numbers, title)
CODE = {
 "4": (CE, "Code.org Course E", [
  ([3], "Swimming Fish with Sprite Lab"), ([4], "Hello World"), ([5], "Mini-Project: Career Journeys"), ([6], "Game Design"),
  ([7], "Variables as Score"), ([8], "Environment and Players"), ([9], "Game Jam Day 1: Create"), ([10], "Game Jam Day 2: Play"),
  ([11], "Songwriting (unplugged)"), ([12], "Functions in Music Lab"), ([13], "Functions in Minecraft"), ([14], "Functions with Artist"),
  ([15], "Conditionals in Minecraft: Voyage Aquatic"), ([16], "Conditionals with the Farmer"), ([19], "End of Course Project (day 1: plan and build)"), ([19], "End of Course Project (day 2: finish and share)"),
 ]),
 "7": (GL, "Code.org CS Discoveries: Interactive Animations and Games", [
  ([1, 2], "Programming for a Purpose; Plotting Shapes"), ([3], "Drawing in Game Lab"), ([4], "Shapes and Parameters"), ([5], "Variables"),
  ([6], "Random Numbers"), ([7], "Mini-Project: Robot Faces"), ([8], "Sprites"), ([9], "Sprite Properties"),
  ([10], "Text"), ([11], "Mini-Project: Captioned Scenes"), ([12], "The Draw Loop"), ([13], "Sprite Movement"),
  ([14], "Mini-Project: Animation"), ([15], "Conditionals"), ([16, 17], "Keyboard Input; Mouse Input"), ([18], "Project: Interactive Card (start; finish in the continuation weeks)"),
 ]),
}

REV = dict(reviewed="2026-10-23", review="Lesson list read on the publisher site 2026-10-23", teacher_only=False)
MARK = "[cs-free-v1]"

daily, keys, pr = load("daily-packets.json"), load("daily-practice-keys.json"), load("planner-resources.json")
R = pr["resources"]
R["typingclub"] = dict(title="TypingClub (free typing lessons)", url=TYPING, provider="TypingClub", kind="Interactive practice", access="Free; optional free account saves progress", note="10 minutes a day; accuracy before speed.", **REV)
for g in "47":
    R[f"cs-dlwb-{g}"] = dict(title=f"Common Sense Digital Literacy & Well-Being - Grade {g} lessons", url=f"https://www.commonsense.org/education/digital-literacy", provider="Common Sense Education", kind="Lesson collection", access="Free (20-minute lessons; free account for slides)", note="", **REV)
    for week in DL[g]:
        for n, title, slug in week:
            R[f"cs-dl{g}-{n:02d}"] = dict(title=f"Common Sense Grade {g}, Lesson {n}: {title}", url=CS + slug, provider="Common Sense Education", kind="Lesson (20 min)", access="Free", note="", **REV)
    base, course, plan = CODE[g]
    R[f"cs-code-{g}"] = dict(title=course, url=base.rsplit("/lessons/", 1)[0], provider="Code.org", kind="Online course", access="Free; parent can create a free teacher account to track progress", note="", **REV)
    for nums, title in plan:
        for n in nums:
            R.setdefault(f"cs-code{g}-{n:02d}", dict(title=f"{course}, Lesson {n}", url=f"{base}{n}", provider="Code.org", kind="Online lesson", access="Free", note="", **REV))
if "7" in CODE:  # chapter 2 for Lillie's continuation weeks
    for n in range(19, 29):
        R.setdefault(f"cs-code7-{n:02d}", dict(title=f"Code.org CS Discoveries: Interactive Animations and Games, Lesson {n}", url=f"{GL}{n}", provider="Code.org", kind="Online lesson", access="Free", note="Chapter 2: Building Games (continuation weeks)", **REV))

# Collect block days per grade, in date order.
blocks = {}
for date in sorted(daily):
    for g, r in daily[date].items():
        e = r.get("elective") or {}
        if e.get("subject") == "computer" and e.get("block") in (2, 6) and "computer" in (r.get("subjects") or []):
            blocks.setdefault((g, e["block"]), []).append((date, r))
for g in "47":
    assert len(blocks[(g, 2)]) == 24 and len(blocks[(g, 6)]) == 16, "expected 24 + 16 computer days"

def wkday(date):
    import datetime
    return datetime.date.fromisoformat(date).isoweekday()  # Mon=1

day_plan = {}  # (g, date) -> dict(task, practice_title, items)
changed_weeks = 0
for g in "47":
    # Block 2
    by_week = {}
    for date, r in blocks[(g, 2)]:
        by_week.setdefault(r["elective"]["week"], []).append((date, r))
    for w, days in sorted(by_week.items()):
        key = f"{g}-{days[0][1]['module']}-{days[0][1]['week']}"
        s = pr["weeks"][key]["computer"]
        if s.get("cs_free") == MARK:
            continue
        lessons = DL[g][w - 1]
        s["resources"] = list(dict.fromkeys(s.get("resources", []) + ["typingclub", f"cs-dlwb-{g}"]))
        s["readings"] = s.get("readings", []) + [dict(resource_id="typingclub", online=True, section="TypingClub warm-up (10 minutes)", weekdays=[1, 2, 3, 4], note="Start where you left off; aim for accuracy, not speed.")]
        for (n, title, slug), wd in zip(lessons, (2, 3, 4)):
            s["readings"].append(dict(resource_id=f"cs-dl{g}-{n:02d}", online=True, section=f"Common Sense Lesson {n}: {title} (20 minutes)", weekdays=[wd], note="Watch or read the lesson together, do the activity, then discuss the questions."))
        s["cs_free"] = MARK
        changed_weeks += 1
        topic = s["topic"]
        for date, r in days:
            d = wkday(date)
            if d == 1:
                task = f"CS: {topic} - Read the booklet chapter with your parent and try the activity. Then TypingClub for 10 minutes."
                q = [f"What is one important idea from today's chapter about {topic.lower()}? Give an example.", "Record your TypingClub accuracy today. What will you practice next time?"]
            else:
                n, title, slug = lessons[d - 2]
                task = f"CS: {topic} - TypingClub 10 minutes, then Common Sense Lesson {n}: {title} (about 20 minutes, link in Materials)."
                q = [f"After the lesson '{title}', write two things you learned.", "Describe one choice you will make online because of today's lesson."]
            day_plan[(g, date)] = (task, f"Computer Foundations & Digital Citizenship - {topic}", q)
    # Block 6
    base, course, plan = CODE[g]
    by_week = {}
    for i, (date, r) in enumerate(blocks[(g, 6)]):
        by_week.setdefault(f"{g}-{r['module']}-{r['week']}", []).append((i, date, r))
    for key, days in by_week.items():
        s = pr["weeks"][key]["computer"]
        if s.get("cs_free") == MARK:
            continue
        s["resources"] = list(dict.fromkeys(s.get("resources", []) + [f"cs-code-{g}"]))
        for i, date, r in days:
            nums, title = plan[i]
            for n in nums:
                s["readings"] = s.get("readings", []) + [dict(resource_id=f"cs-code{g}-{n:02d}", online=True, section=f"{course} Lesson {n}" + (f": {title}" if len(nums) == 1 else ""), weekdays=[wkday(date)], note=f"Today: {title}. Work through the puzzles in order; ask for help after two tries.")]
        if g == "7" and days[-1][0] == 15:  # last coding week: Chapter 2 ready for the continuation weeks
            s["resources"] += [f"cs-code7-{n:02d}" for n in range(19, 29)]
        s["cs_free"] = MARK
        changed_weeks += 1
        for i, date, r in days:
            nums, title = plan[i]
            label = " and ".join(str(n) for n in nums)
            task = f"CS: {course} Lesson{'s' if len(nums) > 1 else ''} {label} - {title}. Open the lesson link in Materials (about 45 minutes)."
            q = [f"What new coding idea did you use in '{title}'?", "Describe one bug you hit and how you fixed it (or what you will try next)."]
            day_plan[(g, date)] = (task, f"Coding & Game Design - {title}", q)

def apply(store, with_answers):
    n = 0
    for (g, date), (task, title, qs) in day_plan.items():
        r = store[date][g]
        if task in r.get("tasks", ""):
            continue
        r["tasks"] = re.sub(r"CS: .*?(?= (?:Math|ELA|Sci|SS|Art|Life|Skills|Sp|Friday):|$)", lambda m: task, r["tasks"], count=1)
        items = [dict(prompt=qs[0], lines=4, points=2), dict(prompt=qs[1], lines=4, points=2)]
        if with_answers:
            items[0]["answer"] = "Look for an accurate idea from today's lesson and a specific example."
            items[1]["answer"] = "Accept any thoughtful, specific answer; reward reflection and safe choices, not speed."
        r["practice"] = [dict(subject="computer", title=title, items=items) if p.get("subject") == "computer" or str(p.get("title", "")).startswith(("Computer", "Coding")) else p for p in r.get("practice", [])]
        n += 1
    return n

a, b = apply(daily, False), apply(keys, True)
planner = load("planner-data.json")
import datetime as _dt
for plan in planner.get("plans", []):
    g = str(plan.get("grade"))
    for w in plan.get("weeks", []):
        for i in range(len(w.get("days", []))):
            date = (_dt.date.fromisoformat(w["start"]) + _dt.timedelta(days=i)).isoformat()
            if (g, date) in day_plan and date in daily and g in daily[date]:
                w["days"][i] = daily[date][g]["tasks"]
save("planner-data.json", planner)
save("planner-resources.json", pr); save("daily-packets.json", daily); save("daily-practice-keys.json", keys)
print(f"{changed_weeks} weeks updated; {a} student days and {b} key days rewritten")
