"""Grade 7 ELA · Unit 7: Voices of the Harlem Renaissance — comparing sources and claims, evaluating evidence, integrating sources, research, and synthesis.
Anchor reading: The Genius of the Harlem Renaissance Reader (Apr 26 – May 21, 2027)."""
from engine import *
from content.elakit import S, MC, OR, SA, DRAW, te, make_test
from content.sched import schedule

HR = "The Genius of the Harlem Renaissance Reader"

# ================================================================= passages
P_INTRO = Passage("The Harlem Renaissance", [
    "In the 1920s and early 1930s, the New York City neighborhood of Harlem became the center of an extraordinary flowering of African American art, music, literature, and ideas. This movement is now called the <b>Harlem Renaissance</b>. <i>Renaissance</i> means “rebirth.”",
    "Writers such as Langston Hughes, Zora Neale Hurston, Claude McKay, Countee Cullen, and Georgia Douglas Johnson published poems, stories, and novels that celebrated Black life and challenged racism. Musicians such as Duke Ellington and Louis Armstrong helped make jazz one of the most important art forms in America. Painters such as Aaron Douglas created bold images inspired by African art and modern design.",
    "The movement grew out of the Great Migration, as hundreds of thousands of Black Southerners moved to Northern cities in search of opportunity. In Harlem, writers, thinkers, and artists found one another, and magazines and newspapers gave them places to publish.",
    "The Harlem Renaissance did not end racism or segregation. But it changed how many Americans saw Black artists and how Black Americans expressed their own identity, and its influence can still be heard and read today.",
], source="An original informational text", genre="Informational text")

P_LANG = Passage("A Note on Historical Language", [
    "Texts from the early 1900s, including titles such as <i>The New Negro</i>, use the word <i>Negro</i>. At that time, it was the respectful, standard term, and Black writers and organizations used it themselves; it was often capitalized as a sign of dignity. Today it is considered outdated, and most people say <i>Black</i> or <i>African American</i>.",
    "When you quote or name historical works, use their original titles and words exactly. When you write in your own voice, use current, respectful terms. Understanding why language changes is part of understanding history.",
], source="An original note for readers", genre="Informational text")

P_MASK = Passage("We Wear the Mask", [
    "> We wear the mask that grins and lies,\\nIt hides our cheeks and shades our eyes,—\\nThis debt we pay to human guile;\\nWith torn and bleeding hearts we smile,\\nAnd mouth with myriad subtleties.",
    "> Why should the world be over-wise,\\nIn counting all our tears and sighs?\\nNay, let them only see us, while\\n        We wear the mask.",
    "> We smile, but, O great Christ, we cry\\nTo thee from tortured souls arise.\\nWe sing, but oh the clay is vile\\nBeneath our feet, and long the mile;\\nBut let the world dream otherwise,\\n        We wear the mask!",
], source="Paul Laurence Dunbar (1895). Public domain.", genre="Poem", numbered=False)

P_DUNBAR_A = Passage("Source A: A Voice Ahead of His Time", [
    "Paul Laurence Dunbar (1872–1906), the son of formerly enslaved parents, became one of the first African American poets to win national fame. Though he is often remembered for poems written in dialect, much of his most powerful work, such as “We Wear the Mask” and “Sympathy,” is written in standard English and expresses the pain of living under racism. Many Harlem Renaissance writers saw Dunbar as an important forerunner.",
], source="An original informational text", genre="Source A", numbered=False)
P_DUNBAR_B = Passage("Source B: Fame and Its Limits", [
    "During his lifetime, Paul Laurence Dunbar's popularity with white audiences rested largely on his dialect poems, which some readers enjoyed as humorous portraits of plantation life. Dunbar himself was frustrated that critics praised these poems while overlooking his serious work. Some later writers criticized dialect poetry for reinforcing stereotypes, while others argued that Dunbar used it with skill and affection for Black speech.",
], source="An original informational text", genre="Source B", numbered=False)

P_MIGRATION = Passage("The Great Migration", [
    "Between about 1910 and 1970, roughly six million African Americans left the rural South and moved to cities in the North, Midwest, and West. Historians call this movement the <b>Great Migration</b>. In its first wave, from about 1910 to 1940, more than a million and a half people made the journey.",
    "People left for many reasons. In the South, Jim Crow laws enforced segregation and denied Black citizens the right to vote. Violence, including lynching, terrorized communities. Many families worked as sharecroppers, renting land and paying with a share of their crops, a system that often kept them in debt. Around 1915, an insect called the boll weevil destroyed cotton crops across the region.",
    "At the same time, Northern cities offered new possibilities. When World War I began, factories needed workers, and immigration from Europe slowed. Black newspapers such as the <i>Chicago Defender</i> published job listings and encouraged readers to come north.",
    "Life in the North was not free of racism. Migrants faced discrimination in housing and jobs, and some cities saw violent attacks. Still, many found better wages, better schools for their children, and the chance to vote. In neighborhoods like Harlem in New York and the South Side of Chicago, new communities formed, and their energy helped fuel the Harlem Renaissance.",
], source="An original informational text based on historical facts", genre="Informational text")

P_JOHNSON = Passage("Charles S. Johnson: Building a Movement", [
    "Charles S. Johnson was a sociologist, a scientist who studies how societies work. In 1923 he became the founding editor of <i>Opportunity</i>, the magazine of the National Urban League. Johnson believed that art and literature could change how Americans thought about race, and he used <i>Opportunity</i> to publish young Black writers and to award prizes for their work.",
    "In 1924, Johnson organized a dinner at the Civic Club in New York, bringing together Black writers and white editors and publishers. Many historians see this event as a turning point: within a year, major magazines and publishing houses were seeking out Black writers. Johnson later became the first Black president of Fisk University, in 1946.",
], source="An original informational text based on historical facts", genre="Informational text")

P_PRESS = Passage("The Black Press", [
    "In the early twentieth century, mainstream newspapers often ignored or misrepresented Black communities. In response, Black journalists built their own press.",
    "The <i>Chicago Defender</i>, founded by Robert S. Abbott in 1905, became one of the most widely read Black newspapers in the country. Railroad porters carried copies south, where they were passed from hand to hand. <i>The Crisis</i>, the magazine of the NAACP edited by W. E. B. Du Bois, began in 1910 and published essays, news, and poetry, including early work by Langston Hughes.",
    "Journalists such as J. A. Rogers, a Jamaican-born writer who wrote for the <i>Pittsburgh Courier</i>, researched and published the achievements of people of African descent throughout history, challenging claims that Black people had no history worth studying.",
    "The Black press informed readers, organized communities, and gave Harlem Renaissance writers a place to be heard. Without it, the movement might never have reached a national audience.",
], source="An original informational text based on historical facts", genre="Informational text")

