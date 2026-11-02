# VenvLearning Tutor

A personal AI tutor for each child, running on the family computer and opened from the Home Assistant School tablet.

- **Knows the curriculum.** It looks up each child's daily schedule, due dates, Friday checks and tests, every textbook and workbook lesson (with answer keys, for checking work), the ELA Reader texts, and the reading list, straight from this repository's data.
- **Teaches at the child's level.** The 4th grader gets short, concrete, step-by-step help; the 7th grader gets more depth, academic vocabulary, and questions that make her do the thinking (`prompt.js`).
- **Hints only.** It never gives answers to assigned work or writes any part of an assignment, and it doesn't help with checks or tests. It explains, models a similar example, and checks the child's own answers.
- **Parents see everything.** Every conversation is saved, and the parent link shows the full history for both children.

The model is Claude Opus 5.5 (`claude-opus-5-5`) through the Anthropic API, with adaptive thinking at medium effort. If Anthropic's safety system declines a request, it's retried automatically on a recommended fallback model (`fallbacks: "default"`); if that also declines, the child gets a kind "ask your parent" redirect.

## Private data folder

Settings, access links, the API key, the knowledge files (which include answer keys), and all chat history live in
`C:\Users\<you>\VenvLearningTutor` (or `TUTOR_DATA_DIR`). **Never put them in this repository**: everything committed here is published to the website.

## Set up (once)

In a terminal, in this `tutor` folder:

```bash
npm install
```

```bash
npm run setup
```

Setup asks for the children's first names (use the same names as their Home Assistant tabs) and your Anthropic API key (create one at console.anthropic.com → API keys; it isn't shown as you type). It builds the knowledge files, then prints each child's link, your history link, and the path of a Home Assistant script.

## Start the tutor

```bash
npm start
```

The first time, Windows Firewall asks whether Node.js may accept connections. Allow it on **private networks** so the tablet can reach this computer. The tutor works only while this computer is on, awake, and running `npm start`.

## Add it to the School dashboard

Open Home Assistant on a computer as an admin, go to the School dashboard, open the browser console, and paste the contents of `add-tutor-to-home-assistant.js` from the data folder. It adds a "My Tutor" card to the top of each child's tab.

If Home Assistant is opened over `https://` (for example through Nabu Casa), the browser blocks the tutor's `http://` page inside it. In that case, open the tutor link directly on the tablet and add it to the home screen.

## After curriculum changes

When lessons, the Reader, or the schedule change (after `tools/integrate-textbooks.py` or a new textbook build), refresh what the tutor knows and restart it:

```bash
npm run knowledge
```

Schedules are read from the repository each time the tutor starts, so a restart picks them up.

## Tests

```bash
npm test
```

The tests run the real curriculum lookups and a full tutoring turn against a stand-in for Claude, so they need the knowledge files but no API key.

## Not included yet

- Assignments that a parent creates on the website (`/assignments`) live in the website's database, so the tutor doesn't see them yet. It sees everything in the textbook plan.
- The tutor reads text only. It can't see photos of work yet.
