"""Grade 4 ELA · Unit 5: Reading Deeply — long literary and informational texts, text features, comparing structure and viewpoint, and the comparison essay.
Anchor reading: Treasure Island Reader, Chapters 5–7 and the Blackbeard selection (Feb 22 – Mar 26, 2027)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule
from content.ela4.unit01 import S, MC, OR, SA
from content.ela4.unit04 import TI


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


# ================================================================= passages
P_CASTAWAY = Passage("The Castaway of Pelican Key", [
    "The storm had wrecked the little supply boat, and when Eli woke, he was lying on warm sand with seaweed tangled in his hair. The boat was gone. The crew was gone. All he could see was a curve of white beach, a cluster of palm trees, and the endless blue ocean.",
    "“Hello?” he called. Only the pelicans answered, squawking from the rocks.",
    "For the first few days, Eli was too frightened to do anything but sit and stare at the horizon, hoping to see a sail. But his stomach growled, and his lips cracked from thirst. He knew that if he waited much longer, he would not survive.",
    "So he made a plan. He followed the pelicans to a freshwater pool behind the rocks. He cracked coconuts with a heavy stone. He wove palm fronds into a roof and built a shelter against the cliff. Every morning, he scratched a line on a flat rock to count the days.",
    "By the thirtieth line, Eli had become a different boy. His arms were brown and strong. He could catch fish with a sharpened stick and build a fire with dry grass and two stones. He even talked to the pelicans, naming the biggest one Captain.",
    "Still, every evening, he climbed the cliff to watch the sea. And on the forty-second evening, he saw it: a white sail, tiny as a gull's feather, far out on the water.",
    "Eli piled every branch he could find on the cliff top and lit the biggest fire he had ever made. Smoke climbed into the orange sky. The sail grew larger. It turned toward the island.",
    "When the sailors rowed ashore, they found a tall, sunburned boy waiting on the beach with a pelican at his side. “We thought you were lost,” said the captain. Eli smiled. “I was,” he said. “But I found my way.”",
], source="An original story", genre="Adventure story")

P_STARS = Passage("Finding the Way: How Sailors Navigated", [
    "<b>Lost at Sea</b>",
    "Today, ships use satellites to know exactly where they are. But for most of history, sailors crossed oceans with no land in sight and no GPS. How did they find their way? They used the sky, simple tools, and a great deal of skill.",
    "<b>Reading the Stars</b>",
    "In the Northern Hemisphere, sailors relied on the North Star, also called Polaris. Unlike other stars, it barely moves across the night sky. By measuring how high Polaris was above the horizon, a navigator could tell how far north the ship was. This measurement is called <b>latitude</b>.",
    "<b>The Compass</b>",
    "A compass has a magnetized needle that always points north. Chinese inventors were using compasses by around 1100, and the tool soon spread to sailors in Europe. With a compass, sailors could keep a steady direction even on cloudy nights when the stars were hidden.",
    "<b>Measuring Speed</b>",
    "To figure out how fast a ship was moving, sailors tossed a piece of wood tied to a long rope over the side. The rope had knots tied at equal distances. A sailor counted how many knots slipped through his hands while a small sand timer ran out. That is why a ship's speed is still measured in <b>knots</b> today.",
    "<b>Putting It Together</b>",
    "By combining direction, speed, and time, a navigator could estimate the ship's position on a map. This method, called <b>dead reckoning</b>, was not perfect. A strong current or a storm could push a ship far off course. That is why sailors on long voyages always watched for birds, floating plants, and changes in the color of the water, all signs that land might be near.",
], source="An original informational text", genre="Informational text", numbered=False)

P_LETTERS = Passage("Letters from Camp", [
    "<b>July 2.</b> Dear Mom and Dad, Camp is okay, I guess. The food is weird and my bunk is squeaky. A boy named Theo snores like a bear. I miss home. Love, Sam",
    "<b>July 5.</b> Dear Mom and Dad, Today we went canoeing! Theo and I tipped over in the middle of the lake, and we laughed so hard we couldn't swim for a minute. The counselor said we were the soggiest team she'd ever seen. Love, Sam",
    "<b>July 9.</b> Dear Mom and Dad, Can I stay for a second session? Theo is staying, and we're building a raft. Also, I don't even notice the squeaky bunk anymore. Love, Sam",
], source="An original story told in letters", genre="Epistolary story", numbered=False)

P_NARR_A = Passage("The Broken Vase · Told by Leo", [
    "I swear I didn't mean to. I was just practicing my soccer kick in the hallway, the ball bounced off the wall, and the vase wobbled and fell. When Mom came in, I froze. My sister pointed at me before I could say a word. Thanks a lot, Mia.",
], source="An original example", genre="First-person narrator", numbered=False)
P_NARR_B = Passage("The Broken Vase · Told by Mia", [
    "I told Leo a hundred times not to kick the ball inside. Then I heard a crash. When Mom walked in, Leo looked like a statue, so I pointed. Somebody had to tell the truth. Later, I helped him glue the pieces back together, because that's what sisters do.",
], source="An original example", genre="First-person narrator", numbered=False)

P_LIGHT_A = Passage("Text A: The Keepers of the Light", [
    "In the 1800s, lighthouse keepers lived lonely lives on rocky islands and windy points. Every evening, the keeper climbed the tower to light the lamp, and every few hours through the night, he or she climbed again to trim the wick and refill the oil.",
    "Some keepers became heroes. In 1838, Grace Darling, the daughter of an English keeper, rowed through a storm with her father to rescue survivors of a shipwreck. Her bravery made her famous.",
    "Many keepers were women. When a keeper died, his wife or daughter often took over the job, and some served for decades.",
], source="An original informational text", genre="Informational text")
P_LIGHT_B = Passage("Text B: How a Lighthouse Works", [
    "A lighthouse has three main parts: a tall tower, a lamp, and a lens. The tower raises the light so it can be seen far out at sea, because the earth curves and a low light would be hidden below the horizon.",
    "The lens is the most important part. In 1822, a French scientist named Augustin Fresnel designed a lens made of many glass rings. It bent and focused the light into a strong beam that could be seen more than 20 miles away.",
    "Each lighthouse flashes in its own pattern, such as two flashes every ten seconds. Sailors use these patterns to tell which lighthouse they are seeing, and therefore where they are.",
], source="An original informational text", genre="Informational text")

P_C13 = Passage("The Kite Contest", [
    "Every spring, Jada's town held a kite contest. This year she had built her own kite from sticks, newspaper, and an old red scarf.",
    "On contest day, the wind was strong. The fancy store-bought kites soared high, and Jada's homemade kite crashed twice. Some kids laughed. Jada's cheeks burned, but she checked the knots, added a longer tail, and tried again.",
    "The third time, the red kite climbed and climbed until it was higher than all the others. When the judges announced the prize for “Most Creative Kite,” Jada's grin was wider than the sky.",
], source="An original story", genre="Realistic fiction")

P_C14 = Passage("The Monarch Migration", [
    "<b>A Long Journey</b>",
    "Every fall, millions of monarch butterflies fly from Canada and the United States to forests in the mountains of Mexico. Some travel nearly 3,000 miles.",
    "<b>A Winter Home</b>",
    "In Mexico, the monarchs cluster together on fir trees, so many that the branches bend under their weight. The cool mountain air lets them rest without using up their energy.",
    "<b>Danger Ahead</b>",
    "Monarchs face many dangers, including the loss of milkweed, the only plant their caterpillars eat. Many people now plant milkweed in their gardens to help.",
], source="An original informational text", genre="Informational text", numbered=False)

P_C15A = Passage("Text A: The Owl", [
    "Owls are skilled night hunters. Their huge eyes gather light, and their soft feathers let them fly almost silently. An owl can hear a mouse moving under the snow.",
], source="An original informational text", genre="Informational text", numbered=False)
P_C15B = Passage("Text B: The Hawk", [
    "Hawks hunt during the day. Their sharp eyesight lets them spot a rabbit from high in the sky. Then they dive at speeds of more than 100 miles per hour.",
], source="An original informational text", genre="Informational text", numbered=False)

P_TEST_A = Passage("Text A: The Iditarod", [
    "Every March, mushers and their sled dogs race about 1,000 miles across Alaska in the Iditarod. The trail crosses frozen rivers, mountains, and lonely tundra.",
    "The race honors a famous trip in 1925. A sickness called diphtheria broke out in the town of Nome, and the medicine needed to stop it was hundreds of miles away. With no roads and planes unable to fly in the cold, teams of sled dogs carried the medicine in a relay. They made the trip in about five and a half days.",
    "Today, mushers spend more than a week on the trail. They care for their dogs first, feeding them and checking their paws at every stop.",
], source="An original informational text", genre="Informational text")
P_TEST_B = Passage("Text B: Balto's Run · A Story", [
    "The wind howled across the ice, so cold it stung like needles. Gunnar Kaasen could barely see his own hands. “Balto, take us home,” he whispered to the lead dog.",
    "Balto pressed his nose to the snow. Even in the whiteout, he found the trail. When the sled almost slid onto thin ice, Balto stopped short and refused to go on, then led the team around the danger.",
    "At dawn, the team pulled into Nome. Kaasen fell to his knees beside Balto, pulling ice from the dog's paws. “You saved them,” he said. “You saved them all.”",
], source="An original story based on a real event", genre="Historical fiction")

# ================================================================= Week 1 · A longer literary text (Chapter 5)
L1 = Lesson("5.1", "Plot Structure",
    "I can identify the parts of a plot in a longer story.", "RL.4.3, RL.4.5",
    [("exposition", "The beginning: characters, setting, and the situation."), ("rising action", "Events that build the problem."), ("climax", "The turning point; the most exciting moment."),
     ("falling action", "Events after the climax."), ("resolution", "How the problem is solved and the story ends.")],
    "Think of your favorite movie. When was the most exciting moment?",
    [ReaderAssign(TI, "Chapter 5: The Man on the Island", "Who does Jim meet? How long has this man been on the island?"),
     Text("Most stories follow a <b>plot structure</b> that rises to a <b>climax</b> and falls to a <b>resolution</b>, like a mountain."),
     Figure(lambda t: plot_arc(t, ["Exposition", "Rising action", "Climax", "Falling action", "Resolution"])),
     P_CASTAWAY,
     Example("Find the climax", "“The Castaway of Pelican Key”", ["Rising action: Eli finds water, builds shelter, survives 42 days.", "Turning point: he sees the sail and lights the fire; will they see it?", "After: the boat turns and rows ashore."],
             "The climax is when Eli lights the signal fire and the sail turns toward the island."),
     KeyIdea("Exposition → rising action → climax → falling action → resolution.")],
    [Problem("Exposition of the story", "Eli wakes alone on an island after a storm wrecked his boat."), Problem("One rising-action event", "finding fresh water; building a shelter; learning to fish"),
     Problem("Resolution", "Sailors rescue Eli; he says he “found his way.”")],
    [S("Warm-Up", [SA("The turning point is the…", "climax"), SA("The beginning that introduces characters is the…", "exposition")], cols=2),
     S("Map the Plot", [OR(f"{part}:", a, lines=2) for part, a in [("Exposition", "Eli wakes alone on the beach of an island after a storm."), ("Rising action (two events)", "He finds water, builds a shelter, counts days, learns to fish and make fire."),
                                                                   ("Climax", "He sees a sail and lights a huge signal fire."), ("Falling action", "The sail grows larger and turns toward the island."),
                                                                   ("Resolution", "Sailors find him; he is rescued, changed and confident.")]], passage=P_CASTAWAY),
     S("Chapter 5", [OR("Describe the man Jim meets in Chapter 5. What is surprising about him?", "Ben Gunn, a marooned man who has lived alone on the island for years; he looks wild and craves cheese.", lines=3, note="Accept accurate details from Chapter 5.")]),
     S("Exit Ticket", [OR("Why does the story end with “I found my way”? What does Eli mean?", "He survived on his own and grew stronger and braver; he found his way in life, not just home.", lines=2)])],
    te("Students identify plot structure.", "Describe in depth an event; explain the structure of stories.", "Treasure Island Reader (Chapter 5), workbook Lesson 5.1",
       "Most exciting movie moment.", ["Read Chapter 5.", "Read “The Castaway of Pelican Key.”"], ["Teach the plot arc.", "Model the climax."], "Your Turn 1–3.",
       ["Calling the first exciting event the climax."], ["Ask: When does everything change?"], ["Plot the whole Treasure Island so far."]),
    summary="Plot: exposition, rising action, climax, falling action, resolution.")

L2 = Lesson("5.2", "Analyzing a Character in Depth",
    "I can describe a character in depth using what the character says, does, thinks, and how others react.", "RL.4.3",
    [("characterization", "How an author shows what a character is like.")],
    "How do you get to know a new friend? What do you notice?",
    [Text("Authors reveal characters through <b>STEAL</b>: <b>S</b>peech, <b>T</b>houghts, <b>E</b>ffect on others, <b>A</b>ctions, and <b>L</b>ooks."),
     Figure(lambda t: table(t, [["STEAL", "Eli (The Castaway)", "What it shows"], ["Speech", "“I was. But I found my way.”", "confident, thoughtful"], ["Thoughts", "He knew if he waited longer, he wouldn't survive.", "realistic"],
                                ["Effect on others", "Sailors expected a lost boy; they find him waiting.", "independent"], ["Actions", "builds shelter, fishes, makes fire", "resourceful, hardworking"],
                                ["Looks", "tall, sunburned, strong arms", "changed by the island"]], [1.2 * inch, 2.5 * inch, 1.8 * inch], width=5.5 * inch, font_size=9)),
     KeyIdea("Use STEAL to find evidence about a character from many parts of the story.")],
    [Problem("Which STEAL letter is “He talked to the pelicans”?", "A (Actions)"), Problem("What trait does naming a pelican Captain show?", "humor; loneliness; creativity"), Problem("How does Eli change?", "from frightened and helpless to strong and resourceful")],
    [S("Warm-Up", [SA("S in STEAL", "Speech"), SA("L in STEAL", "Looks")], cols=2),
     S("STEAL Ben Gunn", [OR(f"{x}: what Ben Gunn {y} (Chapter 5)", "Answers vary; must come from Chapter 5.", lines=2) for x, y in [("Speech", "says"), ("Actions", "does"), ("Looks", "looks like"), ("Effect on others", "makes Jim feel")]]),
     S("Write", [OR("What kind of person is Ben Gunn? Use evidence from two STEAL categories.", "Answers vary.", lines=4)]),
     S("Exit Ticket", [OR("Compare Eli and Ben Gunn in one sentence.", "e.g. Both were castaways, but Eli grew stronger and calmer, while Ben Gunn became wild and odd from loneliness.", lines=2)])],
    te("Students analyze characters with STEAL.", "Describe in depth a character, drawing on specific details.", "Workbook Lesson 5.2",
       "Getting to know a friend.", "Reread parts of Chapter 5.", ["Teach STEAL with the Eli chart."], "Your Turn 1–3.",
       ["Using only one type of evidence."], ["STEAL chart template."], ["STEAL a character from your own reading."]),
    summary="STEAL: Speech, Thoughts, Effect on others, Actions, Looks.")

L3 = Lesson("5.3", "How Setting Shapes a Story",
    "I can explain how the setting affects the characters and events.", "RL.4.3",
    [],
    "Would “The Castaway of Pelican Key” work if it happened in a city?",
    [Text("Setting is more than a backdrop. It can create problems (a storm, an island), shape what characters can do, and affect the mood."),
     Example("Setting and plot", "How does the island setting shape the story?", ["Problem: Eli is alone with no food or shelter.", "Actions: he must use what the island has: coconuts, palm fronds, fish.", "Change: surviving there makes him stronger."],
             "The island creates Eli's problem, determines how he survives, and causes him to grow."),
     KeyIdea("Ask: What problems does the setting cause? How do characters respond? How does it affect the mood?")],
    [Problem("What problem does the setting create in Treasure Island?", "The island is dangerous and the pirates are there; it's far from help."), Problem("How did the setting help Eli?", "fresh water, coconuts, fish, palm fronds"), Problem("What mood does a deserted island create?", "lonely, mysterious, dangerous")],
    [S("Warm-Up", [SA("What is setting?", "when and where a story happens"), SA("Setting of Treasure Island Ch. 5", "the island")], cols=2),
     S("Setting Analysis", [OR("Choose two details of the island setting in Chapter 5. Explain how each affects Jim or Ben Gunn.", "Answers vary.", lines=4),
                            OR("How would Eli's story change if it took place in a snowy forest?", "Different problems (cold), different survival actions (shelter for warmth), possibly a different mood.", lines=3)]),
     S("Exit Ticket", [OR("Why do you think so many adventure stories take place on islands?", "Islands isolate characters, create danger and mystery, and force them to solve problems.", lines=2)])],
    te("Students analyze setting.", "Describe in depth a setting, drawing on specific details.", "Workbook Lesson 5.3",
       "City castaway?", "Reread the island descriptions.", ["Model setting → problem → response."], "Your Turn 1–3.",
       ["Listing setting details without explaining effects."], ["Setting-effect T-chart."], ["Draw a map of Treasure Island using the text."]),
    summary="Settings create problems, shape actions, and set the mood.")

L4 = Lesson("5.4", "Summarizing a Long Story",
    "I can summarize a long story using its plot structure.", "RL.4.2",
    [],
    "How can you summarize a story that took you a whole week to read?",
    [Text("Use the plot arc as a summary plan: one sentence for the exposition, one or two for the rising action, one for the climax, and one for the resolution. Leave out minor details."),
     Example("Plot-arc summary", "“The Castaway of Pelican Key”",
             ["Exposition: After a storm, Eli washes up alone on an island.", "Rising action: Scared at first, he learns to find water, build a shelter, and fish.", "Climax: On the 42nd evening, he sees a sail and lights a signal fire.", "Resolution: Sailors rescue him, and he realizes he has grown."],
             "After a storm, Eli washes up alone on an island. Scared at first, he learns to find water, build a shelter, and fish. On the forty-second evening, he spots a sail and lights a huge signal fire. Sailors rescue him, and Eli realizes he has grown strong and brave."),
     KeyIdea("Plot-arc summary: exposition, rising action, climax, resolution, in four or five sentences.")],
    [Problem("How many sentences for a plot-arc summary?", "about four or five"), Problem("Include that Eli named a pelican?", "No, it's a minor detail."), Problem("What part of the plot is the most important to include?", "the climax (and resolution)")],
    [S("Warm-Up", [SA("Climax =", "turning point"), SA("Resolution =", "how it ends")], cols=2),
     S("Summarize", [OR("Write a plot-arc summary of Treasure Island Chapters 1–5.", "Answers vary: Jim at the inn with the captain; pirates and the map; the voyage; Silver's plot overheard; Jim meets Ben Gunn.", lines=7)]),
     S("Exit Ticket", [OR("What's one detail you left out of your summary, and why?", "Answers vary.", lines=2)])],
    te("Students summarize long stories.", "Summarize the text.", "Workbook Lesson 5.4",
       "Summarizing a week-long read.", "Skim Chapters 1–5.", ["Model the plot-arc summary."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Too many details."], ["One sentence per plot part."], ["Summarize the whole book at the end."]),
    summary="Use the plot arc to summarize long stories.")

# ================================================================= Week 2 · A longer informational text (Blackbeard)
L5 = Lesson("5.5", "Text Features",
    "I can use text features to find and understand information.", "RI.4.7, RI.4.5",
    [("text features", "Parts of a text that help readers find and understand information, such as headings, captions, and bold words."), ("heading", "A title for a section."),
     ("caption", "Words that explain a picture."), ("sidebar", "A box of extra information beside the main text.")],
    "When you open a science book, what do you look at before reading?",
    [ReaderAssign(TI, "Informational selection: Blackbeard", "Use the headings, pictures, and captions to preview before reading."),
     Text("Informational texts use <b>text features</b>. Preview them before reading: they show what the text is about and help you find information fast."),
     Figure(lambda t: table(t, [["Feature", "How it helps"], ["Title and headings", "tell the topic of the text and each section"], ["Bold words", "show important vocabulary"], ["Photos and captions", "show and explain"],
                                ["Maps, diagrams, charts", "show information visually"], ["Timeline", "shows events in order"], ["Sidebar", "adds extra related facts"], ["Glossary and index", "define words; locate topics"]],
                            [1.9 * inch, 3.4 * inch], width=5.3 * inch)),
     P_STARS,
     Example("Use headings", "Where would you look to learn why speed is measured in knots?", ["Scan the headings.", "“Measuring Speed” fits."], "the section “Measuring Speed”"),
     KeyIdea("Preview text features first. Use headings to find information; use bold words for key vocabulary.")],
    [Problem("Which section explains the compass?", "“The Compass”"), Problem("Name a bold word and its meaning.", "latitude: how far north; knots: speed; dead reckoning: estimating position"), Problem("What is the purpose of headings?", "to tell what each section is about")],
    [S("Warm-Up", [SA("Words that explain a picture", "caption"), SA("A title for a section", "heading")], cols=2),
     S("Use the Features", [OR("List the five headings. Under which heading would you find information about storms pushing ships off course?", "Lost at Sea; Reading the Stars; The Compass; Measuring Speed; Putting It Together. Storms: Putting It Together.", lines=3),
                            OR("Why was the North Star useful? Use the text.", "It barely moves, so measuring its height told sailors their latitude.", lines=2),
                            OR("What is dead reckoning, and why wasn't it perfect?", "estimating position from direction, speed, and time; currents and storms could push ships off course", lines=2)], passage=P_STARS),
     S("Blackbeard", [OR("List three text features in the Blackbeard selection and what each taught you.", "Answers vary.", lines=3)])],
    te("Students use text features.", "Interpret information presented visually; describe text structure.", "Treasure Island Reader (Blackbeard selection), workbook Lesson 5.5",
       "What do you look at first?", ["Preview the Blackbeard selection's features; then read it.", "Read “Finding the Way.”"], ["Teach the feature chart."], "Your Turn 1–3.",
       ["Skipping captions and headings."], ["Feature scavenger hunt."], ["Add a sidebar to “Finding the Way.”"]),
    summary="Headings, bold words, captions, diagrams, timelines, and sidebars help readers.")

L6 = Lesson("5.6", "Reading Charts, Diagrams, and Timelines",
    "I can explain how information in a chart, diagram, or timeline adds to a text.", "RI.4.7",
    [("chart", "Information organized in rows and columns."), ("timeline", "A line showing events in time order.")],
    "Why might an author add a timeline instead of just writing the dates in a paragraph?",
    [Text("Visual information lets readers see patterns quickly. Read the title, labels, and every row or point. Then ask: <i>What does this show that the words don't?</i>"),
     Figure(lambda t: table(t, [["Navigation tool", "Invented or first used", "What it measured"], ["Compass", "China, about 1100", "direction"], ["Astrolabe", "used at sea by the 1400s", "height of stars or sun (latitude)"],
                                ["Log and line (knots)", "1500s", "speed"], ["Chronometer (sea clock)", "1700s", "time, which helped find longitude"]], [1.7 * inch, 1.9 * inch, 2.0 * inch], width=5.6 * inch, font_size=9),
            caption="Chart: Tools Sailors Used"),
     Figure(lambda t: timeline_fig(t, [("1100", "Compass used in China"), ("1400s", "Astrolabes at sea"), ("1500s", "Knots measured"), ("1700s", "Chronometer"), ("1900s", "Radio navigation"), ("1990s", "GPS")]),
            caption="Timeline: How Navigation Changed"),
     Example("Use the chart", "Which tool helped sailors find longitude?", ["Find the column “What it measured.”", "Row: chronometer: time, which helped find longitude."], "the chronometer (sea clock)"),
     KeyIdea("Read titles and labels first. Explain what the visual adds to the text.")],
    [Problem("What did an astrolabe measure?", "height of stars or sun (latitude)"), Problem("Which came first: knots or the chronometer?", "knots (1500s)"), Problem("What does the timeline show that the article doesn't?", "how navigation kept changing up to GPS today")],
    [S("Warm-Up", [SA("Rows and columns =", "chart"), SA("Events in order on a line =", "timeline")], cols=2),
     S("Read the Visuals", [SA(q, a) for q, a in [("Oldest tool on the chart", "compass"), ("Tool for measuring speed", "log and line (knots)"), ("When was GPS developed?", "1990s"),
                                                  ("How many years between the compass and the chronometer (about)?", "about 600 years")]], cols=2),
     S("Explain", [OR("How does the chart add to “Finding the Way”?", "It adds tools and dates the article doesn't mention (astrolabe, chronometer) and organizes them by what they measured.", lines=3)]),
     S("Exit Ticket", [OR("Make a three-event timeline of your own day.", "Answers vary.", lines=3)])],
    te("Students interpret charts and timelines.", "Interpret information presented visually and explain how it contributes to understanding.", "Workbook Lesson 5.6",
       "Why a timeline?", "Review the chart and timeline.", ["Model reading the chart."], "Your Turn 1–3.",
       ["Ignoring titles and labels."], ["Point to the label before answering."], ["Make a timeline of Blackbeard's life."]),
    summary="Charts and timelines show information visually; explain what they add.")

L7 = Lesson("5.7", "Main Ideas of Sections and the Whole Text",
    "I can find the main idea of each section and of the whole text.", "RI.4.2",
    [],
    "How is the main idea of one section different from the main idea of the whole article?",
    [Text("In a long text with headings, each section has its own main idea. The main idea of the whole text connects them all."),
     Figure(lambda t: table(t, [["Section", "Main idea"], ["Reading the Stars", "Sailors measured the North Star to find latitude."], ["The Compass", "A compass helped sailors keep direction."],
                                ["Measuring Speed", "Knotted ropes measured speed."], ["Putting It Together", "Sailors combined these to estimate position, though it wasn't perfect."],
                                ["Whole text", "Before GPS, sailors used the sky, simple tools, and skill to navigate."]], [1.8 * inch, 3.8 * inch], width=5.6 * inch)),
     KeyIdea("Section main ideas are the building blocks; the whole-text main idea connects them.")],
    [Problem("Main idea of “Lost at Sea”", "Sailors navigated without GPS using the sky, tools, and skill."), Problem("Which section's main idea is about direction?", "The Compass"), Problem("Main idea of the whole text", "Before GPS, sailors used the sky, simple tools, and skill to find their way.")],
    [S("Warm-Up", [SA("Does each section have a main idea?", "Yes"), SA("What connects section main ideas?", "the main idea of the whole text")], cols=2),
     S("Blackbeard", [OR("Write the main idea of two sections of the Blackbeard selection.", "Answers vary.", lines=4), OR("Write the main idea of the whole selection.", "Answers vary.", lines=2)]),
     S("Summary", [OR("Summarize “Finding the Way” in three sentences using the section main ideas.", "Before GPS, sailors used the North Star to find latitude and a compass to keep direction. They measured speed with knotted ropes. Combining these, they estimated their position, though storms could push them off course.", lines=4)])],
    te("Students identify section and whole-text main ideas.", "Determine the main idea and explain how it is supported; summarize.", "Workbook Lesson 5.7",
       "Section vs whole.", "Reread one section at a time.", ["Model the section chart."], "Your Turn 1–3.",
       ["Using one section's idea as the whole text's main idea."], ["Chart by heading."], ["Write headings for an article that has none."]),
    summary="Each section has a main idea; the whole-text main idea connects them.")

L8 = Lesson("5.8", "Integrating Information to Explain a Topic",
    "I can combine information from a text and its visuals to explain a topic.", "RI.4.7, RI.4.9, W.4.2",
    [("integrate", "Combine information from different sources.")],
    "If you had to teach a younger child about navigation, what would you include?",
    [Text("Integrate means using the words, the chart, and the timeline together. Good explanations use details from each source and name where they came from."),
     Example("Integrate", "How did navigation tools improve over time?", ["Article: compass for direction; knots for speed; dead reckoning not perfect.", "Chart: astrolabe and chronometer added latitude and longitude.", "Timeline: radio and GPS made it exact."],
             "Navigation improved from the compass and star measurements, to tools like the chronometer for longitude, to radio and finally GPS, which shows exact location."),
     KeyIdea("Combine words and visuals; name your sources.")],
    [Problem("Which source tells about GPS?", "the timeline (and the first section)"), Problem("Which source explains dead reckoning?", "the article"), Problem("What does integrate mean?", "combine information from different sources")],
    [S("Warm-Up", [SA("Integrate means", "combine information"), SA("Name one visual source", "chart, timeline")], cols=2),
     S("Write", [OR("Write an informational paragraph explaining how sailors found their way before GPS. Use at least one detail from the article and one from the chart or timeline.", "Answers vary.", lines=10,
                    note="1 point each: topic sentence; article detail; visual detail; explanation; conclusion.")]),
     S("Exit Ticket", [OR("Which detail from a visual did you use? Why was it helpful?", "Answers vary.", lines=2)])],
    te("Students integrate text and visual information in writing.", "Integrate information from two texts; write informative texts.", "Workbook Lesson 5.8",
       "Teach a younger child.", "Reread the article and visuals.", ["Model integrating."], "Plan together.",
       ["Using only the article."], ["Source checklist."], ["Make a poster explaining navigation."], independent="Write the paragraph. Weekly Check tomorrow."),
    summary="Integrate words and visuals; name your sources.")

# ================================================================= Week 3 · Compare structure and viewpoint (Chapter 6)
L9 = Lesson("5.9", "Comparing Story Structures",
    "I can compare how two stories are structured and how the structure affects the reader.", "RL.4.5, RL.4.9",
    [("epistolary", "Told through letters, journals, or messages.")],
    "How would a story feel different if it were told in letters instead of by a narrator?",
    [ReaderAssign(TI, "Chapter 6: The Plan", "What is the plan? Who makes it?"),
     Text("Stories can be structured as a continuous narrative, as letters or journal entries (<b>epistolary</b>), or as a play. The structure affects what readers know and how they feel."),
     P_LETTERS,
     Example("Compare structures", "“Letters from Camp” vs “The Castaway of Pelican Key”",
             ["Letters: dated entries; we see only what Sam writes; time skips between letters.", "Castaway: a narrator describes everything; scenes flow continuously.", "Effect: letters feel personal; the narrative gives a fuller picture."],
             "Letters make the story personal and let readers infer what happened between them; the narrative tells a fuller, continuous story."),
     KeyIdea("Structure affects what readers know and how they feel. Compare how each story is put together.")],
    [Problem("How do we learn time passes in “Letters from Camp”?", "the dates"), Problem("How does Sam change?", "from homesick to wanting to stay"), Problem("What must readers infer between letters?", "what happened at camp, such as his friendship with Theo growing")],
    [S("Warm-Up", [SA("Epistolary means told through…", "letters or journals"), SA("Structure of a play", "cast, dialogue, stage directions")], cols=2),
     S("Compare", [OR("How does Sam's attitude toward Theo change across the letters? Use evidence.", "Letter 1: Theo snores like a bear (annoying). Letter 2: they laugh together. Letter 3: they're building a raft; Sam wants to stay.", lines=3),
                   OR("Compare the structures of “Letters from Camp” and “The Castaway.” How does each structure affect the reader?", "Letters: personal, gaps to infer. Narrative: full, continuous, vivid descriptions.", lines=4)], passage=P_LETTERS),
     S("Exit Ticket", [OR("Write a short diary entry as Jim Hawkins after Chapter 6.", "Answers vary; first person, dated.", lines=4)])],
    te("Students compare story structures.", "Explain structural differences; compare similar themes and topics.", "Treasure Island Reader (Chapter 6), workbook Lesson 5.9",
       "Letters vs narrator.", ["Read Chapter 6.", "Read “Letters from Camp.”"], ["Model the comparison."], "Your Turn 1–3.",
       ["Comparing plots instead of structures."], ["Ask: How is it put together?"], ["Rewrite a scene as letters."]),
    summary="Structure (narrative, letters, drama) shapes what readers know and feel.")

L10 = Lesson("5.10", "Comparing Narrators",
    "I can compare how two narrators tell the same event.", "RL.4.6",
    [],
    "When two people tell the same story, why can both versions sound true?",
    [Text("Two first-person narrators may tell the same event very differently. Each narrator includes what matters to them and leaves out what doesn't."),
     P_NARR_A, P_NARR_B,
     Example("Compare narrators", "Leo vs Mia", ["Leo: focuses on not meaning to; feels betrayed (“Thanks a lot, Mia”).", "Mia: focuses on warning him; telling the truth; helping glue the vase."],
             "Each narrator makes themselves sound reasonable. Mia includes that she helped; Leo doesn't know or mention it."),
     KeyIdea("Ask: What does each narrator include, leave out, and feel? Why?")],
    [Problem("What does Leo leave out?", "that Mia had warned him (and that she helped later)"), Problem("Why did Mia point?", "Somebody had to tell the truth."), Problem("Who is the more reliable narrator? Explain.", "Answers vary; Mia includes more facts, but both are biased.")],
    [S("Warm-Up", [SA("Point of view of both versions", "first person"), SA("Are both narrators characters?", "Yes")], cols=2),
     S("Compare", [OR("How does each narrator feel about Mia pointing?", "Leo: betrayed, annoyed. Mia: it was the right thing.", lines=2),
                   OR("What does Mia tell that Leo doesn't? Why might Leo leave it out?", "She warned him and helped glue it; he's upset and focuses on himself.", lines=3)]),
     S("Chapter 6", [OR("Retell an event from Chapter 6 from a different character's point of view in 3–4 sentences.", "Answers vary.", lines=4)])],
    te("Students compare narrators.", "Compare and contrast the point of view from which stories are narrated.", "Workbook Lesson 5.10",
       "Two true versions?", "Read both vase stories.", ["Model the comparison."], "Your Turn 1–3.",
       ["Deciding one narrator is lying."], ["Both include what matters to them."], ["Write the vase story from Mom's view."]),
    summary="Different narrators include, leave out, and feel different things.")

L11 = Lesson("5.11", "Comparing Two Informational Texts",
    "I can compare the focus and structure of two informational texts on the same topic.", "RI.4.9, RI.4.6",
    [("focus", "The part of a topic a text pays most attention to.")],
    "Two books about volcanoes: why might they still teach you different things?",
    [Text("Two texts on the same topic can have different <b>focus</b> (people vs how something works) and different <b>structures</b>. Reading both gives a fuller picture."),
     P_LIGHT_A, P_LIGHT_B,
     Figure(lambda t: table(t, [["", "Text A", "Text B"], ["Focus", "the people who kept lighthouses", "how lighthouses work"], ["Structure", "description with examples", "parts explained in order"],
                                ["Key detail", "Grace Darling's rescue (1838)", "Fresnel lens (1822)"]], [1.1 * inch, 2.3 * inch, 2.3 * inch], width=5.7 * inch)),
     KeyIdea("Compare focus, structure, and details. Together, two texts give a fuller understanding.")],
    [Problem("Focus of Text A", "lighthouse keepers"), Problem("Focus of Text B", "how lighthouses work"), Problem("Why was the tower tall?", "so the light could be seen over the curve of the earth")],
    [S("Warm-Up", [SA("What is focus?", "the part of a topic a text pays most attention to"), SA("Same topic of both texts", "lighthouses")], cols=2),
     S("Compare", [OR("Why did keepers climb the tower several times a night? (Text A) How might the Fresnel lens have changed keepers' work? (Text B + your thinking)", "To trim the wick and refill the oil; the lens made a stronger beam from the same lamp.", lines=3),
                   OR("What do you learn from reading both texts that you wouldn't learn from just one?", "both the human story and the science of lighthouses", lines=3)]),
     S("Exit Ticket", [OR("How do flash patterns help sailors?", "Each lighthouse has its own pattern, so sailors know which one they see and where they are.", lines=2)])],
    te("Students compare two informational texts.", "Integrate information from two texts on the same topic.", "Workbook Lesson 5.11",
       "Two volcano books.", "Read Texts A and B.", ["Model the comparison chart."], "Your Turn 1–3.",
       ["Summarizing each text separately without comparing."], ["Comparison chart."], ["Research a lighthouse near you or in history."]),
    summary="Compare focus, structure, and details of texts on the same topic.")

L12 = Lesson("5.12", "Speaking Knowledgeably from Two Texts",
    "I can present what I learned from two texts in a short talk.", "RI.4.9, SL.4.4",
    [("presentation", "A talk that shares information with an audience.")],
    "What makes a speaker sound like an expert?",
    [Text("Use details from both texts, organize your talk (introduction, two or three facts, conclusion), speak clearly at a good pace, and look at your audience."),
     Bullets(["Start with a hook: a question or surprising fact.", "Give two or three facts from each text.", "End with a conclusion or something to think about.", "Practice aloud twice before presenting."]),
     KeyIdea("Organize, use evidence from both texts, and speak clearly.")],
    [Problem("Good hook for a lighthouse talk", "e.g. Did you know a lighthouse beam could be seen 20 miles away?"), Problem("How many texts should facts come from?", "both"), Problem("Name a speaking skill.", "eye contact, clear voice, steady pace")],
    [S("Warm-Up", [SA("A hook is…", "an opening that grabs attention"), SA("Speak at a ___ pace.", "steady, clear")], cols=2),
     S("Plan Your Talk", [OR("Hook:", "Answers vary.", lines=1), OR("Facts from Text A:", "Answers vary.", lines=2), OR("Facts from Text B:", "Answers vary.", lines=2), OR("Conclusion:", "Answers vary.", lines=1)]),
     S("Present", [OR("Give your 1–2 minute talk to your family. Ask a listener to write one thing you did well.", "Answers vary.", lines=2)])],
    te("Students present information from two texts.", "Report on a topic in an organized manner, using appropriate facts and details; speak clearly.", "Workbook Lesson 5.12",
       "Expert speakers.", "Review Texts A and B.", ["Model a short talk."], "Plan the talk.",
       ["Reading notes word for word."], ["Note cards with key words only."], ["Add a visual."], independent="Practice and present.", exit_="Listener feedback. Weekly Check tomorrow."),
    summary="Organized talks use evidence from both texts and clear speaking.")

# ================================================================= Week 4 · Write a supported comparison (Chapter 7)
L13 = Lesson("5.13", "Comparison Essay Structure",
    "I can choose a structure for a compare-and-contrast essay.", "W.4.2a, W.4.9",
    [("block structure", "Write all about Subject A, then all about Subject B."), ("point-by-point structure", "Compare A and B on one point at a time.")],
    "How would you organize an essay comparing cats and dogs?",
    [ReaderAssign(TI, "Chapter 7: “Shiver Me Timbers”", "What happens to Jim in this chapter? How is he like or unlike the castaways you've read about?"),
     Text("A comparison essay can use <b>block</b> or <b>point-by-point</b> structure. Both need an introduction with a thesis, body paragraphs with evidence, and a conclusion."),
     Figure(lambda t: table(t, [["Block structure", "Point-by-point structure"], ["Intro", "Intro"], ["Body 1: Eli (survival, change)", "Body 1: How they survived (Eli and Ben Gunn)"],
                                ["Body 2: Ben Gunn (survival, change)", "Body 2: How loneliness changed them (Eli and Ben Gunn)"], ["Conclusion", "Conclusion"]], [W * 0.46, W * 0.46], width=W * 0.92)),
     Example("Thesis", "Compare Eli and Ben Gunn.", ["Name both subjects.", "Say how they are alike and different."], "Eli and Ben Gunn were both castaways, but while Eli grew stronger and calmer, Ben Gunn's years alone left him wild and strange."),
     KeyIdea("Choose block or point-by-point; start with a thesis that names both subjects.")],
    [Problem("Which structure compares one point at a time?", "point-by-point"), Problem("What must a thesis name?", "both subjects (and the comparison)"), Problem("How many body paragraphs at least?", "two")],
    [S("Warm-Up", [SA("Block = ___ then ___", "all of A, then all of B"), SA("Thesis goes in the…", "introduction")], cols=2),
     S("Plan", [OR("Write a thesis comparing Eli (The Castaway) and Jim Hawkins (Chapters 5–7).", "Answers vary; names both and the comparison.", lines=3),
                OR("Which structure will you use? Why?", "Answers vary.", lines=2)]),
     S("Exit Ticket", [OR("What happened to Jim in Chapter 7?", "Answers vary; accurate summary.", lines=3)])],
    te("Students learn comparison essay structure.", "Introduce a topic and group related information; draw evidence from texts.", "Treasure Island Reader (Chapter 7), workbook Lesson 5.13",
       "Cats vs dogs.", "Read Chapter 7.", ["Teach both structures.", "Model a thesis."], "Your Turn 1–3.",
       ["Thesis that names only one subject."], ["Thesis frame: Both ___ and ___, but ___."], ["Plan both structures and choose."]),
    summary="Block or point-by-point; thesis names both subjects.")

L14 = Lesson("5.14", "Planning the Comparison Essay",
    "I can gather evidence and outline a comparison essay.", "W.4.9, W.4.2",
    [],
    "Why gather evidence before writing?",
    [Text("Use a Venn diagram to collect similarities and differences with evidence, then turn it into an outline."),
     Example("Venn to outline", "Eli and Jim", ["Both: face danger alone, show courage, use their wits.", "Eli only: alone 42 days on an island.", "Jim only: involved with pirates, the treasure, and adults."],
             "Outline: Intro (thesis) → Body 1: how both show courage → Body 2: how their situations differ → Conclusion."),
     KeyIdea("Venn diagram → outline → essay. Every point needs evidence.")],
    [Problem("Where do similarities go in a Venn diagram?", "in the middle"), Problem("What should each outline point have?", "evidence"), Problem("Name one way Eli and Jim are alike.", "both brave / act on their own")],
    [S("Warm-Up", [SA("Venn middle =", "similarities"), SA("Outline first part", "introduction with thesis")], cols=2),
     S("Gather Evidence", [OR("Eli only:", "Answers vary.", lines=2), OR("Both:", "Answers vary.", lines=3), OR("Jim only:", "Answers vary.", lines=2)]),
     S("Outline", [OR("Intro/thesis:", "Answers vary.", lines=2), OR("Body 1 + evidence:", "Answers vary.", lines=3), OR("Body 2 + evidence:", "Answers vary.", lines=3), OR("Conclusion:", "Answers vary.", lines=2)])],
    te("Students plan comparison essays.", "Draw evidence from texts; organize writing.", "Workbook Lesson 5.14",
       "Why gather evidence?", "Skim the Castaway story and Chapters 5–7.", ["Model Venn → outline."], "Gather evidence.",
       ["Similarities without evidence."], ["Evidence sticky notes."], ["Add a third body paragraph."], independent="Complete the outline."),
    summary="Venn diagram → outline with evidence.")

L15 = Lesson("5.15", "Drafting the Comparison Essay",
    "I can draft a comparison essay with transitions and evidence.", "W.4.2b, W.4.2c",
    [],
    "What words show a reader you're comparing or contrasting?",
    [Text("Use comparison transitions: <i>Both, Similarly, Likewise, In the same way</i>. Use contrast transitions: <i>However, Unlike, On the other hand, While</i>."),
     Example("Body paragraph", "Point: Both boys show courage.", ["Topic sentence with a comparison transition.", "Evidence for Eli.", "Evidence for Jim.", "Explanation."],
             "Both Eli and Jim show courage when they are alone. Eli climbs the cliff every night and finally lights a signal fire. Similarly, Jim takes risks on his own. These choices show that both boys act bravely instead of waiting for help."),
     KeyIdea("Each body paragraph: topic sentence, evidence about both subjects, transitions, explanation.")],
    [Problem("Comparison transition", "both, similarly, likewise"), Problem("Contrast transition", "however, unlike, on the other hand"), Problem("What follows the evidence?", "explanation")],
    [S("Warm-Up", [SA("Similarly signals…", "a similarity"), SA("However signals…", "a difference")], cols=2),
     S("Draft", [OR("Draft your comparison essay from your Lesson 5.14 outline.", "Answers vary.", lines=24, note="Look for: thesis; two body paragraphs with evidence about both subjects; transitions; conclusion.")])],
    te("Students draft comparison essays.", "Develop the topic with facts and details; link ideas with words and phrases.", "Outlines, workbook Lesson 5.15",
       "Transition words.", "Reread the model body paragraph.", ["Model drafting one paragraph."], "Draft; conference.",
       ["Body paragraphs about only one subject."], ["Two-color highlighting check."], ["Add a quotation."], independent="Finish the draft."),
    summary="Use comparison and contrast transitions with evidence about both subjects.")

L16 = Lesson("5.16", "Revising and Editing the Comparison Essay",
    "I can revise and edit my comparison essay.", "W.4.5, L.4.2",
    [],
    "What is one thing a reader should feel after reading your essay?",
    [Figure(lambda t: table(t, [["Checklist", "✓"], ["Thesis names both subjects and the comparison.", ""], ["Each body paragraph has evidence about BOTH subjects.", ""], ["I used comparison and contrast transitions.", ""],
                                ["Conclusion restates the thesis in new words.", ""], ["Capitals, commas, end marks, and spelling are correct.", ""], ["Titles of stories are in quotation marks; book titles are underlined or italicized.", ""]],
                            [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Revise for ideas and organization; edit for conventions, including how to write titles.")],
    [Problem("How do you write a book title by hand?", "underline it"), Problem("How do you write a short story title?", "in quotation marks"), Problem("What does a conclusion restate?", "the thesis")],
    [S("Warm-Up", [SA("Title format: Treasure Island (handwritten)", "underline"), SA("Title format: “The Castaway of Pelican Key”", "quotation marks")], cols=2),
     S("Revise and Edit", [OR("Use the checklist. List two revisions and two edits you made.", "Answers vary.", lines=4), OR("Copy your revised thesis.", "Answers vary.", lines=2)]),
     S("Exit Ticket", [OR("What did you learn about comparing texts this unit?", "Answers vary.", lines=2)])],
    te("Students revise and edit comparison essays.", "Revise and edit writing; use correct capitalization and punctuation, including titles.", "Drafts, workbook Lesson 5.16, Unit 5 Review",
       "Reader takeaway.", "Read drafts aloud.", ["Teach title formatting.", "Model the checklist."], "Revise with a partner.",
       ["Forgetting title punctuation."], ["Title rules card."], ["Publish and illustrate."], independent="Revise; then the Unit 5 Review.", exit_="Exit Ticket. Tomorrow: Unit 5 Test."),
    summary="Revise for ideas and evidence; edit for conventions and title formatting.")

# ================================================================= checks
C1 = Check("Weekly Check 13: Plot and Character", [S("Read and answer", [
    OR("What is the problem in the story?", "Jada's homemade kite keeps crashing and kids laugh at her.", lines=2),
    OR("What is the climax?", "The third try, when the red kite climbs higher than all the others.", lines=2),
    OR("Use STEAL: what do Jada's actions show about her?", "She checked the knots and added a tail and tried again: determined, resourceful.", lines=2),
    OR("How does Jada feel when kids laugh? What clue shows it?", "embarrassed; her cheeks burned", lines=2),
    MC("What is the resolution?", ["The kite crashes.", "Jada wins Most Creative Kite.", "The wind is strong."], 1)], passage=P_C13)], minutes=20)

C2 = Check("Weekly Check 14: Informational Text Features", [S("Read and answer", [
    OR("List the headings.", "A Long Journey; A Winter Home; Danger Ahead", lines=1),
    OR("Under which heading would you learn why monarchs need help?", "Danger Ahead", lines=1),
    OR("Why do monarchs rest in the cool mountains?", "The cool air lets them rest without using up energy.", lines=2),
    OR("What is the main idea of the whole text?", "Monarchs make a long migration to Mexico and face dangers, so people help them.", lines=2),
    OR("What text feature could the author add to help readers? Explain.", "e.g. a map of the route; a photo with a caption of monarchs clustering", lines=2)], passage=P_C14)], minutes=20)

C3 = Check("Weekly Check 15: Comparing Texts", [S("Read Text A", [], passage=P_C15A), S("Read Text B, then answer", [
    OR("When does each bird hunt?", "Owls at night; hawks during the day.", lines=1),
    OR("Which sense does each text say helps the bird most?", "Owl: hearing (and large eyes); hawk: eyesight.", lines=2),
    OR("Write one sentence comparing the birds using a comparison transition.", "e.g. Both owls and hawks are skilled hunters.", lines=1),
    OR("Write one sentence contrasting the birds using a contrast transition.", "e.g. Owls hunt at night; however, hawks hunt during the day.", lines=1),
    MC("Which structure would put “Owls: when, senses; Hawks: when, senses”?", ["block", "point-by-point"], 0)], passage=P_C15B)], minutes=20)

REVIEW = Check("Unit 5 Review", [
    S("Skills", [SA("Turning point of a plot", "climax"), SA("STEAL stands for", "Speech, Thoughts, Effect, Actions, Looks"), SA("A title for a section", "heading"),
                 SA("Letters/journal story", "epistolary"), SA("Structure: all A, then all B", "block"), SA("Contrast transition", "however")], cols=2),
    S("Apply", [OR("Compare Text A and Text B about lighthouses in two sentences.", "Both are about lighthouses. Text A focuses on keepers, while Text B explains how lighthouses work.", lines=3),
                OR("Write a thesis comparing Ben Gunn and Eli.", "e.g. Both were castaways, but Eli grew strong and calm while Ben Gunn became wild.", lines=2)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 5 Test", [
    S("Part A · Text A (1 point each)", [
        OR("How long is the Iditarod?", "about 1,000 miles", lines=1),
        OR("Why did the 1925 trip happen? Explain with two details.", "Diphtheria broke out in Nome; medicine was hundreds of miles away; no roads and planes couldn't fly.", lines=2, points=2),
        OR("What is the main idea of Text A?", "The Iditarod race honors the 1925 sled-dog relay that carried medicine to Nome.", lines=2)], passage=P_TEST_A),
    S("Part B · Text B (1 point each)", [
        MC("What kind of text is Text B?", ["informational article", "historical fiction story", "a play"], 1),
        OR("What does Balto do at the climax? What does it show about him?", "He stops before the thin ice and leads the team around it; he is smart and protective.", lines=2),
        OR("Explain the simile “so cold it stung like needles.”", "The cold was sharp and painful.", lines=1)], passage=P_TEST_B),
    S("Part C · Compare (1 point each)", [
        OR("What is the focus of each text?", "A: the race and the history; B: one dramatic night told as a story, with feelings.", lines=2),
        OR("What do you learn from Text B that Text A doesn't tell?", "feelings, the danger of the whiteout and thin ice, Balto's role", lines=2),
        OR("What do you learn from Text A that Text B doesn't tell?", "facts: the Iditarod, the distance, diphtheria, five and a half days, how mushers care for dogs", lines=2)]),
    S("Part D · Write (5 points)", [OR("Write a comparison paragraph about Text A and Text B. Include a topic sentence naming both texts, evidence from each, comparison and contrast transitions, and a conclusion.",
                                       "Rubric: topic sentence (1); evidence from A (1); evidence from B (1); transitions (1); conclusion (1).", lines=12, points=5)])],
    kind="test", minutes=45, rubric=[["13–15 (85%+)", "Mastered."], ["10–12", "Proficient; review missed skills."], ["Below 10", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-02-22", "2027-03-01", "2027-03-08", "2027-03-22"], CHECKS, REVIEW, TEST)

UNIT = Unit(5, "Reading Deeply", "Long stories and articles, text features, comparing structure and viewpoint, and the comparison essay, with Treasure Island Chapters 5–7.",
    "As Jim Hawkins explores Treasure Island, you'll explore longer, richer texts: a survival story, an article about how sailors navigated, letters, lighthouse histories, and the Blackbeard selection. You'll analyze plot and character in depth, use text features and visuals, compare texts, and write your first full comparison essay.",
    ["Identify plot structure and analyze characters and settings in depth.", "Use text features, charts, and timelines to understand informational texts.",
     "Compare the structures and narrators of stories and the focus of informational texts.", "Plan, draft, and revise a compare-and-contrast essay."],
    [("RL.4.3, RL.4.5", "Describe characters, settings, and events in depth; explain story structure."), ("RL.4.6, RI.4.6", "Compare points of view and accounts."),
     ("RI.4.7, RI.4.9", "Interpret visual information; integrate information from two texts."), ("W.4.2, W.4.5, W.4.9, SL.4.4", "Write and present organized comparisons with evidence.")],
    [("climax", "The turning point of a plot."), ("characterization", "How an author shows what a character is like."), ("text features", "Headings, captions, bold words, and visuals."),
     ("epistolary", "Told through letters or journals."), ("thesis", "The main claim of an essay.")],
    ["Unit 4: text structure and point of view."], ["Treasure Island Reader (Chapters 5–7, Blackbeard selection)", "Highlighters; note cards for the talk"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Comparing sources is how you decide what to believe: two news stories, two product reviews, or two history books.",
    family_note="Ask your student to teach you something from the navigation article or the lighthouse texts at dinner, then ask, “Which source told you that?”",
    weeks=WEEKS)
