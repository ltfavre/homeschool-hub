"""Grade 4 ELA · Unit 3: Reading Longer Texts — stamina, annotation, point of view, tracking evidence, inference, and organized written responses.
Anchor reading: King Arthur and the Round Table Reader, Chapters 9–12 (Dec 14, 2026 – Jan 22, 2027)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule
from content.ela4.unit01 import S, MC, OR, SA, READER


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


# ================================================================= the serialized story (original)
HOLLOW_1 = Passage("The Secret of Hollow Hill · Part 1", [
    "Nobody in the village of Thornbury went near Hollow Hill. The grown-ups said the hill was dangerous, though none of them could say exactly why. Children whispered that a dragon slept beneath it, or a giant, or the ghost of a wicked king.",
    "Eleven-year-old Pip didn't believe in dragons. She believed in maps. Her grandfather had been the village mapmaker, and when he died, he left Pip his drawings, his compass, and a small brass key with no lock to fit it.",
    "One rainy afternoon, Pip spread Grandfather's oldest map across the kitchen table. In the corner, in faded ink, she noticed something she had never seen before: a tiny drawing of a door on the side of Hollow Hill. Beneath it, Grandfather had written three words: <i>For Pip. Courage.</i>",
    "Pip's heart beat faster. She ran her finger over the words again and again. Grandfather had known she would find this. But why hadn't he told her?",
    "That night, she could hardly sleep. Each time she closed her eyes, she saw the little door. By morning, she had made up her mind. She packed bread, a candle, the compass, and the brass key, and she slipped out of the house before anyone else was awake.",
    "Fog lay over the fields like a gray blanket. As Pip walked, the village roosters began to crow behind her. Ahead, Hollow Hill rose dark and silent. Her legs felt heavy, and twice she almost turned back. Then she remembered the words on the map. <i>Courage.</i> She kept walking.",
], source="An original story in three parts", genre="Adventure story")

HOLLOW_2 = Passage("The Secret of Hollow Hill · Part 2", [
    "Thorny bushes covered the side of the hill. Pip pushed through them, scratching her arms, until she found a gray stone almost hidden in the weeds. Carved into the stone was a keyhole.",
    "Her hands shook as she pulled out the brass key. It slid in perfectly. With a loud click, the stone swung inward, and cool air rushed out of a dark tunnel.",
    "Pip lit her candle. The tunnel walls were smooth and dry, and someone had painted arrows on them in white paint. She followed the arrows deeper and deeper, counting her steps the way Grandfather had taught her. Two hundred steps. Three hundred.",
    "At last the tunnel opened into a round room. Pip gasped. The walls were covered with maps, hundreds of them, showing rivers, forests, roads, and towns, some she knew and some she had never heard of. In the middle of the room stood a wooden desk, and on the desk lay a letter with her name on it.",
    "<i>Dear Pip,</i> the letter began. <i>For fifty years, I have mapped every corner of this valley. I kept this room secret because I was afraid people would laugh at an old man who spent his life drawing. But you never laughed. You asked questions. Now this room is yours. Please don't let my work stay hidden in the dark.</i>",
    "Pip read the letter three times. Then she sat down at Grandfather's desk and cried, but they were not entirely sad tears.",
], source="An original story in three parts", genre="Adventure story")

HOLLOW_3 = Passage("The Secret of Hollow Hill · Part 3", [
    "When Pip returned to Thornbury, the whole village was searching for her. Her mother hugged her so hard she could barely breathe. Then, of course, came the scolding.",
    "“Hollow Hill?” the mayor sputtered. “That hill is dangerous!”",
    "“It isn't,” Pip said quietly. “There's nothing dangerous inside. Only maps.” And she told them everything.",
    "At first, people didn't believe her. So the next day, Pip led a group of villagers through the thorny bushes and into the tunnel. When they saw the round room, no one said a word. Old Mrs. Barrow touched a map of her family's farm, drawn more carefully than any she had ever seen, and her eyes filled with tears.",
    "That spring, the villagers carried Grandfather's maps down from Hollow Hill and hung them in the town hall. Travelers came from far away to see them. The mayor named the room the Mapmaker's Library and asked Pip to be its keeper.",
    "Children in Thornbury still whisper about Hollow Hill. But now, instead of dragons, they talk about a girl who was brave enough to follow a map, and a grandfather who was brave enough, in the end, to share his work.",
], source="An original story in three parts", genre="Adventure story")

P_CATHEDRAL = Passage("How a Medieval Cathedral Was Built", [
    "Cathedrals were the largest buildings in medieval Europe. Some took more than a hundred years to finish, which meant that the workers who began a cathedral often did not live to see it completed.",
    "First, a master builder drew the plans. He decided how tall the walls would be, where the windows would go, and how the roof would be supported. There were no computers, so he used simple tools like string, compasses, and rulers.",
    "Next, workers dug deep trenches for the foundation. The foundation had to be strong enough to hold up thousands of tons of stone, so it was sometimes dug as deep as the walls were tall.",
    "Then the stonecutters went to work. In the quarry, they cut huge blocks of stone and shaped them with hammers and chisels. Each block was marked with the stonecutter's own symbol so he could be paid for his work.",
    "As the walls rose, carpenters built wooden scaffolds, frames that workers stood on to reach high places. Large wheels called treadwheels, powered by men walking inside them like hamsters, lifted the heavy stones into place.",
    "Finally, glassmakers created stained-glass windows. They colored glass with metals, cut it into pieces, and joined the pieces with strips of lead to make pictures. When sunlight shone through, the inside of the cathedral glowed with color.",
    "Today, many medieval cathedrals are still standing. They remind us what people could build with patience, teamwork, and simple tools.",
], source="An original informational text", genre="Informational text")

P_POV1 = Passage("The Storm (Version A)", [
    "I pressed my face to the window as thunder shook the house. My little brother crawled under the table, but I wasn't scared. Well, maybe a little.",
], source="An original example", genre="First-person narrator", numbered=False)
P_POV2 = Passage("The Storm (Version B)", [
    "Marcus pressed his face to the window as thunder shook the house. His little brother crawled under the table. Marcus told himself he wasn't scared, but his heart was pounding.",
], source="An original example", genre="Third-person narrator", numbered=False)

P_C7 = Passage("The Bravest Thing", [
    "I had never been on a stage before. My mouth felt as dry as sand, and my knees knocked together under my costume.",
    "My line was only four words: “The king is coming!” I had practiced it a hundred times. But when the spotlight hit my face, my mind went blank.",
    "Then I saw my best friend, Lucas, in the front row. He gave me a thumbs-up. I took a breath and shouted my line so loudly that the audience laughed. I didn't care. I had done it.",
], source="An original personal narrative", genre="Personal narrative")

P_C8 = Passage("Beavers: Nature's Engineers", [
    "Beavers are some of the best builders in the animal world. They use their sharp front teeth to cut down trees, sometimes chewing through a trunk in a single night.",
    "First, beavers build a dam across a stream. They pile up branches, rocks, and mud until the water backs up into a pond.",
    "Next, they build a home called a lodge in the middle of the pond. The lodge has underwater entrances, so wolves and other predators cannot easily get in.",
    "The pond a beaver makes helps other animals too. Fish, frogs, ducks, and insects move into the new wetland. In this way, one family of beavers can change a whole stream.",
], source="An original informational text", genre="Informational text")

P_C9 = Passage("The Empty Chair", [
    "Every Sunday, Grandpa Joe set five places at the dinner table, even though only four people came. Nobody ever sat in the fifth chair.",
    "When Lena asked why, Grandpa just smiled and passed the potatoes. But she noticed that he always glanced at the door when the wind rattled it.",
    "One Sunday, there was a knock. Grandpa jumped up so fast his napkin fell to the floor. In the doorway stood a tall man in a soldier's uniform. Grandpa hugged him for a long time without saying anything. That night, all five chairs were full.",
], source="An original story", genre="Realistic fiction")

P_TEST = Passage("The Night of the Great Fire", [
    "In 1871, the city of Chicago was mostly made of wood. Houses, sidewalks, barns, and even some streets were wooden. That summer had been the driest anyone could remember. Only an inch of rain had fallen since July.",
    "On the night of October 8, a fire started in a barn on the southwest side of the city. No one knows for sure how it began. Strong winds from the southwest pushed the flames toward the center of the city, and the fire spread from one wooden building to the next.",
    "The city's firefighters worked all night, but they had only a few horse-drawn engines. The fire jumped across the Chicago River and kept going. Burning bits of wood flew through the air and started new fires blocks away.",
    "Thousands of people ran from their homes carrying whatever they could. Some waded into Lake Michigan to escape the heat. When rain finally fell on the night of October 9, the fire had burned for more than a day.",
    "The Great Chicago Fire destroyed about 17,000 buildings and left about 100,000 people homeless. Yet Chicago did not give up. People rebuilt the city, this time using more brick, stone, and iron. Within twenty years, Chicago was one of the largest and most modern cities in the country.",
    "Today, a star on Chicago's flag stands for the Great Fire. It reminds people that the city rose from the ashes stronger than before.",
], source="An original informational text based on historical facts", genre="Informational text")

# ================================================================= Week 1 · Read a longer passage (Chapter 9)
L1 = Lesson("3.1", "Building Reading Stamina",
    "I can read a longer text by breaking it into chunks and checking my understanding.", "RL.4.10, RL.4.1",
    [("stamina", "The ability to keep going for a long time."), ("chunk", "A small section of a text, such as a few paragraphs."), ("gist", "The general idea of a section.")],
    "What helps you keep going when you read a long chapter?",
    [ReaderAssign(READER, "Chapter 9: The Birth of Galahad", "Stop after every few paragraphs and tell yourself the gist."),
     Text("Long texts can feel overwhelming. Strong readers break them into <b>chunks</b>. After each chunk, they stop and state the <b>gist</b> in a few words before moving on."),
     HOLLOW_1,
     Example("Chunk and state the gist", "Paragraphs 1–2", ["Read paragraphs 1–2.", "Ask: What is this part mostly about?", "Say it in a few words."], "People fear Hollow Hill; Pip loves maps and got her grandfather's things."),
     KeyIdea("Read a chunk, stop, state the gist, then keep going.")],
    [Problem("Gist of paragraph 3", "Pip finds a door drawn on the map with a note for her."), Problem("Gist of paragraphs 5–6", "Pip packs up and walks to Hollow Hill even though she's afraid."),
     Problem("What do you predict Pip will find?", "Answers vary; accept predictions based on clues (the key, the door).")],
    [S("Warm-Up", [SA("What is a chunk?", "a small section of a text"), SA("What is the gist?", "the general idea of a section")], cols=2),
     S("Read and Chunk", [OR("Write the gist of each chunk: paragraphs 1–2, 3–4, 5–6.", "1–2: People fear the hill; Pip loves maps and got Grandfather's key. 3–4: She finds the door on the map with a note. 5–6: She packs and goes to the hill, scared but brave.", lines=5),
                          OR("Why does Pip almost turn back? What keeps her going?", "She is scared (legs heavy); she remembers the word Courage.", lines=3)], passage=HOLLOW_1),
     S("Chapter 9", [OR("Write the gist of the first half and the second half of Chapter 9.", "Answers vary.", lines=4)]),
     S("Exit Ticket", [OR("Which chunking strategy helped you most today? Why?", "Answers vary.", lines=2)])],
    te("Students read longer texts in chunks.", "By year end, read and comprehend literature at the grade 4–5 band proficiently.", "King Arthur Reader (Chapter 9), workbook Lesson 3.1",
       "What helps you keep going?", ["Read Chapter 9 in chunks with gist stops.", "Read Part 1 of “Hollow Hill.”"], ["Model chunking and gist statements."], "Your Turn 1–3.",
       ["Reading to the end without checking understanding."], ["Use sticky notes at stopping points."], ["Time a silent reading session and track stamina each day."]),
    summary="Break long texts into chunks; state the gist after each one.")

L2 = Lesson("3.2", "Annotating a Text",
    "I can annotate a text by marking important ideas, questions, and new words.", "RL.4.1, RI.4.1",
    [("annotate", "Make notes and marks on a text while reading.")],
    "If you could write on the pages of a book, what would you mark?",
    [Text("<b>Annotating</b> means marking a text as you read. It keeps you active and helps you find evidence later. Use the same symbols every time."),
     Figure(lambda t: table(t, [["Symbol", "Means"], ["underline", "important idea or event"], ["?", "I have a question"], ["!", "surprising or exciting"], ["circle", "new or interesting word"], ["*", "evidence about a character"]],
                            [1.3 * inch, 3.0 * inch], width=4.3 * inch)),
     HOLLOW_2,
     Example("Annotate a paragraph", "Paragraph 4", ["Underline: the room is covered with hundreds of maps.", "! Pip gasped.", "? Who wrote the letter?"], "Marks show the key event, a surprise, and a question to answer later."),
     KeyIdea("Annotate to stay focused and to find evidence quickly later. In a library book, use sticky notes instead of writing.")],
    [Problem("What symbol shows a question?", "?"), Problem("Which detail in paragraph 3 would you mark with *?", "She counts her steps the way Grandfather taught her (shows she's careful)."), Problem("Which word might you circle?", "Answers vary.")],
    [S("Warm-Up", [SA("What does annotate mean?", "mark and make notes on a text"), SA("What symbol marks a new word?", "circle")], cols=2),
     S("Annotate Part 2", [OR("Annotate Part 2 using the symbols. Then list one thing you underlined, one question, and one surprise.", "Answers vary.", lines=4),
                           OR("Why did Grandfather keep the room secret? Quote the letter.", "“I was afraid people would laugh at an old man who spent his life drawing.”", lines=2),
                           OR("Why does Pip cry “not entirely sad tears”?", "She misses Grandfather, but she is also happy and moved that he left the room to her.", lines=2)], passage=HOLLOW_2),
     S("Exit Ticket", [OR("How did annotating help you answer the questions?", "Answers vary: found evidence faster.", lines=2)])],
    te("Students annotate texts.", "Refer to details and examples in a text.", "Pencils or sticky notes, workbook Lesson 3.2",
       "What would you mark?", "Read Part 2 aloud with annotations modeled.", ["Teach the symbol chart."], "Your Turn 1–3.",
       ["Underlining everything."], ["Limit to three underlines per paragraph."], ["Annotate Chapter 9 with sticky notes."]),
    summary="Annotate with symbols to stay focused and find evidence.")

L3 = Lesson("3.3", "Fix-Up Strategies",
    "I can notice when I'm confused and use a strategy to fix it.", "RL.4.10",
    [("monitor", "Keep track of whether you understand."), ("visualize", "Make a picture in your mind.")],
    "What do you do when you realize you've read a whole page and don't remember any of it?",
    [Text("Strong readers <b>monitor</b> their understanding. When the meaning breaks down, they use a fix-up strategy."),
     Bullets(["<b>Reread</b> the confusing part slowly.", "<b>Read ahead</b> a little to see if it becomes clear.", "<b>Visualize</b> what is happening.",
              "<b>Ask a question</b> and look for the answer.", "<b>Use context clues</b> for a hard word.", "<b>Retell</b> what you just read in your own words."]),
     HOLLOW_3,
     Example("Fix confusion", "Paragraph 6: “a grandfather who was brave enough, in the end, to share his work.” How was sharing brave?",
             ["Reread Part 2: Grandfather hid his maps because he feared people would laugh.", "Connect: sharing meant facing that fear."], "Sharing was brave because he had been afraid of being laughed at."),
     KeyIdea("Notice confusion, then choose a fix-up strategy instead of skipping ahead.")],
    [Problem("Which strategy would you use for a hard word?", "context clues"), Problem("Which strategy helps with a confusing event?", "reread, visualize, or retell"), Problem("Why does Mrs. Barrow cry?", "She sees a beautiful map of her family's farm; she is touched.")],
    [S("Warm-Up", [SA("What does monitor mean?", "keep track of understanding"), SA("Name one fix-up strategy.", "reread, read ahead, visualize, ask, context, retell")], cols=2),
     S("Read Part 3", [OR("Why didn't people believe Pip at first? How did she prove it?", "It sounded impossible; she led a group into the tunnel to see.", lines=3),
                       OR("How did the village change by the end?", "They hung the maps in the town hall; travelers came; Pip became the keeper; children talk about Pip instead of dragons.", lines=3),
                       OR("Write about one place in Part 3 that confused you and the strategy you used.", "Answers vary.", lines=2)], passage=HOLLOW_3),
     S("Exit Ticket", [OR("Retell the whole story of Hollow Hill in three sentences.", "Pip finds a door on Grandfather's map and uses his key to open a tunnel in Hollow Hill. Inside is a secret room of his maps and a letter giving it to her. She shows the village, and the maps become the Mapmaker's Library.", lines=3)])],
    te("Students monitor comprehension and use fix-up strategies.", "Read and comprehend grade-level literature proficiently.", "Workbook Lesson 3.3",
       "Lost-page experience.", "Read Part 3; pause to model a fix-up.", ["Teach strategies list."], "Your Turn 1–3.",
       ["Skipping confusing parts."], ["Bookmark with the strategy list."], ["Teach a fix-up strategy to a sibling."]),
    summary="Monitor your reading; when confused, reread, read ahead, visualize, ask, use context, or retell.")

L4 = Lesson("3.4", "Narrator and Point of View",
    "I can tell whether a story is told in first person or third person and explain how it affects what we learn.", "RL.4.6",
    [("narrator", "The voice telling the story."), ("first-person point of view", "The narrator is a character who uses I, me, and my."),
     ("third-person point of view", "The narrator is outside the story and uses he, she, and they.")],
    "Would a story sound different if the main character told it herself?",
    [Text("A <b>first-person narrator</b> is a character in the story (<i>I, me, my</i>). We only learn what that character knows and feels. A <b>third-person narrator</b> is outside the story (<i>he, she, they</i>) and may tell what several characters think."),
     P_POV1, P_POV2,
     Example("Compare narrators", "How are Version A and Version B different?", ["A uses I; the narrator admits he's “a little” scared.", "B uses Marcus and his; the narrator tells us his heart was pounding."],
             "A is first person; we hear the boy's own voice. B is third person; the narrator describes Marcus from outside."),
     KeyIdea("Look for pronouns: I/me/my = first person; he/she/they = third person. Ask what the narrator can and can't know.")],
    [Problem("Point of view of “The Secret of Hollow Hill”", "third person"), Problem("Point of view of “Grandpa's Sayings” (Lesson 1.10)", "first person"), Problem("Point of view of the King Arthur Reader", "third person")],
    [S("Warm-Up", [SA("Pronouns in first person", "I, me, my, we"), SA("Pronouns in third person", "he, she, they")], cols=2),
     S("Which Point of View?", [SA(q, a) for q, a in [("“I grabbed my sword and ran.”", "first"), ("“Arthur grabbed his sword and ran.”", "third"),
                                                       ("“We laughed until our sides hurt.”", "first"), ("“The children laughed until their sides hurt.”", "third")]], cols=2),
     S("Rewrite", [OR("Rewrite Hollow Hill Part 1, paragraph 4, in first person, as if Pip is telling it.", "e.g. My heart beat faster. I ran my finger over the words again and again. Grandfather had known I would find this. But why hadn't he told me?", lines=4),
                   OR("What can a first-person narrator NOT tell readers?", "what other characters are thinking (only what the narrator knows)", lines=2)]),
     S("Exit Ticket", [OR("Why might an author choose first person for a scary story?", "Readers feel the fear directly with the character.", lines=2)])],
    te("Students identify and compare points of view.", "Compare and contrast the point of view from which different stories are narrated, including first- and third-person.", "Workbook Lesson 3.4",
       "Same story told by the character?", "Read both Storm versions aloud.", ["Teach pronoun clues.", "Model the comparison."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Thinking dialogue with “I” makes a story first person."], ["Look at narration, not dialogue."], ["Retell a King Arthur scene in first person as Arthur."]),
    summary="First person: I/me (a character tells). Third person: he/she (an outside narrator tells).")

# ================================================================= Week 2 · Track evidence across paragraphs (Chapter 10)
L5 = Lesson("3.5", "Tracking a Character Across a Text",
    "I can track how a character changes across a long text using evidence from several places.", "RL.4.3, RL.4.1",
    [("character change", "How a character's feelings, beliefs, or actions are different at the end than at the beginning.")],
    "Think of a character who changes over a whole book. How did you notice the change?",
    [ReaderAssign(READER, "Chapter 10: The Coming of Galahad to Court", "Track Galahad: what he does, what others say about him."),
     Text("In a long text, evidence about a character is spread out. Use a <b>tracking chart</b> to collect evidence from the beginning, middle, and end."),
     Figure(lambda t: table(t, [["Part", "Evidence about Pip", "What it shows"], ["Part 1", "Her legs felt heavy; twice she almost turned back.", "nervous but determined"],
                                ["Part 2", "She followed the arrows and counted her steps.", "careful, brave"], ["Part 3", "She led villagers into the tunnel and became the keeper.", "confident leader"]],
                            [0.8 * inch, 2.9 * inch, 1.8 * inch], width=5.5 * inch)),
     Example("Explain the change", "How does Pip change?", ["Beginning: unsure, almost turns back.", "End: confident; leads the village; becomes keeper."], "Pip grows from a nervous girl into a confident leader."),
     KeyIdea("Collect evidence from the beginning, middle, and end to explain how a character changes.")],
    [Problem("How does the mayor change?", "from calling the hill dangerous to naming the Mapmaker's Library and asking Pip to be keeper"), Problem("How do the village children change?", "They talk about Pip instead of dragons."),
     Problem("How does Grandfather change (from his letter)?", "from hiding his work out of fear to sharing it through Pip")],
    [S("Warm-Up", [SA("What is character change?", "how a character is different at the end"), SA("Why use a tracking chart?", "to collect evidence from many places")], cols=2),
     S("Track Galahad", [OR("Fill in: beginning of Chapter 10, what Galahad does or how others see him:", "Answers vary.", lines=2),
                         OR("Middle:", "Answers vary.", lines=2), OR("End:", "Answers vary.", lines=2),
                         OR("What do these details show about Galahad?", "Answers vary, e.g. he is pure, special, chosen.", lines=3)]),
     S("Exit Ticket", [OR("In one sentence, explain how Pip changes, using one detail from the beginning and one from the end.", "At first Pip almost turns back, but by the end she leads the village and becomes the keeper.", lines=2)])],
    te("Students track character change with evidence.", "Describe in depth a character, drawing on specific details.", "King Arthur Reader (Chapter 10), workbook Lesson 3.5",
       "A character who changes.", "Read Chapter 10.", ["Model the Pip tracking chart."], "Your Turn 1–3.",
       ["Using evidence from only one part."], ["Three-box chart."], ["Track Arthur across all chapters so far."]),
    summary="Track evidence from beginning, middle, and end to explain character change.")

L6 = Lesson("3.6", "Explaining Events and Procedures",
    "I can explain what happened and why in an informational text, using specific details.", "RI.4.3",
    [("procedure", "A series of steps for doing something."), ("sequence", "The order in which things happen.")],
    "How would you explain to a younger child how a sandwich is made, step by step?",
    [Text("Informational texts often explain a <b>procedure</b> (how something is done) or <b>events</b> (what happened and why). Follow the <b>sequence</b> with signal words like <i>first, next, then, as, finally</i>, and explain <b>why</b> each step matters."),
     P_CATHEDRAL,
     Example("Explain a step and why", "Why did the foundation have to be so deep?", ["Find the step: paragraph 3.", "Reason: it had to hold up thousands of tons of stone."], "The foundation was very deep because it had to support the huge weight of the stone walls."),
     KeyIdea("Explain each step in order and tell why it was needed.")],
    [Problem("What was the first step?", "A master builder drew the plans."), Problem("Why did stonecutters mark their blocks?", "so they could be paid for their work"), Problem("What powered the treadwheels?", "men walking inside them")],
    [S("Warm-Up", [SA("What is a procedure?", "a series of steps"), SA("Name two sequence words.", "first, next, then, finally")], cols=2),
     S("Explain the Procedure", [
         OR("List the steps of building a cathedral in order (at least five).", "plans; foundation; cutting stone; scaffolds and lifting stones; stained-glass windows", lines=4),
         OR("Explain how workers lifted heavy stones high into the walls. Use two details.", "Carpenters built scaffolds; treadwheels powered by walking men lifted the stones.", lines=3),
         OR("Why did some workers never see their cathedral finished?", "Cathedrals took more than a hundred years to build.", lines=2)], passage=P_CATHEDRAL),
     S("Exit Ticket", [OR("Explain how stained-glass windows were made in your own words.", "Glass was colored with metals, cut into pieces, and joined with strips of lead to form pictures.", lines=2)])],
    te("Students explain procedures and events.", "Explain events, procedures, ideas, or concepts in a text, including what happened and why.", "Workbook Lesson 3.6",
       "Sandwich steps.", "Read “How a Medieval Cathedral Was Built.”", ["Flowchart the steps.", "Model the foundation question."], "Your Turn 1–3.",
       ["Listing steps without explaining why."], ["Flowchart with a “why” box under each step."], ["Explain how a building near you was built."]),
    summary="Explain each step in order and why it mattered.")

L7 = Lesson("3.7", "Connecting Evidence from Several Paragraphs",
    "I can combine evidence from different parts of a text to answer a big question.", "RI.4.1, RL.4.1",
    [("synthesize", "Put information from different places together to form one idea.")],
    "Can one paragraph always answer a big question?",
    [Text("Big questions need evidence from more than one place. <b>Synthesize</b> by finding a detail in each part, then explaining what they show together."),
     Example("Synthesize", "What qualities did cathedral builders need? (Lesson 3.6 passage)", ["Paragraph 2: master builder planned with simple tools → skill and planning.", "Paragraph 4: stonecutters shaped huge blocks → strength and skill.",
                                                                                               "Paragraph 1 and 7: took over 100 years; patience and teamwork."],
             "Builders needed skill, strength, and above all patience and teamwork, because the work took generations."),
     KeyIdea("For big questions: gather evidence from several paragraphs, then explain what it shows together.")],
    [Problem("Evidence that Grandfather loved Pip (two parts of Hollow Hill)", "He left her his key and maps (Part 1); he wrote her a letter giving her the room (Part 2)."),
     Problem("Evidence that the village valued the maps (Part 3)", "They hung them in the town hall; Mrs. Barrow cried; they named the library."), Problem("What does synthesize mean?", "combine information from different places")],
    [S("Warm-Up", [SA("Synthesize means…", "combine information into one idea"), SA("How many paragraphs for a big question?", "more than one")], cols=2),
     S("Synthesize", [OR("Big question: Why is “Courage” the right word for Grandfather's note? Use evidence from Parts 1, 2, and 3 of Hollow Hill.",
                         "Part 1: Pip needs courage to go to the hill. Part 2: she enters the dark tunnel. Part 3: she faces the village; Grandfather's own courage to share. Courage ties the story together.", lines=7)]),
     S("Chapter 10 Connection", [OR("How do the knights of the Round Table treat Galahad? Use evidence from two places in Chapter 10.", "Answers vary.", lines=4)]),
     S("Exit Ticket", [OR("Write one big question about the King Arthur Reader that needs evidence from more than one chapter.", "Answers vary.", lines=2)])],
    te("Students synthesize evidence across paragraphs.", "Refer to details and examples from across a text.", "Workbook Lesson 3.7",
       "Can one paragraph answer everything?", "Skim all three Hollow Hill parts.", ["Model synthesizing for the builders question."], "Your Turn 1–3.",
       ["Using one strong quote and stopping."], ["Three-part evidence organizer."], ["Synthesize across Chapters 9–10."]),
    summary="Combine evidence from several parts to answer big questions.")

L8 = Lesson("3.8", "Writing with Evidence from Across a Text",
    "I can write a paragraph that uses evidence from at least two parts of a text.", "W.4.9, W.4.2b",
    [],
    "How can you show a reader that your answer is backed up throughout the whole text?",
    [Text("Use ACE with <b>two</b> citations from different parts of the text, joined by transitions such as <i>at the beginning, later, in addition, by the end</i>."),
     Example("Two-citation ACE", "How does Pip show courage?", ["A: Pip shows courage again and again.", "C1: At the beginning, she keeps walking even though she almost turns back.", "C2: Later, she unlocks the door and follows the tunnel alone.", "E: Each time she is afraid, she chooses to keep going."],
             "Pip shows courage again and again. At the beginning, her legs feel heavy and she almost turns back, but she keeps walking. Later, she unlocks the stone door and follows the dark tunnel alone. Each time she is afraid, she chooses to keep going, which is what courage means."),
     KeyIdea("Use two pieces of evidence from different parts and connect them with transitions.")],
    [Problem("Name two transitions for linking evidence.", "at the beginning, later, in addition, by the end"), Problem("Why use two pieces of evidence?", "It shows the answer is true across the text."), Problem("Where should the explanation go?", "after the evidence")],
    [S("Warm-Up", [SA("ACE: A =", "Answer"), SA("A transition for the end of a story", "by the end, finally")], cols=2),
     S("Write", [OR("How does the village of Thornbury change across the story? Write an ACE paragraph with two pieces of evidence from different parts.", "Answers vary: fear of the hill (Part 1) to celebrating the maps (Part 3).", lines=9,
                    note="1 point each: answer; evidence 1; evidence 2 from a different part; explanation; transitions.")]),
     S("Exit Ticket", [OR("Underline the transitions you used.", "Student self-check.", lines=1)])],
    te("Students write with evidence from across a text.", "Draw evidence from texts; link ideas with words and phrases.", "Workbook Lesson 3.8",
       "Backed up throughout?", "Reread Parts 1 and 3.", ["Model the two-citation paragraph."], "Plan together.",
       ["Both citations from the same paragraph."], ["Color-code evidence by part."], ["Add a third citation."], independent="Write the paragraph. Weekly Check tomorrow."),
    summary="Two citations from different parts + transitions + explanation.")

# ================================================================= Week 3 · Explain a supported inference (Chapter 11)
L9 = Lesson("3.9", "Inferences and Predictions",
    "I can make predictions and inferences and revise them as I read.", "RL.4.1",
    [("prediction", "An inference about what will happen next.")],
    "Have you ever predicted the ending of a movie and been wrong? What made you change your mind?",
    [ReaderAssign(READER, "Chapter 11: How the Quest Began", "What is the quest? Predict what will happen to the knights."),
     Text("A <b>prediction</b> is an inference about what will happen. Good readers base predictions on clues and <b>revise</b> them when new information appears."),
     Example("Revise a prediction", "Hollow Hill", ["Part 1 clue: children whisper of dragons; Pip has a key. Prediction: she'll find something dangerous or a treasure.", "Part 2 new information: the room holds maps and a letter.", "Revise: the treasure is Grandfather's work, not gold."],
             "Predictions change as new clues appear; that's what good readers do."),
     KeyIdea("Predict from clues; confirm or revise as you read.")],
    [Problem("What clue in Part 1 suggested Pip would find a door?", "the drawing of a door on the map; the brass key"), Problem("Was the prediction “a dragon lives there” supported?", "No; there were no clues, only rumors."), Problem("Predict one thing that happens next in Chapter 12.", "Answers vary.")],
    [S("Warm-Up", [SA("A prediction is a kind of…", "inference"), SA("Can predictions change?", "Yes")], cols=2),
     S("Chapter 11", [OR("What is the quest? What clues tell you it will be hard?", "Answers vary; the Grail quest; supported by chapter clues.", lines=3),
                      OR("Make a prediction about which knight will succeed. Give a clue.", "Answers vary (e.g. Galahad; he is described as pure/chosen).", lines=3)]),
     S("Prediction Log", [OR("Prediction:", "Answers vary.", lines=1), OR("Clue:", "Answers vary.", lines=1), OR("After reading: confirmed or revised? Why?", "Answers vary.", lines=2)]),
     S("Exit Ticket", [OR("Why is it okay for a prediction to be wrong?", "Predictions are based on the clues available; new information can change them.", lines=2)])],
    te("Students predict and revise.", "Draw inferences from the text.", "King Arthur Reader (Chapter 11), workbook Lesson 3.9",
       "Wrong movie prediction.", "Read Chapter 11 with prediction stops.", ["Model revising a prediction with Hollow Hill."], "Your Turn 1–3.",
       ["Wild guesses with no clues."], ["Require a clue for every prediction."], ["Predict the ending of the whole reader."]),
    summary="Predictions are inferences; confirm or revise them as you read.")

L10 = Lesson("3.10", "Inferring the Theme of a Longer Story",
    "I can infer the theme of a longer story using evidence from the whole text.", "RL.4.2",
    [],
    "How is finding the theme of a long story different from finding it in a fable?",
    [Text("In fables, the lesson is often stated. In longer stories, the theme builds slowly. Look at what changes, what the characters learn, and what the title and ending suggest."),
     Example("Infer a theme", "“The Secret of Hollow Hill”", ["What Pip learns: courage leads to discovery.", "What Grandfather learns: sharing your work matters.", "What the village learns: fear came from not knowing."],
             "Possible themes: Courage helps us discover the truth. / Fear of the unknown can be overcome by facing it. / Sharing your gifts is better than hiding them."),
     KeyIdea("A long story can have more than one theme. Support your theme with evidence from several parts.")],
    [Problem("What theme does the mayor's change support?", "Fear of the unknown can be overcome by learning the truth."), Problem("What does the final paragraph suggest about courage?", "Both Pip and Grandfather needed courage."), Problem("Give one theme in your own words.", "Answers vary.")],
    [S("Warm-Up", [SA("Topic of Hollow Hill", "courage / sharing"), SA("Can a story have more than one theme?", "Yes")], cols=2),
     S("Theme with Evidence", [OR("Write a theme for “The Secret of Hollow Hill.” Support it with evidence from two different parts.", "e.g. Sharing your gifts brings people together: Grandfather hid his maps out of fear (Part 2); when Pip shared them, the village celebrated (Part 3).", lines=6)]),
     S("Chapter 11 Connection", [OR("What theme might the quest in Chapter 11 be building? Explain.", "Answers vary, e.g. true goodness matters more than strength.", lines=3)]),
     S("Exit Ticket", [OR("How does the title “The Secret of Hollow Hill” connect to the theme?", "The secret was something good hidden by fear; uncovering it shows the theme.", lines=2)])],
    te("Students infer themes in longer texts.", "Determine a theme of a story from details.", "Workbook Lesson 3.10",
       "Fable vs long story.", "Skim Hollow Hill.", ["Model themes from three characters."], "Your Turn 1–3.",
       ["Choosing a theme that fits only one scene."], ["Check: does it fit the whole story?"], ["Compare Hollow Hill's theme to Chapter 11's."]),
    summary="Long stories build themes slowly; support them with evidence from across the text.")

L11 = Lesson("3.11", "Inferring the Author's Ideas in Informational Text",
    "I can infer what an author thinks about a topic from the details and words chosen.", "RI.4.8, RI.4.1",
    [("author's point", "The idea the author wants readers to believe or understand.")],
    "If an author calls a building “breathtaking,” what does the author think of it?",
    [Text("Informational authors show their ideas through the details they include and the words they choose. Look for opinion words and the conclusion."),
     Example("Infer the author's point", "“How a Medieval Cathedral Was Built”", ["Word choice: “glowed with color.”", "Conclusion: they remind us what people could build “with patience, teamwork, and simple tools.”"],
             "The author admires the cathedral builders and thinks their work is impressive."),
     KeyIdea("Word choice and the conclusion reveal what the author thinks.")],
    [Problem("Which words show the author admires stained glass?", "“glowed with color”"), Problem("What does the author want us to remember?", "that people built amazing things with patience, teamwork, and simple tools"), Problem("Does the author say “I think”?", "No; the ideas are shown through details.")],
    [S("Warm-Up", [SA("What is an author's point?", "the idea the author wants readers to understand"), SA("Where do authors often state their main point?", "the conclusion")], cols=2),
     S("Infer the Author's Ideas", [OR("Reread “Honeybees in Winter” (Lesson 2.7). What does the author want readers to understand about honeybees? Give evidence.", "They survive through teamwork; “take turns,” and beekeepers should leave honey.", lines=4),
                                    OR("What does the author of “The Printing Press” (Lesson 2.14) think about the invention? Quote a word or phrase.", "It was hugely important: “one of the most important inventions in history.”", lines=3)]),
     S("Exit Ticket", [OR("Write a sentence about a topic you love using a word that shows your opinion.", "Answers vary.", lines=2)])],
    te("Students infer authors' points.", "Explain how an author uses reasons and evidence to support particular points.", "Workbook Lesson 3.11",
       "Breathtaking.", "Reread the cathedral conclusion.", ["Model inferring the author's point."], "Your Turn 1–3.",
       ["Confusing the topic with the author's point."], ["Ask: What does the author want me to think?"], ["Find opinion words in a newspaper article."]),
    summary="Details and word choice reveal the author's point.")

L12 = Lesson("3.12", "Explaining an Inference in Writing",
    "I can explain an inference in a paragraph with two pieces of evidence and clear reasoning.", "W.4.9, RL.4.1",
    [("reasoning", "The explanation of how evidence supports an idea.")],
    "What's the difference between saying “Pip is brave” and proving it?",
    [Text("Reasoning is the bridge between evidence and your inference. Strong reasoning uses <i>because</i>, <i>this shows</i>, or <i>this means</i>, and explains <b>how</b> the evidence proves the idea."),
     Example("Weak vs strong reasoning", "Inference: Grandfather trusted Pip.", ["Evidence: He wrote “For Pip. Courage.” on the map.", "Weak: This shows he trusted her.", "Strong: Leaving a secret message only she would find shows he believed she would understand it and be brave enough to follow it."],
             "Strong reasoning explains how the evidence proves the inference."),
     KeyIdea("Evidence + reasoning = proof. Explain HOW, not just THAT.")],
    [Problem("Reasoning word or phrase", "because, this shows, this means"), Problem("Is “This proves it” strong reasoning?", "No; it doesn't explain how."), Problem("What does reasoning connect?", "evidence and the inference")],
    [S("Warm-Up", [SA("What is reasoning?", "explaining how evidence supports an idea"), SA("Inference = clues + ?", "what I know")], cols=2),
     S("Write", [OR("Why did Grandfather leave the room to Pip instead of to the mayor or the village? Write an inference paragraph with two pieces of evidence and strong reasoning.",
                    "Answers vary: she never laughed, she asked questions (letter); she loved maps (Part 1).", lines=10, note="Score: inference (1), evidence (2), reasoning (1), conventions (1).")]),
     S("Exit Ticket", [OR("Highlight your best reasoning sentence and explain why it is strong.", "Answers vary.", lines=2)])],
    te("Students explain inferences with reasoning.", "Draw evidence from literary texts to support analysis and reflection.", "Workbook Lesson 3.12",
       "Saying vs proving.", "Reread Grandfather's letter.", ["Model weak vs strong reasoning."], "Plan together.",
       ["Repeating the evidence as reasoning."], ["Ask: How does this prove it?"], ["Peer review reasoning."], independent="Write the paragraph. Weekly Check tomorrow."),
    summary="Reasoning explains how evidence proves your inference.")

# ================================================================= Week 4 · Write an organized passage response (Chapter 12)
L13 = Lesson("3.13", "Understanding the Prompt",
    "I can break down a writing prompt to understand exactly what it asks.", "W.4.9, W.4.4",
    [("prompt", "A question or direction that tells you what to write."), ("task", "What the prompt asks you to do.")],
    "Have you ever answered a question and then realized you answered the wrong thing?",
    [ReaderAssign(READER, "Chapter 12: Sir Gawaine on the Quest", "How does Gawaine's quest go? What choices does he make?"),
     Text("Before writing, <b>break down the prompt</b>: circle the task words (<i>explain, describe, compare</i>), underline the topic, and box any requirements (number of examples, texts to use)."),
     Example("Break down a prompt", "“Explain how Pip changes from the beginning to the end of the story. Use at least two details from the text.”",
             ["Task word: <b>Explain</b> (tell how or why).", "Topic: how Pip changes, beginning to end.", "Requirement: at least two details."], "I need to explain Pip's change using at least two details: one from the beginning and one from the end."),
     KeyIdea("Circle the task, underline the topic, box the requirements, then restate the prompt in your own words.")],
    [Problem("Task word in “Compare the two stories”", "Compare"), Problem("Requirement in “Use two details”", "at least two details"), Problem("Restate: “Describe the setting of Chapter 12.”", "I need to tell where and when Chapter 12 happens, with details.")],
    [S("Warm-Up", [SA("What does a prompt do?", "tells you what to write"), SA("A task word", "explain, describe, compare")], cols=2),
     S("Break It Down", [OR(f"“{p}” Task: ___ Topic: ___ Requirements: ___", a, lines=2) for p, a in [
         ("Describe how cathedrals were built. Include at least three steps.", "Task: describe; Topic: how cathedrals were built; Req: three steps"),
         ("Compare Sir Gawaine and Galahad. Use evidence from Chapters 10–12.", "Task: compare; Topic: Gawaine and Galahad; Req: evidence from Ch. 10–12"),
         ("Explain why the villagers changed their minds about Hollow Hill.", "Task: explain; Topic: why villagers changed their minds; Req: (evidence implied)")]]),
     S("Chapter 12", [OR("What choices does Gawaine make on the quest? Give one detail.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Restate this prompt in your own words: “Explain what the quest shows about the knights of the Round Table.”", "e.g. I need to tell what the quest teaches us about what the knights are like, using evidence.", lines=2)])],
    te("Students analyze prompts.", "Produce writing in which development and organization fit task and purpose.", "King Arthur Reader (Chapter 12), workbook Lesson 3.13",
       "Answering the wrong question.", "Read Chapter 12.", ["Teach circle-underline-box.", "Model it."], "Your Turn 1–3.",
       ["Skipping part of the prompt."], ["Checklist from the prompt."], ["Write prompts for a sibling."]),
    summary="Circle the task, underline the topic, box the requirements.")

L14 = Lesson("3.14", "Planning an Organized Response",
    "I can plan a multi-paragraph response with an introduction, body, and conclusion.", "W.4.2a, W.4.4",
    [("introduction", "The first paragraph; states the main idea or answer."), ("body paragraph", "A paragraph with a reason and evidence."), ("conclusion", "The last paragraph; sums up the answer.")],
    "How is a long response like a sandwich?",
    [Text("An organized response has an <b>introduction</b> (restate the prompt and give your answer), <b>body paragraphs</b> (each with one point and evidence), and a <b>conclusion</b> (sum up)."),
     Figure(lambda t: table(t, [["Part", "What goes in it"], ["Introduction", "Restate the prompt; state your answer (claim)."], ["Body 1", "Point 1 + evidence + explanation"],
                                ["Body 2", "Point 2 + evidence + explanation"], ["Conclusion", "Restate the answer in new words; final thought."]], [1.3 * inch, 4.2 * inch], width=5.5 * inch)),
     Example("Plan", "Prompt: Explain how Pip changes. Use two details.", ["Intro: Pip changes from nervous to confident.", "Body 1: Beginning: she almost turns back.", "Body 2: End: she leads the village and becomes keeper.", "Conclusion: Courage helped her grow."],
             "A four-part outline ready to draft."),
     KeyIdea("Plan before you write: intro (answer), body (points + evidence), conclusion.")],
    [Problem("What goes in the introduction?", "restated prompt and your answer"), Problem("How many points per body paragraph?", "one"), Problem("What does a conclusion do?", "sums up the answer")],
    [S("Warm-Up", [SA("First paragraph =", "introduction"), SA("Last paragraph =", "conclusion")], cols=2),
     S("Plan Your Response", [OR("Prompt: Explain what the quest for the Grail shows about the knights of the Round Table. Use evidence from Chapters 11–12. Introduction (answer):", "Answers vary.", lines=3),
                              OR("Body 1 (point + evidence):", "Answers vary.", lines=3), OR("Body 2 (point + evidence):", "Answers vary.", lines=3), OR("Conclusion:", "Answers vary.", lines=2)]),
     S("Exit Ticket", [OR("Which part of your plan is strongest? Which needs more evidence?", "Answers vary.", lines=2)])],
    te("Students plan multi-paragraph responses.", "Introduce a topic clearly and group related information in paragraphs.", "Workbook Lesson 3.14",
       "Sandwich.", "Skim Chapters 11–12.", ["Teach the structure table.", "Model the Pip plan."], "Plan the quest response together.",
       ["Body paragraphs with no evidence."], ["Outline frame."], ["Add a third body paragraph."]),
    summary="Introduction → body paragraphs with evidence → conclusion.")

L15 = Lesson("3.15", "Drafting the Response",
    "I can draft a multi-paragraph response from my plan.", "W.4.2, W.4.9",
    [],
    "Why is it easier to write after you have a plan?",
    [Text("Turn each part of your plan into a paragraph. Indent each new paragraph. Use transitions between paragraphs: <i>First, Another reason, In addition, In conclusion</i>."),
     Example("Model introduction", "Prompt: Explain how Pip changes.", ["Restate: In “The Secret of Hollow Hill,” Pip changes a great deal.", "Answer: She grows from a nervous girl into a confident leader."],
             "In “The Secret of Hollow Hill,” Pip changes a great deal. She grows from a nervous girl who almost turns back into a confident leader who shares her grandfather's gift with the whole village."),
     KeyIdea("One paragraph per part of the plan. Indent and use transitions.")],
    [Problem("Transition for the second body paragraph", "Another reason, In addition"), Problem("Transition for the conclusion", "In conclusion, In the end"), Problem("How do you show a new paragraph?", "indent")],
    [S("Warm-Up", [SA("Transition to start body 1", "First"), SA("Transition for the conclusion", "In conclusion")], cols=2),
     S("Draft", [OR("Draft your response to the quest prompt from Lesson 3.14.", "Answers vary.", lines=22,
                    note="Look for: introduction with answer; two body paragraphs each with evidence from Chapters 11–12 and explanation; conclusion; transitions.")])],
    te("Students draft multi-paragraph responses.", "Write informative texts; link ideas within and across categories.", "Plans from Lesson 3.14, workbook Lesson 3.15",
       "Why plan first?", "Reread a model introduction.", ["Model turning the plan into an introduction."], "Students draft; conference.",
       ["Running everything into one paragraph."], ["Draft one paragraph at a time."], ["Add a counter-example."], independent="Finish the draft.", exit_="Share one transition sentence."),
    summary="Turn each plan part into a paragraph with transitions.")

L16 = Lesson("3.16", "Revising for Organization",
    "I can revise my response for clear organization, evidence, and transitions.", "W.4.5, W.4.2c",
    [],
    "If you moved one paragraph of your response, would it still make sense?",
    [Text("When revising a response, check the order of paragraphs, make sure every body paragraph has evidence and explanation, and add transitions where ideas jump."),
     Figure(lambda t: table(t, [["Revision checklist", "Yes / Not yet"], ["My introduction restates the prompt and answers it.", ""], ["Each body paragraph has one point, evidence, and explanation.", ""],
                                ["I used transitions between paragraphs.", ""], ["My conclusion restates the answer in new words.", ""], ["I indented each paragraph and edited capitals, punctuation, and spelling.", ""]],
                            [W * 0.72, W * 0.2], width=W * 0.92)),
     KeyIdea("Revise for organization first, then edit for conventions.")],
    [Problem("What should every body paragraph have?", "a point, evidence, and explanation"), Problem("Revise first or edit first?", "revise first"), Problem("Name a paragraph transition.", "Another reason, In addition, In conclusion")],
    [S("Warm-Up", [SA("Revising is about…", "ideas, organization, word choice"), SA("Editing is about…", "capitals, punctuation, spelling")], cols=2),
     S("Revise Your Draft", [OR("Use the checklist on your Lesson 3.15 draft. List two changes you made.", "Answers vary.", lines=4),
                             OR("Copy your strongest sentence of explanation.", "Answers vary.", lines=2)]),
     S("Exit Ticket", [OR("What did you learn about writing longer responses this unit?", "Answers vary.", lines=2)])],
    te("Students revise multi-paragraph responses.", "With guidance, develop and strengthen writing by revising and editing.", "Drafts, workbook Lesson 3.16, Unit 3 Review",
       "Would it make sense if moved?", "Read a draft aloud.", ["Teach the checklist."], "Revise with a partner.",
       ["Only fixing spelling."], ["One checklist item at a time."], ["Publish and share the response."], independent="Revise; then the Unit 3 Review.", exit_="Exit Ticket. Tomorrow: Unit 3 Test."),
    summary="Revise for organization, evidence, and transitions; then edit.")

# ================================================================= checks
C1 = Check("Weekly Check 7: Reading Longer Texts", [S("Read and answer", [
    MC("What point of view is this story told from?", ["first person", "third person"], 0),
    OR("Write the gist of paragraph 2.", "The narrator froze and forgot the line when the spotlight hit.", lines=1),
    OR("Explain the simile “My mouth felt as dry as sand.”", "The narrator's mouth was very dry from nervousness.", lines=1),
    OR("What helped the narrator say the line? Give evidence.", "Lucas's thumbs-up from the front row; the narrator took a breath and shouted the line.", lines=2),
    OR("Why does the narrator say “I didn't care” when the audience laughed?", "The narrator was proud of being brave and saying the line.", lines=2)], passage=P_C7)], minutes=20)

C2 = Check("Weekly Check 8: Tracking Evidence", [S("Read and answer", [
    OR("List the steps beavers follow to build their home, in order.", "Cut down trees; build a dam; the water forms a pond; build a lodge in the pond.", lines=2),
    OR("Why does the lodge have underwater entrances?", "so predators like wolves cannot easily get in", lines=1),
    OR("Use evidence from two paragraphs to explain why beavers are called “engineers.”", "They cut trees and build dams that make ponds (par. 1–2) and build lodges with underwater entrances (par. 3).", lines=3),
    OR("How do beavers help other animals?", "Their ponds make wetlands where fish, frogs, ducks, and insects live.", lines=2)], passage=P_C8)], minutes=20)

C3 = Check("Weekly Check 9: Inference", [S("Read and answer", [
    OR("Why do you think Grandpa set a fifth place? Give two clues.", "He was waiting for someone to come home; he glanced at the door; he jumped up at the knock.", lines=3),
    OR("Who is the man at the door likely to be? Explain your reasoning.", "A family member, probably Grandpa's son, coming home from the army; Grandpa hugs him for a long time.", lines=3),
    OR("How does Grandpa feel when he sees the man? Evidence?", "overjoyed and relieved; jumped up so fast his napkin fell; long hug", lines=2),
    MC("What is the best theme?", ["Dinner is important.", "Hope can keep a family together while they wait.", "Soldiers wear uniforms."], 1)], passage=P_C9)], minutes=20)

REVIEW = Check("Unit 3 Review", [
    S("Skills", [SA("What is the gist?", "the general idea of a section"), SA("Symbol for a question while annotating", "?"), SA("First-person pronouns", "I, me, my"),
                 SA("Name two fix-up strategies", "reread, visualize"), SA("Parts of an organized response", "introduction, body, conclusion"), SA("Task word in “Explain why…”", "explain")], cols=2),
    S("Apply", [OR("Reread “How a Medieval Cathedral Was Built.” Explain why scaffolds were needed.", "Workers needed to stand on them to reach high places as the walls rose.", lines=2),
                OR("Plan (don't write) an organized response to: “Explain how Grandfather's letter changes the story.”", "Intro: the letter reveals the secret and gives Pip the room. Body: explains why he hid the maps; leads Pip to share them. Conclusion.", lines=4)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 3 Test", [
    S("Part A · Reading a longer text (1 point each)", [
        OR("Write the gist of paragraph 1.", "Chicago was mostly wooden and very dry in 1871.", lines=1),
        OR("Explain why the fire spread so quickly. Use evidence from two paragraphs.", "Wooden buildings and dry summer (par. 1); strong winds and flying burning wood (par. 2–3).", lines=3, points=2),
        MC("What point of view is this text written in?", ["first person", "third person"], 1),
        OR("What did people do to escape the heat?", "Some waded into Lake Michigan.", lines=1),
        OR("How was the rebuilt city different? Why?", "It used more brick, stone, and iron so it wouldn't burn as easily.", lines=2)], passage=P_TEST),
    S("Part B · Inference (1 point each)", [
        OR("What can you infer about Chicago's firefighters in 1871? Give a clue.", "They didn't have enough equipment to stop such a big fire; “only a few horse-drawn engines.”", lines=2),
        OR("What is the author's point in the last two paragraphs? Quote a phrase.", "Chicago overcame disaster and became stronger: “rose from the ashes stronger than before.”", lines=2),
        MC("Which conclusion is BEST supported?", ["The fire was caused by a cow.", "Chicago's people were determined to rebuild.", "Chicago never recovered."], 1)]),
    S("Part C · Organized response (6 points)", [OR("Prompt: Explain how the Great Chicago Fire changed the city. Write an introduction, two body paragraphs with evidence, and a conclusion.",
                                                   "Rubric: introduction with answer (1); body 1 with evidence (1) and explanation (1); body 2 with evidence and explanation (1); conclusion (1); transitions and conventions (1).",
                                                   lines=20, points=6)])],
    kind="test", minutes=50, rubric=[["13–15 (85%+)", "Mastered."], ["10–12", "Proficient; review missed skills."], ["Below 10", "Reteach organization or evidence and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-12-14", "2027-01-04", "2027-01-11", "2027-01-18"], CHECKS, REVIEW, TEST)

UNIT = Unit(3, "Reading Longer Texts", "Stamina, annotation, point of view, tracking evidence, inference, and organized written responses, with King Arthur Chapters 9–12.",
    "Longer texts ask more of readers: staying focused, keeping track of characters and ideas, and pulling evidence together from many places. In this unit you will read a three-part adventure story, a history of cathedral building, and the beginning of the Grail quest, and you will write your first multi-paragraph responses.",
    ["Read long texts in chunks and annotate them.", "Use fix-up strategies and identify point of view.", "Track characters and ideas across a text and synthesize evidence.",
     "Explain inferences with evidence and reasoning.", "Plan, draft, and revise an organized multi-paragraph response."],
    [("RL.4.1, RI.4.1", "Refer to details and draw inferences."), ("RL.4.3, RI.4.3", "Describe characters in depth; explain events and procedures."), ("RL.4.6", "Compare first- and third-person points of view."),
     ("RI.4.8", "Explain how an author uses reasons and evidence."), ("W.4.2, W.4.4, W.4.5, W.4.9", "Write organized informative responses with evidence; revise.")],
    [("stamina", "Ability to keep going."), ("annotate", "Mark a text while reading."), ("narrator", "The voice telling the story."), ("synthesize", "Combine information."), ("reasoning", "How evidence supports an idea.")],
    ["Unit 2: evidence, inference, theme, summary."], ["King Arthur and the Round Table Reader (Chapters 9–12)", "Sticky notes, pencils, highlighters"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Long reading assignments, research projects, and tests all require stamina, organized notes, and clear written answers.",
    family_note="Read a long chapter book together this month. Stop now and then and ask, “What's the gist so far?”",
    weeks=WEEKS)
