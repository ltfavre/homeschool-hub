"""Grade 7 ELA · Unit 2: Long Passages and the Power of Nouns — analyzing long passages and scenes, comparing text and performance, noun forms and functions, and the literary analysis essay.
Anchor reading: The Tempest Reader, Acts 3–5 (Nov 9 – Dec 11, 2026)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule
from content.ela7.unit01 import TEMPEST

# ================================================================= passages
P_ISLE = Passage("Caliban's Speech, Act 3, Scene 2 (original text, excerpt)", [
    "> Be not afeard; the isle is full of noises,\\nSounds and sweet airs, that give delight and hurt not.",
], source="William Shakespeare, The Tempest. Public domain.", genre="Speech from a play", numbered=False)

P_REVELS = Passage("Prospero's Speech, Act 4, Scene 1 (original text, excerpt)", [
    "> Our revels now are ended. These our actors,\\nAs I foretold you, were all spirits and\\nAre melted into air, into thin air:",
    "> …We are such stuff\\nAs dreams are made on, and our little life\\nIs rounded with a sleep.",
], source="William Shakespeare, The Tempest. Public domain.", genre="Speech from a play", numbered=False)

P_VIRTUE = Passage("Prospero, Act 5, Scene 1 (original text, excerpt)", [
    "> …the rarer action is\\nIn virtue than in vengeance.",
], source="William Shakespeare, The Tempest. Public domain.", genre="Speech from a play", numbered=False)

P_MAGIC = Passage("Magic and Science in Shakespeare's England", [
    "To modern readers, Prospero's magic seems like pure fantasy. To Shakespeare's audience, the line between magic and science was far less clear. In the late 1500s and early 1600s, the same scholars who studied mathematics, astronomy, and navigation often also studied astrology and alchemy, the attempt to transform ordinary metals into gold.",
    "One of the most famous of these scholars was John Dee, an adviser to Queen Elizabeth I. Dee owned one of the largest libraries in England, with thousands of books and manuscripts. He helped English sailors improve their navigation and was respected for his knowledge of geometry. Yet he also tried to communicate with spirits using a polished black mirror and a crystal.",
    "Many people admired such learned men; others feared them. Laws punished those accused of witchcraft, and a scholar's interest in hidden knowledge could make neighbors suspicious. A magician who used his learning for good was a hero to some audiences and a dangerous figure to others.",
    "Prospero reflects this mixed view. He is a scholar who loved his books so much that he neglected his duties as Duke of Milan, which gave his brother the chance to seize power. On the island, his learning becomes power. At the end of the play, he promises to break his staff and drown his book, giving up magic before returning to ordinary life.",
    "Some audiences in Shakespeare's time may have seen this as a wise decision: true power, the play suggests, means knowing when to let it go.",
], source="An original informational text", genre="Informational text")

P_STAGING = Passage("Two Ways to Stage the Storm", [
    "<b>Production A.</b> The curtain rises on a nearly bare stage. Actors sway together on a tilting wooden platform while a single blue light flickers. Thunder is played on a large metal sheet shaken offstage. The audience must imagine the ship and the sea.",
    "<b>Production B.</b> A full-size ship's deck fills the stage. Real water sprays from hidden pipes, wind machines roar, and projections show enormous waves crashing over the rail. The actors shout over the noise, sometimes so loudly that individual lines are lost.",
], source="Original descriptions", genre="Informational text", numbered=False)

P_C4 = Passage("The Long Way Home", [
    "Rain had turned the forest trail into a river of mud by the time Jonah realized he was lost. His phone had no signal, and the map he'd printed was a soggy lump in his pocket.",
    "He forced himself to stop and breathe. His grandfather's voice came back to him: <i>When you're lost, the first thing to find is your head.</i> Jonah looked around. Moss grew thickest on the north side of the trees. The stream he'd crossed an hour ago had been flowing east. Camp was east of the stream.",
    "Jonah followed the water downhill, slipping and grabbing branches. Twice he wanted to sit down and wait for someone to find him. Twice he kept going.",
    "When the orange glow of the campfire finally appeared through the trees, his legs were shaking. His scout leader rushed over, worry on her face. Jonah grinned through the mud. “I found my head first,” he said.",
], source="An original story", genre="Realistic fiction")

P_C5 = Passage("The Masks of Venice", [
    "For centuries, the people of Venice, Italy, have celebrated Carnival, a festival held before the season of Lent. The most famous symbol of Carnival is the mask.",
    "Masks allowed Venetians to hide their identities. A wealthy merchant and a poor servant might stand side by side, and no one could tell them apart. For a few weeks, the strict rules about class seemed to disappear.",
    "Today, mask makers in Venice still craft masks from papier-mâché, paint, and gold leaf. Tourists from around the world buy them, keeping an old tradition alive in a modern city.",
], source="An original informational text", genre="Informational text")

P_C6 = Passage("The Captain's Choice", [
    "Captain Ruiz, the commander of the rescue team, studied the storm on her screen. The crew of the fishing boat, six exhausted men, had been drifting for two days. Her helicopter, an old but reliable machine, had enough fuel for one attempt.",
    "Her co-pilot, Lieutenant Park, gave her a worried look. Courage, she knew, was not the absence of fear. It was a decision. She gave the order to fly.",
], source="An original story", genre="Realistic fiction")

P_TEST = Passage("The Bridge Builders", [
    "In 1869, the engineer John Roebling began designing a bridge to connect the cities of Brooklyn and New York across the East River. At the time, it would be the longest suspension bridge in the world. Many experts said it could not be done.",
    "Only weeks into the project, Roebling's foot was crushed in an accident at the docks, and he died of an infection. His son, Washington Roebling, took over. Washington spent long hours in the caissons, huge underwater chambers where workers dug the foundations. There, many workers developed a mysterious illness, now called decompression sickness, caused by returning too quickly from the high-pressure air below. In 1872, Washington himself became so ill that he could no longer visit the site.",
    "That was when his wife, Emily Warren Roebling, stepped forward. From their apartment window, Washington watched the construction through a telescope. Emily carried his instructions to the engineers, but she did far more than deliver messages. She studied mathematics, the strength of materials, and cable construction. For over a decade, she managed communication with officials and engineers, and many came to rely on her knowledge.",
    "When the Brooklyn Bridge opened on May 24, 1883, Emily Roebling was the first person to ride across it. A plaque on the bridge today honors the three Roeblings, a reminder that the bridge was the work of a family's determination as much as an engineer's design.",
], source="An original informational text based on historical facts", genre="Informational text")

# ================================================================= Week 1 · Long-passage evidence and inference (Act 3)
L1 = Lesson("2.1", "Tracking Multiple Plotlines",
    "I can track several plotlines and explain how they connect.", "RL.7.3, RL.7.5",
    [("plotline", "A sequence of events involving one group of characters."), ("subplot", "A secondary plotline that supports or mirrors the main plot.")],
    "How many different stories are happening on Prospero's island at once?",
    [ReaderAssign(TEMPEST, "Act 3", "Follow each group: Ferdinand and Miranda; Caliban, Stephano, and Trinculo; and the nobles."),
     Text("<i>The Tempest</i> moves among several groups of characters. Each <b>plotline</b> develops separately, but they mirror and connect to one another."),
     Figure(lambda t: table(t, [["Plotline", "Characters", "What happens in Act 3", "Connection"], ["Romance", "Ferdinand, Miranda", "They declare their love; Prospero watches approvingly", "Prospero arranges a future for Miranda"],
                                ["Comic plot", "Caliban, Stephano, Trinculo", "Caliban urges them to kill Prospero", "mirrors Antonio's plot to seize power"], ["Nobles' plot", "Alonso, Antonio, Sebastian, Gonzalo", "Ariel appears as a harpy and accuses the “three men of sin”", "Prospero begins his judgment"]],
                            [1.0 * inch, 1.4 * inch, 1.8 * inch, 1.5 * inch], width=5.7 * inch, font_size=8.5)),
     KeyIdea("Track each plotline separately, then ask how they mirror or connect to each other.")],
    [Problem("What is a subplot?", "a secondary plotline that supports or mirrors the main plot"), Problem("How does Caliban's plot mirror Antonio's?", "Both plot to kill a ruler and take power."), Problem("Who is controlling all three plotlines?", "Prospero (with Ariel)")],
    [S("Warm-Up", [SA("Plotline =", "events for one group of characters"), SA("Name two romance characters", "Ferdinand and Miranda")], cols=2),
     S("Track the Plotlines", [OR("Summarize what happens in each plotline in Act 3.", "Romance: Ferdinand and Miranda pledge love. Comic: Caliban, Stephano, Trinculo plot to kill Prospero. Nobles: Ariel as a harpy accuses Alonso, Antonio, Sebastian.", lines=6),
                               OR("Explain how the comic plot comments on the nobles' plot.", "It repeats the power grab in a foolish, drunken form, making the nobles' ambition look ridiculous.", lines=4)]),
     S("Exit Ticket", [OR("Which plotline interests you most? Why?", "Answers vary.", lines=2)])],
    te("Students track multiple plotlines.", "Analyze how elements of a drama interact; analyze how a scene fits into the overall structure.", "The Tempest Reader (Act 3), workbook Lesson 2.1",
       "How many stories?", "Read Act 3.", ["Model the plotline chart."], "Your Turn 1–3.",
       ["Confusing which characters are where."], ["Color-code plotlines."], ["Draw a map of where each group is on the island."]),
    summary="Track plotlines separately; analyze how they mirror each other.")

L2 = Lesson("2.2", "Close Reading a Speech",
    "I can analyze a speech closely for word choice, imagery, and what it reveals about a character.", "RL.7.4, RL.7.1",
    [("imagery", "Language that appeals to the senses."), ("close reading", "Careful, repeated reading of a short passage to analyze its meaning and craft.")],
    "Who in the play would you expect to describe the island as beautiful?",
    [P_ISLE,
     Text("Surprisingly, it is Caliban, the character Prospero calls a monster, who speaks some of the most beautiful lines about the island. Close reading asks: <i>What does it say? How does it say it? Why does it matter?</i>"),
     Example("Close read", "“Be not afeard; the isle is full of noises, / Sounds and sweet airs, that give delight and hurt not.”",
             ["What: Caliban reassures Stephano and Trinculo that the island's sounds are harmless.", "How: sound imagery; gentle words (sweet, delight); verse rhythm.", "Why: it reveals Caliban's deep sensitivity and connection to his home."],
             "Caliban's lyrical speech complicates the idea that he is merely a monster; he loves and understands the island."),
     KeyIdea("What does it say? How does it say it? Why does it matter for character or theme?")],
    [Problem("What does “afeard” mean?", "afraid"), Problem("What sense does the speech appeal to?", "hearing"), Problem("Why is it surprising that Caliban says this?", "Others call him a monster, yet he speaks with beauty and tenderness.")],
    [S("Warm-Up", [SA("Imagery appeals to…", "the senses"), SA("“airs” here means…", "melodies, songs")], cols=2),
     S("Close Read", [OR("What do these two lines reveal about Caliban's relationship with the island?", "He knows it intimately and loves it; it soothes him.", lines=3),
                      OR("How does this speech change how readers might see Caliban?", "It makes him more sympathetic and human; challenges Prospero's view.", lines=3)], passage=P_ISLE),
     S("Your Own Close Read", [OR("Choose four to six lines from Act 3. Answer: What? How? Why?", "Answers vary.", lines=6)])],
    te("Students close read a speech.", "Determine meanings, including figurative and connotative; analyze impact of word choice.", "Workbook Lesson 2.2",
       "Who would say it?", "Read Caliban's lines aloud several times.", ["Model What/How/Why."], "Your Turn 1–3.",
       ["Paraphrasing without analyzing craft."], ["Three-column close reading chart."], ["Memorize and perform Caliban's lines."]),
    summary="Close reading: what, how, why.")

L3 = Lesson("2.3", "Inference Across a Long Informational Text",
    "I can make and support inferences across a long informational text.", "RI.7.1, RI.7.3",
    [("alchemy", "An early practice that tried to turn ordinary metals into gold."), ("adviser", "A person who gives advice to a leader.")],
    "Why might some people in 1610 have feared a man who read too many books?",
    [P_MAGIC,
     Example("Infer across paragraphs", "What can you infer about how audiences might have viewed Prospero?",
             ["Paragraph 1: magic and science overlapped.", "Paragraph 3: learned men were admired and feared.", "Paragraph 4: Prospero is a scholar whose learning becomes power."],
             "Audiences may have both admired Prospero's knowledge and been uneasy about his power."),
     KeyIdea("Connect details from several paragraphs to draw well-supported inferences.")],
    [Problem("Who was John Dee?", "a scholar and adviser to Queen Elizabeth I"), Problem("How did Prospero's love of books cost him?", "He neglected his duties, letting Antonio seize power."), Problem("What does Prospero promise at the end?", "to break his staff and drown his book")],
    [S("Warm-Up", [SA("Alchemy tried to…", "turn metals into gold"), SA("Dee advised…", "Queen Elizabeth I")], cols=2),
     S("Infer with Evidence", [OR("Infer why the author includes John Dee. Cite two details.", "to show a real person who combined science and magic, like Prospero: navigation and geometry, but spirits and a black mirror", lines=4),
                               OR("What can you infer about why Prospero gives up his magic? Use the text and the play.", "He knows power must be let go to return to ordinary life and rule wisely; the text says true power means knowing when to let go.", lines=4),
                               MC("Which sentence best states a central idea?", ["John Dee owned many books.", "In Shakespeare's time, learned magicians like Prospero were viewed with both admiration and fear.", "Alchemy is not real."], 1)], passage=P_MAGIC),
     S("Exit Ticket", [OR("Do you think Prospero is admirable or dangerous? Use one detail from the article and one from the play.", "Answers vary.", lines=3)])],
    te("Students infer across long informational texts.", "Cite evidence for inferences; analyze interactions between individuals, events, and ideas.", "Workbook Lesson 2.3",
       "Feared readers.", "Read “Magic and Science.”", ["Model a cross-paragraph inference."], "Your Turn 1–3.",
       ["Inferences from one sentence."], ["Paragraph-linking chart."], ["Research John Dee."]),
    summary="Connect several paragraphs for strong inferences.")

L4 = Lesson("2.4", "Writing a Multi-Paragraph Evidence Response",
    "I can write a multi-paragraph response that integrates evidence from a long text.", "W.7.9a, W.7.2",
    [("integrate", "Weave quotations smoothly into your own sentences.")],
    "How can you include a quotation so it sounds like part of your own sentence?",
    [Text("Integrate quotations instead of dropping them in. Use a lead-in, a short quote, and analysis."),
     Figure(lambda t: table(t, [["Dropped quote (weak)", "Integrated quote (strong)"], ["Caliban speaks. “The isle is full of noises.” This is beautiful.", "When Caliban reassures his companions that “the isle is full of noises,” his gentle tone reveals how deeply he loves his home."]],
                            [2.8 * inch, 2.8 * inch], width=5.6 * inch)),
     Example("Response structure", "Prompt: How does Shakespeare complicate the audience's view of Caliban in Act 3?",
             ["Paragraph 1: claim: Caliban is both brutal and sensitive.", "Paragraph 2: brutal: he urges Stephano to kill Prospero (evidence + analysis).", "Paragraph 3: sensitive: his speech about the isle (evidence + analysis).", "Short conclusion."],
             "A three- or four-paragraph response with integrated evidence."),
     KeyIdea("Lead-in + short quote + analysis. Organize paragraphs by idea.")],
    [Problem("What is a lead-in?", "words that introduce a quotation and its context"), Problem("Why keep quotes short?", "to focus on key words and leave room for analysis"), Problem("What follows a quote?", "analysis")],
    [S("Warm-Up", [SA("Integrated quotes need a…", "lead-in"), SA("After the quote, add…", "analysis")], cols=2),
     S("Integrate", [OR("Rewrite as an integrated quotation: Prospero is angry. “Thou shalt be pinched / As thick as honeycomb.”", "e.g. Prospero's anger shows when he threatens that Caliban “shalt be pinched / As thick as honeycomb.”", lines=2)]),
     S("Write", [OR("Prompt: How does Shakespeare complicate the audience's view of Caliban? Write a three- or four-paragraph response with at least two integrated quotations.", "Answers vary.", lines=22,
                    note="Score: claim (1); paragraph with integrated evidence and analysis (2); second paragraph (2); conclusion and conventions (1).")])],
    te("Students write multi-paragraph evidence responses.", "Draw evidence from literary texts; write informative texts with relevant quotations.", "Workbook Lesson 2.4",
       "Quote that sounds like yours.", "Gather Caliban evidence.", ["Model integration."], "Plan together.",
       ["Dropped quotes.", "Quotes without analysis."], ["Lead-in starters."], ["Add a counterclaim paragraph."], independent="Write the response. Weekly Check tomorrow."),
    summary="Integrate quotations with lead-ins and analysis.")

# ================================================================= Week 2 · Long-passage analysis (Act 4)
L5 = Lesson("2.5", "How a Scene Contributes to the Whole",
    "I can analyze how a scene contributes to a drama's structure, theme, and characters.", "RL.7.5",
    [("masque", "An elaborate performance with music, dance, and spectacle, popular in royal courts."), ("structure", "How a text is organized into parts.")],
    "Why would Prospero stop his own story to stage a show?",
    [ReaderAssign(TEMPEST, "Act 4", "Why does Prospero create the masque for Ferdinand and Miranda? Why does he end it so suddenly?"),
     Text("Each scene has a job: advancing plot, developing character, building theme, or shifting mood. Ask: <i>What would be lost if this scene were removed?</i>"),
     Example("Analyze the masque", "What does the masque contribute?", ["Plot: celebrates Ferdinand and Miranda's engagement.", "Theme: shows Prospero's power to create illusions (appearance vs reality).", "Character: Prospero breaks it off when he remembers Caliban's plot, revealing his anxiety and anger."],
             "The masque celebrates the future, displays illusion, and reveals Prospero's troubled mind."),
     KeyIdea("Ask what a scene contributes to plot, character, theme, and mood, and what would be lost without it.")],
    [Problem("What is a masque?", "an elaborate performance with music, dance, and spectacle"), Problem("Why does Prospero end the masque suddenly?", "He remembers Caliban's plot against him."), Problem("Which theme does the masque reflect?", "appearance vs reality / illusion")],
    [S("Warm-Up", [SA("A masque includes…", "music, dance, spectacle"), SA("Whose engagement is celebrated?", "Ferdinand and Miranda's")], cols=2),
     S("Analyze", [OR("What would be lost if Act 4 were removed? Name two things.", "Celebration of the romance; the theme of illusion; Prospero's anxiety and the revels speech.", lines=4),
                   OR("How does Act 4 prepare for Act 5?", "Prospero deals with Caliban's plot and reflects on illusion, preparing to give up magic and confront his enemies.", lines=3)]),
     S("Exit Ticket", [OR("In one sentence, state the main job of Act 4.", "Answers vary.", lines=2)])],
    te("Students analyze a scene's contribution.", "Analyze how a drama's form or structure contributes to its meaning.", "The Tempest Reader (Act 4), workbook Lesson 2.5",
       "Pause for a show?", "Read Act 4.", ["Model the analysis."], "Your Turn 1–3.",
       ["Summarizing the scene instead of analyzing purpose."], ["What-would-be-lost test."], ["Analyze another scene's job."]),
    summary="Scenes advance plot, develop character, build theme, and shift mood.")

L6 = Lesson("2.6", "Analyzing a Famous Speech",
    "I can analyze how figurative language and structure create meaning in a famous speech.", "RL.7.4, RL.7.2",
    [],
    "Have you ever felt that something wonderful was over too quickly, like a dream?",
    [P_REVELS,
     Example("Analyze", "“We are such stuff / As dreams are made on, and our little life / Is rounded with a sleep.”",
             ["Metaphor: human beings are made of the same material as dreams; life is brief and unreal.", "“Rounded with a sleep”: life is surrounded or completed by sleep, suggesting death.", "Connection: the vanished masque becomes a symbol for all of life."],
             "Prospero turns the end of a show into a reflection on how brief life is."),
     KeyIdea("Identify the figurative language, explain it, then connect it to the play's larger meaning.")],
    [Problem("What were the “actors” in the masque?", "spirits"), Problem("What does “melted into air” suggest?", "They vanished completely; illusions disappear."), Problem("What is the speech's larger message?", "Life is brief and dreamlike.")],
    [S("Warm-Up", [SA("revels =", "celebrations, entertainment"), SA("foretold =", "told before")], cols=2),
     S("Analyze the Speech", [OR("Explain the comparison in “We are such stuff / As dreams are made on.”", "People are like dreams: temporary and not as solid as they seem.", lines=3),
                              OR("How does the ending of the masque lead Prospero to think about life itself?", "Just as the spirits vanished, all of life will end; it's a reflection on mortality.", lines=3),
                              OR("How does this speech connect to Prospero's decision to give up magic?", "He recognizes power and illusion are temporary; he prepares to let go.", lines=3)], passage=P_REVELS),
     S("Exit Ticket", [OR("Rewrite the last three lines in modern English.", "We are made of the same stuff as dreams, and our short lives end in sleep.", lines=2)])],
    te("Students analyze a famous speech.", "Determine figurative meanings; analyze theme.", "Workbook Lesson 2.6",
       "Dream ending.", "Read the speech aloud slowly.", ["Model the analysis."], "Your Turn 1–3.",
       ["Literal reading (people are literally dreams)."], ["Paraphrase first."], ["Find this speech quoted in modern culture."]),
    summary="Figurative language in a speech can express the play's biggest ideas.")

L7 = Lesson("2.7", "Comparing Text and Performance",
    "I can compare a written drama to a staged or filmed version and analyze the effects of the director's choices.", "RL.7.7",
    [("director", "The person who decides how a play is staged or filmed."), ("production", "A particular staging or film of a play.")],
    "If you staged The Tempest's opening storm, how would you make the audience feel it?",
    [Text("Directors make choices about sets, lighting, sound, costumes, and acting. Each choice changes how the audience experiences the text."),
     P_STAGING,
     Example("Analyze choices", "Compare Productions A and B.", ["A: simple; relies on actors and imagination; lines are clear.", "B: spectacular; overwhelming effects; some lines lost.", "Effect: A emphasizes words and imagination; B emphasizes the storm's terror."],
             "Each production highlights different parts of the scene."),
     KeyIdea("Compare what the text says with what the production shows; analyze the effect of each choice.")],
    [Problem("Which production is closer to Shakespeare's Globe?", "A (little scenery)"), Problem("What is lost in Production B?", "some lines are hard to hear"), Problem("What is gained in Production B?", "a powerful, realistic sense of danger")],
    [S("Warm-Up", [SA("A director decides…", "how a play is staged"), SA("A production is…", "a particular staging")], cols=2),
     S("Compare", [OR("Which production would you rather see? Explain using effects on the audience.", "Answers vary.", lines=3),
                   OR("Watch a short clip of a Tempest production (with a parent). Compare one choice to the text.", "Answers vary.", lines=4)], passage=P_STAGING),
     S("Design", [DRAW("Sketch your own stage design for the masque in Act 4. Label lighting, sound, and costume choices.", "Answers vary.", space=170)])],
    te("Students compare text and performance.", "Compare a written drama to its staged or filmed version, analyzing the effects of techniques unique to each medium.", "Workbook Lesson 2.7, a short production clip (optional)",
       "Staging the storm.", "Read the two productions.", ["Model the comparison."], "Your Turn 1–3.",
       ["Judging productions by preference only."], ["Effect-on-audience frame."], ["Design a full set."]),
    summary="Productions make choices that change the audience's experience.")

L8 = Lesson("2.8", "Writing a Scene Analysis",
    "I can write an analysis of how a scene contributes to a drama.", "W.7.9a, W.7.2",
    [],
    "What is the single most important thing Act 4 does?",
    [Text("A scene analysis states the scene's purpose (claim), supports it with integrated evidence, and explains its effect on the play as a whole."),
     Example("Topic sentence", "Act 4", ["Name the scene.", "State its contribution."], "In Act 4, Shakespeare uses the masque to celebrate the future while reminding the audience how fragile and fleeting every illusion, even life itself, can be."),
     KeyIdea("Claim about the scene's purpose → integrated evidence → effect on the whole play.")],
    [Problem("What must the topic sentence name?", "the scene and its contribution"), Problem("What kind of evidence?", "integrated quotations or specific details"), Problem("What does the analysis connect to?", "the play as a whole")],
    [S("Warm-Up", [SA("Integrated quotes need…", "lead-ins and analysis"), SA("Act 4's spectacle is the…", "masque")], cols=2),
     S("Write", [OR("Write a two-paragraph analysis: How does Act 4 contribute to The Tempest's themes?", "Answers vary.", lines=18, note="Score: claim (1); evidence 1 + analysis (1); evidence 2 + analysis (1); connection to whole play (1); conventions (1).")])],
    te("Students write scene analyses.", "Draw evidence; write analytically.", "Workbook Lesson 2.8",
       "Most important thing.", "Reread Act 4 key moments.", ["Model a topic sentence."], "Plan.",
       ["Summary instead of analysis."], ["Purpose statement frame."], ["Compare Act 4 to Act 1."], independent="Write. Weekly Check tomorrow."),
    summary="Analyze a scene's purpose with evidence.")

# ================================================================= Week 3 · Noun forms and functions (Act 5)
L9 = Lesson("2.9", "Kinds of Nouns",
    "I can identify concrete, abstract, collective, compound, and proper nouns.", "L.7.1",
    [("concrete noun", "Names something you can perceive with the senses: island, staff."), ("abstract noun", "Names an idea, quality, or feeling: freedom, revenge."),
     ("collective noun", "Names a group: crew, audience."), ("compound noun", "Made of two or more words: shipwreck, sea-change, mother-in-law.")],
    "Which is easier to draw: “a staff” or “forgiveness”? Why?",
    [ReaderAssign(TEMPEST, "Act 5", "How does Prospero treat his enemies? What does he give up?"),
     Figure(lambda t: table(t, [["Kind", "Examples from The Tempest"], ["concrete", "island, book, staff, ship, storm"], ["abstract", "revenge, forgiveness, freedom, power, love"], ["collective", "crew, court, company"],
                                ["compound", "shipwreck, sea-change, boatswain"], ["proper", "Prospero, Milan, Naples, Ariel"]], [1.4 * inch, 4.0 * inch], width=5.4 * inch)),
     Text("Writers use <b>abstract nouns</b> to name big ideas (themes) and <b>concrete nouns</b> to make those ideas visible. Prospero's <i>staff</i> and <i>book</i> (concrete) stand for his <i>power</i> (abstract)."),
     KeyIdea("Concrete nouns can be sensed; abstract nouns name ideas. Writers use concrete nouns to symbolize abstract ones.")],
    [Problem("Concrete or abstract: forgiveness", "abstract"), Problem("Collective noun for sailors", "crew"), Problem("What abstract idea does Prospero's staff represent?", "power / magic")],
    [S("Warm-Up", [SA("Abstract noun example", "freedom, love"), SA("Collective noun example", "crew, audience")], cols=2),
     S("Classify", [SA(w, a) for w, a in [("vengeance", "abstract"), ("audience", "collective"), ("cliffside", "compound (concrete)"), ("Miranda", "proper"), ("loyalty", "abstract"), ("lantern", "concrete"),
                                          ("flock", "collective"), ("mercy", "abstract")]], cols=2),
     S("Symbols", [OR("Prospero promises to break his staff and drown his book. What abstract ideas do these concrete nouns represent? What does giving them up mean?", "power and magic (knowledge); he gives up control and returns to ordinary life", lines=4)])],
    te("Students classify nouns.", "Demonstrate command of grammar and usage.", "The Tempest Reader (Act 5), workbook Lesson 2.9",
       "Draw a staff vs forgiveness.", "Read Act 5.", ["Teach noun types.", "Concrete as symbol of abstract."], "Your Turn 1–3.",
       ["Calling collective nouns plural."], ["Sorting cards."], ["List abstract nouns that name the play's themes."]),
    summary="Concrete, abstract, collective, compound, and proper nouns.")

L10 = Lesson("2.10", "Noun Functions in Sentences",
    "I can identify how nouns function in sentences: subject, direct object, indirect object, object of a preposition, and predicate noun.", "L.7.1",
    [("direct object", "Receives the action of the verb."), ("indirect object", "Tells to whom or for whom the action is done."), ("predicate noun", "Follows a linking verb and renames the subject.")],
    "In “Prospero gave Ariel freedom,” who receives what?",
    [Figure(lambda t: table(t, [["Function", "Example (function underlined in your mind)"], ["subject", "<b>Prospero</b> freed Ariel."], ["direct object", "Prospero freed <b>Ariel</b>."], ["indirect object", "Prospero gave <b>Ariel</b> his freedom."],
                                ["object of preposition", "Ariel flew over the <b>island</b>."], ["predicate noun", "Prospero is the rightful <b>duke</b>."]], [1.6 * inch, 3.8 * inch], width=5.4 * inch)),
     Example("Identify functions", "“Prospero gave Ariel freedom.”", ["Subject: Prospero (who gave?).", "Direct object: freedom (gave what?).", "Indirect object: Ariel (gave to whom?)."], "Prospero = subject; freedom = direct object; Ariel = indirect object"),
     KeyIdea("Ask who/what does it (subject), receives it (direct object), to/for whom (indirect object), after a preposition (object of preposition), or renames the subject after a linking verb (predicate noun).")],
    [Problem("Function of “Miranda” in “Ferdinand loves Miranda.”", "direct object"), Problem("Function of “king” in “Alonso is the king.”", "predicate noun"), Problem("Function of “shore” in “They walked along the shore.”", "object of preposition")],
    [S("Warm-Up", [SA("Who/what does the action?", "subject"), SA("Receives the action?", "direct object")], cols=2),
     S("Identify the Function of the Bold Noun", [SA(q, a) for q, a in [("<b>Caliban</b> carried wood.", "subject"), ("Caliban carried <b>wood</b>.", "direct object"), ("Prospero told <b>Miranda</b> the story.", "indirect object"),
                                                                       ("Prospero told Miranda the <b>story</b>.", "direct object"), ("The ship sank near the <b>island</b>.", "object of preposition"), ("Ariel is a <b>spirit</b>.", "predicate noun"),
                                                                       ("Gonzalo gave <b>Prospero</b> his books.", "indirect object"), ("Ferdinand became a <b>prisoner</b>.", "predicate noun")]], cols=2),
     S("Exit Ticket", [OR("Write a sentence about Act 5 that contains a subject, direct object, and indirect object. Label them.", "Answers vary.", lines=2)])],
    te("Students identify noun functions.", "Explain the function of words in sentences.", "Workbook Lesson 2.10",
       "Who receives what?", "Pull sentences from Act 5.", ["Teach functions; question method."], "Your Turn 1–3.",
       ["Confusing indirect and direct objects."], ["Ask: gave what? gave to whom?"], ["Diagram sentences."]),
    summary="Nouns function as subjects, objects, and predicate nouns.")

L11 = Lesson("2.11", "Appositives",
    "I can use appositives to add information, punctuating them correctly.", "L.7.1, L.7.2",
    [("appositive", "A noun or noun phrase that renames another noun right beside it.")],
    "How can you tell readers who Ariel is without writing a whole new sentence?",
    [Text("An <b>appositive</b> renames a noun: <i>Ariel, <b>a spirit of the air</b>, serves Prospero.</i> Use commas when the appositive adds extra (nonessential) information. No commas when it is essential to identify which one: <i>Shakespeare's play <b>The Tempest</b> is set on an island.</i>"),
     Example("Combine with an appositive", "Caliban lives on the island. Caliban is the son of the witch Sycorax.", ["Find the renaming phrase: the son of the witch Sycorax.", "Place it beside Caliban with commas."], "Caliban, the son of the witch Sycorax, lives on the island."),
     KeyIdea("Appositives rename nouns. Use commas for extra information.")],
    [Problem("Find the appositive: Gonzalo, an honest old counselor, helped Prospero.", "an honest old counselor"), Problem("Combine: Miranda is Prospero's daughter. Miranda has lived on the island since she was very young.", "Miranda, Prospero's daughter, has lived on the island since she was very young."), Problem("Do appositives that add extra information need commas?", "Yes")],
    [S("Warm-Up", [SA("An appositive…", "renames a noun"), SA("Extra info appositives need…", "commas")], cols=2),
     S("Combine with Appositives", [SA(q, a) for q, a in [("Alonso grieved. Alonso is the King of Naples.", "Alonso, the King of Naples, grieved."), ("Stephano got drunk. Stephano is a butler.", "Stephano, a butler, got drunk."),
                                                          ("The Globe held 3,000 people. The Globe was Shakespeare's theater.", "The Globe, Shakespeare's theater, held 3,000 people."), ("John Dee advised the queen. Dee was a famous scholar.", "John Dee, a famous scholar, advised the queen.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence about a family member using an appositive.", "Answers vary; commas correct.", lines=2)])],
    te("Students use appositives.", "Use punctuation to set off nonrestrictive elements; vary sentences.", "Workbook Lesson 2.11",
       "Who is Ariel?", "Find appositives in the Reader.", ["Teach commas for extra info."], "Your Turn 1–3.",
       ["Missing the second comma."], ["Appositive sandwich: comma–phrase–comma."], ["Revise a paragraph with three appositives."]),
    summary="Appositives rename nouns; commas set off extra information.")

L12 = Lesson("2.12", "Forming Nouns from Other Words",
    "I can form nouns with suffixes and use them to write about ideas.", "L.7.4b, L.7.1",
    [("nominalization", "Turning a verb or adjective into a noun, such as forgive → forgiveness.")],
    "How can you turn the verb “forgive” into a word that names the idea?",
    [Figure(lambda t: table(t, [["Suffix", "Base word", "Noun"], ["-ness", "kind, forgive", "kindness, forgiveness"], ["-tion / -sion", "reconcile, decide", "reconciliation, decision"], ["-ment", "imprison, punish", "imprisonment, punishment"],
                                ["-ity", "loyal, generous", "loyalty, generosity"], ["-ance / -ence", "vengeful (venge)/ obey", "vengeance, obedience"], ["-dom", "free", "freedom"]], [1.4 * inch, 1.8 * inch, 2.2 * inch], width=5.4 * inch)),
     Text("Analytical writing often uses abstract nouns: <i>Prospero chooses <b>forgiveness</b> over <b>vengeance</b>.</i>"),
     KeyIdea("Suffixes turn verbs and adjectives into nouns that name ideas, which are essential for writing about themes.")],
    [Problem("Noun form of <i>free</i>", "freedom"), Problem("Noun form of <i>punish</i>", "punishment"), Problem("Noun form of <i>loyal</i>", "loyalty")],
    [S("Warm-Up", [SA("forgive →", "forgiveness"), SA("decide →", "decision")], cols=2),
     S("Form the Noun", [SA(w, a) for w, a in [("betray", "betrayal"), ("generous", "generosity"), ("obey", "obedience"), ("imprison", "imprisonment"), ("celebrate", "celebration"), ("wise", "wisdom")]], cols=2),
     S("Write About Ideas", [OR("Using at least three abstract nouns, write two sentences about what Prospero chooses in Act 5.", "e.g. Prospero chooses forgiveness over vengeance. His decision brings reconciliation and freedom.", lines=3)], passage=P_VIRTUE),
     S("Exit Ticket", [OR("Explain Prospero's line “the rarer action is / In virtue than in vengeance.”", "It is nobler and less common to forgive than to take revenge.", lines=2)])],
    te("Students form nouns from verbs and adjectives.", "Use affixes; demonstrate command of grammar.", "Workbook Lesson 2.12",
       "forgive → ?", "Read Prospero's line in Act 5.", ["Teach suffix chart."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Spelling changes (obey → obedience)."], ["Dictionary check."], ["List theme nouns for The Tempest."]),
    summary="Suffixes form abstract nouns for writing about ideas.")

# ================================================================= Week 4 · Noun usage and writing application (Act 5 response)
L13 = Lesson("2.13", "Precise Nouns for Vivid Writing",
    "I can replace vague nouns with precise ones.", "L.7.3a, W.7.3d",
    [("vague", "Not clear or specific.")],
    "Which paints a clearer picture: “The person carried a thing” or “The boatswain carried a coil of rope”?",
    [Text("Vague nouns (<i>thing, stuff, person, place</i>) leave readers guessing. Precise nouns create images and save words."),
     Figure(lambda t: table(t, [["Vague", "Precise"], ["a person", "a boatswain, a counselor, a jester"], ["a thing", "a staff, a lantern, a scroll"], ["a place", "a cove, a cave, a cliffside"], ["a feeling", "dread, relief, resentment"]],
                            [1.8 * inch, 3.4 * inch], width=5.2 * inch)),
     KeyIdea("Replace vague nouns with precise nouns that create a clear image or name an exact idea.")],
    [Problem("Precise noun for “a building where grain is kept”", "granary"), Problem("Revise: A person on the ship yelled stuff.", "e.g. The boatswain bellowed orders."), Problem("Precise abstract noun for “feeling bad about what you did”", "guilt, remorse")],
    [S("Warm-Up", [SA("Vague noun example", "thing, stuff, person"), SA("Precise noun for a ship's kitchen", "galley")], cols=2),
     S("Revise", [SA(q, a) for q, a in [("The man held a thing.", "e.g. The magician held a carved staff."), ("They went to a place by the water.", "e.g. They hid in a cove by the sea."),
                                        ("She felt a feeling of being glad it was over.", "e.g. She felt relief."), ("The people watched the show.", "e.g. The courtiers watched the masque.")]], cols=1),
     S("Exit Ticket", [OR("Find a sentence in your Act 4 analysis with a vague noun. Revise it.", "Answers vary.", lines=2)])],
    te("Students use precise nouns.", "Choose language that expresses ideas precisely, eliminating wordiness.", "Workbook Lesson 2.13",
       "Person and thing.", "Find precise nouns in the Reader.", ["Model revisions."], "Your Turn 1–3.",
       ["Replacing with fancy but wrong words."], ["Thesaurus plus dictionary check."], ["Revise a past essay paragraph."]),
    summary="Precise nouns create clear images and ideas.")

L14 = Lesson("2.14", "Possessive Nouns and Clear Reference",
    "I can form possessives correctly, including plural, irregular, and joint possession.", "L.7.2, L.7.1",
    [("joint possession", "Two or more people owning the same thing: Ferdinand and Miranda's chessboard.")],
    "Is it “Prospero's and Miranda's cave” or “Prospero and Miranda's cave”?",
    [Figure(lambda t: table(t, [["Rule", "Example"], ["singular: 's", "the duke's book; Prospero's staff"], ["singular ending in s: 's (usually)", "Gonzalo's kindness; James's book"], ["plural ending in s: '", "the sailors' ship"],
                                ["irregular plural: 's", "the men's swords; the children's toys"], ["joint possession: 's on the last name only", "Ferdinand and Miranda's chessboard"], ["separate possession: 's on each name", "Antonio's and Sebastian's swords"]],
                            [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     KeyIdea("Choose the possessive form by number (singular/plural), regularity, and whether ownership is joint or separate.")],
    [Problem("The cave shared by Prospero and Miranda", "Prospero and Miranda's cave"), Problem("The separate swords of Antonio and Sebastian", "Antonio's and Sebastian's swords"), Problem("The ship belonging to the sailors", "the sailors' ship")],
    [S("Warm-Up", [SA("Possessive of the plural sailors", "sailors'"), SA("Possessive of men", "men's")], cols=2),
     S("Write the Possessive", [SA(q, a) for q, a in [("the island of Caliban", "Caliban's island"), ("the songs of the spirits", "the spirits' songs"), ("the courage of the women", "the women's courage"),
                                                      ("the kingdom shared by Alonso and Ferdinand", "Alonso and Ferdinand's kingdom"), ("the separate books of Prospero and Gonzalo", "Prospero's and Gonzalo's books"), ("the plan of Stephano", "Stephano's plan")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence with joint possession and one with separate possession.", "Answers vary.", lines=2)])],
    te("Students form possessives correctly.", "Demonstrate command of capitalization, punctuation, and spelling.", "Workbook Lesson 2.14",
       "Whose cave?", "Find possessives in Act 5.", ["Teach the chart."], "Your Turn 1–3.",
       ["Joint vs separate confusion."], ["Ask: one thing or two?"], ["Proofread a past essay for possessives."]),
    summary="Possessives depend on number, regularity, and joint or separate ownership.")

L15 = Lesson("2.15", "Writing a Literary Analysis Essay",
    "I can write a literary analysis essay about a theme in a drama.", "W.7.2, W.7.9a",
    [("thesis", "The central claim of an essay.")],
    "Is The Tempest a story about revenge or about forgiveness?",
    [P_VIRTUE,
     Text("A literary analysis essay has an <b>introduction</b> (hook, context, thesis), <b>body paragraphs</b> (topic sentence, integrated evidence, analysis), and a <b>conclusion</b> (restated thesis and significance)."),
     Example("Thesis", "Prompt: What does The Tempest suggest about revenge and forgiveness?", ["Take a position.", "Preview reasons."],
             "Although Prospero spends the play controlling his enemies, The Tempest ultimately suggests that forgiveness, not vengeance, is the truer form of power."),
     KeyIdea("Thesis → body paragraphs with integrated evidence and analysis → conclusion with significance.")],
    [Problem("What three parts are in an introduction?", "hook, context, thesis"), Problem("What does a conclusion add besides restating?", "significance: why it matters"), Problem("Name a key quote for forgiveness.", "“the rarer action is / In virtue than in vengeance”")],
    [S("Warm-Up", [SA("Thesis =", "the central claim"), SA("Body paragraph starts with a…", "topic sentence")], cols=2),
     S("Plan", [OR("Thesis:", "Answers vary.", lines=2), OR("Body 1 topic + evidence:", "Answers vary.", lines=3), OR("Body 2 topic + evidence:", "Answers vary.", lines=3)]),
     S("Draft", [OR("Draft your literary analysis essay.", "Answers vary.", lines=22, note="Look for: thesis; two body paragraphs with integrated evidence and analysis; conclusion with significance.")])],
    te("Students write literary analysis essays.", "Write informative/explanatory texts analyzing literature; draw evidence.", "Workbook Lesson 2.15",
       "Revenge or forgiveness?", "Reread Act 5's resolution.", ["Model a thesis and introduction."], "Plan and draft.",
       ["Thesis that only summarizes."], ["Thesis frame: Although…, …suggests…"], ["Add a counterargument paragraph."], independent="Draft the essay."),
    summary="Literary analysis: thesis, evidence, analysis, significance.")

L16 = Lesson("2.16", "Revising the Essay for Precision",
    "I can revise my essay for precise nouns, integrated evidence, and correct conventions.", "W.7.5, L.7.3a",
    [],
    "What one change would make your essay most convincing?",
    [Figure(lambda t: table(t, [["Revision checklist", "✓"], ["Thesis takes a clear position.", ""], ["Each quotation is integrated with a lead-in and analysis.", ""], ["Vague nouns are replaced with precise ones.", ""],
                                ["Appositives add useful information with correct commas.", ""], ["Possessives are correct.", ""], ["Conclusion explains significance.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Revise for argument and evidence first, then precision and conventions.")],
    [Problem("What should you revise first?", "argument and evidence"), Problem("Name a convention to check.", "possessives, commas with appositives"), Problem("Why replace vague nouns?", "to make ideas precise and vivid")],
    [S("Warm-Up", [SA("Appositive commas", "before and after"), SA("A vague noun", "thing")], cols=2),
     S("Revise", [OR("List three revisions you made using the checklist.", "Answers vary.", lines=4), OR("Copy your revised thesis.", "Answers vary.", lines=2)])],
    te("Students revise essays.", "Develop and strengthen writing by revising and editing.", "Drafts, workbook Lesson 2.16, Unit 2 Review",
       "One change.", "Read drafts aloud.", ["Model checklist use."], "Revise.",
       ["Only proofreading."], ["One checklist item at a time."], ["Publish the essay in the portfolio."], independent="Revise; then the Unit 2 Review.", exit_="Tomorrow: Unit 2 Test."),
    summary="Revise argument and evidence, then precision and conventions.")

# ================================================================= checks
C1 = Check("Weekly Check 4: Long-Passage Evidence and Inference", [S("Read and answer", [
    OR("What does Jonah's grandfather's advice mean?", "Stay calm and think clearly before acting.", lines=2),
    OR("Cite two pieces of evidence that Jonah uses reason, not panic.", "He stops and breathes; uses moss and the stream's direction to find camp.", lines=3),
    OR("What can you infer about the scout leader's feelings? Evidence?", "She was worried and relieved; she rushed over with worry on her face.", lines=2),
    OR("Explain how the last line connects to the beginning.", "“I found my head first” echoes his grandfather's advice, showing he followed it.", lines=2)], passage=P_C4)], minutes=20)
C2 = Check("Weekly Check 5: Analysis and Central Ideas", [S("Read and answer", [
    OR("State two central ideas of the passage.", "Masks hid identity and erased class differences during Carnival; the mask tradition continues today.", lines=3),
    OR("Explain how paragraph 2 develops the first central idea.", "A merchant and servant couldn't be told apart, so class rules seemed to disappear.", lines=2),
    OR("Connect this passage to the theme of appearance vs reality in The Tempest.", "Both show disguises and illusions hiding who people really are.", lines=3),
    MC("Which is an objective summary sentence?", ["Venetian masks are the most beautiful art in the world.", "Venetian masks let people of different classes celebrate Carnival without revealing their identities.", "Tourists waste money on masks."], 1)], passage=P_C5)], minutes=20)
C3 = Check("Weekly Check 6: Nouns", [S("Read and answer", [
    SA("Find two appositives.", "the commander of the rescue team; an old but reliable machine (also: six exhausted men)"), SA("Abstract noun in paragraph 2", "courage / fear / absence / decision"),
    SA("Collective noun in paragraph 1", "crew / team"), SA("Function of <i>order</i> in “She gave the order”", "direct object"),
    SA("Function of <i>decision</i> in “It was a decision”", "predicate noun"), SA("Possessive: the boat of the fishermen", "the fishermen's boat"),
    SA("Noun form of <i>brave</i>", "bravery"), SA("Replace the vague noun: She looked at the thing on the screen.", "e.g. She studied the radar map on the screen.")], cols=1, passage=P_C6)], minutes=20)

REVIEW = Check("Unit 2 Review", [
    S("Reading", [SA("A subplot…", "supports or mirrors the main plot"), SA("Close reading asks…", "what, how, why"), SA("A masque is…", "an elaborate performance with music and dance"),
                  SA("RL.7.7 compares text and…", "performance")], cols=2),
    S("Nouns", [SA("Concrete or abstract: mercy", "abstract"), SA("Function: Ariel sang <b>Ferdinand</b> a song.", "indirect object"), SA("Add an appositive: Gonzalo helped Prospero.", "e.g. Gonzalo, a loyal counselor, helped Prospero."),
                SA("Joint possession: Stephano and Trinculo / plan", "Stephano and Trinculo's plan"), SA("Noun form of <i>reconcile</i>", "reconciliation")], cols=1)],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 2 Test", [
    S("Part A · Evidence and inference (1 point each)", [
        OR("Why did many experts doubt the bridge could be built?", "It would be the longest suspension bridge in the world; it seemed impossible.", lines=2),
        OR("What caused the workers' “mysterious illness”?", "returning too quickly from the high-pressure air in the caissons", lines=2),
        OR("Cite two pieces of evidence that Emily Roebling did more than carry messages.", "She studied math, materials, and cable construction; she managed communication; engineers relied on her knowledge.", lines=3, points=2),
        OR("Infer why the author ends with the plaque. What idea does it emphasize?", "The bridge was a shared family achievement; it honors determination as well as design.", lines=2)], passage=P_TEST),
    S("Part B · Central ideas and analysis (1 point each)", [
        OR("State two central ideas of the passage.", "Building the bridge was dangerous and difficult; the Roebling family, especially Emily, persevered to complete it.", lines=3),
        OR("How does paragraph 3 develop the second central idea?", "It shows Emily stepping forward, studying, and managing the project when Washington was ill.", lines=2),
        OR("Write an objective summary (3 sentences).", "John Roebling designed the Brooklyn Bridge but died after an accident. His son Washington continued until illness kept him from the site. His wife Emily studied engineering and managed the project until the bridge opened in 1883.", lines=4, points=2)]),
    S("Part C · Nouns (1 point each)", [
        SA("Find an appositive in paragraph 2.", "huge underwater chambers where workers dug the foundations"), SA("Abstract noun in the last paragraph", "determination"),
        SA("Function of <i>bridge</i> in “Roebling began designing a bridge”", "direct object (of designing)"), SA("Possessive: the knowledge of Emily", "Emily's knowledge"),
        SA("Joint possession: the apartment of Washington and Emily", "Washington and Emily's apartment")], cols=1),
    S("Part D · Analytical writing (5 points)", [OR("Write a two-paragraph analysis: How does the author present Emily Warren Roebling as essential to the bridge's success? Integrate at least two quotations or specific details.",
                                                   "Rubric: thesis (1); integrated evidence with analysis, paragraph 1 (1); paragraph 2 (1); precise word choice (1); conventions (1).", lines=16, points=5)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-11-09", "2026-11-16", "2026-11-30", "2026-12-07"], CHECKS, REVIEW, TEST)

UNIT = Unit(2, "Long Passages and the Power of Nouns", "Multiple plotlines, close reading, scene analysis, text vs performance, noun forms and functions, and the literary analysis essay, with The Tempest, Acts 3–5.",
    "As Prospero's plan reaches its climax, you'll analyze long passages and famous speeches, see how each scene fits the whole play, and compare the written play with performances. You'll also master nouns, the words that name everything from a magician's staff to forgiveness itself, and write a full literary analysis essay.",
    ["Track plotlines; close read speeches; analyze how scenes contribute to the whole.", "Infer across long informational texts; compare text and performance.",
     "Identify kinds and functions of nouns; use appositives and possessives correctly.", "Write multi-paragraph responses and a literary analysis essay with integrated evidence."],
    [("RL.7.1–5, RL.7.7", "Cite evidence; analyze theme, elements, word choice, structure; compare text and performance."), ("RI.7.1–3", "Infer and analyze central ideas and interactions."),
     ("L.7.1–3", "Grammar, punctuation, precise language."), ("W.7.2, W.7.5, W.7.9", "Write and revise analytical essays.")],
    [("subplot", "A secondary plotline."), ("close reading", "Careful analysis of a short passage."), ("abstract noun", "Names an idea."), ("appositive", "Renames a noun."), ("thesis", "An essay's central claim.")],
    ["Unit 1 skills."], ["The Tempest Reader (Acts 3–5)", "Optional: a filmed or staged production clip"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Integrating evidence, analyzing a scene's purpose, and choosing precise words are the same skills used in reviews, reports, and persuasive writing.",
    family_note="Ask your student which character in The Tempest deserves forgiveness most, and why.",
    weeks=WEEKS)
