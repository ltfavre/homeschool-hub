"""Grade 7 ELA · Unit 1: Language and Meaning in The Tempest — roots and context, connotation and figurative language, evidence and inference, theme and summary.
Anchor reading: The Tempest Reader, Introduction through Act 2 (Oct 12 – Nov 6, 2026)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule

TEMPEST = "The Tempest Reader"

# ================================================================= passages (Shakespeare excerpts are public domain; others original)
P_SC1 = Passage("From The Tempest, Act 1, Scene 1 (original text)", [
    "<b>MASTER.</b> Boatswain!",
    "<b>BOATSWAIN.</b> Here, master: what cheer?",
    "<b>MASTER.</b> Good, speak to the mariners: fall to't, yarely, or we run ourselves aground: bestir, bestir.",
    "<i>(Exit. Enter Mariners.)</i>",
    "<b>BOATSWAIN.</b> Heigh, my hearts! cheerly, cheerly, my hearts! yare, yare! Take in the topsail. Tend to the master's whistle.",
], source="William Shakespeare, The Tempest (c. 1611). Public domain.", genre="Drama excerpt", numbered=False)

P_ARIEL = Passage("Ariel's Song, Act 1, Scene 2 (original text)", [
    "> Full fathom five thy father lies;\\nOf his bones are coral made;\\nThose are pearls that were his eyes:\\nNothing of him that doth fade,\\nBut doth suffer a sea-change\\nInto something rich and strange.",
], source="William Shakespeare, The Tempest. Public domain.", genre="Song from a play", numbered=False)

P_GLOBE = Passage("Theater in Shakespeare's London", [
    "In the early 1600s, going to a play was one of the most popular entertainments in London. Theaters such as the Globe were round, open-air buildings that could hold as many as three thousand people.",
    "Wealthy playgoers paid more to sit in covered galleries. Poorer audience members, called <b>groundlings</b>, paid a penny to stand in the open yard right in front of the stage. They often shouted, laughed, and ate during the performance.",
    "Plays were performed in the afternoon, using daylight instead of stage lights. There was little scenery, so playwrights used words to paint the setting. When a character in <i>The Tempest</i> describes a storm or an enchanted island, the audience had to picture it in their imaginations.",
    "All of the actors were men or boys. Young male actors played female characters such as Miranda. Because of this, many audiences of the time thought nothing unusual about a boy playing a young woman.",
], source="An original informational text", genre="Informational text")

P_SEAVENTURE = Passage("The Real Shipwreck Behind The Tempest", [
    "In 1609, a ship called the <i>Sea Venture</i> sailed from England toward the young colony of Jamestown in Virginia. It carried about 150 people, including the colony's new leaders.",
    "Near the islands of Bermuda, a powerful hurricane struck. For days, the crew bailed water as the ship leaked badly. At last, the captain deliberately drove the ship onto a reef near the shore. Astonishingly, everyone aboard survived.",
    "Sailors had long feared Bermuda; some called it the “Isle of Devils” because of its dangerous reefs and strange night noises, which turned out to be birds. Yet the castaways found fresh water, fish, wild pigs, and birds to eat. Over about ten months, they built two new ships from the wreck and the island's cedar trees and finally sailed on to Jamestown.",
    "When news of the survivors reached London in 1610, written accounts of the wreck became popular. Many scholars believe Shakespeare read at least one of these accounts. Within a year or two, he wrote <i>The Tempest</i>, a play that begins with a terrible storm and a shipwreck on a mysterious island.",
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


# ================================================================= Week 1 · Roots, affixes, and context clues (Intro, Prologue, Act 1 Scene 1)
L1 = Lesson("1.1", "Reading Shakespeare's Language",
    "I can use strategies to read and understand Shakespeare's language.", "RL.7.4, RL.7.5",
    [("drama", "A story written to be performed, told through dialogue and stage directions."), ("archaic", "Old-fashioned; no longer in common use."),
     ("inverted syntax", "Word order that differs from normal English, such as putting the verb before the subject.")],
    "Read this line aloud: “Good, speak to the mariners: fall to't, yarely, or we run ourselves aground.” What do you think is happening?",
    [ReaderAssign(TEMPEST, "Introduction, Characters, Prologue, and Act 1, Scene 1", "Who is on the ship? What is happening to it?"),
     Text("Shakespeare wrote about 400 years ago. His English is <i>Early Modern English</i>, not Old English, so most words are familiar. Three strategies help: <b>read aloud</b> for meaning, <b>translate archaic words</b>, and <b>untangle inverted syntax</b>."),
     Figure(lambda t: table(t, [["Shakespeare", "Modern English"], ["thou / thee / thy / thine", "you (subject) / you (object) / your / yours"], ["art / dost / doth / hath", "are / do / does / has"],
                                ["'tis / 't", "it is / it"], ["yare / yarely", "quick / quickly"], ["wherefore", "why"], ["hence / hither / thither", "from here / to here / to there"]], [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     P_SC1,
     Example("Translate a line", "“Good, speak to the mariners: fall to't, yarely, or we run ourselves aground: bestir, bestir.”",
             ["Good = good man (the Master is addressing the Boatswain).", "fall to't = get to it; yarely = quickly.", "run ourselves aground = crash onto land.", "bestir = get moving."],
             "“Tell the sailors to get to work quickly, or we'll crash onto the shore. Move, move!”"),
     KeyIdea("Read aloud, translate archaic words, and untangle word order. Meaning first, then details.")],
    [Problem("Translate “Here, master: what cheer?”", "I'm here, captain. What's the situation?"), Problem("What does “thy” mean?", "your"), Problem("What is happening in Scene 1?", "A ship is caught in a violent storm and the crew struggles to save it.")],
    [S("Warm-Up", [SA("thou =", "you"), SA("hath =", "has")], cols=2),
     S("Translate", [OR(f"“{q}”", a, lines=2) for q, a in [("Heigh, my hearts! cheerly, cheerly, my hearts! yare, yare!", "Come on, my friends! Cheer up! Quickly, quickly!"),
                                                           ("Take in the topsail. Tend to the master's whistle.", "Lower the top sail. Listen for the captain's whistle."),
                                                           ("Wherefore dost thou weep?", "Why are you crying?"), ("Thy father was the Duke of Milan.", "Your father was the Duke of Milan.")]], passage=P_SC1),
     S("Act 1, Scene 1", [OR("Why do you think Shakespeare starts the play in the middle of a storm? What effect does it have on the audience?", "It grabs attention immediately and creates tension and chaos; the audience wants to know who survives.", lines=4)]),
     S("Exit Ticket", [OR("Which reading strategy helped you most today? Give an example.", "Answers vary.", lines=2)])],
    te("Students apply strategies to Shakespeare's language.", "Determine the meaning of words and phrases; analyze how a drama's form contributes to meaning.", "The Tempest Reader (Intro–Act 1.1), workbook Lesson 1.1",
       "Read the Master's line aloud; predict.", ["Read the Reader introduction and character list.", "Read Act 1.1 aloud in parts."], ["Teach the translation chart.", "Model the Master's line."], "Your Turn 1–3.",
       ["Assuming Shakespeare is a different language."], ["Act it out; tone reveals meaning."], ["Memorize and perform four lines."]),
    summary="Read aloud, translate archaic words, untangle word order.")

L2 = Lesson("1.2", "Greek and Latin Roots and Affixes",
    "I can use Greek and Latin roots and affixes to determine word meanings.", "L.7.4b",
    [("root", "A word part that carries the core meaning."), ("affix", "A prefix or suffix.")],
    "What do <i>benefit</i>, <i>benevolent</i>, and <i>benefactor</i> have in common?",
    [Figure(lambda t: table(t, [["Root / affix", "Meaning", "Examples"], ["bene", "good, well", "benefit, benevolent, benefactor"], ["mal", "bad", "malice, malfunction, malevolent"], ["bell", "war", "rebel, belligerent, bellicose"],
                                ["voc / vok", "voice, call", "vocal, invoke, revoke"], ["dict", "say", "predict, contradict, verdict"], ["spect", "look", "spectator, inspect, perspective"],
                                ["ject", "throw", "reject, project, eject"], ["-ous / -ose", "full of", "dangerous, bellicose"], ["-cide", "kill", "pesticide, insecticide"]], [1.2 * inch, 1.4 * inch, 3.0 * inch], width=5.6 * inch, font_size=9)),
     Example("Analyze a word", "What does <i>malevolent</i> mean?", ["mal = bad.", "vol = wish (as in voluntary).", "-ent = having the quality of."], "wishing harm to others; evil-minded"),
     KeyIdea("Break a word into parts, combine meanings, then check the context.")],
    [Problem("<i>benevolent</i>", "wishing good; kind"), Problem("<i>belligerent</i>", "eager to fight; hostile"), Problem("<i>spectator</i>", "a person who watches")],
    [S("Warm-Up", [SA("mal =", "bad"), SA("spect =", "look")], cols=2),
     S("Word Analysis", [SA(w, a) for w, a in [("malfunction", "fail to work properly"), ("contradict", "say the opposite"), ("introspective", "looking inward at oneself"), ("projectile", "an object thrown or launched"),
                                               ("invoke", "call upon"), ("benefactor", "a person who does good / gives help"), ("rebellion", "an uprising; a war against authority"), ("malicious", "full of ill will")]], cols=2),
     S("Context Check", [OR("Prospero was the Duke of Milan until his brother rebelled against him. Explain how the root of <i>rebel</i> fits.", "bell = war; a rebel fights against authority, as Antonio fought to take Prospero's power.", lines=3)]),
     S("Exit Ticket", [OR("Choose a root from the chart and write three words that contain it.", "Answers vary.", lines=2)])],
    te("Students analyze Greek and Latin roots.", "Use common, grade-appropriate Greek or Latin affixes and roots as clues to meaning.", "Workbook Lesson 1.2",
       "bene words.", "Skim the Reader introduction for root words.", ["Teach the root chart.", "Model malevolent."], "Your Turn 1–3.",
       ["Over-relying on roots without checking context."], ["Word-part sums."], ["Start a root journal."]),
    summary="Roots and affixes unlock meaning; confirm with context.")

L3 = Lesson("1.3", "Context Clues in Complex Texts",
    "I can use context to determine the meaning of words and phrases in complex texts.", "L.7.4a, RL.7.4",
    [],
    "In “The groundlings, who paid a penny to stand, often shouted during plays,” what are groundlings?",
    [Text("Complex texts often define words indirectly. Use the <b>sentence</b>, the <b>paragraph</b>, and the <b>overall meaning</b>. Clues include definitions, restatements, examples, contrasts, and cause-effect relationships."),
     P_GLOBE,
     Example("Use paragraph context", "What were groundlings?", ["Paragraph 2 contrasts them with wealthy playgoers in galleries.", "They “paid a penny to stand in the open yard.”"], "poorer audience members who stood in the yard"),
     KeyIdea("Use the sentence, the paragraph, and the passage's overall meaning to figure out unfamiliar words.")],
    [Problem("What were galleries?", "covered seating areas for wealthier playgoers"), Problem("Why did playwrights “paint the setting” with words?", "There was little scenery or lighting."), Problem("What context clue shows how big the Globe was?", "it could hold as many as three thousand people")],
    [S("Warm-Up", [SA("Context means…", "surrounding words and sentences"), SA("A contrast signal word", "but, however, unlike")], cols=2),
     S("Use the Passage", [OR("What does “open-air” mean in paragraph 1? What clue helps?", "without a roof; “using daylight” and “open yard” later", lines=2),
                           OR("Explain how the lack of scenery affected the way Shakespeare wrote.", "He described settings in dialogue so audiences could imagine them.", lines=3),
                           MC("“Thought nothing unusual about” (paragraph 4) means the audiences…", ["found it shocking", "accepted it as normal", "did not notice the actors"], 1)], passage=P_GLOBE),
     S("Context in The Tempest", [OR("Find a word in Act 1 that you didn't know. Write the line, the clue, and your definition.", "Answers vary.", lines=4)])],
    te("Students use context in complex texts.", "Use context as a clue to the meaning of a word or phrase.", "Workbook Lesson 1.3",
       "Groundlings.", "Read “Theater in Shakespeare's London.”", ["Model paragraph-level context."], "Your Turn 1–3.",
       ["Looking only at the immediate sentence."], ["Read one sentence before and after."], ["Find context clues in the Reader footnotes."]),
    summary="Use sentence, paragraph, and passage context.")

L4 = Lesson("1.4", "Reference Tools and Word Origins",
    "I can use dictionaries, glossaries, and footnotes to find meanings, pronunciations, parts of speech, and origins.", "L.7.4c, L.7.4d",
    [("etymology", "The origin and history of a word."), ("footnote", "A note at the bottom of a page that explains a word or reference.")],
    "Where would you look to find out what “boatswain” means and how to say it?",
    [Text("Dictionaries give <b>pronunciation</b>, <b>part of speech</b>, <b>definitions</b>, and <b>etymology</b>. Annotated editions of Shakespeare use <b>footnotes</b> or side glosses. Always check your inferred meaning against a reference."),
     Example("Read a dictionary entry", "boatswain (BOH-sun), noun. A ship's officer in charge of equipment and the crew. [Middle English bot (boat) + swein (servant)]",
             ["Pronunciation: BOH-sun (not boat-swain).", "Part of speech: noun.", "Etymology: “boat servant.”"], "A boatswain is the officer who manages the crew and equipment; the word means “boat servant.”"),
     KeyIdea("Use references to confirm meanings, pronunciation, part of speech, and word origins.")],
    [Problem("How is <i>boatswain</i> pronounced?", "BOH-sun"), Problem("What does etymology tell you?", "a word's origin and history"), Problem("Where does a footnote appear?", "at the bottom of the page")],
    [S("Warm-Up", [SA("Etymology =", "word origin"), SA("Part of speech for <i>tempest</i>", "noun")], cols=2),
     S("Use a Dictionary", [OR(f"Look up <i>{w}</i>. Write its part of speech, a definition that fits The Tempest, and its origin.", a, lines=2) for w, a in [
         ("tempest", "noun; a violent storm; from Latin tempestas (season, weather, storm)"), ("usurp", "verb; to seize power wrongfully; from Latin usurpare (to take possession of)"),
         ("enchant", "verb; to put under a spell; from Latin incantare (to chant a spell)")]]),
     S("Footnotes", [OR("Find two footnotes or glosses in the Reader for Act 1. Copy the word and the explanation.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Why might a word's etymology help you remember its meaning?", "Knowing the parts and history connects the word to familiar ideas.", lines=2)])],
    te("Students use reference materials.", "Consult reference materials to find pronunciation and clarify meaning or part of speech; verify inferred meanings.", "Dictionary (print or online), workbook Lesson 1.4",
       "Boatswain.", "Read Act 1.1 footnotes.", ["Model the entry."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Choosing the first definition without checking fit."], ["Test each definition in the sentence."], ["Trace the etymology of five Tempest words."]),
    summary="References confirm meaning, pronunciation, part of speech, and origin.")

# ================================================================= Week 2 · Vocabulary in context (Act 1 Scene 2, first section)
L5 = Lesson("1.5", "Connotation and Denotation",
    "I can distinguish between the denotation and connotation of words.", "L.7.5c, RL.7.4",
    [("denotation", "A word's dictionary meaning."), ("connotation", "The feelings or associations a word carries: positive, negative, or neutral.")],
    "Would you rather be called <i>thrifty</i> or <i>stingy</i>? Don't they mean the same thing?",
    [ReaderAssign(TEMPEST, "Act 1, Scene 2 (first section)", "How does Prospero describe his brother Antonio? Which words show his feelings?"),
     Text("Words with similar <b>denotations</b> can have very different <b>connotations</b>. Writers choose words to shape how readers feel."),
     P_CONNOTE,
     Example("Compare connotations", "cozy vs cramped", ["Denotation: both mean small.", "Connotation: cozy = warm, comfortable (positive); cramped = uncomfortably tight (negative)."], "Same size, opposite feeling."),
     KeyIdea("Same denotation, different connotation. Word choice shapes the reader's feelings.")],
    [Problem("Connotation of “relaxed” vs “sleepy”", "relaxed: positive; sleepy: negative (dull)"), Problem("Connotation of “generous” vs “excessive”", "generous: positive; excessive: negative"), Problem("Which review is more favorable?", "Review A")],
    [S("Warm-Up", [SA("Denotation =", "dictionary meaning"), SA("Connotation =", "feelings a word carries")], cols=2),
     S("Positive, Negative, or Neutral?", [SA(f"{a} / {b} / {c}", ans) for a, b, c, ans in [("curious", "nosy", "interested", "positive / negative / neutral"), ("confident", "arrogant", "sure", "positive / negative / neutral"),
                                                                                       ("slender", "skinny", "thin", "positive / negative / neutral"), ("determined", "stubborn", "persistent", "positive / negative / neutral")]], cols=1),
     S("Prospero's Words", [OR("Copy two words or phrases Prospero uses about Antonio in Act 1.2. Explain their connotation and what they reveal.", "Answers vary, e.g. “perfidious” / “false brother”: negative; he feels betrayed and bitter.", lines=4)]),
     S("Exit Ticket", [OR("Rewrite Review B's first sentence with positive connotations.", "e.g. The Harbor Grill is an intimate little spot with a peaceful atmosphere.", lines=2)])],
    te("Students distinguish connotation and denotation.", "Distinguish among the connotations of words with similar denotations.", "The Tempest Reader (Act 1.2), workbook Lesson 1.5",
       "Thrifty vs stingy.", ["Read Act 1.2 (first part).", "Read the two reviews."], ["Model cozy/cramped."], "Your Turn 1–3.",
       ["Assuming synonyms are interchangeable."], ["Connotation thermometer."], ["Rewrite an ad with negative connotations."]),
    summary="Connotation shapes feeling beyond the dictionary meaning.")

L6 = Lesson("1.6", "Figurative Language: Metaphor, Personification, and Allusion",
    "I can interpret figurative language and explain its effect.", "L.7.5a, RL.7.4",
    [("personification", "Giving human qualities to something not human."), ("allusion", "A reference to a well-known person, place, event, or text."), ("extended metaphor", "A metaphor developed over several lines.")],
    "What does Shakespeare mean when Ariel sings that “those are pearls that were his eyes”?",
    [P_ARIEL,
     Example("Interpret", "“Those are pearls that were his eyes.”", ["Literal: the drowned man's eyes have turned to pearls.", "Figurative: the sea has transformed him into something beautiful and strange.", "Effect: death is described as magical change, not horror."],
             "The metaphor turns a drowning into a mysterious, beautiful transformation."),
     Text("<b>Sea-change</b>: Ariel's phrase is now an English idiom meaning a complete transformation, showing how Shakespeare's language still shapes ours."),
     KeyIdea("Identify the device, explain the comparison, then explain its effect on meaning or mood.")],
    [Problem("Device in “Of his bones are coral made”", "metaphor"), Problem("What does “sea-change” mean today?", "a complete transformation"), Problem("Mood of Ariel's song", "mysterious, eerie, beautiful")],
    [S("Warm-Up", [SA("Personification gives ___ qualities.", "human"), SA("An allusion refers to…", "something well known")], cols=2),
     S("Interpret", [OR(f"“{q}” Device and meaning:", a, lines=2) for q, a in [("The wind howled its fury at the ship.", "personification: the wind is violent, as if angry"),
                                                                             ("Her silence was a locked door.", "metaphor: she refused to share her feelings"), ("He thinks he's a Hercules.", "allusion: he thinks he's very strong"),
                                                                             ("The island whispered secrets to the wind.", "personification: the island seems mysterious and alive")]]),
     S("Ariel's Song", [OR("How does Ariel's song make Ferdinand's father's “death” seem? Use two lines.", "Beautiful and magical rather than horrible: “pearls that were his eyes,” “something rich and strange.”", lines=4)], passage=P_ARIEL),
     S("Exit Ticket", [OR("Write a metaphor or personification about the storm in Act 1.", "Answers vary.", lines=2)])],
    te("Students interpret figurative language.", "Interpret figures of speech in context; analyze the impact of word choices.", "Workbook Lesson 1.6",
       "Pearls for eyes.", "Read Ariel's song aloud.", ["Model interpreting the metaphor.", "Explain sea-change."], "Your Turn 1–3.",
       ["Identifying the device but not its effect."], ["Device → meaning → effect frame."], ["Find three Shakespeare phrases still used today."]),
    summary="Device → comparison → effect.")

L7 = Lesson("1.7", "Word Relationships and Analogies",
    "I can use relationships between words to understand each word better.", "L.7.5b",
    [("analogy", "A comparison of two pairs of words that share the same relationship.")],
    "Complete: <i>Captain is to ship as king is to ___.</i>",
    [Figure(lambda t: table(t, [["Relationship", "Example"], ["synonyms", "tempest : storm"], ["antonyms", "loyal : treacherous"], ["part to whole", "sail : ship"], ["cause to effect", "storm : shipwreck"],
                                ["item to category", "Miranda : character"], ["worker to tool", "magician : staff"], ["degree", "breeze : gale"]], [1.8 * inch, 3.0 * inch], width=4.8 * inch)),
     Example("Solve an analogy", "captain : ship :: king : ___", ["Relationship: a captain rules a ship.", "A king rules a ___ ."], "kingdom"),
     KeyIdea("Name the relationship in the first pair, then find the word that creates the same relationship.")],
    [Problem("loyal : traitor :: brave : ___", "coward"), Problem("page : book :: scene : ___", "play (act)"), Problem("drizzle : downpour :: breeze : ___", "gale (hurricane)")],
    [S("Warm-Up", [SA("tempest : storm relationship", "synonyms"), SA("sail : ship relationship", "part to whole")], cols=2),
     S("Complete the Analogies", [SA(q, a) for q, a in [("author : novel :: playwright : ___", "play"), ("generous : stingy :: humble : ___", "arrogant (proud)"), ("thunder : lightning :: smoke : ___", "fire"),
                                                        ("painter : brush :: sculptor : ___", "chisel"), ("island : ocean :: oasis : ___", "desert"), ("whisper : shout :: walk : ___", "run (sprint)")]], cols=2),
     S("Create", [OR("Write two analogies using characters or objects from The Tempest. Name each relationship.", "e.g. Prospero : magic :: sailor : rope (worker to tool).", lines=3)])],
    te("Students analyze word relationships.", "Use the relationship between particular words to better understand each of the words.", "Workbook Lesson 1.7",
       "Captain : ship.", "Review Act 1.2 vocabulary.", ["Teach relationship types."], "Your Turn 1–3.",
       ["Reversing the order of the pair."], ["Make a sentence from pair 1."], ["Write analogies for a sibling."]),
    summary="Name the relationship; match it.")

L8 = Lesson("1.8", "Sound and Rhythm in Poetry and Drama",
    "I can analyze the effect of rhyme, repetition, and rhythm.", "RL.7.4",
    [("alliteration", "Repetition of beginning consonant sounds."), ("iambic pentameter", "A line of ten syllables with a da-DUM rhythm repeated five times."), ("blank verse", "Unrhymed iambic pentameter.")],
    "Why might a playwright write lines with a steady beat?",
    [Text("Shakespeare's nobles often speak in <b>blank verse</b> (unrhymed iambic pentameter), while servants and comic characters often speak in prose. Magical songs, like Ariel's, rhyme. Sound and rhythm help reveal character and mood."),
     Example("Hear the rhythm", "“Full fathom five thy father lies”", ["Alliteration: Full, fathom, five, father: repeated f sounds.", "Effect: a soft, rolling sound like waves; makes the song memorable and haunting."], "The f-sounds create a hushed, sea-like mood."),
     Example("Iambic pentameter", "“We are such stuff / As dreams are made on” (Act 4)", ["da-DUM stress pattern: as DREAMS are MADE on…", "Ten syllables per full line."], "Prospero speaks in measured, thoughtful verse."),
     KeyIdea("Rhyme, repetition, and rhythm create mood and reveal who is speaking.")],
    [Problem("Find the alliteration in “Full fathom five thy father lies.”", "f sounds: full, fathom, five, father"), Problem("Rhyme in Ariel's song: lies / ___", "eyes"), Problem("What is blank verse?", "unrhymed iambic pentameter")],
    [S("Warm-Up", [SA("Alliteration repeats…", "beginning consonant sounds"), SA("Iambic pentameter has ___ syllables.", "ten")], cols=2),
     S("Analyze Sound", [OR("Copy the rhyming pairs in Ariel's song. What effect does the rhyme have?", "lies/eyes, made/fade, change/strange; musical, magical, memorable", lines=3),
                         OR("Find a line in Act 1.2 spoken in verse and one in prose (if any). Why might Shakespeare switch?", "Answers vary; verse for nobles/serious moments, prose for common or comic characters.", lines=3)], passage=P_ARIEL),
     S("Create", [OR("Write two lines with alliteration describing the island.", "Answers vary.", lines=2)])],
    te("Students analyze sound and rhythm.", "Analyze the impact of rhymes and other repetitions of sounds on a verse or stanza.", "Workbook Lesson 1.8",
       "Steady beat.", "Clap the rhythm of a line.", ["Teach alliteration, rhyme, iambic pentameter."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Counting syllables wrong."], ["Clap syllables."], ["Write a couplet in iambic pentameter."]),
    summary="Sound devices create mood and reveal character.")

# ================================================================= Week 3 · Evidence and inference (Act 1 Scene 2, second section)
L9 = Lesson("1.9", "Citing Several Pieces of Evidence",
    "I can cite several pieces of textual evidence to support an analysis.", "RL.7.1",
    [("textual evidence", "Quotations or details from the text that support a claim.")],
    "Is one quotation enough to prove that Prospero is controlling?",
    [ReaderAssign(TEMPEST, "Act 1, Scene 2 (second section)", "How does Prospero treat Ariel and Caliban? Collect evidence."),
     Text("Grade 7 analysis requires <b>several</b> pieces of evidence. Choose evidence from different parts of the text, and introduce each with a phrase that shows where it comes from (<i>Early in the scene… Later, when Ariel asks for freedom…</i>)."),
     Example("Build a claim with evidence", "Claim: Prospero uses his power to control others.",
             ["Evidence 1: He reminds Ariel of past suffering when Ariel asks for freedom.", "Evidence 2: He threatens Caliban with cramps and pains.", "Evidence 3: He puts Miranda to sleep with magic."],
             "Three pieces of evidence from different moments show a pattern of control."),
     KeyIdea("Use several, varied pieces of evidence; show where each comes from.")],
    [Problem("Why use evidence from different parts?", "to show a pattern, not a single moment"), Problem("Introduce a quote with its location.", "e.g. Later in the scene, Prospero says…"), Problem("What does Prospero promise Ariel?", "freedom after Ariel completes his tasks")],
    [S("Warm-Up", [SA("Textual evidence =", "quotes or details that support a claim"), SA("How many pieces in Grade 7?", "several (two or more)")], cols=2),
     S("Evidence Collection", [OR("Claim: Caliban resents Prospero. Find two pieces of evidence from Act 1.2.", "Answers vary; e.g. Caliban says the island was his; he curses Prospero.", lines=4),
                               OR("Claim: Ariel wants freedom. Find two pieces of evidence.", "Answers vary; Ariel reminds Prospero of his promise.", lines=4)]),
     S("Exit Ticket", [OR("Which character do you sympathize with most so far? Give two pieces of evidence.", "Answers vary.", lines=3)])],
    te("Students cite several pieces of evidence.", "Cite several pieces of textual evidence to support analysis.", "The Tempest Reader (Act 1.2), workbook Lesson 1.9",
       "One quote enough?", "Read Act 1.2 (second part).", ["Model the three-evidence claim."], "Your Turn 1–3.",
       ["Clustering evidence from one speech."], ["Evidence log by scene section."], ["Debate: Is Prospero a hero or a tyrant?"]),
    summary="Several, varied pieces of evidence build strong analysis.")

L10 = Lesson("1.10", "Inferring Character from Dialogue",
    "I can make inferences about characters from what they say and how others respond.", "RL.7.1, RL.7.3",
    [("subtext", "The meaning beneath what a character actually says.")],
    "When someone says “I'm fine” in an angry voice, what do they really mean?",
    [Text("In drama, there is no narrator to explain feelings. Readers infer from <b>dialogue</b>, <b>stage directions</b>, and <b>other characters' reactions</b>. Listen for <b>subtext</b>."),
     Figure(lambda t: table(t, [["Character", "What they say or do (Act 1.2)", "What we can infer"], ["Prospero", "Retells his history at length; asks Miranda repeatedly if she is listening", "He is consumed by past wrongs and needs her to understand"],
                                ["Miranda", "Pities the sailors in the storm", "She is compassionate"], ["Caliban", "Claims the island was his mother's and his", "He sees Prospero as a thief and usurper"]],
                            [1.0 * inch, 2.6 * inch, 2.1 * inch], width=5.7 * inch, font_size=9)),
     KeyIdea("Infer from dialogue, stage directions, and reactions; look for subtext.")],
    [Problem("What is subtext?", "meaning beneath the words"), Problem("What does Miranda's pity show?", "compassion"), Problem("Why might Prospero keep asking Miranda if she's listening?", "He needs her to understand; he's emotional about the past.")],
    [S("Warm-Up", [SA("Drama has no…", "narrator"), SA("Subtext means…", "hidden meaning beneath words")], cols=2),
     S("Infer", [OR("Choose one exchange between Prospero and Caliban. What is the subtext?", "Answers vary.", lines=4),
                 OR("How does Ariel speak to Prospero? What does it suggest about their relationship?", "Answers vary; respectful but eager for freedom; dependent and controlled.", lines=3)]),
     S("Exit Ticket", [OR("Write one line of dialogue that has subtext. Explain the hidden meaning.", "Answers vary.", lines=2)])],
    te("Students infer from dialogue.", "Analyze how particular elements of a drama interact; cite evidence.", "Workbook Lesson 1.10",
       "I'm fine.", "Reread key exchanges; read aloud with different tones.", ["Model the inference chart."], "Your Turn 1–3.",
       ["Taking every line literally."], ["Read lines in different tones."], ["Perform an exchange two ways."]),
    summary="Infer character from dialogue, directions, and reactions.")

L11 = Lesson("1.11", "Inference in Informational Text",
    "I can draw inferences from an informational text and support them with evidence.", "RI.7.1",
    [],
    "Why might audiences in 1611 have been especially excited by a play about a shipwreck?",
    [P_SEAVENTURE,
     Example("Infer", "Why were people in London so interested in the Sea Venture accounts?", ["Evidence: everyone survived a hurricane; they lived on a feared island; they built new ships.", "Reasoning: a true survival story is thrilling and surprising."],
             "Londoners were fascinated because the survival seemed almost miraculous."),
     KeyIdea("Connect several facts to infer what the author implies but doesn't state.")],
    [Problem("Why did the captain drive the ship onto the reef?", "to keep it from sinking in the storm (saving the passengers)"), Problem("What were the “strange night noises”?", "birds"), Problem("How long did the castaways stay?", "about ten months")],
    [S("Warm-Up", [SA("Year of the wreck", "1609"), SA("Island name", "Bermuda")], cols=2),
     S("Infer with Evidence", [OR("Infer why sailors called Bermuda the “Isle of Devils.” Cite two details.", "dangerous reefs and strange night noises that seemed supernatural", lines=3),
                               OR("What can you infer about the survivors' skills and determination? Cite evidence.", "They were resourceful: found food and water, built two ships from cedar and the wreck.", lines=3),
                               OR("How might the true story have influenced The Tempest? Make two connections.", "storm and shipwreck; mysterious island that seems haunted but is survivable", lines=3)], passage=P_SEAVENTURE),
     S("Exit Ticket", [OR("What word in the passage shows the author is cautious about saying Shakespeare used the accounts?", "“Many scholars believe” / “at least one”", lines=1)])],
    te("Students infer from informational text.", "Cite several pieces of evidence to support inferences drawn from informational text.", "Workbook Lesson 1.11",
       "Excited audiences.", "Read “The Real Shipwreck.”", ["Model the inference."], "Your Turn 1–3.",
       ["Stating facts as inferences."], ["Because X and Y, I infer Z."], ["Research the Sea Venture further."]),
    summary="Connect facts to infer implied ideas.")

L12 = Lesson("1.12", "Writing a Claim-Evidence-Reasoning Paragraph",
    "I can write an analytical paragraph with a claim, multiple pieces of evidence, and reasoning.", "W.7.9a, W.7.1b",
    [("claim", "An arguable statement that answers the question."), ("reasoning", "Explanation of how the evidence supports the claim.")],
    "What separates a summary from an analysis?",
    [Text("An analytical paragraph makes a <b>claim</b>, supports it with <b>two or three pieces of evidence</b>, and explains each with <b>reasoning</b>. It ends with a <b>concluding sentence</b> that connects back to the claim."),
     Example("CER paragraph", "How does Shakespeare present Prospero in Act 1?",
             ["Claim: Prospero is presented as a wronged ruler who has become controlling.", "Evidence 1 + reasoning: his account of Antonio's betrayal.", "Evidence 2 + reasoning: his threats to Caliban.", "Conclusion."],
             "In Act 1, Shakespeare presents Prospero as a man wronged by his brother who now uses his power to control others. When he tells Miranda how Antonio stole his dukedom, his bitter words show how deeply the betrayal still affects him. Yet he himself rules the island harshly, threatening Caliban with painful cramps. Shakespeare creates a complex character who is both a victim and a tyrant."),
     KeyIdea("Claim → evidence → reasoning (repeat) → concluding sentence.")],
    [Problem("Is “Prospero lives on an island” a claim?", "No, it's a fact, not arguable."), Problem("What follows each piece of evidence?", "reasoning"), Problem("What does the concluding sentence do?", "connects back to the claim")],
    [S("Warm-Up", [SA("CER =", "Claim, Evidence, Reasoning"), SA("A claim must be…", "arguable")], cols=2),
     S("Write", [OR("Question: Is Caliban a villain or a victim in Act 1? Write a CER paragraph with at least two pieces of evidence.", "Answers vary.", lines=12,
                    note="Score: claim (1), evidence 1 (1), evidence 2 (1), reasoning (1), conclusion and conventions (1).")])],
    te("Students write CER paragraphs.", "Draw evidence from texts to support analysis; support claims with clear reasons and evidence.", "Workbook Lesson 1.12",
       "Summary vs analysis.", "Gather Caliban evidence.", ["Model the paragraph."], "Plan together.",
       ["Summarizing instead of analyzing."], ["Highlight reasoning sentences."], ["Write a counterclaim sentence."], independent="Write the paragraph. Weekly Check tomorrow."),
    summary="Claim, multiple evidence, reasoning, conclusion.")

# ================================================================= Week 4 · Central ideas, theme, development (Act 2)
L13 = Lesson("1.13", "Theme and Its Development",
    "I can determine a theme and analyze how it develops over the course of a text.", "RL.7.2",
    [("theme", "A message about life or human nature that a text explores."), ("motif", "A repeated image, idea, or symbol that supports a theme.")],
    "What ideas keep coming up in The Tempest so far?",
    [ReaderAssign(TEMPEST, "Act 2", "Which characters plot against others? Who wants power?"),
     Text("Grade 7 readers track how a theme <b>develops</b>: how it is introduced, how events and characters complicate it, and how it is resolved. Recurring <b>motifs</b> (storms, power, freedom, illusion) point to themes."),
     Figure(lambda t: table(t, [["Possible theme topic", "Evidence so far (Acts 1–2)"], ["power and its abuse", "Antonio usurped Prospero; Prospero controls Ariel and Caliban; Antonio urges Sebastian to kill Alonso"],
                                ["freedom vs control", "Ariel asks for freedom; Caliban resents servitude"], ["appearance vs reality", "the storm is magical; Ariel invisible; characters believe others drowned"]],
                            [1.7 * inch, 3.9 * inch], width=5.6 * inch, font_size=9)),
     Example("Develop a theme statement", "Topic: power", ["Introduced: Antonio's betrayal.", "Repeated: Antonio tempts Sebastian in Act 2.", "Complicated: Prospero, the victim, also abuses power."], "Theme: The desire for power can corrupt anyone, even those who have suffered from it."),
     KeyIdea("Track a theme through introduction, repetition, and complication; state it as a full sentence.")],
    [Problem("What is a motif?", "a repeated image or idea that supports a theme"), Problem("How does Act 2 repeat the power theme?", "Antonio persuades Sebastian to kill Alonso to become king"), Problem("Write a theme about freedom.", "e.g. Everyone longs for freedom, and control breeds resentment.")],
    [S("Warm-Up", [SA("A theme is a ___, not a topic.", "message / statement"), SA("Motif example in The Tempest", "storms, power, freedom")], cols=2),
     S("Trace a Theme", [OR("Choose a theme topic. Write a theme statement.", "Answers vary.", lines=2), OR("Evidence where it is introduced (Act 1):", "Answers vary.", lines=2),
                         OR("Evidence where it is repeated or complicated (Act 2):", "Answers vary.", lines=2), OR("How has the theme developed?", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("How is Antonio's plan in Act 2 a mirror of his past actions?", "He again plots to seize power by betraying a ruler, as he did to Prospero.", lines=2)])],
    te("Students analyze theme development.", "Determine a theme and analyze its development over the course of the text.", "The Tempest Reader (Act 2), workbook Lesson 1.13",
       "Recurring ideas.", "Read Act 2.", ["Model tracing power."], "Your Turn 1–3.",
       ["One-word themes."], ["Theme frame: Topic + what the text says about it."], ["Track a motif across the whole play."]),
    summary="Themes develop through introduction, repetition, and complication.")

L14 = Lesson("1.14", "Central Ideas in Informational Text",
    "I can determine two or more central ideas and analyze their development.", "RI.7.2",
    [("central idea", "A main idea that the author develops in a text.")],
    "Can an article have more than one main idea?",
    [Text("Longer informational texts often develop <b>two or more central ideas</b>. Identify each and trace how details develop it."),
     Example("Two central ideas", "“The Real Shipwreck Behind The Tempest”", ["Central idea 1: The Sea Venture survivors endured a remarkable ordeal (paragraphs 1–3).", "Central idea 2: Their story likely inspired Shakespeare (paragraph 4)."],
             "The article develops both the survival story and its literary influence."),
     KeyIdea("Name each central idea; trace the details that develop it.")],
    [Problem("Which paragraphs develop the survival idea?", "1–3"), Problem("Which paragraph connects to Shakespeare?", "4"), Problem("Central idea of “Theater in Shakespeare's London”", "Theater was a popular, lively entertainment that relied on words and audiences' imagination.")],
    [S("Warm-Up", [SA("Central idea =", "a main idea the author develops"), SA("Can a text have two?", "Yes")], cols=2),
     S("Analyze", [OR("Identify two central ideas in “Theater in Shakespeare's London.” Cite a detail for each.", "1) Theater was popular with all classes: 3,000 people, groundlings and galleries. 2) Staging relied on words: little scenery, daylight, all-male actors.", lines=4),
                   OR("How do the two ideas work together?", "Different audiences and simple staging explain why Shakespeare's words had to do so much.", lines=3)], passage=P_GLOBE),
     S("Exit Ticket", [OR("Write a one-sentence statement combining both central ideas of the Sea Venture article.", "The Sea Venture survivors' remarkable ordeal on Bermuda likely inspired Shakespeare's The Tempest.", lines=2)])],
    te("Students determine multiple central ideas.", "Determine two or more central ideas and analyze their development.", "Workbook Lesson 1.14",
       "More than one main idea?", "Reread both informational texts.", ["Model two central ideas."], "Your Turn 1–3.",
       ["Choosing one detail as a central idea."], ["Paragraph-grouping chart."], ["Find central ideas in a news article."]),
    summary="Identify and trace multiple central ideas.")

L15 = Lesson("1.15", "Writing an Objective Summary",
    "I can write an objective summary of a text.", "RL.7.2, RI.7.2",
    [("objective", "Neutral; without personal opinions or judgments.")],
    "What's the difference between “Antonio is a terrible person who plots murder” and “Antonio persuades Sebastian to kill Alonso”?",
    [Text("An <b>objective summary</b> states the central idea or theme and key events in your own words, in order, without opinions, judgments, or minor details."),
     Example("Objective vs subjective", "Act 2 summary", ["Subjective: The evil Antonio cruelly convinces the foolish Sebastian…", "Objective: Antonio persuades Sebastian to kill his brother Alonso and take the throne, but Ariel wakes Gonzalo, whose shout rouses the king in time."],
             "Objective summaries report; they don't judge."),
     KeyIdea("Objective = neutral, concise, central idea + key events, own words.")],
    [Problem("Objective or not: “Ariel cleverly saves the day.”", "Not objective (“cleverly” judges)"), Problem("Should an objective summary include “I think”?", "No"), Problem("What goes first?", "the central idea or theme")],
    [S("Warm-Up", [SA("Objective means…", "neutral, without opinion"), SA("A summary is ___ than the text.", "shorter")], cols=2),
     S("Revise to Objective", [SA(q, a) for q, a in [("The heartless Prospero makes poor Caliban work.", "Prospero makes Caliban work."), ("Miranda sweetly pities the doomed sailors.", "Miranda pities the sailors."),
                                                      ("The amazing survivors brilliantly built two ships.", "The survivors built two ships.")]], cols=1),
     S("Summarize", [OR("Write an objective summary of Acts 1–2 of The Tempest (5–7 sentences).", "Answers vary; neutral, key events in order.", lines=8)])],
    te("Students write objective summaries.", "Provide an objective summary of the text.", "Workbook Lesson 1.15",
       "Judgment vs report.", "Skim Acts 1–2.", ["Model objective revision."], "Your Turn 1–3.",
       ["Loaded adjectives."], ["Circle judgment words."], ["Summarize a news article objectively."]),
    summary="Objective summaries are neutral and concise.")

L16 = Lesson("1.16", "How Setting Shapes Characters and Plot",
    "I can analyze how elements of a story or drama interact, such as how setting shapes characters and plot.", "RL.7.3",
    [],
    "Why does it matter that The Tempest takes place on an isolated island?",
    [Text("Setting can create conflict, limit choices, and reveal character. On Prospero's island, characters are cut off from their normal lives and power, and Prospero controls everything through magic."),
     Example("Analyze interaction", "How does the island shape the plot?", ["Isolation: shipwrecked nobles can't escape or call for help.", "Control: Prospero's magic rules the island, so he can direct events.", "Effect: the island becomes a stage for Prospero's plan."],
             "The isolated island lets Prospero control the shipwrecked characters and test them."),
     KeyIdea("Analyze how setting creates conflict, limits choices, and reveals character.")],
    [Problem("How does isolation affect the castaways?", "They are cut off, vulnerable, and at Prospero's mercy."), Problem("How does the island shape Caliban?", "He was its original inhabitant; losing it shapes his resentment."), Problem("How did Bermuda shape the Sea Venture survivors' story?", "It provided food and cedar to build ships, allowing survival.")],
    [S("Warm-Up", [SA("Setting =", "time and place"), SA("Setting of The Tempest", "a remote magical island")], cols=2),
     S("Analyze", [OR("How does the island setting shape two different characters? Use evidence.", "Answers vary; e.g. Caliban resents losing it; Ferdinand is separated and meets Miranda.", lines=5)]),
     S("Exit Ticket", [OR("How would The Tempest change if it were set in a crowded city?", "Prospero couldn't control everyone; no isolation; the plot of testing castaways wouldn't work.", lines=3)])],
    te("Students analyze setting's effect.", "Analyze how particular elements of a story or drama interact.", "Workbook Lesson 1.16, Unit 1 Review",
       "Why an island?", "Revisit island descriptions.", ["Model the analysis."], "Your Turn 1–3.",
       ["Describing setting without analyzing effect."], ["Setting → effect chart."], ["Compare to another island story."], independent="Workbook and the Unit 1 Review.", exit_="Tomorrow: Unit 1 Test."),
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
    S("Vocabulary", [SA("thou =", "you"), SA("bene =", "good"), SA("Connotation of <i>stubborn</i>", "negative"), SA("tempest : storm relationship", "synonyms"),
                     SA("Device: The waves clawed at the cliffs.", "personification"), SA("Iambic pentameter syllables", "ten")], cols=2),
    S("Reading and writing", [OR("Write a theme statement about power in The Tempest and one piece of evidence.", "Answers vary.", lines=3),
                              OR("Revise to be objective: The cruel Antonio stole the kind Prospero's kingdom.", "Antonio took Prospero's dukedom.", lines=1)])],
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

UNIT = Unit(1, "Language and Meaning", "Shakespeare's language, roots and context, connotation and figurative language, evidence and inference, theme and objective summary, with The Tempest, Introduction–Act 2.",
    "A storm, a shipwreck, an enchanted island, and a powerful magician: <i>The Tempest</i> is one of Shakespeare's most magical plays. In this unit you'll learn to read Shakespeare's language with confidence, unlock words with roots and context, analyze connotation and figurative language, support inferences with several pieces of evidence, and trace themes as they develop.",
    ["Read Shakespeare's language using translation strategies.", "Use roots, affixes, context, and reference tools to determine meaning.", "Analyze connotation, figurative language, word relationships, and sound.",
     "Cite several pieces of evidence to support inferences and claims.", "Determine and trace themes and central ideas; write objective summaries."],
    [("RL.7.1–5, RI.7.1–2", "Cite evidence; determine themes and central ideas; analyze elements, word choice, and dramatic form."), ("L.7.4–5", "Determine word meanings; interpret figurative language and connotation."),
     ("W.7.1b, W.7.9", "Support claims with evidence; draw evidence from texts.")],
    [("archaic", "No longer in common use."), ("connotation", "The feeling a word carries."), ("allusion", "A reference to something well known."), ("theme", "A message about life."),
     ("objective summary", "A neutral, concise retelling."), ("iambic pentameter", "Ten syllables of da-DUM rhythm.")],
    ["Grade 6 reading and writing skills."], ["The Tempest Reader (Introduction–Act 2)", "Dictionary with etymologies", "Highlighters"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Shakespeare gave English hundreds of words and phrases still used today, and analyzing connotation helps you see how ads, speeches, and news shape opinion.",
    family_note="Watch a short clip of a Tempest performance together, or read a few lines aloud dramatically at dinner.",
    weeks=WEEKS)
