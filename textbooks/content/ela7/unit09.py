"""Grade 7 ELA · Unit 9: Capstone — style and tone, transitions and organization, revising arguments, portfolio and cumulative review; Grade 7 ELA Year-End Test.
Anchor reading: The Genius of the Harlem Renaissance Reader (Jun 21 – Jul 16, 2027)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule
from content.ela7.unit07 import HR, P_MASK
from content.ela7.unit08 import rules


# ================================================================= passages
P_HUGHES = Passage("Langston Hughes: Poet of the People", [
    "Langston Hughes (1901–1967) was one of the most important voices of the Harlem Renaissance. He grew up mostly in the Midwest, and as a young man he worked many jobs, including as a sailor and a busboy, while he wrote poetry. His first book of poems, <i>The Weary Blues</i>, appeared in 1926.",
    "Hughes wanted his poems to sound like the people he knew. He borrowed the rhythms of jazz and the blues, repeated lines the way a singer repeats a chorus, and used everyday words instead of fancy ones. His tone could be proud, playful, sorrowful, or defiant, sometimes all in a single poem.",
    "Some critics of his time thought that poetry should be formal and elevated. Hughes disagreed. He believed that the lives, speech, and music of ordinary Black Americans were worthy subjects for art, and generations of later writers followed his lead.",
], source="An original informational text", genre="Informational text")

P_TONE = Passage("Two Reviews of the Same Concert", [
    "<b>Review A.</b> The trumpets blazed. For two hours the band tore through song after song, and the crowd could not sit still. When the final note rang out, the whole hall rose to its feet, roaring. I walked home humming, my heart still keeping time.",
    "<b>Review B.</b> The concert lasted two hours. The band played fourteen songs, mostly fast ones, and the trumpets were loud. At the end, the audience stood and applauded. Tickets were twenty dollars.",
], source="Original texts", genre="Paired texts", numbered=False)

P_JOHNSON = Passage("Georgia Douglas Johnson and the S Street Salon", [
    "Georgia Douglas Johnson (1880–1966) was a poet, playwright, and teacher who lived in Washington, D.C. Her first book of poems, <i>The Heart of a Woman</i>, was published in 1918, and she went on to publish several more collections and to write many plays.",
    "Johnson is also remembered as a host. For years, on Saturday evenings, writers and artists gathered at her home on S Street to read their work aloud, trade ideas, and encourage one another. Young writers such as Langston Hughes and Jean Toomer were among the visitors. As a result, her home became one of the meeting places that connected the Harlem Renaissance to Washington.",
    "In contrast to some writers who became famous quickly, Johnson spent much of her life balancing her writing with work and family. Nevertheless, she kept writing, and her support for other artists helped the movement grow.",
], source="An original informational text based on historical facts", genre="Informational text")

P_DRAFT = Passage("Student Draft: Every Student Should Learn an Instrument", [
    "Every student should learn to play an instrument. Music is fun. Lots of people like music. My cousin plays drums.",
    "Also learning music helps your brain. Also it teaches you to work hard. Also you can play in a band with friends and that is fun too.",
    "Some people say music lessons cost too much. That is wrong. In conclusion, every student should learn an instrument.",
], source="An original student draft for revision", genre="Draft argument")

P_MCDOUGALD = Passage("Elise Johnson McDougald", [
    "Elise Johnson McDougald (1885–1971) was an educator and writer in New York City. She worked to improve schools and job opportunities for Black children and women, and she became one of the first Black women to serve as a principal in the city's public schools.",
    "Her essay “The Task of Negro Womanhood” appeared in <i>The New Negro</i> (1925), the influential collection edited by Alain Locke. In it, she describes the many kinds of work Black women were doing in Harlem, from homes and factories to offices and professions, and argues that they faced the double burden of racism and sexism. She supports her claims with observations of real working lives rather than with stereotypes.",
], source="An original informational text based on historical facts", genre="Informational text")

P_C26 = Passage("The Music of the Movement", [
    "Jazz grew out of African American communities in the South, especially New Orleans. During the Great Migration, musicians carried it north. In Harlem, clubs and dance halls filled with crowds eager to hear it. As a result, musicians such as Duke Ellington became famous.",
    "However, success had a cost. Some of the most famous clubs admitted only white customers, even though Black musicians performed on stage. Despite this injustice, the music spread across the country through radio and records, and jazz eventually became known as one of America's great art forms.",
], source="An original informational text", genre="Informational text")

P_YE1 = Passage("Lanterns on the Hill", [
    "Every summer evening, my grandmother climbed the hill behind her house with a paper lantern. She never explained why. I was eight the first time I followed her, my sneakers slipping on the dry grass.",
    "At the top, she lit the candle inside and held the lantern out over the valley. Below us, one by one, other lights answered: a porch lamp, a flashlight, a lantern just like hers. “Those are my friends,” she said. “We can't always visit. But we can always say, <i>I'm still here</i>.”",
    "Grandma is gone now. Last night I climbed the hill alone, my hands shaking as I struck the match. For a long moment, the valley stayed dark. Then, far below, a single porch light blinked on, and another, and another, like stars remembering their places.",
], source="An original story", genre="Realistic fiction")

P_YE2 = Passage("Should Cities Turn Down the Lights?", [
    "Artificial light at night has changed the way we live. It lets us work, travel, and play after sunset. But many scientists argue that cities now produce too much light, and that this “light pollution” has real costs.",
    "First, it affects wildlife. Many birds migrate at night and use the stars to navigate; bright city lights can confuse them and lead them to crash into buildings. Sea turtle hatchlings, which crawl toward the brightest horizon, may head inland toward streetlights instead of toward the sea.",
    "Second, it wastes energy and money. Lights that shine upward or stay on in empty buildings light nothing useful. In addition, some studies suggest that too much light at night can disturb human sleep.",
    "Critics point out that good lighting helps people feel safe and can prevent accidents. That concern is reasonable. However, cities do not need to choose between safety and darkness. Shielded lights that point downward, motion sensors, and warmer, dimmer bulbs can keep streets safe while letting the stars, and the creatures that depend on them, return.",
], source="An original argumentative article", genre="Argument")

P_T1 = Passage("The Quilt", [
    "My great-aunt Bea's sewing room smelled like cedar and old coffee. The unfinished quilt lay across her table, a patchwork of squares cut from shirts, dresses, and baby blankets that had belonged to four generations of our family.",
    "“This blue is your grandfather's work shirt,” she said, tapping a faded square. “This yellow was my wedding dress. And this one,” she touched a tiny square of green flannel, “was your first blanket.” Her hands trembled now, and the needle slipped more often than it used to.",
    "“I don't think I'll finish it,” she said quietly. For a long moment, the only sound was the clock ticking on the wall. Then she pushed the needle and thread across the table toward me.",
    "I had never sewn anything in my life. My first stitches wandered like lost ants across the fabric. Aunt Bea laughed, then guided my fingers until the thread pulled straight. By the end of summer, the last square was in place, and when we spread the quilt across her bed, it looked like a map of everyone who had ever loved me.",
], source="An original story", genre="Realistic fiction")

P_T2 = Passage("Should School Start Later?", [
    "Many middle and high schools begin classes before 8:00 in the morning. A growing number of doctors and parents argue that this is too early, and that schools should start later.",
    "First, teenagers' bodies are on a different schedule. During puberty, the body's internal clock shifts, so many teens naturally feel sleepy later at night and need to sleep later in the morning. In 2014, the American Academy of Pediatrics recommended that middle and high schools start no earlier than 8:30 a.m.",
    "Second, tired students struggle. Students who do not get enough sleep may have trouble paying attention and remembering what they learn. Some people also believe that sleepy students are grumpier, although this is harder to measure.",
    "Opponents argue that later start times would make it harder to schedule buses, sports, and after-school jobs. These are real challenges. However, schools that have shifted their schedules have found ways to adjust, and the benefits to students' health and learning are worth the effort.",
], source="An original argumentative article", genre="Argument")

# ================================================================= Week 1 · Style and tone (Langston Hughes)
L1 = Lesson("9.1", "Langston Hughes and the Sound of a Poem",
    "I can analyze how a poet's choices about rhythm, repetition, and word choice create a distinctive style.", "RL.7.4, RL.7.5",
    [("style", "The distinctive way a writer uses words, sentences, and sound."), ("refrain", "A line or phrase repeated in a poem or song.")],
    "Can a poem sound like music? How?",
    [ReaderAssign(HR, "Langston Hughes", "What did Hughes write about? What makes his poems sound like music?"),
     P_HUGHES,
     Figure(lambda t: table(t, [["Style element", "What to look for", "Possible effect"], ["rhythm", "a steady beat; lines that swing like a song", "musical, energetic"], ["repetition / refrain", "words or lines that return", "emphasis; a chorus feeling"],
                                ["diction", "everyday or formal words", "conversational or elevated"], ["line length", "short, broken lines or long flowing ones", "pauses, emphasis, speed"]], [1.4 * inch, 2.4 * inch, 1.8 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Style is the sum of a writer's choices: rhythm, repetition, diction, and line shape. Name the choice, then explain its effect.")],
    [Problem("What musical forms influenced Hughes?", "jazz and the blues"), Problem("What is a refrain?", "a repeated line or phrase"), Problem("Why did Hughes use everyday words?", "He wanted his poems to sound like the people he knew; he believed ordinary lives were worthy of art.")],
    [S("Warm-Up", [SA("Style =", "a writer's distinctive way of using language"), SA("Refrain =", "a repeated line")], cols=2),
     S("Analyze", [OR("Choose a Hughes poem from your Reader. Identify two style elements and explain the effect of each.", "Answers vary; e.g. repetition creates a chorus-like emphasis; short lines create pauses.", lines=5),
                   OR("According to the passage, why did some critics object to Hughes's style? How did he respond?", "They thought poetry should be formal and elevated; he believed ordinary Black life, speech, and music were worthy subjects.", lines=3)], passage=P_HUGHES),
     S("Exit Ticket", [OR("Describe Hughes's style in one sentence.", "Answers vary.", lines=2)])],
    te("Students analyze elements of a poet's style.", "Analyze the impact of rhymes and other repetitions of sounds; analyze form.", "Harlem Renaissance Reader (Langston Hughes), workbook Lesson 9.1",
       "Poems as music.", ["Read Langston Hughes in the Reader.", "Read “Poet of the People.”"], ["Read a Hughes poem aloud twice, once flat and once with rhythm."], "Your Turn 1–3.",
       ["Listing devices without effects."], ["Choice → effect frame."], ["Set a few lines to a beat."]),
    summary="Style = rhythm, repetition, diction, and line shape; explain effects.")

L2 = Lesson("9.2", "Tone and Mood",
    "I can identify tone and mood and explain how word choice creates them.", "RL.7.4, L.7.5",
    [("tone", "The writer's attitude toward the subject."), ("mood", "The feeling a text creates in the reader.")],
    "Can the same event be described in a happy way and a bored way?",
    [P_TONE,
     rules([["Tone words", ""], ["positive", "joyful, admiring, hopeful, playful, nostalgic, celebratory"], ["negative", "bitter, mocking, gloomy, defiant, resentful, anxious"], ["neutral", "objective, matter-of-fact, informative, detached"]], (1.2, 4.4), fs=9),
     Example("Compare tone", "Reviews A and B", ["A: “blazed,” “tore through,” “roaring,” “heart still keeping time.”", "B: plain facts: numbers, “loud,” “applauded.”"], "A's tone is enthusiastic and celebratory; B's is matter-of-fact and detached."),
     KeyIdea("Tone is the writer's attitude; mood is the reader's feeling. Both are built from word choice and detail.")],
    [Problem("Tone of Review B", "matter-of-fact, detached"), Problem("Which words in A create excitement?", "blazed, tore through, roaring"), Problem("Tone vs mood?", "Tone = writer's attitude; mood = reader's feeling.")],
    [S("Warm-Up", [SA("Tone =", "writer's attitude"), SA("Mood =", "reader's feeling")], cols=2),
     S("Analyze", [OR("Quote three words from Review A and explain how they create its tone.", "Answers vary; e.g. “blazed” suggests bright, powerful energy.", lines=3),
                   OR("Rewrite Review B's last two sentences in a disappointed tone.", "Answers vary.", lines=3),
                   OR("Name the tone of “We Wear the Mask.” Support with one phrase.", "sorrowful, bitter; e.g. “torn and bleeding hearts.”", lines=2)], passage=P_TONE),
     S("Exit Ticket", [OR("Write one sentence about your summer in a nostalgic tone.", "Answers vary.", lines=2)])],
    te("Students analyze tone and mood.", "Analyze the impact of word choice on meaning and tone.", "Workbook Lesson 9.2",
       "Same event, two ways.", "Read the reviews.", ["Teach tone vs mood; tone-word bank."], "Your Turn 1–3.",
       ["Naming tone with “good” or “bad.”"], ["Tone-word bank."], ["Rewrite a news article in three tones."]),
    summary="Tone = attitude; mood = feeling; both come from word choice.")

L3 = Lesson("9.3", "Developing Your Own Voice",
    "I can make deliberate style choices to create a consistent voice and tone in my writing.", "W.7.3d, L.7.3",
    [("voice", "The personality of a writer that comes through on the page.")],
    "If someone read your writing without your name, would they know it was yours?",
    [Text("Voice comes from the same tools as style: diction, sentence length and rhythm, figurative language, and details you choose to notice. A strong voice is <b>consistent</b>: the tone does not wander by accident."),
     rules([["Choice", "Plain version", "With voice"], ["specific detail", "It was hot.", "The sidewalk could have fried an egg, and the dog refused to leave the shade."], ["sentence rhythm", "I ran. I was late. The bus left.", "I ran, backpack thumping, as the bus coughed and pulled away without me."],
            ["figurative language", "The room was quiet.", "The room was as quiet as a held breath."]], (1.3, 1.6, 2.7), fs=9),
     KeyIdea("Choose details, rhythm, and diction on purpose, and keep the tone consistent.")],
    [Problem("Name two tools that create voice.", "e.g. diction, sentence rhythm, details, figurative language"), Problem("What makes a voice consistent?", "The tone stays the same unless the writer changes it on purpose."), Problem("Add voice: The food was good.", "Answers vary.")],
    [S("Warm-Up", [SA("Voice =", "the writer's personality on the page"), SA("Simile example", "Answers vary.")], cols=2),
     S("Add Voice", [OR(q, "Answers vary.", lines=2) for q in ["The storm was loud.", "My little brother was annoying.", "The city at night was pretty.", "The test was hard."]], cols=1),
     S("Exit Ticket", [OR("Write a 4-sentence paragraph about a place you love, in a consistent voice. Name your tone.", "Answers vary.", lines=5)])],
    te("Students develop voice.", "Use precise words, details, and sensory language; vary sentence patterns for style.", "Workbook Lesson 9.3",
       "Name-free test.", "Share two writing samples without names.", ["Model plain → voice."], "Your Turn 1–3.",
       ["Overloading with adjectives."], ["One strong detail per sentence."], ["Write a paragraph in a famous author's voice."]),
    summary="Voice comes from purposeful, consistent choices.")

L4 = Lesson("9.4", "Comparing Styles Across Time",
    "I can compare how two poets from different times address a similar theme with different styles.", "RL.7.9, RL.7.4",
    [],
    "How might a poet in 1895 and a poet in 1925 write differently about the same struggle?",
    [P_MASK,
     Text("Dunbar wrote “We Wear the Mask” in 1895 using a formal rhyme scheme, elevated diction, and a refrain. Thirty years later, Hughes often wrote in free or blues-shaped verse with everyday speech. Both poets address the experience of Black Americans facing racism, but their tones and styles differ."),
     Figure(lambda t: table(t, [["", "Dunbar, “We Wear the Mask”", "Hughes (poem from your Reader)"], ["form", "rhymed, regular stanzas", ""], ["diction", "formal, elevated (“myriad subtleties”)", ""], ["tone", "sorrowful, bitter, hidden pain", ""], ["theme", "hiding pain to survive", ""]],
                            [1.0 * inch, 2.3 * inch, 2.3 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Compare form, diction, and tone, then explain how each poet's style shapes the theme.")],
    [Problem("What does “the mask” stand for?", "the hidden pain and false smile Black Americans showed to survive racism"), Problem("Describe Dunbar's diction.", "formal, elevated"), Problem("One way Hughes's style differs", "e.g. everyday speech, blues rhythms, free verse")],
    [S("Warm-Up", [SA("Year of “We Wear the Mask”", "1895"), SA("Refrain of the poem", "We wear the mask")], cols=2),
     S("Compare", [OR("Complete the Hughes column of the chart using a poem from your Reader.", "Answers vary.", lines=4),
                   OR("Write a paragraph comparing how the two poets address a similar theme with different styles. Use one quotation from each.", "Answers vary; must compare form/diction/tone and use evidence.", lines=7)], passage=P_MASK),
     S("Exit Ticket", [OR("Which style speaks to you more? Why?", "Answers vary.", lines=2)])],
    te("Students compare styles across time.", "Compare and contrast how texts address similar themes.", "Harlem Renaissance Reader (Hughes poem), workbook Lesson 9.4",
       "1895 vs 1925.", "Reread “We Wear the Mask” and a Hughes poem.", ["Model one chart row."], "Your Turn 1–3.",
       ["Comparing topics, not styles."], ["Chart first, paragraph second."], ["Write a short poem in each style."], independent="Workbook. Weekly Check tomorrow."),
    summary="Compare form, diction, and tone to show how style shapes theme.")

# ================================================================= Week 2 · Transitions and organization (Georgia Douglas Johnson)
L5 = Lesson("9.5", "Georgia Douglas Johnson: Building a Community",
    "I can determine central ideas and analyze how an informational text develops them.", "RI.7.2, RI.7.3",
    [("salon", "A regular gathering of writers, artists, and thinkers to share work and ideas.")],
    "Why might writers need each other?",
    [ReaderAssign(HR, "Georgia Douglas Johnson", "What did Johnson write? Why was her home important?"),
     P_JOHNSON,
     Example("Find the central idea", "“Georgia Douglas Johnson and the S Street Salon”", ["¶1: she was a poet and playwright.", "¶2: her home became a gathering place for writers.", "¶3: she kept writing and supported others despite challenges."],
             "Johnson contributed to the Harlem Renaissance both through her own writing and by building a community that supported other artists."),
     KeyIdea("Trace how each paragraph adds to the central idea.")],
    [Problem("Where did Johnson live?", "Washington, D.C."), Problem("What happened at her home?", "Writers and artists gathered to share work and encourage one another."), Problem("Name a visitor.", "Langston Hughes or Jean Toomer")],
    [S("Warm-Up", [SA("Salon =", "a gathering to share work and ideas"), SA("Johnson's first book", "The Heart of a Woman (1918)")], cols=2),
     S("Analyze", [OR("State the central idea in one sentence.", "Johnson supported the movement through her writing and by building a community of artists.", lines=2),
                   OR("How does paragraph 3 develop the central idea?", "It shows her persistence despite challenges and her support for others.", lines=3),
                   OR("Read a Johnson poem in your Reader. What is its tone?", "Answers vary.", lines=2)], passage=P_JOHNSON),
     S("Exit Ticket", [OR("Who in your life helps you do your best work? How?", "Answers vary.", lines=2)])],
    te("Students analyze central ideas.", "Determine central ideas and analyze their development.", "Harlem Renaissance Reader (Georgia Douglas Johnson), workbook Lesson 9.5",
       "Writers need each other.", ["Read Johnson in the Reader.", "Read the passage."], ["Model paragraph-by-paragraph tracing."], "Your Turn 1–3.",
       ["Summarizing every detail."], ["One phrase per paragraph."], ["Plan a family salon night."]),
    summary="Trace each paragraph's contribution to the central idea.")

L6 = Lesson("9.6", "Transitions That Show Relationships",
    "I can use transitions to show precise relationships between ideas.", "W.7.2c, W.7.1c",
    [("transition", "A word or phrase that shows how ideas connect.")],
    "What's the difference between “and then” and “as a result”?",
    [rules([["Relationship", "Transitions"], ["addition", "also, in addition, furthermore, moreover"], ["contrast", "however, in contrast, on the other hand, nevertheless"], ["cause / effect", "as a result, therefore, consequently, because of this"],
            ["example", "for example, for instance, such as"], ["time / sequence", "first, later, meanwhile, eventually, finally"], ["conclusion", "in conclusion, overall, ultimately"]], (1.4, 4.2), fs=9),
     Example("Find transitions", "“Georgia Douglas Johnson and the S Street Salon”", ["“As a result” (¶2): cause/effect.", "“In contrast” (¶3): contrast.", "“Nevertheless” (¶3): contrast (despite a challenge)."], "Each transition tells the reader exactly how the ideas relate."),
     KeyIdea("Choose the transition that names the exact relationship, not just “and” or “also.”")],
    [Problem("Relationship of “consequently”", "cause/effect"), Problem("Transition for contrast", "e.g. however"), Problem("Join: It rained. The game was canceled.", "It rained; as a result, the game was canceled.")],
    [S("Warm-Up", [SA("Transition =", "a word showing how ideas connect"), SA("Example transition", "for example")], cols=2),
     S("Choose a Transition", [SA(q, a) for q, a in [("Jazz was popular. ___, some clubs excluded Black customers.", "However"), ("Writers gathered at the salon. ___, they read their work aloud.", "During these meetings"),
                                                     ("Many people moved north. ___, Harlem's population grew.", "As a result"), ("Hughes worked many jobs, ___ sailor and busboy.", "such as"),
                                                     ("Johnson faced many challenges. ___, she kept writing.", "Nevertheless")]], cols=1),
     S("Exit Ticket", [OR("Write two sentences about the Harlem Renaissance joined by a cause/effect transition.", "Answers vary.", lines=2)])],
    te("Students use transitions precisely.", "Use appropriate transitions to create cohesion and clarify relationships.", "Workbook Lesson 9.6",
       "and then vs as a result.", "Find transitions in the Johnson passage.", ["Teach the chart."], "Your Turn 1–3.",
       ["Overusing “also.”"], ["Name the relationship first."], ["Revise an essay's transitions."]),
    summary="Pick the transition that names the relationship.")

L7 = Lesson("9.7", "Text Structures",
    "I can identify and use organizational structures that fit my purpose.", "RI.7.5, W.7.2a",
    [("text structure", "The way a text is organized: chronological, compare/contrast, cause/effect, problem/solution.")],
    "How would you organize an essay about why jazz spread?",
    [rules([["Structure", "Purpose", "Signal words"], ["chronological", "tell events in time order", "first, then, in 1925, later"], ["compare / contrast", "show similarities and differences", "both, similarly, in contrast, unlike"],
            ["cause / effect", "explain why something happened", "because, as a result, led to"], ["problem / solution", "present a problem and fixes", "the problem is, one solution, to solve"]], (1.4, 2.2, 2.0), fs=9),
     Example("Identify the structure", "“Georgia Douglas Johnson and the S Street Salon,” paragraph 2", ["Writers gathered at her home on Saturday evenings.", "“As a result,” her home became a meeting place for the movement."], "cause/effect"),
     KeyIdea("Match the structure to your purpose; use signal words so readers can follow it.")],
    [Problem("Structure for “How life changed after the Great Migration”", "cause/effect (or compare/contrast before and after)"), Problem("Structure for a biography", "chronological"), Problem("Signal words for problem/solution", "the problem is, one solution")],
    [S("Warm-Up", [SA("Chronological =", "time order"), SA("Compare/contrast signal word", "e.g. similarly, in contrast")], cols=2),
     S("Choose a Structure", [SA(q, a) for q, a in [("Explain how Dunbar and Hughes differ.", "compare/contrast"), ("Tell the life story of Georgia Douglas Johnson.", "chronological"),
                                                    ("Explain why so many people moved north.", "cause/effect"), ("Argue how cities can reduce light pollution.", "problem/solution")]], cols=1),
     S("Plan", [OR("Plan a short essay on a Harlem Renaissance topic. Name your structure and list three paragraph topics.", "Answers vary.", lines=4)])],
    te("Students analyze and use text structures.", "Analyze structure; organize ideas using strategies such as definition, classification, comparison/contrast, and cause/effect.", "Workbook Lesson 9.7",
       "Organize a jazz essay.", "Review the Reader's sections.", ["Teach the chart."], "Your Turn 1–3.",
       ["Mixing structures without purpose."], ["Purpose → structure match."], ["Diagram each structure."]),
    summary="Match structure to purpose; signal it.")

L8 = Lesson("9.8", "Cohesive Paragraphs",
    "I can write cohesive paragraphs with clear topic sentences, connected support, and concluding sentences.", "W.7.2a, W.7.2c",
    [("cohesion", "The way sentences in a paragraph connect and stay focused.")],
    "What makes a paragraph feel like it holds together?",
    [rules([["Part", "Job"], ["topic sentence", "states the paragraph's main point"], ["support", "evidence and explanation, connected by transitions"], ["concluding sentence", "wraps up or links to the next idea"]], (1.6, 4.0), fs=9.5),
     Example("Revise for cohesion", "Johnson wrote poems. Hughes visited. She lived in D.C. People read their work.",
             ["Add a topic sentence.", "Order the ideas logically.", "Add transitions and a conclusion."],
             "Georgia Douglas Johnson's home was a hub for writers. She lived in Washington, D.C., where she hosted gatherings on Saturday evenings. At these meetings, writers such as Langston Hughes read their work aloud. As a result, her home helped connect a community of artists."),
     KeyIdea("Topic sentence + connected support + concluding sentence = cohesion.")],
    [Problem("What does a topic sentence do?", "states the main point"), Problem("How do transitions help cohesion?", "They connect sentences and show relationships."), Problem("Concluding sentence job", "wraps up or links forward")],
    [S("Warm-Up", [SA("Cohesion =", "sentences connect and stay focused"), SA("Topic sentence goes…", "first (usually)")], cols=2),
     S("Revise", [OR("Revise for cohesion: Jazz came from New Orleans. Radio helped. Duke Ellington was famous. Clubs were in Harlem.", "Answers vary; topic sentence, logical order, transitions, conclusion.", lines=6)]),
     S("Exit Ticket", [OR("Which sentence in your revision is the topic sentence? Underline your transitions.", "Answers vary.", lines=2)])],
    te("Students write cohesive paragraphs.", "Organize ideas; use transitions to create cohesion.", "Workbook Lesson 9.8",
       "Holding together.", "Read the jumbled paragraph.", ["Model the revision."], "Your Turn.",
       ["Topic sentences that are too narrow."], ["Paragraph frame."], ["Revise a portfolio paragraph."], independent="Workbook. Weekly Check tomorrow."),
    summary="Topic sentence, connected support, concluding sentence.")

# ================================================================= Week 3 · Revising an argument (Elise Johnson McDougald)
L9 = Lesson("9.9", "Elise Johnson McDougald: An Argument from Evidence",
    "I can trace an author's argument and evaluate how well evidence supports the claims.", "RI.7.8, RI.7.6",
    [("double burden", "Facing two kinds of unfair treatment at once.")],
    "How can observation of real lives be evidence?",
    [ReaderAssign(HR, "Elise Johnson McDougald", "What did McDougald argue? What kinds of evidence did she use?"),
     P_MCDOUGALD,
     Text("Remember the Unit 7 note on historical language: use the original title when you name McDougald's essay, and current terms when you write in your own voice."),
     KeyIdea("Trace the claim, the evidence, and whether the evidence is relevant and sufficient.")],
    [Problem("Where did McDougald's essay appear?", "The New Negro (1925)"), Problem("What was the “double burden”?", "racism and sexism"), Problem("What kind of evidence did she use?", "observations of real working lives")],
    [S("Warm-Up", [SA("Claim =", "the writer's main argument"), SA("Relevant evidence =", "evidence that directly supports the claim")], cols=2),
     S("Analyze", [OR("State McDougald's claim in your own words.", "Black women in Harlem did many kinds of work and faced both racism and sexism.", lines=2),
                   OR("Why is observation of real working lives stronger evidence than stereotypes?", "It is based on facts and actual experience rather than assumptions.", lines=3),
                   OR("What other evidence might strengthen her argument today?", "Answers vary; e.g. statistics, interviews, records.", lines=2)], passage=P_MCDOUGALD),
     S("Exit Ticket", [OR("How did McDougald's work as an educator connect to her writing?", "Answers vary.", lines=2)])],
    te("Students trace and evaluate an argument.", "Trace and evaluate the argument and claims; assess reasoning and evidence.", "Harlem Renaissance Reader (Elise Johnson McDougald), workbook Lesson 9.9",
       "Observation as evidence.", ["Read McDougald in the Reader.", "Read the passage."], ["Model claim-evidence tracing."], "Your Turn 1–3.",
       ["Confusing topic with claim."], ["Claim / evidence / evaluation chart."], ["Interview a working woman in the family."]),
    summary="Trace the claim and evaluate the evidence.")

L10 = Lesson("9.10", "Revising Claims and Counterclaims",
    "I can revise an argument to strengthen its claim and respond to a counterclaim.", "W.7.1a, W.7.1b, W.7.5",
    [("rebuttal", "A response showing why a counterclaim is weaker or incomplete.")],
    "What's wrong with answering an opposing argument with “That is wrong”?",
    [P_DRAFT,
     rules([["Weak", "Strong"], ["Every student should learn an instrument. (no reasons)", "Every student should learn an instrument because music strengthens the brain, builds discipline, and connects people."],
            ["That is wrong.", "Some argue that lessons cost too much. However, many schools lend instruments and offer free group classes, so cost need not be a barrier."]], (2.4, 3.2), fs=9),
     KeyIdea("A strong claim previews reasons. A fair counterclaim is acknowledged, then rebutted with evidence.")],
    [Problem("Revise the claim", "e.g. Every student should learn an instrument because it strengthens the brain, builds discipline, and connects people."), Problem("Why is “That is wrong” weak?", "It gives no reasons or evidence."), Problem("What is a rebuttal?", "a response showing why the counterclaim is weaker")],
    [S("Warm-Up", [SA("Counterclaim =", "an opposing argument"), SA("Rebuttal =", "a response to the counterclaim")], cols=2),
     S("Revise", [OR("Rewrite paragraph 1 with a strong claim that previews reasons. Cut irrelevant sentences.", "Answers vary; remove “My cousin plays drums.”", lines=4),
                  OR("Rewrite the counterclaim and rebuttal in paragraph 3.", "Answers vary.", lines=4)], passage=P_DRAFT),
     S("Exit Ticket", [OR("Which sentence in the draft is irrelevant? Why?", "“My cousin plays drums.” It doesn't support the claim.", lines=2)])],
    te("Students revise claims and counterclaims.", "Introduce claims, acknowledge alternate claims; strengthen writing by revising.", "Workbook Lesson 9.10",
       "That is wrong.", "Read the draft.", ["Model weak → strong."], "Your Turn 1–3.",
       ["Straw-man counterclaims."], ["Some argue… However… frame."], ["Debate a sibling."]),
    summary="Strong claims preview reasons; rebut counterclaims with evidence.")

L11 = Lesson("9.11", "Revising Evidence and Citations",
    "I can revise an argument to add relevant evidence and cite sources correctly.", "W.7.1b, W.7.8",
    [],
    "Which is more convincing: “Music helps your brain” or a statistic from a study?",
    [P_DRAFT,
     rules([["Revision move", "Example"], ["replace general statements with specific evidence", "Researchers have found links between music training and memory skills (cite the source)."], ["introduce evidence with a signal phrase", "According to the National Association for Music Education, …"],
            ["explain how the evidence supports the claim", "This suggests that practicing music may help students in other subjects too."], ["cite every borrowed idea", "Use the source's author or organization and title; list it in Works Cited."]], (2.2, 3.4), fs=9),
     WatchOut("Never invent statistics. If you don't have a real source, say so and find one, or use reasoning instead."),
     KeyIdea("Specific, cited evidence + explanation is stronger than general opinion.")],
    [Problem("What is a signal phrase?", "words that introduce a source, e.g. According to…"), Problem("Why explain evidence?", "to show how it supports the claim"), Problem("Can you invent a statistic?", "No.")],
    [S("Warm-Up", [SA("Signal phrase example", "According to…"), SA("Works Cited lists…", "sources")], cols=2),
     S("Revise", [OR("Rewrite paragraph 2: cut the repeated “Also,” use precise transitions, and explain each reason.", "Answers vary.", lines=5),
                  OR("Describe what kind of real source you would look for to support “learning music helps your brain.”", "Answers vary; e.g. a university study, a science magazine article.", lines=3)], passage=P_DRAFT),
     S("Exit Ticket", [OR("Write one sentence introducing evidence with a signal phrase.", "Answers vary.", lines=2)])],
    te("Students revise evidence.", "Support claims with relevant evidence using credible sources; avoid plagiarism.", "Workbook Lesson 9.11",
       "Opinion vs evidence.", "Reread the draft.", ["Teach revision moves; the Watch Out."], "Your Turn 1–3.",
       ["Dropping in quotes without explanation."], ["Quote sandwich: introduce, quote, explain."], ["Find one real source together."]),
    summary="Use specific, cited evidence and explain it.")

L12 = Lesson("9.12", "Revision Workshop",
    "I can revise a complete argument or research piece for claim, evidence, organization, and style.", "W.7.1, W.7.5",
    [],
    "Which essay from this year could be even stronger?",
    [Figure(lambda t: table(t, [["Revision checklist", "✓"], ["Claim is clear and previews reasons.", ""], ["Each body paragraph has a topic sentence and relevant, cited evidence.", ""], ["Evidence is explained.", ""],
                                ["Counterclaim is acknowledged and rebutted.", ""], ["Transitions show precise relationships.", ""], ["Style is formal, concise, and consistent.", ""], ["Conclusion follows from the argument.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Revise for big ideas first (claim, evidence, organization), then style, then conventions.")],
    [Problem("What do you revise first?", "big ideas: claim, evidence, organization"), Problem("Name one checklist item.", "Answers vary."), Problem("Revising vs editing?", "Revising changes content and organization; editing fixes conventions.")],
    [S("Warm-Up", [SA("Revise =", "improve content and organization"), SA("Edit =", "fix conventions")], cols=2),
     S("Workshop", [OR("Choose an argument or research piece from this year. Use the checklist. List three revisions you made and why.", "Answers vary.", lines=8)]),
     S("Exit Ticket", [OR("Which revision made the biggest difference?", "Answers vary.", lines=2)])],
    te("Students revise a complete piece.", "Develop and strengthen writing by planning, revising, and editing.", "A portfolio piece, workbook Lesson 9.12",
       "Which essay?", "Select a piece.", ["Model with one paragraph."], "Revise.",
       ["Only fixing commas."], ["Big ideas first."], ["Peer review with a parent."], independent="Workbook. Weekly Check tomorrow."),
    summary="Revise big ideas, then style, then conventions.")

# ================================================================= Week 4 · Portfolio and cumulative review (Dunbar and Hughes)
L13 = Lesson("9.13", "Dreams and Masks: A Conversation Across Generations",
    "I can analyze how later writers respond to and build on earlier writers.", "RL.7.9, RL.7.2",
    [],
    "How do writers “talk” to the writers who came before them?",
    [ReaderAssign(HR, "Paul Laurence Dunbar and Langston Hughes (review)", "What does each writer want readers to see? Does Hughes's speaker hide his feelings or reveal them?"),
     Text("Dunbar's speakers often hide their pain behind a mask. Many Hughes poems, written a generation later, speak openly: proud, hopeful, or defiant. Reading them together shows a literary conversation, as later writers build on, answer, or push against earlier ones."),
     KeyIdea("Compare what each writer reveals or hides, and how the change reflects its time.")],
    [Problem("What does Dunbar's mask hide?", "pain, sorrow"), Problem("How do many Hughes poems differ?", "They speak openly, with pride or defiance."), Problem("What is a literary conversation?", "later writers responding to earlier ones")],
    [S("Warm-Up", [SA("Dunbar's poem year", "1895"), SA("Hughes's first book year", "1926")], cols=2),
     S("Synthesize", [OR("Write an analytical paragraph: How does a Hughes poem in your Reader respond to the idea of the mask? Use a quotation from each poet.", "Answers vary; claim, two quotations, explanation.", lines=8)]),
     S("Exit Ticket", [OR("Which writer from this unit would you most like to talk to? What would you ask?", "Answers vary.", lines=2)])],
    te("Students analyze a literary conversation.", "Compare and contrast texts; analyze theme.", "Harlem Renaissance Reader (Dunbar and Hughes), workbook Lesson 9.13",
       "Writers talking.", "Reread both poets.", ["Model a claim."], "Write.",
       ["Summarizing each poem separately."], ["Reveal vs hide chart."], ["Write a poem that answers one of them."]),
    summary="Later writers answer earlier ones.")

L14 = Lesson("9.14", "Year in Review: Reading Literature and Information",
    "I can apply this year's reading skills to new texts.", "RL.7.1–6, RI.7.1–8",
    [],
    "Which reading skill from this year do you use most?",
    [rules([["Skill", "Ask yourself"], ["cite evidence", "Which exact words prove my answer?"], ["theme / central idea", "What is the message? How does it develop?"], ["character and plot", "How do setting, events, and characters shape each other?"],
            ["word choice and tone", "Which words create this feeling or attitude?"], ["structure", "How does this part fit the whole?"], ["point of view", "Whose view is this? What do they know or not know?"], ["argument", "What's the claim? Is the evidence relevant and sufficient?"]], (1.8, 3.8), fs=9),
     KeyIdea("Every reading skill begins with a question and ends with evidence.")],
    [Problem("What is a theme?", "a message about life"), Problem("What makes evidence sufficient?", "There is enough of it to support the claim."), Problem("Name our four anchor readers.", "The Tempest; Jekyll and Hyde; The Time Machine; The Genius of the Harlem Renaissance")],
    [S("Warm-Up", [SA("Favorite anchor reader", "Answers vary."), SA("Skill you improved most", "Answers vary.")], cols=2),
     S("Apply", [OR("Read “Lanterns on the Hill” in the Year-End Review. State its theme and support it with two pieces of evidence.", "e.g. Love and connection outlast loss; evidence: the lights answer, “I'm still here.”", lines=5),
                 OR("Read “Should Cities Turn Down the Lights?” in the Year-End Review. State the claim and two reasons.", "Claim: cities should reduce light pollution; reasons: harms wildlife, wastes energy/money.", lines=4)]),
     S("Exit Ticket", [OR("Which skill do you still want to practice? Make a plan.", "Answers vary.", lines=2)])],
    te("Students review reading skills.", "Cite evidence; determine theme and central idea; trace arguments.", "Workbook Lesson 9.14, Year-End Review",
       "Most-used skill.", "Read the Year-End Review passages.", ["Review the chart."], "Your Turn 1–3.",
       ["Answers without evidence."], ["Question → evidence → explanation."], ["Teach a skill to a sibling."]),
    summary="Every reading skill: question, then evidence.")

L15 = Lesson("9.15", "Year in Review: Language and Conventions",
    "I can apply this year's grammar, usage, punctuation, and vocabulary skills.", "L.7.1–6",
    [],
    "Which grammar rule finally “clicked” for you this year?",
    [rules([["Topic", "Remember"], ["phrases and clauses", "Independent clauses stand alone; dependent clauses need help."], ["sentence types", "simple, compound, complex, compound-complex"], ["modifiers", "Place modifiers next to what they modify."],
            ["commas, semicolons, colons", "Know each rule and its purpose."], ["pronouns and verbs", "Clear antecedents; consistent tense."], ["vocabulary", "context, roots, connotation, figurative language"], ["style", "precise, concise, formal when needed"]], (1.8, 3.8), fs=9),
     KeyIdea("Conventions and word choice make ideas clear and credible.")],
    [Problem("Sentence type: When the bell rang, we left, and the hall emptied.", "compound-complex"), Problem("Fix: Hanging on the wall, I saw the painting.", "I saw the painting hanging on the wall."), Problem("<i>benevolent</i>: bene =", "good, well")],
    [S("Warm-Up", [SA("FANBOYS", "for, and, nor, but, or, yet, so"), SA("Semicolon joins…", "independent clauses")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Type: Although it rained, we played.", "complex"), ("Fix: Running to class, my books fell.", "Running to class, I dropped my books."), ("Punctuate: She had one goal win.", "She had one goal: win."),
                                          ("Fix the tense shift: She opens the door and saw the crowd.", "She opened the door and saw the crowd."), ("Connotation: thrifty vs stingy", "thrifty positive; stingy negative"), ("Meaning: The news was a bombshell.", "a shocking surprise (metaphor)")]], cols=1),
     S("Exit Ticket", [OR("Write a compound-complex sentence about this year.", "Answers vary.", lines=2)])],
    te("Students review language skills.", "Demonstrate command of conventions; determine word meanings.", "Workbook Lesson 9.15, Year-End Review",
       "Clicked rule.", "Review notes from Units 1–8.", ["Review the chart."], "Your Turn 1–3.",
       ["Cramming instead of targeted review."], ["Review by error type."], ["Make a grammar game."], independent="Practice; continue the Year-End Review."),
    summary="Clear conventions and precise words.")

L16 = Lesson("9.16", "Portfolio Reflection and Presentation",
    "I can select, reflect on, and present my best work from the year.", "W.7.10, SL.7.4, SL.7.6",
    [("portfolio", "A collection of a writer's best work with reflections.")],
    "What piece of writing are you proudest of this year?",
    [Figure(lambda t: table(t, [["Portfolio", "Include"], ["best narrative or creative piece", "final draft + one-sentence reflection"], ["best analytical essay", "final draft + what you revised"], ["best argument or research piece", "final draft + sources"],
                                ["growth piece", "an early piece and a later one side by side"], ["reflection letter", "your growth, goals for Grade 8"]], [2.4 * inch, 3.2 * inch], width=5.6 * inch)),
     Text("<b>Presentation:</b> choose one piece to read aloud or summarize (3–5 minutes). Speak clearly, make eye contact, and explain why you chose it."),
     KeyIdea("Reflection turns finished work into learning: what you did, how you grew, and what's next.")],
    [Problem("What is a portfolio?", "a collection of best work with reflections"), Problem("Name one presentation skill.", "e.g. eye contact, clear volume"), Problem("Why include a growth piece?", "to show progress over time")],
    [S("Warm-Up", [SA("Proudest piece", "Answers vary."), SA("One goal for Grade 8", "Answers vary.")], cols=2),
     S("Reflect", [OR("Write your reflection letter: What did you learn this year as a reader and writer? Which piece shows your growth? What are your goals for Grade 8?", "Answers vary.", lines=10)]),
     S("Exit Ticket", [OR("After presenting, write one thing that went well and one thing to improve.", "Answers vary.", lines=2)])],
    te("Students assemble and present a portfolio.", "Write routinely; present claims and findings; adapt speech to context.", "Portfolio folder, workbook Lesson 9.16, Year-End Review",
       "Proudest piece.", "Gather the year's writing.", ["Model a reflection."], "Assemble and present.",
       ["Choosing pieces without reflection."], ["Reflection sentence starters."], ["Present to family by video."], independent="Presentations and celebration.", exit_="Tomorrow: Year-End Test."),
    summary="Select, reflect, present.")

# ================================================================= checks
C1 = Check("Weekly Check 25: Style and Tone", [S("Read and answer", [
    SA("Tone of Review A", "enthusiastic, celebratory"), SA("Tone of Review B", "matter-of-fact, detached"), SA("Two words in A that create mood", "e.g. blazed, roaring"),
    SA("Tone vs mood", "tone = writer's attitude; mood = reader's feeling"), SA("One element of Hughes's style", "e.g. blues/jazz rhythm, repetition, everyday diction"),
    OR("Rewrite Review B's first sentence with a bored tone.", "Answers vary.", lines=2)], cols=1, passage=P_TONE)], minutes=20)
C2 = Check("Weekly Check 26: Transitions and Structure", [S("Read and answer", [
    SA("Relationship shown by “As a result”", "cause/effect"), SA("Relationship shown by “However”", "contrast"), SA("Relationship shown by “Despite this injustice”", "contrast (concession)"),
    SA("Overall structure of paragraph 1", "cause/effect (chronological)"), SA("Topic sentence of paragraph 2", "However, success had a cost."),
    OR("Write a sentence about jazz using an example transition.", "Answers vary.", lines=2)], cols=1, passage=P_C26)], minutes=20)
C3 = Check("Weekly Check 27: Revising an Argument", [S("Read the draft and answer", [
    SA("Which sentence is irrelevant?", "My cousin plays drums."), SA("What's wrong with paragraph 2's transitions?", "“Also” repeated; imprecise"),
    OR("Write a stronger claim.", "Answers vary; previews reasons.", lines=2), OR("Rewrite the counterclaim and rebuttal.", "Answers vary.", lines=3)], cols=1, passage=P_DRAFT)], minutes=20)

REVIEW = Check("Year-End Review", [
    S("Read: Lanterns on the Hill", [SA("Theme", "Love and connection outlast loss."), SA("Tone of the last paragraph", "hopeful, tender"), SA("What does the lantern symbolize?", "connection, presence, remembering"),
                                     SA("Point of view", "first person")], cols=1, passage=P_YE1),
    S("Read: Should Cities Turn Down the Lights?", [SA("Claim", "Cities should reduce light pollution."), SA("Counterclaim", "Lighting helps people feel safe."), SA("Rebuttal", "Shielded, motion-sensor, dimmer lights can keep streets safe."),
                                                   SA("Structure of the last paragraph", "problem/solution")], cols=1, passage=P_YE2),
    S("Language", [SA("Type: Because it rained, we stayed in.", "complex"), SA("Punctuate: We packed three things water maps and snacks.", "three things: water, maps, and snacks."),
                   SA("Fix: The box of books are heavy.", "is heavy"), SA("<i>chronological</i> root", "chron: time"), SA("Formal: The ending was kind of cool.", "The ending was effective.")], cols=1)],
    kind="review", minutes=50, teacher_note="Spread over the week as homework or use as a study session before the Year-End Test.")

TEST = make_test("Grade 7 ELA Year-End Test", [
    S("Part A · Literature: The Quilt (1 point each unless noted)", [
        MC("Why is the quilt important to the family?", ["It is very expensive.", "It is made from clothing of four generations.", "It won a prize.", "It is the narrator's school project."], 1),
        SA("What does the simile “wandered like lost ants” suggest about the narrator's stitches?", "They were crooked and uneven; the narrator was inexperienced."),
        MC("Why does Aunt Bea push the needle and thread toward the narrator?", ["She is angry.", "She wants the narrator to carry on the family work.", "She wants to stop sewing forever.", "She needs a new needle."], 1),
        OR("State the theme and support it with two pieces of evidence.", "e.g. Family memory and love are passed down through generations. Evidence: squares from four generations; Aunt Bea teaches the narrator to finish it; “a map of everyone who had ever loved me.”", lines=4, points=3),
        SA("What does the quilt symbolize at the end?", "family love and memory; the family's history"),
        SA("Why does the author include the moment when “the only sound was the clock ticking”?", "creates tension/sadness; suggests time running out for Aunt Bea")], passage=P_T1),
    S("Part B · Informational argument: Should School Start Later? (1 point each unless noted)", [
        SA("State the author's claim.", "Schools should start later."),
        OR("Identify two reasons and the evidence for each.", "Teens' internal clocks shift (AAP 2014 recommendation of 8:30 a.m.); tired students struggle (trouble paying attention and remembering).", lines=3, points=2),
        SA("What counterclaim does the author acknowledge?", "Later start times make buses, sports, and jobs harder to schedule."),
        SA("How does the author rebut it?", "Schools that changed have found ways to adjust; the benefits are worth it."),
        MC("Which transition signals contrast in the last paragraph?", ["First", "Second", "However", "Also"], 2),
        SA("What does “internal clock” mean in context?", "the body's natural schedule for sleeping and waking"),
        SA("Is the evidence that sleepy students are grumpier strong or weak? Why?", "weak; the author says some people “believe” it and it is “harder to measure,” with no data")], passage=P_T2),
    S("Part C · Language (1 point each)", [
        SA("Type: Although the trail was steep, we kept climbing, and we reached the top.", "compound-complex"),
        SA("Fix the misplaced modifier: Barking loudly, the mail carrier ran from the dog.", "The mail carrier ran from the dog, which was barking loudly."),
        SA("Punctuate: The guests were doubtful however the narrator wondered.", "The guests were doubtful; however, the narrator wondered."),
        SA("Format: the novel The Time Machine and the poem We Wear the Mask", "The Time Machine (italics); “We Wear the Mask”"),
        SA("Choose: The ending (affected/effected) me deeply.", "affected"),
        SA("<i>incredible</i>: prefix, root, meaning", "in- (not) + cred (believe): unbelievable"),
        SA("Connotation: Which is more positive, <i>curious</i> or <i>nosy</i>?", "curious"),
        SA("Fix the comma splice: Ariel freed the prisoners, Prospero forgave them.", "e.g. Ariel freed the prisoners, and Prospero forgave them.")], cols=1),
    S("Part D · Write (6 points)", [OR("Choose one: (1) Argue whether your school should start later, using evidence from the article and a counterclaim; or (2) Analyze how the author of “The Quilt” uses the quilt to develop the theme. Write 2–3 well-organized paragraphs.",
                                       "Rubric: clear claim (1); relevant evidence from the text (2); explanation/analysis (1); organization and transitions (1); conventions and formal style (1).", lines=20, points=6)])],
    minutes=60, labels=["Ready for Grade 8 ELA.", "Ready; review missed skills over the summer.", "Plan targeted summer review before Grade 8."])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-06-21", "2027-06-28", "2027-07-05", "2027-07-12"], CHECKS, REVIEW, TEST)

UNIT = Unit(9, "Capstone: Style, Revision, and Reflection", "Style and tone, transitions and organization, revising arguments, and a portfolio review, with The Genius of the Harlem Renaissance Reader.",
    "In this final unit, you'll study how Langston Hughes, Georgia Douglas Johnson, and Elise Johnson McDougald shaped their words, and you'll shape your own: developing voice, organizing ideas, and revising an argument. You'll finish by gathering your best work, reflecting on how far you've come, and showing what you know on the Year-End Test.",
    ["Analyze style, tone, and mood, and compare styles across time.", "Use transitions and text structures to write cohesive paragraphs.", "Revise arguments for claims, counterclaims, and cited evidence.", "Assemble, reflect on, and present a writing portfolio."],
    [("RL.7.2–9", "Theme; word choice and tone; structure; comparing texts."), ("RI.7.2–8", "Central ideas; structure; evaluating arguments."), ("W.7.1–2, W.7.5", "Arguments; informational writing; revision."), ("SL.7.4", "Presenting."), ("L.7.1–6", "Cumulative review.")],
    [("style", "A writer's distinctive use of language."), ("tone", "The writer's attitude."), ("mood", "The reader's feeling."), ("transition", "A word showing how ideas connect."), ("rebuttal", "A response to a counterclaim."), ("portfolio", "A collection of best work with reflections.")],
    ["Unit 7: Harlem Renaissance background.", "Unit 8: conventions and formal style."], ["The Genius of the Harlem Renaissance Reader", "Portfolio folder with the year's writing"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Every strong writer revises; reflecting on your growth helps you set goals for next year.",
    family_note="Attend your student's portfolio presentation in the final week and celebrate a year of reading and writing.",
    weeks=WEEKS)
