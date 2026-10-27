"""Grade 7 ELA · Unit 8: Conventions and Word Choice — commas, semicolons, colons, dashes, quotation and title punctuation, editing in context, roots and confusing words, spelling, and precise style.
Anchor reading: The Time Machine Reader, Chapters 13–15 and Epilogue (May 24 – Jun 18, 2027)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule
from content.ela7.unit05 import TM


def rules(rows, widths, fs=9.5):
    return Figure(lambda t: table(t, rows, [w * inch for w in widths], width=sum(widths) * inch, font_size=fs))


P_EDIT = Passage("Edit Me: The Return", [
    "on a cold evening in march the time traveller limped into his dining room his guests stared at him his coat was torn and dusty and his face was pale",
    "“what happened to you” asked the editor. the traveller didnt answer right away, he poured himself a glass of water drank it slowly and then he said “ill tell you everything but first i must eat”",
], source="A passage with errors for editing", genre="Editing passage")

P_SKEPTIC = Passage("Evidence and Belief", [
    "When the Time Traveller finishes his story, most of his guests do not believe him. The Medical Man examines the strange white flowers the Traveller brought back and admits he cannot identify them, yet he still doubts the tale. The Editor jokes that it is a pity the Traveller is not a writer of stories.",
    "Their reaction raises an old question: what kind of evidence is enough to believe something extraordinary? Many scientists follow a principle often summed up as “extraordinary claims require extraordinary evidence.” Two unusual flowers and a battered machine are intriguing, but they are not proof.",
    "Yet the narrator is not so sure. He returns the next day and sees the Traveller preparing to leave again, carrying a small camera and a knapsack, perhaps to bring back the proof his friends demanded.",
], source="An original informational commentary", genre="Informational text")

P_C22 = Passage("Expedition Notes", [
    "On Tuesday, June 3, 2025, our team left base camp in Anchorage, Alaska. We carried three things: food, fuel, and a satellite phone. The weather, however, had other plans; by noon, snow was falling heavily.",
    "Our guide, a quiet woman named Ruth, warned us — calmly but firmly — that we should turn back. We did.",
], source="An original passage", genre="Informational text")

P_C23 = Passage("Edit Me: The Science Fair", [
    "Maya's project which was about solar ovens won first place. Her teacher said “this is the best project I've seen in years.” Maya was proud, she thanked her teacher and called her parents.",
], source="A passage with errors", genre="Editing passage", numbered=False)

P_TEST = Passage("Edit and Analyze: Letter to the Future", [
    "dear reader in the year 2125",
    "i am writing this letter in june 2027 and i wonder what your world is like. do you still read books or do stories appear in the air around you. does anyone still remember the time machine by h g wells",
    "my grandmother who was born in 1955 told me that when she was young computers filled whole rooms. now i carry one in my pocket that is more powerful then all of them combined. i cant imagine what you carry.",
    "please take care of the earth its the only one we have",
], source="An original letter with errors for editing", genre="Editing passage")

# ================================================================= Week 1 · Punctuation and capitalization (Chapter 13)
L1 = Lesson("8.1", "The Climax: The Trap of the White Sphinx",
    "I can analyze how an author builds and resolves a climax.", "RL.7.3, RL.7.5",
    [("climax", "The point of greatest tension in a story."), ("resolution", "How the central conflict is resolved.")],
    "Why might the open doors of the sphinx be a bad sign?",
    [ReaderAssign(TM, "Chapter 13: The Trap of the White Sphinx", "Why are the sphinx's doors open? How does the Traveller escape?"),
     Text("The climax brings the central conflict, the Traveller vs the Morlocks and his struggle to recover the machine, to its highest point. Wells uses darkness, confinement, and physical struggle to make it intense."),
     Example("Analyze the climax", "Chapter 13", ["Setup: the doors are open; the machine is inside.", "Twist: it's a trap; the doors close.", "Struggle: in darkness, with no matches that will light, he fights off the Morlocks.", "Resolution: he escapes on the machine."],
             "Wells builds tension through false hope, darkness, and close combat, then resolves it with a narrow escape."),
     KeyIdea("Analyze how setup, twist, and struggle build to a climax, and how it is resolved.")],
    [Problem("Why are the doors open?", "The Morlocks set a trap."), Problem("Why can't he light his matches?", "They are the kind that strike only on the box, and he has lost the box. (accept: they won't light)"), Problem("How is the conflict resolved?", "He escapes on the machine.")],
    [S("Warm-Up", [SA("Climax =", "point of greatest tension"), SA("Resolution =", "how the conflict is resolved")], cols=2),
     S("Analyze", [OR("List three details Wells uses to build tension in Chapter 13. Explain one.", "Answers vary.", lines=4), OR("How does the escape resolve the central conflict? What does the Traveller lose?", "He regains the machine and escapes the Morlocks, but he has lost Weena.", lines=3)]),
     S("Exit Ticket", [OR("Was the ending of the conflict satisfying? Why?", "Answers vary.", lines=2)])],
    te("Students analyze climax and resolution.", "Analyze how elements interact; how structure contributes to meaning.", "The Time Machine Reader (Chapter 13), workbook Lesson 8.1",
       "Open doors.", "Read Chapter 13.", ["Model the analysis."], "Your Turn 1–3.",
       ["Confusing climax with any exciting event."], ["Plot-arc placement."], ["Rewrite the escape from a Morlock's point of view."]),
    summary="Setup, twist, and struggle build the climax; the escape resolves it.")

L2 = Lesson("8.2", "Comma Rules",
    "I can use commas correctly in all common situations.", "L.7.2a, L.7.2",
    [],
    "Read aloud: “Let's eat Grandma!” vs “Let's eat, Grandma!” Why does the comma matter?",
    [rules([["Rule", "Example"], ["introductory words, phrases, clauses", "However, the machine was gone. / When night fell, the Morlocks came."], ["series of three or more", "He carried matches, camphor, and a lever."],
            ["compound sentence (before FANBOYS)", "The doors were open, but it was a trap."], ["nonessential (nonrestrictive) elements", "Weena, who was frightened, clung to him."], ["coordinate adjectives", "a dark, narrow tunnel"],
            ["direct address", "Tell us, Traveller, what you saw."], ["dates and places", "On June 3, 2027, in Dayton, Ohio, …"], ["dialogue tags", "“I'm back,” he said."]], (2.4, 3.2), fs=9),
     KeyIdea("Commas mark introductions, series, compound sentences, nonessential elements, coordinate adjectives, direct address, dates and places, and dialogue.")],
    [Problem("Add commas: After the escape the Traveller rested.", "After the escape, the Traveller rested."), Problem("Add commas: Wells who wrote the novel lived in England.", "Wells, who wrote the novel, lived in England."), Problem("Add commas: Look Weena the stars!", "Look, Weena, the stars!")],
    [S("Warm-Up", [SA("Comma before FANBOYS joins…", "two independent clauses"), SA("Comma in direct address example", "Yes, Mom, I'm coming.")], cols=2),
     S("Add Commas", [SA(q, a) for q, a in [("Exhausted and hungry the Traveller returned.", "Exhausted and hungry, the Traveller returned."), ("The guests the Editor and the Doctor laughed.", "The guests, the Editor and the Doctor, laughed."),
                                            ("He saw crabs a red sun and a dark sea.", "He saw crabs, a red sun, and a dark sea."), ("It was cold yet he stayed.", "It was cold, yet he stayed."),
                                            ("On March 10 1895 they met in London England.", "On March 10, 1895, they met in London, England."), ("“Sit down” said the narrator.", "“Sit down,” said the narrator.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence that uses commas for an introductory phrase and a nonessential clause.", "Answers vary.", lines=2)])],
    te("Students apply comma rules.", "Use commas correctly; demonstrate command of punctuation.", "Workbook Lesson 8.2",
       "Let's eat Grandma.", "Find commas in Chapter 13.", ["Teach the chart."], "Your Turn 1–3.",
       ["Commas between subject and verb."], ["Read aloud for pauses, then check rules."], ["Comma rule poster."]),
    summary="Know the comma rules and their purposes.")

L3 = Lesson("8.3", "Semicolons and Colons",
    "I can use semicolons and colons correctly.", "L.7.2",
    [("semicolon", "Joins two closely related independent clauses, or separates items in a complex list."), ("colon", "Introduces a list, explanation, or quotation after a complete sentence.")],
    "What's the difference between “He had one goal: escape.” and “He had one goal; escape”?",
    [rules([["Mark", "Use", "Example"], ["semicolon", "join related independent clauses", "The doors were open; the machine was inside."], ["semicolon", "before a transition joining clauses", "He struck a match; however, it wouldn't light."],
            ["semicolon", "list items that contain commas", "He visited London, England; Paris, France; and the year 802,701."], ["colon", "after a complete sentence to introduce a list", "He packed three things: matches, a camera, and a bag."],
            ["colon", "after a complete sentence to introduce an explanation", "He had one goal: escape."]], (0.9, 2.3, 2.6), fs=9),
     WatchOut("A colon must follow a complete sentence. Wrong: “He packed: matches and a camera.” Right: “He packed two things: matches and a camera.”"),
     KeyIdea("Semicolons join related independent clauses; colons introduce after a complete sentence.")],
    [Problem("Punctuate: The fire spread the Morlocks fled.", "The fire spread; the Morlocks fled."), Problem("Correct? “He needed: light.”", "No; He needed one thing: light."), Problem("Punctuate: It was dark however he kept going.", "It was dark; however, he kept going.")],
    [S("Warm-Up", [SA("Semicolon joins two…", "independent clauses"), SA("A colon must follow a…", "complete sentence")], cols=2),
     S("Punctuate", [SA(q, a) for q, a in [("The Eloi played the Morlocks worked.", "The Eloi played; the Morlocks worked."), ("Weena gave him two things flowers and friendship.", "Weena gave him two things: flowers and friendship."),
                                           ("He was tired nevertheless he climbed on.", "He was tired; nevertheless, he climbed on."), ("The guests came from Leeds England Cork Ireland and Bath England.", "Leeds, England; Cork, Ireland; and Bath, England."),
                                           ("The Traveller said one word home.", "The Traveller said one word: home.")]], cols=1),
     S("Exit Ticket", [OR("Write one sentence with a semicolon and one with a colon about Chapter 13.", "Answers vary.", lines=2)])],
    te("Students use semicolons and colons.", "Demonstrate command of punctuation.", "Workbook Lesson 8.3",
       "goal: escape.", "Find semicolons in the Reader.", ["Teach uses; the Watch Out."], "Your Turn 1–3.",
       ["Colons after incomplete sentences."], ["Cover what follows; is it a sentence?"], ["Rewrite comma splices with semicolons."]),
    summary="Semicolons join; colons introduce.")

L4 = Lesson("8.4", "Dashes, Parentheses, Ellipses, and Advanced Capitalization",
    "I can use dashes, parentheses, and ellipses for effect and apply advanced capitalization rules.", "L.7.2, L.8.2a",
    [("dash", "A mark (—) that sets off information dramatically or shows an interruption."), ("ellipsis", "Three dots (…) that show omitted words or a pause.")],
    "How does punctuation change the voice of a sentence?",
    [rules([["Mark", "Effect", "Example"], ["dash —", "dramatic emphasis or interruption", "The doors were open — a trap."], ["parentheses ( )", "quiet, extra information", "The Time Traveller (as we called him) smiled."],
            ["ellipsis …", "omission in a quote or a trailing pause", "“I'll tell you everything, but first…”"]], (1.2, 2.0, 2.6), fs=9),
     rules([["Capitalize", "Don't capitalize"], ["regions: the South, the Midwest", "directions: drive south"], ["titles before names: Doctor Lanyon", "titles used generally: the doctor"],
            ["family words used as names: Is Grandma here?", "with possessives: my grandma"], ["specific courses: Algebra I, English", "general subjects: math, science"]], (2.8, 2.8), fs=9),
     KeyIdea("Dashes emphasize, parentheses whisper, ellipses omit or pause. Capitalize specific names, not general words.")],
    [Problem("Which mark adds dramatic emphasis?", "dash"), Problem("Capitalize? “We moved to the south.” (region)", "the South"), Problem("Capitalize? “my uncle” vs “Uncle Ray”", "my uncle (lowercase); Uncle Ray (capitalized)")],
    [S("Warm-Up", [SA("An ellipsis shows…", "omission or pause"), SA("Parentheses add ___ information.", "extra, quiet")], cols=2),
     S("Punctuate and Capitalize", [SA(q, a) for q, a in [("The machine was gone stolen.", "The machine was gone — stolen."), ("H. G. Wells 1866–1946 wrote the novel.", "H. G. Wells (1866–1946) wrote the novel."),
                                                         ("we drove north to visit grandma in the midwest.", "We drove north to visit Grandma in the Midwest."), ("my mom teaches science and spanish.", "My mom teaches science and Spanish."),
                                                         ("“I wonder” she whispered, trailing off.", "“I wonder…” she whispered, trailing off.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence using a dash for emphasis.", "Answers vary.", lines=2)])],
    te("Students use advanced punctuation and capitalization.", "Use punctuation to indicate a pause or break; use an ellipsis to indicate an omission; capitalize correctly.", "Workbook Lesson 8.4",
       "Punctuation voice.", "Find dashes in the Reader.", ["Teach both charts."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Overusing dashes."], ["One dash per paragraph."], ["Rewrite a paragraph three ways with different punctuation."]),
    summary="Dashes emphasize, parentheses whisper, ellipses omit; capitalize specifics.")

# ================================================================= Week 2 · Edit conventions in context (Chapter 14)
L5 = Lesson("8.5", "Imagery and Mood in the Far Future",
    "I can analyze how imagery creates mood and develops theme.", "RL.7.4, RL.7.2",
    [],
    "What would the end of the world look like?",
    [ReaderAssign(TM, "Chapter 14: The Further Vision", "What does the Traveller see millions of years in the future? How does it make him feel?"),
     Text("In Chapter 14, the Traveller journeys to a distant future: a dim red sun, a cold beach, giant crab-like creatures, and finally an eerie darkness. Wells uses imagery of cold, silence, and fading light to create a mood of desolation."),
     Figure(lambda t: table(t, [["Image", "Mood / idea"], ["huge red sun", "the aging, dying solar system"], ["cold, silent beach", "loneliness, the end of life"], ["giant crab creatures", "menace; life reduced to strange forms"], ["growing darkness", "the end of everything"]],
                            [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     KeyIdea("Imagery creates mood and suggests theme: here, the impermanence of humanity and life itself.")],
    [Problem("What color is the sun?", "red (dim)"), Problem("What mood does the far future create?", "desolate, lonely, eerie"), Problem("What theme does it suggest?", "Nothing lasts forever, even humanity.")],
    [S("Warm-Up", [SA("Imagery appeals to…", "the senses"), SA("Mood of Chapter 14", "desolate, eerie")], cols=2),
     S("Analyze", [OR("Copy two images from Chapter 14 and explain the mood each creates.", "Answers vary.", lines=4), OR("How does this vision connect to the novel's themes?", "It extends the decline of humanity to the end of life itself; impermanence.", lines=3)]),
     S("Exit Ticket", [OR("Why do you think Wells included this chapter after the Morlock story was resolved?", "Answers vary; to broaden the theme beyond humanity to all life and time.", lines=2)])],
    te("Students analyze imagery and mood.", "Analyze the impact of word choice on meaning and tone; determine theme.", "The Time Machine Reader (Chapter 14), workbook Lesson 8.5",
       "End of the world.", "Read Chapter 14.", ["Model the chart."], "Your Turn 1–3.",
       ["Summarizing instead of analyzing imagery."], ["Image → mood → theme chart."], ["Paint or draw the final scene."]),
    summary="Imagery creates mood and suggests theme.")

L6 = Lesson("8.6", "Quotations and Titles",
    "I can punctuate quotations and titles correctly.", "L.7.2",
    [],
    "Is it <i>The Time Machine</i> or “The Time Machine”?",
    [rules([["Italicize (underline by hand)", "Quotation marks"], ["books: <i>The Time Machine</i>", "chapters: “The Further Vision”"], ["plays: <i>The Tempest</i>", "short stories: “The Translator”"], ["magazines and newspapers: <i>The Crisis</i>", "poems: “We Wear the Mask”"],
            ["movies, albums, ships: <i>Sea Venture</i>", "articles, songs, episodes"]], (2.8, 2.8), fs=9),
     rules([["Quotation rule", "Example"], ["commas and periods inside", "“I'm tired,” he said. She called it a “fairy tale.”"], ["question/exclamation inside if part of the quote", "“Where were you?” asked the Editor."],
            ["question/exclamation outside if not part of the quote", "Did he really say “I traveled in time”?"], ["quotation within a quotation: single marks", "“He told me, ‘The future is dark,’” said the narrator."]], (2.6, 3.0), fs=9),
     KeyIdea("Long works: italics. Short works: quotation marks. Commas and periods go inside quotation marks.")],
    [Problem("Format: the poem Sympathy", "“Sympathy”"), Problem("Format: the novel Strange Case of Dr. Jekyll and Mr. Hyde", "italics"), Problem("Punctuate: Did you really call the story a fairy tale", "Did you really call the story a “fairy tale”?")],
    [S("Warm-Up", [SA("Book titles are…", "italicized"), SA("Poem titles go in…", "quotation marks")], cols=2),
     S("Punctuate", [SA(q, a) for q, a in [("We read the chapter The Last Night in Strange Case of Dr. Jekyll and Mr. Hyde.", "“The Last Night” … Strange Case of Dr. Jekyll and Mr. Hyde (italicized)"),
                                           ("Who wrote We Wear the Mask", "Who wrote “We Wear the Mask”?"), ("The Traveller said I have seen the future", "The Traveller said, “I have seen the future.”"),
                                           ("She said My teacher told us Read every word", "She said, “My teacher told us, ‘Read every word.’”")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence naming a book, a chapter, and a poem from this year with correct formatting.", "Answers vary.", lines=2)])],
    te("Students punctuate quotations and titles.", "Demonstrate command of punctuation.", "Workbook Lesson 8.6",
       "Italics or quotes?", "Review titles from this year.", ["Teach both charts."], "Your Turn 1–3.",
       ["Question marks placed incorrectly."], ["Is the question part of the quote?"], ["Format a reading list."]),
    summary="Italics for long works, quotation marks for short; punctuation inside.")

L7 = Lesson("8.7", "Common Errors: Splices, Run-Ons, Fragments, and Agreement",
    "I can find and fix comma splices, run-ons, fragments, and agreement errors in context.", "L.7.1, L.7.2",
    [("comma splice", "Two independent clauses joined only by a comma.")],
    "What's wrong with “The Traveller returned, he was exhausted”?",
    [rules([["Error", "Example", "Fixes"], ["comma splice", "He returned, he was exhausted.", "He returned. He was exhausted. / He returned; he was exhausted. / He returned, and he was exhausted. / When he returned, he was exhausted."],
            ["run-on", "He returned he was exhausted.", "same fixes as above"], ["fragment", "Because the doors were open.", "Because the doors were open, he went inside."], ["agreement", "The box of matches were empty.", "The box of matches was empty."]],
           (1.1, 2.0, 2.6), fs=8.5),
     KeyIdea("Fix splices and run-ons with a period, semicolon, comma + FANBOYS, or subordination. Complete fragments. Match subjects and verbs.")],
    [Problem("Fix: Weena was lost, he searched.", "Weena was lost; he searched. (or other fix)"), Problem("Fix: After the fire.", "e.g. After the fire, Weena was gone."), Problem("Fix: Each of the guests were doubtful.", "Each of the guests was doubtful.")],
    [S("Warm-Up", [SA("Comma splice =", "two independent clauses joined by only a comma"), SA("Four fixes", "period, semicolon, comma + FANBOYS, subordination")], cols=2),
     S("Fix the Error", [SA(q, a) for q, a in [("The sun was red, the beach was cold.", "The sun was red, and the beach was cold."), ("The crabs moved closer the Traveller fled.", "As the crabs moved closer, the Traveller fled."),
                                               ("While the guests listened.", "e.g. While the guests listened, the Traveller told his story."), ("Neither the Editor nor the Doctor believe him.", "Neither the Editor nor the Doctor believes him."),
                                               ("The flowers in the vase is strange.", "The flowers in the vase are strange.")]], cols=1),
     S("Exit Ticket", [OR("Write a comma splice, then fix it two different ways.", "Answers vary.", lines=3)])],
    te("Students fix common sentence errors.", "Demonstrate command of grammar and punctuation.", "Workbook Lesson 8.7",
       "returned, he was.", "Find errors in a sample paragraph.", ["Teach fixes."], "Your Turn 1–3.",
       ["Fixing splices with “and” only."], ["Four-fix menu."], ["Edit a past essay for splices."]),
    summary="Fix splices, run-ons, fragments, and agreement.")

L8 = Lesson("8.8", "Editing a Passage in Context",
    "I can edit a passage for multiple kinds of errors.", "L.7.1, L.7.2, W.7.5",
    [],
    "How many errors can you find in a single paragraph?",
    [P_EDIT,
     Text("Edit in passes: <b>(1)</b> sentence boundaries, <b>(2)</b> capitalization, <b>(3)</b> commas and other punctuation, <b>(4)</b> quotation marks and dialogue, <b>(5)</b> spelling, contractions, and confused words."),
     Example("Edit paragraph 1", "on a cold evening in march the time traveller limped into his dining room his guests stared at him his coat was torn and dusty and his face was pale",
             ["Sentence boundaries: three sentences.", "Capitals: On, March, Time Traveller, His.", "Commas: after March (introductory phrase); before and (compound)."],
             "On a cold evening in March, the Time Traveller limped into his dining room. His guests stared at him. His coat was torn and dusty, and his face was pale."),
     KeyIdea("Edit in passes; each pass catches a different kind of error.")],
    [Problem("Edit paragraph 2", "“What happened to you?” asked the Editor. The Traveller didn't answer right away; he poured himself a glass of water, drank it slowly, and then he said, “I'll tell you everything, but first I must eat.”"),
     Problem("How many sentences in paragraph 1?", "three"), Problem("Which pass catches “didnt”?", "pass 5 (contractions)")],
    [S("Warm-Up", [SA("First editing pass", "sentence boundaries"), SA("Fix: didnt", "didn't")], cols=2),
     S("Edit", [OR("Rewrite paragraph 2 correctly.", "“What happened to you?” asked the Editor. The Traveller didn't answer right away; he poured himself a glass of water, drank it slowly, and then he said, “I'll tell you everything, but first I must eat.”", lines=5)], passage=P_EDIT),
     S("Exit Ticket", [OR("Which pass found the most errors? Why do you think so?", "Answers vary.", lines=2)])],
    te("Students edit passages in context.", "Demonstrate command of conventions; edit writing.", "Workbook Lesson 8.8",
       "Error count.", "Read the passage.", ["Model passes on paragraph 1."], "Edit paragraph 2.",
       ["One-pass editing."], ["Colored pencil per pass."], ["Create an edit-me passage for a parent."], independent="Workbook. Weekly Check tomorrow."),
    summary="Edit in five passes.")

# ================================================================= Week 3 · Word parts and confusing words (Chapter 15 and After the Story)
L9 = Lesson("8.9", "Evidence, Belief, and the Narrator",
    "I can analyze how characters respond to evidence and how the narrator shapes the ending.", "RL.7.6, RI.7.8",
    [("skeptic", "A person who doubts claims until there is evidence.")],
    "If a friend told you they had traveled in time, what proof would you want?",
    [ReaderAssign(TM, "Chapter 15 and After the Story", "How do the guests react to the story? What evidence does the Traveller offer?"),
     P_SKEPTIC,
     KeyIdea("Compare how characters weigh evidence; notice how the narrator's view differs from the skeptics'.")],
    [Problem("What evidence does the Traveller show?", "strange white flowers (and the battered machine)"), Problem("How does the Editor respond to the story?", "He jokes that it's a pity the Traveller isn't a writer of stories (he treats it as fiction)."), Problem("How does the narrator differ from the other guests?", "He is less sure it's a lie; he returns the next day.")],
    [S("Warm-Up", [SA("Skeptic =", "one who doubts without evidence"), SA("What did Weena give him?", "flowers")], cols=2),
     S("Analyze", [OR("Is the guests' skepticism reasonable? Use the principle in the passage.", "Yes, partly: extraordinary claims require extraordinary evidence, and flowers aren't proof; but they also ignore puzzling evidence.", lines=4),
                   OR("Why does Wells end with the narrator's uncertainty instead of clear proof?", "It leaves readers to decide, preserving mystery and making them weigh the evidence too.", lines=3)], passage=P_SKEPTIC),
     S("Exit Ticket", [OR("Do you believe the Traveller's story within the novel? Explain with evidence.", "Answers vary.", lines=2)])],
    te("Students analyze evidence and belief.", "Analyze points of view; evaluate evidence.", "The Time Machine Reader (Chapter 15, After the Story), workbook Lesson 8.9",
       "Proof of time travel.", ["Read Chapter 15 and After the Story.", "Read “Evidence and Belief.”"], ["Discuss extraordinary claims."], "Your Turn 1–3.",
       ["Dismissing skepticism as rude."], ["Evidence scale: weak to strong."], ["Debate: believer vs skeptic."]),
    summary="Weigh evidence; the narrator leaves the question open.")

L10 = Lesson("8.10", "Greek and Latin Roots Review",
    "I can use Greek and Latin roots to determine the meanings of academic and scientific words.", "L.7.4b",
    [],
    "What do <i>chronology</i>, <i>synchronize</i>, and <i>chronic</i> share?",
    [rules([["Root", "Meaning", "Examples"], ["chron", "time", "chronology, chronic, synchronize"], ["temp / tempor", "time", "temporary, contemporary, tempo"], ["scope", "look, see", "telescope, microscope, periscope"],
            ["phon", "sound", "telephone, symphony, phonetic"], ["vid / vis", "see", "evidence, visible, revise"], ["cred", "believe", "credible, incredible, credentials"], ["dict", "say", "predict, contradict, dictionary"],
            ["bio", "life", "biology, biography, antibiotic"], ["geo", "earth", "geology, geography"], ["-logy", "study of", "biology, chronology"]], (1.3, 1.3, 3.0), fs=9),
     Example("Analyze", "<i>incredible</i>", ["in- = not.", "cred = believe.", "-ible = able to be."], "not able to be believed"),
     KeyIdea("Roots unlock academic and scientific vocabulary; combine prefix + root + suffix.")],
    [Problem("<i>contemporary</i>", "existing at the same time"), Problem("<i>evidence</i>", "something that helps you see what is true"), Problem("<i>chronology</i>", "the study or order of events in time")],
    [S("Warm-Up", [SA("chron =", "time"), SA("cred =", "believe")], cols=2),
     S("Analyze", [SA(w, a) for w, a in [("synchronize", "make happen at the same time"), ("temporary", "lasting a limited time"), ("geology", "study of the earth"), ("credentials", "proof of qualifications (that make someone believable)"),
                                         ("biography", "written account of someone's life"), ("contradict", "say the opposite"), ("periscope", "an instrument for looking around/over obstacles"), ("anachronism", "something out of its proper time")]], cols=2),
     S("Apply", [OR("Use three root words from the chart in sentences about The Time Machine.", "Answers vary.", lines=3)])],
    te("Students review roots.", "Use Greek or Latin roots as clues to meaning.", "Workbook Lesson 8.10",
       "chron words.", "Find root words in Chapter 15.", ["Teach the chart."], "Your Turn 1–3.",
       ["Ignoring prefixes that reverse meaning (in-)."], ["Word-part sums."], ["Make a root word tree."]),
    summary="Roots unlock academic and scientific words.")

L11 = Lesson("8.11", "Commonly Confused Words",
    "I can correctly use commonly confused words.", "L.7.1, L.7.2b",
    [],
    "Does the story “affect” or “effect” you?",
    [rules([["Words", "Meaning", "Example"], ["affect / effect", "verb: influence / noun: result", "The story affected me. Its effect was strong."], ["accept / except", "receive / excluding", "He accepted the flowers. Everyone except the narrator doubted."],
            ["than / then", "comparison / time", "Bigger than a house. Then he left."], ["lose / loose", "misplace / not tight", "Don't lose the key. The bolt was loose."], ["principal / principle", "school head or main / rule or belief", "the principal reason; a scientific principle"],
            ["complement / compliment", "completes / praise", "The colors complement each other. She gave a compliment."], ["their / there / they're", "possessive / place / they are", "They're putting their coats over there."], ["its / it's", "possessive / it is", "It's late; the machine lost its lever."]],
           (1.5, 1.9, 2.4), fs=8.5),
     KeyIdea("Learn the meaning of each confusable; test contractions by expanding them.")],
    [Problem("The fire had a terrible (affect/effect).", "effect"), Problem("Everyone (accept/except) the narrator laughed.", "except"), Problem("The machine was faster (than/then) light. (in the story)", "than")],
    [S("Warm-Up", [SA("affect is usually a…", "verb"), SA("effect is usually a…", "noun")], cols=2),
     S("Choose", [SA(q, a) for q, a in [("The darkness (affected/effected) his mood.", "affected"), ("Will you (accept/except) the invitation?", "accept"), ("He was more tired (than/then) ever.", "than"),
                                        ("Don't (lose/loose) the matches!", "lose"), ("Honesty is an important (principal/principle).", "principle"), ("(Its/It's) a strange flower.", "It's"), ("The guests offered a (complement/compliment).", "compliment"),
                                        ("(Their/There/They're) waiting for the Traveller.", "They're")]], cols=2),
     S("Exit Ticket", [OR("Write a sentence using both affect and effect correctly.", "e.g. The ending affected me; its effect lasted for days.", lines=2)])],
    te("Students use confusable words.", "Demonstrate command of conventions, including spelling.", "Workbook Lesson 8.11",
       "affect or effect?", "Review the chart.", ["Teach memory tricks (e.g. Affect = Action; Effect = End result)."], "Your Turn 1–3.",
       ["Relying on spell-check."], ["Memory tricks."], ["Find confusable errors online."]),
    summary="Know the meanings of confusable words.")

L12 = Lesson("8.12", "Spelling Rules and Patterns",
    "I can spell correctly by applying spelling rules for prefixes and suffixes.", "L.7.2b",
    [],
    "Why is it “beginning” but “opening”?",
    [rules([["Rule", "Examples"], ["Double the final consonant (one-syllable or stressed last syllable, short vowel + one consonant) before a vowel suffix", "stop → stopped; begin → beginning; but open → opening (stress not on last syllable)"],
            ["Drop silent e before a vowel suffix; keep it before a consonant suffix", "hope → hoping; hope → hopeful"], ["Change y to i (consonant + y) except before -ing", "carry → carried; carry → carrying"],
            ["Adding a prefix doesn't change the base spelling", "mis + spell → misspell; un + necessary → unnecessary"], ["-able vs -ible: -able usually follows a complete word", "comfortable, readable vs visible, credible"]],
           (3.0, 2.6), fs=8.5),
     KeyIdea("Apply doubling, drop-e, y-to-i, and prefix rules; check uncertain words in a dictionary.")],
    [Problem("Add -ing: refer", "referring"), Problem("Add -ness: happy", "happiness"), Problem("Prefix: dis + satisfied", "dissatisfied")],
    [S("Warm-Up", [SA("hope + ing", "hoping"), SA("hope + ful", "hopeful")], cols=2),
     S("Add the Ending or Prefix", [SA(q, a) for q, a in [("occur + ed", "occurred"), ("travel + er (American)", "traveler"), ("argue + ment", "argument"), ("deny + al", "denial"), ("mis + step", "misstep"), ("im + mobile", "immobile"),
                                                          ("rely + able", "reliable"), ("admit + ance", "admittance")]], cols=2),
     S("Exit Ticket", [OR("List three words you often misspell and the rule that helps with each.", "Answers vary.", lines=3)])],
    te("Students apply spelling rules.", "Spell correctly.", "Dictionary, workbook Lesson 8.12",
       "beginning vs opening.", "Review personal spelling lists.", ["Teach the rules."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Over-applying doubling."], ["Stress check: say it aloud."], ["Spelling bee with a sibling."]),
    summary="Apply spelling rules; check with a dictionary.")

# ================================================================= Week 4 · Reference tools and precise word choice (Epilogue)
L13 = Lesson("8.13", "Open Endings and Symbols",
    "I can analyze an open ending and the symbolism of a final image.", "RL.7.2, RL.7.5",
    [("open ending", "An ending that leaves important questions unanswered.")],
    "Why might an author choose not to tell readers what happened to the main character?",
    [ReaderAssign(TM, "Epilogue", "What happens to the Time Traveller? What does the narrator keep?"),
     Text("The Traveller leaves on another journey and never returns. The narrator keeps two strange white flowers, shriveled now, and reflects that even when intelligence and strength are gone, gratitude and tenderness lived on in a human heart."),
     Example("Analyze the final symbol", "The flowers", ["They came from Weena, a gift of affection.", "They are evidence the narrator can't explain.", "They suggest kindness survives even in a decaying world."], "The flowers symbolize hope and human tenderness that outlast even civilization's decline."),
     KeyIdea("Open endings invite readers to think; final images often carry the theme.")],
    [Problem("What happens to the Traveller?", "He leaves on another journey and never returns."), Problem("What does the narrator keep?", "two strange white flowers"), Problem("What do the flowers symbolize?", "gratitude, tenderness, hope")],
    [S("Warm-Up", [SA("Open ending =", "leaves questions unanswered"), SA("Who gave the flowers?", "Weena")], cols=2),
     S("Analyze", [OR("Why does Wells end with the flowers instead of with the Traveller's fate? What theme does this suggest?", "The flowers carry the hopeful theme that kindness endures; the open fate keeps mystery.", lines=4),
                   OR("Write your own two-sentence theory of where the Traveller went.", "Answers vary.", lines=2)]),
     S("Exit Ticket", [OR("Do you prefer open or closed endings? Why?", "Answers vary.", lines=2)])],
    te("Students analyze open endings and symbols.", "Determine theme; analyze structure.", "The Time Machine Reader (Epilogue), workbook Lesson 8.13",
       "Unanswered ending.", "Read the Epilogue.", ["Model symbol analysis."], "Your Turn 1–3.",
       ["Wanting a definite answer."], ["Theory-with-evidence frame."], ["Write a sequel opening."]),
    summary="Open endings invite thought; final symbols carry theme.")

L14 = Lesson("8.14", "Using Reference Tools for Precise Word Choice",
    "I can use a dictionary and thesaurus to choose words with precise meanings and connotations.", "L.7.4c, L.7.4d, L.7.5c",
    [("nuance", "A subtle difference in meaning or feeling.")],
    "Why might a thesaurus suggestion be the wrong word?",
    [Text("A thesaurus offers synonyms, but synonyms differ in <b>nuance</b> and <b>connotation</b>. After choosing a synonym, check its dictionary definition and example sentences to be sure it fits."),
     Example("Choose precisely", "The guests were ___ about the story. (thesaurus for “doubtful”: skeptical, suspicious, cynical, dubious)", ["skeptical: wanting evidence before believing (fits).", "suspicious: thinking someone is guilty or dishonest (too strong).", "cynical: believing people act only selfishly (wrong idea)."], "skeptical"),
     KeyIdea("Thesaurus for options; dictionary for precision; context for the final choice.")],
    [Problem("Which fits a scientist who wants proof: skeptical or cynical?", "skeptical"), Problem("Why check the dictionary after the thesaurus?", "to confirm the exact meaning and connotation"), Problem("What is nuance?", "a subtle difference in meaning")],
    [S("Warm-Up", [SA("Thesaurus gives…", "synonyms"), SA("Dictionary confirms…", "exact meaning")], cols=2),
     S("Choose the Precise Word", [MC(q, ch, k) for q, ch, k in [("The far-future beach was ___ (empty and depressing).", ["vacant", "desolate", "spacious"], 1), ("The Traveller's escape was ___ (barely successful).", ["narrow", "thin", "slim"], 0),
                                                                 ("Weena was ___ (gentle and easily frightened).", ["timid", "cowardly", "weak"], 0), ("The Morlocks' tunnels were ___ (causing a feeling of horror).", ["scary", "ghastly", "unpleasant"], 1)]]),
     S("Exit Ticket", [OR("Choose one vague word from your recent writing. Use a thesaurus and dictionary to replace it. Explain your choice.", "Answers vary.", lines=3)])],
    te("Students use references for precise words.", "Consult reference materials; verify meanings; distinguish connotations.", "Dictionary and thesaurus, workbook Lesson 8.14",
       "Wrong thesaurus words.", "Look up “doubtful” in a thesaurus.", ["Model the process."], "Your Turn 1–3.",
       ["Choosing the fanciest synonym."], ["Thesaurus → dictionary → sentence test."], ["Build a personal precise-words list."]),
    summary="Thesaurus for options, dictionary for precision.")

L15 = Lesson("8.15", "Concise, Formal Style",
    "I can write concisely in a formal style appropriate to academic writing.", "W.7.1d, W.7.2e, L.7.3a",
    [("formal style", "Language without slang, contractions, or casual phrases, suited to academic writing.")],
    "Would you write a school essay the way you text a friend?",
    [rules([["Informal or wordy", "Formal and concise"], ["Wells's book is super creepy and kind of sad.", "Wells's novel is unsettling and melancholy."], ["The reason why is because the Morlocks are scary.", "The Morlocks are frightening."],
            ["In my opinion, I think the ending is good.", "The ending is effective because…"], ["The Traveller doesn't really get along with the guests.", "The Traveller struggles to persuade his skeptical guests."], ["At this point in time", "now"]], (2.8, 2.8), fs=9),
     KeyIdea("Formal academic writing: no slang, fewer contractions, precise words, no padding.")],
    [Problem("Formal: kind of sad", "melancholy, somewhat sad"), Problem("Concise: The reason why is because", "because"), Problem("Remove: In my opinion, I think", "(state the claim directly)")],
    [S("Warm-Up", [SA("Formal replacement for “super”", "extremely, very (or precise word)"), SA("Concise: due to the fact that", "because")], cols=2),
     S("Revise to Formal and Concise", [SA(q, a) for q, a in [("The Eloi are basically just lazy kids.", "The Eloi are childlike and idle."), ("Wells wanted to say like that inequality is bad.", "Wells warns against inequality."),
                                                             ("It is really very important to note that the ending is open.", "Notably, the ending is open."), ("The Traveller gets totally freaked out by the Morlocks.", "The Morlocks terrify the Traveller.")]], cols=1),
     S("Exit Ticket", [OR("Revise one paragraph from a past essay for formal, concise style.", "Answers vary.", lines=5)])],
    te("Students write in a concise formal style.", "Establish and maintain a formal style; choose concise language.", "Workbook Lesson 8.15",
       "Texting vs essays.", "Compare a text message and an essay sentence.", ["Model revisions."], "Your Turn 1–3.",
       ["Overly fancy, unclear words."], ["Formal ≠ complicated."], ["Revise a portfolio piece."]),
    summary="Formal, concise, precise academic style.")

L16 = Lesson("8.16", "Final Edit of a Portfolio Piece",
    "I can edit a complete piece of writing for conventions and style.", "W.7.5, L.7.1–3",
    [],
    "Which piece from this year deserves a final polish?",
    [Figure(lambda t: table(t, [["Final edit checklist", "✓"], ["Sentence boundaries: no splices, run-ons, or fragments.", ""], ["Commas, semicolons, colons, and dashes are correct.", ""], ["Titles and quotations are punctuated correctly.", ""],
                                ["Capitalization is correct.", ""], ["Confused words and spelling are correct.", ""], ["Words are precise; style is formal and concise.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("A final edit checks every convention and sharpens style.")],
    [Problem("Name one item on the checklist.", "Answers vary."), Problem("Why edit in passes?", "Each pass focuses on one kind of error."), Problem("What does formal style avoid?", "slang, casual phrases, padding")],
    [S("Warm-Up", [SA("Fix: its a classic", "It's a classic."), SA("Format: the novel The Time Machine", "italics")], cols=2),
     S("Final Edit", [OR("Choose a piece from this year. Edit it with the checklist. List five corrections and two style improvements.", "Answers vary.", lines=7)])],
    te("Students perform a final edit.", "Strengthen writing by editing; demonstrate command of conventions.", "A portfolio piece, workbook Lesson 8.16, Unit 8 Review",
       "Which piece?", "Select a piece.", ["Model the checklist."], "Edit.",
       ["Skipping the style pass."], ["One item per pass."], ["Share the polished piece."], independent="Edit; then the Unit 8 Review.", exit_="Tomorrow: Unit 8 Test."),
    summary="Final edit: conventions and style.")

# ================================================================= checks
C1 = Check("Weekly Check 22: Punctuation", [S("Read and answer", [
    SA("Why is there a comma after “2025”?", "a date in the middle of a sentence"), SA("Why is there a colon after “three things”?", "it introduces a list after a complete sentence"),
    SA("Why is there a semicolon after “plans”?", "it joins two related independent clauses"), SA("Why are commas around “a quiet woman named Ruth”?", "it's a nonessential appositive"),
    SA("What do the dashes emphasize?", "how she warned them (calmly but firmly)"), SA("Punctuate: We had one choice turn back.", "We had one choice: turn back."),
    SA("Capitalize: we flew south to visit the south.", "We flew south to visit the South.")], cols=1, passage=P_C22)], minutes=20)
C2 = Check("Weekly Check 23: Editing in Context", [S("Edit the passage", [
    OR("Add commas around the nonessential clause.", "Maya's project, which was about solar ovens, won first place.", lines=1),
    OR("Fix the quotation.", "Her teacher said, “This is the best project I've seen in years.”", lines=1),
    OR("Fix the comma splice two ways.", "Maya was proud. She thanked… / Maya was proud, so she thanked her teacher and called her parents.", lines=2),
    OR("Format: the book Their Eyes Were Watching God and the poem Sympathy.", "Their Eyes Were Watching God (italics); “Sympathy”", lines=1),
    OR("Fix: Did she really say I won", "Did she really say, “I won”?", lines=1)], cols=1, passage=P_C23)], minutes=20)
C3 = Check("Weekly Check 24: Words and Spelling", [S("Show what you know", [
    SA("<i>chronicle</i> root and meaning", "chron: time; a record of events in time order"), SA("<i>incredible</i>", "not able to be believed"), SA("The news (affected/effected) everyone.", "affected"),
    SA("Everyone (accept/except) Leo came.", "except"), SA("(Than/Then) we left.", "Then"), SA("begin + ing", "beginning"), SA("carry + ed", "carried"), SA("mis + spell", "misspell")], cols=2)], minutes=15)

REVIEW = Check("Unit 8 Review", [
    S("Punctuation", [SA("Punctuate: It rained however we played.", "It rained; however, we played."), SA("Punctuate: He needed one thing courage.", "He needed one thing: courage."),
                      SA("Format: the chapter The Further Vision", "“The Further Vision”"), SA("Fix the splice: I read the book, it was great.", "I read the book, and it was great.")], cols=1),
    S("Words and style", [SA("affect =", "verb: to influence"), SA("principle =", "a rule or belief"), SA("deny + al", "denial"), SA("Formal: The ending is kind of weird.", "The ending is unsettling.")], cols=2)],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 8 Test", [
    S("Part A · Edit the letter (1 point each)", [
        SA("Edit line 1 (the greeting).", "Dear Reader in the Year 2125,"),
        OR("Edit paragraph 2.", "I am writing this letter in June 2027, and I wonder what your world is like. Do you still read books, or do stories appear in the air around you? Does anyone still remember The Time Machine (italics) by H. G. Wells?", lines=4, points=3),
        OR("Edit paragraph 3.", "My grandmother, who was born in 1955, told me that when she was young, computers filled whole rooms. Now I carry one in my pocket that is more powerful than all of them combined. I can't imagine what you carry.", lines=4, points=3),
        OR("Edit the last line.", "Please take care of the Earth; it's the only one we have.", lines=2)], passage=P_TEST),
    S("Part B · Rules (1 point each)", [
        SA("Why does “who was born in 1955” need commas?", "It's a nonessential clause."), SA("Which word in paragraph 3 is a confused word?", "then (should be than)"),
        SA("Why is The Time Machine italicized?", "It's a book (long work)."), SA("Root of <i>chronology</i> and its meaning", "chron: time")], cols=1),
    S("Part C · Precise and formal style (1 point each)", [
        SA("Formal: The future is gonna be super different.", "The future will be dramatically different."), SA("Concise: at this point in time", "now"),
        MC("Most precise word for “empty and sad” describing a future city:", ["empty", "desolate", "big"], 1)], cols=1),
    S("Part D · Write (5 points)", [OR("Write your own letter to a reader in 2125 (6–8 sentences). Use a colon, a semicolon, a nonessential clause with commas, a correctly formatted title, and formal, precise language.",
                                       "Rubric: colon (1); semicolon (1); nonessential clause (1); title formatted (1); formal, precise, error-free (1).", lines=14, points=5)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-05-24", "2027-05-31", "2027-06-07", "2027-06-14"], CHECKS, REVIEW, TEST)

UNIT = Unit(8, "Conventions and Word Choice", "Commas, semicolons, colons, dashes, quotation and title punctuation, editing, roots, confusing words, spelling, and precise formal style, with The Time Machine, Chapters 13–15 and Epilogue.",
    "The Time Traveller escapes the Morlocks, glimpses the end of the world, and returns home to skeptical friends. As his story ends, you'll sharpen the conventions that make writing clear and credible: advanced punctuation, careful editing, word roots and confusing words, spelling rules, and precise, formal style.",
    ["Analyze the novel's climax, imagery, evidence, and open ending.", "Use commas, semicolons, colons, dashes, parentheses, ellipses, and capitalization correctly.",
     "Punctuate quotations and titles; edit for splices, fragments, and agreement in context.", "Use roots, confusable words, spelling rules, references, and formal concise style."],
    [("RL.7.2–6", "Theme; word choice; structure; point of view."), ("L.7.1–5", "Grammar, punctuation, spelling, precise language, roots, and nuance."), ("W.7.1d, W.7.5", "Formal style; editing.")],
    [("semicolon", "Joins related independent clauses."), ("colon", "Introduces after a complete sentence."), ("comma splice", "Two sentences joined by only a comma."), ("nuance", "A subtle difference in meaning."), ("formal style", "Academic language without slang.")],
    ["Units 5–6 grammar."], ["The Time Machine Reader (Chapters 13–15, Epilogue)", "Dictionary and thesaurus"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Polished conventions make applications, emails, and reports credible; a single misplaced comma can change meaning.",
    family_note="Have your student proofread a family email or letter before it is sent.",
    weeks=WEEKS)
