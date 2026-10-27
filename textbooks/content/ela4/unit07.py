"""Grade 4 ELA · Unit 7: Reading Across Texts — text sets, quest patterns across cultures, myth and science explanations, integrating sources, and the synthesis essay.
Anchor reading: King Arthur and the Round Table Reader, Chapters 13–16 (Apr 26 – May 21, 2027)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule
from content.ela4.unit01 import S, MC, OR, SA, READER


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


# ================================================================= passages (original retellings and texts)
P_JASON = Passage("Jason and the Golden Fleece · A Greek Myth Retold", [
    "Long ago in Greece, a young man named Jason learned that his uncle had stolen his father's throne. When Jason demanded it back, his uncle smiled slyly. “Bring me the Golden Fleece,” he said, “and the throne is yours.” The fleece hung in a faraway land, guarded by a dragon that never slept.",
    "Jason built a great ship called the <i>Argo</i> and gathered the bravest heroes of Greece to sail with him. On the journey, they rowed past clashing rocks that smashed ships to splinters and faced storms and strange creatures.",
    "In the land of the fleece, the king gave Jason impossible tasks, such as plowing a field with fire-breathing bulls. With the help of the king's daughter, Medea, who knew magic, Jason completed the tasks, put the dragon to sleep, and took the fleece.",
    "Jason sailed home a hero. His quest had tested his courage, but he could not have succeeded alone.",
], source="An original retelling of a traditional Greek myth", genre="Myth")

P_MOMOTARO = Passage("Momotaro, the Peach Boy · A Japanese Folktale Retold", [
    "An old woman washing clothes in a river saw a giant peach floating by. She carried it home, and when she and her husband cut it open, out stepped a baby boy. They named him Momotaro, which means “Peach Boy,” and raised him with love.",
    "When Momotaro grew up, ogres were stealing from the villages nearby. Momotaro decided to stop them. His mother packed him millet dumplings for the journey.",
    "Along the way, he shared his dumplings with a hungry dog, a monkey, and a pheasant. Each one joined him. Together they crossed the sea to the ogres' island. The pheasant flew over the walls, the monkey opened the gate, and the dog and Momotaro charged in. The ogres surrendered and returned everything they had stolen.",
    "Momotaro came home with the treasure and his loyal friends, and the villages were safe again.",
], source="An original retelling of a traditional Japanese folktale", genre="Folktale")

P_PERSEPHONE = Passage("Persephone and the Seasons · A Greek Myth Retold", [
    "Demeter was the goddess of the harvest. Wherever she walked, crops grew tall and flowers bloomed. She loved nothing more than her daughter, Persephone.",
    "One day Hades, ruler of the underworld, carried Persephone away to his dark kingdom. Demeter searched everywhere. In her grief, she stopped caring for the earth. Plants withered, snow fell, and people grew hungry.",
    "At last, the king of the gods made an agreement. Persephone could return to her mother, but because she had eaten six pomegranate seeds in the underworld, she must spend six months of every year there.",
    "And so, the ancient Greeks said, every year when Persephone goes below, Demeter mourns, and the earth grows cold and bare: autumn and winter. When Persephone returns, Demeter rejoices, and the earth blooms again: spring and summer.",
], source="An original retelling of a traditional Greek myth", genre="Myth")

P_SEASONS = Passage("What Causes the Seasons?", [
    "Many people think seasons happen because Earth moves closer to and farther from the sun. That's not the reason. In fact, Earth is closest to the sun in early January, during winter in the Northern Hemisphere.",
    "The real cause is Earth's <b>tilt</b>. Earth's axis, the imaginary line it spins around, is tilted about 23.5 degrees. As Earth travels around the sun during the year, the tilt stays pointed the same direction in space.",
    "For part of the year, the Northern Hemisphere is tilted toward the sun. Sunlight hits it more directly, and days are longer, so it is summer. Six months later, the Northern Hemisphere is tilted away from the sun. Sunlight hits at a low angle, days are shorter, and it is winter.",
    "That's why, when it is summer in the United States, it is winter in Australia.",
], source="An original informational text", genre="Science text")

P_TIDES_A = Passage("Explanation A: Tides", [
    "The ocean rises and falls along the shore twice a day. These changes are called tides. Tides are caused by the moon.",
], source="An original informational text", genre="Informational text", numbered=False)
P_TIDES_B = Passage("Explanation B: Why the Ocean Has Tides", [
    "Along most coasts, the ocean rises to a high tide and falls to a low tide about twice a day. The main cause is the moon's <b>gravity</b>, the force that pulls objects toward each other.",
    "The moon pulls on the whole Earth, but it pulls hardest on the side closest to it. Ocean water on that side bulges toward the moon. A second bulge forms on the opposite side of Earth. As Earth spins, a coastline passes through both bulges each day, which is why most places have two high tides.",
    "The sun's gravity affects tides too. When the sun and moon line up, at full moon and new moon, tides are extra high and extra low.",
], source="An original informational text", genre="Informational text")

KNIGHT_SOURCES = [
    Passage("Source 1: Becoming a Page", [
        "Boys from noble families began training for knighthood at about age seven. They became <b>pages</b> and lived in the castle of a lord. Pages learned manners, served meals, and practiced riding and fighting with wooden swords.",
    ], source="An original informational text", genre="Source 1", numbered=False),
    Passage("Source 2: The Squire's Training", [
        "At about fourteen, a page became a <b>squire</b>. A squire served one knight, caring for his horse, polishing his armor, and following him into battle. Squires trained hard with real weapons and learned the code of chivalry.",
    ], source="An original informational text", genre="Source 2", numbered=False),
    Passage("Source 3: The Dubbing Ceremony", [
        "Around age twenty-one, a squire who had proven himself could become a knight in a ceremony called <b>dubbing</b>. Often he spent the night before praying. In the morning, a lord tapped him on the shoulder with a sword and declared him a knight.",
    ], source="An original informational text", genre="Source 3", numbered=False),
]

P_C19 = Passage("The Girl Who Brought Back the Spring · An Original Folktale", [
    "In a valley where winter never ended, a girl named Anya set out to find the Spring, which the Frost King had locked in his ice palace.",
    "On the way, she shared her bread with a starving fox, freed a sparrow from a trap, and carried an old woman across a frozen river. Each one promised to help her.",
    "At the palace, the fox showed her a secret tunnel, the sparrow pecked the key from the Frost King's belt, and the old woman, who was really the Spring Fairy, melted the ice with a touch. Anya returned home as flowers burst from the snow.",
], source="An original folktale", genre="Folktale")

P_C20A = Passage("Text A: How the Moon Got Its Phases · An Original Myth", [
    "Long ago, the Moon was proud of her round, silver face. Each month she grew so vain that she ate too many stars and swelled to a full circle. Then, ashamed, she hid her face a little more each night until she disappeared. Slowly she returned, and the cycle began again.",
], source="An original myth", genre="Myth", numbered=False)
P_C20B = Passage("Text B: Why the Moon Has Phases", [
    "The moon does not make its own light. It reflects light from the sun. As the moon orbits Earth about once a month, we see different amounts of its sunlit side. When we see the whole lit side, it is a full moon. When the lit side faces away from us, it is a new moon.",
], source="An original science text", genre="Science text", numbered=False)

P_C21A = Passage("Source A: Castle Walls", [
    "Castle walls were often more than ten feet thick at the bottom. They were built from stone because wood could be burned by attackers.",
], source="An original informational text", genre="Source A", numbered=False)
P_C21B = Passage("Source B: Under Attack", [
    "Attackers sometimes surrounded a castle for months, a tactic called a <b>siege</b>, hoping the people inside would run out of food. Castles stored grain and had wells so they could survive a long siege.",
], source="An original informational text", genre="Source B", numbered=False)

P_TEST_A = Passage("Text A: Vulcan's Forge · A Roman Myth Retold", [
    "The ancient Romans told of Vulcan, the god of fire and metalworking. Deep beneath a mountain, Vulcan kept his forge, where he hammered out armor and thunderbolts for the gods.",
    "When Vulcan worked hard, smoke and sparks poured from the top of the mountain, and the ground shook with the pounding of his hammer. Sometimes, when he was angry, melted rock spilled down the mountainside.",
    "Our word <i>volcano</i> comes from Vulcan's name.",
], source="An original retelling of a traditional Roman myth", genre="Myth")
P_TEST_B = Passage("Text B: How Volcanoes Form", [
    "Deep under Earth's surface, it is so hot that some rock melts into a thick liquid called <b>magma</b>. Magma is lighter than the solid rock around it, so it slowly rises.",
    "When magma collects under the surface, pressure builds, like the pressure in a shaken soda bottle. If the pressure becomes great enough, magma bursts out through an opening. Once it reaches the surface, it is called <b>lava</b>.",
    "Eruptions can send out ash, gas, and rock. Before many eruptions, the ground shakes with small earthquakes as magma moves underground. Scientists watch for these signs to warn people living nearby.",
], source="An original science text", genre="Science text")

# ================================================================= Week 1 · Read and annotate multiple texts (Chapter 13)
L1 = Lesson("7.1", "Reading a Text Set with a Guiding Question",
    "I can read several texts on one topic with a guiding question in mind.", "RI.4.9, RL.4.9",
    [("text set", "A group of texts about the same topic or theme."), ("guiding question", "A big question you try to answer by reading several texts.")],
    "If you wanted to understand what makes a hero, would one story be enough?",
    [ReaderAssign(READER, "Chapter 13: Sir Percival", "How is Percival like and unlike the other knights you've read about?"),
     Text("A <b>text set</b> is a group of texts about one topic. Reading with a <b>guiding question</b> keeps you focused. After each text, jot down what it adds to your answer."),
     Figure(lambda t: table(t, [["Guiding question: What makes a hero?", ""], ["Text", "What it adds"], ["King Arthur (the Reader)", "courage, fairness, loyalty to others"],
                                ["The Secret of Hollow Hill", "a hero can be an ordinary kid who faces fear"], ["The Lighthouse Keeper's Daughter", "acting quickly to save others"], ["Momotaro (Lesson 7.3)", "kindness and teamwork"]],
                            [2.5 * inch, 3.0 * inch], width=5.5 * inch, header=False)),
     KeyIdea("Read each text with the guiding question in mind; record what each adds.")],
    [Problem("What is a text set?", "a group of texts about the same topic"), Problem("Why use a guiding question?", "to stay focused and connect the texts"), Problem("What does Percival add to the question “What makes a hero?”", "Answers vary; supported by Chapter 13.")],
    [S("Warm-Up", [SA("A guiding question is…", "a big question answered with several texts"), SA("Name one hero from this year's reading.", "Arthur, Pip, Nell, Ada, Jim, etc.")], cols=2),
     S("Build the Text Set", [OR("Guiding question: What makes a hero? Write what each of these adds: Arthur, Pip (Hollow Hill), Nell (Lighthouse), Ada (Bridge at Millbrook).", "Answers vary; e.g. Arthur: leadership/fairness; Pip: courage; Nell: acting under pressure; Ada: quick thinking.", lines=6),
                              OR("Chapter 13: What does Sir Percival add?", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Write your first answer to the guiding question in one sentence.", "Answers vary.", lines=2)])],
    te("Students read text sets with a guiding question.", "Compare and contrast themes and patterns of events across texts.", "King Arthur Reader (Chapter 13), workbook Lesson 7.1",
       "One story enough?", "Read Chapter 13.", ["Teach text sets and guiding questions.", "Model the chart."], "Your Turn 1–3.",
       ["Summarizing each text without connecting to the question."], ["Chart with a “what it adds” column."], ["Add a hero from a family story."]),
    summary="Read text sets with a guiding question; record what each text adds.")

L2 = Lesson("7.2", "Annotating Across Texts",
    "I can annotate texts to connect ideas across them.", "RI.4.9, RL.4.1",
    [],
    "How can sticky notes help you connect two books?",
    [Text("When annotating across texts, use codes that show connections:"),
     Figure(lambda t: table(t, [["Code", "Means"], ["S", "Same idea as another text"], ["D", "Different from another text"], ["+", "New information"], ["?", "Question"], ["Q", "Great quote for my guiding question"]],
                            [1.0 * inch, 3.6 * inch], width=4.6 * inch)),
     P_JASON,
     Example("Annotate with connections", "Paragraph 4: “he could not have succeeded alone.”", ["Code S: like Pip, who needed Grandfather's map.", "Code Q: a great quote about heroes needing help."], "S and Q"),
     KeyIdea("Connection codes (S, D, +, ?, Q) help you see patterns across texts.")],
    [Problem("What does code S mean?", "same idea as another text"), Problem("Which detail in Jason could get a D compared to Arthur?", "Jason used help from magic/Medea; Arthur's sword came from the Lady of the Lake (or accept reasonable)"), Problem("Why is the last sentence a good Q?", "It states an idea about heroes directly.")],
    [S("Warm-Up", [SA("Code for new information", "+"), SA("Code for a great quote", "Q")], cols=2),
     S("Annotate Jason", [OR("Annotate “Jason and the Golden Fleece” with the codes. List two S connections and one D.", "Answers vary.", lines=4),
                          OR("What dangers does Jason face on his quest?", "clashing rocks, storms, strange creatures, fire-breathing bulls, a dragon", lines=2),
                          OR("Who helps Jason? Why does it matter?", "the heroes on the Argo and Medea; heroes often need help", lines=2)], passage=P_JASON),
     S("Exit Ticket", [OR("Copy your best Q quote and explain why you chose it.", "Answers vary.", lines=2)])],
    te("Students annotate with connection codes.", "Refer to details; compare themes across texts.", "Sticky notes, workbook Lesson 7.2",
       "Sticky-note connections.", "Read the Jason retelling.", ["Teach the codes.", "Model paragraph 4."], "Your Turn 1–3.",
       ["Codes without explanation."], ["Write one word beside each code."], ["Annotate Chapter 13 the same way."]),
    summary="Use connection codes to see patterns across texts.")

L3 = Lesson("7.3", "The Quest Pattern Across Cultures",
    "I can compare the quest pattern in stories from different cultures.", "RL.4.9",
    [("quest", "A long, difficult journey to find or achieve something important."), ("traditional literature", "Stories passed down over generations: myths, folktales, legends, and fables.")],
    "What do the Grail quest, Jason's voyage, and a video game adventure have in common?",
    [Text("Stories from many cultures follow a similar <b>quest pattern</b>: a hero leaves home for an important goal, faces trials, gets help, succeeds, and returns changed."),
     P_MOMOTARO,
     Figure(lambda t: table(t, [["Quest step", "Jason (Greece)", "Momotaro (Japan)"], ["Call to the quest", "win back the throne", "stop the ogres"], ["Helpers", "Argo heroes, Medea", "dog, monkey, pheasant"],
                                ["Trials", "clashing rocks, fire bulls, dragon", "crossing the sea, ogres' fortress"], ["Return", "home a hero with the fleece", "home with treasure; villages safe"]],
                            [1.4 * inch, 2.1 * inch, 2.1 * inch], width=5.6 * inch, font_size=9)),
     KeyIdea("Quests across cultures share a pattern: call, journey, helpers, trials, success, return.")],
    [Problem("How did Momotaro gain his helpers?", "by sharing his dumplings"), Problem("Name one difference between the two quests.", "e.g. Momotaro's helpers are animals; Jason's helper uses magic"), Problem("What culture does each story come from?", "Jason: Greece; Momotaro: Japan")],
    [S("Warm-Up", [SA("What is a quest?", "a long journey to achieve something important"), SA("Name a type of traditional literature.", "myth, folktale, legend, fable")], cols=2),
     S("Compare the Quests", [OR("How are Jason's and Momotaro's quests alike? Give two similarities with evidence.", "Both leave home for a goal, face dangerous trials, get help from others, and return heroes.", lines=4),
                              OR("How are they different?", "Jason seeks a throne using magic help; Momotaro helps villages with animal friends gained through kindness.", lines=3),
                              OR("How does the Grail quest in the Reader fit this pattern?", "Knights leave Camelot to seek the Grail and face trials; answers vary with details.", lines=3)], passage=P_MOMOTARO),
     S("Exit Ticket", [OR("What theme do both quest stories share?", "e.g. Heroes succeed with help from others.", lines=2)])],
    te("Students compare quest patterns across cultures.", "Compare and contrast the treatment of similar themes and patterns of events (e.g., the quest) in stories from different cultures.", "Workbook Lesson 7.3",
       "Grail, Jason, video games.", "Read Momotaro.", ["Teach the quest pattern.", "Model the comparison chart."], "Your Turn 1–3.",
       ["Comparing surface details only (names, places)."], ["Use the pattern steps."], ["Find a quest story from another culture."]),
    summary="Quest stories across cultures share a pattern.")

L4 = Lesson("7.4", "Good and Evil in Traditional Stories",
    "I can compare how traditional stories show good and evil.", "RL.4.9, RL.4.2",
    [("opposition", "A struggle between two sides.")],
    "Why do so many old stories have a clear villain?",
    [Text("Traditional stories often show the <b>opposition of good and evil</b>. Heroes usually show kindness, courage, or honesty, while villains show greed, cruelty, or trickery. Comparing how stories show this reveals what different cultures valued."),
     Figure(lambda t: table(t, [["Story", "Good shown by", "Evil shown by", "What the culture valued"], ["Jason", "courage, teamwork", "the uncle's trickery", "bravery; keeping promises"],
                                ["Momotaro", "kindness, sharing", "ogres who steal", "kindness; protecting the community"], ["King Arthur", "loyalty, fairness", "betrayal, greed", "loyalty; justice"]],
                            [1.0 * inch, 1.4 * inch, 1.4 * inch, 1.9 * inch], width=5.7 * inch, font_size=9)),
     KeyIdea("Good vs evil reveals what a culture values. Compare the qualities of heroes and villains.")],
    [Problem("What does the villain in Jason want?", "to keep the throne"), Problem("How does Momotaro show good?", "kindness and sharing; protecting villages"), Problem("What do all three stories value?", "courage / doing what is right")],
    [S("Warm-Up", [SA("Opposition means…", "a struggle between two sides"), SA("A quality of a hero", "courage, kindness")], cols=2),
     S("Compare", [OR("Choose two stories. Explain how each shows good and evil, and what each culture valued.", "Answers vary.", lines=6)]),
     S("Exit Ticket", [OR("Is every story this clear about good and evil? Give an example from King Arthur where it's complicated.", "Answers vary, e.g. Lancelot is good but makes a choice that causes harm.", lines=3)])],
    te("Students compare good and evil across stories.", "Compare themes (opposition of good and evil) across cultures.", "Workbook Lesson 7.4",
       "Why villains?", "Review the three stories.", ["Model the chart."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Thinking all characters are all good or all bad."], ["Trait sorting."], ["Write a short folktale with a clear hero and villain."]),
    summary="Good vs evil in traditional stories shows what cultures valued.")

# ================================================================= Week 2 · Compare explanations (Chapter 14)
L5 = Lesson("7.5", "Myths as Explanations",
    "I can explain how a myth explains something in nature.", "RL.4.2, RL.4.9",
    [("myth", "A traditional story, often about gods or heroes, that explains something about the world.")],
    "Before science, how might people have explained why winter comes?",
    [ReaderAssign(READER, "Chapter 14: The Death of Dindrane", "What sacrifice is made in this chapter? How do the knights respond?"),
     Text("Long ago, people told <b>myths</b> to explain things they saw in nature, such as thunder, the seasons, or the stars. Myths also teach lessons about human feelings."),
     P_PERSEPHONE,
     Example("Find the explanation", "What does the myth explain?", ["When Persephone is in the underworld, Demeter grieves and the earth grows cold.", "When she returns, Demeter is happy and plants grow."], "The myth explains why there are seasons."),
     KeyIdea("Myths explain nature through characters' actions and feelings.")],
    [Problem("Why does Demeter stop caring for the earth?", "She is grieving for her daughter."), Problem("Why must Persephone return to the underworld each year?", "She ate six pomegranate seeds there."), Problem("Which seasons happen when Persephone is away?", "autumn and winter")],
    [S("Warm-Up", [SA("A myth explains…", "something in nature (or the world)"), SA("Who is Demeter?", "goddess of the harvest")], cols=2),
     S("Use the Myth", [OR("Explain how the myth connects Demeter's feelings to the seasons.", "Grief → cold, bare winter; joy → blooming spring and summer.", lines=3),
                        OR("What lesson about feelings might the myth teach?", "e.g. Love between parents and children is powerful; grief and joy affect everything around us.", lines=2)], passage=P_PERSEPHONE),
     S("Exit Ticket", [OR("Invent a one-sentence myth explaining why it rains.", "Answers vary.", lines=2)])],
    te("Students analyze myths as explanations.", "Determine theme; compare traditional literature.", "King Arthur Reader (Chapter 14), workbook Lesson 7.5",
       "Pre-science winter.", ["Read Chapter 14.", "Read Persephone."], ["Teach myths as explanations."], "Your Turn 1–3.",
       ["Thinking myths are meant as science today."], ["Ask: What did people observe? How did the story explain it?"], ["Read another nature myth."]),
    summary="Myths explained nature through stories of gods and feelings.")

L6 = Lesson("7.6", "Scientific Explanations",
    "I can explain a scientific process using details from the text.", "RI.4.3",
    [("axis", "An imaginary line that something spins around."), ("hemisphere", "Half of Earth: Northern or Southern.")],
    "Do you think Earth is closer to the sun in summer? Why?",
    [Text("Scientific explanations are based on observations and evidence. They often correct <b>misconceptions</b> (wrong ideas) and explain causes step by step."),
     P_SEASONS,
     Example("Explain the cause", "Why is it summer in the Northern Hemisphere in July?", ["Earth's tilt points the Northern Hemisphere toward the sun.", "Sunlight hits more directly; days are longer."], "The Northern Hemisphere is tilted toward the sun, so it gets more direct light and longer days."),
     KeyIdea("Scientific explanations give causes with evidence, step by step.")],
    [Problem("What misconception does the text correct?", "that seasons happen because Earth is closer to or farther from the sun"), Problem("How much is Earth tilted?", "about 23.5 degrees"), Problem("Why is it winter in Australia during U.S. summer?", "The Southern Hemisphere is tilted away from the sun then.")],
    [S("Warm-Up", [SA("An axis is…", "an imaginary line something spins around"), SA("Two hemispheres", "Northern and Southern")], cols=2),
     S("Explain", [OR("Explain the cause of seasons in three steps.", "Earth's axis is tilted; as Earth orbits, one hemisphere tilts toward the sun (direct light, long days, summer); the other tilts away (low light, short days, winter).", lines=4),
                   OR("What evidence shows distance from the sun is NOT the cause?", "Earth is closest to the sun in early January, during Northern winter.", lines=2)], passage=P_SEASONS),
     S("Exit Ticket", [Problem("Draw a quick sketch of Earth tilted toward the sun and label summer.", "Sketch: tilted Earth; hemisphere toward sun labeled summer.", space=120, wide=True)])],
    te("Students explain scientific processes.", "Explain events, procedures, ideas, or concepts in a scientific text.", "Flashlight and ball (optional), workbook Lesson 7.6",
       "Closer in summer?", "Read the seasons text.", ["Demonstrate tilt with a flashlight and ball."], "Your Turn 1–3.",
       ["Distance misconception."], ["Flashlight demo."], ["Research equinoxes and solstices."]),
    summary="Seasons are caused by Earth's tilt, not its distance from the sun.")

L7 = Lesson("7.7", "Comparing a Myth and a Scientific Explanation",
    "I can compare how a myth and a scientific text explain the same thing.", "RL.4.9, RI.4.9",
    [],
    "Can a myth be valuable even if it isn't scientifically true?",
    [Text("A myth and a science text may explain the same event very differently. Compare <b>what</b> each says causes it, <b>how</b> each explains it, and <b>why</b> each was written."),
     Figure(lambda t: table(t, [["", "Persephone myth", "What Causes the Seasons?"], ["Cause", "Demeter's grief and joy", "Earth's tilt"], ["Based on", "stories and beliefs", "observations and evidence"],
                                ["Purpose", "explain nature; teach about feelings; entertain", "inform with facts"], ["Genre", "myth", "science text"]], [1.1 * inch, 2.3 * inch, 2.3 * inch], width=5.7 * inch)),
     KeyIdea("Myths explain with stories and teach values; science explains with evidence. Both show how people understand the world.")],
    [Problem("What causes the seasons in the myth?", "Demeter's feelings about Persephone"), Problem("What causes the seasons in science?", "Earth's tilt"), Problem("What is still valuable about the myth?", "It teaches about love and grief and shows how ancient Greeks thought.")],
    [S("Warm-Up", [SA("Myth purpose", "explain nature, teach, entertain"), SA("Science purpose", "inform with evidence")], cols=2),
     S("Compare", [OR("Write a paragraph comparing the two explanations of the seasons. Use a comparison transition and a contrast transition.", "Both explain why seasons change. However, the myth uses Demeter's feelings, while science uses Earth's tilt and evidence.", lines=7)]),
     S("Exit Ticket", [OR("Answer the Get Ready question: Can a myth be valuable even if it isn't scientifically true? Explain.", "Answers vary; yes, it teaches values and history of ideas.", lines=2)])],
    te("Students compare myth and science.", "Integrate information from two texts; compare genres.", "Workbook Lesson 7.7",
       "Valuable myths?", "Reread both texts.", ["Model the chart."], "Write the paragraph.",
       ["Calling the myth “wrong” and stopping there."], ["Focus on purpose."], ["Compare a weather myth with a weather report."]),
    summary="Compare cause, basis, and purpose of myth and science explanations.")

L8 = Lesson("7.8", "Which Explanation Is Better?",
    "I can evaluate which of two explanations is clearer and better supported.", "RI.4.8, RI.4.9",
    [("gravity", "The force that pulls objects toward each other.")],
    "If one explanation is one sentence and another is three paragraphs, which is better?",
    [Text("A better explanation is not just longer: it is <b>complete</b> (explains how, not just what), <b>accurate</b>, <b>clear</b>, and <b>supported</b> with details."),
     P_TIDES_A, P_TIDES_B,
     Example("Evaluate", "Which explains tides better?", ["A says the moon causes tides but not how.", "B explains gravity, the two bulges, Earth's spin, and the sun's role."], "B is better: it is complete and gives supporting details."),
     KeyIdea("Judge explanations by completeness, accuracy, clarity, and support.")],
    [Problem("What does A leave out?", "how the moon causes tides"), Problem("Why do most places have two high tides a day?", "Earth spins through two bulges"), Problem("When are tides extra high?", "when the sun and moon line up: full and new moon")],
    [S("Warm-Up", [SA("Gravity is…", "a force that pulls objects toward each other"), SA("Is longer always better?", "No")], cols=2),
     S("Evaluate", [OR("Explain why Explanation B is more complete. Use two details from B.", "It explains gravity pulling the water into a bulge and Earth spinning through two bulges.", lines=3),
                    OR("Is there anything Explanation A does well?", "It is short and clear; it gets the main cause right.", lines=2),
                    OR("Add one sentence to Explanation A to make it better.", "e.g. The moon's gravity pulls ocean water toward it, making a bulge.", lines=2)]),
     S("Exit Ticket", [OR("Which seasons explanation from this week was more complete, the myth or the science text, if your goal is to understand the cause? Why?", "The science text, because it explains the real cause with evidence.", lines=2)])],
    te("Students evaluate explanations.", "Explain how an author uses reasons and evidence; integrate information from two texts.", "Workbook Lesson 7.8",
       "Short vs long.", "Read both tide explanations.", ["Teach the four criteria."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Choosing the longer text automatically."], ["Criteria checklist."], ["Rewrite a confusing explanation from a manual."]),
    summary="Better explanations are complete, accurate, clear, and supported.")

# ================================================================= Week 3 · Integrate source details (Chapter 15)
L9 = Lesson("7.9", "Integrating Details from Several Sources",
    "I can combine details from several sources into one clear paragraph.", "RI.4.9, W.4.2b",
    [],
    "How is combining sources like making a smoothie?",
    [ReaderAssign(READER, "Chapter 15: The Achievement of the Grail", "Who achieves the Grail? Why him?"),
     Text("When you integrate sources, you blend details from each into one smooth explanation, using transitions and naming the sources."),
     KNIGHT_SOURCES[0], KNIGHT_SOURCES[1], KNIGHT_SOURCES[2],
     Example("Integrate three sources", "How did a boy become a knight?",
             ["Source 1: page at seven, manners and wooden swords.", "Source 2: squire at fourteen, served a knight, real weapons.", "Source 3: dubbed around twenty-one."],
             "Becoming a knight took about fourteen years. Boys began as pages at around seven, learning manners and practicing with wooden swords. At about fourteen they became squires, serving a knight and training with real weapons. Finally, around age twenty-one, a squire could be dubbed a knight in a special ceremony."),
     KeyIdea("Blend details in a logical order with transitions; don't just list source by source.")],
    [Problem("At what age did a page become a squire?", "about fourteen"), Problem("What is dubbing?", "the ceremony that made a squire a knight"), Problem("What transition words help integrate?", "first, then, at about…, finally")],
    [S("Warm-Up", [SA("Page age", "about seven"), SA("Knight age", "about twenty-one")], cols=2),
     S("Integrate", [OR("Write a paragraph explaining what a squire did. Use details from at least two sources.", "Squires served a knight, cared for his horse and armor, followed him to battle, trained with real weapons, and learned chivalry; some later became knights by dubbing.", lines=6)]),
     S("Chapter 15", [OR("Who achieves the Grail, and what qualities from the knight sources does he show?", "Answers vary; e.g. Galahad shows purity, loyalty, chivalry.", lines=3)])],
    te("Students integrate details from multiple sources.", "Integrate information from several texts on the same topic in order to write knowledgeably.", "King Arthur Reader (Chapter 15), workbook Lesson 7.9",
       "Smoothie metaphor.", ["Read Chapter 15.", "Read the three knight sources."], ["Model integrating in time order."], "Write together.",
       ["Writing three separate mini-summaries."], ["Timeline organizer first."], ["Add a quote from the Reader."]),
    summary="Integrate: blend details from sources in logical order with transitions.")

L10 = Lesson("7.10", "Quoting and Citing Within Writing",
    "I can include short quotations and name the source within my sentences.", "W.4.8, W.4.9",
    [("citation", "Naming where information came from.")],
    "How can readers tell which source a fact came from?",
    [Text("Name the source in the sentence: <i>According to “The Squire's Training,” …</i> or <i>Source 3 explains that …</i>. Put exact words in quotation marks and keep quotations short."),
     Figure(lambda t: table(t, [["Citation starters"], ["According to “___,” …"], ["The author of “___” explains that …"], ["In “___,” we learn that …"], ["As Source ___ states, “…”"]], [4.2 * inch], width=4.2 * inch)),
     Example("Quote and cite", "Combine a quote with your own words.", ["Choose a short, important phrase.", "Introduce it with the source."], "According to “The Dubbing Ceremony,” a lord “tapped him on the shoulder with a sword and declared him a knight.”"),
     KeyIdea("Name the source; quote only short, powerful phrases; put exact words in quotation marks.")],
    [Problem("Citation starter", "According to “___,” …"), Problem("Should quotes be long or short?", "short"), Problem("What goes around exact words?", "quotation marks")],
    [S("Warm-Up", [SA("A citation tells…", "where information came from"), SA("Exact words need…", "quotation marks")], cols=2),
     S("Practice", [OR(f"Write a sentence that cites {src} and includes a short quotation.", "Answers vary.", lines=2) for src in ["“Becoming a Page”", "“What Causes the Seasons?”", "“Why the Ocean Has Tides”"]]),
     S("Exit Ticket", [OR("Why is citing sources important?", "It gives credit, shows readers where facts came from, and avoids plagiarism.", lines=2)])],
    te("Students quote and cite within writing.", "Recall relevant information; take notes; provide a list of sources; draw evidence.", "Workbook Lesson 7.10",
       "Which source?", "Review sources.", ["Teach citation starters."], "Your Turn 1–3.",
       ["Long block quotes."], ["Limit quotes to ten words."], ["Cite the Reader in a sentence."]),
    summary="Name sources and quote short phrases within sentences.")

L11 = Lesson("7.11", "Quote, Paraphrase, or Summarize?",
    "I can choose whether to quote, paraphrase, or summarize information from a source.", "W.4.8",
    [],
    "When should you use the author's exact words?",
    [Figure(lambda t: table(t, [["Choice", "Use it when…", "Example"], ["Quote", "the exact words are powerful or important", "“he could not have succeeded alone”"],
                                ["Paraphrase", "you need one specific idea in your own words", "Jason needed help to complete his quest."], ["Summarize", "you need the main points of a whole text", "Jason sailed with heroes, completed impossible tasks with Medea's help, and won the fleece."]],
                            [1.0 * inch, 2.3 * inch, 2.4 * inch], width=5.7 * inch, font_size=9)),
     KeyIdea("Quote for powerful words, paraphrase for one idea, summarize for the whole text, and always cite.")],
    [Problem("Best choice to share the main points of the seasons text", "summarize"), Problem("Best choice for “the earth blooms again”", "quote (vivid words)"), Problem("Best choice for one fact about tides", "paraphrase")],
    [S("Warm-Up", [SA("Summarize =", "main points of a whole text"), SA("Paraphrase =", "one idea in your own words")], cols=2),
     S("Practice All Three", [OR("Quote from “Momotaro”:", "Answers vary; exact words in quotes.", lines=2), OR("Paraphrase one idea from “Momotaro”:", "e.g. Momotaro made friends by sharing his food.", lines=2),
                              OR("Summarize “Momotaro” in two sentences:", "A boy born from a peach sets out to stop ogres. With animal friends he gained by sharing, he defeats them and returns the treasure.", lines=3)]),
     S("Exit Ticket", [OR("Which is hardest for you: quote, paraphrase, or summarize? Why?", "Answers vary.", lines=2)])],
    te("Students choose quote, paraphrase, or summary.", "Paraphrase information; summarize; take notes.", "Workbook Lesson 7.11",
       "Exact words?", "Review Momotaro.", ["Teach the chart."], "Your Turn 1–3.",
       ["Paraphrases too close to the original."], ["Cover the text before paraphrasing."], ["Use all three in a paragraph."]),
    summary="Quote powerful words, paraphrase ideas, summarize whole texts.")

L12 = Lesson("7.12", "Collaborative Discussion",
    "I can take part in a discussion by building on others' ideas and using evidence.", "SL.4.1",
    [("discussion norms", "Agreed rules for a respectful conversation.")],
    "What makes a conversation about a book go well?",
    [Text("Good discussions follow <b>norms</b>: come prepared, listen, take turns, build on others' ideas, ask questions, and support opinions with evidence."),
     Figure(lambda t: table(t, [["Discussion starters"], ["I agree with ___ because …"], ["I'd like to add to what ___ said …"], ["I see it differently because …"], ["Can you explain what you mean by …?"], ["My evidence is on page ___, where …"]],
                            [4.6 * inch], width=4.6 * inch)),
     KeyIdea("Prepare, listen, build on ideas, ask questions, and use evidence.")],
    [Problem("Starter to disagree respectfully", "I see it differently because…"), Problem("Why come prepared?", "to share evidence and ideas"), Problem("What should you do while others speak?", "listen; think about how to build on their ideas")],
    [S("Warm-Up", [SA("A discussion norm", "take turns, listen"), SA("Starter to add on", "I'd like to add to what ___ said…")], cols=2),
     S("Prepare", [OR("Discussion question: Why did Galahad achieve the Grail when other great knights did not? Write your answer with two pieces of evidence from the Reader.", "Answers vary.", lines=5),
                   OR("Write one question to ask others.", "Answers vary.", lines=1)]),
     S("Reflect", [OR("After the discussion: What idea did someone else share that changed or added to your thinking?", "Answers vary.", lines=3)])],
    te("Students take part in collaborative discussion.", "Engage effectively in collaborative discussions, building on others' ideas and expressing their own clearly.", "Workbook Lesson 7.12",
       "Good book talks.", "Skim Chapter 15.", ["Teach norms and starters."], "Hold a 10–15 minute family discussion.",
       ["Waiting to talk instead of listening."], ["Talking chips or turns."], ["Lead the discussion."], independent="Discussion and reflection.", exit_="Reflection. Weekly Check tomorrow."),
    summary="Discuss with norms, evidence, and respect.")

# ================================================================= Week 4 · Write and revise a synthesis (Chapter 16)
L13 = Lesson("7.13", "Planning a Synthesis Essay",
    "I can plan an essay that answers a guiding question with evidence from several texts.", "W.4.2, W.4.9",
    [("synthesis essay", "An essay that combines ideas from several texts to answer one question.")],
    "After reading so many hero stories, what do you now think makes a hero?",
    [ReaderAssign(READER, "Chapter 16: Sir Lancelot and the Lily Maid of Astolat", "Is Lancelot a hero in this chapter? Why or why not?"),
     Text("A <b>synthesis essay</b> answers a guiding question with a thesis, then supports it with evidence from <b>several texts</b>. Each body paragraph makes one point and uses at least two texts."),
     Example("Plan", "Guiding question: What makes a hero?", ["Thesis: A hero is someone who faces fear for others and accepts help along the way.", "Body 1: facing fear for others (Nell, Ada, Pip).", "Body 2: accepting help (Jason, Momotaro, Arthur)."],
             "Each body paragraph uses at least two texts."),
     KeyIdea("Thesis → body paragraphs that each use two or more texts → conclusion.")],
    [Problem("What is a synthesis essay?", "an essay combining ideas from several texts to answer a question"), Problem("How many texts per body paragraph?", "at least two"), Problem("What goes first?", "the thesis (in the introduction)")],
    [S("Warm-Up", [SA("Synthesis combines…", "ideas from several texts"), SA("Guiding question this unit", "What makes a hero?")], cols=2),
     S("Plan", [OR("Your thesis:", "Answers vary.", lines=2), OR("Body 1 point + two texts with evidence:", "Answers vary.", lines=4), OR("Body 2 point + two texts with evidence:", "Answers vary.", lines=4), OR("Conclusion idea:", "Answers vary.", lines=2)])],
    te("Students plan synthesis essays.", "Write informative texts; draw evidence from multiple texts.", "King Arthur Reader (Chapter 16), workbook Lesson 7.13",
       "What makes a hero now?", "Read Chapter 16.", ["Model the plan."], "Plan.",
       ["Body paragraphs using one text each."], ["Grid: points × texts."], ["Include a counterexample (Lancelot)."], independent="Finish the plan."),
    summary="Plan a thesis and body paragraphs using several texts each.")

L14 = Lesson("7.14", "Drafting the Synthesis Essay",
    "I can draft a synthesis essay that integrates and cites several texts.", "W.4.2, W.4.8, W.4.9",
    [],
    "How do you move smoothly from one text to another in a paragraph?",
    [Text("Use transitions to move between texts: <i>Similarly, Likewise, In the same way, Another example is, On the other hand</i>. Cite each text by title."),
     Example("Body paragraph", "Point: Heroes face fear to help others.",
             ["Topic sentence.", "Text 1 evidence: In “The Lighthouse Keeper's Daughter,” Nell climbs the tower with trembling hands.", "Transition + Text 2: Similarly, in “The Bridge at Millbrook,” Ada stands in the rain to stop the wagons.", "Explanation."],
             "Heroes face their fears to help others. In “The Lighthouse Keeper's Daughter,” Nell climbs a hundred stairs in a storm with trembling hands to light the lamp. Similarly, in “The Bridge at Millbrook,” Ada races to warn the town before the bridge collapses. Both girls are afraid, but they act anyway, which is what makes them heroes."),
     KeyIdea("Move between texts with transitions; cite each; explain how the evidence supports your point.")],
    [Problem("Transition to add a second example", "Similarly, Another example is"), Problem("How do you cite a short story?", "title in quotation marks"), Problem("What follows the evidence?", "explanation")],
    [S("Warm-Up", [SA("Transition: In the same ___", "way"), SA("Short story title format", "quotation marks")], cols=2),
     S("Draft", [OR("Draft your synthesis essay.", "Answers vary.", lines=24, note="Look for: thesis; two body paragraphs each with two or more texts cited; transitions; explanations; conclusion.")])],
    te("Students draft synthesis essays.", "Write informative texts linking ideas across categories; draw evidence from texts.", "Plans, workbook Lesson 7.14",
       "Moving between texts.", "Reread model paragraph.", ["Model a body paragraph."], "Draft.",
       ["Forgetting to name texts."], ["Highlight each text in a different color."], ["Add a third body paragraph."], independent="Finish the draft."),
    summary="Use transitions and citations to move between texts.")

L15 = Lesson("7.15", "Revising with Peer Feedback",
    "I can give and use helpful feedback to revise my essay.", "W.4.5, SL.4.1",
    [("feedback", "Comments that help a writer improve.")],
    "What kind of feedback actually helps you improve?",
    [Text("Helpful feedback is <b>kind</b>, <b>specific</b>, and <b>helpful</b>. Use the frame: <i>I like… because…</i> / <i>I wonder… / Have you thought about…?</i>"),
     Figure(lambda t: table(t, [["Feedback checklist for a partner's essay"], ["Can I find the thesis? Underline it."], ["Does each body paragraph use two or more texts?"], ["Are the texts named?"], ["Is there an explanation after the evidence?"], ["Does the conclusion answer the guiding question?"]],
                            [5.0 * inch], width=5.0 * inch)),
     KeyIdea("Kind, specific, helpful feedback; then revise using it.")],
    [Problem("Is “It's good” helpful feedback?", "No, not specific"), Problem("Feedback frame starter", "I like… because… / I wonder…"), Problem("What should you do with feedback?", "use it to revise")],
    [S("Warm-Up", [SA("Feedback should be…", "kind, specific, helpful"), SA("Unhelpful feedback example", "It's good.")], cols=2),
     S("Give and Use Feedback", [OR("Feedback I received (two comments):", "Answers vary.", lines=3), OR("Two revisions I made because of it:", "Answers vary.", lines=3)])],
    te("Students give and use peer feedback.", "Develop and strengthen writing with guidance and support from peers and adults.", "Drafts, workbook Lesson 7.15",
       "Helpful feedback.", "Read a partner's draft.", ["Model feedback frames."], "Exchange feedback.",
       ["Only praising or only criticizing."], ["Frame cards."], ["Give feedback on a sibling's writing."], independent="Revise."),
    summary="Kind, specific, helpful feedback leads to better revisions.")

L16 = Lesson("7.16", "Editing and Publishing the Synthesis Essay",
    "I can edit and publish my synthesis essay.", "W.4.5, W.4.6, L.4.2",
    [],
    "How will you share your final essay?",
    [Figure(lambda t: table(t, [["Editing checklist", "✓"], ["Titles: books underlined/italic; stories in quotation marks.", ""], ["Quotations have quotation marks and are introduced.", ""], ["Commas after introductory words (However, Similarly, In addition,).", ""],
                                ["Complete sentences; no run-ons.", ""], ["Spelling checked.", ""]], [W * 0.8, W * 0.12], width=W * 0.92)),
     Text("Publish by typing the essay (with help, if needed) or copying it neatly. Add a title and a source list."),
     KeyIdea("Edit for conventions, then publish with a title and source list.")],
    [Problem("Punctuate: However the myth is still valuable", "However, the myth is still valuable."), Problem("Format: Treasure Island (typed)", "italics"), Problem("Format: Momotaro, the Peach Boy (story)", "quotation marks")],
    [S("Warm-Up", [SA("Comma after: Similarly", "Similarly,"), SA("Typed book titles are…", "italic")], cols=2),
     S("Edit Sentences", [SA(q, a) for q, a in [("in addition jason needed help", "In addition, Jason needed help."), ("according to the seasons text earth is tilted", "According to the seasons text, Earth is tilted."),
                                                ("momotaro shared his dumplings", "Momotaro shared his dumplings."), ("however the myth explains winter", "However, the myth explains winter.")]], cols=1),
     S("Publish", [OR("Publish your essay. Write your final title here and one sentence about what you're proudest of.", "Answers vary.", lines=2)])],
    te("Students edit and publish.", "Use technology to produce and publish writing; demonstrate command of conventions.", "Final drafts, computer (optional), workbook Lesson 7.16, Unit 7 Review",
       "Sharing plans.", "Read the checklist.", ["Model editing commas after introductory words."], "Edit.",
       ["Missing commas after transitions."], ["Circle every transition, then check its comma."], ["Read the essay at a family “author's celebration.”"], independent="Publish; then the Unit 7 Review.", exit_="Tomorrow: Unit 7 Test."),
    summary="Edit conventions; publish with a title and sources.")

# ================================================================= checks
C1 = Check("Weekly Check 19: Quest Patterns", [S("Read and answer", [
    OR("What is Anya's quest?", "to find the Spring and bring it back from the Frost King's ice palace", lines=2),
    OR("How does Anya gain helpers? What does this show about her?", "by sharing bread, freeing a sparrow, carrying an old woman; she is kind", lines=2),
    OR("Compare Anya's quest with Momotaro's. Give one similarity and one difference.", "Similar: kindness earns helpers who help defeat the villain. Different: Anya's helpers include a fairy; Momotaro fights ogres.", lines=3),
    OR("What theme does this folktale share with Momotaro?", "Kindness to others is rewarded.", lines=2)], passage=P_C19)], minutes=20)

C2 = Check("Weekly Check 20: Comparing Explanations", [S("Read Text A", [], passage=P_C20A), S("Read Text B, then answer", [
    OR("According to the myth, why does the moon change shape?", "She eats too many stars and swells, then hides her face in shame.", lines=2),
    OR("According to science, why does the moon have phases?", "We see different amounts of its sunlit side as it orbits Earth.", lines=2),
    MC("Which text is based on evidence?", ["Text A", "Text B"], 1),
    OR("What lesson might the myth teach?", "e.g. Being too proud or greedy leads to shame.", lines=2)], passage=P_C20B)], minutes=20)

C3 = Check("Weekly Check 21: Integrating Sources", [S("Read Source A", [], passage=P_C21A), S("Read Source B, then answer", [
    OR("What is a siege?", "surrounding a castle for months so the people inside run out of food", lines=1),
    OR("Write one sentence that integrates a detail from each source.", "e.g. Castles had stone walls over ten feet thick and stored grain and water, so they could survive both fire and long sieges.", lines=3),
    OR("Write a sentence that cites Source A with a short quotation.", "e.g. According to “Castle Walls,” walls were “more than ten feet thick.”", lines=2),
    MC("To give the main points of Source B, you would…", ["quote it", "summarize it", "copy it"], 1)], passage=P_C21B)], minutes=20)

REVIEW = Check("Unit 7 Review", [
    S("Skills", [SA("A text set is…", "texts on one topic"), SA("Steps of the quest pattern", "call, journey, helpers, trials, success, return"), SA("Myths explain with…", "stories of gods and heroes"),
                 SA("Science explains with…", "evidence"), SA("Citation starter", "According to “___,”"), SA("Feedback should be…", "kind, specific, helpful")], cols=2),
    S("Apply", [OR("Integrate details from two knight sources into one sentence.", "e.g. Boys trained as pages from about age seven and became squires at fourteen, serving a knight.", lines=2),
                OR("Write a thesis answering: What makes a good explanation?", "e.g. A good explanation is complete, accurate, and supported by evidence.", lines=2)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 7 Test", [
    S("Part A · Text A (1 point each)", [
        OR("What does the myth say causes smoke and sparks from the mountain?", "Vulcan working at his forge beneath the mountain", lines=2),
        OR("What does the myth say causes melted rock to spill out?", "Vulcan's anger", lines=1),
        OR("What word comes from Vulcan's name?", "volcano", lines=1)], passage=P_TEST_A),
    S("Part B · Text B (1 point each)", [
        OR("What is the difference between magma and lava?", "Magma is melted rock underground; lava is magma that reaches the surface.", lines=2),
        OR("Explain the soda-bottle comparison.", "Pressure builds as magma collects, like gas in a shaken bottle, until it bursts out.", lines=2),
        OR("Why do scientists watch for small earthquakes?", "They can be a sign magma is moving before an eruption; to warn people.", lines=2)], passage=P_TEST_B),
    S("Part C · Compare and integrate (1 point each)", [
        OR("Both texts mention the ground shaking. How does each explain it?", "Myth: Vulcan pounding his hammer. Science: magma moving underground causes small earthquakes.", lines=3, points=2),
        MC("Which text's main purpose is to inform with evidence?", ["Text A", "Text B"], 1),
        OR("What do the ancient Romans' myth and modern science both notice about volcanoes?", "smoke/ash, shaking ground, melted rock coming out", lines=2)]),
    S("Part D · Synthesis writing (5 points)", [OR("Write a paragraph comparing how the two texts explain volcanoes. Include a topic sentence, evidence from both texts with citations, comparison and contrast transitions, and a concluding sentence about why both texts are valuable.",
                                                   "Rubric: topic sentence (1); cited evidence from A (1); cited evidence from B (1); transitions (1); conclusion on the value of both (1).", lines=14, points=5)])],
    kind="test", minutes=45, rubric=[["13–15 (85%+)", "Mastered."], ["10–12", "Proficient; review missed skills."], ["Below 10", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-04-26", "2027-05-03", "2027-05-10", "2027-05-17"], CHECKS, REVIEW, TEST)

UNIT = Unit(7, "Reading Across Texts", "Text sets, quests across cultures, myth and science explanations, integrating sources, discussion, and the synthesis essay, with King Arthur Chapters 13–16.",
    "The Grail quest reaches its end, and you'll discover that quest stories appear all over the world. You'll read myths and folktales from Greece and Japan, compare ancient explanations of nature with scientific ones, combine information from several sources, discuss ideas with others, and write a synthesis essay answering the question: What makes a hero?",
    ["Read text sets with a guiding question and annotate connections.", "Compare quest patterns and good vs evil across cultures.", "Compare myths and scientific explanations; evaluate explanations.",
     "Integrate, quote, paraphrase, and summarize sources; discuss with evidence.", "Plan, draft, revise, and publish a synthesis essay."],
    [("RL.4.9", "Compare themes and patterns of events in stories, myths, and traditional literature from different cultures."), ("RI.4.3, RI.4.8, RI.4.9", "Explain scientific concepts; evaluate reasons and evidence; integrate texts."),
     ("W.4.2, W.4.5, W.4.8, W.4.9", "Write informative texts from several sources; revise; cite."), ("SL.4.1", "Engage in collaborative discussions.")],
    [("text set", "Texts about one topic."), ("quest", "A journey toward an important goal."), ("myth", "A traditional story explaining the world."), ("citation", "Naming a source."), ("synthesis", "Combining ideas from several texts.")],
    ["Units 5–6: comparing texts and sources."], ["King Arthur and the Round Table Reader (Chapters 13–16)", "Sticky notes; a flashlight and ball for the seasons demo"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="When you research anything, from a school project to a big purchase, you read several sources and combine what they say.",
    family_note="Share a story or myth from your own family's culture or heritage and compare it with the quest stories your student read.",
    weeks=WEEKS)
