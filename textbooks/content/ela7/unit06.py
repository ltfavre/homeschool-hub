"""Grade 7 ELA · Unit 6: Sentence Craft — clauses and sentence types, phrase functions, sentence combining, variety, parallelism, and an analytical essay.
Anchor reading: The Time Machine Reader, Chapters 5–12 (Mar 29 – Apr 23, 2027)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule
from content.ela7.unit05 import TM


def rules(rows, widths, fs=9.5):
    return Figure(lambda t: table(t, rows, [w * inch for w in widths], width=sum(widths) * inch, font_size=fs))


P_UTOPIA = Passage("Utopias and Dystopias", [
    "A <b>utopia</b> is an imagined perfect society, where everyone is happy and no one suffers. The word was coined in 1516 by the English writer Thomas More, who combined Greek roots meaning “no place,” a sly hint that such a perfect world may not exist.",
    "A <b>dystopia</b> is the opposite: an imagined society in which something has gone terribly wrong, often hidden behind a surface that looks peaceful or orderly. Dystopian stories usually exaggerate a problem in the writer's own time to warn readers about where it might lead.",
    "When the Time Traveller first arrives in the year 802,701, he believes he has found a utopia. The Eloi live in a garden-like world without work, war, or disease. But as he explores, he discovers that the beautiful surface hides a disturbing truth. Many readers see <i>The Time Machine</i> as an early dystopian warning about the growing divide between the wealthy and the working poor in Victorian England.",
], source="An original informational text", genre="Informational text")

P_SENT = Passage("The Lighthouse at Dawn", [
    "The storm ended. Gray light crept over the water, and the waves, which had roared all night, settled into a slow, tired rhythm. Because the beam had stayed lit through the darkness, every boat had found the harbor.",
    "Exhausted but proud, the keeper climbed down the tower. She had not slept, she had not eaten, and she had not once doubted that the light mattered.",
], source="An original passage", genre="Descriptive writing")

P_C16 = Passage("The Garden of the Eloi (a retelling)", [
    "The Traveller walked through the ruined city. Flowers grew everywhere, and the air was warm. Although the buildings were enormous, they were crumbling. The Eloi laughed and played in the gardens, but they never seemed to work.",
], source="An original retelling", genre="Narrative", numbered=False)

P_C17 = Passage("The Expedition", [
    "Hoping to find the lost city, the explorers hiked deep into the jungle. Carrying heavy packs and sharp machetes, they cut a path through the vines. Finding the city would change history. They wanted to photograph every wall carved with ancient symbols.",
], source="An original passage", genre="Narrative", numbered=False)

P_C18 = Passage("Choppy Draft", [
    "The museum was dusty. It was old. The Traveller walked through it. He found matches. He found a lever. He used the lever as a weapon. Weena was with him. She was afraid of the dark.",
], source="An original draft for revision", genre="Draft", numbered=False)

P_TEST = Passage("The Seed Vault", [
    "On a frozen island far north of mainland Norway, a tunnel leads deep into a mountain of permafrost. At the end of the tunnel, behind thick steel doors, lies the Svalbard Global Seed Vault, which some people call a “doomsday vault.”",
    "Opened in 2008, the vault stores backup copies of seeds from seed banks around the world. Because crops can be lost to war, disease, or natural disaster, scientists wanted a safe place where samples of the world's food plants could survive almost any catastrophe. The vault can hold about 4.5 million seed samples, and it already holds more than one million.",
    "The location was chosen carefully. Svalbard is remote, politically stable, and geologically quiet. The permafrost keeps the rock naturally cold, so even if the cooling system failed, the seeds would stay frozen for years.",
    "In 2015, the vault was used for the first time. War in Syria had damaged a major seed bank near the city of Aleppo, and researchers withdrew seeds that had been deposited at Svalbard to begin rebuilding the collection elsewhere. The withdrawal proved the vault's purpose: it is not a museum but an insurance policy for the future of farming.",
], source="An original informational text based on facts", genre="Informational text")

# ================================================================= Week 1 · Sentence and clause structure (Chapters 5–6)
L1 = Lesson("6.1", "Utopia or Dystopia?",
    "I can analyze how an author's portrayal of a future society develops a theme.", "RL.7.2, RI.7.2",
    [("utopia", "An imagined perfect society."), ("dystopia", "An imagined society where something has gone terribly wrong.")],
    "Would a world with no work, no war, and no disease be perfect?",
    [ReaderAssign(TM, "Chapters 5–6: In the Golden Age; The Sunset", "What are the Eloi like? What does the Traveller first conclude about their world?"),
     P_UTOPIA,
     Example("Analyze the first impression", "What does the Traveller first believe?", ["He sees gardens, peace, and no labor.", "He concludes humanity has achieved an easy, comfortable life."], "He believes the future is a kind of utopia, though readers sense something is missing."),
     KeyIdea("Utopias and dystopias comment on the author's own time. Look beneath the surface.")],
    [Problem("What do the roots of “utopia” mean?", "no place"), Problem("What are the Eloi like?", "small, gentle, playful, childlike; they don't work"), Problem("What might the Eloi's world warn about?", "a comfortable society that has lost curiosity and strength; class division")],
    [S("Warm-Up", [SA("Utopia =", "a perfect society"), SA("Dystopia =", "a society gone wrong")], cols=2),
     S("Analyze", [OR("Describe the Eloi using three details from Chapters 5–6. What seems missing from their lives?", "Answers vary; small, fragile, childlike, easily distracted; missing curiosity, effort, knowledge.", lines=4),
                   OR("Why might Wells show a beautiful world first before revealing its problems?", "To set up a contrast and make the dark truth more shocking; like a dystopia's peaceful surface.", lines=3)], passage=P_UTOPIA),
     S("Exit Ticket", [OR("Is a world without challenges a utopia? Explain your view.", "Answers vary.", lines=2)])],
    te("Students analyze utopia and dystopia.", "Determine themes and central ideas; analyze development.", "The Time Machine Reader (Chapters 5–6), workbook Lesson 6.1",
       "Perfect world?", ["Read Chapters 5–6.", "Read “Utopias and Dystopias.”"], ["Model surface vs truth."], "Your Turn 1–3.",
       ["Accepting the Traveller's first impression."], ["Surface/beneath chart."], ["Design your own utopia and its hidden flaw."]),
    summary="Utopias and dystopias comment on real societies.")

L2 = Lesson("6.2", "Independent and Dependent Clauses",
    "I can identify independent and dependent clauses.", "L.7.1a, L.7.1b",
    [("clause", "A group of words with a subject and a verb."), ("independent clause", "A clause that can stand alone as a sentence."), ("dependent clause", "A clause that cannot stand alone; it begins with a subordinating word.")],
    "Why is “Because the Traveller lost his machine” not a complete sentence?",
    [rules([["Clause", "Example", "Can it stand alone?"], ["independent", "The Traveller lost his machine.", "yes"], ["dependent (adverb)", "because the Traveller lost his machine", "no"],
            ["dependent (adjective)", "which had vanished overnight", "no"], ["dependent (noun)", "that the Eloi were afraid of the dark", "no"]], (1.6, 2.8, 1.3), fs=9),
     Example("Identify clauses", "When night fell, the Eloi hid in their great halls.", ["“When night fell”: subordinating word → dependent.", "“the Eloi hid in their great halls”: independent."], "one dependent + one independent clause"),
     KeyIdea("Every clause has a subject and verb. Dependent clauses begin with subordinating words and need an independent clause.")],
    [Problem("Independent or dependent: although they were gentle", "dependent"), Problem("Independent or dependent: The Eloi feared the dark.", "independent"), Problem("Find the dependent clause: The machine that he built was gone.", "that he built")],
    [S("Warm-Up", [SA("A clause has a subject and a…", "verb"), SA("A subordinating word", "because, although, when, which, that")], cols=2),
     S("Identify", [SA(q, a) for q, a in [("since the sun had set", "dependent"), ("Weena followed him everywhere", "independent"), ("who had saved her from the river", "dependent"), ("The Traveller searched for clues", "independent"),
                                          ("if he could find the machine", "dependent"), ("that the future was dangerous", "dependent")]], cols=2),
     S("Exit Ticket", [OR("Write a sentence with one independent and one dependent clause about Chapter 6. Underline the dependent clause.", "Answers vary.", lines=2)])],
    te("Students identify clauses.", "Explain the function of phrases and clauses.", "Workbook Lesson 6.2",
       "Incomplete because?", "Find clauses in Chapter 6.", ["Teach the chart."], "Your Turn 1–3.",
       ["Calling phrases clauses."], ["Find the subject and verb first."], ["Clause scavenger hunt."]),
    summary="Independent clauses stand alone; dependent clauses don't.")

L3 = Lesson("6.3", "Four Sentence Types",
    "I can write simple, compound, complex, and compound-complex sentences to signal relationships among ideas.", "L.7.1b",
    [("compound-complex sentence", "Two or more independent clauses and at least one dependent clause.")],
    "How can one idea be written four different ways?",
    [rules([["Type", "Structure", "Example"], ["simple", "one independent clause", "The machine vanished."], ["compound", "two independent clauses", "The machine vanished, and the Traveller panicked."],
            ["complex", "independent + dependent", "When the machine vanished, the Traveller panicked."], ["compound-complex", "two independent + one or more dependent", "When the machine vanished, the Traveller panicked, but he soon began to search."]],
           (1.4, 2.0, 2.4), fs=9),
     KeyIdea("Choose sentence types to show relationships: equal ideas (compound), cause/time/contrast (complex), both (compound-complex).")],
    [Problem("Type: The Eloi laughed, but the Traveller worried.", "compound"), Problem("Type: Because Weena feared the dark, she clung to him.", "complex"), Problem("Type: The sun set.", "simple")],
    [S("Warm-Up", [SA("Compound = two ___ clauses", "independent"), SA("Complex = independent + ___", "dependent")], cols=2),
     S("Identify the Type", [SA(q, a) for q, a in [("Weena slept beside him.", "simple"), ("He lit a match, and the Morlocks fled.", "compound"), ("Although he was tired, he kept walking.", "complex"),
                                                   ("After the fire died, the forest was dark, and Weena was gone.", "compound-complex"), ("The Traveller, who was desperate, searched the sphinx.", "complex")]], cols=1),
     S("Transform", [OR("Rewrite “The Traveller found the machine” as a compound, complex, and compound-complex sentence.", "e.g. Compound: …, and he climbed in. Complex: When he reached the sphinx, the Traveller found the machine. Compound-complex: When the doors opened, the Traveller found the machine, and he leapt inside.", lines=4)])],
    te("Students use four sentence types.", "Choose among simple, compound, complex, and compound-complex sentences to signal differing relationships.", "Workbook Lesson 6.3",
       "Four ways.", "Find each type in Chapter 6.", ["Teach the chart."], "Your Turn 1–3.",
       ["Calling a compound predicate a compound sentence."], ["Count independent clauses."], ["Write a paragraph using all four types."]),
    summary="Simple, compound, complex, compound-complex.")

L4 = Lesson("6.4", "Analyzing Sentence Structure for Effect",
    "I can analyze how sentence structures create rhythm, emphasis, and meaning.", "L.7.3, RL.7.4",
    [],
    "Why might an author follow a long sentence with a very short one?",
    [P_SENT,
     Example("Analyze", "“The storm ended.”", ["Simple, three words, the first sentence.", "Effect: a sudden calm after the chaos; emphasis on relief."], "The short sentence enacts the sudden stillness."),
     Example("Analyze repetition", "“She had not slept, she had not eaten, and she had not once doubted…”", ["Compound sentence with repeated structure.", "Builds to the most important clause."], "The repetition builds to a climax: her faith in the light."),
     KeyIdea("Short sentences emphasize; long sentences build; repeated structures create rhythm and climax.")],
    [Problem("Sentence type: “The storm ended.”", "simple"), Problem("Find the complex sentence that begins with “Because.”", "Because the beam had stayed lit through the darkness, every boat had found the harbor."), Problem("What does the repetition in paragraph 2 emphasize?", "her endurance and faith")],
    [S("Warm-Up", [SA("Short sentences create…", "emphasis"), SA("Repetition creates…", "rhythm")], cols=2),
     S("Analyze", [OR("Identify the type of each sentence in paragraph 1.", "simple; compound (with adjective clause); complex", lines=3),
                   OR("Choose a passage from Chapters 5–6 of the Reader. Analyze how Wells's sentence structure creates an effect.", "Answers vary.", lines=5)], passage=P_SENT),
     S("Exit Ticket", [OR("Write a short paragraph that ends with a three-word sentence for emphasis.", "Answers vary.", lines=3)])],
    te("Students analyze sentence structure for effect.", "Use knowledge of language to achieve effects; analyze word choice.", "Workbook Lesson 6.4",
       "Long then short.", "Read “The Lighthouse at Dawn.”", ["Model both analyses."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Naming types without effects."], ["Type → effect chart."], ["Imitate a sentence pattern from the Reader."]),
    summary="Sentence structure creates emphasis and rhythm.")

# ================================================================= Week 2 · Phrase functions (Chapters 7–8)
L5 = Lesson("6.5", "Revising a Hypothesis",
    "I can analyze how a character's reasoning changes as new evidence appears.", "RL.7.3, RL.7.1",
    [("hypothesis", "A proposed explanation that can be tested.")],
    "What does a good scientist do when the evidence doesn't fit the theory?",
    [ReaderAssign(TM, "Chapters 7–8: A Sudden Shock; Explanation", "What happens to the machine? What new creatures does the Traveller glimpse? How does his explanation change?"),
     Text("The Traveller thinks like a scientist. He forms a <b>hypothesis</b> about the future, then revises it when new evidence appears. Tracking these revisions shows how Wells builds suspense and develops theme."),
     Figure(lambda t: table(t, [["Evidence", "Traveller's explanation"], ["peaceful gardens, no labor (Ch. 5–6)", "humanity has reached a comfortable, easy life"], ["machine stolen; strange wells; pale creatures at night (Ch. 7–8)", "another species lives underground"],
                                ["Morlocks' behavior (later)", "the two species descend from divided social classes"]], [2.6 * inch, 3.0 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Track how a character's theory changes with evidence; each revision deepens the theme.")],
    [Problem("What is a hypothesis?", "a proposed explanation that can be tested"), Problem("What evidence challenges the Traveller's first theory?", "the stolen machine, the wells, pale creatures"), Problem("Why does revising a hypothesis build suspense?", "Each new clue reveals the world is more dangerous than it seemed.")],
    [S("Warm-Up", [SA("Hypothesis =", "a testable explanation"), SA("Where was the machine taken?", "into the White Sphinx (pedestal)")], cols=2),
     S("Track the Reasoning", [OR("Explain the Traveller's first hypothesis and the evidence for it.", "Answers vary.", lines=3), OR("What new evidence appears in Chapters 7–8? How does his hypothesis change?", "Answers vary.", lines=4)]),
     S("Exit Ticket", [OR("Is the Traveller a good scientist? Explain with evidence.", "Answers vary; yes, he revises when evidence changes.", lines=2)])],
    te("Students analyze a character's reasoning.", "Analyze how elements interact; cite evidence.", "The Time Machine Reader (Chapters 7–8), workbook Lesson 6.5",
       "Evidence vs theory.", "Read Chapters 7–8.", ["Model the chart."], "Your Turn 1–3.",
       ["Treating the first theory as the truth."], ["Evidence → theory chart."], ["Compare to a real scientific revision."]),
    summary="Characters revise hypotheses as evidence changes.")

L6 = Lesson("6.6", "Five Kinds of Phrases",
    "I can identify prepositional, appositive, participial, gerund, and infinitive phrases and their functions.", "L.7.1a",
    [("phrase", "A group of related words without both a subject and a verb.")],
    "In “Searching for the machine, the Traveller pried at the sphinx,” what does “Searching for the machine” describe?",
    [rules([["Phrase", "Starts with", "Function", "Example"], ["prepositional", "a preposition", "adjective/adverb", "<b>under the sphinx</b>"], ["appositive", "a noun", "renames a noun", "Weena, <b>an Eloi girl</b>, …"],
            ["participial", "-ing or -ed verb form", "adjective", "<b>Exhausted by the search</b>, he rested."], ["gerund", "-ing verb form", "noun", "<b>Finding the machine</b> was his goal."],
            ["infinitive", "to + verb", "noun, adjective, or adverb", "He wanted <b>to escape</b>."]], (1.1, 1.3, 1.4, 1.9), fs=8.5),
     Example("Participial vs gerund", "“Searching for the machine” in two sentences", ["Searching for the machine, the Traveller pried at the sphinx. → describes the Traveller → participial.", "Searching for the machine took days. → acts as the subject → gerund."], "Same words, different functions."),
     KeyIdea("Identify a phrase by its first word and its job in the sentence.")],
    [Problem("Phrase type: to find Weena", "infinitive"), Problem("Phrase type: Frightened by the dark, Weena trembled.", "participial (Frightened by the dark)"), Problem("Phrase type: Lighting matches kept the Morlocks away.", "gerund (Lighting matches)")],
    [S("Warm-Up", [SA("Gerunds act as…", "nouns"), SA("Participial phrases act as…", "adjectives")], cols=2),
     S("Identify the Bold Phrase", [SA(q, a) for q, a in [("<b>Holding a match</b>, he stepped forward.", "participial"), ("<b>Exploring the ruins</b> was dangerous.", "gerund"), ("He hoped <b>to return home</b>.", "infinitive"),
                                                          ("The Morlocks, <b>pale creatures of the dark</b>, feared light.", "appositive"), ("They hid <b>beneath the ground</b>.", "prepositional"), ("<b>To understand the future</b> became his obsession.", "infinitive")]], cols=1),
     S("Exit Ticket", [OR("Write sentences using a participial phrase and a gerund phrase with the same words.", "e.g. Climbing the hill, he saw the city. / Climbing the hill took an hour.", lines=2)])],
    te("Students identify phrase types.", "Explain the function of phrases in general and their function in specific sentences.", "Workbook Lesson 6.6",
       "What does it describe?", "Find phrases in Chapter 8.", ["Teach the chart; participle vs gerund."], "Your Turn 1–3.",
       ["Confusing gerunds and participles."], ["Ask: noun job or describing job?"], ["Phrase scavenger hunt."]),
    summary="Prepositional, appositive, participial, gerund, infinitive.")

L7 = Lesson("6.7", "Participial Phrases as Modifiers",
    "I can use participial phrases to add detail and punctuate them correctly.", "L.7.1a, L.7.1c",
    [("participle", "A verb form used as an adjective: frightened, glowing.")],
    "How can you combine “Weena was frightened” and “Weena clung to him” into one smooth sentence?",
    [Text("Participial phrases add action and detail. An introductory participial phrase is followed by a comma, and it must describe the subject right after the comma (or it dangles)."),
     Example("Combine", "Weena was frightened by the dark. She clung to the Traveller.", ["Turn the first sentence into a participial phrase.", "Place it next to “she.”"], "Frightened by the dark, Weena clung to the Traveller."),
     KeyIdea("Use participial phrases to combine and add detail; place them next to the noun they describe.")],
    [Problem("Combine: The Traveller was exhausted. He fell asleep.", "Exhausted, the Traveller fell asleep."), Problem("Fix: Glowing in the dark, the Traveller saw their eyes.", "The Traveller saw their eyes glowing in the dark."), Problem("Comma after an introductory participial phrase?", "Yes")],
    [S("Warm-Up", [SA("Participles act as…", "adjectives"), SA("Introductory participial phrase needs a…", "comma")], cols=2),
     S("Combine", [SA(q, a) for q, a in [("The Morlocks were blinded by the light. They retreated.", "Blinded by the light, the Morlocks retreated."), ("Weena was laughing. She chased the butterflies.", "Laughing, Weena chased the butterflies."),
                                         ("The Traveller gripped the iron bar. He waited.", "Gripping the iron bar, the Traveller waited."), ("The palace was covered in dust. It stood on a hill.", "Covered in dust, the palace stood on a hill.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence about Chapter 8 that begins with a participial phrase.", "Answers vary.", lines=2)])],
    te("Students use participial phrases.", "Use phrases to convey meaning and add variety; place modifiers correctly.", "Workbook Lesson 6.7",
       "Combine Weena sentences.", "Find participial phrases in the Reader.", ["Model combining."], "Your Turn 1–3.",
       ["Dangling participles."], ["Check: who is doing it?"], ["Revise a past paragraph with three participial phrases."]),
    summary="Participial phrases add detail; place them next to the subject.")

L8 = Lesson("6.8", "Gerunds and Infinitives as Nouns",
    "I can use gerund and infinitive phrases as subjects and objects.", "L.7.1a",
    [("gerund", "An -ing verb form used as a noun."), ("infinitive", "To + a verb, used as a noun, adjective, or adverb.")],
    "What is the subject of “Finding the machine became his only goal”?",
    [rules([["Function", "Gerund", "Infinitive"], ["subject", "<b>Exploring the ruins</b> was risky.", "<b>To explore the ruins</b> was risky."], ["direct object", "He enjoyed <b>studying the stars</b>.", "He wanted <b>to study the stars</b>."],
            ["predicate noun", "His goal was <b>finding the machine</b>.", "His goal was <b>to find the machine</b>."]], (1.3, 2.2, 2.2), fs=9),
     KeyIdea("Gerund and infinitive phrases can act as nouns: subjects, objects, and predicate nouns.")],
    [Problem("Function of “to warn his friends” in “He decided to warn his friends.”", "direct object (infinitive)"), Problem("Function of “Escaping the Morlocks” in “Escaping the Morlocks required fire.”", "subject (gerund)"), Problem("Gerund in “Weena loved collecting flowers.”", "collecting flowers")],
    [S("Warm-Up", [SA("Gerunds end in…", "-ing"), SA("Infinitives begin with…", "to")], cols=2),
     S("Identify Phrase and Function", [SA(q, a) for q, a in [("Traveling through time made him ill.", "gerund; subject"), ("The Eloi refused to enter the dark.", "infinitive; direct object"), ("His dream was to return.", "infinitive; predicate noun"),
                                                             ("Weena enjoyed walking beside him.", "gerund; direct object"), ("To light a fire seemed wise.", "infinitive; subject")]], cols=1),
     S("Exit Ticket", [OR("Write one sentence with a gerund subject and one with an infinitive object about the Traveller.", "Answers vary.", lines=2)])],
    te("Students use gerund and infinitive phrases.", "Explain the function of phrases.", "Workbook Lesson 6.8",
       "What's the subject?", "Find gerunds in Chapter 8.", ["Teach the chart."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Calling every -ing word a gerund."], ["Noun test: replace with “it.”"], ["Rewrite five sentences switching gerunds and infinitives."]),
    summary="Gerund and infinitive phrases can act as nouns.")

# ================================================================= Week 3 · Combine sentences precisely (Chapters 9–10)
L9 = Lesson("6.9", "Allegory and Social Commentary",
    "I can analyze how a story functions as an allegory or social commentary.", "RL.7.2, RL.7.6",
    [("allegory", "A story in which characters and events represent larger ideas."), ("social commentary", "Writing that criticizes or comments on society.")],
    "Why might the Eloi live above ground and the Morlocks below?",
    [ReaderAssign(TM, "Chapters 9–10: Morlocks; Night", "What does the Traveller discover underground? What is the relationship between the Eloi and the Morlocks?"),
     Text("The Traveller concludes that the Eloi descended from the leisured upper class and the Morlocks from the laboring class who worked underground. Over time, the divide became so extreme that humanity split into two species. Many readers see this as Wells's <b>social commentary</b> on class inequality in Victorian England."),
     Figure(lambda t: table(t, [["Story element", "May represent"], ["Eloi above ground in gardens", "the wealthy who don't work"], ["Morlocks underground with machines", "industrial workers"], ["Morlocks preying on Eloi", "the danger of extreme inequality"],
                                ["Eloi helplessness", "comfort without effort leading to weakness"]], [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     KeyIdea("Allegories use characters and events to comment on real ideas or society.")],
    [Problem("What is an allegory?", "a story in which characters and events represent larger ideas"), Problem("What might the Morlocks represent?", "industrial workers / the laboring class"), Problem("What is Wells warning about?", "extreme class inequality")],
    [S("Warm-Up", [SA("Allegory =", "story representing larger ideas"), SA("Social commentary =", "commenting on society")], cols=2),
     S("Analyze", [OR("Explain how the Eloi and Morlocks reflect Victorian class division. Cite evidence from Chapters 9–10.", "Answers vary.", lines=5),
                   OR("Is the Traveller's explanation certain? How do you know?", "No; he admits it is a theory based on limited evidence.", lines=3)]),
     S("Exit Ticket", [OR("What might Wells want readers in 1895 to do or think after reading?", "Answers vary; address inequality, value effort and knowledge.", lines=2)])],
    te("Students analyze allegory.", "Determine theme; analyze point of view and purpose.", "The Time Machine Reader (Chapters 9–10), workbook Lesson 6.9",
       "Above and below.", "Read Chapters 9–10.", ["Model the allegory chart."], "Your Turn 1–3.",
       ["Treating allegory as literal prediction."], ["Element → idea chart."], ["Research Victorian factory conditions."]),
    summary="Allegory uses story to comment on society.")

L10 = Lesson("6.10", "Combining with Conjunctions and Relative Clauses",
    "I can combine sentences with conjunctions and relative clauses to show precise relationships.", "L.7.1b, L.7.3a",
    [],
    "How can three short sentences become one clear sentence?",
    [Example("Combine", "The Morlocks lived underground. They were pale. They feared light.", ["Use a relative clause for one detail.", "Join actions with and."], "The Morlocks, who lived underground, were pale and feared light."),
     rules([["Relationship", "Tool", "Example"], ["addition", "and, also; relative clause", "Weena, who was gentle, followed him."], ["contrast", "but, although, while", "Although the Eloi were beautiful, they were helpless."],
            ["cause", "because, since, so", "Because the Morlocks feared light, he lit matches."], ["time", "when, after, before, until", "When night fell, the Eloi huddled together."]], (1.0, 1.8, 2.8), fs=9),
     KeyIdea("Combine to show the exact relationship; use relative clauses for extra detail.")],
    [Problem("Combine: Weena was small. She was brave.", "Weena was small but brave."), Problem("Combine: The fire spread. The Morlocks fled. (cause)", "Because the fire spread, the Morlocks fled."), Problem("Combine with a relative clause: The palace was a museum. It was ruined.", "The palace, which was a ruined museum, …")],
    [S("Warm-Up", [SA("Contrast conjunction", "but, although"), SA("Relative pronoun", "who, which, that")], cols=2),
     S("Combine", [SA(q, a) for q, a in [("The Traveller found matches. They were in a sealed case.", "The Traveller found matches that were in a sealed case."), ("It was dark. The Morlocks came closer.", "As it grew dark, the Morlocks came closer."),
                                         ("The Eloi were frightened. They did nothing.", "The Eloi were frightened, but they did nothing."), ("The machine was hidden. The Traveller couldn't escape.", "Because the machine was hidden, the Traveller couldn't escape.")]], cols=1),
     S("Exit Ticket", [OR("Combine three short sentences of your own into one precise sentence.", "Answers vary.", lines=2)])],
    te("Students combine with conjunctions and clauses.", "Choose sentence types to signal relationships; express ideas precisely.", "Workbook Lesson 6.10",
       "Three into one.", "Find combined sentences in Chapter 10.", ["Model combining."], "Your Turn 1–3.",
       ["Combining with the wrong relationship word."], ["Relationship menu."], ["Combine a choppy paragraph."]),
    summary="Combine to show exact relationships.")

L11 = Lesson("6.11", "Combining with Phrases",
    "I can combine sentences using appositive, participial, and prepositional phrases.", "L.7.1a, L.7.3a",
    [],
    "What's the shortest clear way to say the Traveller, a scientist, lit a match?",
    [Example("Combine with phrases", "The Traveller was a scientist. He studied the Morlocks. He hid behind a pillar.", ["Appositive: a scientist.", "Participial: Hiding behind a pillar.", "Main clause: the Traveller studied the Morlocks."],
             "Hiding behind a pillar, the Traveller, a scientist, studied the Morlocks."),
     KeyIdea("Phrases combine sentences more tightly than conjunctions; check for clarity and correct punctuation.")],
    [Problem("Combine with an appositive: Weena was an Eloi girl. She gave him flowers.", "Weena, an Eloi girl, gave him flowers."), Problem("Combine with a participial phrase: He carried a lever. He walked into the dark.", "Carrying a lever, he walked into the dark."), Problem("Combine with a prepositional phrase: He slept. He was by the fire.", "He slept by the fire.")],
    [S("Warm-Up", [SA("Appositive renames a…", "noun"), SA("Participial phrase acts as an…", "adjective")], cols=2),
     S("Combine", [SA(q, a) for q, a in [("The sphinx was white. It was made of stone. It stood on a bronze pedestal.", "The white stone sphinx stood on a bronze pedestal."), ("The Traveller was tired. He was hungry. He sat on the grass.", "Tired and hungry, the Traveller sat on the grass."),
                                         ("The museum was the Palace of Green Porcelain. It was full of old machines.", "The museum, the Palace of Green Porcelain, was full of old machines."), ("The Morlocks climbed. They climbed out of the wells.", "The Morlocks climbed out of the wells.")]], cols=1),
     S("Exit Ticket", [OR("Combine into one sentence using a phrase: The fire was spreading. It was roaring. It was moving toward the hill.", "e.g. Roaring, the fire spread toward the hill.", lines=2)])],
    te("Students combine with phrases.", "Use phrases to convey precise meaning; reduce wordiness.", "Workbook Lesson 6.11",
       "Shortest clear way.", "Model sentences from Chapter 10.", ["Model combining with phrases."], "Your Turn 1–3.",
       ["Dangling participles when combining."], ["Check the subject."], ["Sentence-combining challenge."]),
    summary="Phrases combine sentences tightly.")

L12 = Lesson("6.12", "Precision vs. Over-Combining",
    "I can judge when combining improves clarity and when it creates confusing sentences.", "L.7.3a, W.7.5",
    [],
    "Is a longer sentence always better?",
    [Text("Combining can make writing smoother, but over-combined sentences pile up clauses until readers get lost. Aim for clarity: each sentence should have one main idea and clear relationships."),
     Example("Over-combined", "The Traveller, who was exhausted after the long night, which had been terrifying because the Morlocks, who feared light, had surrounded him, finally reached the sphinx, which was open.",
             ["Too many nested clauses.", "Split into two or three clear sentences."], "After a terrifying night surrounded by Morlocks, the exhausted Traveller finally reached the sphinx. To his surprise, its doors were open."),
     KeyIdea("Combine for clarity, not length. If a sentence needs rereading, split it.")],
    [Problem("When should you split a sentence?", "when it has too many clauses and readers get lost"), Problem("What should each sentence have?", "one main idea with clear relationships"), Problem("Is a longer sentence always better?", "No")],
    [S("Warm-Up", [SA("Over-combining causes…", "confusion"), SA("Goal of combining", "clarity and flow")], cols=2),
     S("Fix Over-Combined Sentences", [OR("Rewrite clearly: Weena, who was the Eloi girl whom the Traveller had saved from the river where she was drowning while the others watched, followed him, which pleased him because he was lonely.",
                                          "e.g. The Traveller had saved Weena from drowning while the other Eloi watched. Afterward, she followed him everywhere, which pleased him because he was lonely.", lines=4)]),
     S("Revise Your Writing", [OR("Find one choppy passage and one over-combined sentence in your past writing. Revise both.", "Answers vary.", lines=4)])],
    te("Students balance combining and clarity.", "Choose language that expresses ideas precisely and concisely.", "Workbook Lesson 6.12",
       "Longer better?", "Read the over-combined example aloud.", ["Model splitting."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Equating long with sophisticated."], ["Read aloud; out of breath = split."], ["Edit a sibling's writing."]),
    summary="Combine for clarity, not length.")

# ================================================================= Week 4 · Revise sentence variety and clarity (Chapters 11–12)
L13 = Lesson("6.13", "Symbolism in the Palace and the Fire",
    "I can analyze symbols and how they develop the novel's themes.", "RL.7.2, RL.7.4",
    [],
    "What might a ruined museum full of forgotten machines symbolize?",
    [ReaderAssign(TM, "Chapters 11–12: The Palace of Green Porcelain; In the Darkness", "What does the Traveller find in the museum? What happens in the forest?"),
     Figure(lambda t: table(t, [["Symbol", "Possible meaning"], ["the ruined museum", "lost human knowledge and achievement"], ["rotting books", "the decay of learning and curiosity"],
                                ["matches and fire", "human ingenuity; also its danger when uncontrolled"], ["the dark forest", "fear, danger, the unknown"], ["Weena's flowers", "kindness and humanity in a fallen world"]],
                            [2.0 * inch, 3.6 * inch], width=5.6 * inch)),
     KeyIdea("Symbols connect objects to themes; explain how each develops the novel's warning.")],
    [Problem("What does the ruined museum suggest?", "humanity's knowledge and achievements have been lost"), Problem("How is fire both helpful and harmful?", "It protects from Morlocks but also spreads out of control (and Weena is lost)."), Problem("What theme do these symbols develop?", "the decline of humanity / the cost of losing curiosity and effort")],
    [S("Warm-Up", [SA("A symbol is…", "an object representing an idea"), SA("Where are the matches found?", "the museum (Palace of Green Porcelain)")], cols=2),
     S("Analyze", [OR("Choose two symbols. Explain how each develops a theme, with evidence from Chapters 11–12.", "Answers vary.", lines=6)]),
     S("Exit Ticket", [OR("Which symbol do you find most powerful? Why?", "Answers vary.", lines=2)])],
    te("Students analyze symbolism.", "Determine theme; analyze word choice.", "The Time Machine Reader (Chapters 11–12), workbook Lesson 6.13",
       "Ruined museum.", "Read Chapters 11–12.", ["Model the chart."], "Your Turn 1–3.",
       ["Symbols without evidence."], ["Symbol → evidence → theme chart."], ["Design a symbol for a story about your community."]),
    summary="Symbols develop the novel's warning.")

L14 = Lesson("6.14", "Sentence Variety",
    "I can vary sentence beginnings, lengths, and types to improve flow and emphasis.", "L.7.3, W.7.5",
    [],
    "What happens when every sentence starts with “The”?",
    [rules([["Strategy", "Example"], ["begin with a prepositional phrase", "In the dark forest, the Traveller lit a fire."], ["begin with a participial phrase", "Clutching Weena's hand, he ran."], ["begin with an adverb", "Suddenly, the Morlocks appeared."],
            ["begin with a dependent clause", "When the fire spread, chaos followed."], ["mix lengths", "Long build-up sentences, then a short one. Like this."], ["mix types", "simple, compound, complex, compound-complex"]], (2.2, 3.4), fs=9),
     KeyIdea("Vary beginnings, lengths, and types; use short sentences for emphasis.")],
    [Problem("Vary the start: The Traveller ran through the forest.", "e.g. Through the forest, the Traveller ran."), Problem("Strategy: Suddenly, the fire roared.", "begin with an adverb"), Problem("Why vary sentences?", "better flow, less monotony, more emphasis")],
    [S("Warm-Up", [SA("A sentence opener type", "prepositional phrase, adverb, clause"), SA("Short sentences give…", "emphasis")], cols=2),
     S("Revise for Variety", [OR("Rewrite with varied beginnings and lengths: The Traveller entered the museum. The Traveller found books. The books were rotting. The Traveller felt sad. The Traveller found matches. The Traveller was happy.",
                                 "e.g. Inside the museum, the Traveller found shelves of rotting books, a sight that saddened him. Then, in a sealed case, he discovered matches. He laughed with relief.", lines=5)]),
     S("Exit Ticket", [OR("Rewrite a paragraph from your science-fiction scene (Unit 5) with at least three sentence-opener types.", "Answers vary.", lines=4)])],
    te("Students vary sentences.", "Vary sentence patterns for meaning, reader interest, and style.", "Workbook Lesson 6.14",
       "All “The” starts.", "Review the chart.", ["Model revision."], "Your Turn 1–3.",
       ["Varying randomly without purpose."], ["Opener checklist."], ["Count openers in a published passage."]),
    summary="Vary beginnings, lengths, and types.")

L15 = Lesson("6.15", "Parallel Structure",
    "I can use parallel structure in lists, comparisons, and paired ideas.", "L.7.1, L.7.3",
    [("parallel structure", "Using the same grammatical form for items in a list or pair.")],
    "What sounds wrong in “The Eloi liked singing, to dance, and they played”?",
    [rules([["Not parallel", "Parallel"], ["The Eloi liked singing, to dance, and they played.", "The Eloi liked singing, dancing, and playing."], ["He was tired, hungry, and feeling afraid.", "He was tired, hungry, and afraid."],
            ["Not only did he lose the machine but also Weena.", "He lost not only the machine but also Weena."], ["The Morlocks worked underground, and the Eloi were living above.", "The Morlocks worked underground, and the Eloi lived above."]], (2.8, 2.8), fs=9),
     KeyIdea("Match forms in lists, pairs, and correlative constructions: nouns with nouns, -ing with -ing, clauses with clauses.")],
    [Problem("Make parallel: to read, writing, and to explore", "to read, to write, and to explore"), Problem("Make parallel: He wanted fame, money, and to be respected.", "He wanted fame, money, and respect."), Problem("Why use parallel structure?", "clarity, rhythm, emphasis")],
    [S("Warm-Up", [SA("Parallel means…", "same grammatical form"), SA("Fix: running, swimming, to bike", "running, swimming, biking")], cols=2),
     S("Make It Parallel", [SA(q, a) for q, a in [("The Traveller was curious, brave, and had intelligence.", "The Traveller was curious, brave, and intelligent."), ("Weena liked flowers, the sunlight, and to laugh.", "Weena liked flowers, sunlight, and laughter."),
                                                  ("Either he finds the machine or staying forever.", "Either he finds the machine or he stays forever."), ("The Morlocks were pale, they were silent, and moving quickly.", "The Morlocks were pale, silent, and quick.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence with three parallel verbs describing the fire in the forest.", "e.g. The fire crackled, roared, and raced through the trees.", lines=2)])],
    te("Students use parallel structure.", "Use language for effect; demonstrate command of grammar.", "Workbook Lesson 6.15",
       "Singing, to dance…", "Find parallel structure in a famous speech.", ["Teach the chart."], "Your Turn 1–3.",
       ["Mixed forms in lists."], ["Line up list items vertically."], ["Write a parallel-structure poem."]),
    summary="Match grammatical forms in lists and pairs.")

L16 = Lesson("6.16", "Revising an Analytical Essay",
    "I can write and revise an analytical essay using varied, clear, and parallel sentences.", "W.7.2, W.7.5, L.7.3",
    [],
    "What is The Time Machine warning us about?",
    [Text("Write an analytical essay: <i>What warning does Wells give through the Eloi and the Morlocks?</i> Then revise using this unit's sentence skills."),
     Figure(lambda t: table(t, [["Revision checklist", "✓"], ["Thesis states the warning clearly.", ""], ["Body paragraphs integrate evidence from Chapters 5–12.", ""], ["Sentences vary in beginnings, lengths, and types.", ""],
                                ["Choppy sentences are combined; over-combined sentences are split.", ""], ["Lists and pairs use parallel structure.", ""], ["No dangling participles; phrases are punctuated correctly.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Revise sentences for variety, clarity, and parallelism after the ideas are solid.")],
    [Problem("What should the thesis state?", "the warning Wells gives"), Problem("Name a sentence revision strategy.", "combine, split, vary openers, parallel structure"), Problem("When do you revise sentences?", "after the ideas and evidence are solid")],
    [S("Warm-Up", [SA("Wells's warning concerns…", "class inequality / loss of effort and curiosity"), SA("Parallel fix: to learn, growing", "to learn, to grow")], cols=2),
     S("Write and Revise", [OR("Draft a 4–5 paragraph analytical essay on Wells's warning.", "Answers vary.", lines=26, note="Score: thesis (1); evidence and analysis (2); sentence variety and parallelism (1); conventions (1)."),
                            OR("List three sentence-level revisions you made.", "Answers vary.", lines=3)])],
    te("Students write and revise analytical essays.", "Write informative texts; strengthen writing by revising.", "Workbook Lesson 6.16, Unit 6 Review",
       "The warning.", "Review Chapters 5–12 evidence.", ["Model a thesis and a revised paragraph."], "Draft and revise.",
       ["Revising only words, not sentences."], ["Sentence checklist."], ["Publish in the portfolio."], independent="Draft and revise; then the Unit 6 Review.", exit_="Tomorrow: Unit 6 Test."),
    summary="Strong ideas, then varied, clear, parallel sentences.")

# ================================================================= checks
C1 = Check("Weekly Check 16: Clauses and Sentence Types", [S("Read and answer", [
    SA("Type: The Traveller walked through the ruined city.", "simple"), SA("Type: Flowers grew everywhere, and the air was warm.", "compound"),
    SA("Type: Although the buildings were enormous, they were crumbling.", "complex"), SA("Dependent clause in sentence 3", "Although the buildings were enormous"),
    SA("Type: The Eloi laughed and played in the gardens, but they never seemed to work.", "compound"), SA("Rewrite sentence 1 as complex.", "e.g. As the sun rose, the Traveller walked through the ruined city."),
    OR("Write a compound-complex sentence about the Eloi.", "Answers vary.", lines=2)], cols=1, passage=P_C16)], minutes=20)
C2 = Check("Weekly Check 17: Phrases", [S("Read and answer", [
    SA("Participial phrase in sentence 1", "Hoping to find the lost city"), SA("Infinitive phrase inside it", "to find the lost city"), SA("Participial phrase in sentence 2", "Carrying heavy packs and sharp machetes"),
    SA("Gerund phrase in sentence 3", "Finding the city"), SA("Function of that gerund phrase", "subject"), SA("Infinitive phrase in sentence 4 and its function", "to photograph every wall carved with ancient symbols; direct object"),
    SA("Participial phrase in sentence 4", "carved with ancient symbols")], cols=1, passage=P_C17)], minutes=20)
C3 = Check("Weekly Check 18: Combining and Variety", [S("Revise the choppy draft", [
    OR("Combine the first three sentences into one.", "The Traveller walked through the dusty old museum.", lines=2),
    OR("Combine sentences 4–6 using a participial phrase or parallel structure.", "He found matches and a lever, which he used as a weapon. / Finding matches and a lever, he used the lever as a weapon.", lines=2),
    OR("Combine the last two sentences with a relative clause.", "Weena, who was afraid of the dark, was with him.", lines=2),
    OR("Rewrite the whole draft as 3–4 varied sentences.", "e.g. Inside the dusty old museum, the Traveller found matches and an iron lever, which he could use as a weapon. Beside him, Weena trembled; she was terrified of the dark.", lines=4)], cols=1, passage=P_C18)], minutes=20)

REVIEW = Check("Unit 6 Review", [
    S("Grammar", [SA("Clause that can stand alone", "independent"), SA("Type: When it rained, we stayed inside.", "complex"), SA("Phrase acting as a noun ending in -ing", "gerund"), SA("Fix: Running to the sphinx, the doors opened.", "As he ran to the sphinx, the doors opened."),
                  SA("Parallel: He liked reading, to write, and art.", "He liked reading, writing, and drawing."), SA("Combine: The Eloi were gentle. They were helpless.", "The Eloi were gentle but helpless.")], cols=1),
    S("Reading", [OR("Explain the Eloi and Morlocks as social commentary.", "They reflect Victorian class division: idle rich above, workers below; extreme inequality endangers everyone.", lines=3)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 6 Test", [
    S("Part A · Reading (1 point each)", [
        OR("What is the purpose of the Svalbard Global Seed Vault?", "to store backup seeds so food crops can survive disasters", lines=2),
        OR("Why was Svalbard chosen? Give two reasons.", "remote, politically stable, geologically quiet; permafrost keeps seeds cold", lines=2),
        OR("Why was the 2015 withdrawal significant?", "It was the first use and proved the vault's purpose after war damaged a seed bank near Aleppo.", lines=2),
        OR("Explain the metaphor “an insurance policy for the future of farming.”", "It protects against future loss, like insurance protects against disaster.", lines=2)], passage=P_TEST),
    S("Part B · Sentences and clauses (1 point each)", [
        SA("Type: “Opened in 2008, the vault stores backup copies of seeds from seed banks around the world.”", "simple (with a participial phrase)"),
        SA("Type of the sentence beginning “Because crops can be lost…”", "complex"), SA("Dependent clause in that sentence", "Because crops can be lost to war, disease, or natural disaster"),
        SA("Type: “The vault can hold about 4.5 million seed samples, and it already holds more than one million.”", "compound"), SA("Find a participial phrase in paragraph 1 or 2.", "Opened in 2008")], cols=1),
    S("Part C · Phrases, combining, parallelism (1 point each)", [
        SA("Find an appositive or adjective clause in paragraph 1.", "which some people call a “doomsday vault”"), SA("Is “remote, politically stable, and geologically quiet” parallel? Explain.", "Yes; all adjectives"),
        SA("Combine: The vault is cold. It is dark. It is inside a mountain.", "The cold, dark vault is inside a mountain."), SA("Fix: Stored in the vault, scientists protect the seeds.", "Scientists protect the seeds stored in the vault."),
        SA("Make parallel: The vault protects seeds from war, disease, and when disasters happen.", "…from war, disease, and natural disaster.")], cols=1),
    S("Part D · Writing (5 points)", [OR("Write a paragraph (7–9 sentences) explaining why the seed vault matters. Use at least one simple, compound, complex, and compound-complex sentence, a participial phrase, and parallel structure.",
                                         "Rubric: clear explanation with evidence (1); four sentence types (2); participial phrase correctly placed (1); parallel structure and conventions (1).", lines=16, points=5)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-03-29", "2027-04-05", "2027-04-12", "2027-04-19"], CHECKS, REVIEW, TEST)

UNIT = Unit(6, "Sentence Craft", "Clauses and sentence types, phrases, combining, variety, parallelism, and analytical writing, with The Time Machine, Chapters 5–12.",
    "In the year 802,701, the Time Traveller discovers that a beautiful world hides a terrible secret. As you follow him into the darkness, you'll master the building blocks of strong sentences: clauses, phrases, and the four sentence types. You'll combine and vary sentences for clarity and power, and write an essay about Wells's warning to the future.",
    ["Analyze utopia, dystopia, allegory, and symbolism.", "Identify clauses and write all four sentence types.", "Identify and use prepositional, appositive, participial, gerund, and infinitive phrases.",
     "Combine sentences precisely; vary sentences; use parallel structure; revise an analytical essay."],
    [("RL.7.1–4, RL.7.6, RI.7.2", "Cite evidence; theme; analyze elements, word choice, point of view."), ("L.7.1a–c, L.7.3a", "Phrases, clauses, sentence types; misplaced modifiers; precise language."),
     ("W.7.2, W.7.5", "Write and revise analytical essays.")],
    [("independent clause", "Can stand alone."), ("dependent clause", "Cannot stand alone."), ("gerund", "An -ing verb used as a noun."), ("allegory", "A story representing larger ideas."), ("parallel structure", "Same grammatical form in a series.")],
    ["Unit 5: modifiers and parts of speech."], ["The Time Machine Reader (Chapters 5–12)"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Writers, lawyers, and leaders use sentence variety and parallelism to make arguments memorable, and dystopian stories still shape debates about technology and fairness.",
    family_note="Ask your student: If Wells visited today, what warning might he write about our world?",
    weeks=WEEKS)
