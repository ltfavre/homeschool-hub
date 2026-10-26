"""Grade 7 ELA · Unit 4: Craft and Perspective — word choice and tone, structure, point of view and purpose, symbolism, and comparing fiction with history.
Anchor reading: Strange Case of Dr. Jekyll and Mr. Hyde Reader, Chapters 5–10 (Jan 25 – Feb 19, 2027)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule
from content.ela7.unit03 import JH

# ================================================================= passages
P_TWO = Passage("Jekyll's Statement, Chapter 10 (original text, excerpt)", [
    "“…man is not truly one, but truly two.”",
], source="Robert Louis Stevenson, Strange Case of Dr. Jekyll and Mr. Hyde. Public domain.", genre="Classic novel excerpt", numbered=False)

P_LONDON = Passage("Fog and Gaslight: Victorian London", [
    "<b>A City of Contrasts</b>",
    "In the 1880s, London was the largest city in the world, home to more than four million people. Its wealthy neighborhoods had grand squares and elegant houses. Only a short walk away, poor families crowded into narrow lanes and dark courtyards.",
    "<b>The Famous Fog</b>",
    "London's fogs were thick, yellow-brown, and sometimes deadly. Coal fires in homes and factories filled the damp air with smoke. On the worst days, people could not see their own hands, and travelers lost their way on familiar streets.",
    "<b>Light in the Darkness</b>",
    "Gas streetlamps lit the main roads at night. Lamplighters walked the streets each evening, lighting lamps one by one. But the light was dim, and alleys and back streets remained in deep shadow.",
    "<b>Respectability and Secrets</b>",
    "Victorian society placed great value on <b>respectability</b>, a reputation for proper behavior. Gentlemen were expected to control their emotions and hide any private weaknesses. Many historians believe this pressure to appear perfect is one reason stories about hidden second selves fascinated Victorian readers.",
], source="An original informational text", genre="Informational text", numbered=False)

P_HAND = Passage("Handwriting as Evidence", [
    "When a document's author is in doubt, investigators may call on a <b>forensic document examiner</b>, an expert who analyzes handwriting, paper, and ink.",
    "No two people write exactly alike. Examiners compare <b>exemplars</b>, samples known to be written by a person, with the <b>questioned document</b>. They look at letter shapes, spacing, slant, pen pressure, and the way letters connect.",
    "A clever forger may copy the shapes of letters but often writes too slowly and carefully. The result can show shaky lines, blunt starts and stops, and unnatural pauses, which examiners call signs of <b>hesitation</b>.",
    "Handwriting analysis cannot prove guilt by itself, but combined with other evidence it can be powerful. In <i>Strange Case of Dr. Jekyll and Mr. Hyde</i>, a clerk's observation about two handwriting samples gives Mr. Utterson a chilling clue.",
], source="An original informational text", genre="Informational text")

P_OPED = Passage("Should Science Have Limits?", [
    "Scientific discoveries have given us vaccines, electricity, and the internet. Some people argue that science should never be restricted, because we cannot know which experiment will lead to the next great breakthrough.",
    "I disagree. Science must have limits, especially when experiments involve human beings. History offers painful examples of researchers who harmed people in the name of progress, often people who never agreed to take part.",
    "Of course, limits can slow discovery, and rules written by people who don't understand the research may block valuable work. These concerns are real. But careful review by independent experts, who weigh risks and benefits before an experiment begins, protects both the public and the trust that science depends on.",
    "Freedom to explore is one of science's greatest strengths. Responsibility is another. A scientist who ignores the second may lose the first.",
], source="An original opinion essay", genre="Argument")

P_SELF = Passage("Scientists Who Experimented on Themselves", [
    "<b>The Doctor Who Reached His Own Heart</b>",
    "In 1929, a young German doctor named Werner Forssmann believed a thin tube could be guided through a vein all the way to the heart, a procedure many experts considered deadly. When his supervisors refused permission, Forssmann numbed his own arm, inserted a tube into a vein, and pushed it toward his heart. Then he walked to the X-ray room to photograph the result.",
    "Forssmann's colleagues were not impressed, and he was criticized for his reckless act. Decades later, however, the technique, called cardiac catheterization, became a standard part of medicine. In 1956, Forssmann shared the Nobel Prize in Physiology or Medicine.",
    "<b>The Doctor Who Drank Bacteria</b>",
    "In the early 1980s, Australian doctors Barry Marshall and Robin Warren argued that many stomach ulcers were caused by bacteria, not stress. Other scientists doubted them. In 1984, Marshall drank a culture of the bacteria. Within days he became ill with stomach inflammation, supporting the doctors' claim. Marshall and Warren received the Nobel Prize in 2005.",
    "<b>A Risky Tradition</b>",
    "Self-experimentation has produced important discoveries, but it can also cause serious harm, and its results can be misleading because they involve only one person. Today, research involving people is reviewed by ethics committees designed to protect volunteers, including the scientists themselves.",
], source="An original informational text based on historical facts", genre="Informational text", numbered=False)

P_C10 = Passage("The Abandoned Theater", [
    "The Rialto Theater had been closed for forty years. Its marquee sagged, its letters long since fallen, and its doors were chained shut. Pigeons nested in the broken ticket booth.",
    "But on the night of the storm, Cass saw a flicker of light in the upper window. Then music, faint, tinny, and impossibly old, drifted out into the rain.",
], source="An original story", genre="Mystery")

P_C11 = Passage("Two Diary Entries", [
    "<b>Sam's diary, June 3.</b> Best day ever! My brother Nate finally agreed to take me fishing at the lake. We caught three fish and he even let me row the boat. I think he actually likes hanging out with me.",
    "<b>Nate's diary, June 3.</b> Mom made me take Sam fishing because she had to work. I was supposed to go to Jake's party. Sam talked the entire time and scared away half the fish. But when he caught his first bass, his face lit up like fireworks. Okay. Maybe it wasn't the worst day.",
], source="Original diary entries", genre="Fiction", numbered=False)

P_C12 = Passage("The Locket", [
    "Grandmother's silver locket had always been closed. When Rosa finally opened it, after the funeral, she expected a photograph of Grandfather. Instead she found a tiny folded paper.",
    "On it, in faded ink, was a single word: <i>Brave.</i> Rosa remembered her grandmother crossing the border with two children and one suitcase, remembered her learning English from library books at sixty. Rosa closed the locket and fastened it around her own neck.",
], source="An original story", genre="Realistic fiction")

P_TEST = Passage("The Understudy", [
    "For six weeks, Priya had been the understudy for the lead role in the school play. Every afternoon she sat in the back row of the auditorium, mouthing every line while Madison rehearsed onstage. She knew the part better than anyone. No one noticed.",
    "Then, on opening night, Madison lost her voice.",
    "Backstage was chaos. The director paced. The stage manager whispered into her headset. Priya stood very still, her heart hammering so hard she could hear it, a drum in an empty room. Someone pressed a costume into her arms.",
    "When the curtain rose, the lights blazed, hot and blinding. For one terrible second, Priya's mind was a blank page. Then she heard the first line, the one she had whispered to herself a hundred times in the dark, and it came out of her mouth as naturally as breathing.",
    "Afterward, in the crowded hallway, Madison found her. Her voice was a hoarse whisper, but her smile was real. “You were the role,” she said. Priya laughed. For six weeks she had felt invisible. Tonight, for the first time, she felt like she was standing in her own light.",
], source="An original story", genre="Realistic fiction")

# ================================================================= Week 1 · Word meaning and text structure (Chapters 5–6)
L1 = Lesson("4.1", "Word Choice and Tone",
    "I can analyze how word choice creates tone and mood.", "RL.7.4, L.7.5c",
    [("tone", "The author's attitude toward the subject or audience."), ("mood", "The feeling a text creates in the reader."), ("diction", "An author's choice of words.")],
    "What words would you use to describe a house where something terrible has happened?",
    [ReaderAssign(JH, "Chapters 5–6: Incident of the Letter; Remarkable Incident of Dr. Lanyon", "What does Guest notice about the handwriting? What happens to Dr. Lanyon?"),
     Text("Stevenson's <b>diction</b> is precise and often dark: words like <i>dreary, sinister, ghastly, loathing</i>. Analyze how specific words build a tone of dread and a mood of suspense."),
     Figure(lambda t: table(t, [["Word or phrase type", "Example effect"], ["dark adjectives", "build dread: “dismal,” “ghastly”"], ["weather and light", "fog and darkness mirror secrecy"],
                                ["restrained narration", "Utterson's calm voice makes horror feel more real"], ["physical reactions", "pallor, trembling, and fainting show fear without explaining it"]], [2.2 * inch, 3.4 * inch], width=5.6 * inch)),
     Example("Analyze diction", "Lanyon's change in Chapter 6", ["Details: Lanyon looks pale, aged, and frightened; he refuses to speak of Jekyll.", "Effect: his sudden decline signals that he has seen something terrible."],
             "Stevenson uses Lanyon's physical collapse to suggest a horror too great to describe."),
     KeyIdea("Diction creates tone and mood. Explain how specific words produce the effect.")],
    [Problem("Tone vs mood", "tone: author's attitude; mood: reader's feeling"), Problem("What does Guest notice?", "Hyde's handwriting resembles Jekyll's, but slanted differently."), Problem("What mood does Lanyon's decline create?", "dread, suspense")],
    [S("Warm-Up", [SA("Diction =", "word choice"), SA("Mood =", "the reader's feeling")], cols=2),
     S("Analyze Diction", [OR("Copy three words or phrases from Chapters 5–6 that create a dark mood. Explain each.", "Answers vary.", lines=5),
                           OR("How does Stevenson use Lanyon's physical condition instead of direct explanation? Why is this effective?", "He shows the shock through appearance and refusal to speak, letting readers imagine something horrible.", lines=4)]),
     S("Exit Ticket", [OR("Describe Stevenson's tone in one precise adjective and justify it.", "e.g. ominous: dark diction and withheld explanations", lines=2)])],
    te("Students analyze diction, tone, and mood.", "Analyze the impact of specific word choices on meaning and tone.", "Jekyll and Hyde Reader (Chapters 5–6), workbook Lesson 4.1",
       "Terrible house words.", "Read Chapters 5–6.", ["Teach tone vs mood; diction chart."], "Your Turn 1–3.",
       ["“The tone is scary” without evidence."], ["Tone word bank."], ["Rewrite a paragraph with a cheerful tone."]),
    summary="Word choice creates tone (author's attitude) and mood (reader's feeling).")

L2 = Lesson("4.2", "Structure: Letters, Documents, and Delay",
    "I can analyze how a novel's structure creates suspense.", "RL.7.5",
    [("epistolary elements", "Letters or documents included within a story."), ("delayed revelation", "Withholding key information until late in a story.")],
    "Why might an author give the reader sealed letters that can't be opened yet?",
    [Text("Stevenson builds his novel from <b>documents</b>: a will, letters, Lanyon's sealed narrative, and Jekyll's statement. Some documents must wait to be opened, which delays the revelation and makes readers impatient for the truth."),
     Figure(lambda t: table(t, [["Document", "Where", "Effect on suspense"], ["Jekyll's will", "Ch. 2", "raises the question of Hyde's hold on Jekyll"], ["Hyde's letter and Jekyll's note", "Ch. 5", "the handwriting clue"],
                                ["Lanyon's sealed letter", "Ch. 6", "a secret promised but withheld"], ["Lanyon's narrative and Jekyll's statement", "Ch. 9–10", "the final revelation"]], [1.9 * inch, 0.7 * inch, 2.9 * inch], width=5.5 * inch, font_size=9)),
     KeyIdea("Documents and delayed revelations structure the mystery and build suspense.")],
    [Problem("What does Lanyon's sealed letter instruct?", "not to open it until Jekyll's death or disappearance"), Problem("Why delay the revelation?", "to build suspense and keep the mystery alive"), Problem("Which chapters reveal the truth?", "9 and 10")],
    [S("Warm-Up", [SA("Delayed revelation =", "withholding key information"), SA("A document in Chapter 5", "Hyde's letter / Jekyll's note")], cols=2),
     S("Analyze", [OR("Why does Stevenson have Utterson promise not to open Lanyon's letter? How does this affect readers?", "It delays the truth; readers share Utterson's frustration and curiosity, increasing suspense.", lines=4),
                   OR("How would the novel change if it were told in order by Jekyll from the start?", "No mystery; readers would know the secret, losing suspense.", lines=3)]),
     S("Exit Ticket", [OR("Name another book or movie that delays its big reveal. How?", "Answers vary.", lines=2)])],
    te("Students analyze structure and suspense.", "Analyze how a text's form or structure contributes to its meaning.", "Workbook Lesson 4.2",
       "Sealed letters.", "Review documents so far.", ["Model the chart."], "Your Turn 1–3.",
       ["Summarizing documents without analyzing structure."], ["Ask: why here, why now?"], ["Restructure a fairy tale to delay its reveal."]),
    summary="Documents and delays create suspense.")

L3 = Lesson("4.3", "How Sections Build an Informational Text",
    "I can analyze how sections of an informational text contribute to the whole and develop ideas.", "RI.7.5, RI.7.3",
    [("respectability", "A reputation for proper, socially acceptable behavior.")],
    "How might the setting of Victorian London have shaped Stevenson's story?",
    [P_LONDON,
     Example("Analyze sections", "How does the final section connect to the rest?", ["Sections 1–3 describe contrasts, fog, and shadow.", "Section 4 explains respectability and hidden selves.", "Together: a city of light and darkness mirrors people with public and private sides."],
             "The sections build toward the idea that Victorian London's contrasts mirrored the double lives that fascinated readers."),
     KeyIdea("Each section contributes; analyze how the sections build the central idea.")],
    [Problem("Why was London's fog so thick?", "coal smoke mixed with damp air"), Problem("What does respectability mean?", "a reputation for proper behavior"), Problem("How does the setting mirror Jekyll and Hyde?", "contrasts of light and dark, public and hidden lives")],
    [S("Warm-Up", [SA("Number of sections", "four"), SA("Population of London in the 1880s", "more than four million")], cols=2),
     S("Analyze", [OR("Explain how each section contributes to the article's central idea.", "Contrasts → fog → dim light and shadows → respectability and secrets: London's literal and social darkness explains the appeal of double-life stories.", lines=5),
                   OR("Connect the article to one scene in the novel.", "Answers vary, e.g. fog in the Carew murder; Hyde's door in a shabby street near a respectable square.", lines=3)], passage=P_LONDON),
     S("Exit Ticket", [OR("Which section helped you understand the novel most? Why?", "Answers vary.", lines=2)])],
    te("Students analyze informational structure.", "Analyze the structure an author uses, including how major sections contribute to the whole.", "Workbook Lesson 4.3",
       "Setting's influence.", "Read “Fog and Gaslight.”", ["Model section analysis."], "Your Turn 1–3.",
       ["Summarizing each section separately."], ["Section → central idea arrows."], ["Research the Great Smog of 1952."]),
    summary="Sections build the central idea together.")

L4 = Lesson("4.4", "Technical Vocabulary",
    "I can determine the meaning of technical words in an informational text.", "RI.7.4, L.7.6",
    [("forensic", "Related to scientific methods used to investigate crimes."), ("exemplar", "A known sample used for comparison.")],
    "What clue does handwriting give Utterson in Chapter 5?",
    [P_HAND,
     Example("Use context", "What is a questioned document?", ["Paragraph 2 contrasts it with exemplars (known samples).", "So a questioned document is one whose author is unknown or disputed."], "a document whose author is in doubt"),
     KeyIdea("Technical words are often defined by context or contrast. Use them precisely in your own writing.")],
    [Problem("What is a forensic document examiner?", "an expert who analyzes handwriting, paper, and ink"), Problem("What are signs of hesitation?", "shaky lines, blunt starts and stops, unnatural pauses"), Problem("What does Guest notice?", "the two handwritings are alike except for slant")],
    [S("Warm-Up", [SA("Forensic =", "scientific methods for investigating crimes"), SA("Exemplar =", "a known sample")], cols=2),
     S("Technical Vocabulary", [SA(w, a) for w, a in [("questioned document", "a document whose author is in doubt"), ("slant", "the angle of handwriting"), ("hesitation", "signs of slow, careful forgery"), ("pen pressure", "how hard the writer presses")]], cols=2),
     S("Apply", [OR("Explain why the handwriting clue in Chapter 5 is so chilling. Use two technical terms.", "Comparing the exemplar (Jekyll's note) with the questioned document (Hyde's letter) shows only the slant differs, suggesting Jekyll wrote Hyde's letter.", lines=4)], passage=P_HAND),
     S("Exit Ticket", [OR("Why can't handwriting analysis prove guilt by itself?", "It must be combined with other evidence; it can suggest but not prove.", lines=2)])],
    te("Students determine technical vocabulary.", "Determine the meaning of words, including technical meanings; acquire domain-specific words.", "Workbook Lesson 4.4",
       "Handwriting clue.", "Read “Handwriting as Evidence.”", ["Model context for technical terms."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Using technical words loosely."], ["Glossary card."], ["Compare your handwriting slant with a family member's."]),
    summary="Context defines technical words; use them precisely.")

# ================================================================= Week 2 · Purpose and viewpoint (Chapters 7–8)
L5 = Lesson("4.5", "Point of View and Dramatic Irony",
    "I can analyze how differences in characters' and readers' knowledge create effects such as suspense.", "RL.7.6",
    [("limited third-person", "A narrator outside the story who follows one character's thoughts and knowledge."), ("dramatic irony", "When readers know (or suspect) something a character doesn't.")],
    "Why does Jekyll slam the window shut in Chapter 7?",
    [ReaderAssign(JH, "Chapters 7–8: Incident at the Window; The Last Night", "What do Utterson and Enfield see at the window? What do Utterson and Poole find when they break down the door?"),
     Text("The novel's narrator follows <b>Utterson</b> closely. We learn what he learns, when he learns it. Because many readers today already know the twist, they experience <b>dramatic irony</b>: understanding clues that Utterson misreads."),
     Example("Analyze", "The window scene", ["Utterson sees only Jekyll's face freeze in terror.", "Readers may suspect a transformation beginning.", "Effect: horror for readers; confusion for Utterson."],
             "The limited point of view keeps Utterson in the dark while readers sense the horror."),
     KeyIdea("Point of view controls what characters and readers know; gaps create suspense or irony.")],
    [Problem("Whose perspective does the narrator follow?", "Utterson's"), Problem("What is dramatic irony?", "readers knowing more than a character"), Problem("What do they find in Chapter 8?", "Hyde's body (dead), and documents left by Jekyll; Jekyll is gone")],
    [S("Warm-Up", [SA("Limited third-person follows…", "one character"), SA("Dramatic irony =", "readers know more than a character")], cols=2),
     S("Analyze", [OR("How does the limited point of view build suspense in Chapter 8?", "We only know what Utterson and Poole hear and see: strange voices, footsteps, the cabinet door, so the mystery stays unsolved until they break in.", lines=4),
                   OR("Explain a moment of dramatic irony in Chapters 7–8.", "Answers vary, e.g. Poole thinks his master has been murdered.", lines=3)]),
     S("Exit Ticket", [OR("If the story were told by Jekyll from the start, what would be lost?", "the suspense and mystery", lines=2)])],
    te("Students analyze point of view and irony.", "Analyze how an author develops and contrasts the points of view of different characters or narrators.", "Jekyll and Hyde Reader (Chapters 7–8), workbook Lesson 4.5",
       "Slammed window.", "Read Chapters 7–8.", ["Teach limited POV and dramatic irony."], "Your Turn 1–3.",
       ["Confusing dramatic irony with sarcasm."], ["Who knows what? chart."], ["Rewrite the window scene from Jekyll's POV."]),
    summary="Limited POV controls knowledge; gaps create suspense and irony.")

L6 = Lesson("4.6", "Author's Purpose and Point of View in Arguments",
    "I can determine an author's point of view and purpose in an argument.", "RI.7.6, RI.7.8",
    [("argument", "Writing that states a claim and supports it with reasons and evidence."), ("position", "The author's stance on an issue.")],
    "What would Dr. Jekyll say about whether science should have limits?",
    [P_OPED,
     Example("Identify position and purpose", "“Should Science Have Limits?”", ["Position: “I disagree. Science must have limits.”", "Purpose: to persuade readers to support independent review of experiments.", "Reasons: past harm to people; protects public trust."],
             "The author argues that science needs limits, especially for experiments on people."),
     KeyIdea("Find the position (often signaled by I believe, I disagree, must) and the purpose (persuade, inform, explain).")],
    [Problem("What is the author's position?", "Science must have limits, especially for human experiments."), Problem("What view does the author disagree with?", "that science should never be restricted"), Problem("What solution does the author propose?", "careful review by independent experts")],
    [S("Warm-Up", [SA("Position =", "the author's stance"), SA("Purpose of an argument", "to persuade")], cols=2),
     S("Analyze", [OR("List the author's two main reasons.", "Experiments have harmed people; review protects the public and trust.", lines=3),
                   OR("How would Jekyll respond to this essay? Use evidence from the novel.", "Answers vary; he ignored limits and harmed himself and others.", lines=4)], passage=P_OPED),
     S("Exit Ticket", [OR("Do you agree with the author? State your position in one sentence.", "Answers vary.", lines=2)])],
    te("Students identify position and purpose.", "Determine an author's point of view or purpose; trace and evaluate argument.", "Workbook Lesson 4.6",
       "Jekyll on limits.", "Read the opinion essay.", ["Model position and purpose."], "Your Turn 1–3.",
       ["Confusing others' views with the author's."], ["Mark “some argue” vs “I.”"], ["Write a response letter."]),
    summary="Identify the author's position, purpose, and reasons.")

L7 = Lesson("4.7", "Acknowledging Other Viewpoints",
    "I can analyze how an author acknowledges and responds to conflicting viewpoints.", "RI.7.6",
    [("counterclaim", "An opposing argument."), ("concession", "Admitting that part of the opposing view is valid."), ("rebuttal", "A response that shows why the counterclaim is weaker.")],
    "Why might an author mention arguments against their own position?",
    [Example("Find concession and rebuttal", "Paragraph 3 of “Should Science Have Limits?”", ["Counterclaim: limits can slow discovery; rules may block valuable work.", "Concession: “These concerns are real.”", "Rebuttal: independent expert review weighs risks and protects trust."],
             "The author strengthens the argument by admitting valid concerns and then answering them."),
     Figure(lambda t: table(t, [["Signal phrases"], ["Counterclaim: Some argue… / Critics claim… / It is true that…"], ["Concession: Admittedly… / Of course… / These concerns are real."], ["Rebuttal: However… / But… / Still, the evidence shows…"]],
                            [5.0 * inch], width=5.0 * inch)),
     KeyIdea("Strong arguments acknowledge counterclaims, concede what's valid, and rebut.")],
    [Problem("Find the concession phrase in paragraph 3.", "“Of course” / “These concerns are real.”"), Problem("Find the rebuttal signal.", "“But”"), Problem("Why include counterclaims?", "It shows fairness and makes the argument more convincing.")],
    [S("Warm-Up", [SA("Counterclaim =", "opposing argument"), SA("Rebuttal =", "response to the counterclaim")], cols=2),
     S("Analyze", [OR("Explain how paragraph 4 answers the opposing view in a memorable way.", "It honors freedom as a strength but says responsibility is equally important; ignoring responsibility could cost freedom.", lines=3)], passage=P_OPED),
     S("Write", [OR("Write a paragraph on a school issue (e.g., phones in class) that includes a counterclaim, concession, and rebuttal.", "Answers vary.", lines=8)])],
    te("Students analyze counterclaims.", "Analyze how an author distinguishes their position from that of others.", "Workbook Lesson 4.7",
       "Why mention the other side?", "Reread paragraph 3.", ["Teach signal phrases."], "Your Turn 1–3.",
       ["Ignoring counterclaims or giving up the argument."], ["CCR frame: Counterclaim, Concession, Rebuttal."], ["Debate with a family member."]),
    summary="Acknowledge, concede, rebut.")

L8 = Lesson("4.8", "Retelling from a Different Point of View",
    "I can write a narrative from a different character's point of view.", "W.7.3, RL.7.6",
    [],
    "How would Poole, the loyal butler, describe The Last Night?",
    [Text("Retelling a scene from another character's point of view requires using only what that character knows, sees, and feels, and giving them a believable voice."),
     Example("Poole's voice", "Opening line", ["First person; Poole's worry and loyalty.", "Formal speech of a Victorian butler."], "I have served Dr. Jekyll for twenty years, sir, and I never once feared to knock upon his door until this week."),
     KeyIdea("Stay within the character's knowledge; give them a distinct voice; use dialogue and sensory detail.")],
    [Problem("What can Poole NOT know?", "Jekyll's secret, until the documents are read"), Problem("What point of view should you use?", "first person as Poole"), Problem("Name a detail Poole would notice.", "the voice from the cabinet, the footsteps, the orders for chemicals")],
    [S("Warm-Up", [SA("Poole's role", "Jekyll's butler"), SA("Point of view for Poole's account", "first person")], cols=2),
     S("Write", [OR("Write Poole's account of The Last Night (12–16 sentences). Use first person, a consistent voice, dialogue, and sensory details. Do not include anything Poole couldn't know.", "Answers vary.", lines=20,
                    note="Score: consistent first-person POV (1); limited knowledge (1); voice (1); dialogue and sensory detail (1); conventions (1).")])],
    te("Students write from another point of view.", "Write narratives using effective technique and relevant details.", "Workbook Lesson 4.8",
       "Poole's version.", "Reread Chapter 8.", ["Model Poole's voice."], "Draft.",
       ["Including information Poole couldn't know."], ["Knowledge checklist."], ["Write Utterson's reply letter."], independent="Write. Weekly Check tomorrow."),
    summary="Stay inside one character's knowledge and voice.")

# ================================================================= Week 3 · Long-passage craft analysis (Chapter 9)
L9 = Lesson("4.9", "Testimony and Reliability",
    "I can evaluate a first-person narrator's reliability.", "RL.7.6, RL.7.1",
    [("testimony", "A formal statement of what someone witnessed."), ("reliable narrator", "A narrator whose account readers can trust.")],
    "Why would Stevenson let Lanyon, a rational scientist, describe the transformation?",
    [ReaderAssign(JH, "Chapter 9: Dr. Lanyon's Narrative", "What does Lanyon witness? How does it affect him?"),
     Text("Lanyon's narrative is written like <b>testimony</b>. Because he is a skeptical scientist who doubted Jekyll's theories, his shocked account is especially convincing."),
     Example("Evaluate reliability", "Is Lanyon reliable?", ["He is a respected doctor and skeptic.", "He records specific details calmly.", "His shock shows he didn't want to believe it."], "Yes; his skepticism makes his testimony more believable."),
     KeyIdea("Consider the narrator's background, motives, and tone when judging reliability.")],
    [Problem("What does Lanyon witness?", "Hyde drinking a potion and transforming into Jekyll"), Problem("Why is a skeptic a good witness?", "He wouldn't believe without proof, so his account is convincing."), Problem("What happens to Lanyon afterward?", "He is shattered and dies soon after.")],
    [S("Warm-Up", [SA("Testimony =", "a formal statement of what someone witnessed"), SA("Lanyon's profession", "doctor / scientist")], cols=2),
     S("Analyze", [OR("Find two details showing Lanyon tries to stay rational. Then find one detail showing his horror.", "Answers vary.", lines=4),
                   OR("Why is it powerful that the transformation is described by Lanyon rather than Jekyll?", "An outside skeptical witness makes the impossible believable and shows its horror from outside.", lines=3)]),
     S("Exit Ticket", [OR("Is Enfield (Chapter 1) as reliable as Lanyon? Explain.", "Answers vary; Enfield is honest but gives secondhand impressions and vague feelings.", lines=2)])],
    te("Students evaluate narrator reliability.", "Analyze points of view of narrators.", "Jekyll and Hyde Reader (Chapter 9), workbook Lesson 4.9",
       "Why Lanyon?", "Read Chapter 9.", ["Model reliability evaluation."], "Your Turn 1–3.",
       ["Assuming all narrators are reliable."], ["Background-motive-tone chart."], ["Compare to a court witness."]),
    summary="Judge reliability by background, motive, and tone.")

L10 = Lesson("4.10", "Pacing and Sentence Structure at the Climax",
    "I can analyze how sentence structure and pacing heighten a climax.", "RL.7.4, L.7.3",
    [("pacing", "The speed at which events unfold in a story.")],
    "How can sentence length make your heart beat faster?",
    [Text("At a climax, authors often slow time down with detail or speed it up with short, sharp sentences. Long, building sentences create tension; a sudden short sentence delivers shock."),
     Example("Analyze pacing", "“The house was silent. Wind pressed against the windows, and somewhere upstairs a floorboard creaked, slow and deliberate, as though someone heavy were shifting from one foot to the other, waiting. Then the lights went out.”",
             ["The long middle sentence stretches time with sound details, building tension.", "The final short sentence arrives suddenly.", "Effect: the reader's tension breaks into shock."],
             "A long, building sentence followed by a short one creates a sudden shock at the climax."),
     KeyIdea("Long sentences build; short sentences strike. Paragraph breaks control pace.")],
    [Problem("Effect of a one-sentence paragraph", "emphasis, shock, a turning point"), Problem("Effect of detailed slow description at a climax", "stretches time and builds tension"), Problem("What is pacing?", "the speed at which events unfold")],
    [S("Warm-Up", [SA("Short sentences create…", "shock, urgency"), SA("Long sentences can…", "build tension")], cols=2),
     S("Analyze Chapter 9", [OR("Find a passage in Lanyon's narrative where Stevenson slows down or speeds up time. Copy a phrase and explain the effect.", "Answers vary.", lines=5)]),
     S("Write", [OR("Write a climactic paragraph (any story) using long building sentences followed by a short, shocking one.", "Answers vary.", lines=6)])],
    te("Students analyze pacing.", "Analyze the impact of sentence structure; use language for effect.", "Workbook Lesson 4.10",
       "Heartbeat sentences.", "Reread the transformation scene.", ["Model the pacing analysis."], "Your Turn 1–3.",
       ["Noticing length but not effect."], ["Mark long and short sentences."], ["Rewrite a scene at a different pace."]),
    summary="Pacing and sentence length heighten climaxes.")

L11 = Lesson("4.11", "Symbolism",
    "I can analyze symbols and explain how they develop a theme.", "RL.7.2, RL.7.4",
    [("symbol", "An object, place, or person that stands for a larger idea.")],
    "What might the door in Chapter 1 represent?",
    [Figure(lambda t: table(t, [["Symbol", "Possible meaning"], ["the shabby back door", "Jekyll's hidden, secret self"], ["Jekyll's respectable front entrance", "his public reputation"], ["fog", "secrecy, confusion, moral murkiness"],
                                ["the potion", "the temptation to escape responsibility"], ["the mirror in Jekyll's cabinet", "self-knowledge; facing one's true nature"]], [2.2 * inch, 3.4 * inch], width=5.6 * inch)),
     Example("Analyze a symbol", "The two entrances to Jekyll's house", ["Front: elegant, respectable.", "Back: neglected, used by Hyde.", "Both lead to the same house."],
             "The two entrances symbolize Jekyll's divided self: one respectable face, one hidden, both belonging to the same man."),
     KeyIdea("Symbols are concrete objects that stand for abstract ideas; connect them to themes.")],
    [Problem("What does fog symbolize?", "secrecy, confusion"), Problem("Why is it important that both doors lead to one house?", "Jekyll and Hyde are one person."), Problem("What is a symbol?", "an object that stands for a larger idea")],
    [S("Warm-Up", [SA("A symbol is concrete or abstract?", "concrete (stands for abstract)"), SA("Fog symbolizes…", "secrecy, confusion")], cols=2),
     S("Analyze", [OR("Choose a symbol from the chart. Explain how it develops the theme of duality, with evidence.", "Answers vary.", lines=6)]),
     S("Exit Ticket", [OR("Propose your own symbol from the novel not on the chart and explain it.", "Answers vary, e.g. the cane: violence; the will: control.", lines=2)])],
    te("Students analyze symbols.", "Determine a theme and analyze its development; analyze word choice.", "Workbook Lesson 4.11",
       "The door.", "Revisit the door description.", ["Model the two-entrance symbol."], "Your Turn 1–3.",
       ["Making every object a symbol."], ["Is it repeated or emphasized?"], ["Draw a symbolic image of Jekyll and Hyde."]),
    summary="Symbols connect concrete details to abstract themes.")

L12 = Lesson("4.12", "Writing a Craft Analysis Paragraph",
    "I can write an analysis of how an author's craft creates meaning.", "W.7.9a, W.7.2",
    [],
    "Which of Stevenson's techniques is most effective?",
    [Text("A craft analysis names a technique, gives an example, and explains its effect on the reader and the meaning: <i>Technique → Example → Effect</i>."),
     Example("TEE paragraph", "Technique: delayed revelation", ["Technique: Stevenson delays the truth through sealed documents.", "Example: Lanyon's letter must not be opened until Jekyll's death.", "Effect: readers share Utterson's frustration, heightening suspense."],
             "Stevenson builds suspense by delaying the truth through sealed documents. When Lanyon gives Utterson a letter that must not be opened until Jekyll's death or disappearance, readers, like Utterson, are forced to wait. This delay makes the final revelation in Chapters 9 and 10 far more shocking."),
     KeyIdea("Technique → example → effect, connected to meaning.")],
    [Problem("What does TEE stand for?", "Technique, Example, Effect"), Problem("Name a Stevenson technique.", "delayed revelation, symbolism, limited POV, diction"), Problem("What must the effect connect to?", "the reader and the meaning/theme")],
    [S("Warm-Up", [SA("Technique example", "symbolism"), SA("Effect is on…", "the reader and meaning")], cols=2),
     S("Write", [OR("Write a TEE paragraph analyzing one of Stevenson's techniques from Chapters 1–9.", "Answers vary.", lines=12, note="Score: technique (1), example (1), integrated quote (1), effect (1), conventions (1).")])],
    te("Students write craft analyses.", "Draw evidence; write analytically.", "Workbook Lesson 4.12",
       "Most effective technique.", "List techniques studied.", ["Model TEE."], "Plan.",
       ["Naming a technique without effect."], ["TEE frame."], ["Analyze two techniques."], independent="Write. Weekly Check tomorrow."),
    summary="Technique, example, effect.")

# ================================================================= Week 4 · Compare craft across texts (Chapter 10)
L13 = Lesson("4.13", "The Confession and the Theme of Duality",
    "I can analyze how the final chapter develops the novel's central theme.", "RL.7.2, RL.7.1",
    [("duality", "Having two sides or natures.")],
    "Is Hyde truly a different person from Jekyll?",
    [ReaderAssign(JH, "Chapter 10: Henry Jekyll's Full Statement of the Case", "What did Jekyll hope to achieve? Why did he lose control?"),
     P_TWO,
     Example("Analyze theme", "What does Jekyll's statement reveal?", ["Jekyll believed he could separate his good and evil sides.", "He enjoyed being Hyde, free of consequences.", "Hyde grew stronger until Jekyll could no longer control the change."],
             "Theme: Every person has both good and evil within, and trying to escape responsibility for our darker side can destroy us."),
     KeyIdea("The final chapter reveals and completes the theme of duality.")],
    [Problem("What did Jekyll want to separate?", "his good and evil natures"), Problem("Why did he lose control?", "Hyde grew stronger; the transformations happened without the potion; the ingredient ran out"), Problem("State the theme in your own words.", "Everyone has good and bad in them; denying responsibility leads to destruction.")],
    [S("Warm-Up", [SA("Duality =", "having two sides"), SA("Who wrote the final statement?", "Henry Jekyll")], cols=2),
     S("Analyze", [OR("What does “man is not truly one, but truly two” mean? Do you agree?", "People have conflicting sides within them; answers vary on agreement.", lines=3),
                   OR("Trace how the duality theme develops from Chapter 1 to Chapter 10. Cite three moments.", "Answers vary: door (ch1), handwriting (ch5), transformation (ch9), statement (ch10).", lines=6)], passage=P_TWO),
     S("Exit Ticket", [OR("Was Jekyll responsible for Hyde's crimes? Explain.", "Answers vary; most argue yes.", lines=2)])],
    te("Students analyze the final chapter's theme.", "Determine a theme and analyze its development.", "Jekyll and Hyde Reader (Chapter 10), workbook Lesson 4.13",
       "Different person?", "Read Chapter 10.", ["Model theme analysis."], "Your Turn 1–3.",
       ["Thinking Hyde is purely a separate person."], ["Theme timeline."], ["Debate Jekyll's responsibility."]),
    summary="The confession completes the theme of duality.")

L14 = Lesson("4.14", "Comparing Narrators Across the Novel",
    "I can compare how different narrators reveal the story and why the author arranged them this way.", "RL.7.6, RL.7.5",
    [],
    "Why does Stevenson save Jekyll's own voice for last?",
    [Figure(lambda t: table(t, [["Narrator / perspective", "What they know", "Effect"], ["Enfield (Ch. 1)", "an incident and a feeling of disgust", "introduces the mystery"], ["Utterson (limited 3rd)", "clues, suspicions", "builds suspense; reader as detective"],
                                ["Lanyon (Ch. 9)", "the transformation, witnessed", "shock and proof"], ["Jekyll (Ch. 10)", "everything, from inside", "explanation and confession"]], [1.6 * inch, 2.0 * inch, 2.0 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Stevenson moves from outside to inside: from rumor, to investigation, to witness, to confession.")],
    [Problem("Which narrator gives the inside view?", "Jekyll"), Problem("Why save Jekyll for last?", "to keep the mystery until the end; the confession explains everything"), Problem("What role does the reader play during Utterson's sections?", "detective")],
    [S("Warm-Up", [SA("First outside view", "Enfield"), SA("Final inside view", "Jekyll")], cols=2),
     S("Compare", [OR("Compare Lanyon's narrative and Jekyll's statement. How do they describe the transformation differently?", "Lanyon: horrified outside observer; Jekyll: inside experience, feelings, motives.", lines=4),
                   OR("Explain why the outside-to-inside structure is effective.", "It mirrors a detective solving a case and saves the deepest truth for last.", lines=3)]),
     S("Exit Ticket", [OR("Which perspective did you find most powerful? Why?", "Answers vary.", lines=2)])],
    te("Students compare narrators.", "Analyze how an author develops and contrasts points of view.", "Workbook Lesson 4.14",
       "Jekyll's voice last.", "Skim Chapters 1, 9, 10.", ["Model the chart."], "Your Turn 1–3.",
       ["Summarizing each narrator without comparing."], ["Outside → inside arrow."], ["Rewrite the novel's order."]),
    summary="Narrators move from outside to inside.")

L15 = Lesson("4.15", "Fiction and History: Self-Experimentation",
    "I can compare a fictional portrayal with historical accounts.", "RL.7.9, RI.7.9",
    [("self-experimentation", "A scientist testing a procedure or substance on themselves.")],
    "Did real scientists ever test dangerous ideas on themselves?",
    [P_SELF,
     Figure(lambda t: table(t, [["", "Jekyll (fiction)", "Forssmann and Marshall (history)"], ["Goal", "to separate good and evil", "to prove a medical idea"], ["Method", "a secret potion", "a catheter; drinking bacteria"],
                                ["Result", "loses control; destruction", "risky but useful discoveries; Nobel Prizes"], ["Shared idea", "willingness to take personal risk", "willingness to take personal risk"]], [1.0 * inch, 2.3 * inch, 2.4 * inch], width=5.7 * inch, font_size=9)),
     KeyIdea("Compare how fiction and history portray a similar topic; notice what fiction exaggerates or changes for its purpose.")],
    [Problem("What did Forssmann do?", "inserted a tube into his own vein to his heart (1929)"), Problem("What did Marshall do?", "drank bacteria to show they cause stomach illness (1984)"), Problem("What protects research volunteers today?", "ethics committees")],
    [S("Warm-Up", [SA("Self-experimentation =", "testing on oneself"), SA("Nobel year for Marshall and Warren", "2005")], cols=2),
     S("Compare", [OR("How are Jekyll's and the real doctors' motives different?", "Jekyll wanted personal escape/pleasure; the real doctors wanted to prove medical ideas that could help others.", lines=3),
                   OR("Why might Stevenson's story end in disaster while the real stories led to discoveries?", "Fiction warns about unchecked ambition and moral danger; the real experiments were narrow and aimed at verifiable knowledge.", lines=3),
                   OR("Does the informational text present self-experimentation as heroic, reckless, or both? Cite evidence.", "Both: important discoveries (Nobel) but serious harm and misleading results; ethics committees now protect volunteers.", lines=3)], passage=P_SELF),
     S("Exit Ticket", [OR("Connect “Should Science Have Limits?” to these texts in one sentence.", "Answers vary.", lines=2)])],
    te("Students compare fiction and history.", "Compare a fictional portrayal and a historical account of the same period or topic; analyze how authors shape facts.", "Workbook Lesson 4.15",
       "Real self-experimenters?", "Read “Scientists Who Experimented on Themselves.”", ["Model the comparison chart."], "Your Turn 1–3.",
       ["Treating fiction as history."], ["Fiction/history T-chart."], ["Research another self-experimenting scientist."]),
    summary="Fiction exaggerates and warns; history records outcomes.")

L16 = Lesson("4.16", "Writing a Comparative Analysis",
    "I can write a comparative analysis of a fictional and an informational text.", "W.7.2, W.7.9",
    [],
    "What can Jekyll's story teach us about real science?",
    [Text("A comparative analysis has a thesis that names both texts and the point of comparison, body paragraphs organized point by point, integrated evidence from both texts, and a conclusion about what the comparison reveals."),
     Example("Thesis", "Compare Jekyll with Forssmann and Marshall.", ["Name both texts.", "Point of comparison: risk and responsibility."],
             "Both Stevenson's Dr. Jekyll and the real doctors Forssmann and Marshall risked their own bodies for knowledge, but while their experiments advanced medicine, Jekyll's selfish secrecy shows how ambition without responsibility leads to ruin."),
     KeyIdea("Name both texts, compare point by point, integrate evidence, and explain what the comparison reveals.")],
    [Problem("What must the thesis name?", "both texts and the point of comparison"), Problem("Which structure works well?", "point by point"), Problem("What does the conclusion explain?", "what the comparison reveals")],
    [S("Warm-Up", [SA("Point-by-point means…", "comparing on one point at a time"), SA("A comparison transition", "similarly, however, unlike")], cols=2),
     S("Write", [OR("Write a comparative analysis (3–4 paragraphs) of Strange Case of Dr. Jekyll and Mr. Hyde and “Scientists Who Experimented on Themselves.”", "Answers vary.", lines=24,
                    note="Score: thesis (1); evidence from novel (1); evidence from article (1); point-by-point analysis (1); conclusion and conventions (1).")])],
    te("Students write comparative analyses.", "Write informative texts; draw evidence from literary and informational texts.", "Workbook Lesson 4.16, Unit 4 Review",
       "Jekyll and real science.", "Review both texts.", ["Model the thesis."], "Plan.",
       ["Writing about one text at a time without comparing."], ["Point-by-point outline."], ["Add a third text (the op-ed)."], independent="Draft; then the Unit 4 Review.", exit_="Tomorrow: Unit 4 Test."),
    summary="Comparative analysis: thesis, point by point, both texts, significance.")

# ================================================================= checks
C1 = Check("Weekly Check 10: Word Choice and Structure", [S("Read and answer", [
    OR("Copy three words or phrases that create an eerie mood.", "sagged; chained shut; broken ticket booth; flicker of light; faint, tinny, impossibly old music", lines=2),
    OR("What is the tone of the passage?", "mysterious, ominous", lines=1),
    OR("How does the structure (short second paragraph) affect suspense?", "It shifts suddenly from abandonment to a sign of life, raising questions and ending on a mystery.", lines=2),
    OR("What does “impossibly old” suggest?", "The music seems to come from the theater's past, as if supernatural.", lines=2),
    MC("The word “tinny” has a connotation that is…", ["rich and full", "thin and metallic", "loud and joyful"], 1)], passage=P_C10)], minutes=20)
C2 = Check("Weekly Check 11: Point of View", [S("Read and answer", [
    OR("How do Sam's and Nate's points of view differ about the same day?", "Sam thinks it was the best day and Nate likes him; Nate was forced to go and annoyed.", lines=2),
    OR("What does the reader know that Sam doesn't?", "Nate was made to go and missed a party.", lines=2),
    OR("What is this an example of?", "dramatic irony", lines=1),
    OR("How does Nate's attitude change by the end? Cite evidence.", "He softens: “his face lit up like fireworks… Maybe it wasn't the worst day.”", lines=2),
    OR("Explain the simile “his face lit up like fireworks.”", "Sam's face showed sudden, bright joy.", lines=1)], passage=P_C11)], minutes=20)
C3 = Check("Weekly Check 12: Symbolism and Craft", [S("Read and answer", [
    OR("What does the locket symbolize?", "the grandmother's hidden strength / her legacy of courage", lines=2),
    OR("Why is the single word “Brave” more powerful than a long message?", "Its brevity matches the grandmother's quiet strength and lets memories fill in the meaning.", lines=2),
    OR("What does Rosa's final action suggest?", "She accepts her grandmother's legacy and will carry that courage herself.", lines=2),
    OR("Write a TEE sentence about the author's use of the locket.", "e.g. The author uses the locket as a symbol; when Rosa wears it, it shows courage passing to the next generation.", lines=2)], passage=P_C12)], minutes=20)

REVIEW = Check("Unit 4 Review", [
    S("Concepts", [SA("Tone vs mood", "author's attitude vs reader's feeling"), SA("Dramatic irony", "readers know more than a character"), SA("Concession", "admitting part of the other side is valid"),
                   SA("Symbol", "object representing an idea"), SA("TEE", "Technique, Example, Effect"), SA("Reliable narrator", "a narrator readers can trust")], cols=2),
    S("Apply", [OR("Explain how Stevenson's arrangement of narrators builds the mystery.", "outside to inside: rumor, investigation, witness, confession; truth saved for last", lines=3),
                OR("Write a thesis comparing Jekyll with a real self-experimenting scientist.", "Answers vary.", lines=2)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 4 Test", [
    S("Part A · Word choice and structure (1 point each)", [
        OR("What does the phrase “No one noticed” reveal about Priya's situation?", "She felt invisible and unappreciated despite her hard work.", lines=2),
        OR("Explain the effect of the one-sentence paragraph “Then, on opening night, Madison lost her voice.”", "It creates a sudden turning point and shock.", lines=2),
        OR("Explain the metaphor “her heart… a drum in an empty room.”", "Her heartbeat was loud and echoing; she was nervous and alone.", lines=2),
        OR("How does the author's diction in paragraph 3 create a tense mood? Cite two words.", "chaos, paced, whispered, hammering", lines=2),
        OR("Explain the simile “as naturally as breathing.”", "The lines came effortlessly because she knew them so well.", lines=1)], passage=P_TEST),
    S("Part B · Point of view and symbolism (1 point each)", [
        MC("The story is told from…", ["first person (Priya)", "limited third person (following Priya)", "Madison's point of view"], 1),
        OR("What does the reader know about Priya that the other characters don't?", "She has mouthed every line for six weeks and knows the part better than anyone.", lines=2),
        OR("What does light symbolize in the story? Cite the beginning and the end.", "recognition/being seen: she watched from the dark back row; at the end she stands “in her own light.”", lines=3, points=2),
        OR("How does Madison's line “You were the role” develop the theme?", "Even the star recognizes Priya's talent; being prepared lets you shine when the moment comes.", lines=2)]),
    S("Part C · Theme (1 point each)", [
        OR("State a theme.", "e.g. Quiet preparation allows people to rise when opportunity comes.", lines=2),
        OR("How does Priya change from beginning to end?", "From invisible and overlooked to confident and recognized.", lines=2)]),
    S("Part D · Craft analysis (5 points)", [OR("Write a TEE analysis (two paragraphs) of how the author uses two techniques (for example, pacing, metaphor, symbolism, diction) to show Priya's transformation.",
                                               "Rubric: technique 1 with example and effect (2); technique 2 with example and effect (2); conventions and integrated quotations (1).", lines=16, points=5)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-01-25", "2027-02-01", "2027-02-08", "2027-02-15"], CHECKS, REVIEW, TEST)

UNIT = Unit(4, "Craft and Perspective", "Word choice and tone, structure and delayed revelation, point of view and purpose, symbolism, and comparing fiction with history, with Strange Case of Dr. Jekyll and Mr. Hyde, Chapters 5–10.",
    "The mystery deepens, the truth is revealed, and Stevenson's craft comes into full view. You'll analyze how word choice creates tone, how documents and delays build suspense, how point of view controls what we know, and how symbols carry the novel's theme of duality. Then you'll compare Jekyll's fictional experiment with real scientists who experimented on themselves.",
    ["Analyze diction, tone, and mood; analyze structure and pacing.", "Analyze point of view, dramatic irony, reliability, and arguments with counterclaims.",
     "Analyze symbols and theme development.", "Compare fiction with historical accounts; write craft and comparative analyses."],
    [("RL.7.2, RL.7.4–6, RL.7.9", "Theme; word choice; structure; point of view; compare fiction and history."), ("RI.7.3–6, RI.7.8–9", "Analyze structure, technical words, author's point of view, arguments, and multiple texts."),
     ("W.7.2, W.7.3, W.7.9", "Write analyses and narratives from different points of view."), ("L.7.3, L.7.5c, L.7.6", "Use language for effect; connotation; academic vocabulary.")],
    [("tone", "The author's attitude."), ("dramatic irony", "Readers know more than a character."), ("symbol", "An object that represents an idea."), ("duality", "Having two sides."), ("counterclaim", "An opposing argument.")],
    ["Unit 3: Jekyll and Hyde Chapters 1–4."], ["Strange Case of Dr. Jekyll and Mr. Hyde Reader (Chapters 5–10)"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Analyzing tone, perspective, and argument helps you read news, reviews, and debates critically, and the question of science's limits is debated today.",
    family_note="Discuss at dinner: Is there a “Mr. Hyde” side in everyone? What helps people choose their better side?",
    weeks=WEEKS)