P_LOCKE = Passage("Alain Locke and The New Negro", [
    "In March 1925, the magazine <i>Survey Graphic</i>, edited by Paul Kellogg, published a special issue devoted to Harlem. Its guest editor was Alain Locke, a philosopher at Howard University and the first African American Rhodes Scholar.",
    "Later that year, Locke expanded the issue into a book, <i>The New Negro: An Interpretation</i>. It gathered essays, fiction, poetry, and art by many of the movement's leading figures.",
    "In his essays, Locke argued that a new spirit of pride, self-respect, and creativity was rising among Black Americans, especially young people in cities. He believed that through art and literature, Black Americans could define themselves rather than be defined by others' stereotypes.",
    "Not everyone agreed with Locke's emphasis on art. Some leaders argued that political and economic action, such as fighting for voting rights and better jobs, mattered more. The debate itself shows how many voices the Harlem Renaissance included.",
], source="An original informational text based on historical facts", genre="Informational text")

P_C19A = Passage("Source A: Jazz Comes North", [
    "Jazz was born in New Orleans in the early 1900s. As musicians joined the Great Migration, they carried jazz north to Chicago and New York, where it flourished in clubs and dance halls during the 1920s.",
], source="An original informational text", genre="Source A", numbered=False)
P_C19B = Passage("Source B: The Sound of a City", [
    "To many listeners in the 1920s, jazz was the sound of the modern city: fast, inventive, and free. Some critics at the time dismissed it as noise, but by the end of the decade, jazz had become one of America's most popular forms of music.",
], source="An original informational text", genre="Source B", numbered=False)

P_C20 = Passage("Why We Should Study the Harlem Renaissance", [
    "Every middle school should teach the Harlem Renaissance. First, its writers created some of the most important poems in American literature; Langston Hughes's work is read around the world. Second, studying the period helps students understand how art can respond to injustice. Third, it's really interesting, and everyone I know loves jazz.",
], source="An original argument paragraph", genre="Argument", numbered=False)

P_C21 = Passage("Zora Neale Hurston", [
    "Zora Neale Hurston grew up in Eatonville, Florida, one of the first all-Black towns to be incorporated in the United States. She studied anthropology and traveled through the South collecting folktales, songs, and stories. Her 1937 novel <i>Their Eyes Were Watching God</i> is now considered a classic of American literature, though it was out of print for years before writers and scholars revived interest in it in the 1970s.",
], source="An original informational text", genre="Informational text", numbered=False)

P_TEST_A = Passage("Source A: Langston Hughes, Poet of the People", [
    "Langston Hughes (1901–1967) became one of the most famous writers of the Harlem Renaissance. His poem “The Negro Speaks of Rivers,” published in <i>The Crisis</i> in 1921 when he was still a teenager, connects Black Americans to ancient rivers such as the Euphrates, the Congo, and the Nile.",
    "Hughes wanted to write about ordinary people: workers, musicians, and families. He used the rhythms of blues and jazz in his poetry so that his poems sounded like the music of Harlem.",
], source="An original informational text", genre="Source A")
P_TEST_B = Passage("Source B: A Divided Reception", [
    "When Langston Hughes published his second book of poems in 1927, many reviewers in the Black press criticized it harshly. They argued that his poems about working-class life and blues singers presented an unflattering picture of Black Americans to white readers.",
    "Hughes defended his choices. In a famous 1926 essay, “The Negro Artist and the Racial Mountain,” he argued that Black artists should express themselves freely and honestly, without worrying about pleasing either white or Black audiences. Today, many critics consider that book among his best work.",
], source="An original informational text", genre="Source B")

# ================================================================= Week 1 · Compare sources and claims
L1 = Lesson("7.1", "Entering the Harlem Renaissance",
    "I can explain the historical context of the Harlem Renaissance and discuss historical language respectfully.", "RI.7.2, RI.7.3",
    [("renaissance", "A rebirth or revival, especially of art and learning."), ("historical context", "The time, place, and events surrounding a text.")],
    "What do you already know about jazz, Harlem, or the 1920s?",
    [ReaderAssign(HR, "Language of race (historical language in context) and the introduction", "Why does the Reader begin with a note about language? What was Harlem like in the 1920s?"),
     P_INTRO, P_LANG,
     KeyIdea("Understand the historical context before analyzing texts; quote historical language accurately and write in current, respectful terms.")],
    [Problem("What does renaissance mean?", "rebirth"), Problem("Name two writers and one musician of the movement.", "e.g. Langston Hughes, Zora Neale Hurston; Duke Ellington"), Problem("What movement helped create the Harlem Renaissance?", "the Great Migration")],
    [S("Warm-Up", [SA("Harlem is in…", "New York City"), SA("Decade of the Harlem Renaissance", "1920s")], cols=2),
     S("Context", [OR("State the central idea of “The Harlem Renaissance.” Cite two details.", "A flowering of Black art, music, literature, and ideas centered in 1920s Harlem; Hughes, Hurston; jazz; Aaron Douglas.", lines=4),
                   OR("Why does the Reader include a note about historical language? How will you handle it in your writing?", "Older texts use terms that were standard then but outdated now; quote accurately, write in current respectful terms.", lines=3),
                   OR("According to the passage, what did the movement change, and what didn't it change?", "Changed how Americans saw Black artists and how Black Americans expressed identity; did not end racism or segregation.", lines=3)], passage=P_INTRO),
     S("Exit Ticket", [OR("Write one question you hope to answer during this unit.", "Answers vary.", lines=2)])],
    te("Students build historical context.", "Determine central ideas; analyze interactions among individuals, events, and ideas.", "Harlem Renaissance Reader (introduction, language note), workbook Lesson 7.1",
       "What do you know?", ["Read the Reader's language note and introduction.", "Read “The Harlem Renaissance.”"], ["Discuss historical language thoughtfully and respectfully."], "Your Turn 1–3.",
       ["Avoiding the topic of racism, which is central to the period."], ["Context timeline."], ["Listen to a 1920s jazz recording."]),
    summary="Context first; quote historical language accurately, write respectfully.")

