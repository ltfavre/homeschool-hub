"""Grade 7 ELA · Unit 1: Language and Meaning in A Christmas Carol — roots and context, connotation and figurative language, evidence and inference, theme and summary.
Anchor reading: A Christmas Carol (Grade 7 Reader), Introduction through Stave Three (first section)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule

CAROL = "A Christmas Carol Reader"

# ================================================================= passages (Dickens excerpts are public domain; others original)
P_OPEN = Passage("From A Christmas Carol, Stave One (original text)", [
    "MARLEY was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge’s name was good upon ’Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail.",
    "“Bah!” said Scrooge, “Humbug!”",
], source="Charles Dickens, A Christmas Carol (1843). Public domain.", genre="Novella excerpt", numbered=False)

P_FLINT = Passage("Scrooge, Stave One (original text)", [
    "Oh! But he was a tight-fisted hand at the grind-stone, Scrooge! a squeezing, wrenching, grasping, scraping, clutching, covetous, old sinner! Hard and sharp as flint, from which no steel had ever struck out generous fire; secret, and self-contained, and solitary as an oyster. The cold within him froze his old features, nipped his pointed nose, shrivelled his cheek, stiffened his gait; made his eyes red, his thin lips blue; and spoke out shrewdly in his grating voice. A frosty rime was on his head, and on his eyebrows, and his wiry chin. He carried his own low temperature always about with him; he iced his office in the dog-days; and didn’t thaw it one degree at Christmas.",
    "External heat and cold had little influence on Scrooge. No warmth could warm, no wintry weather chill him. No wind that blew was bitterer than he, no falling snow was more intent upon its purpose, no pelting rain less open to entreaty.",
], source="Charles Dickens, A Christmas Carol. Public domain.", genre="Novella excerpt", numbered=False)

P_LONDON = Passage("Christmas in Dickens's London", [
    "In 1843, London was the largest city in the world, home to about two million people. Its factories, banks, and docks made some families very rich. Yet many Londoners lived crowded into a single damp room, and a coal fire, a hot meal, or a pair of boots was a luxury.",
    "For a working family, the Christmas feast took planning. Many saved for months by joining a <b>goose club</b>, paying a few pennies each week to a shopkeeper so that they could collect a goose at Christmas. Families with no oven of their own carried their dinner to the local baker's shop, where it was roasted in the big bread ovens for a small fee.",
    "People who could not support themselves at all might be sent to a <b>workhouse</b>. Under the Poor Law of 1834, workhouses were made deliberately unpleasant: families were separated, the work was hard, and the food was plain and meager, so that only the truly desperate would ask to enter.",
    "Christmas itself was changing. The first Christmas card for sale was printed in London in 1843, the same year <i>A Christmas Carol</i> appeared. Over the following decades, the holiday grew from a modest celebration into the family festival of gifts, feasting, and charity that Dickens's story helped to shape.",
], source="An original informational text", genre="Informational text")

P_ORIGIN = Passage("Why Dickens Wrote A Christmas Carol", [
    "Early in 1843, the British government published a report on children working in mines, mills, and workshops. It described children as young as five or six working twelve hours a day. Charles Dickens read it and was horrified. He told a friend he planned to write a pamphlet, an appeal on behalf of “the poor man's child.”",
    "That autumn he visited a ragged school, a free school run by volunteers for the poorest children in London. He saw children who were hungry, dirty, and had never been taught to read. A few weeks later, speaking to a crowd in Manchester, he argued that education was the best hope for children like these.",
    "Dickens never wrote the pamphlet. Instead, he decided that a story would strike a much harder blow, because readers who would ignore a report might be moved by characters they cared about. Within about six weeks he had written <i>A Christmas Carol</i>.",
    "Dickens also remembered his own childhood. When he was twelve, his father was imprisoned for debt, and Charles was sent to work in a factory, pasting labels on pots of boot polish. Many readers believe that this experience is one reason his story takes the side of poor children so fiercely.",
], source="An original informational text based on historical accounts", genre="Informational text")

P_CONNOTE = Passage("Two Reviews of the Same Restaurant", [
    "<b>Review A.</b> The Harbor Grill is a cozy little spot with a relaxed atmosphere. The menu is simple, and the portions are generous. Service is unhurried, giving diners time to enjoy their meal.",
    "<b>Review B.</b> The Harbor Grill is a cramped little spot with a sleepy atmosphere. The menu is limited, and the portions are excessive. Service is slow, leaving diners waiting for their meal.",
], source="Original examples", genre="Opinion writing", numbered=False)

P_CHECK1 = Passage("The Lighthouse Keeper's Log", [
    "For thirty-one years, Agnes Brewer kept the light at Pelican Point. Her log, a weathered leather book now held in the county archive, records the weather, the passing ships, and the condition of the lamp in brief, unsentimental entries.",
    "Yet occasionally Agnes's restraint gives way. On November 3, 1913, after a storm wrecked two schooners on the reef, she wrote only: “Heavy seas. Lamp kept. Seven men brought ashore. Four not.” The terse entry is more harrowing than any detailed description could be.",
    "Historians value such logs precisely because they were not meant to be literature. They are firsthand records, written in the moment, by people whose work kept others alive.",
], source="An original informational text", genre="Informational text")

P_CHECK2 = Passage("The Inheritance", [
    "When Aunt Theodora died, she left Mira an old trunk, a box of letters, and one instruction: <i>Read them in order.</i>",
    "Mira's cousins laughed. They had inherited the house and the car. “Enjoy your junk,” said Derek, tossing her the trunk key.",
    "That night, Mira opened the first letter. It was dated 1952 and began: <i>To whoever is patient enough to read this…</i> By the tenth letter, Mira understood that the trunk held something her cousins would never see: the story of a woman who had crossed an ocean alone at seventeen, taught herself three languages, and spent her life helping others do the same.",
    "Mira closed the last letter at dawn. She didn't feel like the cousin who got the junk. She felt like the one who got the treasure.",
], source="An original story", genre="Realistic fiction")

P_CHECK3 = Passage("The Gardener's Gift", [
    "Every spring, Mr. Okafor planted more tomatoes than he could possibly eat. Neighbors assumed he was simply a poor planner.",
    "In July, the reason became clear. Each morning, a bag of ripe tomatoes appeared on a different doorstep: the widow who rarely left her apartment, the family whose father had lost his job, the teenager who lived alone above the laundromat.",
    "No one ever saw him deliver them. When asked, Mr. Okafor only shrugged. “A garden,” he said, “is too big a thing for one person.”",
], source="An original story", genre="Realistic fiction")

P_TEST = Passage("The Translator", [
    "When Ana's family moved from Colombia to Ohio, Ana was eleven, and her English was better than anyone else's in the family. Almost overnight she became the family's translator.",
    "She translated at the bank, where a man in a gray suit spoke too fast and sighed impatiently when her mother asked him to repeat himself. She translated at the doctor's office, choosing words carefully so that her little brother wouldn't be frightened. She translated letters from the landlord, bills from the electric company, and notes from her own teachers, though she sometimes softened those.",
    "At first Ana resented it. Her classmates spent afternoons at soccer practice, while she spent hers in waiting rooms. Translating made her feel older than she wanted to be, as if she carried a heavy backpack no one else could see.",
    "But one evening, after Ana helped her father through a job interview over the phone, he hung up and was silent for a long moment. Then he said, in careful English, “Thank you, mija. Today you were my voice.” His eyes were bright.",
    "Ana realized that translating was not only a burden. It was a bridge, and she was the one building it. The next week, she signed up to volunteer at the community center, helping other newcomers with forms and phone calls. The backpack still felt heavy some days. But now she knew what she was carrying, and why.",
], source="An original story", genre="Realistic fiction")


# ================================================================= Week 1 · Roots, affixes, and context clues (Introduction, Stave One first section)
L1 = Lesson("1.1", "Reading Dickens's Language",
    "I can use strategies to read and understand the language of a classic novel.", "RL.7.4, RL.7.5",
    [("novella", "A story longer than a short story but shorter than a novel."), ("archaic", "Old-fashioned; no longer in common use."),
     ("narrator", "The voice that tells a story. Dickens's narrator often speaks directly to the reader.")],
    "Read this line aloud: “Old Marley was as dead as a door-nail.” Why would a story begin by insisting that someone is dead?",
    [ReaderAssign(CAROL, "Introduction and Stave One (first section)", "Who is Scrooge? How do other people react to him on Christmas Eve?"),
     Text("Dickens wrote <i>A Christmas Carol</i> in 1843, so most of his words are familiar, but some are old-fashioned or British, and his sentences can be long. Three strategies help: <b>read aloud</b> for meaning, <b>translate old words</b>, and <b>break long sentences</b> at their semicolons and commas."),
     Figure(lambda t: table(t, [["Dickens's word", "Modern meaning"], ["’Change", "the Exchange, where merchants met to do business"], ["counting-house", "a business office"], ["humbug", "nonsense; a fraud"],
                                ["dog-days", "the hottest days of summer"], ["rime", "frost"], ["comforter", "a long woolen scarf"], ["workhouse", "a grim public home for the very poor"]], [2.0 * inch, 3.6 * inch], width=5.6 * inch)),
     P_OPEN,
     Example("Translate a sentence", "“Scrooge’s name was good upon ’Change, for anything he chose to put his hand to.”",
             ["’Change = the Exchange, where merchants did business.", "his name was good = people trusted his signature.", "anything he chose to put his hand to = any deal he signed."],
             "“The merchants trusted Scrooge’s signature on any deal he made.” He is respected in business, which tells us money is what he is known for."),
     KeyIdea("Read aloud, translate old words, and break long sentences into parts. Meaning first, then details.")],
    [Problem("What does “Humbug!” mean?", "Nonsense!"), Problem("What is a counting-house?", "a business office"), Problem("What happens on Christmas Eve in the first section of Stave One?", "Scrooge refuses his nephew's invitation, turns away men collecting for the poor, and grudgingly gives Bob the day off.")],
    [S("Warm-Up", [SA("humbug =", "nonsense"), SA("rime =", "frost")], cols=2),
     S("Translate", [OR(f"“{q}”", a, lines=2) for q, a in [("Old Marley was as dead as a door-nail.", "Marley was completely, certainly dead."),
                                                           ("He iced his office in the dog-days.", "Even in the hottest summer days, his office felt cold."),
                                                           ("“Don’t be cross, uncle!” said the nephew.", "“Don't be angry, uncle!” said his nephew."), ("“I can’t afford to make idle people merry.”", "I won't pay to make lazy people happy.")]], passage=P_OPEN),
     S("Stave One", [OR("Why do you think Dickens opens the story by insisting so strongly that Marley is dead? What effect does it have on the reader?", "It is funny and a little spooky; it prepares us for something wonderful (a ghost) and makes us curious about why it matters.", lines=4)]),
     S("Exit Ticket", [OR("Which reading strategy helped you most today? Give an example.", "Answers vary.", lines=2)])],
    te("Students apply strategies to Dickens's language.", "Determine the meaning of words and phrases; analyze how a text's form contributes to meaning.", "Grade 7 Reader: A Christmas Carol (Introduction–Stave One, first section), workbook Lesson 1.1",
       "Read the door-nail line aloud; predict.", ["Read the Reader introduction and character list.", "Read the first section of Stave One aloud, taking turns."], ["Teach the word chart.", "Model translating the ’Change sentence."], "Your Turn 1–3.",
       ["Skipping a long sentence instead of breaking it apart."], ["Read aloud with expression; the narrator is joking with you."], ["Read Scrooge's lines aloud in his voice and Fred's in his."]),
    summary="Read aloud, translate old words, break long sentences into parts.")

L2 = Lesson("1.2", "Greek and Latin Roots and Affixes",
    "I can use Greek and Latin roots and affixes to determine word meanings.", "L.7.4b",
    [("root", "A word part that carries the core meaning."), ("affix", "A prefix or suffix.")],
    "What do <i>benefit</i>, <i>benevolent</i>, and <i>benefactor</i> have in common?",
    [Figure(lambda t: table(t, [["Root / affix", "Meaning", "Examples"], ["bene", "good, well", "benefit, benevolent, benefactor"], ["mal", "bad", "malice, malfunction, malevolent"], ["liber", "free", "liberty, liberal, liberality"],
                                ["voc / vok", "voice, call", "vocal, invoke, revoke"], ["dict", "say", "predict, contradict, verdict"], ["spect", "look", "spectator, inspect, spectre"],
                                ["ject", "throw", "reject, project, eject"], ["-ous / -ose", "full of", "covetous, morose"], ["sol", "alone", "solitary, solo, desolate"]], [1.2 * inch, 1.4 * inch, 3.0 * inch], width=5.6 * inch, font_size=9)),
     Example("Analyze a word", "What does <i>malevolent</i> mean?", ["mal = bad.", "vol = wish (as in voluntary).", "-ent = having the quality of."], "wishing harm to others; evil-minded"),
     KeyIdea("Break a word into parts, combine meanings, then check the context.")],
    [Problem("<i>benevolent</i>", "wishing good; kind"), Problem("<i>solitary</i>", "alone; without companions"), Problem("<i>spectator</i>", "a person who watches")],
    [S("Warm-Up", [SA("mal =", "bad"), SA("spect =", "look")], cols=2),
     S("Word Analysis", [SA(w, a) for w, a in [("malfunction", "fail to work properly"), ("contradict", "say the opposite"), ("introspective", "looking inward at oneself"), ("projectile", "an object thrown or launched"),
                                               ("invoke", "call upon"), ("benefactor", "a person who does good / gives help"), ("desolate", "empty and lonely"), ("malicious", "full of ill will")]], cols=2),
     S("Context Check", [OR("The gentlemen collecting for the poor hope that Marley's “liberality” lives on in Scrooge. Use the root <i>liber</i> to explain the word, then explain why their hope is ironic.", "liber = free; liberality is giving freely, or generosity. It is ironic because Scrooge, like Marley, gives nothing.", lines=3)]),
     S("Exit Ticket", [OR("Choose a root from the chart and write three words that contain it.", "Answers vary.", lines=2)])],
    te("Students analyze Greek and Latin roots.", "Use common, grade-appropriate Greek or Latin affixes and roots as clues to meaning.", "Workbook Lesson 1.2",
       "bene words.", "Skim Stave One for root words (solitary, covetous, liberality).", ["Teach the root chart.", "Model malevolent."], "Your Turn 1–3.",
       ["Over-relying on roots without checking context."], ["Word-part sums."], ["Start a root journal."]),
    summary="Roots and affixes unlock meaning; confirm with context.")

L3 = Lesson("1.3", "Context Clues in Complex Texts",
    "I can use context to determine the meaning of words and phrases in complex texts.", "L.7.4a, RL.7.4",
    [],
    "In “Many saved for months by joining a goose club, paying a few pennies each week to a shopkeeper,” what is a goose club?",
    [Text("Complex texts often define words indirectly. Use the <b>sentence</b>, the <b>paragraph</b>, and the <b>overall meaning</b>. Clues include definitions, restatements, examples, contrasts, and cause-effect relationships."),
     P_LONDON,
     Example("Use paragraph context", "What was a goose club?", ["The sentence restates it: “paying a few pennies each week to a shopkeeper.”", "The purpose follows: “so that they could collect a goose at Christmas.”"], "a savings plan for buying a Christmas goose a little at a time"),
     KeyIdea("Use the sentence, the paragraph, and the passage's overall meaning to figure out unfamiliar words.")],
    [Problem("Why did families take their dinner to the baker's?", "They had no oven of their own."), Problem("What does “deliberately unpleasant” tell you about workhouses?", "They were made hard on purpose to discourage people from entering."), Problem("What context clue shows how big London was?", "about two million people; the largest city in the world")],
    [S("Warm-Up", [SA("Context means…", "surrounding words and sentences"), SA("A contrast signal word", "but, however, yet")], cols=2),
     S("Use the Passage", [OR("What does “meager” mean in paragraph 3? What clue helps?", "small; not enough. The food was “plain” and meant to discourage people.", lines=2),
                           OR("Explain how the contrast in paragraph 1 helps you understand London in 1843.", "“Yet” contrasts very rich families with families crowded into one room; London had great wealth and great poverty.", lines=3),
                           MC("“Only the truly desperate would ask to enter” (paragraph 3) means people entered the workhouse…", ["for a holiday", "when they had no other choice", "to learn a trade"], 1)], passage=P_LONDON),
     S("Context in A Christmas Carol", [OR("Find a word in Stave One that you didn't know. Write the sentence, the clue, and your definition.", "Answers vary.", lines=4)])],
    te("Students use context in complex texts.", "Use context as a clue to the meaning of a word or phrase.", "Workbook Lesson 1.3",
       "Goose club.", "Read “Christmas in Dickens's London.”", ["Model paragraph-level context."], "Your Turn 1–3.",
       ["Looking only at the immediate sentence."], ["Read one sentence before and after."], ["Find context clues for a Words to Know word in the Reader."]),
    summary="Use sentence, paragraph, and passage context.")

L4 = Lesson("1.4", "Reference Tools and Word Origins",
    "I can use dictionaries, glossaries, and footnotes to find meanings, pronunciations, parts of speech, and origins.", "L.7.4c, L.7.4d",
    [("etymology", "The origin and history of a word."), ("glossary", "A list of difficult words and their meanings, like the Words to Know boxes in your Reader.")],
    "Where would you look to find out what “miser” means and how to say it?",
    [Text("Dictionaries give <b>pronunciation</b>, <b>part of speech</b>, <b>definitions</b>, and <b>etymology</b>. Your Reader's <b>Words to Know</b> boxes work like a glossary. Always check your inferred meaning against a reference."),
     Example("Read a dictionary entry", "miser (MY-zer), noun. A person who hoards money and spends as little as possible. [Latin <i>miser</i>, wretched, unhappy]",
             ["Pronunciation: MY-zer.", "Part of speech: noun.", "Etymology: from the Latin word for “wretched.”"], "A miser hoards money; the word's origin hints that misers are unhappy, which is exactly Scrooge's problem."),
     KeyIdea("Use references to confirm meanings, pronunciation, part of speech, and word origins.")],
    [Problem("How is <i>miser</i> pronounced?", "MY-zer"), Problem("What does etymology tell you?", "a word's origin and history"), Problem("What part of your Reader works like a glossary?", "the Words to Know boxes")],
    [S("Warm-Up", [SA("Etymology =", "word origin"), SA("Part of speech for <i>miser</i>", "noun")], cols=2),
     S("Use a Dictionary", [OR(f"Look up <i>{w}</i>. Write its part of speech, a definition that fits A Christmas Carol, and its origin.", a, lines=2) for w, a in [
         ("covetous", "adjective; greedy for wealth or possessions; from Latin cupiditas (desire)"), ("solitary", "adjective; alone; from Latin solus (alone)"),
         ("apparition", "noun; a ghost or ghostlike figure; from Latin apparere (to appear)")]]),
     S("Glossary", [OR("Choose two words from the Words to Know box for Stave One. Copy each word and its meaning, then write the sentence from the story where it appears.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Why might a word's etymology help you remember its meaning?", "Knowing the parts and history connects the word to familiar ideas.", lines=2)])],
    te("Students use reference materials.", "Consult reference materials to find pronunciation and clarify meaning or part of speech; verify inferred meanings.", "Dictionary (print or online), workbook Lesson 1.4",
       "Miser.", "Read the Words to Know box for Stave One.", ["Model the entry."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Choosing the first definition without checking fit."], ["Test each definition in the sentence."], ["Trace the etymology of five words from Stave One."]),
    summary="References confirm meaning, pronunciation, part of speech, and origin.")

# ================================================================= Week 2 · Vocabulary in context (Stave One, second section)
L5 = Lesson("1.5", "Connotation and Denotation",
    "I can distinguish between the denotation and connotation of words.", "L.7.5c, RL.7.4",
    [("denotation", "A word's dictionary meaning."), ("connotation", "The feelings or associations a word carries: positive, negative, or neutral.")],
    "Would you rather be called <i>thrifty</i> or <i>stingy</i>? Don't they mean the same thing?",
    [ReaderAssign(CAROL, "Stave One (second section)", "What is Marley's Ghost wearing, and why? Which words show how he feels about the life he lived?"),
     Text("Words with similar <b>denotations</b> can have very different <b>connotations</b>. Writers choose words to shape how readers feel."),
     P_CONNOTE,
     Example("Compare connotations", "cozy vs cramped", ["Denotation: both mean small.", "Connotation: cozy = warm, comfortable (positive); cramped = uncomfortably tight (negative)."], "Same size, opposite feeling."),
     KeyIdea("Same denotation, different connotation. Word choice shapes the reader's feelings.")],
    [Problem("Connotation of “relaxed” vs “sleepy”", "relaxed: positive; sleepy: negative (dull)"), Problem("Connotation of “generous” vs “excessive”", "generous: positive; excessive: negative"), Problem("Which review is more favorable?", "Review A")],
    [S("Warm-Up", [SA("Denotation =", "dictionary meaning"), SA("Connotation =", "feelings a word carries")], cols=2),
     S("Positive, Negative, or Neutral?", [SA(f"{a} / {b} / {c}", ans) for a, b, c, ans in [("thrifty", "stingy", "careful with money", "positive / negative / neutral"), ("confident", "arrogant", "sure", "positive / negative / neutral"),
                                                                                       ("slender", "skinny", "thin", "positive / negative / neutral"), ("determined", "stubborn", "persistent", "positive / negative / neutral")]], cols=1),
     S("Words About Scrooge", [OR("Copy two words or phrases the narrator uses about Scrooge in Stave One. Explain their connotation and what they reveal.", "Answers vary, e.g. “tight-fisted,” “covetous old sinner”: negative; he is greedy and unkind.", lines=4),
                               OR("Scrooge calls Christmas “humbug.” His nephew calls it “a kind, forgiving, charitable, pleasant time.” How do their word choices show two different attitudes?", "Scrooge's word is scornful and negative; Fred's words are warm and positive. Scrooge sees Christmas as a waste, Fred as a time of kindness.", lines=3)]),
     S("Exit Ticket", [OR("Rewrite Review B's first sentence with positive connotations.", "e.g. The Harbor Grill is an intimate little spot with a peaceful atmosphere.", lines=2)])],
    te("Students distinguish connotation and denotation.", "Distinguish among the connotations of words with similar denotations.", "Grade 7 Reader: A Christmas Carol (Stave One, second section), workbook Lesson 1.5",
       "Thrifty vs stingy.", ["Read the second section of Stave One.", "Read the two reviews."], ["Model cozy/cramped."], "Your Turn 1–3.",
       ["Assuming synonyms are interchangeable."], ["Connotation thermometer."], ["Rewrite an ad with negative connotations."]),
    summary="Connotation shapes feeling beyond the dictionary meaning.")

L6 = Lesson("1.6", "Figurative Language: Simile, Metaphor, and Hyperbole",
    "I can interpret figurative language and explain its effect.", "L.7.5a, RL.7.4",
    [("simile", "A comparison using like or as."), ("hyperbole", "Deliberate exaggeration for effect."), ("extended metaphor", "A metaphor developed over several sentences.")],
    "What does Dickens mean when he says Scrooge is “solitary as an oyster”?",
    [P_FLINT,
     Example("Interpret", "“Hard and sharp as flint, from which no steel had ever struck out generous fire.”",
             ["Literal: flint is a hard stone; striking it with steel makes sparks for a fire.", "Figurative: no one has ever struck even a spark of generosity out of Scrooge.", "Effect: Scrooge seems cold, hard, and impossible to warm."],
             "The simile and the image of fire show that generosity cannot be struck out of Scrooge."),
     Text("<b>Cold</b> runs through the whole paragraph as an extended metaphor: the cold inside Scrooge freezes his face, he “iced his office,” and he never thaws, even at Christmas. Today, calling someone “a Scrooge” means he or she is stingy, which shows how strongly Dickens's character has shaped our language."),
     KeyIdea("Identify the device, explain the comparison, then explain its effect on meaning or mood.")],
    [Problem("Device in “solitary as an oyster”", "simile"), Problem("What does it mean to call someone “a Scrooge” today?", "that the person is stingy"), Problem("Device in “he iced his office in the dog-days”", "hyperbole (and part of the extended metaphor of cold)")],
    [S("Warm-Up", [SA("A simile uses…", "like or as"), SA("Hyperbole is…", "deliberate exaggeration")], cols=2),
     S("Interpret", [OR(f"“{q}” Device and meaning:", a, lines=2) for q, a in [("The wind howled its fury at the house.", "personification: the wind is violent, as if angry"),
                                                                             ("Her silence was a locked door.", "metaphor: she refused to share her feelings"), ("I've told you a million times.", "hyperbole: I've told you many times"),
                                                                             ("He was as cheerful as a robin in spring.", "simile: he was very cheerful")]]),
     S("Scrooge's Cold", [OR("How does Dickens use the idea of cold to describe Scrooge's personality? Use two phrases from the passage.", "His coldness is inside him: “The cold within him froze his old features”; “didn’t thaw it one degree at Christmas.” Cold stands for his lack of warmth toward people.", lines=4)], passage=P_FLINT),
     S("Exit Ticket", [OR("Write a simile or hyperbole about Marley's Ghost.", "Answers vary.", lines=2)])],
    te("Students interpret figurative language.", "Interpret figures of speech in context; analyze the impact of word choices.", "Workbook Lesson 1.6",
       "Solitary as an oyster.", "Read the flint paragraph aloud.", ["Model interpreting the flint simile.", "Trace the extended metaphor of cold."], "Your Turn 1–3.",
       ["Identifying the device but not its effect."], ["Device → meaning → effect frame."], ["Find three more similes in Stave One."]),
    summary="Device → comparison → effect.")

L7 = Lesson("1.7", "Word Relationships and Analogies",
    "I can use relationships between words to understand each word better.", "L.7.5b",
    [("analogy", "A comparison of two pairs of words that share the same relationship.")],
    "Complete: <i>Captain is to ship as king is to ___.</i>",
    [Figure(lambda t: table(t, [["Relationship", "Example"], ["synonyms", "miser : skinflint"], ["antonyms", "generous : stingy"], ["part to whole", "link : chain"], ["cause to effect", "frost : ice"],
                                ["item to category", "Scrooge : character"], ["worker to tool", "clerk : pen"], ["degree", "chilly : frozen"]], [1.8 * inch, 3.0 * inch], width=4.8 * inch)),
     Example("Solve an analogy", "captain : ship :: king : ___", ["Relationship: a captain rules a ship.", "A king rules a ___ ."], "kingdom"),
     KeyIdea("Name the relationship in the first pair, then find the word that creates the same relationship.")],
    [Problem("loyal : traitor :: brave : ___", "coward"), Problem("page : book :: stave : ___", "carol (book)"), Problem("drizzle : downpour :: breeze : ___", "gale (hurricane)")],
    [S("Warm-Up", [SA("miser : skinflint relationship", "synonyms"), SA("link : chain relationship", "part to whole")], cols=2),
     S("Complete the Analogies", [SA(q, a) for q, a in [("author : novel :: playwright : ___", "play"), ("generous : stingy :: humble : ___", "arrogant (proud)"), ("thunder : lightning :: smoke : ___", "fire"),
                                                        ("painter : brush :: sculptor : ___", "chisel"), ("island : ocean :: oasis : ___", "desert"), ("whisper : shout :: walk : ___", "run (sprint)")]], cols=2),
     S("Create", [OR("Write two analogies using characters or objects from A Christmas Carol. Name each relationship.", "e.g. Marley : chain :: Bob Cratchit : comforter (character to object he wears); Scrooge : miser :: Fred : optimist (item to category).", lines=3)])],
    te("Students analyze word relationships.", "Use the relationship between particular words to better understand each of the words.", "Workbook Lesson 1.7",
       "Captain : ship.", "Review Stave One vocabulary.", ["Teach relationship types."], "Your Turn 1–3.",
       ["Reversing the order of the pair."], ["Make a sentence from pair 1."], ["Write analogies for a sibling."]),
    summary="Name the relationship; match it.")

L8 = Lesson("1.8", "Sound and Rhythm in Prose",
    "I can analyze the effect of repetition, rhythm, and sound in prose.", "RL.7.4",
    [("alliteration", "Repetition of beginning consonant sounds."), ("parallelism", "Repeating the same grammatical pattern, such as “no warmth could warm, no wintry weather chill him.”"),
     ("read-aloud prose", "Prose written to be heard as well as read. Dickens performed this story on stage.")],
    "Why might a writer pile up a long list of words instead of choosing just one?",
    [Text("Dickens wrote <i>A Christmas Carol</i> to be read aloud, and later performed it himself in theaters. His sentences have rhythm: he piles up lists, repeats patterns, and repeats sounds. Sound and rhythm help reveal character and mood."),
     Example("Hear the list", "“a squeezing, wrenching, grasping, scraping, clutching, covetous, old sinner!”",
             ["Six words in a row all describe greed.", "Most end in -ing and are full of harsh sounds (sq, wr, gr, scr, cl).", "Effect: the list sounds like grabbing hands that won't let go."], "The harsh, piled-up list makes Scrooge's greed sound ugly and endless."),
     Example("Hear the pattern", "“No warmth could warm, no wintry weather chill him. No wind that blew was bitterer than he…”",
             ["Parallelism: “No warmth… no wintry weather… No wind…”", "Alliteration: warmth, warm, wintry, weather, wind."], "The repeated “No…” builds the idea that nothing at all can reach Scrooge."),
     KeyIdea("Lists, repetition, parallelism, and repeated sounds create mood and reveal character.")],
    [Problem("Find the alliteration in “No warmth could warm, no wintry weather chill him.”", "w sounds: warmth, warm, wintry, weather"), Problem("What pattern repeats in that sentence?", "“No …” (parallelism)"), Problem("Why did Dickens care how his sentences sound?", "He wrote the story to be read aloud and performed it himself.")],
    [S("Warm-Up", [SA("Alliteration repeats…", "beginning consonant sounds"), SA("Parallelism repeats…", "a grammatical pattern")], cols=2),
     S("Analyze Sound", [OR("Read the first paragraph of the passage aloud. Copy one place where Dickens repeats a sound or pattern. What effect does it have?", "Answers vary, e.g. the -ing list sounds harsh and grasping; “The cold within him froze…, nipped…, shrivelled…, stiffened…” builds a chilling picture.", lines=3),
                         OR("Fred describes Christmas as “a kind, forgiving, charitable, pleasant time.” How does the sound of his list compare with the narrator's list about Scrooge?", "Fred's list is soft and warm; the list about Scrooge is harsh. The sounds match their opposite attitudes.", lines=3)], passage=P_FLINT),
     S("Create", [OR("Write a sentence with a list of three or more describing words about a winter day. Use alliteration.", "Answers vary.", lines=2)])],
    te("Students analyze sound and rhythm in prose.", "Analyze the impact of rhymes and other repetitions of sounds on a specific section of a text.", "Workbook Lesson 1.8",
       "Piling up words.", "Read the passage aloud twice, once fast and once slow.", ["Teach alliteration, lists, and parallelism."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Naming the device without its effect."], ["Read aloud and listen."], ["Perform a paragraph of Stave One as Dickens might have."]),
    summary="Sound devices create mood and reveal character.")

# ================================================================= Week 3 · Evidence and inference (Stave Two)
L9 = Lesson("1.9", "Citing Several Pieces of Evidence",
    "I can cite several pieces of textual evidence to support an analysis.", "RL.7.1",
    [("textual evidence", "Quotations or details from the text that support a claim.")],
    "Is one quotation enough to prove that Scrooge is starting to change?",
    [ReaderAssign(CAROL, "Stave Two", "What does Scrooge see from his past? How does he react to each scene?"),
     Text("Grade 7 analysis requires <b>several</b> pieces of evidence. Choose evidence from different parts of the text, and introduce each with a phrase that shows where it comes from (<i>Early in the stave… Later, at Fezziwig's party…</i>)."),
     Example("Build a claim with evidence", "Claim: Scrooge's memories begin to soften him.",
             ["Evidence 1: He weeps to see himself as a lonely boy left at school.", "Evidence 2: He wishes he had given something to the boy singing a carol at his door.", "Evidence 3: After Fezziwig's party, he wishes he could “say a word or two” to his clerk."],
             "Three pieces of evidence from different moments show a pattern of change."),
     KeyIdea("Use several, varied pieces of evidence; show where each comes from.")],
    [Problem("Why use evidence from different parts?", "to show a pattern, not a single moment"), Problem("Introduce a quote with its location.", "e.g. Later in the stave, Scrooge says…"), Problem("Who comes to bring young Scrooge home from school?", "his little sister, Fan")],
    [S("Warm-Up", [SA("Textual evidence =", "quotes or details that support a claim"), SA("How many pieces in Grade 7?", "several (two or more)")], cols=2),
     S("Evidence Collection", [OR("Claim: Scrooge once had people who loved him. Find two pieces of evidence from Stave Two.", "Answers vary; e.g. Fan comes to bring him home; Belle loved him and wanted to marry him; Fezziwig treated him kindly.", lines=4),
                               OR("Claim: Scrooge chose money over love. Find two pieces of evidence.", "Answers vary; Belle says “Another idol has displaced me,” “A golden one”; she says he fears the world too much.", lines=4)]),
     S("Exit Ticket", [OR("Which scene from Scrooge's past affected him most? Give two pieces of evidence.", "Answers vary.", lines=3)])],
    te("Students cite several pieces of evidence.", "Cite several pieces of textual evidence to support analysis.", "Grade 7 Reader: A Christmas Carol (Stave Two), workbook Lesson 1.9",
       "One quote enough?", "Read Stave Two.", ["Model the three-evidence claim."], "Your Turn 1–3.",
       ["Clustering evidence from one scene."], ["Evidence log by scene."], ["Debate: Is Scrooge to blame for becoming a miser?"]),
    summary="Several, varied pieces of evidence build strong analysis.")

L10 = Lesson("1.10", "Inferring Character from Dialogue",
    "I can make inferences about characters from what they say and how others respond.", "RL.7.1, RL.7.3",
    [("subtext", "The meaning beneath what a character actually says.")],
    "When someone says “Nothing” in a quiet voice after a long pause, what do they really mean?",
    [Text("Dickens's narrator tells us a great deal, but some of the most important moments are left for readers to infer from <b>dialogue</b>, <b>actions</b>, and <b>other characters' reactions</b>. Listen for <b>subtext</b>."),
     Figure(lambda t: table(t, [["Character", "What they say or do (Stave Two)", "What we can infer"], ["Scrooge", "After praising Fezziwig, says “Nothing particular,” then wishes to say a word to his clerk", "He is thinking guiltily about how he treats Bob"],
                                ["Fezziwig", "“No more work to-night. Christmas Eve, Dick. Christmas, Ebenezer!”", "He is generous and joyful and treats his apprentices like family"], ["Belle", "“Another idol has displaced me… A golden one.”", "She is hurt but calm; she sees that money now matters more to him than she does"]],
                            [1.0 * inch, 2.6 * inch, 2.1 * inch], width=5.7 * inch, font_size=9)),
     KeyIdea("Infer from dialogue, actions, and reactions; look for subtext.")],
    [Problem("What is subtext?", "meaning beneath the words"), Problem("What does Fezziwig's party show about him?", "He is generous and kind to the people who work for him."), Problem("Why might Scrooge say “Nothing particular”?", "He doesn't want to admit he feels guilty about Bob.")],
    [S("Warm-Up", [SA("Subtext means…", "hidden meaning beneath words"), SA("Who was Scrooge's old employer?", "Fezziwig")], cols=2),
     S("Infer", [OR("Choose one exchange between Scrooge and Belle. What is the subtext?", "Answers vary.", lines=4),
                 OR("How does Scrooge speak to the Ghost of Christmas Past at the end of the stave? What does it suggest about his feelings?", "Answers vary; he begs it to stop showing him more; the memories are painful and he is ashamed.", lines=3)]),
     S("Exit Ticket", [OR("Write one line of dialogue that has subtext. Explain the hidden meaning.", "Answers vary.", lines=2)])],
    te("Students infer from dialogue.", "Analyze how particular elements of a story interact; cite evidence.", "Workbook Lesson 1.10",
       "Nothing.", "Reread key exchanges; read aloud with different tones.", ["Model the inference chart."], "Your Turn 1–3.",
       ["Taking every line literally."], ["Read lines in different tones."], ["Perform the Belle scene two ways."]),
    summary="Infer character from dialogue, actions, and reactions.")

L11 = Lesson("1.11", "Inference in Informational Text",
    "I can draw inferences from an informational text and support them with evidence.", "RI.7.1",
    [],
    "Why might Dickens have thought a story could change more minds than a report?",
    [P_ORIGIN,
     Example("Infer", "Why did Dickens decide to write a story instead of a pamphlet?", ["Evidence: readers “who would ignore a report might be moved by characters they cared about.”", "Reasoning: people feel more for a person than for a statistic."],
             "Dickens believed a story would make readers feel for poor children and act."),
     KeyIdea("Connect several facts to infer what the author implies but doesn't state.")],
    [Problem("What was a ragged school?", "a free school run by volunteers for the poorest children"), Problem("What report did Dickens read in 1843?", "a government report on children working in mines, mills, and workshops"), Problem("How long did it take Dickens to write the story?", "about six weeks")],
    [S("Warm-Up", [SA("Year of the story", "1843"), SA("Dickens's job at age twelve", "pasting labels on pots of boot polish")], cols=2),
     S("Infer with Evidence", [OR("Infer why the ragged school made such a strong impression on Dickens. Cite two details.", "The children were hungry and had never learned to read; it reminded him of his own hard childhood.", lines=3),
                               OR("What can you infer about how Dickens felt about education? Cite evidence.", "He believed it was the best hope for poor children: he argued this in his Manchester speech.", lines=3),
                               OR("How might Dickens's own childhood have shaped A Christmas Carol? Make two connections.", "He worked in a factory as a poor child, as many children in the report did; the story takes the side of poor children like Tiny Tim.", lines=3)], passage=P_ORIGIN),
     S("Exit Ticket", [OR("Which words in paragraph 4 show the author is careful not to claim too much?", "“Many readers believe” / “one reason”", lines=1)])],
    te("Students infer from informational text.", "Cite several pieces of evidence to support inferences drawn from informational text.", "Workbook Lesson 1.11",
       "A story vs a report.", "Read “Why Dickens Wrote A Christmas Carol.”", ["Model the inference."], "Your Turn 1–3.",
       ["Stating facts as inferences."], ["Because X and Y, I infer Z."], ["Research the ragged schools."]),
    summary="Connect facts to infer implied ideas.")

L12 = Lesson("1.12", "Writing a Claim-Evidence-Reasoning Paragraph",
    "I can write an analytical paragraph with a claim, multiple pieces of evidence, and reasoning.", "W.7.9a, W.7.1b",
    [("claim", "An arguable statement that answers the question."), ("reasoning", "Explanation of how the evidence supports the claim.")],
    "What separates a summary from an analysis?",
    [Text("An analytical paragraph makes a <b>claim</b>, supports it with <b>two or three pieces of evidence</b>, and explains each with <b>reasoning</b>. It ends with a <b>concluding sentence</b> that connects back to the claim."),
     Example("CER paragraph", "How does Dickens present Scrooge in Stave One?",
             ["Claim: Scrooge is presented as a man whose greed has cut him off from everyone.", "Evidence 1 + reasoning: “solitary as an oyster.”", "Evidence 2 + reasoning: his words about the poor.", "Conclusion."],
             "In Stave One, Dickens presents Scrooge as a man whose greed has cut him off from other people. The narrator calls him “solitary as an oyster,” a creature shut tight inside a hard shell. When the gentlemen ask him to help the poor, he answers that if they would rather die, they should “decrease the surplus population,” showing that he sees suffering people as numbers. Dickens creates a character so cold that readers wonder whether anything could ever change him."),
     KeyIdea("Claim → evidence → reasoning (repeat) → concluding sentence.")],
    [Problem("Is “Scrooge lives in London” a claim?", "No, it's a fact, not arguable."), Problem("What follows each piece of evidence?", "reasoning"), Problem("What does the concluding sentence do?", "connects back to the claim")],
    [S("Warm-Up", [SA("CER =", "Claim, Evidence, Reasoning"), SA("A claim must be…", "arguable")], cols=2),
     S("Write", [OR("Question: Does Stave Two make the reader pity Scrooge? Write a CER paragraph with at least two pieces of evidence.", "Answers vary.", lines=12,
                    note="Score: claim (1), evidence 1 (1), evidence 2 (1), reasoning (1), conclusion and conventions (1).")])],
    te("Students write CER paragraphs.", "Draw evidence from texts to support analysis; support claims with clear reasons and evidence.", "Workbook Lesson 1.12",
       "Summary vs analysis.", "Gather evidence from Stave Two.", ["Model the paragraph."], "Plan together.",
       ["Summarizing instead of analyzing."], ["Highlight reasoning sentences."], ["Write a counterclaim sentence."], independent="Write the paragraph. Weekly Check tomorrow."),
    summary="Claim, multiple evidence, reasoning, conclusion.")

# ================================================================= Week 4 · Central ideas, theme, development (Stave Three, first section)
L13 = Lesson("1.13", "Theme and Its Development",
    "I can determine a theme and analyze how it develops over the course of a text.", "RL.7.2",
    [("theme", "A message about life or human nature that a text explores."), ("motif", "A repeated image, idea, or symbol that supports a theme.")],
    "What ideas keep coming up in A Christmas Carol so far?",
    [ReaderAssign(CAROL, "Stave Three (first section)", "What does the Ghost of Christmas Present show Scrooge? How do the Cratchits celebrate with so little?"),
     Text("Grade 7 readers track how a theme <b>develops</b>: how it is introduced, how events and characters complicate it, and how it is resolved. Recurring <b>motifs</b> (cold and warmth, chains, money, light) point to themes."),
     Figure(lambda t: table(t, [["Possible theme topic", "Evidence so far (Staves 1–3)"], ["generosity vs greed", "Scrooge refuses to give; Fezziwig and Fred give freely; the Cratchits share a small dinner joyfully"],
                                ["isolation", "“solitary as an oyster”; Scrooge alone at school; Belle leaves him"], ["the chance to change", "Marley warns Scrooge he still has “a chance and hope”; Scrooge weeps and wishes he had been kinder"]],
                            [1.7 * inch, 3.9 * inch], width=5.6 * inch, font_size=9)),
     Example("Develop a theme statement", "Topic: greed", ["Introduced: Scrooge's coldness and Marley's chain.", "Repeated: Belle says money has become Scrooge's idol.", "Complicated: the poor Cratchits, with almost nothing, are happier than rich Scrooge."], "Theme: Greed cuts people off from the love and joy that make life worth living."),
     KeyIdea("Track a theme through introduction, repetition, and complication; state it as a full sentence.")],
    [Problem("What is a motif?", "a repeated image or idea that supports a theme"), Problem("How does Stave Three develop the greed theme?", "The poor Cratchits are joyful and generous with very little, while rich Scrooge is miserable."), Problem("Write a theme about generosity.", "e.g. Generosity brings joy to the giver as well as to the receiver.")],
    [S("Warm-Up", [SA("A theme is a ___, not a topic.", "message / statement"), SA("Motif example in A Christmas Carol", "cold and warmth, chains, money")], cols=2),
     S("Trace a Theme", [OR("Choose a theme topic. Write a theme statement.", "Answers vary.", lines=2), OR("Evidence where it is introduced (Stave One):", "Answers vary.", lines=2),
                         OR("Evidence where it is repeated or complicated (Staves Two–Three):", "Answers vary.", lines=2), OR("How has the theme developed?", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("How does the Ghost of Christmas Present turn Scrooge's own words against him when Scrooge asks if Tiny Tim will live?", "The Ghost repeats Scrooge's line that if he is like to die, he had better do it and “decrease the surplus population,” making Scrooge ashamed.", lines=2)])],
    te("Students analyze theme development.", "Determine a theme and analyze its development over the course of the text.", "Grade 7 Reader: A Christmas Carol (Stave Three, first section), workbook Lesson 1.13",
       "Recurring ideas.", "Read the first section of Stave Three.", ["Model tracing greed."], "Your Turn 1–3.",
       ["One-word themes."], ["Theme frame: Topic + what the text says about it."], ["Track a motif across the whole story."]),
    summary="Themes develop through introduction, repetition, and complication.")

L14 = Lesson("1.14", "Central Ideas in Informational Text",
    "I can determine two or more central ideas and analyze their development.", "RI.7.2",
    [("central idea", "A main idea that the author develops in a text.")],
    "Can an article have more than one main idea?",
    [Text("Longer informational texts often develop <b>two or more central ideas</b>. Identify each and trace how details develop it."),
     Example("Two central ideas", "“Why Dickens Wrote A Christmas Carol”", ["Central idea 1: Dickens was moved by the suffering of poor children in 1843 (paragraphs 1–2).", "Central idea 2: He chose to answer that suffering with a story, shaped by his own childhood (paragraphs 3–4)."],
             "The article develops both the problem Dickens saw and the way he chose to respond."),
     KeyIdea("Name each central idea; trace the details that develop it.")],
    [Problem("Which paragraphs describe what Dickens saw?", "1–2"), Problem("Which paragraph connects to his childhood?", "4"), Problem("Central idea of “Christmas in Dickens's London”", "London had great wealth and great poverty, and poor families worked hard to celebrate Christmas.")],
    [S("Warm-Up", [SA("Central idea =", "a main idea the author develops"), SA("Can a text have two?", "Yes")], cols=2),
     S("Analyze", [OR("Identify two central ideas in “Christmas in Dickens's London.” Cite a detail for each.", "1) Many Londoners were very poor: one damp room; workhouses. 2) Christmas was becoming a bigger celebration: goose clubs, bakers' ovens, the first Christmas card.", lines=4),
                   OR("How do the two ideas work together?", "Even very poor families saved and planned for Christmas, which shows how much the holiday meant, and why Dickens set his story then.", lines=3)], passage=P_LONDON),
     S("Exit Ticket", [OR("Write a one-sentence statement combining both central ideas of “Why Dickens Wrote A Christmas Carol.”", "Moved by the suffering of poor children and his own memories, Dickens wrote a story instead of a pamphlet to change readers' hearts.", lines=2)])],
    te("Students determine multiple central ideas.", "Determine two or more central ideas and analyze their development.", "Workbook Lesson 1.14",
       "More than one main idea?", "Reread both informational texts.", ["Model two central ideas."], "Your Turn 1–3.",
       ["Choosing one detail as a central idea."], ["Paragraph-grouping chart."], ["Find central ideas in a news article."]),
    summary="Identify and trace multiple central ideas.")

L15 = Lesson("1.15", "Writing an Objective Summary",
    "I can write an objective summary of a text.", "RL.7.2, RI.7.2",
    [("objective", "Neutral; without personal opinions or judgments.")],
    "What's the difference between “Scrooge is a horrible man who hates the poor” and “Scrooge refuses to give money to help the poor”?",
    [Text("An <b>objective summary</b> states the central idea or theme and key events in your own words, in order, without opinions, judgments, or minor details."),
     Example("Objective vs subjective", "Stave Two summary", ["Subjective: The wonderful Ghost shows heartless Scrooge his sad, lonely past…", "Objective: The Ghost of Christmas Past shows Scrooge scenes from his life: his lonely boyhood, his sister Fan, Fezziwig's party, and Belle ending their engagement because he loves money more."],
             "Objective summaries report; they don't judge."),
     KeyIdea("Objective = neutral, concise, central idea + key events, own words.")],
    [Problem("Objective or not: “Fezziwig throws an amazing party.”", "Not objective (“amazing” judges)"), Problem("Should an objective summary include “I think”?", "No"), Problem("What goes first?", "the central idea or theme")],
    [S("Warm-Up", [SA("Objective means…", "neutral, without opinion"), SA("A summary is ___ than the text.", "shorter")], cols=2),
     S("Revise to Objective", [SA(q, a) for q, a in [("The cruel Scrooge makes poor Bob work with a tiny fire.", "Scrooge keeps Bob's fire very small."), ("Sweet Fan joyfully rescues her brother.", "Fan comes to bring her brother home."),
                                                      ("The kind, wise Belle sadly leaves greedy Scrooge.", "Belle ends her engagement to Scrooge.")]], cols=1),
     S("Summarize", [OR("Write an objective summary of Staves One and Two of A Christmas Carol (5–7 sentences).", "Answers vary; neutral, key events in order.", lines=8)])],
    te("Students write objective summaries.", "Provide an objective summary of the text.", "Workbook Lesson 1.15",
       "Judgment vs report.", "Skim Staves One and Two.", ["Model objective revision."], "Your Turn 1–3.",
       ["Loaded adjectives."], ["Circle judgment words."], ["Summarize a news article objectively."]),
    summary="Objective summaries are neutral and concise.")

L16 = Lesson("1.16", "How Setting Shapes Characters and Plot",
    "I can analyze how elements of a story interact, such as how setting shapes characters and plot.", "RL.7.3",
    [],
    "Why does it matter that A Christmas Carol takes place in a cold, foggy London on Christmas Eve?",
    [Text("Setting can create conflict, limit choices, and reveal character. Dickens's London is full of fog, cold, and poverty, but also of bright shops and warm homes. Christmas is the one time of year when Scrooge's coldness stands out most."),
     Example("Analyze interaction", "How does the setting shape the story?", ["Time: Christmas Eve, when everyone else is celebrating, makes Scrooge's meanness obvious.", "Place: the foggy, freezing counting-house matches Scrooge's cold heart, while the Cratchits' small, warm home matches their love.", "Effect: the contrast between cold and warm places shows what Scrooge is missing."],
             "The Christmas setting and the contrast between cold and warm places reveal Scrooge's character and set up his journey."),
     KeyIdea("Analyze how setting creates conflict, limits choices, and reveals character.")],
    [Problem("How does Christmas Eve affect the way readers see Scrooge?", "His meanness stands out because everyone else is generous and joyful."), Problem("How is the Cratchits' home different from Scrooge's office?", "It is small and poor but warm and full of love; the office is cold and gloomy."), Problem("How did London's poverty shape Dickens's purpose?", "He wanted readers to care about the poor people all around them.")],
    [S("Warm-Up", [SA("Setting =", "time and place"), SA("Setting of A Christmas Carol", "London, Christmas Eve and Christmas Day, 1840s")], cols=2),
     S("Analyze", [OR("How does the setting shape two different characters? Use evidence.", "Answers vary; e.g. Scrooge's cold counting-house matches his cold heart; the Cratchits make their small home warm and joyful.", lines=5)]),
     S("Exit Ticket", [OR("How would A Christmas Carol change if it took place in July?", "Scrooge's refusal to celebrate wouldn't stand out; the ideas of charity, family, and the cold of poverty would lose their force.", lines=3)])],
    te("Students analyze setting's effect.", "Analyze how particular elements of a story or drama interact.", "Workbook Lesson 1.16, Unit 1 Review",
       "Why Christmas Eve?", "Revisit descriptions of fog, cold, and warm homes.", ["Model the analysis."], "Your Turn 1–3.",
       ["Describing setting without analyzing effect."], ["Setting → effect chart."], ["Compare with another story set at a holiday."], independent="Workbook and the Unit 1 Review.", exit_="Tomorrow: Unit 1 Test."),
    summary="Setting creates conflict, limits choices, and reveals character.")

# ================================================================= checks
C1 = Check("Weekly Check 1: Words and Roots", [S("Read and answer", [
    OR("What does <i>unsentimental</i> mean? Use the prefix and context.", "un- = not; not emotional; brief and factual entries", lines=2),
    OR("What does <i>terse</i> mean? What clue helps?", "brief, using few words; “brief” entries and the short quoted line", lines=2),
    OR("What does <i>harrowing</i> mean in paragraph 2?", "deeply disturbing, distressing", lines=1),
    SA("<i>archive</i>: part of speech", "noun"), SA("Root of <i>describe</i> and meaning", "scrib/script: write"),
    OR("Why is the entry “Four not.” so powerful? Use the word <i>restraint</i>.", "Her restraint, saying so little about four deaths, makes the tragedy feel heavier.", lines=2)], passage=P_CHECK1)], minutes=20)
C2 = Check("Weekly Check 2: Connotation and Figurative Language", [S("Read and answer", [
    OR("What is the connotation of “junk” in Derek's line? What does it reveal about him?", "negative; he looks down on the gift and on Mira", lines=2),
    OR("Explain the metaphor “the one who got the treasure.”", "The letters' story is more valuable than money or property.", lines=2),
    MC("Which word has the most positive connotation?", ["old", "antique", "worn-out"], 1),
    OR("Complete: house : cousins :: letters : ___", "Mira", lines=1),
    OR("How does the contrast between the cousins and Mira develop the theme?", "They value material things; Mira values the story and wisdom, showing real treasure is not material.", lines=3)], passage=P_CHECK2)], minutes=20)
C3 = Check("Weekly Check 3: Evidence and Inference", [S("Read and answer", [
    OR("Why does Mr. Okafor plant so many tomatoes? Cite two details.", "To give them away to neighbors in need: bags on doorsteps; the widow, the family, the teenager.", lines=3),
    OR("What can you infer about why he never lets anyone see him deliver them?", "He is humble and doesn't want credit or to embarrass people.", lines=2),
    OR("Explain his statement “A garden is too big a thing for one person.”", "Its abundance is meant to be shared with the community.", lines=2),
    OR("Write a CER claim about Mr. Okafor's character.", "e.g. Mr. Okafor is quietly generous.", lines=1)], passage=P_CHECK3)], minutes=20)

REVIEW = Check("Unit 1 Review", [
    S("Vocabulary", [SA("humbug =", "nonsense"), SA("bene =", "good"), SA("Connotation of <i>stubborn</i>", "negative"), SA("miser : skinflint relationship", "synonyms"),
                     SA("Device: solitary as an oyster", "simile"), SA("Parallelism repeats…", "a grammatical pattern")], cols=2),
    S("Reading and writing", [OR("Write a theme statement about greed in A Christmas Carol and one piece of evidence.", "Answers vary.", lines=3),
                              OR("Revise to be objective: The heartless Scrooge cruelly refused the kind gentlemen.", "Scrooge refused to give money to the gentlemen collecting for the poor.", lines=1)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 1 Test", [
    S("Part A · Vocabulary (1 point each)", [
        OR("What does <i>resented</i> mean in paragraph 3? What clue helps?", "felt bitter or upset about; she spent afternoons in waiting rooms while classmates played", lines=2),
        MC("Which word in paragraph 2 has a negative connotation?", ["carefully", "impatiently", "translated"], 1),
        OR("Explain the metaphor of the backpack.", "Translating was an invisible burden or responsibility she carried.", lines=2),
        OR("Explain the metaphor “It was a bridge.”", "Translating connected her family to their new world and helped them cross into it.", lines=2),
        SA("Prefix and meaning in <i>translator</i>", "trans-: across; one who carries words across languages")], passage=P_TEST),
    S("Part B · Evidence and inference (1 point each)", [
        OR("What can you infer about why Ana sometimes “softened” her teachers' notes?", "She wanted to protect herself or her parents from worry or criticism.", lines=2),
        OR("What does her father's statement reveal about how he feels? Cite evidence.", "Grateful and moved: “Today you were my voice”; his eyes were bright.", lines=2),
        OR("How does Ana change? Cite evidence from the beginning and the end.", "From resenting translating (classmates at soccer) to seeing it as meaningful and volunteering to help others.", lines=3, points=2)]),
    S("Part C · Theme and summary (1 point each)", [
        OR("State a theme of the story.", "e.g. Responsibilities that feel like burdens can also give our lives purpose.", lines=2),
        OR("Explain how the theme develops from paragraph 3 to paragraph 5.", "Burden and resentment → father's gratitude → Ana sees purpose and chooses to help others.", lines=3),
        OR("Write an objective summary of the story (3–4 sentences).", "After moving from Colombia to Ohio, eleven-year-old Ana becomes her family's translator. At first she resents the responsibility. After helping her father with a job interview, she realizes her role is important, and she volunteers to help other newcomers.", lines=5, points=2)]),
    S("Part D · Analytical writing (5 points)", [OR("Write a CER paragraph: How does the author use the backpack metaphor to show Ana's growth? Include at least two pieces of evidence.",
                                                   "Rubric: claim (1); evidence 1 (1); evidence 2 (1); reasoning (1); conclusion and conventions (1).", lines=12, points=5)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-10-12", "2026-10-19", "2026-10-26", "2026-11-02"], CHECKS, REVIEW, TEST)

UNIT = Unit(1, "Language and Meaning", "Dickens's language, roots and context, connotation and figurative language, evidence and inference, theme and objective summary, with A Christmas Carol, Introduction–Stave Three.",
    "A cold-hearted miser, a ghost in chains, and three Spirits who visit on Christmas Eve: <i>A Christmas Carol</i> is one of the most famous stories ever written. In this unit you'll learn to read Dickens's language with confidence, unlock words with roots and context, analyze connotation and figurative language, support inferences with several pieces of evidence, and trace themes as they develop.",
    ["Read a classic novella's language using translation strategies.", "Use roots, affixes, context, and reference tools to determine meaning.", "Analyze connotation, figurative language, word relationships, and sound.",
     "Cite several pieces of evidence to support inferences and claims.", "Determine and trace themes and central ideas; write objective summaries."],
    [("RL.7.1–5, RI.7.1–2", "Cite evidence; determine themes and central ideas; analyze elements, word choice, and form."), ("L.7.4–5", "Determine word meanings; interpret figurative language and connotation."),
     ("W.7.1b, W.7.9", "Support claims with evidence; draw evidence from texts.")],
    [("archaic", "No longer in common use."), ("connotation", "The feeling a word carries."), ("simile", "A comparison using like or as."), ("theme", "A message about life."),
     ("objective summary", "A neutral, concise retelling."), ("parallelism", "Repeating a grammatical pattern.")],
    ["Grade 6 reading and writing skills."], ["Grade 7 Reader: A Christmas Carol (Introduction–Stave Three)", "Dictionary with etymologies", "Highlighters"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Dickens wrote this story to change how readers treated the poor, and it worked; analyzing connotation and figurative language helps you see how ads, speeches, and news shape opinion today.",
    family_note="Read a page of Stave One aloud together, giving Scrooge and Fred different voices, or watch a short clip of a stage version.",
    weeks=WEEKS)
