"""Grade 4 ELA · Unit 9: Capstone — year in review, writing portfolio, revision, and presentation; Year-End Test.
Anchor reading: King Arthur and the Round Table Reader, Chapters 21–22 (and rereading) (Jun 21 – Jul 16, 2027)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule
from content.ela4.unit01 import S, MC, OR, SA, READER
from content.ela4.unit04 import TI


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


P_REVIEW_LIT = Passage("The Last Lantern", [
    "Every night for sixty years, Grandmother Rosa lit a lantern in her window. The village children believed it was magic. Some said it kept wolves away; others said it called home lost sailors.",
    "When Rosa grew too weak to climb the stairs, her grandson Mateo found her staring at the dark window. “Who will light it now?” she whispered.",
    "Mateo had always thought the lantern was silly. But that night, he climbed the stairs, struck a match, and lit the wick. The flame trembled, then glowed steady and gold.",
    "The next morning, a fisherman knocked at the door. “Last night the fog was so thick I lost my way,” he said. “Then I saw your light. I steered toward it and found the harbor.”",
    "Mateo looked at his grandmother. She smiled. “It was never magic,” she said. “It was just someone remembering to care.” From then on, Mateo lit the lantern every night.",
], source="An original story", genre="Realistic fiction")

P_REVIEW_INFO = Passage("Coral Reefs: Cities Under the Sea", [
    "<b>Tiny Builders</b>",
    "A coral reef may look like a colorful rock, but it is built by millions of tiny animals called <b>coral polyps</b>. Each polyp makes a hard shell of limestone around its soft body. Over thousands of years, these shells pile up to form reefs.",
    "<b>A Busy Neighborhood</b>",
    "Reefs cover less than one percent of the ocean floor, yet about one quarter of all ocean species live on or near them. Fish, sea turtles, octopuses, and sharks find food and shelter among the coral.",
    "<b>Reefs in Danger</b>",
    "When ocean water becomes too warm, corals push out the tiny algae that live inside them and give them color and food. The coral turns white, which is called <b>coral bleaching</b>. If the water stays warm too long, the coral can die.",
    "<b>Protecting Reefs</b>",
    "Scientists are growing young corals in underwater nurseries and replanting them on damaged reefs. Visitors can help by never touching or standing on coral and by using sunscreen that is safe for reefs.",
], source="An original informational text", genre="Informational text", numbered=False)

P_C25 = Passage("The Promise Tree", [
    "When Lily's family moved to the city, her grandfather gave her an acorn. “Plant this,” he said, “and when it grows, remember that you can grow anywhere.”",
    "The city apartment had no yard. Lily planted the acorn in a coffee can on the fire escape. For weeks, nothing happened. She almost threw it away.",
    "Then one spring morning, a tiny green shoot poked through the soil. Lily laughed out loud. She sent her grandfather a photo with three words: <i>I'm growing too.</i>",
], source="An original story", genre="Realistic fiction")

P_TEST_LIT = Passage("The Clockmaker's Apprentice", [
    "Old Master Brenner was the finest clockmaker in the city. His shop was crowded with clocks of every size: tall clocks in wooden cases, tiny clocks set in silver lockets, and one enormous clock in the window with a painted moon that rose and set each night.",
    "When eleven-year-old Hana became his apprentice, she was so eager that she worked too quickly. Gears slipped from her tweezers. Springs flew across the room. Once she even dropped a pocket watch into a bowl of soup.",
    "“Patience,” Master Brenner said, gently fishing the watch from the soup. “A clock cannot be rushed. Neither can a clockmaker.”",
    "Hana frowned. She wanted to build something wonderful, not sweep up springs. But she tried to slow down. She learned to breathe before she lifted a gear and to check each tiny screw twice.",
    "One winter night, the great clock in the window stopped. The moon froze halfway across its painted sky. Master Brenner was sick in bed, and the city's New Year celebration would begin at midnight, when everyone gathered to watch the moon clock strike twelve.",
    "Hana opened the clock's case. Inside were hundreds of gears. Her heart raced, but she remembered: <i>Patience.</i> Slowly, carefully, she found the problem, a single bent tooth on one small gear. She straightened it with her tweezers, held her breath, and gave the pendulum a gentle push.",
    "Tick. Tock. The painted moon began to move.",
    "At midnight, the great clock struck twelve as the crowd cheered. Master Brenner, wrapped in a blanket at his window, smiled. Hana was no longer just an apprentice. She was a clockmaker.",
], source="An original story", genre="Realistic fiction")

P_TEST_INFO = Passage("How Clocks Changed the World", [
    "<b>Before Clocks</b>",
    "For thousands of years, people told time by the sun. Sundials used a shadow to show the hour, but they did not work on cloudy days or at night. Water clocks and candles marked with lines helped, but none were very exact.",
    "<b>Gears and Pendulums</b>",
    "The first mechanical clocks appeared in Europe around 1300. They used gears and falling weights. In 1656, a Dutch scientist named Christiaan Huygens built a clock with a <b>pendulum</b>, a weight that swings back and forth at a steady rate. Pendulum clocks were far more accurate than earlier clocks.",
    "<b>Time for Everyone</b>",
    "Accurate clocks changed daily life. Factories could set work hours, and trains could run on schedules. In fact, train travel led many countries to create standard time zones in the 1880s so that schedules made sense from city to city.",
], source="An original informational text", genre="Informational text", numbered=False)

# ================================================================= Week 1 · Review vocabulary and comprehension (Chapter 21)
L1 = Lesson("9.1", "Vocabulary Review",
    "I can use word parts, context clues, and figurative language skills to understand words.", "L.4.4, L.4.5",
    [],
    "Which vocabulary strategy do you use most when you meet a new word?",
    [ReaderAssign(READER, "Chapter 21: The Last Battle and the Death of Arthur", "Watch for unfamiliar words and use a strategy for each one."),
     Figure(lambda t: table(t, [["Strategy (Unit)", "Ask yourself"], ["Word parts (1)", "Do I know a prefix, suffix, or root?"], ["Context clues (1)", "Is there a definition, synonym, antonym, or example nearby?"],
                                ["Figurative language (1)", "Is this a simile, metaphor, or idiom? What two things are compared?"], ["Allusions (4)", "Does this refer to a myth (Herculean, Achilles' heel)?"],
                                ["Reference tools (1, 8)", "Can I check a glossary or dictionary?"]], [1.7 * inch, 3.9 * inch], width=5.6 * inch)),
     P_REVIEW_LIT,
     Example("Use strategies", "What does “trembled” mean in paragraph 3?", ["Context: “then glowed steady.” Steady is an antonym clue.", "So trembled means shook or flickered."], "flickered, shook"),
     KeyIdea("Choose the strategy that fits: word parts, context, figurative meaning, allusion, or reference tools.")],
    [Problem("What does “It was just someone remembering to care” mean?", "The lantern's power was kindness, not magic."), Problem("Prefix and meaning in <i>unlit</i>", "un-: not lit"), Problem("Figurative or literal: “glowed steady and gold”?", "literal description")],
    [S("Warm-Up", [SA("Prefix meaning “again”", "re-"), SA("Suffix meaning “without”", "-less")], cols=2),
     S("Vocabulary in Context", [
         MC("In paragraph 1, the children “believed it was magic.” What does the word “believed” suggest?", ["They knew for certain.", "They thought so without proof.", "They were told the truth."], 1),
         OR("What does “steered” mean in paragraph 4? What clue helps?", "guided the boat; “toward it and found the harbor”", lines=2),
         OR("Write a word from the story with a prefix or suffix and explain its meaning.", "e.g. fisherman (-man: a person who fishes)", lines=2),
         OR("Use a strategy to define one hard word from Chapter 21. Name the strategy.", "Answers vary.", lines=2)], passage=P_REVIEW_LIT),
     S("Exit Ticket", [OR("Which vocabulary strategy will you use most next year? Why?", "Answers vary.", lines=2)])],
    te("Students review vocabulary strategies.", "Determine word meanings using strategies; understand figurative language.", "King Arthur Reader (Chapter 21), workbook Lesson 9.1",
       "Favorite strategy.", ["Read Chapter 21.", "Read “The Last Lantern.”"], ["Review the strategy chart."], "Your Turn 1–3.",
       ["Skipping words."], ["Strategy bookmark."], ["Teach a strategy to a younger child."]),
    summary="Use word parts, context, figurative meaning, allusions, and references.")

L2 = Lesson("9.2", "Comprehension Review: Literature",
    "I can determine theme, describe characters, and make inferences in a story.", "RL.4.1, RL.4.2, RL.4.3",
    [],
    "What lesson does “The Last Lantern” teach?",
    [Figure(lambda t: table(t, [["Skill", "Ask yourself"], ["Theme (Unit 2)", "What does the main character learn?"], ["Character (Units 2, 5)", "What do STEAL clues show? How does the character change?"],
                                ["Inference (Units 2–3)", "What clues + what I know lead to a conclusion?"], ["Plot (Unit 5)", "What is the climax? How is it resolved?"], ["Point of view (Units 3–5)", "Who is telling the story?"]],
                            [1.9 * inch, 3.7 * inch], width=5.6 * inch)),
     Example("Theme", "“The Last Lantern”", ["Mateo thinks the lantern is silly.", "Lighting it saves a fisherman.", "Rosa: it was about caring."], "Small acts of caring can make a big difference."),
     KeyIdea("Theme, character, inference, plot, point of view: support each with evidence.")],
    [Problem("How does Mateo change?", "from thinking the lantern is silly to lighting it every night"), Problem("What is the climax?", "Mateo lights the lantern / the fisherman reveals it saved him"), Problem("Point of view", "third person")],
    [S("Warm-Up", [SA("Theme is…", "the life lesson"), SA("STEAL stands for…", "Speech, Thoughts, Effect, Actions, Looks")], cols=2),
     S("Answer with Evidence", [OR("Why does Mateo light the lantern even though he thinks it's silly? Make an inference.", "He loves his grandmother and wants to keep her tradition / ease her worry.", lines=3),
                                OR("What is the theme? Support it with two details.", "Small acts of caring matter: Mateo lights the lamp; the fisherman finds the harbor; Rosa's words.", lines=4),
                                OR("Compare the theme with “The Lighthouse Keeper's Daughter” (Unit 2).", "Both show a light that saves sailors and someone choosing to care for others.", lines=3)], passage=P_REVIEW_LIT),
     S("Chapter 21", [OR("How does Arthur's story end? What theme does the ending suggest?", "Answers vary.", lines=3)])],
    te("Students review literary comprehension.", "Refer to details; determine theme; describe characters.", "Workbook Lesson 9.2",
       "Lantern lesson.", "Reread “The Last Lantern.”", ["Review the skills chart."], "Your Turn 1–3.",
       ["Answers without evidence."], ["ACE frame."], ["Write a theme statement for all of King Arthur."]),
    summary="Support theme, character, and inference answers with evidence.")

L3 = Lesson("9.3", "Comprehension Review: Informational Text",
    "I can find main ideas, explain text structures, and use text features and evidence.", "RI.4.1, RI.4.2, RI.4.5, RI.4.7",
    [],
    "What do you look at first when you read an article?",
    [P_REVIEW_INFO,
     Example("Main idea of the whole text", "“Coral Reefs: Cities Under the Sea”", ["Section ideas: polyps build reefs; reefs host many species; warm water causes bleaching; people help protect them."],
             "Coral reefs, built by tiny polyps, are home to many sea creatures but are in danger, so people are working to protect them."),
     KeyIdea("Preview features, find section and whole-text main ideas, identify the structure, and cite evidence.")],
    [Problem("What is coral bleaching?", "coral turning white when it pushes out algae because the water is too warm"), Problem("Structure of “Reefs in Danger”", "cause and effect"), Problem("Structure of “Protecting Reefs”", "problem and solution")],
    [S("Warm-Up", [SA("Text feature in this article", "headings, bold words"), SA("Cause-effect signal word", "when, because")], cols=2),
     S("Answer with Evidence", [OR("Why are reefs called “cities under the sea”? Use evidence.", "Many species live there: about one quarter of ocean species, like a crowded city.", lines=3),
                                OR("Explain the cause and effect of coral bleaching.", "Warm water causes corals to push out algae; they turn white and may die.", lines=3),
                                OR("What can visitors do to help? Paraphrase.", "Don't touch or stand on coral; use reef-safe sunscreen.", lines=2)], passage=P_REVIEW_INFO),
     S("Exit Ticket", [OR("What visual would help this article? Why?", "e.g. a diagram of a polyp; a photo of bleached vs healthy coral", lines=2)])],
    te("Students review informational comprehension.", "Determine main idea; describe structure; interpret visuals.", "Workbook Lesson 9.3",
       "First look.", "Read the coral article.", ["Model main idea from sections."], "Your Turn 1–3.",
       ["Choosing a detail as main idea."], ["Section chart."], ["Research a reef animal."]),
    summary="Features → section ideas → whole main idea → structure → evidence.")

L4 = Lesson("9.4", "Strategies for Reading Tests",
    "I can use smart strategies to answer reading questions.", "RL.4.1, RI.4.1",
    [("eliminate", "Cross out answers you know are wrong.")],
    "What do you do when a test question seems hard?",
    [Bullets(["<b>Preview</b> the questions, then read the passage.", "<b>Annotate</b> as you read.", "<b>Go back</b> to the text; don't answer from memory.", "<b>Eliminate</b> wrong choices, then choose the best one.",
              "For written answers, use <b>ACE</b>: Answer, Cite, Explain.", "<b>Check</b>: Did I answer every part of the question?"]),
     Example("Eliminate choices", "Why did the fisherman knock at the door? A) to buy fish B) to thank them for the light C) to complain about the fog D) to visit Rosa",
             ["A: not in the text.", "C: he mentions fog but isn't complaining.", "D: not why he came.", "B: he found the harbor because of the light."], "B"),
     KeyIdea("Preview, annotate, go back to the text, eliminate, use ACE, and check.")],
    [Problem("Should you answer from memory?", "No, go back to the text."), Problem("What does ACE stand for?", "Answer, Cite, Explain"), Problem("What do you do with obviously wrong choices?", "eliminate them")],
    [S("Warm-Up", [SA("First step", "preview the questions"), SA("Eliminate means…", "cross out wrong answers")], cols=2),
     S("Practice", [MC("In “Coral Reefs,” what do coral polyps build their shells from?", ["sand", "limestone", "algae", "wood"], 1),
                    MC("Which sentence best states the theme of “The Last Lantern”?", ["Lanterns are magic.", "Small acts of caring can make a big difference.", "Fog is dangerous.", "Grandmothers are old."], 1),
                    OR("Answer with ACE: How did Mateo's opinion of the lantern change?", "At first he thought it was silly; after the fisherman's story, he understood it helped people, so he lit it every night.", lines=4)]),
     S("Exit Ticket", [OR("Which test strategy will you use first next time?", "Answers vary.", lines=2)])],
    te("Students practice test strategies.", "Refer to details and examples when answering questions.", "Workbook Lesson 9.4",
       "Hard questions.", "Practice passage review.", ["Teach strategies; model elimination."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Choosing the first answer that looks right."], ["Strategy checklist."], ["Write test questions for a passage."]),
    summary="Preview, annotate, go back, eliminate, ACE, check.")

# ================================================================= Week 2 · Plan a portfolio (Chapter 22)
L5 = Lesson("9.5", "Building a Writing Portfolio",
    "I can select pieces that show my growth as a writer.", "W.4.10, W.4.5",
    [("portfolio", "A collection of your best work that shows growth over time.")],
    "If you could show next year's teacher three pieces of your writing, which would you choose?",
    [ReaderAssign(READER, "Chapter 22: The Death of Guenevere and of Sir Lancelot", "How does the book end? What happens to the Round Table?"),
     Text("A <b>portfolio</b> shows your growth. Choose pieces from different kinds of writing: narrative (Unit 1), responses (Units 2–3), comparison (Units 4–5), opinion and research (Unit 6), synthesis (Unit 7)."),
     Figure(lambda t: table(t, [["Portfolio piece", "Why I chose it"], ["1. A narrative", ""], ["2. An opinion or comparison essay", ""], ["3. A research report or synthesis essay", ""], ["4. My capstone piece (Week 3)", ""]],
                            [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     KeyIdea("Choose pieces that show different types of writing and your growth.")],
    [Problem("Name a narrative you wrote this year.", "e.g. the Unit 1 legend-style story"), Problem("Why include different types of writing?", "to show a range of skills"), Problem("What is a portfolio?", "a collection of best work that shows growth")],
    [S("Warm-Up", [SA("A portfolio shows…", "growth"), SA("Types of writing this year", "narrative, response, comparison, opinion, research, synthesis")], cols=2),
     S("Select Pieces", [OR(f"Piece {i}: title and why you chose it", "Answers vary.", lines=2) for i in (1, 2, 3)]),
     S("Chapter 22", [OR("How does the King Arthur Reader end? How did you feel about the ending?", "Answers vary.", lines=3)])],
    te("Students select portfolio pieces.", "Write routinely over extended time frames; strengthen writing.", "Student writing from the year, folder, workbook Lesson 9.5",
       "Three pieces.", "Read Chapter 22.", ["Explain portfolios."], "Sort writing from the year.",
       ["Choosing only the longest pieces."], ["Lay out pieces by unit."], ["Add art or photos."]),
    summary="Choose varied pieces that show growth.")

L6 = Lesson("9.6", "Writing a Reflection",
    "I can write a reflection about how I've grown as a reader and writer.", "W.4.10",
    [("reflection", "Writing that looks back and thinks about what you learned.")],
    "What is something that was hard for you in October that is easier now?",
    [Text("A reflection is honest and specific. Name what you learned, give an example from your work, and explain how you changed."),
     Example("Reflection paragraph", "Reflect on evidence.", ["What I learned: how to support answers with evidence.", "Example: my Unit 2 ACE paragraphs.", "How I changed: I used to write opinions only; now I quote the text."],
             "At the start of the year, I answered questions with just my opinion. In Unit 2, I learned ACE, and my paragraphs about the Round Table used real quotes. Now I always go back to the text to prove my answers."),
     KeyIdea("Be specific: what you learned, an example, and how you changed.")],
    [Problem("Name a skill you improved.", "Answers vary."), Problem("What makes a reflection specific?", "examples from your work"), Problem("Should a reflection be honest about challenges?", "Yes")],
    [S("Warm-Up", [SA("A reflection looks…", "back"), SA("A reflection should include an…", "example")], cols=2),
     S("Reflect", [OR("Write a reflection paragraph about how you grew as a reader.", "Answers vary.", lines=7), OR("Write a reflection paragraph about how you grew as a writer.", "Answers vary.", lines=7)])],
    te("Students write reflections.", "Write routinely for a range of purposes.", "Portfolio pieces, workbook Lesson 9.6",
       "Hard then, easier now.", "Reread early and recent work side by side.", ["Model a reflection."], "Write reflections.",
       ["Vague reflections (“I got better”)."], ["Sentence frames."], ["Write a letter to next year's self."]),
    summary="Reflections name learning, give examples, and explain growth.")

L7 = Lesson("9.7", "Setting Goals",
    "I can set reading and writing goals for next year.", "W.4.10, SL.4.1",
    [("goal", "Something you plan to achieve.")],
    "What do you want to get better at in fifth grade?",
    [Text("Good goals are <b>specific</b> and have a <b>plan</b>. Instead of “read more,” try “read two chapter books a month and keep a reading log.”"),
     Figure(lambda t: table(t, [["Vague goal", "Specific goal with a plan"], ["Write better.", "Use transitions in every paragraph; check with my revision checklist."], ["Read more.", "Read 20 minutes every night and log my books."],
                                ["Learn new words.", "Add three new words a week to a word journal."]], [2.0 * inch, 3.6 * inch], width=5.6 * inch)),
     KeyIdea("Make goals specific, with a plan to reach them.")],
    [Problem("Make specific: “Be a better speller.”", "e.g. Study my personal spelling list for 10 minutes three times a week."), Problem("What makes a goal specific?", "it says exactly what and how"), Problem("Why have a plan?", "so you know how to reach the goal")],
    [S("Warm-Up", [SA("A goal is…", "something you plan to achieve"), SA("Vague or specific: “Read more.”", "vague")], cols=2),
     S("My Goals", [OR("Reading goal and plan:", "Answers vary.", lines=3), OR("Writing goal and plan:", "Answers vary.", lines=3), OR("Portfolio table of contents (titles in order):", "Answers vary.", lines=4)])],
    te("Students set goals.", "Engage in discussion; reflect.", "Workbook Lesson 9.7",
       "Fifth-grade goals.", "Review reflections.", ["Model a specific goal."], "Write goals.",
       ["Vague goals."], ["Goal frame: I will ___ by ___."], ["Share goals with the family."]),
    summary="Specific goals with plans.")

L8 = Lesson("9.8", "Planning a Capstone Piece",
    "I can plan a new piece of writing that shows my best skills.", "W.4.1, W.4.2, W.4.3, W.4.4",
    [("capstone", "A final project that shows everything you've learned.")],
    "If you could write anything about the books and topics from this year, what would it be?",
    [Text("Choose one capstone option. Plan it with the organizer that fits."),
     Figure(lambda t: table(t, [["Option", "Prompt", "Organizer"], ["Narrative", "Write a new adventure about a character from King Arthur or Treasure Island.", "plot arc (Unit 5)"],
                                ["Opinion", "Who is the greatest hero from this year's reading? Convince your reader.", "opinion plan (Unit 6)"],
                                ["Informational", "Research and explain a topic from this year (knights, ships, navigation, reefs, bees).", "category notes (Unit 6)"]], [1.2 * inch, 3.1 * inch, 1.4 * inch], width=5.7 * inch, font_size=9)),
     KeyIdea("Choose the option that lets you show your best skills, and plan before drafting.")],
    [Problem("Organizer for a narrative", "plot arc"), Problem("Organizer for an opinion piece", "opinion plan: opinion, reasons, evidence"), Problem("What is a capstone?", "a final project showing what you learned")],
    [S("Warm-Up", [SA("Narrative organizer", "plot arc"), SA("Opinion parts", "opinion, reasons, evidence, conclusion")], cols=2),
     S("Plan", [OR("My capstone option and topic:", "Answers vary.", lines=2), Problem("My plan (use the matching organizer):", "Answers vary.", space=260, wide=True)])],
    te("Students plan capstone writing.", "Produce clear and coherent writing appropriate to task, purpose, and audience.", "Workbook Lesson 9.8",
       "Anything you'd write.", "Review organizers from past units.", ["Present the options."], "Choose and plan.",
       ["Choosing a topic that's too big."], ["Narrow with a focus question."], ["Write in two genres."], independent="Finish the plan. Weekly Check tomorrow."),
    summary="Choose an option and plan with the right organizer.")

# ================================================================= Week 3 · Revise and edit a selected piece (Treasure Island reread)
L9 = Lesson("9.9", "Drafting and Revising for Ideas and Organization",
    "I can draft my capstone and revise it for clear ideas and organization.", "W.4.5, W.4.4",
    [],
    "What is the difference between a first draft and a final draft?",
    [ReaderAssign(TI, "Reread Chapter 9: The Adventure Comes to an End", "Notice how Stevenson's story wraps up. Use it as a model for your ending."),
     Text("Draft quickly from your plan. Then revise: Is the main idea or opinion clear? Does each paragraph have one focus? Are events or reasons in the best order? Is the ending satisfying?"),
     KeyIdea("Draft from the plan; revise for focus, order, and a strong ending.")],
    [Problem("What should a first draft focus on?", "getting ideas down from the plan"), Problem("One question to ask when revising", "Is each paragraph focused?"), Problem("What makes an ending satisfying?", "It resolves the problem or restates the main idea with a final thought.")],
    [S("Warm-Up", [SA("Revise is about…", "ideas, organization, word choice"), SA("Edit is about…", "conventions")], cols=2),
     S("Draft", [OR("Draft your capstone piece.", "Answers vary.", lines=24)]),
     S("Revise", [OR("Two revisions for ideas or organization:", "Answers vary.", lines=3)])],
    te("Students draft and revise capstones.", "Develop and strengthen writing by revising.", "Treasure Island Reader (Chapter 9 reread), plans, workbook Lesson 9.9",
       "First vs final.", "Reread the end of Treasure Island.", ["Model a revision."], "Draft.",
       ["Skipping revision."], ["Revise one paragraph at a time."], ["Add a scene or a third reason."]),
    summary="Draft from the plan; revise for focus, order, and ending.")

L10 = Lesson("9.10", "Revising for Word Choice and Sentence Variety",
    "I can revise for precise words and varied sentences.", "L.4.3a, W.4.5",
    [("sentence variety", "Using sentences of different lengths and beginnings.")],
    "What happens when every sentence starts the same way?",
    [Example("Combine and vary", "The ship sailed. The ship was fast. The ship reached the island.", ["Combine: The fast ship sailed to the island.", "Vary beginnings: At dawn, the fast ship reached the island."],
             "At dawn, the fast ship skimmed across the waves and reached the island."),
     Bullets(["Replace tired words (went, said, good, nice) with precise words (Unit 1).", "Combine short choppy sentences with and, but, so, who, which (Unit 8).", "Start some sentences with a prepositional phrase or transition."]),
     KeyIdea("Precise words and varied sentences make writing flow.")],
    [Problem("Combine: Ada was brave. Ada was quick.", "Ada was brave and quick."), Problem("Vary the start: We sailed at dawn.", "At dawn, we sailed."), Problem("Precise word for said (whispered)", "whispered, murmured")],
    [S("Warm-Up", [SA("A tired word", "went, said, nice, good"), SA("A combining word", "and, but, so, who")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Combine: Pip found a key. The key was brass.", "Pip found a brass key."), ("Combine: Jim hid. He heard Silver's plan.", "Jim hid, and he heard Silver's plan."),
                                          ("Vary: The storm ended after midnight.", "After midnight, the storm ended.")]], cols=1),
     S("Revise Your Capstone", [OR("Copy two sentences before and after revising for word choice or variety.", "Answers vary.", lines=4)])],
    te("Students revise for word choice and fluency.", "Choose words precisely; vary sentences.", "Workbook Lesson 9.10",
       "Same-start sentences.", "Read a choppy paragraph aloud.", ["Model combining and varying."], "Practice.",
       ["Making every sentence long."], ["Read aloud for rhythm."], ["Revise an old piece too."]),
    summary="Precise words and varied sentences.")

L11 = Lesson("9.11", "Editing with a Checklist",
    "I can edit my capstone for conventions using a checklist.", "L.4.1, L.4.2, W.4.5",
    [],
    "Which grammar rule from Unit 8 do you most need to check?",
    [Figure(lambda t: table(t, [["Editing checklist (four passes)", "✓"], ["Capitals: sentence starts, I, names, places, titles", ""], ["Punctuation: end marks, commas (lists, compound sentences, after introductions), dialogue", ""],
                                ["Grammar: agreement, tense, complete sentences", ""], ["Spelling and confused words: their/there/they're, its/it's, your/you're, to/too/two", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Four passes: capitals, punctuation, grammar, spelling.")],
    [Problem("Second pass checks…", "punctuation"), Problem("Fix: its time to go", "It's time to go."), Problem("Fix: the knights rides home", "The knights ride home.")],
    [S("Warm-Up", [SA("Fix: i", "I"), SA("Fix: there going", "they're going")], cols=2),
     S("Edit Your Capstone", [OR("List the mistakes you fixed in each pass.", "Answers vary.", lines=6)])],
    te("Students edit capstones.", "Demonstrate command of conventions.", "Workbook Lesson 9.11",
       "Most-needed rule.", "Review Unit 8 rules.", ["Model a four-pass edit."], "Edit.",
       ["Rushing one pass."], ["Colored pencils per pass."], ["Edit a family member's email (with permission)."]),
    summary="Edit in four passes.")

L12 = Lesson("9.12", "Publishing",
    "I can publish a polished final copy of my capstone.", "W.4.6",
    [("publish", "Prepare a final copy to share with readers.")],
    "How can the way a piece looks help readers enjoy it?",
    [Bullets(["Type or neatly copy the final version.", "Add a title page with your name and date.", "Add an illustration, map, diagram, or chart if it helps.", "Include a source list for informational pieces.", "Add the piece to your portfolio."]),
     KeyIdea("A polished, well-designed final copy shows respect for your readers.")],
    [Problem("What goes on a title page?", "title, name, date"), Problem("When do you need a source list?", "for informational/research pieces"), Problem("Name a visual you might add.", "illustration, map, diagram, chart")],
    [S("Warm-Up", [SA("Publish means…", "prepare a final copy to share"), SA("Where does the final copy go?", "the portfolio")], cols=2),
     S("Publish", [OR("Publish your capstone. Write its title and describe one design choice you made.", "Answers vary.", lines=3)])],
    te("Students publish capstones.", "Use technology to produce and publish writing.", "Computer (optional), paper, art supplies, workbook Lesson 9.12",
       "Looks matter?", "Show sample published pages.", ["Model a title page."], "Publish.",
       ["Rushing the final copy."], ["Typing help as needed."], ["Bind the portfolio."], independent="Publish. Weekly Check tomorrow."),
    summary="Publish a polished final copy for the portfolio.")

# ================================================================= Week 4 · Present learning with source evidence (Chapters 1 and 22 reread)
L13 = Lesson("9.13", "Planning a Presentation with Evidence",
    "I can plan a presentation that uses evidence from texts.", "SL.4.4, RL.4.2",
    [],
    "How did King Arthur's story change from Chapter 1 to Chapter 22?",
    [ReaderAssign(READER, "Reread Chapters 1 and 22", "Compare the beginning and the end. What changed? What stayed the same?"),
     Text("Your presentation shares your capstone OR answers: <i>How did Arthur's story come full circle?</i> Use at least two pieces of text evidence."),
     Figure(lambda t: table(t, [["Part", "What to say"], ["Hook", "a question, quote, or surprising fact"], ["Main point 1", "with text evidence"], ["Main point 2", "with text evidence"], ["Conclusion", "what you want listeners to remember"]],
                            [1.4 * inch, 4.0 * inch], width=5.4 * inch)),
     KeyIdea("Hook, main points with evidence, conclusion.")],
    [Problem("How long should a presentation be?", "about 2–3 minutes"), Problem("How many pieces of evidence?", "at least two"), Problem("Name a hook type.", "question, quote, surprising fact")],
    [S("Warm-Up", [SA("A hook grabs…", "attention"), SA("Evidence comes from…", "the text")], cols=2),
     S("Plan", [OR("Hook:", "Answers vary.", lines=1), OR("Main point 1 + evidence:", "Answers vary.", lines=3), OR("Main point 2 + evidence:", "Answers vary.", lines=3), OR("Conclusion:", "Answers vary.", lines=2)])],
    te("Students plan presentations.", "Report on a topic or text with appropriate facts and relevant details.", "King Arthur Reader (Chapters 1 and 22), workbook Lesson 9.13",
       "Full circle?", "Reread Chapters 1 and 22.", ["Model a plan."], "Plan.",
       ["Reading the plan word for word later."], ["Key-word note cards."], ["Add a visual."]),
    summary="Plan a hook, evidence-based points, and a conclusion.")

L14 = Lesson("9.14", "Visuals and Speaking Skills",
    "I can use a visual and speak clearly to an audience.", "SL.4.4, SL.4.5",
    [],
    "What makes a speaker easy to listen to?",
    [Bullets(["Look at your audience.", "Speak loudly and clearly at a steady pace.", "Use note cards with key words, not full sentences.", "Point to your visual when you talk about it.", "Stand still and use natural gestures."]),
     Text("Create a visual: a poster, a slide, a map, a timeline, or a drawing. Keep text short and pictures large."),
     KeyIdea("Eye contact, clear voice, steady pace, and a simple visual.")],
    [Problem("Name two speaking skills.", "eye contact, clear voice"), Problem("Should note cards have full sentences?", "No, key words"), Problem("What makes a good visual?", "short text, large pictures")],
    [S("Warm-Up", [SA("Speak at a ___ pace.", "steady"), SA("Look at your…", "audience")], cols=2),
     S("Create", [Problem("Sketch your visual here first.", "Answers vary.", space=220, wide=True), OR("Write your note cards (key words only):", "Answers vary.", lines=5)])],
    te("Students prepare visuals and practice speaking.", "Add audio recordings and visual displays to presentations; speak clearly.", "Poster board or slides, workbook Lesson 9.14",
       "Easy-to-hear speakers.", "Watch a short speech together (optional).", ["Model good and poor speaking."], "Create visuals.",
       ["Reading from the poster."], ["Practice with a timer."], ["Record a practice video."]),
    summary="Clear speaking plus a simple visual.")

L15 = Lesson("9.15", "Practicing and Listening",
    "I can practice my presentation and listen to identify a speaker's reasons and evidence.", "SL.4.3, SL.4.1",
    [],
    "What should a good listener do during a presentation?",
    [Text("Practice twice: once alone, once for a listener. As a listener, identify the speaker's main points and evidence, then give kind, specific feedback and ask a question."),
     Figure(lambda t: table(t, [["Listener notes"], ["Speaker's main point:"], ["Evidence they used:"], ["One thing they did well:"], ["One question I have:"]], [5.0 * inch], width=5.0 * inch)),
     KeyIdea("Practice with feedback; listen for main points and evidence.")],
    [Problem("What should a listener identify?", "main points and evidence"), Problem("How many times should you practice?", "at least twice"), Problem("Feedback should be…", "kind and specific")],
    [S("Warm-Up", [SA("Good listeners…", "look, listen, take notes, ask questions"), SA("Feedback should be…", "kind and specific")], cols=2),
     S("Practice", [OR("Feedback I received:", "Answers vary.", lines=3), OR("Change I'll make:", "Answers vary.", lines=2)]),
     S("Listen", [OR("Listener notes for someone else's practice talk:", "Answers vary.", lines=5)])],
    te("Students practice and listen actively.", "Identify the reasons and evidence a speaker provides; engage in discussions.", "Workbook Lesson 9.15, Year-End Review",
       "Good listeners.", "Practice talks.", ["Model listener notes."], "Practice in pairs.",
       ["Interrupting speakers."], ["Listener notes frame."], ["Coach a sibling's talk."], independent="Practice; begin the Year-End Review."),
    summary="Practice with feedback; listen for points and evidence.")

L16 = Lesson("9.16", "Presentation Day and Celebration",
    "I can present my learning and reflect on my year.", "SL.4.4, W.4.10",
    [],
    "What are you proudest of from fourth grade?",
    [Text("Present your capstone or full-circle talk to your family. Afterward, share your portfolio and celebrate a year of reading and writing!"),
     KeyIdea("You read legends, adventures, myths, and articles; you wrote stories, essays, reports, and reflections. Celebrate how much you've grown!")],
    [Problem("Name your favorite book or story from this year.", "Answers vary."), Problem("Name your favorite piece of your own writing.", "Answers vary."), Problem("Name one skill you'll use in fifth grade.", "Answers vary.")],
    [S("After Presenting", [OR("How did your presentation go? What would you do differently?", "Answers vary.", lines=3), OR("Write a short note to yourself to read on the first day of fifth grade.", "Answers vary.", lines=5)])],
    te("Students present and celebrate.", "Report on a topic; reflect on growth.", "Presentations, portfolios, workbook Lesson 9.16",
       "Proudest moment.", "Gather the family audience.", ["Presentations."], "Share portfolios.",
       ["Nerves; remind of practice."], ["Allow note cards."], ["Present to grandparents by video."], independent="Presentations and celebration.", exit_="Tomorrow: Year-End Test."),
    summary="Present, share the portfolio, and celebrate.")

# ================================================================= checks
C1 = Check("Weekly Check 25: Reading Review", [S("Read and answer", [
    OR("What did Grandfather mean by “you can grow anywhere”?", "Lily can be happy and thrive even in a new place.", lines=2),
    OR("How does Lily feel when nothing grows? Clue?", "discouraged; she almost threw it away", lines=2),
    OR("What is the theme? Use two details.", "Patience helps you grow in new places: the acorn grows in a coffee can; Lily writes “I'm growing too.”", lines=3),
    MC("“I'm growing too” is…", ["literal only", "a comparison between the tree and Lily", "a simile using like"], 1),
    OR("Point of view?", "third person", lines=1)], passage=P_C25)], minutes=20)
C2 = Check("Weekly Check 26: Portfolio and Goals", [S("Show what you know", [
    SA("A portfolio shows…", "growth over time"), SA("A reflection includes…", "what I learned, an example, how I changed"), SA("Make specific: “Write more.”", "e.g. Write in a journal 10 minutes every day."),
    SA("Organizer for a narrative", "plot arc"), SA("Organizer for opinion", "opinion, reasons, evidence"), SA("What is a capstone?", "a final project showing what you learned")], cols=1)], minutes=15)
C3 = Check("Weekly Check 27: Revising and Editing", [S("Show what you know", [
    SA("Combine: The dog barked. The dog was small.", "The small dog barked."), SA("Vary: We left after lunch.", "After lunch, we left."),
    SA("Edit: jim and i found there map", "Jim and I found their map."), SA("Edit: whats in the chest asked ben", "“What's in the chest?” asked Ben."),
    SA("Precise word for went (slowly)", "trudged, strolled, wandered"), SA("Edit: The pirates was hungry they ate", "The pirates were hungry, so they ate.")], cols=1)], minutes=15)

REVIEW = Check("Year-End Review", [
    S("Vocabulary and grammar", [SA("<i>misplace</i> means…", "put in the wrong place"), SA("Achilles' heel means…", "a weak spot"), SA("Plural of <i>wolf</i>", "wolves"),
                                 SA("Past of <i>bring</i>", "brought"), SA("Fix: its raining", "It's raining."), SA("Possessive: toys of the children", "the children's toys")], cols=2),
    S("Reading", [OR("Name three text structures and their signal words.", "chronological (first, then), compare/contrast (both, however), cause/effect (because, as a result), problem/solution", lines=3),
                  OR("Explain the difference between theme and main idea.", "Theme is a story's life lesson; main idea is an informational text's most important point.", lines=2),
                  OR("Explain the difference between primary and secondary sources.", "Primary: from the time by someone there; secondary: written later to explain.", lines=2)]),
    S("Writing", [OR("List the parts of an ACE response and an opinion essay.", "ACE: Answer, Cite, Explain. Opinion: introduction with opinion, reasons with evidence, linking words, conclusion.", lines=3)])],
    kind="review", minutes=50, teacher_note="Spread over the week as homework or use as a study session before the Year-End Test.")

TEST = Check("Grade 4 ELA Year-End Test", [
    S("Part A · Literature (1 point each)", [
        OR("Describe the setting in paragraph 1. Use two details.", "a clock shop crowded with clocks: tall clocks, tiny locket clocks, a huge window clock with a painted moon", lines=2),
        OR("What problem does Hana have at the beginning? Give evidence.", "She works too quickly and makes mistakes: gears slip, springs fly, watch in the soup.", lines=2),
        OR("What does Master Brenner mean by “A clock cannot be rushed. Neither can a clockmaker”?", "Good work and learning take patience.", lines=2),
        OR("What is the climax of the story?", "Hana fixes the great clock before midnight.", lines=1),
        OR("How does Hana change? Use evidence from the beginning and the end.", "From rushing and careless to patient and skilled: dropped a watch in soup; carefully finds and fixes the bent tooth.", lines=3, points=2),
        OR("State the theme.", "Patience leads to success / skill grows with patience.", lines=1),
        MC("“The moon froze halfway across its painted sky” means…", ["the moon turned to ice", "the painted moon stopped moving", "it was cold outside"], 1)], passage=P_TEST_LIT),
    S("Part B · Informational text (1 point each)", [
        OR("List two problems with telling time before mechanical clocks.", "Sundials didn't work on cloudy days or at night; water clocks and candles weren't exact.", lines=2),
        OR("What is a pendulum, and why did it matter?", "a weight that swings at a steady rate; it made clocks far more accurate", lines=2),
        MC("Which structure does the section “Time for Everyone” mostly use?", ["cause and effect", "compare and contrast", "problem and solution"], 0),
        OR("What is the main idea of the whole text?", "Clocks became more accurate over time and changed how people lived and worked.", lines=2)], passage=P_TEST_INFO),
    S("Part C · Connect the texts (1 point each)", [
        OR("What kind of clock does Hana fix? Use Text B to explain how it works.", "a pendulum clock; the pendulum swings at a steady rate to keep accurate time", lines=2),
        OR("Why might a whole city care so much about one clock (Text A)? Use Text B for support.", "Accurate clocks organized daily life and schedules; the city depended on its clock for events like New Year.", lines=2)]),
    S("Part D · Language (1 point each)", [
        SA("<i>enormous</i> (paragraph 1) means…", "very big"), SA("Plural of <i>watch</i>", "watches"), SA("Edit: hana said im ready", "Hana said, “I'm ready.”"), SA("Combine: Hana was careful. Hana was brave.", "Hana was careful and brave.")], cols=1),
    S("Part E · Writing (6 points)", [OR("Opinion: Is patience the most important quality for an apprentice? Write a paragraph with a clear opinion, two reasons with evidence from the texts, linking words, and a conclusion.",
                                         "Rubric: opinion (1); reason 1 with evidence (1); reason 2 with evidence (1); explanation (1); linking words (1); conclusion and conventions (1).", lines=16, points=6)])],
    kind="test", minutes=60, rubric=[["21–24 (85%+)", "Mastered: ready for Grade 5 ELA."], ["17–20", "Proficient: review missed skills over the summer."], ["Below 17", "Review missed parts, then retest those parts."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-06-21", "2027-06-28", "2027-07-05", "2027-07-12"], CHECKS, REVIEW, TEST)

UNIT = Unit(9, "Capstone", "Year in review, a writing portfolio, a capstone piece, and a presentation, with King Arthur Chapters 21–22.",
    "The legend of King Arthur comes to its end, and so does your fourth-grade year. You'll review the reading and language skills you've mastered, build a portfolio of your best writing, write and polish a capstone piece, and present your learning to an audience.",
    ["Review vocabulary, literary, and informational reading skills.", "Select portfolio pieces, reflect on growth, and set goals.", "Draft, revise, edit, and publish a capstone piece.", "Plan and deliver a presentation with evidence and a visual."],
    [("RL.4.1–3, RI.4.1–7", "Review comprehension standards."), ("L.4.1–5", "Review language standards."), ("W.4.4–6, W.4.10", "Produce, revise, and publish writing; write routinely."),
     ("SL.4.1, SL.4.3–5", "Discuss, listen for reasons and evidence, and present.")],
    [("portfolio", "A collection showing growth."), ("reflection", "Writing that looks back on learning."), ("capstone", "A final project."), ("goal", "Something you plan to achieve.")],
    ["All Grade 4 ELA units."], ["King Arthur and the Round Table Reader (Chapters 1, 21–22)", "Treasure Island Reader (Chapter 9)", "A folder for the portfolio; poster board or slides"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Portfolios, reflections, and presentations are how artists, scientists, and professionals share their best work.",
    family_note="Plan a family “author's celebration” for presentation day. Invite grandparents in person or by video.",
    weeks=WEEKS)