L2 = Lesson("7.2", "Analyzing a Poem: Dunbar's “We Wear the Mask”",
    "I can analyze how a poem's form, imagery, and figurative language develop its meaning.", "RL.7.4, RL.7.5, RL.7.2",
    [("extended metaphor", "A metaphor developed throughout a work."), ("refrain", "A repeated line or phrase in a poem."), ("rondeau", "A French poetic form with fifteen lines, two rhymes, and a refrain.")],
    "Have you ever smiled when you didn't feel like smiling? Why?",
    [ReaderAssign(HR, "Literary tradition and Paul Laurence Dunbar", "What did Dunbar write about? How did later writers view him?"),
     P_MASK,
     Example("Analyze the extended metaphor", "What is “the mask”?", ["Literal: a face covering.", "Figurative: the cheerful appearance Black Americans were forced to show to survive racism.", "Evidence: “grins and lies,” “torn and bleeding hearts we smile.”"],
             "The mask is an extended metaphor for hiding pain behind a smile in a hostile society."),
     Text("Dunbar uses the <b>rondeau</b>, a strict European form, with the refrain “We wear the mask.” Some readers see the controlled form itself as another mask over intense emotion."),
     KeyIdea("Analyze extended metaphors, refrains, and form to understand a poem's meaning.")],
    [Problem("What does “guile” mean?", "deceit, trickery"), Problem("What is the refrain?", "“We wear the mask”"), Problem("Why does the speaker say the world should not be “over-wise”?", "The world shouldn't see their suffering; they choose to hide it.")],
    [S("Warm-Up", [SA("A refrain is…", "a repeated line"), SA("Year the poem was published", "1895")], cols=2),
     S("Analyze the Poem", [OR("Identify two contrasts in the poem (outside vs inside). Explain their effect.", "smile/torn and bleeding hearts; sing/clay is vile: shows the gap between appearance and suffering.", lines=4),
                            OR("How does the final refrain (with an exclamation point) differ from the earlier one?", "It sounds more forceful and defiant.", lines=2),
                            OR("State the poem's theme.", "People facing oppression may hide their pain to survive; appearances can conceal deep suffering.", lines=2)], passage=P_MASK),
     S("Exit Ticket", [OR("Connect this poem to the theme of duality from Jekyll and Hyde. How are the ideas similar and different?", "Both involve a hidden self; Dunbar's mask is imposed by oppression, while Jekyll chose to split himself.", lines=3)])],
    te("Students analyze a poem.", "Analyze impact of rhymes, repetition, and form on meaning; determine theme.", "Harlem Renaissance Reader (Dunbar section), workbook Lesson 7.2",
       "Smiling when you don't feel like it.", ["Read the Reader's Dunbar section.", "Read the poem aloud twice."], ["Model the extended metaphor."], "Your Turn 1–3.",
       ["Reading the mask literally."], ["Outside/inside chart."], ["Memorize the poem."]),
    summary="Extended metaphor, refrain, and form create meaning.")

L3 = Lesson("7.3", "Comparing Sources: How Authors Shape Information",
    "I can analyze how two authors writing about the same topic emphasize different evidence or interpretations.", "RI.7.9, RI.7.6",
    [("interpretation", "An explanation of what facts mean.")],
    "Can two accurate sources give different impressions of the same person?",
    [P_DUNBAR_A, P_DUNBAR_B,
     Figure(lambda t: table(t, [["", "Source A", "Source B"], ["Focus", "Dunbar's serious standard-English poems", "his popularity and the dialect poems"], ["Interpretation", "a pioneering, powerful voice", "a poet whose fame was limited by audience expectations"],
                                ["Shared facts", "Dunbar became famous; wrote dialect and standard poems", "Dunbar became famous; wrote dialect and standard poems"]], [1.1 * inch, 2.3 * inch, 2.3 * inch], width=5.7 * inch, font_size=9)),
     KeyIdea("Accurate sources can differ in focus and interpretation; compare what each emphasizes and why.")],
    [Problem("What does Source A emphasize?", "his serious poems and influence"), Problem("What does Source B emphasize?", "his popularity with white audiences, dialect poems, and debate over them"), Problem("Do the sources contradict each other?", "No; they emphasize different aspects.")],
    [S("Warm-Up", [SA("Interpretation =", "an explanation of what facts mean"), SA("Dunbar's lifespan", "1872–1906")], cols=2),
     S("Compare", [OR("What fact do both sources share?", "Dunbar wrote both dialect and standard-English poems and became famous.", lines=2),
                   OR("How does each author shape the reader's view of Dunbar?", "A presents him as a powerful pioneer; B presents his fame as complicated and limited by audience expectations.", lines=3),
                   OR("Why is it valuable to read both sources?", "Together they give a fuller, more balanced picture.", lines=2)]),
     S("Exit Ticket", [OR("Which source would you cite to argue Dunbar was a forerunner of the Harlem Renaissance? Why?", "Source A; it directly states Harlem writers saw him as a forerunner.", lines=2)])],
    te("Students compare how sources shape information.", "Analyze how two authors writing about the same topic shape their presentations by emphasizing different evidence or interpretations.", "Workbook Lesson 7.3",
       "Same person, different impressions.", "Read Sources A and B.", ["Model the comparison chart."], "Your Turn 1–3.",
       ["Assuming one source is wrong."], ["Focus/interpretation chart."], ["Compare two biographies of a famous person."]),
    summary="Sources can share facts but differ in focus and interpretation.")

