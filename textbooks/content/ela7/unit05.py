"""Grade 7 ELA · Unit 5: Modifiers and Precise Description — adjectives, adverbs, comparison, modifier placement, prepositions, interjections, conjunctions, and a science-fiction scene.
Anchor reading: The Time Machine Reader, Chapters 1–4 (Feb 22 – Mar 26, 2027)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule

TM = "The Time Machine Reader"


def rules(rows, widths, fs=9.5):
    return Figure(lambda t: table(t, rows, [w * inch for w in widths], width=sum(widths) * inch, font_size=fs))


P_OPEN = Passage("From The Time Machine, Chapter 1 (original 1895 text)", [
    "The Time Traveller (for so it will be convenient to speak of him) was expounding a recondite matter to us. His grey eyes shone and twinkled, and his usually pale face was flushed and animated.",
], source="H. G. Wells, The Time Machine (1895). Public domain.", genre="Classic novel excerpt", numbered=False)

P_FOURTH = Passage("What Is the Fourth Dimension?", [
    "We usually describe space with three <b>dimensions</b>: length, width, and height. A shoebox, for example, is a certain number of inches long, wide, and tall. To find any point inside it, you need exactly three measurements.",
    "But objects also exist in <b>time</b>. A shoebox that sits on a shelf for ten years has a past and a future as well as a size. Scientists and writers have long wondered whether time might be thought of as a fourth dimension, one that we move through steadily in one direction.",
    "In 1895, H. G. Wells imagined a machine that could travel along this fourth dimension as easily as a train travels along a track. Ten years later, the physicist Albert Einstein published his theory of special relativity, which treats space and time as closely connected, and which soon led scientists to describe the universe as four-dimensional “spacetime.”",
    "Einstein's work showed that time is not the same for everyone: a clock moving very fast ticks more slowly than one at rest. This effect is tiny at everyday speeds but measurable. Satellites in the GPS system must correct their clocks for it, or the maps on our phones would quickly become inaccurate.",
], source="An original informational text", genre="Science text")

P_SENSE = Passage("The First Jump", [
    "Mara gripped the brass lever with both hands. The machine hummed softly, then louder, until the whole laboratory trembled. She took a long breath and pushed.",
    "Instantly, the room dissolved. Sunlight and darkness flickered across the walls faster than she could blink, day and night racing like the pages of a book flipped by an impatient thumb. The plant on the windowsill shot upward, bloomed, withered, and crumbled into dust. Outside, buildings rose like mushrooms after rain, then sagged, then vanished.",
    "Her stomach lurched. Wow! she thought, half terrified and half thrilled. She pulled the lever back, gently, carefully, and the flickering slowed to a dizzy blur.",
], source="An original science-fiction story", genre="Science fiction")

P_C13 = Passage("The Abandoned Observatory", [
    "The old stone observatory stood alone on the windswept hill. Its huge copper dome, green with age, had not opened in decades. Inside, a dusty, enormous telescope pointed silently at a sky it could no longer see.",
    "Tess climbed the narrow spiral stairs slowly and carefully. At the top, she wiped the grime from a small brass plaque. It read: <i>For those who look up.</i>",
], source="An original story", genre="Realistic fiction")

P_C14 = Passage("Faster, Smaller, Cheaper", [
    "In 1946, one of the first electronic computers, ENIAC, filled a large room and weighed about thirty tons. It was faster than any earlier calculating machine, but it used thousands of glowing vacuum tubes that often burned out.",
    "Today, a smartphone that fits in your pocket is millions of times more powerful. Computers have become faster, smaller, and cheaper with each generation.",
], source="An original informational text", genre="Informational text")

P_C15 = Passage("The Message", [
    "Oh no! The signal from the probe had stopped. For three tense hours, the engineers stared at their screens, but nothing came through the static.",
    "Then, just before midnight, a faint beep sounded across the control room. Hooray! The probe was alive, and its first photos of the distant moon were on their way.",
], source="An original story", genre="Realistic fiction")

P_TEST = Passage("The Last Library", [
    "In the year 2340, the city of New Aldora had no books. Information floated in the air as shimmering holograms, appearing instantly whenever anyone spoke a question. Paper had not been made for two hundred years.",
    "Twelve-year-old Ren had never touched a book until the afternoon she followed a stray cat through a crumbling doorway at the edge of the old district. Inside, dust drifted lazily through slanted beams of sunlight. Shelves stretched from the cracked marble floor to the high, arched ceiling, and every shelf was crowded with books: thick ones, thin ones, leather-bound ones with gold letters worn nearly smooth.",
    "Ren pulled one down carefully. The pages were yellow and fragile, and they smelled like old wood and rain. She sat on the floor and read until the light faded completely. The story did not appear instantly. She had to wait for it, page by page, and somehow the waiting made it better.",
    "The next day, Ren came back. The day after that, she brought her best friend, Kai, who rolled his eyes until he opened a book of maps and fell silent for an hour. By the end of the month, a small, curious group of children met in the old library every afternoon, reading quietly, arguing loudly, and dusting the shelves with surprising care.",
], source="An original science-fiction story", genre="Science fiction")

# ================================================================= Week 1 · Adjectives and adverbs (Chapter 1)
L1 = Lesson("5.1", "Science Fiction and the Frame Narrative",
    "I can analyze the elements of science fiction and how a frame narrative shapes a story.", "RL.7.3, RL.7.5",
    [("science fiction", "Fiction that imagines how science and technology might change the world."), ("narrator", "The voice telling the story.")],
    "If you could travel in time, would you go to the past or the future? Why?",
    [ReaderAssign(TM, "Chapter 1: The Inventor", "What does the Time Traveller explain to his guests? How do they react?"),
     Text("<i>The Time Machine</i> (1895) by H. G. Wells helped invent modern science fiction. Like <i>Jekyll and Hyde</i>, it uses a frame: an unnamed narrator describes the Time Traveller's dinner guests and then retells the Traveller's own story."),
     P_OPEN,
     Example("Analyze the opening", "What do we learn in the first two sentences?", ["The narrator doesn't name the Time Traveller.", "“Recondite” means obscure or difficult.", "Shining eyes and flushed face show excitement."],
             "The Traveller is an enthusiastic, brilliant scientist explaining a difficult idea to his guests."),
     KeyIdea("Science fiction imagines scientific possibilities; a frame narrator filters the Traveller's story through a listener.")],
    [Problem("What does “recondite” mean?", "obscure, difficult to understand"), Problem("Why might the narrator not name the Time Traveller?", "to keep him mysterious / focus on his role"), Problem("How do the guests react to his ideas?", "skeptical, doubtful")],
    [S("Warm-Up", [SA("Author of The Time Machine", "H. G. Wells"), SA("Year published", "1895")], cols=2),
     S("Analyze Chapter 1", [OR("What evidence does the Time Traveller give for a fourth dimension? How do the guests respond?", "Answers vary; he argues time is a dimension like length, width, height; the guests are doubtful.", lines=4),
                             OR("Compare the frame narrative here with Jekyll and Hyde's.", "Both filter the story through observers and delay the main character's own account.", lines=3)], passage=P_OPEN),
     S("Exit Ticket", [OR("Which guest would you be: believer or skeptic? Why?", "Answers vary.", lines=2)])],
    te("Students analyze science fiction and frames.", "Analyze how elements interact; analyze structure.", "The Time Machine Reader (Chapter 1), workbook Lesson 5.1",
       "Past or future?", ["Read Chapter 1.", "Read Wells's original opening."], ["Teach sci-fi elements."], "Your Turn 1–3.",
       ["Assuming sci-fi is not literature."], ["Genre chart."], ["List modern technology predicted by sci-fi."]),
    summary="Science fiction imagines scientific possibilities; the frame filters the story.")

L2 = Lesson("5.2", "Adjectives: Proper, Compound, and Coordinate",
    "I can use proper, compound, and coordinate adjectives with correct punctuation.", "L.7.2a, L.7.1",
    [("coordinate adjectives", "Two or more adjectives that equally describe a noun; separated by a comma."), ("compound adjective", "Two or more words joined to act as one adjective, often hyphenated.")],
    "Should there be a comma in “a dusty enormous telescope”?",
    [rules([["Type", "Example", "Rule"], ["proper adjective", "a Victorian house, an English scientist", "capitalize"], ["compound adjective before a noun", "a well-known inventor, a time-traveling machine", "hyphenate"],
            ["coordinate adjectives", "a cold, dark night", "comma (could use “and”; order can switch)"], ["cumulative adjectives", "a large brass lever", "no comma (can't use “and”; order fixed)"]], (1.8, 2.3, 1.7), fs=9),
     Example("Comma test", "a dusty enormous telescope", ["Test 1: a dusty and enormous telescope? Sounds fine.", "Test 2: an enormous, dusty telescope? Sounds fine.", "Both pass → coordinate → comma."], "a dusty, enormous telescope"),
     KeyIdea("If you can add “and” or switch the order, use a comma. Hyphenate compound adjectives before nouns. Capitalize proper adjectives.")],
    [Problem("Comma? “a bright shiny lever”", "Yes: a bright, shiny lever"), Problem("Comma? “three old books”", "No (cumulative)"), Problem("Fix: a well known scientist", "a well-known scientist")],
    [S("Warm-Up", [SA("Proper adjective from England", "English"), SA("Coordinate adjective test", "add “and” / switch the order")], cols=2),
     S("Punctuate", [SA(q, a) for q, a in [("a long dark hallway", "a long, dark hallway"), ("the little red machine", "the little red machine (no comma)"), ("a twenty year old house", "a twenty-year-old house"),
                                          ("a french inventor", "a French inventor"), ("a strange glowing light", "a strange, glowing light"), ("a high tech lab", "a high-tech lab")]], cols=2),
     S("Exit Ticket", [OR("Describe the Time Machine in a sentence with coordinate adjectives and a compound adjective.", "e.g. The gleaming, delicate machine had a quartz-and-brass frame.", lines=2)])],
    te("Students punctuate adjectives.", "Use a comma to separate coordinate adjectives.", "Workbook Lesson 5.2",
       "Comma or not?", "Find adjectives in Chapter 1.", ["Teach the tests."], "Your Turn 1–3.",
       ["Commas between cumulative adjectives."], ["And/switch tests."], ["Describe five objects at home."]),
    summary="Comma for coordinate adjectives; hyphens for compound adjectives; capitals for proper adjectives.")

L3 = Lesson("5.3", "Adverbs and Their Placement",
    "I can use adverbs to modify verbs, adjectives, and other adverbs and place them for clarity.", "L.7.1",
    [("adverb", "A word that modifies a verb, adjective, or another adverb, telling how, when, where, or to what extent.")],
    "What's the difference between “She only touched the lever” and “Only she touched the lever”?",
    [rules([["Modifies", "Example"], ["a verb", "The machine hummed softly."], ["an adjective", "The laboratory was extremely quiet."], ["another adverb", "She pulled the lever very gently."]], (1.6, 3.6)),
     Example("Placement changes meaning", "only", ["Only she touched the lever. (no one else did)", "She only touched the lever. (she didn't pull it)", "She touched only the lever. (nothing else)"], "Place limiting adverbs (only, just, almost, nearly) right before what they modify."),
     KeyIdea("Adverbs tell how, when, where, or to what extent. Place limiting adverbs carefully.")],
    [Problem("Adverb in “The guests laughed nervously.”", "nervously (modifies laughed)"), Problem("What does “very” modify in “very gently”?", "gently (an adverb)"), Problem("Meaning: “I almost read the whole book.”", "I didn't read it; I nearly did.")],
    [S("Warm-Up", [SA("Adverbs often end in…", "-ly"), SA("Adverbs tell how, when, where, or…", "to what extent")], cols=2),
     S("Find and Explain", [SA(q, a) for q, a in [("The Traveller spoke quite seriously.", "quite → seriously; seriously → spoke"), ("Yesterday the machine vanished.", "Yesterday → vanished (when)"),
                                                  ("The model was incredibly small.", "incredibly → small"), ("They waited outside.", "outside → waited (where)")]], cols=1),
     S("Placement", [OR("Write two sentences using “just” in different places so the meanings differ. Explain each.", "e.g. Just Mara pushed the lever (only Mara). Mara just pushed the lever (a moment ago).", lines=3)])],
    te("Students use and place adverbs.", "Demonstrate command of grammar; place modifiers for clarity.", "Workbook Lesson 5.3",
       "Only she vs she only.", "Find adverbs in Chapter 1.", ["Teach functions and placement."], "Your Turn 1–3.",
       ["Overusing very and really."], ["Replace very + adjective with one strong word."], ["Rewrite sentences moving “only.”"]),
    summary="Adverbs tell how, when, where, extent; placement matters.")

L4 = Lesson("5.4", "How Modifiers Create Description",
    "I can analyze how an author's modifiers create vivid description and tone.", "RL.7.4, L.7.3",
    [],
    "What do “shone and twinkled” and “flushed and animated” tell you about the Time Traveller?",
    [Text("Modifiers do the heavy lifting in description. Ask: Which modifiers stand out? What image or feeling do they create? How do they shape the reader's view of the character or scene?"),
     Example("Analyze Wells's modifiers", "“His grey eyes shone and twinkled, and his usually pale face was flushed and animated.”",
             ["“usually pale”: the adverb tells us this is unusual excitement.", "“flushed and animated”: pairs of adjectives show energy.", "“shone and twinkled”: verbs pair with light imagery."],
             "Wells's modifiers show a normally quiet scientist made radiant by excitement about his idea."),
     KeyIdea("Analyze specific modifiers: what image, what feeling, what effect on the reader.")],
    [Problem("What does “usually” tell us?", "His flushed face is unusual; he's especially excited."), Problem("What tone do the modifiers create?", "enthusiastic, energetic"), Problem("Name a modifier that is an adverb.", "usually")],
    [S("Warm-Up", [SA("Adjectives modify…", "nouns"), SA("Adverbs modify…", "verbs, adjectives, adverbs")], cols=2),
     S("Analyze", [OR("Choose a descriptive passage from Chapter 1 of the Reader. Copy four modifiers and explain the effect of each.", "Answers vary.", lines=6)]),
     S("Exit Ticket", [OR("Rewrite Wells's sentence with modifiers that make the Time Traveller seem nervous instead.", "e.g. His grey eyes darted anxiously, and his usually calm face was pale and strained.", lines=2)])],
    te("Students analyze modifiers in description.", "Analyze word choice; use language for effect.", "Workbook Lesson 5.4",
       "Shone and twinkled.", "Reread the opening.", ["Model the analysis."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Listing modifiers without effects."], ["Modifier → image → effect chart."], ["Describe a family member's excitement."]),
    summary="Modifiers create images and tone.")

# ================================================================= Week 2 · Modifiers and comparison (Chapter 2)
L5 = Lesson("5.5", "Comparative and Superlative Forms",
    "I can use comparative and superlative forms correctly, including irregular forms and fewer/less.", "L.7.1",
    [("comparative", "Compares two things: faster, more careful."), ("superlative", "Compares three or more: fastest, most careful.")],
    "Is the Time Machine “more faster” than a train?",
    [ReaderAssign(TM, "Chapter 2: The Machine", "What happens to the small model machine? How do the guests explain it?"),
     rules([["Rule", "Comparative", "Superlative"], ["one syllable: -er, -est", "faster", "fastest"], ["most two+ syllables: more, most", "more careful", "most careful"], ["two syllables ending in -y: -ier, -iest", "happier", "happiest"],
            ["irregular good/well", "better", "best"], ["irregular bad/badly", "worse", "worst"], ["irregular many/much", "more", "most"]], (2.4, 1.6, 1.6), fs=9),
     Text("<b>Fewer</b> is for things you can count (fewer guests); <b>less</b> is for amounts you can't count (less time). Never double up: <i>more faster</i> is incorrect."),
     KeyIdea("Comparative for two, superlative for three or more; no double comparisons; fewer for countable, less for uncountable.")],
    [Problem("Correct: The model was (smaller/smallest) of the two machines.", "smaller"), Problem("Correct: (Fewer/Less) people believed him.", "Fewer"), Problem("Correct: This is the (baddest/worst) storm.", "worst")],
    [S("Warm-Up", [SA("Comparative of good", "better"), SA("Superlative of bad", "worst")], cols=2),
     S("Choose the Form", [SA(q, a) for q, a in [("The Traveller was the (more/most) curious of all the guests.", "most"), ("Of the two clocks, this one is (more accurate/most accurate).", "more accurate"),
                                                 ("We have (fewer/less) time than we thought.", "less"), ("She felt (worse/worser) after the jump.", "worse"), ("It was the (happiest/most happiest) day.", "happiest"),
                                                 ("There are (fewer/less) books in the city now.", "fewer")]], cols=2),
     S("Exit Ticket", [OR("Compare the model machine and the full-size machine in two sentences using comparative and superlative forms.", "Answers vary.", lines=2)])],
    te("Students use comparative and superlative forms.", "Demonstrate command of grammar.", "The Time Machine Reader (Chapter 2), workbook Lesson 5.5",
       "More faster?", "Read Chapter 2.", ["Teach the chart; fewer/less."], "Your Turn 1–3.",
       ["Double comparisons."], ["Count it? fewer."], ["Find fewer/less errors on signs."]),
    summary="Comparatives for two, superlatives for more; fewer vs less.")

L6 = Lesson("5.6", "Phrases and Clauses as Modifiers",
    "I can use adjective and adverb clauses and phrases to add precise detail.", "L.7.1a, L.7.1b",
    [("adjective clause", "A dependent clause that modifies a noun, often beginning with who, which, or that."), ("adverb clause", "A dependent clause that modifies a verb, telling when, why, or how, often beginning with because, when, although, if.")],
    "How can you add detail to “The machine vanished”?",
    [rules([["Modifier", "Example"], ["adjective phrase", "The machine <b>with the brass lever</b> vanished."], ["adjective clause", "The machine, <b>which the Traveller had built</b>, vanished."],
            ["adverb phrase", "The machine vanished <b>in an instant</b>."], ["adverb clause", "<b>When he pressed the lever</b>, the machine vanished."]], (1.7, 3.9)),
     Text("Use commas around adjective clauses that add extra (nonessential) information; no commas when the clause is essential to identify the noun. Put a comma after an introductory adverb clause."),
     KeyIdea("Phrases and clauses add precise detail; punctuate essential and nonessential clauses correctly.")],
    [Problem("Identify: The guest who doubted him was the Psychologist.", "adjective clause (who doubted him)"), Problem("Identify: Because the model vanished, the guests argued.", "adverb clause (Because the model vanished)"), Problem("Comma needed after an introductory adverb clause?", "Yes")],
    [S("Warm-Up", [SA("Adjective clauses often begin with…", "who, which, that"), SA("Adverb clauses often begin with…", "because, when, although, if")], cols=2),
     S("Expand the Sentence", [OR(f"“{q}” Add the modifier described.", a, lines=2) for q, a in [("The lever moved. (adjective clause)", "e.g. The lever, which was made of brass, moved."),
                                                                                                ("The guests laughed. (adverb clause)", "e.g. When the model disappeared, the guests laughed nervously."),
                                                                                                ("The scientist smiled. (adjective phrase)", "e.g. The scientist with grey eyes smiled."),
                                                                                                ("The room trembled. (adverb phrase)", "e.g. The room trembled for several seconds.")]]),
     S("Exit Ticket", [OR("Write a sentence about Chapter 2 with an adjective clause and an adverb clause.", "Answers vary.", lines=2)])],
    te("Students use modifying phrases and clauses.", "Explain the function of phrases and clauses; choose among sentence types.", "Workbook Lesson 5.6",
       "Add detail.", "Find clauses in Chapter 2.", ["Teach the chart; commas."], "Your Turn 1–3.",
       ["Missing commas after introductory clauses."], ["Clause starters list."], ["Expand five short sentences."]),
    summary="Phrases and clauses modify; punctuate correctly.")

L7 = Lesson("5.7", "Misplaced and Dangling Modifiers",
    "I can recognize and correct misplaced and dangling modifiers.", "L.7.1c",
    [("misplaced modifier", "A modifier placed too far from the word it describes, causing confusion."), ("dangling modifier", "A modifier with no clear word in the sentence to describe.")],
    "What's funny about: “Covered in dust, the Traveller found the model”?",
    [rules([["Problem", "Example", "Fix"], ["misplaced", "The guests watched the machine vanish with wide eyes.", "With wide eyes, the guests watched the machine vanish."],
            ["misplaced", "She found a book in the library that was falling apart.", "In the library, she found a book that was falling apart."],
            ["dangling", "Pushing the lever, the room began to shake.", "As Mara pushed the lever, the room began to shake."], ["dangling", "After eating dinner, the machine was demonstrated.", "After eating dinner, the Traveller demonstrated the machine."]],
           (0.9, 2.5, 2.4), fs=8.5),
     KeyIdea("Put modifiers next to what they modify. An opening phrase must describe the subject that follows it.")],
    [Problem("Fix: Hungry and tired, the dinner looked delicious to the Traveller.", "Hungry and tired, the Traveller thought the dinner looked delicious."), Problem("Fix: I saw a strange bird walking to school.", "Walking to school, I saw a strange bird."), Problem("What must an opening phrase describe?", "the subject right after it")],
    [S("Warm-Up", [SA("Misplaced modifier =", "too far from the word it describes"), SA("Dangling modifier =", "no clear word to describe")], cols=2),
     S("Fix the Modifier", [SA(q, a) for q, a in [("Flickering wildly, Mara watched the lights.", "Mara watched the lights flickering wildly."), ("The Traveller served soup to the guests in bowls.", "The Traveller served the guests soup in bowls."),
                                                  ("After traveling for hours, the future appeared.", "After traveling for hours, the Traveller saw the future appear."), ("Ren nearly read every book.", "Ren read nearly every book."),
                                                  ("Rusty and old, Kai opened the door.", "Kai opened the rusty, old door.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence with a dangling modifier on purpose, then fix it.", "Answers vary.", lines=2)])],
    te("Students fix misplaced and dangling modifiers.", "Place phrases and clauses within a sentence, recognizing and correcting misplaced and dangling modifiers.", "Workbook Lesson 5.7",
       "Covered in dust.", "Share funny examples.", ["Teach the chart."], "Your Turn 1–3.",
       ["Assuming meaning is obvious."], ["Draw the funny literal meaning."], ["Collect dangling modifiers from real writing."]),
    summary="Place modifiers next to what they modify.")

L8 = Lesson("5.8", "Precise Modifiers in Scientific Writing",
    "I can analyze how precise language communicates scientific ideas.", "RI.7.4, RI.7.3",
    [("dimension", "A measurable extent, such as length, width, height, or time."), ("spacetime", "Space and time combined into a single four-dimensional framework.")],
    "How would you explain the “fourth dimension” to a ten-year-old?",
    [P_FOURTH,
     Example("Analyze precision", "“a clock moving very fast ticks more slowly than one at rest”", ["Comparative “more slowly” compares two clocks precisely.", "“very fast” and “at rest” define the conditions."], "Precise modifiers make a surprising scientific claim clear and specific."),
     KeyIdea("Scientific writers use precise modifiers and comparisons to explain complex ideas clearly.")],
    [Problem("What are the three spatial dimensions?", "length, width, height"), Problem("Who published the theory of special relativity, and when?", "Albert Einstein, 1905"), Problem("Why must GPS correct its clocks?", "Time passes differently for fast-moving satellites; maps would become inaccurate.")],
    [S("Warm-Up", [SA("Dimension =", "a measurable extent"), SA("Spacetime combines…", "space and time")], cols=2),
     S("Analyze", [OR("How does the shoebox example help explain dimensions?", "A familiar object shows three measurements locate any point, and its existence over time suggests a fourth.", lines=3),
                   OR("How does the passage connect Wells's fiction to real science?", "Wells imagined time as a dimension; Einstein's theory later treated spacetime as four-dimensional.", lines=3),
                   OR("Find two precise modifiers or comparisons and explain their purpose.", "e.g. “tiny at everyday speeds but measurable”; “more slowly than one at rest”", lines=3)], passage=P_FOURTH),
     S("Exit Ticket", [OR("Explain the fourth dimension in two sentences for a younger student.", "Answers vary.", lines=2)])],
    te("Students analyze precise scientific language.", "Determine technical meanings; analyze interactions of ideas.", "Workbook Lesson 5.8",
       "Explain to a ten-year-old.", "Read “What Is the Fourth Dimension?”", ["Model precision analysis."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Vague explanations."], ["Use a concrete example."], ["Research time dilation for astronauts."]),
    summary="Precise modifiers and comparisons explain science clearly.")

# ================================================================= Week 3 · Prepositions and interjections (Chapter 3)
L9 = Lesson("5.9", "Prepositions and Prepositional Phrases",
    "I can identify prepositional phrases and explain whether they act as adjectives or adverbs.", "L.7.1",
    [("preposition", "A word showing a relationship between a noun and another word: in, on, through, during, beneath."), ("object of the preposition", "The noun or pronoun that ends a prepositional phrase.")],
    "How do prepositions help readers picture where and when things happen?",
    [ReaderAssign(TM, "Chapter 3: The Time Traveller Returns", "What condition is the Traveller in when he returns? How do the guests react?"),
     rules([["Function", "Example", "Answers"], ["adjective phrase", "the man <b>with the limp</b>", "which man?"], ["adverb phrase", "He limped <b>into the room</b>.", "where?"], ["adverb phrase", "He returned <b>after a week</b>.", "when?"]], (1.5, 2.7, 1.3)),
     Example("Identify", "“The Traveller stood in the doorway with dust on his coat.”", ["in the doorway → where he stood (adverb).", "with dust → describes the Traveller (adjective).", "on his coat → where the dust was (adjective modifying dust)."], "Three prepositional phrases adding place and detail."),
     KeyIdea("Prepositional phrases act as adjectives (which one?) or adverbs (where, when, how?).")],
    [Problem("Find the prepositional phrase: The guests sat around the table.", "around the table"), Problem("Function of “around the table”", "adverb (where they sat)"), Problem("Object of the preposition in “after dinner”", "dinner")],
    [S("Warm-Up", [SA("Five prepositions", "in, on, at, through, during"), SA("A prepositional phrase ends with…", "a noun or pronoun (object)")], cols=2),
     S("Identify Phrases and Functions", [SA(q, a) for q, a in [("The machine in the laboratory gleamed.", "in the laboratory: adjective"), ("He limped toward the table.", "toward the table: adverb"),
                                                               ("During the dinner, nobody spoke.", "During the dinner: adverb"), ("The guest from London laughed.", "from London: adjective"),
                                                               ("She hid the key beneath the floorboard.", "beneath the floorboard: adverb")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence describing the Traveller's return with three prepositional phrases.", "Answers vary.", lines=2)])],
    te("Students identify prepositional phrases.", "Explain the function of phrases.", "The Time Machine Reader (Chapter 3), workbook Lesson 5.9",
       "Picture where and when.", "Read Chapter 3.", ["Teach functions."], "Your Turn 1–3.",
       ["Confusing infinitives (to go) with prepositional phrases."], ["Ends in a noun? → prepositional phrase."], ["Write a treasure-hunt clue with prepositions."]),
    summary="Prepositional phrases act as adjectives or adverbs.")

L10 = Lesson("5.10", "Interjections and Tone in Dialogue",
    "I can use interjections and punctuation to convey emotion and tone.", "L.7.1, L.7.3",
    [("interjection", "A word or phrase that expresses sudden emotion: Wow! Oh no! Hey, well, alas.")],
    "What does “Oh!” add to a character's line?",
    [Text("Interjections show emotion. Strong ones take an exclamation point; mild ones take a comma: <i>Wow! It worked. / Well, I suppose so.</i> Use them sparingly in formal writing; they're most at home in dialogue."),
     P_SENSE,
     Example("Analyze an interjection", "“Wow! she thought, half terrified and half thrilled.”", ["“Wow!” bursts with sudden emotion.", "The phrase “half terrified and half thrilled” explains the mixed feeling."], "The interjection captures Mara's shock in a single word."),
     KeyIdea("Interjections convey sudden emotion; use exclamation points for strong feeling, commas for mild.")],
    [Problem("Punctuate: well I suppose you're right", "Well, I suppose you're right."), Problem("Punctuate: ouch that hurt", "Ouch! That hurt."), Problem("Where do interjections belong most?", "dialogue and informal writing")],
    [S("Warm-Up", [SA("A strong interjection", "Wow! / Oh no!"), SA("A mild interjection", "well, oh, hey")], cols=2),
     S("Analyze the Passage", [OR("Find two similes in paragraph 2 and explain how they help readers imagine time travel.", "“like the pages of a book flipped by an impatient thumb” (speed); “buildings rose like mushrooms after rain” (sudden growth).", lines=4),
                               OR("Find two adverbs in paragraph 3. What do they show about how Mara acts?", "gently, carefully: she acts with control and caution after the shock.", lines=2)], passage=P_SENSE),
     S("Exit Ticket", [OR("Write a two-line dialogue between the Traveller and a guest using two interjections.", "Answers vary.", lines=2)])],
    te("Students use interjections.", "Use language to convey tone; demonstrate command of grammar.", "Workbook Lesson 5.10",
       "Oh!", "Read “The First Jump.”", ["Teach punctuation."], "Your Turn 1–3.",
       ["Overusing interjections in essays."], ["Interjection list."], ["Write a comic strip."]),
    summary="Interjections express emotion; punctuate by strength.")

L11 = Lesson("5.11", "Conjunctions: Coordinating, Subordinating, and Correlative",
    "I can use conjunctions to show relationships between ideas.", "L.7.1b",
    [("coordinating conjunction", "Joins equal parts: for, and, nor, but, or, yet, so."), ("subordinating conjunction", "Begins a dependent clause: because, although, when, if, since, while."),
     ("correlative conjunctions", "Work in pairs: either…or, neither…nor, both…and, not only…but also.")],
    "How is “The Traveller returned, but he was injured” different from “Although the Traveller returned, he was injured”?",
    [rules([["Type", "Example", "Relationship"], ["coordinating", "The machine shook, but it held together.", "contrast (equal ideas)"], ["subordinating", "Because the lever stuck, Mara panicked.", "cause"],
            ["subordinating", "Although he was exhausted, he told his story.", "concession"], ["correlative", "Not only was he hungry, but he was also hurt.", "addition (paired)"]], (1.3, 3.0, 1.5), fs=9),
     Text("Correlative conjunctions need <b>parallel structure</b>: <i>either to the past or to the future</i> (not <i>either to the past or the future travel</i>)."),
     KeyIdea("Choose conjunctions that show the exact relationship: addition, contrast, cause, time, or condition.")],
    [Problem("Relationship shown by “although”", "concession/contrast"), Problem("Complete: Neither the Psychologist ___ the Doctor believed him.", "nor"), Problem("Coordinating or subordinating: because", "subordinating")],
    [S("Warm-Up", [SA("FANBOYS =", "for, and, nor, but, or, yet, so"), SA("A correlative pair", "either…or, neither…nor, both…and")], cols=2),
     S("Combine with the Best Conjunction", [SA(q, a) for q, a in [("He was tired. He kept talking. (concession)", "Although he was tired, he kept talking."), ("The model vanished. The guests were amazed. (cause)", "Because the model vanished, the guests were amazed."),
                                                                  ("She could go forward. She could go back. (correlative)", "She could go either forward or back."), ("The machine was small. It was powerful. (contrast, coordinating)", "The machine was small, yet it was powerful.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence about Chapter 3 with “not only…but also.”", "Answers vary.", lines=2)])],
    te("Students use conjunctions.", "Choose among simple, compound, complex sentences to signal relationships.", "Workbook Lesson 5.11",
       "but vs although.", "Find conjunctions in Chapter 3.", ["Teach types and relationships."], "Your Turn 1–3.",
       ["Non-parallel correlatives."], ["Relationship menu."], ["Combine choppy sentences in a past essay."]),
    summary="Conjunctions show relationships between ideas.")

L12 = Lesson("5.12", "Parts of Speech in Context",
    "I can determine a word's part of speech by how it functions in a sentence.", "L.7.1, L.7.4c",
    [],
    "Is “light” a noun, verb, or adjective?",
    [Text("Many words can function as more than one part of speech. Decide by asking how the word works in <i>this</i> sentence."),
     rules([["Sentence", "Word", "Part of speech"], ["The light flickered.", "light", "noun"], ["Light the lamp.", "light", "verb"], ["The model was light enough to hold.", "light", "adjective"],
            ["She traveled far.", "far", "adverb"], ["The far future was strange.", "far", "adjective"], ["He walked down the stairs.", "down", "preposition"], ["She looked down.", "down", "adverb"]], (2.8, 0.8, 1.6), fs=9),
     KeyIdea("Function determines part of speech: name it (noun), act (verb), describe a noun (adjective), modify a verb/adjective/adverb (adverb), relate (preposition).")],
    [Problem("“Time flies.” Part of speech of “flies”", "verb"), Problem("“The time machine” Part of speech of “time”", "adjective (noun used as a modifier)"), Problem("“She looked up.” Part of speech of “up”", "adverb")],
    [S("Warm-Up", [SA("A word that names", "noun"), SA("A word that relates a noun to another word", "preposition")], cols=2),
     S("Identify the Bold Word's Part of Speech", [SA(q, a) for q, a in [("The <b>future</b> frightened him.", "noun"), ("The <b>future</b> world was empty.", "adjective"), ("They <b>travel</b> through time.", "verb"),
                                                                        ("Time <b>travel</b> is impossible, they said.", "noun"), ("He climbed <b>over</b> the wall.", "preposition"), ("The dinner was <b>over</b>.", "adjective"),
                                                                        ("<b>Oh</b>, I see.", "interjection"), ("She worked <b>hard</b>.", "adverb")]], cols=2),
     S("Exit Ticket", [OR("Write three sentences using the word “back” as a noun, an adverb, and a verb.", "e.g. My back hurts. She went back. They back the plan.", lines=3)])],
    te("Students identify parts of speech by function.", "Demonstrate command of grammar; verify part of speech.", "Workbook Lesson 5.12",
       "light?", "Find flexible words in Chapter 3.", ["Model the chart."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Labeling by the word alone."], ["Ask: What job does it do?"], ["Create a parts-of-speech game."]),
    summary="Function determines part of speech.")

# ================================================================= Week 4 · Apply modifiers in revised writing (Chapter 4)
L13 = Lesson("5.13", "Analyzing Descriptive Writing",
    "I can analyze how an author describes an extraordinary experience.", "RL.7.4, RL.7.3",
    [("sensory details", "Details that appeal to sight, sound, touch, taste, or smell.")],
    "How would you describe something no one has ever experienced?",
    [ReaderAssign(TM, "Chapter 4: Time Travelling", "How does the Traveller describe the feeling of traveling through time? What does he see?"),
     Text("Wells had to describe something impossible: traveling through time. He relies on comparisons to familiar things, sensory details, and the Traveller's physical and emotional reactions."),
     Figure(lambda t: table(t, [["Technique", "What to look for in Chapter 4"], ["comparison", "time passing compared to familiar things"], ["sensory detail", "light flickering, sound, motion, sickness"],
                                ["physical reaction", "dizziness, nausea, fear"], ["accelerated change", "the sun and seasons racing past"]], [1.6 * inch, 4.0 * inch], width=5.6 * inch)),
     KeyIdea("Authors make the impossible vivid with comparisons, sensory details, and characters' reactions.")],
    [Problem("Why compare an impossible experience to familiar things?", "so readers can imagine it"), Problem("Name a sensory detail from Chapter 4.", "Answers vary; e.g. flickering light, rushing sensation."), Problem("How does the Traveller feel?", "Answers vary; e.g. dizzy, excited, frightened.")],
    [S("Warm-Up", [SA("Sensory details appeal to…", "the five senses"), SA("Year the Traveller arrives in", "802,701")], cols=2),
     S("Analyze Chapter 4", [OR("Copy two descriptions of time travel from Chapter 4. For each, name the technique and explain its effect.", "Answers vary.", lines=6),
                             OR("Compare Wells's description with “The First Jump” (Lesson 5.10). Which is more vivid to you? Why?", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("If you could ask the Traveller one question about the year 802,701, what would it be?", "Answers vary.", lines=2)])],
    te("Students analyze descriptive writing.", "Analyze word choice and how elements interact.", "The Time Machine Reader (Chapter 4), workbook Lesson 5.13",
       "Describing the impossible.", "Read Chapter 4.", ["Model technique analysis."], "Your Turn 1–3.",
       ["Summarizing instead of analyzing technique."], ["Technique chart."], ["Describe an impossible experience."]),
    summary="Comparisons, senses, and reactions make the impossible vivid.")

L14 = Lesson("5.14", "Planning a Science-Fiction Scene",
    "I can plan a science-fiction scene with a clear setting, conflict, and point of view.", "W.7.3a",
    [("conflict", "A struggle between opposing forces.")],
    "If you invented a machine, what would go wrong?",
    [Text("Your scene: a character uses an invention or arrives in a future or past world. Plan the <b>setting</b> (time, place, technology), <b>character</b>, <b>conflict</b>, <b>point of view</b>, and the <b>sensory details</b> you'll use."),
     Figure(lambda t: table(t, [["Plan element", "Questions"], ["Setting", "When and where? What technology exists?"], ["Character", "Who? What do they want?"], ["Conflict", "What goes wrong or stands in the way?"],
                                ["Point of view", "First person or third person limited?"], ["Sensory details", "What will the reader see, hear, feel?"], ["Ending", "How is the moment resolved, or left on a cliffhanger?"]],
                            [1.5 * inch, 4.1 * inch], width=5.6 * inch)),
     KeyIdea("Plan setting, character, conflict, point of view, sensory details, and ending before drafting.")],
    [Problem("What is conflict?", "a struggle between opposing forces"), Problem("Name two points of view you could use.", "first person, third person limited"), Problem("Why plan sensory details?", "to make the scene vivid")],
    [S("Warm-Up", [SA("Conflict =", "a struggle"), SA("Point of view options", "first person, third limited")], cols=2),
     S("Plan", [OR(f"{x}:", "Answers vary.", lines=2) for x in ["Setting", "Character and goal", "Conflict", "Point of view", "Five sensory details", "Ending"]])],
    te("Students plan science-fiction scenes.", "Engage and orient the reader by establishing context and point of view.", "Workbook Lesson 5.14",
       "What would go wrong?", "Review model passages.", ["Model a plan."], "Plan.",
       ["Too much plot for one scene."], ["One-moment focus."], ["Plan a sequel scene."], independent="Finish the plan."),
    summary="Plan setting, character, conflict, POV, details, ending.")

L15 = Lesson("5.15", "Drafting with Precise Modifiers and Concise Language",
    "I can draft a scene using precise modifiers while eliminating wordiness and redundancy.", "W.7.3d, L.7.3a",
    [("redundancy", "Saying the same thing twice: “past history,” “completely finished.”"), ("wordiness", "Using more words than needed.")],
    "Which is better: “The machine was very, very, extremely fast” or “The machine was blindingly fast”?",
    [rules([["Wordy or redundant", "Concise"], ["due to the fact that", "because"], ["at this point in time", "now"], ["completely finished", "finished"], ["return back", "return"],
            ["very scared", "terrified"], ["She moved quickly and fast.", "She darted."]], (2.6, 2.6)),
     Text("Choose one precise modifier instead of several weak ones. Cut redundant words. Use strong verbs so you need fewer adverbs."),
     KeyIdea("One precise word beats three vague ones. Cut redundancy and wordiness.")],
    [Problem("Concise: in the event that", "if"), Problem("Concise: very tired", "exhausted"), Problem("Redundant phrase: “past history.” Fix.", "history")],
    [S("Warm-Up", [SA("Redundancy =", "saying the same thing twice"), SA("Concise: very big", "huge, enormous")], cols=2),
     S("Make It Concise", [SA(q, a) for q, a in [("The Traveller returned back to his house.", "The Traveller returned to his house."), ("Due to the fact that it was late, the guests left.", "Because it was late, the guests left."),
                                                 ("She was very, very happy.", "She was elated."), ("The machine disappeared and vanished from sight.", "The machine vanished.")]], cols=1),
     S("Draft", [OR("Draft your science-fiction scene from your plan. Use precise modifiers and concise language.", "Answers vary.", lines=22, note="Look for: clear setting and conflict; consistent POV; precise modifiers; sensory details; concise language.")])],
    te("Students draft concisely.", "Use precise language and sensory details; choose language that expresses ideas precisely and concisely.", "Plans, workbook Lesson 5.15",
       "Very very fast.", "Review the concise chart.", ["Model a concise revision."], "Draft.",
       ["Stacking adverbs."], ["One-word upgrade list."], ["Write a 50-word micro story."], independent="Finish the draft."),
    summary="Precise, concise language strengthens writing.")

L16 = Lesson("5.16", "Revising and Editing the Scene",
    "I can revise and edit my scene for modifiers, punctuation, and clarity.", "W.7.5, L.7.1c, L.7.2a",
    [],
    "Which sentence in your draft is the most vivid? Which is the weakest?",
    [Figure(lambda t: table(t, [["Checklist", "✓"], ["Coordinate adjectives have commas; compound adjectives have hyphens.", ""], ["No misplaced or dangling modifiers.", ""], ["Comparatives and superlatives are correct (no double comparisons; fewer/less).", ""],
                                ["Interjections are punctuated correctly and used sparingly.", ""], ["Conjunctions show clear relationships; correlatives are parallel.", ""], ["Wordiness and redundancy are cut.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Revise for vividness and clarity; edit for modifier rules and punctuation.")],
    [Problem("Fix: Racing through time, the stars blurred.", "As she raced through time, the stars blurred."), Problem("Fix: a strange flickering light", "a strange, flickering light"), Problem("Fix: less buildings", "fewer buildings")],
    [S("Warm-Up", [SA("Dangling modifier fix", "add the right subject"), SA("Hyphenate: a world famous inventor", "a world-famous inventor")], cols=2),
     S("Revise and Edit", [OR("List four improvements you made using the checklist.", "Answers vary.", lines=4), OR("Copy your most vivid sentence.", "Answers vary.", lines=2)])],
    te("Students revise and edit narratives.", "Develop and strengthen writing; demonstrate command of conventions.", "Drafts, workbook Lesson 5.16, Unit 5 Review",
       "Most vivid / weakest.", "Read drafts aloud.", ["Model the checklist."], "Revise and edit.",
       ["Only spell-checking."], ["One checklist item per pass."], ["Illustrate the scene."], independent="Revise; then the Unit 5 Review.", exit_="Tomorrow: Unit 5 Test."),
    summary="Revise for vividness; edit modifiers and punctuation.")

# ================================================================= checks
C1 = Check("Weekly Check 13: Adjectives and Adverbs", [S("Read and answer", [
    SA("Find coordinate adjectives in paragraph 1.", "dusty, enormous"), SA("Why is there no comma in “old stone observatory”?", "cumulative adjectives (can't add “and” naturally)"),
    SA("Find two adverbs in paragraph 2.", "slowly, carefully"), SA("What do those adverbs modify?", "climbed"), SA("What does “silently” modify?", "pointed"),
    SA("Hyphenate: a decades old dome", "a decades-old dome"), OR("How do the modifiers in paragraph 1 create mood?", "windswept, alone, green with age, dusty, silently: lonely, abandoned, mysterious", lines=2)], cols=1, passage=P_C13)], minutes=20)
C2 = Check("Weekly Check 14: Comparison and Placement", [S("Read and answer", [
    SA("Find a comparative form.", "faster / more powerful"), SA("Find a list of comparatives.", "faster, smaller, and cheaper"), SA("Superlative of “powerful”", "most powerful"),
    SA("(Fewer/Less) vacuum tubes burned out.", "Fewer"), SA("Fix: Weighing thirty tons, engineers built ENIAC.", "Engineers built ENIAC, which weighed thirty tons."),
    SA("Fix: The computer in the room that was huge glowed.", "The huge computer in the room glowed."), SA("Correct: today's phone is (more powerful/more powerfuller).", "more powerful")], cols=1, passage=P_C14)], minutes=20)
C3 = Check("Weekly Check 15: Prepositions, Interjections, Conjunctions", [S("Read and answer", [
    SA("Find two interjections.", "Oh no! / Hooray!"), SA("Find a prepositional phrase that acts as an adverb.", "across the control room / at their screens / before midnight"),
    SA("Find a coordinating conjunction.", "but / and"), SA("Part of speech of “just” in “just before midnight”", "adverb"),
    SA("Combine with a subordinating conjunction: The signal stopped. The engineers worried.", "When the signal stopped, the engineers worried."), SA("Correlative: Write with “not only…but also” about the probe.", "e.g. The probe not only survived but also sent photos.")], cols=1, passage=P_C15)], minutes=20)

REVIEW = Check("Unit 5 Review", [
    S("Modifiers", [SA("Comma? a cold windy night", "Yes: a cold, windy night"), SA("Hyphenate: a well known author", "a well-known author"), SA("Superlative of good", "best"), SA("(Fewer/less) mistakes", "fewer"),
                    SA("Fix: Walking home, the rain started.", "As I walked home, the rain started."), SA("Concise: completely destroyed", "destroyed")], cols=2),
    S("Other parts of speech", [SA("Preposition in “under the bridge”", "under"), SA("Interjection example", "Wow!"), SA("Subordinating conjunction example", "although"), SA("Part of speech: “The <b>light</b> lamp”", "adjective")], cols=2)],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 5 Test", [
    S("Part A · Reading (1 point each)", [
        OR("What is surprising about New Aldora's relationship with books?", "There are no books; information appears as holograms; paper hasn't been made for 200 years.", lines=2),
        OR("How does Ren's experience of reading differ from getting information as holograms?", "It is slow; she has to wait page by page, and the waiting makes it better.", lines=2),
        OR("How does Kai change? Cite evidence.", "From rolling his eyes to falling silent for an hour over a book of maps.", lines=2),
        OR("State a theme.", "e.g. Slow, patient experiences can be more meaningful than instant ones.", lines=2)], passage=P_TEST),
    S("Part B · Modifiers (1 point each)", [
        SA("Find coordinate adjectives (paragraph 2).", "high, arched"), SA("Find a compound adjective.", "leather-bound"), SA("What does “lazily” modify?", "drifted"),
        SA("Find an adjective clause.", "who rolled his eyes until he opened a book of maps"), SA("Find an adverb clause.", "until the light faded completely / until he opened a book of maps"),
        SA("Fix: Crumbling and old, Ren entered the library.", "Ren entered the crumbling, old library."), SA("Comparative or superlative: “made it better”", "comparative")], cols=1),
    S("Part C · Other parts of speech (1 point each)", [
        SA("Prepositional phrase in paragraph 2 acting as an adverb", "through a crumbling doorway / through slanted beams of sunlight / from the cracked marble floor"),
        SA("Part of speech of “old” in “the old district”", "adjective"), SA("Write an interjection Ren might say on finding the library.", "e.g. Wow!"), SA("Coordinating conjunction in paragraph 3", "and")], cols=1),
    S("Part D · Writing (5 points)", [OR("Write a short scene (8–10 sentences) in which another child in New Aldora discovers the library. Use coordinate and compound adjectives, an adverb clause, a prepositional phrase, and concise, vivid language.",
                                         "Rubric: setting and conflict (1); coordinate and compound adjectives correctly punctuated (1); adverb clause and prepositional phrase (1); no misplaced modifiers (1); concise, vivid language (1).", lines=16, points=5)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-02-22", "2027-03-01", "2027-03-08", "2027-03-22"], CHECKS, REVIEW, TEST)

UNIT = Unit(5, "Modifiers and Precise Description", "Adjectives, adverbs, comparison, modifier placement, prepositions, interjections, conjunctions, and science-fiction writing, with The Time Machine, Chapters 1–4.",
    "H. G. Wells imagined a machine that could travel through time, and he had to describe something no one had ever experienced. In this unit you'll study how writers use modifiers to make description vivid and precise, master the grammar of adjectives, adverbs, phrases, and clauses, and write your own science-fiction scene.",
    ["Analyze science fiction, frame narratives, and descriptive craft.", "Use and punctuate adjectives and adverbs; form comparisons correctly.", "Place modifiers correctly; use prepositions, interjections, and conjunctions.",
     "Write and revise a vivid, concise science-fiction scene."],
    [("RL.7.3–5, RI.7.3–4", "Analyze elements, word choice, structure, and technical language."), ("L.7.1a–c, L.7.2a, L.7.3a", "Phrases and clauses; misplaced modifiers; coordinate adjectives; concise language."),
     ("W.7.3, W.7.5", "Write and revise narratives.")],
    [("coordinate adjectives", "Equal adjectives separated by a comma."), ("dangling modifier", "A modifier with no clear word to describe."), ("comparative", "Compares two."), ("interjection", "Expresses sudden emotion."), ("redundancy", "Saying the same thing twice.")],
    ["Unit 4 analysis skills; basic parts of speech."], ["The Time Machine Reader (Chapters 1–4)"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Precise, concise language makes everything from product descriptions to science reports clearer, and GPS really does depend on Einstein's ideas about time.",
    family_note="Ask your student to describe the most vivid moment of their science-fiction scene without using the word “very.”",
    weeks=WEEKS)
