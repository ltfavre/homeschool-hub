"""Grade 7 ELA · Unit 2: Long Passages and the Power of Nouns — analyzing long passages and scenes, comparing text and performance, noun forms and functions, and the literary analysis essay.
Anchor reading: A Christmas Carol (Grade 7 Reader), Stave Three (second section) through Stave Five."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule
from content.ela7.unit01 import CAROL

# ================================================================= passages
P_WANT = Passage("The Ghost of Christmas Present, Stave Three (original text, excerpt)", [
    "“They are Man’s,” said the Spirit, looking down upon them. “And they cling to me, appealing from their fathers. This boy is Ignorance. This girl is Want. Beware them both, and all of their degree, but most of all beware this boy, for on his brow I see that written which is Doom, unless the writing be erased.”",
    "“Have they no refuge or resource?” cried Scrooge.",
    "“Are there no prisons?” said the Spirit, turning on him for the last time with his own words. “Are there no workhouses?”",
], source="Charles Dickens, A Christmas Carol. Public domain.", genre="Novella excerpt", numbered=False)

P_COURSES = Passage("Scrooge, Stave Four (original text, excerpt)", [
    "“Men’s courses will foreshadow certain ends, to which, if persevered in, they must lead,” said Scrooge. “But if the courses be departed from, the ends will change. Say it is thus with what you show me!”",
    "“Spirit!” he cried, tight clutching at its robe, “hear me! I am not the man I was. I will not be the man I must have been but for this intercourse. Why show me this, if I am past all hope!”",
], source="Charles Dickens, A Christmas Carol. Public domain.", genre="Novella excerpt", numbered=False)

P_HONOUR = Passage("Scrooge's Promise, Stave Four (original text, excerpt)", [
    "“I will honour Christmas in my heart, and try to keep it all the year. I will live in the Past, the Present, and the Future. The Spirits of all Three shall strive within me. I will not shut out the lessons that they teach.”",
], source="Charles Dickens, A Christmas Carol. Public domain.", genre="Novella excerpt", numbered=False)

P_RAGGED = Passage("Ignorance and Want in 1843", [
    "When the Ghost of Christmas Present reveals two starving children named Ignorance and Want, Dickens was not inventing a fantasy. In 1843, thousands of children in London never went to school. Many worked from the age of six or seven, sweeping chimneys, selling matches, or sorting rags. Others had no work and no home at all.",
    "Some reformers tried to help. Volunteers opened <b>ragged schools</b>, so called because the children who came were dressed in rags. The schools were free and met in whatever rooms could be found, often in the poorest streets. Teachers taught reading, writing, arithmetic, and religion, and some schools gave out bread and clothing.",
    "Dickens visited one of these schools in September 1843. He wrote to a wealthy friend, Angela Burdett-Coutts, who gave large sums to charity, describing the crowded room and the children's hunger, and asking her to support the school. He believed that a child who was never taught anything would grow up with no choices except crime or the workhouse.",
    "Not everyone agreed. Many comfortable people argued that the poor would only become idle if they were helped, and that prisons and workhouses were enough. Dickens put those very words in Scrooge's mouth, and then had the Ghost throw them back at him.",
    "Over the next decades, Britain slowly changed. Laws limited children's working hours, and in 1870 Parliament began creating schools for every child. Dickens did not live to see all of these changes, but his story helped persuade a generation of readers that the poor were not a “surplus population” but neighbors.",
], source="An original informational text based on historical facts", genre="Informational text")

P_STAGING = Passage("Two Ways to Stage the Last Spirit", [
    "<b>Production A.</b> The stage goes dark except for one cold spotlight. An actor on hidden stilts, wrapped in a tall black robe and hood, glides slowly toward Scrooge without a sound. The Spirit never speaks; it only points. The audience hears nothing but Scrooge's breathing.",
    "<b>Production B.</b> A film version fills the screen with swirling black shadow. Deep, booming music swells, the Spirit's huge shape looms over the rooftops of London, and computer effects send Scrooge flying through the streets. The scenes move quickly, and some of Scrooge's lines are cut.",
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

# ================================================================= Week 1 · Long-passage evidence and inference (Stave Three, second section)
L1 = Lesson("2.1", "Tracking Multiple Plotlines",
    "I can track several plotlines and explain how they connect.", "RL.7.3, RL.7.5",
    [("plotline", "A sequence of events involving one group of characters."), ("subplot", "A secondary plotline that supports or mirrors the main plot.")],
    "How many different Christmases does the Ghost of Christmas Present show Scrooge?",
    [ReaderAssign(CAROL, "Stave Three (second section)", "Follow each group the Spirit shows Scrooge: the miners, the lighthouse keepers, the sailors, Fred's party, and the two children under the Spirit's robe."),
     Text("<i>A Christmas Carol</i> follows Scrooge, but the Spirits also show him other people's stories. Each <b>plotline</b> develops separately, but they mirror Scrooge's story and connect to it."),
     Figure(lambda t: table(t, [["Plotline", "Characters", "What happens in Stave Three", "Connection"], ["The Cratchits", "Bob, Mrs. Cratchit, Tiny Tim, and the children", "a joyful dinner; Tiny Tim is ill; Bob toasts Scrooge", "Scrooge learns that his clerk's son may die"],
                                ["Fred's party", "Fred, his wife, and their guests", "games, music, and a toast to “Uncle Scrooge”", "the family Scrooge refused still welcomes him"], ["Strangers", "miners, lighthouse keepers, sailors", "people in lonely, hard places still keep Christmas", "shows that joy does not depend on money"]],
                            [1.0 * inch, 1.4 * inch, 1.8 * inch, 1.5 * inch], width=5.7 * inch, font_size=8.5)),
     KeyIdea("Track each plotline separately, then ask how it mirrors or connects to the main character's story.")],
    [Problem("What is a subplot?", "a secondary plotline that supports or mirrors the main plot"), Problem("What game does Fred's party play about Scrooge?", "Yes and No"), Problem("Who is guiding Scrooge through all of these scenes?", "the Ghost of Christmas Present")],
    [S("Warm-Up", [SA("Plotline =", "events for one group of characters"), SA("Name two of the Cratchit children", "Tiny Tim, Martha, Belinda, Peter")], cols=2),
     S("Track the Plotlines", [OR("Summarize what happens in two of the plotlines in Stave Three.", "Answers vary; e.g. The Cratchits share a small, joyful dinner, but Tiny Tim may die. Fred's guests laugh at Scrooge in a game, yet Fred toasts him and plans to keep inviting him.", lines=6),
                               OR("Explain how the miners and the lighthouse keepers comment on Scrooge's life.", "They have almost nothing and live in harsh places, yet they celebrate together, while rich Scrooge spends Christmas alone and unhappy.", lines=4)]),
     S("Exit Ticket", [OR("Which plotline do you think affects Scrooge most? Why?", "Answers vary.", lines=2)])],
    te("Students track multiple plotlines.", "Analyze how elements of a story interact; analyze how a section fits into the overall structure.", "Grade 7 Reader: A Christmas Carol (Stave Three, second section), workbook Lesson 2.1",
       "How many Christmases?", "Read the second section of Stave Three.", ["Model the plotline chart."], "Your Turn 1–3.",
       ["Losing track of where Scrooge is."], ["Color-code plotlines."], ["Map every place the Spirit takes Scrooge."]),
    summary="Track plotlines separately; analyze how they mirror the main story.")

L2 = Lesson("2.2", "Close Reading a Speech",
    "I can analyze a speech closely for word choice, imagery, and what it reveals about a character.", "RL.7.4, RL.7.1",
    [("symbol", "A person, object, or event that stands for a larger idea."), ("close reading", "Careful, repeated reading of a short passage to analyze its meaning and craft.")],
    "Why would Dickens give two starving children the names Ignorance and Want?",
    [P_WANT,
     Text("At the end of Stave Three, the Ghost reveals two children hiding under his robe. Close reading asks: <i>What does it say? How does it say it? Why does it matter?</i>"),
     Example("Close read", "“This boy is Ignorance. This girl is Want. Beware them both… but most of all beware this boy.”",
             ["What: the Spirit names the children as symbols of society's problems.", "How: short, blunt sentences; warning words (beware, Doom).", "Why: the children belong to all of “Man,” so everyone, including Scrooge, is responsible for them."],
             "The Ghost turns two children into symbols to warn that ignoring poverty and lack of education will bring disaster."),
     KeyIdea("What does it say? How does it say it? Why does it matter for character or theme?")],
    [Problem("What does “Want” mean here?", "need; poverty; lack of food and care"), Problem("Why must Scrooge “most of all beware this boy”?", "Ignorance (lack of education) leads to the worst harm, or Doom."), Problem("Whose words does the Spirit repeat?", "Scrooge's own: “Are there no prisons? Are there no workhouses?”")],
    [S("Warm-Up", [SA("A symbol stands for…", "a larger idea"), SA("Ignorance means…", "lack of knowledge or education")], cols=2),
     S("Close Read", [OR("Why does the Spirit say the children are “Man’s” and not his own?", "They belong to all of humanity; society created them and is responsible for them.", lines=3),
                      OR("How does repeating Scrooge's own words make the moment more powerful?", "It forces Scrooge to hear how cruel his words sound when applied to real, suffering children.", lines=3)], passage=P_WANT),
     S("Your Own Close Read", [OR("Choose four to six sentences from Stave Three. Answer: What? How? Why?", "Answers vary.", lines=6)])],
    te("Students close read a speech.", "Determine meanings, including figurative and connotative; analyze impact of word choice.", "Workbook Lesson 2.2",
       "Why those names?", "Read the Spirit's words aloud several times.", ["Model What/How/Why."], "Your Turn 1–3.",
       ["Paraphrasing without analyzing craft."], ["Three-column close reading chart."], ["Memorize and perform the Spirit's speech."]),
    summary="Close reading: what, how, why.")

L3 = Lesson("2.3", "Inference Across a Long Informational Text",
    "I can make and support inferences across a long informational text.", "RI.7.1, RI.7.3",
    [("reformer", "A person who works to improve society."), ("ragged school", "A free school for the poorest children in Victorian Britain.")],
    "Why might some people in 1843 have opposed helping poor children?",
    [P_RAGGED,
     Example("Infer across paragraphs", "What can you infer about why Dickens included Ignorance and Want in his story?",
             ["Paragraph 1: many real children had no school and no home.", "Paragraph 3: Dickens had just seen a ragged school and believed uneducated children had no future.", "Paragraph 4: he used his story to answer people who refused to help."],
             "Dickens included the two children to make readers face a real problem he had seen himself."),
     KeyIdea("Connect details from several paragraphs to draw well-supported inferences.")],
    [Problem("Why were ragged schools given that name?", "The children who attended were dressed in rags."), Problem("Who was Angela Burdett-Coutts?", "a wealthy friend of Dickens who gave to charity"), Problem("What happened in 1870?", "Parliament began creating schools for every child.")],
    [S("Warm-Up", [SA("A reformer…", "works to improve society"), SA("Dickens visited a ragged school in…", "September 1843")], cols=2),
     S("Infer with Evidence", [OR("Infer why the author includes the letter to Angela Burdett-Coutts. Cite two details.", "To show Dickens acted, not just wrote: he described the children's hunger and asked her to support the school.", lines=4),
                               OR("What can you infer about why the Spirit warns most of all against Ignorance? Use the text and the story.", "Dickens believed a child who was never educated would have no choices except crime or the workhouse, so ignorance does the deepest harm.", lines=4),
                               MC("Which sentence best states a central idea?", ["Ragged schools met in small rooms.", "Dickens drew on the real suffering of uneducated, poor children to challenge readers to help them.", "Parliament passed a law in 1870."], 1)], passage=P_RAGGED),
     S("Exit Ticket", [OR("Do you think Dickens's story could change readers' minds more than a report could? Use one detail from the article and one from the story.", "Answers vary.", lines=3)])],
    te("Students infer across long informational texts.", "Cite evidence for inferences; analyze interactions between individuals, events, and ideas.", "Workbook Lesson 2.3",
       "Opposing help.", "Read “Ignorance and Want in 1843.”", ["Model a cross-paragraph inference."], "Your Turn 1–3.",
       ["Inferences from one sentence."], ["Paragraph-linking chart."], ["Research the ragged schools."]),
    summary="Connect several paragraphs for strong inferences.")

L4 = Lesson("2.4", "Writing a Multi-Paragraph Evidence Response",
    "I can write a multi-paragraph response that integrates evidence from a long text.", "W.7.9a, W.7.2",
    [("integrate", "Weave quotations smoothly into your own sentences.")],
    "How can you include a quotation so it sounds like part of your own sentence?",
    [Text("Integrate quotations instead of dropping them in. Use a lead-in, a short quote, and analysis."),
     Figure(lambda t: table(t, [["Dropped quote (weak)", "Integrated quote (strong)"], ["The Spirit is angry. “Are there no prisons?” This is Scrooge's line.", "When the Spirit asks, “Are there no prisons?”, he throws Scrooge's own cruel words back at him, forcing Scrooge to hear how they sound."]],
                            [2.8 * inch, 2.8 * inch], width=5.6 * inch)),
     Example("Response structure", "Prompt: How does the Ghost of Christmas Present change the way Scrooge sees the poor?",
             ["Paragraph 1: claim: the Ghost shows Scrooge that the poor are real people, not a “surplus population.”", "Paragraph 2: the Cratchits and Tiny Tim (evidence + analysis).", "Paragraph 3: Ignorance and Want (evidence + analysis).", "Short conclusion."],
             "A three- or four-paragraph response with integrated evidence."),
     KeyIdea("Lead-in + short quote + analysis. Organize paragraphs by idea.")],
    [Problem("What is a lead-in?", "words that introduce a quotation and its context"), Problem("Why keep quotes short?", "to focus on key words and leave room for analysis"), Problem("What follows a quote?", "analysis")],
    [S("Warm-Up", [SA("Integrated quotes need a…", "lead-in"), SA("After the quote, add…", "analysis")], cols=2),
     S("Integrate", [OR("Rewrite as an integrated quotation: Scrooge is upset. “Oh, no, kind Spirit! say he will be spared.”", "e.g. Scrooge's concern for Tiny Tim shows when he begs, “Oh, no, kind Spirit! say he will be spared.”", lines=2)]),
     S("Write", [OR("Prompt: How does the Ghost of Christmas Present change the way Scrooge sees the poor? Write a three- or four-paragraph response with at least two integrated quotations.", "Answers vary.", lines=22,
                    note="Score: claim (1); paragraph with integrated evidence and analysis (2); second paragraph (2); conclusion and conventions (1).")])],
    te("Students write multi-paragraph evidence responses.", "Draw evidence from literary texts; write informative texts with relevant quotations.", "Workbook Lesson 2.4",
       "Quote that sounds like yours.", "Gather evidence from Stave Three.", ["Model integration."], "Plan together.",
       ["Dropped quotes.", "Quotes without analysis."], ["Lead-in starters."], ["Add a counterclaim paragraph."], independent="Write the response. Weekly Check tomorrow."),
    summary="Integrate quotations with lead-ins and analysis.")

# ================================================================= Week 2 · Long-passage analysis (Stave Four)
L5 = Lesson("2.5", "How a Scene Contributes to the Whole",
    "I can analyze how a scene contributes to a story's structure, theme, and characters.", "RL.7.5",
    [("suspense", "A feeling of tense uncertainty about what will happen."), ("structure", "How a text is organized into parts.")],
    "Why would Dickens show strangers selling a dead man's belongings?",
    [ReaderAssign(CAROL, "Stave Four", "Who is the dead man? How do people react to his death? What does Scrooge beg the Spirit at the end?"),
     Text("Each scene has a job: advancing plot, developing character, building theme, or creating mood and suspense. Ask: <i>What would be lost if this scene were removed?</i>"),
     Example("Analyze the scene at old Joe's shop", "What does it contribute?", ["Plot: shows how the dead man is treated once he is gone.", "Theme: no one mourns him; his greed left him with no one who cared.", "Suspense: readers suspect who the man is long before Scrooge admits it."],
             "The shop scene shows the lonely end of a greedy life and builds suspense about the dead man's name."),
     KeyIdea("Ask what a scene contributes to plot, character, theme, and mood, and what would be lost without it.")],
    [Problem("What is suspense?", "a feeling of tense uncertainty about what will happen"), Problem("What do the visitors bring to old Joe?", "things they took from the dead man, even his bed-curtains"), Problem("Which theme does the scene reflect?", "greed leaves a person alone and unmourned")],
    [S("Warm-Up", [SA("Suspense means…", "tense uncertainty"), SA("The last Spirit never…", "speaks")], cols=2),
     S("Analyze", [OR("What would be lost if the shop scene were removed? Name two things.", "the proof that no one mourns the dead man; the dark mood; suspense about his identity", lines=4),
                   OR("How does Stave Four prepare for Stave Five?", "Scrooge sees his own grave and begs for a chance to change, so readers are ready to see whether he will.", lines=3)]),
     S("Exit Ticket", [OR("In one sentence, state the main job of Stave Four.", "Answers vary.", lines=2)])],
    te("Students analyze a scene's contribution.", "Analyze how a text's form or structure contributes to its meaning.", "Grade 7 Reader: A Christmas Carol (Stave Four), workbook Lesson 2.5",
       "A dead man's belongings?", "Read Stave Four.", ["Model the analysis."], "Your Turn 1–3.",
       ["Summarizing the scene instead of analyzing purpose."], ["What-would-be-lost test."], ["Analyze another scene's job."]),
    summary="Scenes advance plot, develop character, build theme, and create suspense.")

L6 = Lesson("2.6", "Analyzing a Famous Speech",
    "I can analyze how figurative language and structure create meaning in a famous speech.", "RL.7.4, RL.7.2",
    [],
    "Can the future be changed, or is it already written?",
    [P_COURSES,
     Example("Analyze", "“Men’s courses will foreshadow certain ends, to which, if persevered in, they must lead. But if the courses be departed from, the ends will change.”",
             ["Metaphor: a person's life is a course, or path, that leads to an end, or destination.", "Structure: two balanced sentences, the second turning on “But.”", "Connection: Scrooge argues that the future the Spirit shows can still change if he changes his path."],
             "Scrooge turns the image of a path into an argument for hope: change the road, and you change where it ends."),
     KeyIdea("Identify the figurative language, explain it, then connect it to the story's larger meaning.")],
    [Problem("What does “courses” mean here?", "paths; the ways people live their lives"), Problem("What does “I am not the man I was” show?", "Scrooge has already begun to change."), Problem("What is the speech's larger message?", "The future is not fixed; people can change.")],
    [S("Warm-Up", [SA("foreshadow =", "hint at what will happen"), SA("persevered in =", "continued")], cols=2),
     S("Analyze the Speech", [OR("Explain the comparison of a life to a course or path.", "Our choices lead us somewhere, as a road leads to a place; a different road leads somewhere else.", lines=3),
                              OR("Why does Scrooge ask this question before looking at the gravestone?", "He is afraid of what it says and wants to know whether he can still change his fate.", lines=3),
                              OR("How does this speech connect to Marley's warning in Stave One?", "Marley said Scrooge still had “a chance and hope” of escaping his fate; Scrooge now begs for that chance.", lines=3)], passage=P_COURSES),
     S("Exit Ticket", [OR("Rewrite Scrooge's first sentence in modern English.", "The way people live leads to certain endings, but if they change how they live, the endings will change.", lines=2)])],
    te("Students analyze a famous speech.", "Determine figurative meanings; analyze theme.", "Workbook Lesson 2.6",
       "Can the future change?", "Read the speech aloud slowly.", ["Model the analysis."], "Your Turn 1–3.",
       ["Literal reading (a course is a race track)."], ["Paraphrase first."], ["Find a modern speech that uses the image of a path."]),
    summary="Figurative language in a speech can express the story's biggest ideas.")

L7 = Lesson("2.7", "Comparing Text and Performance",
    "I can compare a written story to a staged or filmed version and analyze the effects of the director's choices.", "RL.7.7",
    [("director", "The person who decides how a story is staged or filmed."), ("adaptation", "A version of a story changed for a new medium, such as a play or film.")],
    "If you staged the arrival of the last, silent Spirit, how would you make the audience feel Scrooge's fear?",
    [Text("<i>A Christmas Carol</i> has been adapted for the stage and screen hundreds of times; Dickens even performed it himself. Directors make choices about sets, lighting, sound, costumes, and acting. Each choice changes how the audience experiences the text."),
     P_STAGING,
     Example("Analyze choices", "Compare Productions A and B.", ["A: silent and simple; relies on the actor and the audience's imagination.", "B: spectacular; overwhelming effects; some lines lost.", "Effect: A makes the Spirit eerie and close; B makes it huge and terrifying."],
             "Each production highlights different parts of the scene."),
     KeyIdea("Compare what the text says with what the production shows; analyze the effect of each choice.")],
    [Problem("Which production is closer to Dickens's description of a silent Spirit?", "A"), Problem("What is lost in Production B?", "some of Scrooge's lines"), Problem("What is gained in Production B?", "a powerful sense of size and terror")],
    [S("Warm-Up", [SA("A director decides…", "how a story is staged or filmed"), SA("An adaptation is…", "a version for a new medium")], cols=2),
     S("Compare", [OR("Which production would you rather see? Explain using effects on the audience.", "Answers vary.", lines=3),
                   OR("Watch a short clip of a stage or film version of A Christmas Carol (with a parent). Compare one choice to the text.", "Answers vary.", lines=4)], passage=P_STAGING),
     S("Design", [DRAW("Sketch your own stage design for Marley's Ghost entering Scrooge's room. Label lighting, sound, and costume choices.", "Answers vary.", space=170)])],
    te("Students compare text and performance.", "Compare a written story to its staged or filmed version, analyzing the effects of techniques unique to each medium.", "Workbook Lesson 2.7, a short production clip (optional)",
       "Staging the last Spirit.", "Read the two productions.", ["Model the comparison."], "Your Turn 1–3.",
       ["Judging productions by preference only."], ["Effect-on-audience frame."], ["Design a full set."]),
    summary="Productions make choices that change the audience's experience.")

L8 = Lesson("2.8", "Writing a Scene Analysis",
    "I can write an analysis of how a scene contributes to a story.", "W.7.9a, W.7.2",
    [],
    "What is the single most important thing Stave Four does?",
    [Text("A scene analysis states the scene's purpose (claim), supports it with integrated evidence, and explains its effect on the story as a whole."),
     Example("Topic sentence", "Stave Four", ["Name the scene.", "State its contribution."], "In Stave Four, Dickens shows the lonely, unmourned death of a greedy man so that Scrooge, and the reader, can see where his path is leading while there is still time to change it."),
     KeyIdea("Claim about the scene's purpose → integrated evidence → effect on the whole story.")],
    [Problem("What must the topic sentence name?", "the scene and its contribution"), Problem("What kind of evidence?", "integrated quotations or specific details"), Problem("What does the analysis connect to?", "the story as a whole")],
    [S("Warm-Up", [SA("Integrated quotes need…", "lead-ins and analysis"), SA("The last Spirit is the Ghost of Christmas…", "Yet to Come")], cols=2),
     S("Write", [OR("Write a two-paragraph analysis: How does Stave Four contribute to A Christmas Carol's themes?", "Answers vary.", lines=18, note="Score: claim (1); evidence 1 + analysis (1); evidence 2 + analysis (1); connection to whole story (1); conventions (1).")])],
    te("Students write scene analyses.", "Draw evidence; write analytically.", "Workbook Lesson 2.8",
       "Most important thing.", "Reread key moments in Stave Four.", ["Model a topic sentence."], "Plan.",
       ["Summary instead of analysis."], ["Purpose statement frame."], ["Compare Stave Four to Stave One."], independent="Write. Weekly Check tomorrow."),
    summary="Analyze a scene's purpose with evidence.")

# ================================================================= Week 3 · Noun forms and functions (Stave Five)
L9 = Lesson("2.9", "Kinds of Nouns",
    "I can identify concrete, abstract, collective, compound, and proper nouns.", "L.7.1",
    [("concrete noun", "Names something you can perceive with the senses: chain, turkey."), ("abstract noun", "Names an idea, quality, or feeling: greed, generosity."),
     ("collective noun", "Names a group: family, crowd."), ("compound noun", "Made of two or more words: counting-house, door-knocker, schoolboy.")],
    "Which is easier to draw: “a chain” or “greed”? Why?",
    [ReaderAssign(CAROL, "Stave Five", "How has Scrooge changed? What does he do first, and how do other people react?"),
     Figure(lambda t: table(t, [["Kind", "Examples from A Christmas Carol"], ["concrete", "chain, crutch, turkey, gravestone, fire"], ["abstract", "greed, charity, fear, joy, hope"], ["collective", "family, crowd, party, flock"],
                                ["compound", "counting-house, door-knocker, schoolboy"], ["proper", "Scrooge, London, Camden Town, Tiny Tim"]], [1.4 * inch, 4.0 * inch], width=5.4 * inch)),
     Text("Writers use <b>abstract nouns</b> to name big ideas (themes) and <b>concrete nouns</b> to make those ideas visible. Marley's <i>chain</i> (concrete) stands for the <i>greed</i> and <i>selfishness</i> (abstract) he forged “link by link” in life."),
     KeyIdea("Concrete nouns can be sensed; abstract nouns name ideas. Writers use concrete nouns to symbolize abstract ones.")],
    [Problem("Concrete or abstract: generosity", "abstract"), Problem("Collective noun for a group of carol singers", "choir"), Problem("What abstract idea does Marley's chain represent?", "greed / selfish choices")],
    [S("Warm-Up", [SA("Abstract noun example", "joy, charity"), SA("Collective noun example", "family, crowd")], cols=2),
     S("Classify", [SA(w, a) for w, a in [("charity", "abstract"), ("audience", "collective"), ("churchyard", "compound (concrete)"), ("Belle", "proper"), ("loyalty", "abstract"), ("lantern", "concrete"),
                                          ("flock", "collective"), ("mercy", "abstract")]], cols=2),
     S("Symbols", [OR("In Stave Three the Spirit sees “a crutch without an owner, carefully preserved.” In Stave Five, Tiny Tim does not die. What abstract ideas do the crutch and the chain represent? What does Scrooge's change mean for them?", "The chain stands for greed and its punishment; the crutch stands for Tiny Tim's life, need, and the family's love. Scrooge's change breaks the chain and saves Tim.", lines=4)])],
    te("Students classify nouns.", "Demonstrate command of grammar and usage.", "Grade 7 Reader: A Christmas Carol (Stave Five), workbook Lesson 2.9",
       "Draw a chain vs greed.", "Read Stave Five.", ["Teach noun types.", "Concrete as symbol of abstract."], "Your Turn 1–3.",
       ["Calling collective nouns plural."], ["Sorting cards."], ["List abstract nouns that name the story's themes."]),
    summary="Concrete, abstract, collective, compound, and proper nouns.")

L10 = Lesson("2.10", "Noun Functions in Sentences",
    "I can identify how nouns function in sentences: subject, direct object, indirect object, object of a preposition, and predicate noun.", "L.7.1",
    [("direct object", "Receives the action of the verb."), ("indirect object", "Tells to whom or for whom the action is done."), ("predicate noun", "Follows a linking verb and renames the subject.")],
    "In “Scrooge sent Bob a turkey,” who receives what?",
    [Figure(lambda t: table(t, [["Function", "Example (function in bold)"], ["subject", "<b>Scrooge</b> bought a turkey."], ["direct object", "Scrooge bought a <b>turkey</b>."], ["indirect object", "Scrooge sent <b>Bob</b> a turkey."],
                                ["object of preposition", "The boy ran to the <b>poulterer's</b>."], ["predicate noun", "Scrooge became a good <b>friend</b>."]], [1.6 * inch, 3.8 * inch], width=5.4 * inch)),
     Example("Identify functions", "“Scrooge sent Bob a turkey.”", ["Subject: Scrooge (who sent?).", "Direct object: turkey (sent what?).", "Indirect object: Bob (sent to whom?)."], "Scrooge = subject; turkey = direct object; Bob = indirect object"),
     KeyIdea("Ask who/what does it (subject), receives it (direct object), to/for whom (indirect object), after a preposition (object of preposition), or renames the subject after a linking verb (predicate noun).")],
    [Problem("Function of “Scrooge” in “Fred invited Scrooge.”", "direct object"), Problem("Function of “clerk” in “Bob is the clerk.”", "predicate noun"), Problem("Function of “street” in “Scrooge walked along the street.”", "object of preposition")],
    [S("Warm-Up", [SA("Who/what does the action?", "subject"), SA("Receives the action?", "direct object")], cols=2),
     S("Identify the Function of the Bold Noun", [SA(q, a) for q, a in [("<b>Bob</b> carried Tiny Tim.", "subject"), ("Bob carried <b>Tiny Tim</b>.", "direct object"), ("Scrooge gave <b>Bob</b> a raise.", "indirect object"),
                                                                       ("Scrooge gave Bob a <b>raise</b>.", "direct object"), ("The Spirit stood beside the <b>grave</b>.", "object of preposition"), ("Marley was a <b>ghost</b>.", "predicate noun"),
                                                                       ("Fred offered <b>Scrooge</b> a seat.", "indirect object"), ("Scrooge became a second <b>father</b>.", "predicate noun")]], cols=2),
     S("Exit Ticket", [OR("Write a sentence about Stave Five that contains a subject, direct object, and indirect object. Label them.", "Answers vary.", lines=2)])],
    te("Students identify noun functions.", "Explain the function of words in sentences.", "Workbook Lesson 2.10",
       "Who receives what?", "Pull sentences from Stave Five.", ["Teach functions; question method."], "Your Turn 1–3.",
       ["Confusing indirect and direct objects."], ["Ask: gave what? gave to whom?"], ["Diagram sentences."]),
    summary="Nouns function as subjects, objects, and predicate nouns.")

L11 = Lesson("2.11", "Appositives",
    "I can use appositives to add information, punctuating them correctly.", "L.7.1, L.7.2",
    [("appositive", "A noun or noun phrase that renames another noun right beside it.")],
    "How can you tell readers who Fred is without writing a whole new sentence?",
    [Text("An <b>appositive</b> renames a noun: <i>Fred, <b>Scrooge's nephew</b>, invites him to dinner.</i> Use commas when the appositive adds extra (nonessential) information. No commas when it is essential to identify which one: <i>Dickens's novella <b>A Christmas Carol</b> was published in 1843.</i>"),
     Example("Combine with an appositive", "Bob Cratchit works in the counting-house. Bob Cratchit is Scrooge's clerk.", ["Find the renaming phrase: Scrooge's clerk.", "Place it beside Bob Cratchit with commas."], "Bob Cratchit, Scrooge's clerk, works in the counting-house."),
     KeyIdea("Appositives rename nouns. Use commas for extra information.")],
    [Problem("Find the appositive: Fezziwig, a kind old merchant, threw a Christmas party.", "a kind old merchant"), Problem("Combine: Fan is Scrooge's sister. Fan brings him home from school.", "Fan, Scrooge's sister, brings him home from school."), Problem("Do appositives that add extra information need commas?", "Yes")],
    [S("Warm-Up", [SA("An appositive…", "renames a noun"), SA("Extra info appositives need…", "commas")], cols=2),
     S("Combine with Appositives", [SA(q, a) for q, a in [("Belle ended the engagement. Belle was the woman Scrooge loved.", "Belle, the woman Scrooge loved, ended the engagement."), ("Old Joe bought stolen goods. Old Joe was a shopkeeper.", "Old Joe, a shopkeeper, bought stolen goods."),
                                                          ("The Ghost wore a green robe. The Ghost was a jolly giant.", "The Ghost, a jolly giant, wore a green robe."), ("Dickens visited a ragged school. Dickens was a famous author.", "Dickens, a famous author, visited a ragged school.")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence about a family member using an appositive.", "Answers vary; commas correct.", lines=2)])],
    te("Students use appositives.", "Use punctuation to set off nonrestrictive elements; vary sentences.", "Workbook Lesson 2.11",
       "Who is Fred?", "Find appositives in the Reader.", ["Teach commas for extra info."], "Your Turn 1–3.",
       ["Missing the second comma."], ["Appositive sandwich: comma–phrase–comma."], ["Revise a paragraph with three appositives."]),
    summary="Appositives rename nouns; commas set off extra information.")

L12 = Lesson("2.12", "Forming Nouns from Other Words",
    "I can form nouns with suffixes and use them to write about ideas.", "L.7.4b, L.7.1",
    [("nominalization", "Turning a verb or adjective into a noun, such as generous → generosity.")],
    "How can you turn the adjective “generous” into a word that names the idea?",
    [Figure(lambda t: table(t, [["Suffix", "Base word", "Noun"], ["-ness", "kind, happy", "kindness, happiness"], ["-tion / -sion", "transform, decide", "transformation, decision"], ["-ment", "punish, astonish", "punishment, astonishment"],
                                ["-ity", "generous, charitable", "generosity, charity"], ["-ance / -ence", "repent / obey", "repentance, obedience"], ["-dom", "free, wise", "freedom, wisdom"]], [1.4 * inch, 1.8 * inch, 2.2 * inch], width=5.4 * inch)),
     Text("Analytical writing often uses abstract nouns: <i>Scrooge's <b>transformation</b> replaces <b>greed</b> with <b>generosity</b>.</i>"),
     KeyIdea("Suffixes turn verbs and adjectives into nouns that name ideas, which are essential for writing about themes.")],
    [Problem("Noun form of <i>free</i>", "freedom"), Problem("Noun form of <i>punish</i>", "punishment"), Problem("Noun form of <i>generous</i>", "generosity")],
    [S("Warm-Up", [SA("generous →", "generosity"), SA("decide →", "decision")], cols=2),
     S("Form the Noun", [SA(w, a) for w, a in [("transform", "transformation"), ("charitable", "charity"), ("obey", "obedience"), ("astonish", "astonishment"), ("celebrate", "celebration"), ("wise", "wisdom")]], cols=2),
     S("Write About Ideas", [OR("Using at least three abstract nouns, write two sentences about what Scrooge chooses in Stave Five.", "e.g. Scrooge chooses generosity over greed. His transformation brings happiness to the Cratchits and to himself.", lines=3)], passage=P_HONOUR),
     S("Exit Ticket", [OR("Explain Scrooge's promise: “I will honour Christmas in my heart, and try to keep it all the year.”", "He will live with the kindness and generosity of Christmas every day, not just once a year.", lines=2)])],
    te("Students form nouns from verbs and adjectives.", "Use affixes; demonstrate command of grammar.", "Workbook Lesson 2.12",
       "generous → ?", "Read Scrooge's promise at the end of Stave Four.", ["Teach suffix chart."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Spelling changes (obey → obedience)."], ["Dictionary check."], ["List theme nouns for A Christmas Carol."]),
    summary="Suffixes form abstract nouns for writing about ideas.")

# ================================================================= Week 4 · Noun usage and writing application (response to the whole story)
L13 = Lesson("2.13", "Precise Nouns for Vivid Writing",
    "I can replace vague nouns with precise ones.", "L.7.3a, W.7.3d",
    [("vague", "Not clear or specific.")],
    "Which paints a clearer picture: “The person carried a thing” or “The clerk carried a crutch”?",
    [Text("Vague nouns (<i>thing, stuff, person, place</i>) leave readers guessing. Precise nouns create images and save words."),
     Figure(lambda t: table(t, [["Vague", "Precise"], ["a person", "a clerk, a miser, a poulterer"], ["a thing", "a ledger, a crutch, a door-knocker"], ["a place", "a counting-house, a garret, a churchyard"], ["a feeling", "dread, remorse, relief"]],
                            [1.8 * inch, 3.4 * inch], width=5.2 * inch)),
     KeyIdea("Replace vague nouns with precise nouns that create a clear image or name an exact idea.")],
    [Problem("Precise noun for “a building where grain is kept”", "granary"), Problem("Revise: A person in the office wrote stuff.", "e.g. The clerk copied letters."), Problem("Precise abstract noun for “feeling bad about what you did”", "guilt, remorse")],
    [S("Warm-Up", [SA("Vague noun example", "thing, stuff, person"), SA("Precise noun for a shop that sells poultry", "poulterer's")], cols=2),
     S("Revise", [SA(q, a) for q, a in [("The man held a thing.", "e.g. The miser held a candle."), ("They went to a place with graves.", "e.g. They walked into a churchyard."),
                                        ("She felt a feeling of being glad it was over.", "e.g. She felt relief."), ("The people watched the show.", "e.g. The audience watched the play.")]], cols=1),
     S("Exit Ticket", [OR("Find a sentence in your Stave Four analysis with a vague noun. Revise it.", "Answers vary.", lines=2)])],
    te("Students use precise nouns.", "Choose language that expresses ideas precisely, eliminating wordiness.", "Workbook Lesson 2.13",
       "Person and thing.", "Find precise nouns in the Reader.", ["Model revisions."], "Your Turn 1–3.",
       ["Replacing with fancy but wrong words."], ["Thesaurus plus dictionary check."], ["Revise a past essay paragraph."]),
    summary="Precise nouns create clear images and ideas.")

L14 = Lesson("2.14", "Possessive Nouns and Clear Reference",
    "I can form possessives correctly, including plural, irregular, and joint possession.", "L.7.2, L.7.1",
    [("joint possession", "Two or more people owning the same thing: Bob and Mrs. Cratchit's home.")],
    "Is it “Bob's and Mrs. Cratchit's home” or “Bob and Mrs. Cratchit's home”?",
    [Figure(lambda t: table(t, [["Rule", "Example"], ["singular: 's", "the clerk's desk; Marley's chain"], ["singular ending in s: 's (usually)", "Dickens's novel; James's book"], ["plural ending in s: '", "the Cratchits' dinner"],
                                ["irregular plural: 's", "the children's games; the men's hats"], ["joint possession: 's on the last name only", "Bob and Mrs. Cratchit's home"], ["separate possession: 's on each name", "Scrooge's and Fred's houses"]],
                            [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     KeyIdea("Choose the possessive form by number (singular/plural), regularity, and whether ownership is joint or separate.")],
    [Problem("The home shared by Bob and Mrs. Cratchit", "Bob and Mrs. Cratchit's home"), Problem("The separate houses of Scrooge and Fred", "Scrooge's and Fred's houses"), Problem("The dinner belonging to the Cratchits", "the Cratchits' dinner")],
    [S("Warm-Up", [SA("Possessive of the plural Cratchits", "Cratchits'"), SA("Possessive of children", "children's")], cols=2),
     S("Write the Possessive", [SA(q, a) for q, a in [("the office of Scrooge", "Scrooge's office"), ("the songs of the miners", "the miners' songs"), ("the games of the children", "the children's games"),
                                                      ("the business shared by Scrooge and Marley", "Scrooge and Marley's business"), ("the separate visits of the three Spirits", "the three Spirits' visits"), ("the crutch of Tiny Tim", "Tiny Tim's crutch")]], cols=1),
     S("Exit Ticket", [OR("Write a sentence with joint possession and one with separate possession.", "Answers vary.", lines=2)])],
    te("Students form possessives correctly.", "Demonstrate command of capitalization, punctuation, and spelling.", "Workbook Lesson 2.14",
       "Whose home?", "Find possessives in Stave Five.", ["Teach the chart."], "Your Turn 1–3.",
       ["Joint vs separate confusion."], ["Ask: one thing or two?"], ["Proofread a past essay for possessives."]),
    summary="Possessives depend on number, regularity, and joint or separate ownership.")

L15 = Lesson("2.15", "Writing a Literary Analysis Essay",
    "I can write a literary analysis essay about a theme in a novel or novella.", "W.7.2, W.7.9a",
    [("thesis", "The central claim of an essay.")],
    "Can a person really change? What does A Christmas Carol suggest?",
    [P_HONOUR,
     Text("A literary analysis essay has an <b>introduction</b> (hook, context, thesis), <b>body paragraphs</b> (topic sentence, integrated evidence, analysis), and a <b>conclusion</b> (restated thesis and significance)."),
     Example("Thesis", "Prompt: What does A Christmas Carol suggest about whether people can change?", ["Take a position.", "Preview reasons."],
             "Although Scrooge begins the story as “solitary as an oyster,” A Christmas Carol suggests that anyone can change when he or she truly sees how choices affect other people."),
     KeyIdea("Thesis → body paragraphs with integrated evidence and analysis → conclusion with significance.")],
    [Problem("What three parts are in an introduction?", "hook, context, thesis"), Problem("What does a conclusion add besides restating?", "significance: why it matters"), Problem("Name a key quote for change.", "“I am not the man I was.” / “I will honour Christmas in my heart, and try to keep it all the year.”")],
    [S("Warm-Up", [SA("Thesis =", "the central claim"), SA("Body paragraph starts with a…", "topic sentence")], cols=2),
     S("Plan", [OR("Thesis:", "Answers vary.", lines=2), OR("Body 1 topic + evidence:", "Answers vary.", lines=3), OR("Body 2 topic + evidence:", "Answers vary.", lines=3)]),
     S("Draft", [OR("Draft your literary analysis essay.", "Answers vary.", lines=22, note="Look for: thesis; two body paragraphs with integrated evidence and analysis; conclusion with significance.")])],
    te("Students write literary analysis essays.", "Write informative/explanatory texts analyzing literature; draw evidence.", "Workbook Lesson 2.15",
       "Can people change?", "Reread Stave Five.", ["Model a thesis and introduction."], "Plan and draft.",
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
    OR("Connect this passage to Fezziwig's Christmas party in A Christmas Carol.", "In both, rich and poor celebrate side by side: at Fezziwig's, the master, apprentices, and servants all dance together, and differences of class seem to disappear for a night.", lines=3),
    MC("Which is an objective summary sentence?", ["Venetian masks are the most beautiful art in the world.", "Venetian masks let people of different classes celebrate Carnival without revealing their identities.", "Tourists waste money on masks."], 1)], passage=P_C5)], minutes=20)
C3 = Check("Weekly Check 6: Nouns", [S("Read and answer", [
    SA("Find two appositives.", "the commander of the rescue team; an old but reliable machine (also: six exhausted men)"), SA("Abstract noun in paragraph 2", "courage / fear / absence / decision"),
    SA("Collective noun in paragraph 1", "crew / team"), SA("Function of <i>order</i> in “She gave the order”", "direct object"),
    SA("Function of <i>decision</i> in “It was a decision”", "predicate noun"), SA("Possessive: the boat of the fishermen", "the fishermen's boat"),
    SA("Noun form of <i>brave</i>", "bravery"), SA("Replace the vague noun: She looked at the thing on the screen.", "e.g. She studied the radar map on the screen.")], cols=1, passage=P_C6)], minutes=20)

REVIEW = Check("Unit 2 Review", [
    S("Reading", [SA("A subplot…", "supports or mirrors the main plot"), SA("Close reading asks…", "what, how, why"), SA("Suspense is…", "tense uncertainty about what will happen"),
                  SA("RL.7.7 compares text and…", "performance")], cols=2),
    S("Nouns", [SA("Concrete or abstract: mercy", "abstract"), SA("Function: Fred gave <b>Scrooge</b> an invitation.", "indirect object"), SA("Add an appositive: Fezziwig helped Scrooge.", "e.g. Fezziwig, a kind old merchant, helped Scrooge."),
                SA("Joint possession: Bob and Mrs. Cratchit / children", "Bob and Mrs. Cratchit's children"), SA("Noun form of <i>transform</i>", "transformation")], cols=1)],
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

UNIT = Unit(2, "Long Passages and the Power of Nouns", "Multiple plotlines, close reading, scene analysis, text vs performance, noun forms and functions, and the literary analysis essay, with A Christmas Carol, Stave Three–Stave Five.",
    "As Scrooge's journey reaches its climax, you'll analyze long passages and famous speeches, see how each scene fits the whole story, and compare the book with stage and film versions. You'll also master nouns, the words that name everything from Marley's chain to generosity itself, and write a full literary analysis essay.",
    ["Track plotlines; close read speeches; analyze how scenes contribute to the whole.", "Infer across long informational texts; compare text and performance.",
     "Identify kinds and functions of nouns; use appositives and possessives correctly.", "Write multi-paragraph responses and a literary analysis essay with integrated evidence."],
    [("RL.7.1–5, RL.7.7", "Cite evidence; analyze theme, elements, word choice, structure; compare text and performance."), ("RI.7.1–3", "Infer and analyze central ideas and interactions."),
     ("L.7.1–3", "Grammar, punctuation, precise language."), ("W.7.2, W.7.5, W.7.9", "Write and revise analytical essays.")],
    [("subplot", "A secondary plotline."), ("close reading", "Careful analysis of a short passage."), ("abstract noun", "Names an idea."), ("appositive", "Renames a noun."), ("thesis", "An essay's central claim.")],
    ["Unit 1 skills."], ["Grade 7 Reader: A Christmas Carol (Stave Three–Stave Five)", "Optional: a filmed or staged production clip"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Integrating evidence, analyzing a scene's purpose, and choosing precise words are the same skills used in reviews, reports, and persuasive writing.",
    family_note="Ask your student which moment finally changes Scrooge's mind, and why.",
    weeks=WEEKS)