L4 = Lesson("7.4", "Comparing Claims Across Sources",
    "I can trace and compare claims across sources and decide which is better supported.", "RI.7.8, RI.7.9",
    [],
    "If two sources disagree, how do you decide which to trust?",
    [Text("To compare claims: identify each claim, list the evidence for each, and evaluate whether the evidence is relevant and sufficient. Consider the author's purpose and expertise."),
     Example("Compare claims", "Claim 1: Dialect poems reinforced stereotypes. Claim 2: Dunbar used dialect with skill and affection.", ["Both appear in Source B as views held by different critics.", "Evidence needed: examples of the poems, Dunbar's own statements, audience responses.", "Conclusion: both views have supporters; more evidence is needed to decide."],
             "A careful reader notes that the source reports a debate rather than settling it."),
     KeyIdea("Identify claims, weigh evidence, consider authors, and acknowledge debates that sources don't settle.")],
    [Problem("What two claims about dialect does Source B report?", "It reinforced stereotypes / Dunbar used it with skill and affection"), Problem("What evidence would help decide?", "the poems themselves, Dunbar's statements, historical reactions"), Problem("Should you choose a side without enough evidence?", "No; acknowledge the debate")],
    [S("Warm-Up", [SA("A claim is…", "an arguable statement"), SA("Sufficient evidence means…", "enough to convince")], cols=2),
     S("Evaluate", [OR("Claim: “We Wear the Mask” is a protest poem. Find two pieces of evidence in the poem that support it.", "“grins and lies,” “torn and bleeding hearts,” “tortured souls,” “let the world dream otherwise”", lines=3),
                    OR("A classmate claims Dunbar only wrote humorous dialect poems. Use both sources and the poem to respond.", "That's inaccurate; Source A names serious standard-English poems like “We Wear the Mask,” and the poem itself shows serious protest.", lines=4)]),
     S("Exit Ticket", [OR("What is one question about Dunbar you'd research further?", "Answers vary.", lines=2)])],
    te("Students compare and evaluate claims.", "Trace and evaluate the argument and claims; compare texts.", "Workbook Lesson 7.4",
       "Disagreeing sources.", "Review Sources A and B and the poem.", ["Model claim comparison."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Picking the source they like better."], ["Claim-evidence chart."], ["Read Dunbar's “Sympathy.”"]),
    summary="Weigh claims by evidence; acknowledge unsettled debates.")

# ================================================================= Week 2 · Evaluate reasons and evidence (Great Migration, Charles S. Johnson)
L5 = Lesson("7.5", "The Great Migration: Causes and Effects",
    "I can analyze the causes and effects of a historical movement using evidence.", "RI.7.3, RI.7.1",
    [("push factor", "A reason that drives people away from a place."), ("pull factor", "A reason that attracts people to a place."), ("Jim Crow laws", "Laws that enforced racial segregation in the South.")],
    "What would make a family leave everything behind to move hundreds of miles?",
    [ReaderAssign(HR, "The Great Migration and Charles S. Johnson", "Why did people leave the South? How did Johnson help writers?"),
     P_MIGRATION,
     Figure(lambda t: table(t, [["Push factors (South)", "Pull factors (North)"], ["Jim Crow segregation; denied voting", "factory jobs (World War I)"], ["violence and lynching", "better wages"], ["sharecropping debt", "better schools; right to vote"],
                                ["boll weevil destroyed cotton", "Black newspapers encouraging migration"]], [2.8 * inch, 2.8 * inch], width=5.6 * inch)),
     KeyIdea("Historical movements have multiple causes (push and pull) and multiple effects.")],
    [Problem("About how many people moved in the whole Great Migration?", "about six million"), Problem("What is sharecropping?", "renting land and paying with a share of crops"), Problem("Name one effect on Northern cities.", "new Black communities such as Harlem; cultural energy for the Harlem Renaissance")],
    [S("Warm-Up", [SA("Push factor =", "drives people away"), SA("Pull factor =", "attracts people")], cols=2),
     S("Causes and Effects", [OR("Explain two push factors and two pull factors with evidence.", "Answers vary from the chart and passage.", lines=4),
                              OR("Was the North a promised land? Use evidence from paragraph 4.", "Not entirely: discrimination in housing and jobs and violence, though many found better wages, schools, and voting rights.", lines=3),
                              OR("Explain how the Great Migration helped cause the Harlem Renaissance.", "It brought many Black Americans to cities like Harlem, where artists and writers formed communities and found publishers.", lines=3)], passage=P_MIGRATION),
     S("Exit Ticket", [OR("Which factor do you think mattered most? Explain.", "Answers vary.", lines=2)])],
    te("Students analyze causes and effects.", "Analyze interactions between individuals, events, and ideas.", "Harlem Renaissance Reader (Great Migration, Johnson), workbook Lesson 7.5",
       "Leaving everything.", ["Read the Reader section.", "Read “The Great Migration.”"], ["Model push/pull."], "Your Turn 1–3.",
       ["One-cause explanations."], ["Push/pull chart."], ["Interview a relative about a family move."]),
    summary="Push and pull factors; multiple causes and effects.")

L6 = Lesson("7.6", "Evaluating Reasons and Evidence",
    "I can evaluate whether an author's reasoning is sound and evidence is relevant and sufficient.", "RI.7.8",
    [("sound reasoning", "Logic that clearly connects evidence to a claim."), ("anecdote", "A brief personal story used as evidence.")],
    "Is “everyone I know loves jazz” good evidence?",
    [P_JOHNSON,
     Example("Evaluate a claim", "Claim: Charles S. Johnson helped launch the Harlem Renaissance.", ["Evidence 1: founded and edited Opportunity; published young writers; gave prizes. (relevant)", "Evidence 2: organized the 1924 Civic Club dinner; publishers sought Black writers within a year. (relevant, specific)", "Reasoning: connecting writers to publishers expanded their audience. (sound)"],
             "The claim is well supported by relevant, specific evidence and sound reasoning."),
     Figure(lambda t: table(t, [["Strong evidence", "Weak evidence"], ["specific facts, dates, statistics", "vague generalizations"], ["expert sources", "unsupported opinions"], ["relevant to the claim", "off-topic details"],
                                ["enough to convince", "a single anecdote"]], [2.8 * inch, 2.8 * inch], width=5.6 * inch)),
     KeyIdea("Evaluate relevance, sufficiency, and reasoning; watch for vague or unsupported evidence.")],
    [Problem("What magazine did Johnson edit?", "Opportunity"), Problem("Why was the Civic Club dinner important?", "It connected Black writers with white editors and publishers."), Problem("Is “everyone I know loves jazz” strong evidence?", "No; it's vague and anecdotal.")],
    [S("Warm-Up", [SA("Relevant =", "connected to the claim"), SA("Sufficient =", "enough to convince")], cols=2),
     S("Evaluate", [OR("Is the claim that Johnson helped launch the movement well supported? Explain using the criteria.", "Yes; specific relevant facts (Opportunity, prizes, 1924 dinner, publishers' interest) and sound reasoning.", lines=4),
                    OR("What additional evidence would make the claim even stronger?", "e.g. names of writers whose careers began through Opportunity; publishing data after 1924", lines=3)], passage=P_JOHNSON),
     S("Exit Ticket", [OR("Write one strong and one weak piece of evidence for: “Jazz changed American music.”", "Answers vary.", lines=2)])],
    te("Students evaluate reasons and evidence.", "Trace and evaluate argument; assess whether reasoning is sound and evidence relevant and sufficient.", "Workbook Lesson 7.6",
       "Everyone loves jazz?", "Read the Johnson passage.", ["Model evaluation."], "Your Turn 1–3.",
       ["Accepting any fact as strong evidence."], ["Evidence checklist."], ["Evaluate an online claim."]),
    summary="Evidence must be relevant, sufficient, and soundly connected.")

L7 = Lesson("7.7", "Comparing Text and Data",
    "I can compare information in a text with information in a chart or graph.", "RI.7.7",
    [],
    "What can numbers show that words can't?",
    [Figure(lambda t: bar_graph(t, ["1910", "1920", "1930", "1940"], [44, 110, 234, 278], title="Chicago's Black Population (thousands, rounded)", ylabel="thousands", step=50, height=180),
            caption="Approximate figures from U.S. Census counts, rounded to the nearest thousand."),
     Example("Compare text and graph", "How does the graph support “The Great Migration”?", ["Text: more than a million and a half people moved in the first wave.", "Graph: Chicago's Black population grew from about 44,000 to about 278,000 between 1910 and 1940."],
             "The graph shows one city's dramatic growth, making the text's general claim concrete."),
     KeyIdea("Compare what a text says with what data shows; explain how each adds to understanding.")],
    [Problem("About how much did the population grow from 1910 to 1940?", "about 234,000"), Problem("Which decade saw the biggest increase?", "1920–1930"), Problem("What does the graph add to the text?", "specific numbers for one city")],
    [S("Warm-Up", [SA("Population in 1920 (thousands)", "about 110"), SA("Population in 1940 (thousands)", "about 278")], cols=2),
     S("Analyze", [SA("About how many times larger in 1930 than in 1910?", "about 5 times (234 ÷ 44 ≈ 5.3)"), SA("Increase from 1910 to 1920 (thousands)", "about 66"),
                   OR("What limitation does the graph have compared with the text?", "It shows one city and numbers only, not reasons, experiences, or the whole country.", lines=2),
                   OR("Write two sentences integrating the text and the graph.", "e.g. The Great Migration reshaped Northern cities. In Chicago alone, the Black population grew from about 44,000 in 1910 to about 278,000 in 1940.", lines=3)], cols=1),
     S("Exit Ticket", [OR("What question does the graph raise that the text doesn't answer?", "Answers vary.", lines=2)])],
    te("Students compare text and data.", "Compare a text to a visual or quantitative presentation, analyzing each medium's portrayal.", "Workbook Lesson 7.7",
       "Numbers vs words.", "Read the graph carefully.", ["Model integration."], "Your Turn 1–3.",
       ["Reading bars without the scale."], ["Read title, axes, and caption first."], ["Graph Harlem's population changes."]),
    summary="Data makes general claims concrete; text explains why.")

L8 = Lesson("7.8", "Writing an Argument with Strong Evidence",
    "I can write an argument paragraph supported by relevant, sufficient evidence and sound reasoning.", "W.7.1a, W.7.1b",
    [],
    "What was the most important cause of the Great Migration?",
    [Text("An argument states a <b>claim</b>, supports it with <b>relevant, sufficient evidence</b> from credible sources, explains with <b>sound reasoning</b>, and acknowledges a <b>counterclaim</b>."),
     Example("Argument paragraph", "Claim: Economic opportunity was the strongest pull factor.", ["Evidence: wartime factories needed workers; better wages.", "Data: Chicago's population grew fivefold.", "Counterclaim: escaping violence and Jim Crow mattered greatly too.", "Rebuttal: these pushed people out, but jobs determined where they went."],
             "A paragraph that weighs causes and supports a claim with evidence."),
     KeyIdea("Claim, relevant and sufficient evidence, reasoning, and a counterclaim with rebuttal.")],
    [Problem("Name the four parts.", "claim, evidence, reasoning, counterclaim/rebuttal"), Problem("Why include a counterclaim?", "to show fairness and strengthen the argument"), Problem("Where can evidence come from in this unit?", "the Reader, the Great Migration text, the graph")],
    [S("Warm-Up", [SA("Counterclaim =", "opposing view"), SA("Rebuttal =", "response to the counterclaim")], cols=2),
     S("Write", [OR("Argue: What was the most important cause of the Great Migration? Write an argument paragraph with at least two pieces of evidence and a counterclaim.", "Answers vary.", lines=14,
                    note="Score: claim (1); evidence (2); reasoning (1); counterclaim and rebuttal (1).")])],
    te("Students write argument paragraphs.", "Introduce claims, acknowledge alternate claims, support with logical reasoning and relevant evidence.", "Workbook Lesson 7.8",
       "Most important cause.", "Review evidence.", ["Model the paragraph."], "Plan.",
       ["Listing causes without arguing."], ["Claim frame."], ["Debate with a family member."], independent="Write. Weekly Check tomorrow."),
    summary="Argue with evaluated evidence and a counterclaim.")

# ================================================================= Week 3 · Long-passage source integration (Harlem, the Black press, J. A. Rogers)
L9 = Lesson("7.9", "The Black Press and Long-Passage Analysis",
    "I can analyze how a long informational text develops central ideas through key individuals and events.", "RI.7.2, RI.7.3",
    [("mainstream", "Belonging to the dominant or most widely accepted group.")],
    "Why would a community build its own newspapers?",
    [ReaderAssign(HR, "Harlem, the Black press, and J. A. Rogers", "What role did newspapers and magazines play? What did J. A. Rogers write about?"),
     P_PRESS,
     Example("Trace ideas through individuals", "How do the individuals develop the central idea?", ["Abbott: built a national newspaper that spread news and encouraged migration.", "Du Bois: published essays and poetry, including Hughes.", "Rogers: researched and published Black history."],
             "Each individual shows a different way the Black press gave Black Americans a voice."),
     KeyIdea("Trace how key individuals and events develop central ideas across a long text.")],
    [Problem("Who founded the Chicago Defender?", "Robert S. Abbott (1905)"), Problem("Who edited The Crisis?", "W. E. B. Du Bois"), Problem("What did J. A. Rogers challenge?", "claims that Black people had no history worth studying")],
    [S("Warm-Up", [SA("Mainstream =", "dominant, widely accepted"), SA("Year The Crisis began", "1910")], cols=2),
     S("Analyze", [OR("State the central idea of “The Black Press.”", "Black journalists built their own press to inform, organize, and give voice to Black communities and writers.", lines=2),
                   OR("How did railroad porters help the Defender?", "They carried copies south, spreading news and job information.", lines=2),
                   OR("How does the final paragraph connect the Black press to the Harlem Renaissance?", "It gave writers a place to publish and a national audience.", lines=3)], passage=P_PRESS),
     S("Exit Ticket", [OR("Why does the author include three different individuals?", "to show different contributions and develop the central idea fully", lines=2)])],
    te("Students analyze long informational texts.", "Determine central ideas; analyze interactions of individuals and events.", "Harlem Renaissance Reader (Black press, Rogers), workbook Lesson 7.9",
       "Own newspapers.", ["Read the Reader section.", "Read “The Black Press.”"], ["Model tracing individuals."], "Your Turn 1–3.",
       ["Listing people without connecting to ideas."], ["Person → contribution → idea chart."], ["Look at a digitized 1920s newspaper page."]),
    summary="Key individuals develop central ideas.")

L10 = Lesson("7.10", "Quoting, Paraphrasing, and Citing Sources",
    "I can quote and paraphrase sources accurately and cite them to avoid plagiarism.", "W.7.8",
    [("plagiarism", "Presenting someone else's words or ideas as your own."), ("citation", "Information that identifies a source.")],
    "Is changing a few words in someone's sentence enough to make it yours?",
    [Text("When you use a source: <b>quote</b> exact words in quotation marks, or <b>paraphrase</b> completely in your own words and sentence structure. Either way, <b>cite</b> the source."),
     Figure(lambda t: table(t, [["", "Example"], ["Original", "“The Black press informed readers, organized communities, and gave Harlem Renaissance writers a place to be heard.”"],
                                ["Plagiarism (patchwriting)", "The Black press informed readers, organized people, and gave writers a place to be heard."], ["Paraphrase + citation", "By publishing news and new writing, Black newspapers built communities and helped writers find readers (“The Black Press”)."],
                                ["Quotation + citation", "One historian notes that the Black press gave writers “a place to be heard” (“The Black Press”)."]], [1.6 * inch, 4.0 * inch], width=5.6 * inch, font_size=9)),
     Text("For a works cited list, include the author (if known), title, publication, and date. Example: “The Black Press.” <i>Grade 7 ELA Textbook</i>, VenvLearning, 2027."),
     KeyIdea("Quote exactly or paraphrase completely, and always cite.")],
    [Problem("What is patchwriting?", "changing a few words of a source but keeping its structure; a form of plagiarism"), Problem("What goes in quotation marks?", "the exact words"), Problem("Does a paraphrase need a citation?", "Yes")],
    [S("Warm-Up", [SA("Plagiarism =", "using others' words or ideas as your own"), SA("Paraphrase =", "your own words and structure")], cols=2),
     S("Practice", [OR("Paraphrase and cite: “Charles S. Johnson believed that art and literature could change how Americans thought about race.”", "e.g. Johnson saw creative work as a way to shift public attitudes about race (“Charles S. Johnson: Building a Movement”).", lines=3),
                    OR("Quote and cite a short phrase from “The Great Migration.”", "Answers vary; exact words in quotes with title.", lines=2),
                    OR("Write a works cited entry for “The Great Migration.”", "“The Great Migration.” Grade 7 ELA Textbook, VenvLearning, 2027.", lines=2)]),
     S("Exit Ticket", [OR("Explain why paraphrasing well is harder than quoting.", "You must fully restate ideas in your own words and structure while keeping meaning.", lines=2)])],
    te("Students quote, paraphrase, and cite.", "Quote or paraphrase data and conclusions while avoiding plagiarism; follow a standard citation format.", "Workbook Lesson 7.10",
       "A few words changed?", "Review sources.", ["Teach the chart."], "Your Turn 1–3.",
       ["Patchwriting."], ["Read, cover, write, check."], ["Build a works cited list for the unit."]),
    summary="Quote exactly, paraphrase completely, cite always.")

L11 = Lesson("7.11", "Credibility and Accuracy of Sources",
    "I can assess the credibility and accuracy of print and digital sources.", "W.7.8",
    [("credible", "Trustworthy and believable."), ("bias", "A one-sided view that may affect fairness.")],
    "Would you trust a website about jazz history with no author and lots of ads?",
    [Figure(lambda t: table(t, [["Question", "Look for"], ["Who created it?", "named author or organization with expertise"], ["When?", "date of publication or update"], ["Why?", "purpose: inform, persuade, sell"],
                                ["Where does it get information?", "cited sources, primary documents"], ["Does it agree with other reliable sources?", "corroboration"], ["Is there bias?", "one-sided language, missing perspectives"]],
                            [2.4 * inch, 3.2 * inch], width=5.6 * inch)),
     Example("Evaluate", "A museum website on Harlem Renaissance art vs an anonymous fan blog", ["Museum: experts, cited sources, educational purpose.", "Blog: no author, no sources, mixed opinion."], "The museum site is more credible; the blog might be a starting point but needs checking."),
     KeyIdea("Assess author, date, purpose, sources, corroboration, and bias.")],
    [Problem("More credible: a university library page or a social media post?", "a university library page"), Problem("Why check other sources?", "to corroborate accuracy"), Problem("What is bias?", "a one-sided view")],
    [S("Warm-Up", [SA("Credible =", "trustworthy"), SA("Bias =", "one-sided view")], cols=2),
     S("Evaluate", [OR(q, a, lines=2) for q, a in [("A documentary on PBS about jazz with historian interviews", "credible: expert sources, reputable producer"),
                                                    ("An online store page selling “authentic Harlem Renaissance posters” with a short history", "less credible for history: commercial purpose"),
                                                    ("A 1926 newspaper article from the Chicago Defender", "a primary source: valuable for its time, but reflects its era's views"),
                                                    ("An encyclopedia entry written by a university professor", "credible: expert author")]]),
     S("Exit Ticket", [OR("Why can a primary source be valuable even if it shows bias?", "It reveals what people thought at the time.", lines=2)])],
    te("Students assess credibility.", "Gather relevant information from multiple sources; assess credibility and accuracy.", "Workbook Lesson 7.11",
       "Anonymous website.", "Discuss sample sources.", ["Teach the chart."], "Your Turn 1–3.",
       ["Trusting professional-looking design."], ["Credibility checklist."], ["Evaluate three real websites with a parent."]),
    summary="Check author, date, purpose, sources, corroboration, bias.")

L12 = Lesson("7.12", "Research Questions",
    "I can develop a focused research question and generate additional related questions.", "W.7.7",
    [],
    "What about the Harlem Renaissance do you still wonder about?",
    [Text("A good research question is focused, open-ended, and researchable. As you learn, new questions appear; good researchers follow them."),
     Figure(lambda t: table(t, [["Too broad", "Focused"], ["What was the Harlem Renaissance?", "How did magazines like Opportunity and The Crisis help Harlem Renaissance writers reach readers?"],
                                ["Tell about jazz.", "How did the Great Migration spread jazz from New Orleans to Chicago and New York?"], ["Who was Zora Neale Hurston?", "How did Hurston's work as a folklore collector shape her fiction?"]],
                            [2.0 * inch, 3.6 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Focused, open-ended, researchable questions; let new questions guide further research.")],
    [Problem("Broad or focused: “Music”", "broad"), Problem("What makes a question researchable?", "information exists to answer it"), Problem("Why generate more questions?", "research reveals new angles worth exploring")],
    [S("Warm-Up", [SA("Open-ended means…", "can't be answered yes/no"), SA("A focused question narrows the…", "topic")], cols=2),
     S("Develop Questions", [OR("Write a focused research question about the Harlem Renaissance.", "Answers vary.", lines=2), OR("List three related questions that might come up.", "Answers vary.", lines=3),
                             OR("List three credible sources you could use.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Why is your question focused enough?", "Answers vary.", lines=2)])],
    te("Students develop research questions.", "Conduct short research projects to answer a question, generating additional related questions.", "Workbook Lesson 7.12",
       "Still wondering.", "Review the unit's texts.", ["Model narrowing questions."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Yes/no questions."], ["Who/how/why starters."], ["Begin a mini-research project."]),
    summary="Focused, open-ended, researchable questions.")

# ================================================================= Week 4 · Write an evidence-based synthesis (The New Negro: Locke and Kellogg)
L13 = Lesson("7.13", "Locke's Argument",
    "I can trace an author's argument and analyze how others responded to it.", "RI.7.8, RI.7.6",
    [],
    "Can art change how people see themselves and others?",
    [ReaderAssign(HR, "The New Negro: Locke and Kellogg", "What did Locke argue? Why was the book important?"),
     P_LOCKE,
     Example("Trace the argument", "Locke's claim", ["Claim: a new spirit of pride and creativity was rising among Black Americans.", "Reasoning: through art, Black Americans could define themselves instead of being defined by stereotypes.", "Counterview: some leaders argued political and economic action mattered more."],
             "Locke argued for art's power; the debate shows the movement's many voices."),
     KeyIdea("Trace the claim, reasoning, and responses; recognize that historical movements include debate.")],
    [Problem("Who edited Survey Graphic?", "Paul Kellogg"), Problem("What was Locke's main claim?", "A new spirit of pride and creativity was rising; art could let Black Americans define themselves."), Problem("What was the counterview?", "political and economic action mattered more")],
    [S("Warm-Up", [SA("Year The New Negro was published", "1925"), SA("Locke was the first African American…", "Rhodes Scholar")], cols=2),
     S("Analyze", [OR("Explain Locke's argument in your own words, citing the text.", "Answers vary.", lines=3), OR("Evaluate: Which view do you find more convincing, art or political action, or both? Explain with evidence from this unit.", "Answers vary.", lines=4)], passage=P_LOCKE),
     S("Exit Ticket", [OR("How does the debate described in paragraph 4 show the richness of the movement?", "Many voices with different ideas about how to fight for equality.", lines=2)])],
    te("Students trace an argument and responses.", "Trace and evaluate argument; analyze author's position.", "Harlem Renaissance Reader (The New Negro), workbook Lesson 7.13",
       "Art and self-image.", ["Read the Reader section.", "Read “Alain Locke and The New Negro.”"], ["Model tracing."], "Your Turn 1–3.",
       ["Assuming everyone agreed."], ["Claim/response chart."], ["Look at Aaron Douglas's illustrations for The New Negro."]),
    summary="Trace the argument and the debate around it.")

L14 = Lesson("7.14", "Planning a Synthesis Essay",
    "I can plan a synthesis essay that combines evidence from multiple sources to answer a question.", "W.7.2, W.7.9, W.7.8",
    [],
    "How did the Harlem Renaissance change the way Black Americans were seen and saw themselves?",
    [Text("A synthesis essay combines ideas from several sources into one argument. Organize by <b>idea</b>, not by source: each body paragraph makes one point and uses two or more sources."),
     Figure(lambda t: table(t, [["Body paragraph idea", "Possible sources"], ["Art expressed truths hidden behind “the mask”", "Dunbar poem; Sources A and B on Dunbar; Locke"], ["New communities and institutions gave artists a voice", "Great Migration; Black press; Johnson"],
                                ["Artists defined themselves despite criticism", "Locke; Hughes sources (if researched); Reader"]], [2.8 * inch, 2.8 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Organize by idea; each paragraph synthesizes two or more sources.")],
    [Problem("Organize by idea or by source?", "by idea"), Problem("How many sources per body paragraph?", "two or more"), Problem("What goes at the end?", "a works cited list")],
    [S("Warm-Up", [SA("Synthesis =", "combining ideas from sources"), SA("Organize by…", "idea")], cols=2),
     S("Plan", [OR("Thesis:", "Answers vary.", lines=2), OR("Body 1: idea + sources + evidence:", "Answers vary.", lines=4), OR("Body 2: idea + sources + evidence:", "Answers vary.", lines=4), OR("Body 3 (optional):", "Answers vary.", lines=3)])],
    te("Students plan synthesis essays.", "Write informative texts integrating information from multiple sources.", "Workbook Lesson 7.14",
       "Seen and saw themselves.", "Review sources and notes.", ["Model the chart."], "Plan.",
       ["Source-by-source summaries."], ["Idea × source grid."], ["Include an original research source."], independent="Finish the plan."),
    summary="Organize by idea; synthesize sources in each paragraph.")

L15 = Lesson("7.15", "Drafting the Synthesis Essay",
    "I can draft a synthesis essay that integrates and cites multiple sources.", "W.7.2, W.7.8, W.7.9",
    [],
    "How do you move between sources inside one paragraph?",
    [Example("Synthesis paragraph", "Idea: Art expressed truths hidden behind “the mask.”", ["Topic sentence.", "Source 1: Dunbar's poem: “With torn and bleeding hearts we smile.”", "Source 2: Locke argued art let Black Americans define themselves.", "Analysis connecting both."],
             "Harlem Renaissance artists used their work to reveal truths that had long been hidden. Decades earlier, Paul Laurence Dunbar described smiling “with torn and bleeding hearts,” capturing the pain behind a forced appearance. Alain Locke later argued that through art, Black Americans could “define themselves” rather than be defined by stereotypes (“Alain Locke and The New Negro”). Together, these voices show art moving from hiding pain to claiming identity."),
     KeyIdea("Use transitions between sources, cite each, and explain how they connect.")],
    [Problem("Transition between sources", "Similarly, Later, In addition, Building on this"), Problem("What follows evidence from two sources?", "analysis connecting them"), Problem("How do you cite in-text?", "author or title in parentheses or in the sentence")],
    [S("Warm-Up", [SA("A transition between sources", "Similarly"), SA("Short story / article titles go in…", "quotation marks")], cols=2),
     S("Draft", [OR("Draft your synthesis essay.", "Answers vary.", lines=26, note="Look for: thesis; body paragraphs organized by idea with two or more cited sources; analysis; conclusion.")])],
    te("Students draft synthesis essays.", "Write informative texts; integrate and cite sources.", "Plans, workbook Lesson 7.15",
       "Moving between sources.", "Reread the model paragraph.", ["Model drafting a paragraph."], "Draft.",
       ["Dropping quotes without analysis."], ["Color-code sources."], ["Add a counterargument."], independent="Finish the draft."),
    summary="Integrate and connect sources with transitions and citations.")

L16 = Lesson("7.16", "Revising, Citing, and Publishing",
    "I can revise my synthesis essay and prepare a works cited list.", "W.7.5, W.7.8",
    [("works cited", "An alphabetical list of sources at the end of an essay.")],
    "How can a reader check your sources?",
    [Figure(lambda t: table(t, [["Checklist", "✓"], ["Thesis answers the question.", ""], ["Each body paragraph synthesizes two or more sources.", ""], ["Quotations are exact; paraphrases are fully in my own words.", ""],
                                ["Every source is cited in the text.", ""], ["Historical terms are quoted accurately; my own words are current and respectful.", ""], ["Works cited list is alphabetical and complete.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Revise for synthesis and accuracy; complete the works cited list.")],
    [Problem("How is a works cited list ordered?", "alphabetically"), Problem("What must every paraphrase have?", "a citation"), Problem("Why cite?", "credit authors, let readers check, avoid plagiarism")],
    [S("Warm-Up", [SA("Works cited order", "alphabetical"), SA("Patchwriting is…", "plagiarism")], cols=2),
     S("Revise and Cite", [OR("List three revisions you made.", "Answers vary.", lines=3), OR("Write your works cited list.", "Answers vary.", lines=6)])],
    te("Students revise and cite.", "Strengthen writing; follow a standard citation format.", "Drafts, workbook Lesson 7.16, Unit 7 Review",
       "Checking sources.", "Read the checklist.", ["Model a works cited list."], "Revise.",
       ["Missing in-text citations."], ["Highlight every borrowed idea."], ["Publish in the portfolio."], independent="Revise; then the Unit 7 Review.", exit_="Tomorrow: Unit 7 Test."),
    summary="Revise for synthesis; cite completely.")

# ================================================================= checks
C1 = Check("Weekly Check 19: Comparing Sources", [S("Read Source A", [], passage=P_C19A), S("Read Source B, then answer", [
    OR("What does Source A focus on?", "where jazz began and how it spread north", lines=1), OR("What does Source B focus on?", "what jazz meant to 1920s listeners and its reception", lines=1),
    OR("What fact or idea do both sources share?", "Jazz flourished/became popular in the 1920s.", lines=1),
    OR("How does Source B acknowledge a different view?", "It notes some critics dismissed jazz as noise.", lines=2),
    OR("Write one sentence synthesizing both sources.", "e.g. Carried north by migrating musicians, jazz became the sound of the modern city by the end of the 1920s, despite early critics.", lines=2)], passage=P_C19B)], minutes=20)
C2 = Check("Weekly Check 20: Evaluating Evidence", [S("Read and answer", [
    OR("What is the claim?", "Every middle school should teach the Harlem Renaissance.", lines=1), OR("List the three reasons.", "important poems; understanding art's response to injustice; it's interesting", lines=2),
    OR("Which reason is weakest? Why?", "The third: vague, anecdotal (“everyone I know loves jazz”).", lines=2),
    OR("Suggest stronger evidence for reason 1.", "e.g. evidence that Hughes's poems are taught internationally or translated into many languages", lines=2),
    OR("Write a counterclaim and rebuttal for this argument.", "e.g. Some say school time is limited; however, the period connects history, literature, and music at once.", lines=3)], passage=P_C20)], minutes=20)
C3 = Check("Weekly Check 21: Integrating and Citing", [S("Read and answer", [
    OR("Quote and cite a phrase from the passage.", "e.g. Their Eyes Were Watching God is “now considered a classic of American literature” (“Zora Neale Hurston”).", lines=2),
    OR("Paraphrase the last sentence and cite it.", "e.g. Hurston's 1937 novel went out of print until scholars renewed interest in the 1970s; it is now a classic (“Zora Neale Hurston”).", lines=3),
    OR("Write a focused research question based on the passage.", "e.g. How did Hurston's folklore research shape her novels?", lines=2),
    OR("Write a works cited entry for this passage.", "“Zora Neale Hurston.” Grade 7 ELA Textbook, VenvLearning, 2027.", lines=1)], passage=P_C21)], minutes=20)

REVIEW = Check("Unit 7 Review", [
    S("Concepts", [SA("Renaissance =", "rebirth"), SA("Push factor example", "Jim Crow laws / violence / boll weevil"), SA("Extended metaphor in Dunbar's poem", "the mask"), SA("Patchwriting =", "plagiarism"),
                   SA("Credible source criteria (two)", "expert author, cited sources"), SA("Organize a synthesis by…", "idea")], cols=2),
    S("Apply", [OR("Explain how two sources can be accurate but give different impressions.", "They emphasize different evidence or interpretations.", lines=2),
                OR("Evaluate: “Jazz is great because I like it.” Is this strong evidence? Revise it.", "Weak; e.g. jazz influenced later genres such as swing and rock.", lines=2)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = make_test("Unit 7 Test", [
    S("Part A · Source A (1 point each)", [
        OR("What does “The Negro Speaks of Rivers” connect Black Americans to?", "ancient rivers such as the Euphrates, the Congo, and the Nile; a long history", lines=2),
        OR("Why did Hughes use blues and jazz rhythms?", "so his poems sounded like Harlem's music and reflected ordinary people's lives", lines=2)], passage=P_TEST_A),
    S("Part B · Source B (1 point each)", [
        OR("Why did some reviewers criticize Hughes's 1927 book?", "They thought its poems about working-class life gave an unflattering picture to white readers.", lines=2),
        OR("How did Hughes respond? Cite the source.", "In “The Negro Artist and the Racial Mountain” he argued artists should express themselves freely and honestly (Source B).", lines=2)], passage=P_TEST_B),
    S("Part C · Compare and evaluate (1 point each)", [
        OR("How do the two sources shape their presentation of Hughes differently?", "A celebrates his achievements and goals; B focuses on controversy and his defense.", lines=3, points=2),
        OR("Connect Hughes's view to Locke's argument from this unit.", "Both believed Black artists should define themselves; Hughes emphasized honest freedom even when it drew criticism.", lines=3),
        OR("Paraphrase a sentence from Source A and cite it.", "e.g. Hughes chose ordinary people as his subjects (Source A).", lines=2),
        OR("Write a focused research question raised by these sources.", "e.g. How did Hughes use blues forms in his poetry?", lines=2)]),
    S("Part D · Synthesis (6 points)", [OR("Write a synthesis paragraph (or short essay): How did Langston Hughes help Black Americans define themselves through art? Use both sources and at least one other text from this unit, with citations.",
                                           "Rubric: thesis (1); evidence from Source A (1); evidence from Source B (1); evidence from another unit text (1); analysis connecting sources (1); citations and conventions (1).", lines=18, points=6)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-04-26", "2027-05-03", "2027-05-10", "2027-05-17"], CHECKS, REVIEW, TEST)

UNIT = Unit(7, "Voices of the Harlem Renaissance", "Historical context, poetry analysis, comparing sources and claims, evaluating evidence, integrating and citing sources, research, and synthesis.",
    "In the 1920s, Harlem became the heart of a cultural rebirth that transformed American literature and music. In this unit you'll study the movement's history and voices, from Paul Laurence Dunbar's “We Wear the Mask” to the Great Migration, the Black press, and Alain Locke's <i>The New Negro</i>, and you'll learn the research skills of comparing, evaluating, integrating, and citing sources.",
    ["Build historical context and discuss historical language respectfully.", "Analyze poetry and compare how sources shape information and claims.",
     "Evaluate reasons, evidence, and data; write arguments with counterclaims.", "Quote, paraphrase, and cite; assess credibility; develop research questions; write a synthesis essay."],
    [("RI.7.1–3, RI.7.6–9", "Cite evidence; central ideas; analyze interactions; compare texts and data; evaluate arguments."), ("RL.7.2, RL.7.4–5", "Analyze theme, figurative language, and form in poetry."),
     ("W.7.1, W.7.2, W.7.5, W.7.7–9", "Write arguments and syntheses; conduct research; cite sources.")],
    [("renaissance", "Rebirth."), ("Great Migration", "The movement of millions of Black Southerners to other regions."), ("extended metaphor", "A metaphor developed throughout a work."), ("plagiarism", "Using others' words or ideas as your own."),
     ("synthesis", "Combining ideas from several sources.")],
    ["Unit 4 argument analysis; Unit 6 sentence skills."], ["The Genius of the Harlem Renaissance Reader", "Library or approved online sources for research", "Optional: recordings of 1920s jazz"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Evaluating sources, avoiding plagiarism, and synthesizing evidence are the foundation of every research project, and the Harlem Renaissance still shapes American music, poetry, and art.",
    family_note="Listen together to a Duke Ellington or Louis Armstrong recording and talk about what it might have felt like to hear it new in 1925.",
    weeks=WEEKS)
