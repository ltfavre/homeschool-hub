"""Grade 7 ELA · Unit 3: Mystery and Grammar — mystery structure and characterization; pronoun case, reference, and agreement; verb tense, voice, and mood; consistency and editing.
Anchor reading: Strange Case of Dr. Jekyll and Mr. Hyde Reader, Chapters 1–4 (Dec 14, 2026 – Jan 22, 2027)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule

JH = "Strange Case of Dr. Jekyll and Mr. Hyde Reader"


def rules(rows, widths, fs=9.5):
    return Figure(lambda t: table(t, rows, [w * inch for w in widths], width=sum(widths) * inch, font_size=fs))


# ================================================================= passages (Stevenson excerpts public domain; others original)
P_UTTERSON = Passage("From Chapter 1, “Story of the Door” (original 1886 text)", [
    "Mr. Utterson the lawyer was a man of a rugged countenance that was never lighted by a smile; cold, scanty and embarrassed in discourse; backward in sentiment; lean, long, dusty, dreary and yet somehow lovable.",
], source="Robert Louis Stevenson, Strange Case of Dr. Jekyll and Mr. Hyde (1886). Public domain.", genre="Classic novel excerpt", numbered=False)

P_ENFIELD = Passage("Enfield Describes Hyde, Chapter 1 (original text, excerpt)", [
    "“There is something wrong with his appearance; something displeasing, something down-right detestable. I never saw a man I so disliked, and yet I scarce know why.”",
], source="Robert Louis Stevenson, Strange Case of Dr. Jekyll and Mr. Hyde. Public domain.", genre="Classic novel excerpt", numbered=False)

P_SEEK = Passage("Utterson's Vow, Chapter 2 (original text, excerpt)", [
    "“If he be Mr. Hyde,” he had thought, “I shall be Mr. Seek.”",
], source="Robert Louis Stevenson, Strange Case of Dr. Jekyll and Mr. Hyde. Public domain.", genre="Classic novel excerpt", numbered=False)

P_FOG = Passage("Fog over the City", [
    "By ten o'clock the fog had swallowed the city whole. Gas lamps glowed like dim orange moons, and the cobblestones gleamed with damp. Somewhere a church bell struck the hour, its sound muffled as if wrapped in wool.",
    "Inspector Hale turned up his collar and listened. A door creaked. Footsteps hurried away. When he reached the alley, it was empty, except for a single silver button lying in a puddle, catching the lamplight.",
    "Hale picked it up. It was engraved with two letters, so worn he could barely read them. Someone had left in a hurry. Someone, he suspected, who had very good reasons not to be seen.",
], source="An original story", genre="Mystery")

P_PASSIVE = Passage("The Museum Robbery: Two Reports", [
    "<b>Report A.</b> Last night, a thief broke a window at the city museum, climbed inside, and stole a gold necklace from the Egyptian exhibit. A guard spotted the thief and called the police.",
    "<b>Report B.</b> Last night, a window at the city museum was broken, and a gold necklace was stolen from the Egyptian exhibit. The police were called after a suspicious figure was spotted.",
], source="Original examples", genre="News writing", numbered=False)

P_C7 = Passage("The Locked Room", [
    "When Ms. Patel arrived at the library on Monday, she found the rare-books room locked, just as she had left it. But the glass case in the middle of the room was empty. The map that had been there, a 300-year-old chart of the coast, was gone.",
    "She called her assistant, Leo, and he came at once. He said that he had locked the door himself on Friday. When she asked him who else had a key, he hesitated. “Only you and me,” he said, “and the cleaning company.”",
], source="An original mystery", genre="Mystery")

P_C8 = Passage("A Question of Character", [
    "Everyone in the village thought that Mr. Grimsby was a miser. He wore the same patched coat every winter, and nobody had ever seen him buy anything but bread and tea.",
    "When he died, the townspeople were astonished. His will left his entire fortune to the village school, which needed a new roof. Each of the teachers received a letter from him, thanking them for their work.",
], source="An original story", genre="Realistic fiction")

P_C9 = Passage("The Experiment", [
    "Dr. Lena Ruiz had worked on the formula for three years. If it worked, it would clean polluted water in minutes. Tonight was the final test.",
    "She mixed the solution carefully. The murky sample was poured into the beaker. Lena held her breath and watched. Slowly, the brown water cleared, until it sparkled like glass.",
    "“Record everything,” she told her assistant. “Be sure that every step is written down.”",
], source="An original story", genre="Science fiction")

P_TEST = Passage("The Vanishing Violinist", [
    "On the night of the concert, the famous violinist Marco Bellini did not appear. The orchestra waited, the audience grew restless, and at last the conductor announced that the performance would be canceled.",
    "Detective June Okoro was called the next morning. Bellini's dressing room was neat, except for an open violin case. The case was empty. On the mirror, someone had written three words in red lipstick: <i>Ask the twin.</i>",
    "Okoro learned that Bellini had a twin brother, Luca, who had once played violin too. The brothers had not spoken in years. Luca was found that afternoon at a café across town, calmly drinking coffee. When Okoro showed him a photograph of the message, he went pale. “He has done it again,” Luca whispered.",
    "Luca explained that whenever Marco felt he could not perform perfectly, he disappeared and blamed his brother so that no one would think he was afraid. Okoro found Marco hiding at a hotel, his violin in his lap. He had been practicing all night.",
    "“Perfection,” Marco said quietly, “is a cage I built myself.” The next evening, he walked onto the stage, bowed to the audience, and played, not perfectly, but beautifully.",
], source="An original mystery", genre="Mystery")

# ================================================================= Week 1 · Pronouns and reference clarity (Chapter 1)
L1 = Lesson("3.1", "The Mystery Genre and Frame Narratives",
    "I can analyze how a mystery is structured, including stories told within stories.", "RL.7.5, RL.7.3",
    [("mystery", "A genre built around a puzzle or crime that characters try to solve."), ("frame narrative", "A story that contains another story told by a character."), ("Gothic", "A style of fiction with dark settings, mystery, and a mood of horror or dread.")],
    "What makes a mystery story hard to put down?",
    [ReaderAssign(JH, "Chapter 1: Story of the Door", "What story does Mr. Enfield tell? Why does it disturb Mr. Utterson?"),
     Text("<i>Strange Case of Dr. Jekyll and Mr. Hyde</i> (1886) is a Gothic mystery. Stevenson withholds the truth until the very end. Much of the story reaches us secondhand: in Chapter 1, Mr. Enfield tells Mr. Utterson a story within the story, a <b>frame narrative</b>."),
     Figure(lambda t: table(t, [["Mystery element", "In Chapter 1"], ["a puzzle", "Why would respectable Dr. Jekyll's name be on a cheque given by the brutal Mr. Hyde?"], ["clues", "the door, the cheque, Hyde's strange appearance"],
                                ["an investigator", "Mr. Utterson, the lawyer"], ["withheld information", "Enfield refuses to name the signer at first"]], [1.8 * inch, 3.8 * inch], width=5.6 * inch)),
     P_UTTERSON,
     Example("Analyze characterization", "What kind of investigator is Utterson?", ["“never lighted by a smile”; “cold, scanty and embarrassed in discourse”: reserved, serious.", "“and yet somehow lovable”: loyal, trustworthy."], "Utterson is a reserved, serious man whom readers can trust to pursue the truth."),
     KeyIdea("Mysteries withhold information and plant clues; frame narratives filter events through a character's telling.")],
    [Problem("Who tells the story of the door?", "Mr. Enfield"), Problem("What crime does Hyde commit in Enfield's story?", "He tramples a young girl."), Problem("What is the central puzzle?", "why Jekyll's name is connected to Hyde (on the cheque)")],
    [S("Warm-Up", [SA("A frame narrative is…", "a story within a story"), SA("Gothic fiction has…", "dark settings, mystery, dread")], cols=2),
     S("Analyze Chapter 1", [OR("Explain how the frame narrative affects what readers know about Hyde.", "We only know Hyde through Enfield's secondhand account and feelings; it keeps him mysterious.", lines=3),
                             OR("List three clues from Chapter 1 and the questions each raises.", "Answers vary: the door (where does it lead?), the cheque (why Jekyll?), Hyde's appearance (what is wrong with him?).", lines=4),
                             OR("Paraphrase Stevenson's description of Utterson.", "Utterson had a rough face that never smiled; he was cold, spoke little and awkwardly, didn't show feelings, was thin and dull, yet people loved him.", lines=3)], passage=P_UTTERSON),
     S("Exit Ticket", [OR("Predict: what do you think connects Jekyll and Hyde? Cite one clue.", "Answers vary.", lines=2)])],
    te("Students analyze mystery structure.", "Analyze how a text's structure contributes to its meaning; how elements interact.", "Jekyll and Hyde Reader (Chapter 1), workbook Lesson 3.1",
       "Hard to put down.", ["Read Chapter 1.", "Read Stevenson's Utterson description aloud."], ["Teach mystery elements and frame narrative."], "Your Turn 1–3.",
       ["Spoiling the ending for others."], ["Clue tracker chart."], ["Keep a detective notebook for the whole book."]),
    summary="Mysteries withhold truth and plant clues; frames filter what we know.")

L2 = Lesson("3.2", "Pronoun Case",
    "I can use subjective, objective, and possessive pronouns correctly.", "L.7.1",
    [("pronoun case", "The form a pronoun takes depending on its job: subjective, objective, or possessive.")],
    "Which is correct: “Enfield and him walked” or “Enfield and he walked”?",
    [rules([["Case", "Pronouns", "Used as"], ["subjective", "I, you, he, she, it, we, they, who", "subjects; predicate pronouns"], ["objective", "me, you, him, her, it, us, them, whom", "objects of verbs and prepositions"],
            ["possessive", "my/mine, your/yours, his, her/hers, its, our/ours, their/theirs, whose", "ownership"]], (1.2, 2.6, 1.8)),
     Example("Compound subjects and objects", "Enfield and (he/him) walked down the street.", ["Remove “Enfield and”: him walked? He walked.", "Subject → subjective case."], "Enfield and he walked down the street."),
     Example("After a preposition", "The secret stayed between Jekyll and (I/me).", ["“between” is a preposition → objective case."], "between Jekyll and me"),
     KeyIdea("Drop the other noun to test compound pronouns. Prepositions take objective pronouns.")],
    [Problem("Utterson and (I/me) read the will.", "I"), Problem("The lawyer warned Lanyon and (she/her).", "her"), Problem("This secret is (theirs/their's).", "theirs")],
    [S("Warm-Up", [SA("Subjective pronoun", "I, he, she, we, they"), SA("Objective pronoun", "me, him, her, us, them")], cols=2),
     S("Choose the Correct Pronoun", [SA(q, a) for q, a in [("(He/Him) and Enfield took a walk.", "He"), ("The story frightened Utterson and (I/me).", "me"), ("Between you and (I/me), Hyde is strange.", "me"),
                                                            ("It was (she/her) who answered the door.", "she"), ("Give the letter to (we/us) lawyers.", "us"), ("(We/Us) readers suspect Hyde.", "We"),
                                                            ("The dog wagged (its/it's) tail.", "its"), ("Is this cane (yours/your's)?", "yours")]], cols=2),
     S("Exit Ticket", [OR("Write a sentence with a compound object that uses an objective pronoun correctly.", "e.g. The news shocked Utterson and him.", lines=2)])],
    te("Students use pronoun case correctly.", "Demonstrate command of grammar and usage.", "Workbook Lesson 3.2",
       "he or him?", "Find pronouns in Chapter 1.", ["Teach the case chart; drop-the-noun test."], "Your Turn 1–3.",
       ["“Between you and I.”"], ["Drop-the-noun test."], ["Find case errors in ads or headlines."]),
    summary="Subjective for subjects, objective for objects, possessive for ownership.")

L3 = Lesson("3.3", "Clear Pronoun Reference",
    "I can identify and fix vague or ambiguous pronouns.", "L.7.1, L.6.1d",
    [("antecedent", "The noun a pronoun refers to."), ("ambiguous", "Having more than one possible meaning.")],
    "In “Utterson told Enfield that he was worried,” who was worried?",
    [Text("A pronoun must clearly point to one antecedent. <b>Ambiguous</b> pronouns could refer to two people. <b>Vague</b> pronouns (<i>it, this, they</i>) refer to no specific noun."),
     rules([["Problem", "Example", "Fix"], ["ambiguous", "Utterson told Enfield that he was worried.", "Utterson told Enfield, “I am worried.” / Utterson was worried, and he told Enfield."],
            ["vague “they”", "In the newspaper, they said Hyde fled.", "The newspaper reported that Hyde fled."], ["vague “this”", "Hyde trampled the child and paid money. This upset Enfield.", "Hyde's cruelty upset Enfield."]],
           (1.1, 2.2, 2.5), fs=9),
     KeyIdea("Every pronoun needs one clear antecedent. If it could mean two people or no one, rewrite.")],
    [Problem("Fix: When Jekyll met Utterson, he smiled.", "e.g. Jekyll smiled when he met Utterson."), Problem("Fix: They say Hyde is dangerous.", "e.g. Witnesses say Hyde is dangerous."), Problem("What is an antecedent?", "the noun a pronoun refers to")],
    [S("Warm-Up", [SA("Ambiguous means…", "having more than one possible meaning"), SA("A pronoun points to its…", "antecedent")], cols=2),
     S("Fix the Reference", [SA(q, a) for q, a in [("Lanyon argued with Jekyll until he left.", "e.g. Lanyon argued with Jekyll until Jekyll left."), ("It says in the will that Hyde inherits everything.", "The will says that Hyde inherits everything."),
                                                   ("The maid saw the man with the cane, and it was terrible.", "e.g. The maid saw the man attack with the cane; the attack was terrible."),
                                                   ("Enfield and Utterson walked past the door, and he remembered the story.", "e.g. As they walked past the door, Enfield remembered the story.")]], cols=1),
     S("Exit Ticket", [OR("Write an ambiguous sentence on purpose, then fix it.", "Answers vary.", lines=2)])],
    te("Students fix vague and ambiguous pronouns.", "Recognize and correct vague pronouns.", "Workbook Lesson 3.3",
       "Who was worried?", "Reread Chapter 1 dialogue.", ["Teach the chart."], "Your Turn 1–3.",
       ["Thinking “this” is always clear."], ["Draw arrows from pronouns to nouns."], ["Edit an older essay for vague pronouns."]),
    summary="Each pronoun needs one clear antecedent.")

L4 = Lesson("3.4", "Characterization Through Description",
    "I can analyze how an author's description and characters' reactions develop a character.", "RL.7.3, RL.7.4",
    [("direct characterization", "The author tells us what a character is like."), ("indirect characterization", "The author shows character through actions, speech, appearance, and others' reactions.")],
    "Why might a reader find Hyde more frightening if no one can describe him clearly?",
    [P_ENFIELD,
     Example("Analyze", "What does Enfield's description reveal?", ["He can't say what is wrong: “I scarce know why.”", "Repeated “something” words build unease.", "Effect: Hyde is frightening because he cannot be explained."],
             "Stevenson makes Hyde terrifying through vagueness and others' reactions rather than a clear description."),
     KeyIdea("Analyze both what the author says directly and what is shown through reactions and details.")],
    [Problem("What does “detestable” mean?", "deserving hatred"), Problem("Why does Enfield repeat “something”?", "He can't name what is wrong; it builds unease."), Problem("Is this direct or indirect characterization?", "indirect (through Enfield's reaction)")],
    [S("Warm-Up", [SA("Direct characterization", "the author tells"), SA("Indirect characterization", "the author shows")], cols=2),
     S("Analyze", [OR("How does Stevenson use other characters' reactions to develop Hyde? Cite two details from Chapter 1.", "Enfield's disgust (“I never saw a man I so disliked”); the crowd's hatred after the trampling.", lines=4),
                   OR("Compare how Stevenson characterizes Utterson and Hyde.", "Utterson: direct description of appearance and manner, “somehow lovable.” Hyde: indirect, vague, through others' revulsion.", lines=4)], passage=P_ENFIELD),
     S("Write", [OR("Write a short paragraph analyzing how Stevenson makes Hyde mysterious. Use clear pronoun references.", "Answers vary.", lines=7)])],
    te("Students analyze characterization.", "Analyze how particular elements of a story interact; analyze word choice.", "Workbook Lesson 3.4",
       "Undescribable fear.", "Read Enfield's description.", ["Teach direct vs indirect."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Only listing traits."], ["Detail → effect chart."], ["Describe a character only through others' reactions."]),
    summary="Characters develop through description and others' reactions.")

# ================================================================= Week 2 · Pronoun agreement and application (Chapter 2)
L5 = Lesson("3.5", "Building Suspense Through Pursuit",
    "I can analyze how an author builds suspense and develops a character's motivation.", "RL.7.3, RL.7.1",
    [("motivation", "The reason a character acts.")],
    "Why would a respectable lawyer stand in a dark doorway for nights on end?",
    [ReaderAssign(JH, "Chapter 2: Search for Mr. Hyde", "What does Utterson learn from Jekyll's will? What happens when he finally meets Hyde?"),
     P_SEEK,
     Example("Analyze motivation", "Why does Utterson pursue Hyde?", ["Clue: Jekyll's will leaves everything to Hyde.", "Fear: Utterson suspects Hyde has some hold over Jekyll.", "Wordplay: Hyde/hide → Seek, showing his determination."],
             "Utterson's loyalty to Jekyll and fear for his safety motivate the pursuit."),
     KeyIdea("Suspense grows as a character's motivation pushes him toward danger.")],
    [Problem("What does Jekyll's will say?", "Everything goes to Hyde if Jekyll dies or disappears."), Problem("Explain the pun “Mr. Seek.”", "Hyde sounds like hide; Utterson will seek him."), Problem("What is Utterson's motivation?", "concern for his friend Jekyll")],
    [S("Warm-Up", [SA("Motivation =", "the reason a character acts"), SA("Hyde sounds like…", "hide")], cols=2),
     S("Analyze Chapter 2", [OR("How does the will increase Utterson's suspicion? Cite evidence.", "Answers vary; the will names Hyde as heir, which Utterson disliked and found suspicious.", lines=3),
                             OR("Describe Utterson's meeting with Hyde. How does Stevenson build suspense?", "Answers vary; long wait, footsteps, Hyde's sudden appearance and odd behavior.", lines=4)]),
     S("Exit Ticket", [OR("What question would you ask Jekyll if you were Utterson?", "Answers vary.", lines=2)])],
    te("Students analyze suspense and motivation.", "Analyze interactions of elements; cite evidence.", "Jekyll and Hyde Reader (Chapter 2), workbook Lesson 3.5",
       "Waiting in doorways.", "Read Chapter 2.", ["Model motivation analysis."], "Your Turn 1–3.",
       ["Confusing motive with action."], ["Why? chain."], ["Write Utterson's diary entry."]),
    summary="Motivation drives suspenseful pursuit.")

L6 = Lesson("3.6", "Pronoun-Antecedent Agreement and Indefinite Pronouns",
    "I can make pronouns agree with their antecedents, including indefinite pronouns.", "L.7.1",
    [("indefinite pronoun", "A pronoun that doesn't refer to a specific person or thing: everyone, each, someone, several.")],
    "Which is correct: “Everyone took their seat” or “Everyone took his or her seat”?",
    [rules([["Indefinite pronoun", "Number", "Example"], ["each, everyone, everybody, someone, anyone, nobody, either, neither", "singular", "Each of the servants knows his or her duties."],
            ["both, few, many, several", "plural", "Several of the witnesses gave their accounts."], ["all, some, most, none, any", "depends on the noun after “of”", "Some of the money was missing. Some of the doors were locked."]],
           (2.6, 1.0, 2.2), fs=9),
     Text("In formal writing, singular indefinite pronouns take singular verbs. Many style guides now also accept singular <i>they</i> for a person whose gender is unknown; choose one approach and use it consistently. Rewriting with a plural noun often avoids the problem: <i>All of the guests took their seats.</i>"),
     KeyIdea("Match number: singular antecedents with singular pronouns and verbs; plural with plural.")],
    [Problem("Each of the lawyers (has/have) a key.", "has"), Problem("Several of the clerks lost (his/their) notes.", "their"), Problem("Most of the cake (was/were) eaten.", "was")],
    [S("Warm-Up", [SA("Is “everyone” singular or plural?", "singular"), SA("Is “several” singular or plural?", "plural")], cols=2),
     S("Agreement", [SA(q, a) for q, a in [("Neither of the doctors (was/were) at home.", "was"), ("Both of the friends (trust/trusts) Utterson.", "trust"), ("Somebody left (their/his or her) cane.", "his or her (their accepted if consistent)"),
                                           ("All of the windows (was/were) dark.", "were"), ("Each of the servants (knows/know) the rules.", "knows"), ("None of the fog (has/have) lifted.", "has")]], cols=2),
     S("Exit Ticket", [OR("Rewrite to avoid the agreement problem: Everyone in the house locked their door.", "All of the residents locked their doors.", lines=2)])],
    te("Students apply agreement with indefinite pronouns.", "Demonstrate command of grammar.", "Workbook Lesson 3.6",
       "their or his or her?", "Find indefinite pronouns in Chapter 2.", ["Teach the chart; discuss singular they."], "Your Turn 1–3.",
       ["Plural verbs with each/everyone."], ["Cross out the of-phrase."], ["Edit a paragraph for agreement."]),
    summary="Match pronouns and verbs to their antecedents' number.")

L7 = Lesson("3.7", "Reflexive, Intensive, and Relative Pronouns: Who and Whom",
    "I can use reflexive and intensive pronouns and choose between who and whom.", "L.7.1",
    [("reflexive pronoun", "Ends in -self/-selves and refers back to the subject: He hurt himself."), ("intensive pronoun", "Ends in -self/-selves and emphasizes a noun: Utterson himself went.")],
    "Is it “Who did Utterson suspect?” or “Whom did Utterson suspect?”",
    [rules([["Use", "Example"], ["reflexive (needed for meaning)", "Jekyll locked himself in the laboratory."], ["intensive (adds emphasis; can be removed)", "Utterson himself read the will."],
            ["error: -self as a subject", "Myself and Utterson went. → Utterson and I went."], ["who = subject (he/she)", "Who wrote the letter? (He wrote it.)"], ["whom = object (him/her)", "Whom did Utterson suspect? (He suspected him.)"]],
           (2.4, 3.2)),
     KeyIdea("Use -self pronouns only to reflect or intensify. Who = he; whom = him.")],
    [Problem("Reflexive or intensive: The maid herself saw the attack.", "intensive"), Problem("(Who/Whom) did the maid see?", "Whom"), Problem("Fix: Lanyon and myself disagreed.", "Lanyon and I disagreed.")],
    [S("Warm-Up", [SA("who = he or him?", "he"), SA("whom = he or him?", "him")], cols=2),
     S("Choose", [SA(q, a) for q, a in [("(Who/Whom) is knocking at the door?", "Who"), ("To (who/whom) did Jekyll leave his money?", "whom"), ("The doctor (who/whom) Utterson visited was Lanyon.", "whom"),
                                        ("The man (who/whom) trampled the girl was Hyde.", "who"), ("Jekyll blamed (hisself/himself).", "himself"), ("Fix: Give the key to myself.", "Give the key to me.")]], cols=2),
     S("Exit Ticket", [OR("Write one sentence with an intensive pronoun and one with whom.", "Answers vary.", lines=2)])],
    te("Students use reflexive, intensive, who, and whom.", "Demonstrate command of grammar.", "Workbook Lesson 3.7",
       "Who or whom?", "Find -self pronouns in Chapter 2.", ["Teach the chart; he/him test."], "Your Turn 1–3.",
       ["“Myself” as a subject."], ["he/him substitution."], ["Who/whom quiz for a parent."]),
    summary="Reflexive and intensive -self pronouns; who for subjects, whom for objects.")

L8 = Lesson("3.8", "Writing a Character Analysis with Clear Pronouns",
    "I can write a character analysis that uses pronouns clearly and correctly.", "W.7.2, L.7.1",
    [],
    "When writing about two male characters, how do you keep “he” clear?",
    [Text("When you analyze two characters of the same gender, repeat names or use descriptive phrases (<i>the lawyer, the doctor</i>) to keep pronouns clear."),
     Example("Clear references", "Weak: When Utterson met Hyde, he was rude to him, and he felt disgusted.", ["Who was rude? Who felt disgusted?"], "When Utterson met Hyde, Hyde was rude to the lawyer, and Utterson felt disgusted."),
     KeyIdea("Use names and descriptive phrases to keep pronouns clear when two characters share a gender.")],
    [Problem("Descriptive phrase for Utterson", "the lawyer"), Problem("Descriptive phrase for Lanyon", "the doctor / Jekyll's old friend"), Problem("Why repeat names sometimes?", "to avoid ambiguous pronouns")],
    [S("Warm-Up", [SA("Phrase for Hyde", "the strange man / the stranger"), SA("Phrase for Jekyll", "the doctor / the scientist")], cols=2),
     S("Write", [OR("Write a paragraph analyzing Utterson's character in Chapters 1–2 with at least two pieces of evidence. Check every pronoun for a clear antecedent.", "Answers vary.", lines=12,
                    note="Score: claim (1); evidence (2); analysis (1); clear pronouns (1).")])],
    te("Students write character analyses with clear pronouns.", "Write analytically; demonstrate command of grammar.", "Workbook Lesson 3.8",
       "Two hes.", "Gather Utterson evidence.", ["Model clear reference."], "Plan.",
       ["Ambiguous he/him."], ["Highlight every pronoun and draw arrows."], ["Peer edit for pronouns."], independent="Write. Weekly Check tomorrow."),
    summary="Clear pronouns keep analysis readable.")

# ================================================================= Week 3 · Verb tense, mood, and voice (Chapter 3)
L9 = Lesson("3.9", "Verb Tenses: Simple, Perfect, and Progressive",
    "I can form and use simple, perfect, and progressive tenses to show time relationships.", "L.7.1",
    [("perfect tense", "Uses has/have/had/will have + past participle to show completed action relative to another time.")],
    "What's the difference between “Utterson read the will” and “Utterson had read the will before he met Hyde”?",
    [ReaderAssign(JH, "Chapter 3: Dr. Jekyll Was Quite at Ease", "How does Jekyll react when Utterson mentions Hyde?"),
     rules([["Tense", "Form", "Example"], ["simple past", "verb + -ed / irregular", "Utterson visited Jekyll."], ["past perfect", "had + past participle", "Utterson had read the will before the dinner."],
            ["present perfect", "has/have + past participle", "Jekyll has asked Utterson for a favor."], ["future perfect", "will have + past participle", "By midnight, the guests will have left."],
            ["past progressive", "was/were + -ing", "Jekyll was smiling, but his face changed."]], (1.3, 2.0, 2.4), fs=9),
     Example("Choose the tense", "By the time Utterson arrived, the other guests (left / had left).", ["Two past actions; the leaving happened first.", "Earlier past action → past perfect."], "had left"),
     KeyIdea("Perfect tenses show which action happened first. Progressive tenses show ongoing action.")],
    [Problem("Past perfect of <i>write</i> (Jekyll)", "Jekyll had written"), Problem("Present perfect of <i>see</i> (I)", "I have seen"), Problem("By next week, Utterson ___ (finish) the case.", "will have finished")],
    [S("Warm-Up", [SA("Past participle of <i>go</i>", "gone"), SA("Past participle of <i>speak</i>", "spoken")], cols=2),
     S("Write the Verb", [SA(q, a) for q, a in [("Before the dinner, Utterson ___ (decide) to speak with Jekyll.", "had decided"), ("Jekyll ___ (be) Utterson's friend for twenty years.", "has been"),
                                                ("By the end of the novel, Utterson ___ (learn) the truth.", "will have learned"), ("While they ___ (talk), the fire crackled.", "were talking"),
                                                ("The guests ___ (eat) when Jekyll's face changed.", "were eating"), ("Hyde ___ (vanish) before the police arrived.", "had vanished")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence about Chapter 3 using the past perfect.", "Answers vary.", lines=2)])],
    te("Students use simple, perfect, and progressive tenses.", "Demonstrate command of grammar.", "Jekyll and Hyde Reader (Chapter 3), workbook Lesson 3.9",
       "read vs had read.", "Read Chapter 3.", ["Teach the tense chart; timeline method."], "Your Turn 1–3.",
       ["Using simple past for earlier actions."], ["Timeline sketch."], ["Rewrite a scene in present tense."]),
    summary="Perfect tenses show order; progressive shows ongoing action.")

L10 = Lesson("3.10", "Active and Passive Voice",
    "I can identify active and passive voice and explain the effect of each.", "L.7.1, L.7.3",
    [("active voice", "The subject does the action: Hyde struck the man."), ("passive voice", "The subject receives the action: The man was struck by Hyde.")],
    "Which sounds more dramatic: “Hyde struck the man” or “The man was struck”?",
    [P_PASSIVE,
     Example("Compare", "Report A vs Report B", ["A (active): a thief broke, climbed, stole; the actor is clear and vivid.", "B (passive): was broken, was stolen; the actor is hidden.", "Effect: B is vaguer; useful when the actor is unknown, but less vivid."],
             "Active voice is clearer and more direct; passive voice hides or downplays who acted."),
     Bullets(["Form passive voice with a form of <i>be</i> + past participle: was stolen, were called.", "Use passive when the actor is unknown or unimportant, or to emphasize the receiver.", "Prefer active voice for clear, lively writing."]),
     KeyIdea("Active: subject acts. Passive: subject receives. Choose voice on purpose.")],
    [Problem("Active or passive: The will was signed by Jekyll.", "passive"), Problem("Rewrite in active: The will was signed by Jekyll.", "Jekyll signed the will."), Problem("Why might a criminal prefer passive voice?", "It hides who did it.")],
    [S("Warm-Up", [SA("Passive voice uses a form of…", "be (+ past participle)"), SA("Active voice: subject…", "does the action")], cols=2),
     S("Identify and Rewrite", [SA(q, a) for q, a in [("The door was opened by a key. (to active)", "A key opened the door. / Someone opened the door with a key."), ("Utterson questioned the butler. (to passive)", "The butler was questioned by Utterson."),
                                                      ("The letter was burned. (identify)", "passive (actor unknown)"), ("Lanyon refused the invitation. (identify)", "active")]], cols=1),
     S("Analyze", [OR("Which report would a museum spokesperson prefer? Why?", "B, because it avoids saying the guard didn't stop the thief; it sounds calmer and less specific.", lines=3)], passage=P_PASSIVE),
     S("Exit Ticket", [OR("Write one sentence about Chapter 3 in active voice, then rewrite it in passive.", "Answers vary.", lines=2)])],
    te("Students analyze voice.", "Use verbs in active and passive voice to achieve particular effects.", "Workbook Lesson 3.10",
       "Dramatic sentence.", "Read both reports.", ["Teach forms and uses."], "Your Turn 1–3.",
       ["Thinking all past tense is passive."], ["Look for be + participle and “by.”"], ["Find passive voice in a news article."]),
    summary="Active is direct; passive emphasizes the receiver or hides the actor.")

L11 = Lesson("3.11", "Verb Moods",
    "I can identify and use indicative, imperative, interrogative, conditional, and subjunctive moods.", "L.7.1",
    [("mood", "The form of a verb that shows the speaker's attitude: stating, commanding, asking, wishing, or imagining.")],
    "How is “Find Mr. Hyde!” different from “If I were Utterson, I would find Mr. Hyde”?",
    [rules([["Mood", "Purpose", "Example"], ["indicative", "states facts or opinions", "Utterson visits Jekyll."], ["imperative", "commands or requests", "Promise me you will help him."], ["interrogative", "asks questions", "Did you see the man's face?"],
            ["conditional", "states what would happen under a condition", "If Hyde returned, Utterson would follow him."], ["subjunctive", "expresses wishes or contrary-to-fact ideas", "I wish Jekyll were honest. If I were you, I would leave."]],
           (1.2, 2.2, 2.4), fs=9),
     Text("Notice the subjunctive <i>were</i> for all subjects in wishes and contrary-to-fact statements: <i>If he were here…</i> (not <i>was</i>). Stevenson's “If he be Mr. Hyde” is an older subjunctive form."),
     KeyIdea("Mood shows attitude: state, command, ask, imagine, or wish. Use “were” in contrary-to-fact statements.")],
    [Problem("Mood: “Tell me the truth.”", "imperative"), Problem("Mood: “If I were Jekyll, I would confess.”", "subjunctive (with conditional)"), Problem("Fix: I wish Hyde was gone.", "I wish Hyde were gone.")],
    [S("Warm-Up", [SA("Imperative mood", "commands"), SA("Subjunctive uses “were” for…", "wishes and contrary-to-fact ideas")], cols=2),
     S("Identify the Mood", [SA(q, a) for q, a in [("Lock the door behind you.", "imperative"), ("Why did Jekyll grow pale?", "interrogative"), ("Jekyll trusted Utterson.", "indicative"),
                                                   ("If the cheque were forged, the bank would refuse it.", "subjunctive/conditional"), ("If Utterson waits, he might see Hyde.", "conditional"), ("I suggest that he be careful.", "subjunctive")]], cols=2),
     S("Exit Ticket", [OR("Write a sentence in the subjunctive mood about what you would do if you were Utterson.", "e.g. If I were Utterson, I would go to the police.", lines=2)])],
    te("Students identify and use verb moods.", "Form and use verbs in the indicative, imperative, interrogative, conditional, and subjunctive mood.", "Workbook Lesson 3.11",
       "Command vs imagine.", "Find moods in Chapter 3 dialogue.", ["Teach the chart; the subjunctive were."], "Your Turn 1–3.",
       ["“If I was” in contrary-to-fact."], ["Contrary-to-fact → were."], ["Write an imperative “detective's rules” list."]),
    summary="Moods: indicative, imperative, interrogative, conditional, subjunctive.")

L12 = Lesson("3.12", "Analyzing Voice and Mood for Effect",
    "I can explain how an author's choice of voice and mood creates effects such as suspense.", "L.7.3, RL.7.4",
    [],
    "How can a sentence's grammar make a scene feel mysterious?",
    [P_FOG,
     Example("Analyze effects", "“Someone had left in a hurry.”", ["Indefinite pronoun “someone”: the actor is unknown.", "Past perfect: the event happened before Hale arrived.", "Effect: suspense: we only see the aftermath."],
             "The grammar hides the culprit and places the action just out of reach."),
     KeyIdea("Grammar choices (voice, mood, tense, pronouns) create effects like suspense, distance, or urgency.")],
    [Problem("Find a simile in paragraph 1.", "like dim orange moons / as if wrapped in wool"), Problem("What does the button suggest?", "Someone was there and left a clue."), Problem("Which pronoun creates mystery?", "someone")],
    [S("Warm-Up", [SA("Passive voice can hide…", "the actor"), SA("Past perfect shows…", "an earlier action")], cols=2),
     S("Analyze", [OR("Find two grammar or word choices that create suspense. Explain each.", "“Someone had left in a hurry” (unknown actor, past perfect); short sentences “A door creaked. Footsteps hurried away.” create tension.", lines=4),
                   OR("Rewrite paragraph 2 so the culprit is visible (active voice, named person). How does the effect change?", "e.g. A tall man in a black coat creaked open the door and ran. Suspense decreases.", lines=4)], passage=P_FOG),
     S("Exit Ticket", [OR("Find a sentence in Chapter 3 where Stevenson's grammar creates an effect. Explain.", "Answers vary.", lines=2)])],
    te("Students analyze grammar for effect.", "Use knowledge of language to achieve effects; analyze word choice.", "Workbook Lesson 3.12",
       "Grammar and mystery.", "Read “Fog over the City.”", ["Model the analysis."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Labeling grammar without explaining effect."], ["Choice → effect frame."], ["Write a suspenseful paragraph using passive voice purposefully."]),
    summary="Grammar choices create effects like suspense.")

# ================================================================= Week 4 · Verb consistency and editing (Chapter 4)
L13 = Lesson("3.13", "Clues, Red Herrings, and Foreshadowing",
    "I can analyze how an author plants clues and foreshadows events.", "RL.7.3, RL.7.1",
    [("foreshadowing", "Hints about what will happen later."), ("red herring", "A misleading clue.")],
    "What clue in Chapter 4 points directly to Hyde?",
    [ReaderAssign(JH, "Chapter 4: The Carew Murder Case", "Who witnesses the crime? What evidence is found? What does Utterson recognize?"),
     Text("Mystery writers plant <b>clues</b> (and sometimes <b>red herrings</b>) and <b>foreshadow</b> later events. Careful readers track them and ask what they point to."),
     Figure(lambda t: table(t, [["Clue in Chapter 4", "What it suggests"], ["a maid witnesses the attack and recognizes Hyde", "Hyde is the murderer"], ["half of a broken cane", "a physical link to the killer"],
                                ["Utterson recognizes the cane", "a link to Jekyll (Utterson had given it to him)"], ["Hyde's rooms are ransacked; he has fled", "Hyde had warning or planned escape"]],
                            [2.8 * inch, 2.8 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Track clues and foreshadowing; ask what each points to and whether it might mislead.")],
    [Problem("Who was murdered?", "Sir Danvers Carew"), Problem("Why is the cane important?", "Utterson had given it to Jekyll, linking the murder to Jekyll."), Problem("What is a red herring?", "a misleading clue")],
    [S("Warm-Up", [SA("Foreshadowing =", "hints about the future"), SA("Red herring =", "misleading clue")], cols=2),
     S("Clue Tracker", [OR("List three clues from Chapters 1–4 that connect Jekyll and Hyde.", "the cheque signed by Jekyll; the will; the cane given to Jekyll; Jekyll's reaction to Hyde's name", lines=4),
                        OR("What do you predict Utterson will do next? Base your prediction on clues.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Which clue do you think is most important? Why?", "Answers vary.", lines=2)])],
    te("Students analyze clues and foreshadowing.", "Cite evidence; analyze how elements interact.", "Jekyll and Hyde Reader (Chapter 4), workbook Lesson 3.13",
       "The direct clue.", "Read Chapter 4.", ["Model the clue chart."], "Your Turn 1–3.",
       ["Ignoring small details."], ["Detective notebook."], ["Write a red herring for your own mystery."]),
    summary="Clues and foreshadowing point toward the solution.")

L14 = Lesson("3.14", "Avoiding Shifts in Tense, Voice, and Mood",
    "I can recognize and correct inappropriate shifts in verb tense, voice, and mood.", "L.7.1, L.8.1d",
    [("shift", "An unnecessary change in tense, voice, or mood within a sentence or paragraph.")],
    "What's wrong with: “Utterson walks to the house and knocked on the door”?",
    [rules([["Shift", "Error", "Fix"], ["tense", "Utterson walks to the house and knocked.", "Utterson walked to the house and knocked."], ["voice", "The maid saw the attack, and the police were called by her.", "The maid saw the attack and called the police."],
            ["mood", "Find the cane, and then you should call the inspector.", "Find the cane, and then call the inspector."]], (0.8, 2.6, 2.4), fs=9),
     Text("When writing about literature, use the <b>literary present</b> consistently: <i>Utterson visits Jekyll and asks about Hyde.</i>"),
     KeyIdea("Keep tense, voice, and mood consistent unless meaning requires a change. Write about literature in the present tense.")],
    [Problem("Fix: Hyde ran away and hides.", "Hyde ran away and hid. (or runs … hides)"), Problem("Fix: Jekyll wrote the letter, and it was signed by him.", "Jekyll wrote and signed the letter."), Problem("Which tense is used to write about literature?", "present")],
    [S("Warm-Up", [SA("Literary present example", "Utterson visits Jekyll."), SA("A shift in voice is from active to…", "passive")], cols=2),
     S("Fix the Shifts", [SA(q, a) for q, a in [("The maid looks out the window and saw a man.", "The maid looked out the window and saw a man. (or looks … sees)"),
                                                ("Utterson read the will, and then a visit was paid to Lanyon.", "Utterson read the will and then visited Lanyon."),
                                                ("Be careful, and you should lock the door.", "Be careful, and lock the door."), ("In the novel, Jekyll seemed calm, but he grows pale.", "In the novel, Jekyll seems calm, but he grows pale.")]], cols=1),
     S("Exit Ticket", [OR("Write two sentences about Chapter 4 in the literary present with no shifts.", "Answers vary.", lines=2)])],
    te("Students correct shifts.", "Recognize and correct inappropriate shifts in verb voice and mood (and tense).", "Workbook Lesson 3.14",
       "walks … knocked.", "Find consistent tense in a past essay.", ["Teach the chart; literary present."], "Your Turn 1–3.",
       ["Shifting between past and present in essays."], ["Highlight every verb."], ["Edit an old essay for shifts."]),
    summary="Keep tense, voice, and mood consistent; use literary present.")

L15 = Lesson("3.15", "Writing a News Report",
    "I can write an objective news report with consistent verbs.", "W.7.2, W.7.4",
    [("lead", "The first sentence of a news story; answers who, what, when, where, why, and how."), ("inverted pyramid", "News structure that puts the most important information first.")],
    "If you were a London reporter in 1886, how would you report the Carew murder?",
    [Text("News reports use the <b>inverted pyramid</b>: the most important facts first, details after. They are objective, use past tense consistently, and quote witnesses."),
     Example("Write a lead", "The Carew murder", ["Who: Sir Danvers Carew.", "What: was killed.", "Where/when: a London street, late at night.", "How: beaten with a cane; a maid witnessed it."],
             "Sir Danvers Carew, a respected member of Parliament, was beaten to death on a London street late last night, according to a maid who witnessed the attack from her window."),
     KeyIdea("Lead with the 5 Ws and H, then add details in order of importance. Stay objective and consistent.")],
    [Problem("What goes in a lead?", "who, what, when, where, why, how"), Problem("Is a news report objective or subjective?", "objective"), Problem("Why might a reporter use passive voice in the lead?", "to emphasize the victim when the attacker is not confirmed")],
    [S("Warm-Up", [SA("Inverted pyramid puts…", "most important information first"), SA("A news report is written in ___ tense.", "past")], cols=2),
     S("Write", [OR("Write a news report (2–3 paragraphs) about the Carew murder for an 1886 London newspaper. Include a lead, details in order of importance, a witness quotation, and consistent past tense.", "Answers vary.", lines=18,
                    note="Score: lead with 5 Ws (1); details in order (1); objective tone (1); quotation (1); consistent verbs (1).")])],
    te("Students write news reports.", "Write informative texts; produce writing appropriate to task and audience.", "Workbook Lesson 3.15",
       "1886 reporter.", "Review Chapter 4 facts.", ["Model a lead."], "Draft.",
       ["Opinions in news.", "Tense shifts."], ["5 Ws chart."], ["Add a headline and illustration."], independent="Write the report."),
    summary="News: lead with 5 Ws, inverted pyramid, objective, consistent.")

L16 = Lesson("3.16", "Editing for Pronouns and Verbs",
    "I can edit writing for pronoun and verb errors.", "L.7.1, W.7.5",
    [],
    "Which grammar error from this unit do you make most often?",
    [Figure(lambda t: table(t, [["Editing checklist", "✓"], ["Pronoun case correct (I/me, he/him, who/whom).", ""], ["Every pronoun has one clear antecedent.", ""], ["Pronouns agree with antecedents (each … his or her).", ""],
                                ["No -self pronouns as subjects or objects.", ""], ["Tense is consistent; perfect tenses show order.", ""], ["No unnecessary shifts in voice or mood.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Edit pronouns and verbs with a checklist, one item at a time.")],
    [Problem("Fix: Him and me read the novel.", "He and I read the novel."), Problem("Fix: Everyone brought their own book. (formal)", "Everyone brought his or her own book. / All of the students brought their own books."), Problem("Fix: If I was Jekyll, I would confess.", "If I were Jekyll, I would confess.")],
    [S("Warm-Up", [SA("who = he or him?", "he"), SA("Subjunctive: If I ___ you", "were")], cols=2),
     S("Edit", [SA(q, a) for q, a in [("Utterson and myself suspects Hyde.", "Utterson and I suspect Hyde."), ("The butler told Utterson that he was afraid.", "e.g. The butler told Utterson, “I am afraid.”"),
                                      ("Each of the doors were locked.", "Each of the doors was locked."), ("Hyde runs away and was never seen again.", "Hyde ran away and was never seen again."),
                                      ("Whom opened the door?", "Who opened the door?")]], cols=1),
     S("Edit Your Report", [OR("Edit your news report using the checklist. List three corrections.", "Answers vary.", lines=3)])],
    te("Students edit for pronouns and verbs.", "Demonstrate command of grammar; edit writing.", "Workbook Lesson 3.16, Unit 3 Review",
       "Most common error.", "Review the checklist.", ["Model editing."], "Edit.",
       ["Rushing the checklist."], ["One item per pass."], ["Teach a grammar rule to the family."], independent="Edit; then the Unit 3 Review.", exit_="Tomorrow: Unit 3 Test."),
    summary="Edit pronouns and verbs with a checklist.")

# ================================================================= checks
C1 = Check("Weekly Check 7: Pronouns and Reference", [S("Read and answer", [
    SA("Fix: Leo and her had keys.", "Leo and she had keys."), SA("Leo says “Only you and me.” Which case is “me”? What would formal writing use?", "objective; formal: “Only you and I (have a key)”"),
    SA("Fix the ambiguous pronoun: Ms. Patel told the cleaner that she had lost the key.", "e.g. Ms. Patel told the cleaner, “I lost the key.”"),
    OR("What is the central puzzle of this mystery?", "How was the map taken from a locked room?", lines=2),
    OR("Which detail might be a clue, and which might be a red herring? Explain.", "e.g. Leo's hesitation (clue or red herring); the cleaning company (possible suspect).", lines=3)], passage=P_C7)], minutes=20)
C2 = Check("Weekly Check 8: Agreement and Characterization", [S("Read and answer", [
    SA("Each of the teachers ___ (was/were) surprised.", "was"), SA("Several of the townspeople ___ (owe/owes) him thanks.", "owe"),
    SA("Who or whom: The man ___ everyone misjudged was generous.", "whom"), SA("Intensive pronoun example about Mr. Grimsby", "e.g. Mr. Grimsby himself wrote the letters."),
    OR("How does the author use the townspeople's reactions to characterize Mr. Grimsby?", "They thought he was a miser, so the surprise reveals his hidden generosity.", lines=3),
    OR("State the theme.", "Appearances can be misleading; generosity can be quiet.", lines=2)], passage=P_C8)], minutes=20)
C3 = Check("Weekly Check 9: Verbs", [S("Read and answer", [
    SA("Tense of “had worked”", "past perfect"), SA("Voice of “The murky sample was poured into the beaker.”", "passive"), SA("Rewrite that sentence in active voice.", "Lena poured the murky sample into the beaker."),
    SA("Mood of “Record everything.”", "imperative"), SA("Mood of “If it worked, it would clean polluted water.”", "conditional"), SA("Mood of “Be sure that every step is written down.”", "imperative"),
    OR("Why might the author use passive voice for the sample being poured?", "It focuses on the sample/experiment rather than Lena; scientific style.", lines=2)], cols=1, passage=P_C9)], minutes=20)

REVIEW = Check("Unit 3 Review", [
    S("Pronouns", [SA("(Who/Whom) did Utterson trust?", "Whom"), SA("Fix: Jekyll and me disagreed.", "Jekyll and I disagreed."), SA("Neither of the men ___ (was/were) honest.", "was"), SA("Fix: Myself found the key.", "I found the key.")], cols=2),
    S("Verbs", [SA("Past perfect of <i>leave</i> (Hyde)", "Hyde had left"), SA("Active or passive: Carew was killed.", "passive"), SA("Mood: If I were you, I'd hide.", "subjunctive"), SA("Fix the shift: She opens the door and screamed.", "She opened the door and screamed.")], cols=2),
    S("Reading", [OR("What is a frame narrative? Give an example from Chapter 1.", "a story within a story; Enfield tells the story of the door", lines=2)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 3 Test", [
    S("Part A · Reading (1 point each)", [
        OR("What is the central mystery in paragraphs 1–2?", "Why did the violinist vanish, and what does “Ask the twin” mean?", lines=2),
        OR("Identify one clue and one red herring. Explain each.", "Clue: the empty case (he took the violin, so he planned to leave). Red herring: “Ask the twin” points to Luca, who is innocent.", lines=3, points=2),
        OR("How does Luca's reaction characterize him?", "He goes pale and whispers “He has done it again”: he knows his brother's pattern and is hurt/worried.", lines=2),
        OR("Explain the metaphor “Perfection is a cage I built myself.”", "His need to be perfect trapped him; he created his own prison.", lines=2),
        OR("State a theme of the story.", "Striving for perfection can imprison us; beauty matters more than perfection.", lines=2)], passage=P_TEST),
    S("Part B · Pronouns (1 point each)", [
        SA("(Who/Whom) did Okoro find at the café?", "Whom"), SA("Fix: Okoro and him spoke.", "Okoro and he spoke."), SA("Each of the musicians ___ (was/were) waiting.", "was"),
        SA("Fix the ambiguity: Marco told Luca that he was afraid.", "e.g. Marco told Luca, “I am afraid.”")], cols=1),
    S("Part C · Verbs (1 point each)", [
        SA("Voice: “The performance would be canceled.”", "passive"), SA("Rewrite in active voice.", "The conductor would cancel the performance."), SA("Tense of “had been practicing”", "past perfect progressive"),
        SA("Fix the shift: Okoro enters the room and saw the case.", "Okoro entered the room and saw the case."), SA("Fix the mood: If I was Marco, I would play.", "If I were Marco, I would play.")], cols=1),
    S("Part D · Writing (5 points)", [OR("Write a short news report about the vanishing violinist for the next morning's paper. Use a strong lead, the inverted pyramid, an objective tone, one quotation, and consistent past tense.",
                                         "Rubric: lead (1); inverted pyramid (1); objective tone (1); quotation (1); consistent verbs and clear pronouns (1).", lines=14, points=5)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-12-14", "2027-01-04", "2027-01-11", "2027-01-18"], CHECKS, REVIEW, TEST)

UNIT = Unit(3, "Mystery and Grammar", "Mystery structure and characterization, pronouns, verb tense, voice, and mood, with Strange Case of Dr. Jekyll and Mr. Hyde, Chapters 1–4.",
    "Fog-filled London streets, a sinister stranger, and a respectable doctor with a secret: Stevenson's <i>Strange Case of Dr. Jekyll and Mr. Hyde</i> is one of the most famous mysteries ever written. As you investigate alongside Mr. Utterson, you'll also investigate how grammar works: how pronouns keep meaning clear and how verbs control time, focus, and attitude.",
    ["Analyze mystery structure, frame narratives, characterization, clues, and foreshadowing.", "Use pronoun case, clear reference, and agreement correctly.",
     "Use and analyze verb tenses, active and passive voice, and moods.", "Avoid shifts; write and edit an objective news report."],
    [("RL.7.1, RL.7.3–5", "Cite evidence; analyze elements, word choice, and structure."), ("L.7.1, L.7.3", "Demonstrate command of grammar; use language for effect, including voice and mood."),
     ("W.7.2, W.7.4, W.7.5", "Write informative texts appropriate to task; edit.")],
    [("frame narrative", "A story within a story."), ("antecedent", "The noun a pronoun refers to."), ("passive voice", "The subject receives the action."), ("subjunctive", "The mood for wishes and contrary-to-fact ideas."),
     ("foreshadowing", "Hints about later events.")],
    ["Unit 2 nouns; Grade 6 pronoun basics."], ["Strange Case of Dr. Jekyll and Mr. Hyde Reader (Chapters 1–4)", "A notebook for clue tracking"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Clear pronouns and consistent verbs matter in every report, email, and essay, and noticing passive voice helps you see when someone is avoiding responsibility.",
    family_note="Ask your student to share their clue tracker and predict the solution, without spoiling the ending for anyone who hasn't read it!",
    weeks=WEEKS)
