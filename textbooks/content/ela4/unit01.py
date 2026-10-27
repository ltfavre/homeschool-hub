"""Grade 4 ELA · Unit 1: Word Power — word parts, context clues, figurative language, and vocabulary in writing.
Anchor reading: King Arthur and the Round Table Reader, Chapters 1–4 (Oct 12 – Nov 6, 2026)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule

READER = "King Arthur and the Round Table Reader"


def S(title, problems, intro=None, cols=1, passage=None):
    return Section(title, problems, intro, cols, passage)


def MC(prompt, choices, correct, note=None):
    """Multiple choice. correct: index of the right choice."""
    return Problem(prompt, f"{chr(65 + correct)}. {choices[correct]}", choices=choices, space=0, note=note, wide=True)


def OR(prompt, answer, lines=2, note=None, points=1):
    """Open response written on lines."""
    return Problem(prompt, answer, lines=lines, space=0, wide=True, note=note, points=points)


def SA(prompt, answer, note=None):
    """Short answer on one answer line (two per row)."""
    return Problem(prompt, answer, space=0, note=note)


# ================================================================= passages (original)
P_KITE = Passage("The Unlucky Kite", [
    "Mia was unhappy. Her new kite had disappeared over the tall fence behind the library. She had misjudged the wind, and the string had slipped right out of her fingers.",
    "“We can rebuild it,” said her brother Theo. “I'll reread the directions, and you can retie the tail.”",
    "Mia shook her head. “It's not the same. That kite was a gift from Grandma. I disliked the old one, but I loved this one.”",
    "Just then, a woman leaned over the fence. She held up a bright red kite with a crooked tail. “Is this yours?” she asked with a smile. “It landed in my tomato plants. Next time, I suggest you pretest the wind before you let out all that string!”",
    "Mia's frown disappeared. This was not such an unlucky day after all.",
], source="An original story", genre="Realistic fiction")

P_GARDEN = Passage("Mr. Hollis and the Hopeless Garden", [
    "Everyone on Pine Street agreed that the empty lot was hopeless. It was full of broken bottles, rusty cans, and weeds taller than a fourth grader.",
    "Then Mr. Hollis, a retired gardener, moved in next door. Every morning he worked slowly and carefully, pulling weeds and filling bags with trash. His neighbors thought his effort was pointless.",
    "By June, though, the darkness of the old lot had given way to bright sunflowers and rows of beans. Children who had once been fearless about climbing the fence now walked gently between the rows. Mr. Hollis let anyone pick vegetables, as long as they were thankful and left the plants unharmed.",
    "“Nothing is hopeless,” Mr. Hollis told a reporter, “if you are willing to get your hands dirty.”",
], source="An original story", genre="Realistic fiction")

P_MESSAGES = Passage("Messages Across the Miles", [
    "Long ago, sending a message far away was slow. A rider might transport a letter on horseback for weeks. Some kingdoms used tall towers with fires on top, so that a guard could see a visible signal from one hill to the next.",
    "In the 1800s, the <b>telegraph</b> changed everything. Electric signals traveled along wires, and an operator wrote down the message in dots and dashes. A few years later, the <b>telephone</b> let people hear each other's voices across many miles.",
    "Today, a video call lets a grandmother in Texas see and hear her grandson in Japan at the same moment. The audience for a single online video can include millions of people. The roots of these words come from Greek and Latin, but the inventions are as modern as the phone in your pocket.",
], source="An original informational text", genre="Informational text")

P_SMITH = Passage("The Blacksmith's Apprentice", [
    "When Tom turned ten, his father sent him to be an <b>apprentice</b>, a young worker who learns a trade by helping a master. His master was Old Rowan, the village blacksmith.",
    "The smithy was always hot. In the middle of the room stood the <b>forge</b>, a fireplace where metal is heated until it glows. Tom's first job was to pump the <b>bellows</b>. Each time he squeezed the leather bag, it pushed a gust of air into the fire, and the coals blazed orange.",
    "Rowan held glowing iron on the <b>anvil</b> and pounded it with his hammer. Sparks flew like tiny stars. Unlike the soft, bendable iron that came out of the fire, the finished horseshoe was <b>rigid</b> after it cooled in a bucket of water.",
    "At the end of the first week, Tom's arms ached and his face was smudged with soot. But when a knight's horse trotted away on shoes Tom had helped make, he felt as proud as a king.",
], source="An original story", genre="Historical fiction")

P_KNIGHTS = Passage("Two Brothers, Two Knights", [
    "Sir Gareth and Sir Gaheris were brothers, but they were as different as night and day. Gareth was <b>boisterous</b>. He laughed loudly, sang at dinner, and told jokes that echoed through the great hall. Gaheris, on the other hand, was quiet and thoughtful.",
    "Gareth was also <b>impulsive</b>. He jumped into adventures without thinking. Gaheris was cautious; he studied every map and asked every question before he rode out.",
    "Yet the brothers agreed on one thing: a knight must be <b>gallant</b>, or brave and polite, to everyone, from the queen to the poorest farmer.",
], source="An original story", genre="Historical fiction")

P_KITCHEN = Passage("The Castle Kitchen", [
    "Before sunrise, the castle kitchen was already busy. Cooks chopped onions, turnips, and other <b>root vegetables</b>. A boy turned a huge spit so the meat roasting over the fire would cook evenly.",
    "The head cook was <b>stern</b>. She never smiled, and when a kitchen maid dropped a basket of eggs, the cook's voice was so sharp that everyone froze.",
    "By noon the long tables in the hall were covered with platters of bread, stews, and pies. The <b>feast</b> lasted until the candles burned low, and the guests could not eat another bite.",
], source="An original informational story", genre="Historical fiction")

P_FAIR = Passage("A Day at the Fair", [
    "On Saturday, Leo and his sister Nia went to the county fair. First they watched a juggler toss knives into the air. “Watch your step!” called a man as they passed a muddy puddle near the pig pens.",
    "Nia wanted to ride the Ferris wheel, but the line was long. “Let's wait,” said Leo. “It will move faster after the band starts to play.”",
    "Later, Leo paid two dollars to throw rings at a row of bottles. He tossed the last ring, and it landed right around a bottle neck. He won a stuffed bear as big as a pillow.",
], source="An original story", genre="Realistic fiction")

P_STORM = Passage("Storm over the Moor", [
    "The sky over the moor turned as dark as an iron pot. Wind howled like a hungry wolf, and the tall grass bent low to the ground.",
    "Sir Bedivere pulled his cloak tighter. His horse was a statue, refusing to take another step. Rain fell in silver sheets, stinging his face like a hundred tiny needles.",
    "At last, a light appeared in the distance. The little cottage was a lighthouse in a sea of storm. Bedivere's heart, cold as a stone a moment before, warmed with hope.",
], source="An original story", genre="Historical fiction")

P_GRANDPA = Passage("Grandpa's Sayings", [
    "My grandpa has a saying for everything. When I complained about cleaning my room, he said, “Many hands make light work,” and then he helped me fold my clothes.",
    "When my sister was nervous about her piano recital, he told her to “break a leg.” She looked worried until Mom explained that it means “good luck.”",
    "Last week, I wanted to quit soccer after we lost three games in a row. Grandpa put his hand on my shoulder. “Rome wasn't built in a day,” he said. “Keep practicing.”",
    "I used to think his sayings were silly. Now, whenever I'm about to give up, I can almost hear him say, “Hang in there, kiddo.”",
], source="An original personal narrative", genre="Personal narrative")

P_CASTLES = Passage("How a Castle Kept People Safe", [
    "During the Middle Ages, lords built castles to protect their land and people. Many castles were surrounded by a <b>moat</b>, a deep ditch often filled with water.",
    "To enter, visitors crossed a <b>drawbridge</b>, a bridge that could be raised to block the gate. The tops of the thick walls had <b>battlements</b>, which were walls with gaps that let archers shoot while staying protected.",
    "The strongest part of the castle was the <b>keep</b>, a tall tower where the lord's family lived. If enemies broke through the outer walls, everyone could retreat to the keep.",
], source="An original informational text", genre="Informational text")

# Checks and test passages
P_C1 = Passage("The Unbreakable Promise", [
    "Ava was careless with her library books. She had misplaced two of them, and the librarian, Mr. Chen, was displeased.",
    "“I will repay you for them,” Ava promised. “I'll use the money I earn walking dogs.”",
    "For three weeks, Ava walked dogs every afternoon, rain or shine. When she finally handed Mr. Chen the money, he smiled. “That was a thoughtful thing to do. Your promise was unbreakable.”",
], source="An original story", genre="Realistic fiction")

P_C2 = Passage("The Falconer", [
    "Lady Elaine was the castle's <b>falconer</b>. Like a teacher for birds, she trained falcons to hunt and return to her glove.",
    "Training a falcon took great <b>patience</b>. Elaine waited for hours, never hurrying, until the young bird trusted her.",
    "Her best falcon, Swift, was <b>docile</b> with Elaine but wild with strangers. When anyone else came near, Swift screeched and flapped its wings.",
    "One day Swift soared so high it was barely visible, just a speck in the clouds. Then it <b>plummeted</b>, dropping straight down like a stone, and landed gently on Elaine's glove.",
], source="An original story", genre="Historical fiction")

P_C3 = Passage("Snow Day", [
    "When I woke up, the world outside my window was a giant white blanket. Snowflakes danced like tiny ballerinas past the glass.",
    "My little brother was a rocket, zooming down the stairs to find his boots. “It's raining cats and dogs!” he shouted. “Snow cats and snow dogs!”",
    "We built a snowman as tall as Dad. By lunchtime, my fingers were icicles, but I had never felt happier.",
], source="An original personal narrative", genre="Personal narrative")

P_TEST = Passage("The Squire's First Tournament", [
    "Will had been a <b>squire</b>, a knight's helper in training, for only one month when Sir Owen entered the great tournament. Will's job was to keep Sir Owen's armor polished and his horse ready. He was nervous; he didn't want to be careless and disappoint his master.",
    "On the morning of the tournament, the field was a sea of colorful tents. Banners snapped in the wind like flags on a ship. Hundreds of people crowded the stands, cheering and waving.",
    "Will checked every buckle twice. Then he noticed something terrible: a strap on Sir Owen's saddle was <b>frayed</b>, its threads worn and coming apart. If it broke during the joust, Sir Owen could fall.",
    "Will didn't hesitate. He ran to the saddle maker's tent and returned with a new strap just as the trumpets sounded. His hands were shaking, but he replaced the strap quickly and carefully.",
    "Sir Owen won his first match. Afterward, he clapped Will on the shoulder. “A knight is only as good as his squire,” he said. “Today, you were my hero.” Will's face glowed like the sunrise.",
], source="An original story", genre="Historical fiction")


# ================================================================= Week 1 · Use word parts (Chapter 1)
L1 = Lesson("1.1", "Meet King Arthur: Reading a Legend",
    "I can describe the characters and setting of a legend and use details from the text.", "RL.4.1, RL.4.3",
    [("legend", "A story from long ago about a hero; parts may be true, but much is made up."), ("character", "A person or animal in a story."),
     ("setting", "When and where a story takes place."), ("detail", "A small piece of information in a text.")],
    "Have you ever heard a story about a hero who did something no one else could do? What made that person a hero?",
    [ReaderAssign(READER, "Chapter 1: The Birth of Arthur", "Who are the important characters? Where and when does the story take place?"),
     Text("The stories of King Arthur are <b>legends</b>. People told them for hundreds of years, and each storyteller added new details. A legend usually has a hero, a time long ago, and events that are hard to believe, such as magic."),
     Text("When you describe a character or setting, use <b>details from the text</b>, not just your opinion. Strong readers say what the text says and then explain what it shows."),
     Example("Describe a character", "What kind of person is Merlin?",
             ["Find a detail: Merlin is a wizard who takes care of the baby Arthur's future.", "Ask: What does that show about him?", "Write a sentence that names the trait and the detail."],
             "Merlin is wise and powerful. He uses his magic and knowledge to protect the baby Arthur and plan for his future."),
     KeyIdea("Describe characters and settings with details from the text, then explain what the details show.")],
    [Problem("Name two characters in Chapter 1.", "Possible: Arthur, Merlin, King Uther, Sir Ector (accept any characters from the chapter)."),
     Problem("Describe the setting of the legend.", "Britain long ago, in the time of knights, kings, and castles."),
     Problem("Which part of the chapter seems like a legend rather than real history? Why?", "Answers vary: Merlin's magic or prophecy; magic doesn't happen in real history.")],
    [S("Warm-Up", [SA("What is a setting?", "When and where a story takes place"), SA("Name a story you know that has a hero.", "Answers vary.")], cols=2),
     S("Read and Respond: Chapter 1", [
         OR("Who is the main character the legend is about? How do you know he will be important?", "Arthur. The chapter is about his birth, and the book is named after him; Merlin plans for his future.", lines=3),
         OR("Describe Merlin. Use one detail from the chapter.", "Merlin is a wise, powerful wizard. Detail: he takes the baby Arthur and plans his future.", lines=3,
            note="Accept any trait supported by a detail from the chapter."),
         OR("Describe the setting. Include when and where.", "Long ago in Britain, in a time of kings, knights, and castles.", lines=2),
         MC("A legend is…", ["a true report written by a reporter", "a story from long ago about a hero, with parts that are made up", "a poem that rhymes", "a set of directions"], 1)]),
     S("Think Deeper", [OR("Why do you think people kept telling stories about King Arthur for hundreds of years?", "Answers vary: they are exciting, they show bravery and loyalty, people like heroes.", lines=3)]),
     S("Exit Ticket", [OR("Write one sentence describing a character from Chapter 1. Include a detail from the text.", "Answers vary; must name a trait and a supporting detail.", lines=2)])],
    TE("Students describe characters and setting in a legend using text details.", "Refer to details and examples in a text; describe a character, setting, or event.",
       "King Arthur Reader (Chapter 1), workbook Lesson 1.1",
       eflow("Ask: What makes someone a hero?", ["Read Chapter 1 aloud together; students follow along.", "Pause after each page: Who is this? Where are we?"],
             ["Teach the words legend, character, setting.", "Say: Strong readers prove what they think with details.", "Model the Merlin example."],
             "Your Turn 1–3 together."),
       ["Describing a character with an opinion only (“he is cool”)."], ["Give a sentence frame: ___ is ___ because in the text ___."],
       ["Start a character chart for the whole book: name, traits, evidence."]),
    summary="Legends are old hero stories. Describe characters and settings with text details.")

L2 = Lesson("1.2", "Prefixes",
    "I can use prefixes to figure out the meaning of new words.", "L.4.4b, RF.4.3a",
    [("prefix", "A word part added to the beginning of a word that changes its meaning."), ("base word", "A word that can stand alone, to which prefixes and suffixes are added.")],
    "What do the words <i>unhappy</i>, <i>unlock</i>, and <i>unfair</i> have in common? What does <i>un-</i> do to each word?",
    [Text("A <b>prefix</b> is added to the beginning of a base word. If you know what the prefix means, you can often figure out the whole word."),
     Figure(lambda t: table(t, [["Prefix", "Meaning", "Example"], ["un-", "not; opposite of", "unhappy = not happy"], ["re-", "again; back", "rebuild = build again"],
                                ["dis-", "not; opposite of", "disappear = opposite of appear"], ["mis-", "wrongly; badly", "misjudge = judge wrongly"],
                                ["pre-", "before", "pretest = test before"], ["non-", "not", "nonstop = without stopping"]], [1.0 * inch, 1.8 * inch, 2.6 * inch], width=5.4 * inch)),
     Passage(P_KITE.title, P_KITE.paras, P_KITE.source, P_KITE.genre),
     Example("Use the prefix", "In paragraph 1, what does <i>misjudged</i> mean?",
             ["Find the base word: <i>judged</i>.", "Find the prefix: <i>mis-</i> means “wrongly.”", "Put them together and check the sentence: she judged the wind wrongly, so the string slipped."],
             "<i>Misjudged</i> means “judged wrongly.”"),
     WatchOut("Not every word that starts with these letters has a prefix. In <i>uncle</i> and <i>real</i>, <i>un</i> and <i>re</i> are not prefixes, because <i>-cle</i> and <i>-al</i> are not base words."),
     KeyIdea("Prefix meaning + base word meaning = new word meaning. Check that the meaning makes sense in the sentence.")],
    [Problem("What does <i>retie</i> mean in paragraph 2?", "tie again"), Problem("What does <i>disliked</i> mean in paragraph 3?", "did not like"),
     Problem("What does <i>pretest</i> mean in paragraph 4?", "test before")],
    [S("Warm-Up", [SA("Add <i>un-</i> to <i>kind</i>. Meaning?", "unkind: not kind"), SA("Add <i>re-</i> to <i>read</i>. Meaning?", "reread: read again")], cols=2),
     S("Prefix Practice", [SA(f"<i>{w}</i>", m) for w, m in [("unsafe", "not safe"), ("replay", "play again"), ("disagree", "not agree"), ("misspell", "spell wrongly"),
                                                            ("preview", "view before"), ("nonfiction", "not fiction (true writing)"), ("disconnect", "undo a connection"), ("refill", "fill again")]],
       intro="Write the meaning of each word.", cols=2),
     S("Use the Passage", [
         OR("Find two words with prefixes in “The Unlucky Kite.” Write each word and its meaning.", "Any two: unhappy (not happy), disappeared (opposite of appeared), misjudged (judged wrongly), rebuild (build again), reread (read again), retie (tie again), disliked (did not like), pretest (test before), unlucky (not lucky).", lines=3),
         MC("In paragraph 5, “Mia's frown <i>disappeared</i>” means her frown…", ["got bigger", "went away", "came back", "was misjudged"], 1)], passage=P_KITE),
     S("Think Deeper", [OR("Is <i>under</i> a word with the prefix <i>un-</i>? Explain how you know.", "No. If you remove “un,” “der” is not a base word.", lines=2)]),
     S("Exit Ticket", [OR("Write a sentence using a word with the prefix <i>re-</i> or <i>mis-</i>. Underline the word.", "Answers vary; word must use the prefix correctly.", lines=2)])],
    TE("Students use prefixes to determine word meaning.", "Use common, grade-appropriate Greek and Latin affixes as clues to the meaning of a word.", "Workbook Lesson 1.2; index cards (optional)",
       eflow("Ask: What do unhappy, unlock, unfair share?", "Read “The Unlucky Kite” aloud; students raise a hand at each prefix word.", ["Teach the prefix table.", "Model “misjudged.”", "Teach the Watch Out (uncle, real)."],
             "Your Turn 1–3; prove each meaning in the sentence."),
       ["Treating any word starting with un/re as having a prefix."], ["Cover the prefix with a finger; is a real word left?"], ["Make prefix flashcards; play a matching game."]),
    summary="Prefixes come at the beginning of words: un-, dis-, non- (not), re- (again), mis- (wrongly), pre- (before).")

L3 = Lesson("1.3", "Suffixes",
    "I can use suffixes to figure out the meaning and part of speech of new words.", "L.4.4b",
    [("suffix", "A word part added to the end of a word that changes its meaning or how it is used.")],
    "How are <i>help</i>, <i>helpful</i>, <i>helpless</i>, and <i>helper</i> different?",
    [Text("A <b>suffix</b> is added to the end of a base word. Suffixes change the meaning and often change the part of speech (for example, from a verb to an adjective)."),
     Figure(lambda t: table(t, [["Suffix", "Meaning", "Example"], ["-ful", "full of", "careful = full of care"], ["-less", "without", "hopeless = without hope"],
                                ["-ly", "in a certain way", "slowly = in a slow way"], ["-ness", "state of being", "darkness = state of being dark"],
                                ["-able", "able to be", "breakable = able to be broken"], ["-er, -or", "a person who", "gardener = a person who gardens"]], [1.0 * inch, 1.8 * inch, 2.6 * inch], width=5.4 * inch)),
     Passage(P_GARDEN.title, P_GARDEN.paras, P_GARDEN.source, P_GARDEN.genre),
     Example("Use the suffix", "What does <i>pointless</i> mean in paragraph 2?",
             ["Base word: <i>point</i> (a purpose).", "Suffix: <i>-less</i> means “without.”", "Check: the neighbors thought his work had no purpose."], "<i>Pointless</i> means “without a point or purpose.”"),
     WatchOut("Sometimes the base word changes spelling: <i>happy</i> + <i>-ness</i> = <i>happiness</i> (y changes to i)."),
     KeyIdea("Base word + suffix meaning = new word meaning. Suffixes like -ful and -less are opposites.")],
    [Problem("What does <i>carefully</i> mean?", "in a way full of care"), Problem("What does <i>fearless</i> mean?", "without fear"), Problem("What is a <i>gardener</i>?", "a person who gardens")],
    [S("Warm-Up", [SA("Add <i>-ful</i> to <i>joy</i>. Meaning?", "joyful: full of joy"), SA("Add <i>-less</i> to <i>joy</i>. Meaning?", "joyless: without joy")], cols=2),
     S("Suffix Practice", [SA(f"<i>{w}</i>", m) for w, m in [("powerful", "full of power"), ("spotless", "without spots"), ("quietly", "in a quiet way"), ("kindness", "state of being kind"),
                                                            ("washable", "able to be washed"), ("teacher", "a person who teaches"), ("sailor", "a person who sails"), ("thankful", "full of thanks")]],
       intro="Write the meaning of each word.", cols=2),
     S("Use the Passage", [
         MC("In paragraph 1, <i>hopeless</i> means…", ["full of hope", "without hope", "hoping again", "a person who hopes"], 1),
         OR("Mr. Hollis said, “Nothing is hopeless.” What did he mean? Use a detail from the story.", "Even something that looks impossible can get better with work. Detail: the trash-filled lot became a garden of sunflowers and beans.", lines=3)], passage=P_GARDEN),
     S("Think Deeper", [OR("Write a sentence that uses both <i>careful</i> and <i>careless</i> to show the difference.", "Answers vary, e.g. A careful painter stays in the lines, but a careless one drips paint everywhere.", lines=2)]),
     S("Exit Ticket", [SA("Add a suffix to <i>loud</i> to tell how something was done.", "loudly"), SA("Add a suffix to <i>fear</i> to mean “without fear.”", "fearless")], cols=2)],
    TE("Students use suffixes to determine meaning.", "Use common affixes as clues to the meaning of a word.", "Workbook Lesson 1.3",
       eflow("Ask: How are help, helpful, helpless, helper different?", "Read the garden story; list suffix words on the board.", ["Teach the suffix table.", "Model “pointless.”", "Spelling changes (happy → happiness)."],
             "Your Turn 1–3."),
       ["Confusing -ful and -less."], ["Sort -ful and -less words into two columns."], ["Find suffix words in the reader."]),
    summary="Suffixes come at the end: -ful (full of), -less (without), -ly (how), -ness (state of), -able (can be), -er/-or (person who).")

L4 = Lesson("1.4", "Greek and Latin Roots",
    "I can use Greek and Latin roots to figure out the meaning of words.", "L.4.4b",
    [("root", "The main part of a word that carries its meaning; many English roots come from Greek or Latin.")],
    "The word <i>telephone</i> has two parts: <i>tele</i> and <i>phone</i>. What do you think each part means?",
    [Figure(lambda t: table(t, [["Root", "Origin", "Meaning", "Examples"], ["tele", "Greek", "far", "telephone, telescope"], ["phon", "Greek", "sound", "telephone, phonics"],
                                ["graph", "Greek", "write, draw", "autograph, paragraph"], ["port", "Latin", "carry", "transport, portable"], ["aud", "Latin", "hear", "audience, audio"],
                                ["vis / vid", "Latin", "see", "visible, video"]], [0.9 * inch, 0.8 * inch, 1.2 * inch, 2.4 * inch], width=5.3 * inch)),
     Passage(P_MESSAGES.title, P_MESSAGES.paras, P_MESSAGES.source, P_MESSAGES.genre),
     Example("Put roots together", "What does <i>telegraph</i> mean?", ["<i>tele</i> = far.", "<i>graph</i> = write.", "The telegraph sent written messages over long distances."], "a machine that sends writing far away"),
     KeyIdea("Roots carry the main meaning. Combine the root with prefixes and suffixes, then check the sentence.")],
    [Problem("<i>Portable</i> means…", "able to be carried"), Problem("An <i>audience</i> is…", "people who hear (or watch) something"), Problem("<i>Visible</i> means…", "able to be seen")],
    [S("Warm-Up", [SA("Which root means “hear”?", "aud"), SA("Which root means “carry”?", "port")], cols=2),
     S("Root Practice", [SA(f"<i>{w}</i>", m) for w, m in [("telescope", "a tool to see far"), ("autograph", "a person's own written name"), ("transport", "carry across / from place to place"),
                                                          ("audio", "sound you hear"), ("vision", "the ability to see"), ("export", "carry goods out of a country")]], intro="Use the roots to write each meaning.", cols=2),
     S("Use the Passage", [
         MC("In paragraph 1, a <i>visible</i> signal is one that can be…", ["heard", "carried", "seen", "written"], 2),
         OR("Explain how the telephone was different from the telegraph. Use the word roots to help.", "Telegraph (far + write) sent written dots and dashes; telephone (far + sound) let people hear voices.", lines=3)], passage=P_MESSAGES),
     S("Think Deeper", [OR("Invent a new word using two roots from the chart. Tell what it would mean.", "Answers vary, e.g. “audiograph”: a machine that writes down what it hears.", lines=2)]),
     S("Writing Connection", [OR("Write 3–4 sentences about how you like to send messages to family or friends. Use at least two words with roots, prefixes, or suffixes from this week. Underline them.",
                                 "Answers vary; look for correct use of at least two affix/root words.", lines=5, note="Check that each underlined word fits its meaning.")])],
    TE("Students use Greek and Latin roots to determine meaning.", "Use Greek and Latin affixes and roots as clues to meaning.", "Workbook Lesson 1.4",
       eflow("Ask: What might tele and phone mean?", "Read “Messages Across the Miles.”", ["Teach the roots table.", "Model telegraph."], "Your Turn 1–3. Weekly Check tomorrow."),
       ["Guessing from the first letters only."], ["Draw a word-part sum: tele + graph = far + write."], ["Find root words in a science book."]),
    summary="Roots carry meaning: tele (far), phon (sound), graph (write), port (carry), aud (hear), vis (see).")

# ================================================================= Week 2 · Use context clues (Chapter 2)
L5 = Lesson("1.5", "Context Clues: Definitions and Restatements",
    "I can use definition and restatement clues to figure out new words.", "L.4.4a",
    [("context", "The words and sentences around a word."), ("context clue", "A hint in the text that helps you figure out a word's meaning.")],
    "Read this: “The knight wore a <i>gauntlet</i>, an armored glove, on each hand.” What is a gauntlet? How did you know?",
    [ReaderAssign(READER, "Chapter 2: The Sword in the Stone", "Watch for unfamiliar words. Which ones can you figure out from the sentences around them?"),
     Text("Authors often help you with hard words. A <b>definition clue</b> tells the meaning right in the sentence, often after a comma or the words <i>is</i>, <i>means</i>, or <i>which is</i>. A <b>restatement clue</b> says the same thing in easier words, often after <i>or</i>, a dash, or parentheses."),
     Passage(P_SMITH.title, P_SMITH.paras, P_SMITH.source, P_SMITH.genre),
     Example("Definition clue", "What is a <i>forge</i>? (paragraph 2)", ["Look right after the word.", "The comma introduces “a fireplace where metal is heated until it glows.”"], "A forge is a fireplace where metal is heated until it glows."),
     KeyIdea("Look for commas, dashes, parentheses, and the words <i>is</i>, <i>means</i>, and <i>or</i>. They often signal a definition or restatement.")],
    [Problem("What is an <i>apprentice</i>?", "a young worker who learns a trade by helping a master"), Problem("What do <i>bellows</i> do?", "push air into the fire to make it hotter"),
     Problem("What clue word or punctuation helped you with <i>apprentice</i>?", "the comma after the word introduces the definition")],
    [S("Warm-Up", [SA("What is context?", "the words around a word"), SA("Name one signal for a definition clue.", "a comma, dash, parentheses, is, means, or")], cols=2),
     S("Find the Clue", [
         OR("The castle had a <i>portcullis</i>, a heavy iron gate that slid down to block the entrance. What is a portcullis?", "a heavy iron gate that slides down to block the entrance", lines=1),
         OR("The squire polished the <i>hauberk</i> (a shirt made of small metal rings) until it shone. What is a hauberk?", "a shirt of small metal rings (chain mail)", lines=1),
         OR("The jester, or clown, made the king laugh. What is a jester?", "a clown", lines=1),
         OR("They stored grain in the <i>granary</i> — the building where grain is kept. What is a granary?", "a building where grain is stored", lines=1)]),
     S("Use the Passage", [
         MC("In paragraph 3, what is an <i>anvil</i>?", ["a hammer", "a heavy block where metal is pounded", "a bucket of water", "a horse"], 1,
            note="This is an inference from how Rowan uses it; the definition is not stated directly."),
         OR("How did Tom feel at the end of the first week? Use a detail.", "Tired but proud; his arms ached, but he felt as proud as a king when the knight's horse wore his shoes.", lines=3)], passage=P_SMITH),
     S("Chapter 2 Connection", [OR("Find one word in Chapter 2 that you didn't know. Write the sentence, the clue, and what you think the word means.", "Answers vary.", lines=4)]),
     S("Exit Ticket", [OR("Write a sentence that defines the word <i>moat</i> using a definition clue.", "e.g. The castle was surrounded by a moat, a deep ditch filled with water.", lines=2)])],
    TE("Students use definition and restatement clues.", "Use context as a clue to the meaning of a word or phrase.", "King Arthur Reader (Chapter 2), workbook Lesson 1.5",
       eflow("Read the gauntlet sentence; ask how they knew.", ["Read Chapter 2 together.", "Then read “The Blacksmith's Apprentice.”"], ["Teach definition and restatement signals.", "Model “forge.”"], "Your Turn 1–3."),
       ["Skipping hard words instead of looking for clues."], ["Circle signal punctuation."], ["Write a short story with three definition clues for a sibling."]),
    summary="Definition and restatement clues explain the word right in the sentence. Watch for commas, dashes, parentheses, is, means, or.")

L6 = Lesson("1.6", "Context Clues: Synonyms and Antonyms",
    "I can use synonym and antonym clues to figure out new words.", "L.4.4a, L.4.5c",
    [("synonym", "A word that means the same or almost the same as another word."), ("antonym", "A word that means the opposite of another word.")],
    "“Gareth was boisterous, but his brother was quiet.” What does <i>boisterous</i> probably mean?",
    [Text("A <b>synonym clue</b> uses a word with a similar meaning nearby. An <b>antonym clue</b> uses a word with the opposite meaning. Antonym clues are often signaled by <i>but</i>, <i>unlike</i>, <i>however</i>, <i>on the other hand</i>, or <i>instead</i>."),
     Passage(P_KNIGHTS.title, P_KNIGHTS.paras, P_KNIGHTS.source, P_KNIGHTS.genre),
     Example("Antonym clue", "What does <i>impulsive</i> mean? (paragraph 2)", ["Gareth jumps into adventures without thinking.", "Gaheris is the opposite: cautious, studying every map.", "So impulsive means acting quickly without thinking."],
             "<i>Impulsive</i> means acting without thinking first."),
     KeyIdea("Synonym clues show the same meaning nearby. Antonym clues show the opposite, often after <i>but</i>, <i>unlike</i>, or <i>on the other hand</i>.")],
    [Problem("What does <i>boisterous</i> mean?", "loud and lively"), Problem("Which word is an antonym clue for <i>impulsive</i>?", "cautious"), Problem("What does <i>gallant</i> mean?", "brave and polite")],
    [S("Warm-Up", [SA("A synonym for <i>happy</i>", "glad, joyful"), SA("An antonym for <i>happy</i>", "sad")], cols=2),
     S("Synonym or Antonym Clue?", [
         OR("The puppy was <i>timid</i>, but the older dog was bold. What does timid mean? What type of clue?", "shy or fearful; antonym clue (bold)", lines=1),
         OR("The path was <i>treacherous</i>; it was dangerous and slippery. What does treacherous mean? What type of clue?", "dangerous; synonym clue (dangerous)", lines=1),
         OR("Unlike his <i>tidy</i> sister, Max kept a messy room. What does tidy mean? What type of clue?", "neat; antonym clue (messy)", lines=1),
         OR("The feast was <i>lavish</i>. It was rich and grand, with forty dishes. What does lavish mean?", "rich, grand, plentiful; synonym clue", lines=1)]),
     S("Use the Passage", [
         MC("Which words in paragraph 1 signal an antonym clue for <i>boisterous</i>?", ["as different as night and day", "on the other hand", "told jokes", "the great hall"], 1),
         OR("Which brother would you rather go on a quest with? Use two details from the passage.", "Answers vary; must use two details about the chosen brother.", lines=3)], passage=P_KNIGHTS),
     S("Think Deeper", [OR("Write a sentence that uses an antonym clue to explain the word <i>ancient</i>.", "e.g. Unlike the new church, the castle was ancient, built hundreds of years ago.", lines=2)]),
     S("Exit Ticket", [SA("Synonym for <i>gallant</i>", "brave, noble"), SA("Antonym for <i>cautious</i>", "careless, reckless, impulsive")], cols=2)],
    TE("Students use synonym and antonym clues.", "Use context as a clue to meaning; relate words to synonyms and antonyms.", "Workbook Lesson 1.6",
       eflow("Read the boisterous sentence.", "Read “Two Brothers, Two Knights.”", ["Teach signal words for antonym clues.", "Model “impulsive.”"], "Your Turn 1–3."),
       ["Using the clue word itself as the definition when it is an antonym."], ["Ask: same or opposite?"], ["Keep a synonym/antonym word wall."]),
    summary="Synonym clues show the same meaning; antonym clues (but, unlike, on the other hand) show the opposite.")

L7 = Lesson("1.7", "Context Clues: Examples and Inference",
    "I can use example clues and the whole passage to infer word meanings.", "L.4.4a",
    [("infer", "Figure out something the author does not say directly, using clues and what you know.")],
    "“The cook chopped root vegetables such as onions, turnips, and carrots.” What are root vegetables?",
    [Text("An <b>example clue</b> gives examples of the word, often after <i>such as</i>, <i>for example</i>, <i>like</i>, or <i>including</i>. Sometimes there is no single clue, and you must <b>infer</b> from the whole sentence or paragraph."),
     Passage(P_KITCHEN.title, P_KITCHEN.paras, P_KITCHEN.source, P_KITCHEN.genre),
     Example("Infer from the paragraph", "What does <i>stern</i> mean? (paragraph 2)", ["The cook never smiled.", "Her voice was sharp; everyone froze.", "Those clues describe someone strict and serious."], "<i>Stern</i> means strict and serious."),
     KeyIdea("Look for examples after <i>such as</i>, <i>like</i>, or <i>including</i>. If there's no clear clue, use all the details to infer.")],
    [Problem("What are root vegetables? What clue helped?", "vegetables that grow underground, like onions and turnips; example clue"), Problem("What is a <i>feast</i>?", "a big, special meal"),
     Problem("Which details helped you infer the meaning of <i>feast</i>?", "tables covered with platters of bread, stews, pies; lasted until candles burned low; guests full")],
    [S("Warm-Up", [SA("Signal words for example clues", "such as, for example, like, including"), SA("What does infer mean?", "figure out from clues")], cols=2),
     S("Use the Clues", [
         OR("Knights carried many <i>weapons</i>, such as swords, lances, and maces. What are weapons?", "tools for fighting", lines=1),
         OR("The peddler sold <i>wares</i> including pots, ribbons, and spoons. What are wares?", "things for sale; goods", lines=1),
         OR("After walking all day in the hot sun without water, the travelers were <i>parched</i>. What does parched mean?", "very thirsty, dry", lines=1),
         OR("The <i>jubilant</i> crowd cheered, sang, and danced in the streets after the victory. What does jubilant mean?", "very happy; celebrating", lines=1)]),
     S("Chapter 2 Connection", [
         OR("In Chapter 2, how did people react when Arthur pulled the sword from the stone? What does that show?", "Many were surprised or doubtful because he was a young boy; it shows he was chosen to be king even though people did not expect it.", lines=4,
            note="Accept answers supported by the chapter.")]),
     S("Exit Ticket", [OR("Write a sentence with an example clue for the word <i>instruments</i>.", "e.g. The band played instruments such as drums, flutes, and horns.", lines=2)])],
    TE("Students use example and inference clues.", "Use context as a clue to meaning.", "King Arthur Reader (Chapter 2), workbook Lesson 1.7",
       eflow("Read the root-vegetable sentence.", ["Reread the sword-pulling part of Chapter 2.", "Read “The Castle Kitchen.”"], ["Teach example signals.", "Model inferring “stern.”"], "Your Turn 1–3."),
       ["Picking one example as the whole meaning (“root vegetables means onions”)."], ["Ask: What do all the examples have in common?"], ["Find inference clues in Chapter 2."]),
    summary="Example clues follow such as, like, including. Without a clear clue, infer from all the details.")

L8 = Lesson("1.8", "Multiple-Meaning Words and the Dictionary",
    "I can use context to choose the right meaning of a multiple-meaning word and check it in a dictionary.", "L.4.4a, L.4.4c",
    [("multiple-meaning word", "A word with more than one meaning, like <i>bat</i> or <i>spring</i>."), ("dictionary entry", "A word in a dictionary with its pronunciation, part of speech, and meanings."),
     ("guide words", "The two words at the top of a dictionary page that show the first and last entries on the page.")],
    "What does <i>bat</i> mean in “The bat flew out of the cave”? In “Leo swung the bat”?",
    [Text("Many English words have more than one meaning. Use context to decide which meaning fits, then check in a dictionary or glossary."),
     Passage(P_FAIR.title, P_FAIR.paras, P_FAIR.source, P_FAIR.genre),
     Figure(lambda t: table(t, [["step  (verb)", "1. to move by lifting your foot and putting it down", "2. —"], ["step  (noun)", "1. one movement of the foot", "2. a stair"], ["line  (noun)", "1. a long thin mark", "2. a row of people waiting"]],
                            [1.2 * inch, 2.8 * inch, 1.6 * inch], width=5.6 * inch, header=False)),
     Example("Choose the meaning", "“The <i>line</i> was long.” (paragraph 2)", ["Possible meanings: a long thin mark, or a row of people waiting.", "Context: Nia wanted to ride but had to wait."], "a row of people waiting"),
     KeyIdea("Try each meaning in the sentence. The one that makes sense is the right one. Use guide words to find entries quickly.")],
    [Problem("In paragraph 1, which meaning of <i>step</i> is used?", "where you put your feet (a movement of the foot)"), Problem("What does <i>play</i> mean in paragraph 2?", "make music"),
     Problem("Would <i>fair</i> come between the guide words <i>face</i> and <i>fall</i>?", "Yes")],
    [S("Warm-Up", [SA("Two meanings of <i>bark</i>", "a dog's sound; the outside of a tree"), SA("Two meanings of <i>ring</i>", "jewelry for a finger; a sound a bell makes")], cols=2),
     S("Which Meaning?", [
         MC("“The queen wore a crown on her <i>head</i>.” <i>Head</i> means…", ["the top part of the body", "the leader of a group", "to go toward"], 0),
         MC("“The team will <i>head</i> home after the game.” <i>Head</i> means…", ["the top part of the body", "the leader of a group", "to go toward"], 2),
         MC("“Leo won a <i>fair</i> game of ring toss.” <i>Fair</i> means…", ["a festival with rides", "honest, following the rules", "light in color"], 1),
         MC("“The knight's <i>mail</i> clanked as he walked.” <i>Mail</i> means…", ["letters and packages", "armor made of metal rings", "to send"], 1, note="Connects to Lesson 1.5 (hauberk).")]),
     S("Guide Words", [SA(f"Guide words <i>{a}</i> – <i>{b}</i>. Is <i>{w}</i> on the page?", ans) for a, b, w, ans in
                       [("kettle", "knot", "knight", "Yes"), ("sail", "salt", "sword", "No"), ("castle", "cave", "cat", "Yes"), ("lance", "large", "lake", "No")]], cols=2),
     S("Exit Ticket", [OR("Write two sentences that use <i>spring</i> with two different meanings.", "e.g. Flowers bloom in spring. The cat will spring onto the table.", lines=2)])],
    TE("Students choose meanings of multiple-meaning words and use a dictionary.", "Consult reference materials to find the pronunciation and determine or clarify meaning.", "Print or online dictionary, workbook Lesson 1.8",
       eflow("Bat sentences.", "Read “A Day at the Fair.”", ["Model choosing the meaning of “line.”", "Show a real dictionary entry and guide words."], "Your Turn 1–3. Weekly Check tomorrow."),
       ["Choosing the most common meaning without checking context."], ["Try each meaning in the sentence."], ["Find five multiple-meaning words in Chapter 2."]),
    summary="Use context to pick the right meaning; check it in a dictionary using guide words.")

# ================================================================= Week 3 · Practice grade-level vocabulary (Chapter 3)
L9 = Lesson("1.9", "Similes and Metaphors",
    "I can explain the meaning of similes and metaphors in a text.", "L.4.5a, RL.4.4",
    [("figurative language", "Words used in an unusual way to create a picture or feeling, not to be taken literally."), ("simile", "A comparison of two unlike things using <i>like</i> or <i>as</i>."),
     ("metaphor", "A comparison of two unlike things that says one thing <i>is</i> another, without <i>like</i> or <i>as</i>.")],
    "What does it mean if someone says, “My little brother is a tornado”?",
    [ReaderAssign(READER, "Chapter 3: The Sword in the Lake", "Notice descriptive language. How does the author help you picture the lake and the magic sword?"),
     Text("Writers use <b>similes</b> and <b>metaphors</b> to help readers picture things. To understand one, ask: <i>What two things are compared? How are they alike?</i>"),
     Passage(P_STORM.title, P_STORM.paras, P_STORM.source, P_STORM.genre),
     Example("Explain a simile", "“Wind howled like a hungry wolf.”", ["Compared: wind and a hungry wolf.", "Alike: both make a loud, wild, scary howling sound."], "The wind was loud, wild, and frightening."),
     Example("Explain a metaphor", "“His horse was a statue.”", ["Compared: the horse and a statue.", "Alike: a statue does not move."], "The horse stood completely still and would not move."),
     KeyIdea("Simile: <i>like</i> or <i>as</i>. Metaphor: says one thing <i>is</i> another. Explain what the two things have in common.")],
    [Problem("Simile or metaphor: “The cottage was a lighthouse in a sea of storm.”", "metaphor"), Problem("What does that comparison mean?", "The cottage's light guided him and gave him safety and hope in the storm."),
     Problem("Find one more simile in the passage.", "dark as an iron pot; like a hundred tiny needles; cold as a stone")],
    [S("Warm-Up", [SA("Which word signals a simile?", "like or as"), SA("Does a metaphor use <i>like</i>?", "No")], cols=2),
     S("Simile or Metaphor? What does it mean?", [
         OR(f"“{q}”", a, lines=1) for q, a in [("The classroom was a zoo.", "metaphor: the classroom was noisy and wild"), ("Her smile was as bright as the sun.", "simile: her smile was cheerful and happy"),
                                               ("The snow was a white blanket on the field.", "metaphor: the snow covered everything smoothly"), ("He ran like the wind.", "simile: he ran very fast")]]),
     S("Use the Passage", [
         OR("Explain the simile “rain … stinging his face like a hundred tiny needles.”", "The rain hit hard and hurt, like many sharp needles poking his skin.", lines=2),
         OR("How do Bedivere's feelings change at the end? Which comparison shows it?", "From cold and miserable to hopeful; “heart, cold as a stone… warmed with hope.”", lines=3)], passage=P_STORM),
     S("Exit Ticket", [OR("Write one simile and one metaphor about a knight's sword.", "Answers vary; simile uses like/as; metaphor says the sword is something.", lines=2)])],
    TE("Students explain similes and metaphors.", "Explain the meaning of simple similes and metaphors in context.", "King Arthur Reader (Chapter 3), workbook Lesson 1.9",
       eflow("Tornado brother.", ["Read Chapter 3.", "Read “Storm over the Moor.”"], ["Teach simile vs metaphor.", "Model the wolf simile and statue metaphor."], "Your Turn 1–3."),
       ["Calling every comparison with “is” a metaphor (e.g. “The dog is brown”)."], ["Ask: Are two unlike things compared?"], ["Find figurative language in Chapter 3."]),
    summary="Similes compare with like or as; metaphors say one thing is another. Explain how the things are alike.")

L10 = Lesson("1.10", "Idioms, Adages, and Proverbs",
    "I can explain the meaning of common idioms, adages, and proverbs.", "L.4.5b",
    [("idiom", "A phrase whose meaning is different from the meanings of its words, like “break a leg.”"), ("adage / proverb", "A short, well-known saying that gives advice or states a truth.")],
    "If your coach says, “Keep your eye on the ball,” does she mean to put your eye on it?",
    [Text("An <b>idiom</b> can't be understood word by word. <i>It's raining cats and dogs</i> means it is raining very hard. An <b>adage</b> or <b>proverb</b> is a wise saying, like <i>Look before you leap</i>."),
     Passage(P_GRANDPA.title, P_GRANDPA.paras, P_GRANDPA.source, P_GRANDPA.genre),
     Example("Explain a proverb", "“Rome wasn't built in a day.”", ["Literal: a huge city took a long time to build.", "Situation: the narrator wants to quit after losing.", "Lesson: great things take time and effort."], "Big goals take time; keep working."),
     KeyIdea("Use context to figure out the real meaning. Ask: What is the speaker trying to tell someone?")],
    [Problem("What does “break a leg” mean?", "good luck"), Problem("What does “Many hands make light work” mean?", "When many people help, work is easier."), Problem("What does “Hang in there” mean?", "Don't give up.")],
    [S("Warm-Up", [SA("Is “break a leg” literal?", "No"), SA("Name an idiom you know.", "Answers vary.")], cols=2),
     S("Match the Meaning", [MC(f"“{q}” means…", ch, k) for q, ch, k in [
         ("A piece of cake", ["a dessert", "something very easy", "a small amount"], 1), ("Look before you leap", ["think before you act", "jump high", "watch where you walk"], 0),
         ("Under the weather", ["outside in rain", "feeling sick", "below the clouds"], 1), ("The early bird catches the worm", ["birds eat worms", "people who start early succeed", "wake up birds"], 1)]]),
     S("Use the Passage", [OR("Which saying from Grandpa would you use to encourage a friend who is struggling with math? Explain why.", "“Rome wasn't built in a day” or “Hang in there”: learning takes time; don't give up.", lines=3)], passage=P_GRANDPA),
     S("Exit Ticket", [OR("Draw or describe the literal picture of “raining cats and dogs.” Then write what it really means.", "Literal: animals falling from the sky. Real: raining very hard.", lines=3)])],
    TE("Students explain idioms, adages, and proverbs.", "Recognize and explain the meaning of common idioms, adages, and proverbs.", "Workbook Lesson 1.10",
       eflow("Eye on the ball.", "Read “Grandpa's Sayings.”", ["Literal vs real meaning.", "Model “Rome wasn't built in a day.”"], "Your Turn 1–3."),
       ["Interpreting idioms literally."], ["Draw literal vs real meanings side by side."], ["Collect sayings from grandparents or older relatives."]),
    summary="Idioms and proverbs mean something different from their words. Use context to find the real meaning.")

L11 = Lesson("1.11", "Shades of Meaning",
    "I can choose among words with similar meanings to say exactly what I mean.", "L.4.5c, L.4.3a",
    [("shades of meaning", "Small differences between words that mean almost the same thing."), ("thesaurus", "A reference book that lists synonyms and antonyms.")],
    "Is there a difference between saying a knight <i>walked</i>, <i>marched</i>, or <i>tiptoed</i> into the hall?",
    [Text("Synonyms are not all exactly the same. <i>Cold</i>, <i>chilly</i>, and <i>freezing</i> all describe low temperature, but <i>freezing</i> is much stronger. Choosing the right shade of meaning makes writing precise."),
     Figure(lambda t: table(t, [["weaker", "", "", "stronger"], ["warm", "hot", "boiling", "scorching"], ["glad", "happy", "joyful", "ecstatic"], ["whisper", "say", "shout", "roar"], ["walk", "hurry", "run", "sprint"]],
                            [1.3 * inch] * 4, width=5.2 * inch)),
     Example("Choose the best word", "The baby was asleep, so the knight ___ past the cradle. (walked, stomped, tiptoed)", ["Stomped is loud: wrong.", "Walked is okay but plain.", "Tiptoed shows moving quietly so the baby won't wake."], "tiptoed"),
     KeyIdea("Use a thesaurus to find synonyms, then pick the one whose exact meaning fits the sentence.")],
    [Problem("Order from weakest to strongest: furious, annoyed, angry", "annoyed, angry, furious"), Problem("Best word: The lion ___ (said, roared) loudly.", "roared"),
     Problem("A stronger word for <i>big</i>", "huge, enormous, gigantic")],
    [S("Warm-Up", [SA("Synonym for <i>small</i>", "little, tiny"), SA("Antonym for <i>small</i>", "big, large")], cols=2),
     S("Order the Words", [SA(f"{w}", a) for w, a in [("hot, warm, scorching", "warm, hot, scorching"), ("giggle, chuckle, howl (laughs)", "giggle, chuckle, howl"),
                                                      ("drizzle, downpour, shower", "drizzle, shower, downpour"), ("tired, exhausted, sleepy", "sleepy, tired, exhausted")]], intro="Write from weakest to strongest.", cols=2),
     S("Choose the Best Word", [MC(q, ch, k) for q, ch, k in [
         ("Sir Kay ___ into the hall, angry that he had lost the joust.", ["stomped", "strolled", "tiptoed"], 0),
         ("The tiny kitten ___ softly from the box.", ["roared", "mewed", "shouted"], 1),
         ("After the long journey, the travelers were ___.", ["exhausted", "awake", "sleepy"], 0)]]),
     S("Exit Ticket", [OR("Rewrite this sentence with more precise words: “The good knight went to the big castle.”", "e.g. The noble knight galloped to the enormous castle.", lines=2)])],
    TE("Students distinguish shades of meaning.", "Demonstrate understanding of words by relating them to synonyms; choose words for effect.", "Thesaurus, workbook Lesson 1.11",
       eflow("Walked vs marched vs tiptoed.", "Act out the verbs.", ["Teach the word ladder.", "Model the tiptoed example."], "Your Turn 1–3."),
       ["Treating all synonyms as equal."], ["Act out or draw the words."], ["Make paint-chip word ladders."]),
    summary="Synonyms differ in strength and feeling. Choose the most precise word.")

L12 = Lesson("1.12", "Academic and Content Words",
    "I can learn and use words about a topic (content words) and words used in school (academic words).", "L.4.6",
    [("academic word", "A word used in many school subjects, like <i>compare</i>, <i>describe</i>, or <i>explain</i>."), ("content word", "A word that belongs to one topic, like <i>moat</i> for castles."),
     ("glossary", "A list of important words and their meanings at the back of a book.")],
    "What does a question mean when it asks you to <i>compare</i>? To <i>explain</i>?",
    [Text("Some words appear in every subject: <b>academic words</b> such as <i>compare</i> (tell how things are alike and different), <i>describe</i> (tell details about), and <i>explain</i> (tell how or why). Other words belong to a topic: <b>content words</b> such as <i>moat</i> or <i>keep</i> for castles."),
     Passage(P_CASTLES.title, P_CASTLES.paras, P_CASTLES.source, P_CASTLES.genre),
     Example("Use a content word", "Explain how a drawbridge kept people safe.", ["Find the definition: a bridge that could be raised to block the gate.", "Explain how: when raised, enemies could not cross the moat."], "When the drawbridge was raised, enemies couldn't cross the moat to reach the gate."),
     KeyIdea("Learn what academic question words ask you to do. Use content words correctly when you write about a topic.")],
    [Problem("What does <i>compare</i> ask you to do?", "tell how things are alike and different"), Problem("What was the keep?", "the strongest tower, where the lord's family lived"), Problem("What were battlements for?", "protecting archers while they shot")],
    [S("Warm-Up", [SA("What does <i>describe</i> ask?", "tell details about something"), SA("What does <i>explain</i> ask?", "tell how or why")], cols=2),
     S("Content Words", [SA(w, a) for w, a in [("moat", "a deep ditch, often filled with water, around a castle"), ("drawbridge", "a bridge that can be raised"), ("battlements", "wall tops with gaps for archers"), ("keep", "the strongest tower of a castle")]], cols=2),
     S("Use the Passage", [
         OR("Compare a moat and a drawbridge. How were they alike? How were they different?", "Alike: both kept enemies out. Different: a moat was a ditch of water; a drawbridge was a bridge that could be raised.", lines=3),
         OR("Explain why everyone retreated to the keep if enemies broke through.", "It was the strongest, safest part of the castle.", lines=2)], passage=P_CASTLES),
     S("Chapter 3 Connection", [OR("Describe the Lady of the Lake and what she gave Arthur. Use one content word from the chapter.", "She is a magical lady who gives Arthur the sword Excalibur (and its scabbard).", lines=3,
                                   note="Accept accurate details from Chapter 3.")])],
    TE("Students use academic and content words.", "Acquire and use general academic and domain-specific words.", "Workbook Lesson 1.12",
       eflow("Compare vs explain.", "Read “How a Castle Kept People Safe.”", ["Academic question words.", "Content word glossary."], "Your Turn 1–3. Weekly Check tomorrow."),
       ["Answering a “compare” question with only one side."], ["Use a two-column alike/different chart."], ["Make an illustrated castle glossary."]),
    summary="Academic words tell you what to do; content words name things in a topic.")

# ================================================================= Week 4 · Apply vocabulary in writing (Chapter 4)
L13 = Lesson("1.13", "Strong Verbs and Vivid Adjectives",
    "I can choose strong verbs and vivid adjectives to make my writing come alive.", "L.4.3a, W.4.3d",
    [("verb", "A word that shows action or being."), ("adjective", "A word that describes a noun."), ("vivid", "Bright and clear, so the reader can picture it.")],
    "Which sentence do you picture better: “The knight went down the hill” or “The knight thundered down the rocky hill”?",
    [ReaderAssign(READER, "Chapter 4: Sir Balin and the Hallows", "Collect three strong verbs or vivid adjectives the author uses."),
     Text("Plain words like <i>went</i>, <i>said</i>, <i>good</i>, and <i>nice</i> don't give readers much to picture. <b>Strong verbs</b> show exactly how an action happens. <b>Vivid adjectives</b> add sensory detail."),
     Example("Revise a sentence", "The dog went across the yard.", ["Replace <i>went</i> with a verb that shows how: dashed.", "Add an adjective: muddy."], "The dog dashed across the muddy yard."),
     KeyIdea("Replace tired words with precise verbs and adjectives that help the reader see, hear, and feel.")],
    [Problem("Stronger verb for <i>said</i> (loudly)", "shouted, bellowed"), Problem("Stronger verb for <i>ate</i> (quickly)", "gobbled, devoured"), Problem("Vivid adjective for a sword", "gleaming, sharp, heavy")],
    [S("Warm-Up", [SA("Is <i>gleaming</i> a verb or adjective here: “a gleaming sword”?", "adjective"), SA("Verb in “Arthur drew the sword.”", "drew")], cols=2),
     S("Revise", [OR(f"“{q}”", a, lines=2) for q, a in [("The horse went fast.", "e.g. The black stallion galloped across the field."), ("The castle was big.", "e.g. The towering stone castle loomed over the village."),
                                                         ("The girl said she was happy.", "e.g. The girl laughed, “I'm thrilled!”"), ("The fire was nice.", "e.g. The crackling fire warmed the chilly hall.")]], intro="Rewrite each sentence with a strong verb and a vivid adjective."),
     S("Chapter 4 Connection", [OR("Copy two strong verbs or vivid adjectives from Chapter 4. Explain what each helps you picture.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Write one sentence about a knight using a strong verb and a vivid adjective. Underline them.", "Answers vary.", lines=2)])],
    TE("Students choose strong verbs and vivid adjectives.", "Choose words and phrases to convey ideas precisely; use concrete words and sensory details.", "King Arthur Reader (Chapter 4), workbook Lesson 1.13",
       eflow("Compare the two knight sentences.", "Read Chapter 4; collect strong words.", ["Model revising the dog sentence.", "Brainstorm verbs for went and said."], "Your Turn 1–3."),
       ["Piling on adjectives (“the big, huge, giant, large castle”)."], ["One strong word beats three weak ones."], ["Make a “Said is tired” word chart."]),
    summary="Strong verbs and vivid adjectives help readers picture your writing.")

L14 = Lesson("1.14", "Planning a Narrative: Sequence and Transitions",
    "I can plan a story with a clear beginning, middle, and end, using transition words.", "W.4.3a, W.4.3c",
    [("narrative", "A story that tells about events, real or imagined."), ("sequence", "The order in which events happen."), ("transition word", "A word or phrase that connects ideas and shows order, like <i>first</i>, <i>then</i>, <i>suddenly</i>.")],
    "Think of a legend you know. What happens at the beginning, in the middle, and at the end?",
    [Text("A good narrative introduces a character and setting (<b>beginning</b>), builds a problem (<b>middle</b>), and solves it (<b>end</b>). Transition words guide the reader through time."),
     Figure(lambda t: table(t, [["Beginning", "Middle", "End"], ["at first, one day, long ago, once", "then, next, after that, suddenly, meanwhile, later", "finally, at last, in the end"]], width=W * 0.95)),
     Example("Plan a story", "A squire must find a lost horse before the tournament.",
             ["Beginning: Will, a squire, wakes up; Sir Owen's horse is gone.", "Middle: He searches the stables and the forest; he finds hoofprints; suddenly he hears a neigh in the woods.", "End: He finds the horse caught in brambles and frees it just in time."],
             "A three-part plan with characters, a problem, events in order, and a solution."),
     KeyIdea("Plan beginning, middle, and end before you write. Use transitions to show the order of events.")],
    [Problem("Name two transition words for the middle of a story.", "then, next, suddenly, after that"), Problem("What belongs in the beginning?", "characters and setting (and the start of the problem)"), Problem("What belongs in the end?", "how the problem is solved")],
    [S("Warm-Up", [SA("A transition word for the end", "finally, at last"), SA("What is a sequence?", "the order of events")], cols=2),
     S("Order the Events", [OR("Number these events in order and add a transition word to each: ___ the knight crossed the river. ___ he saw the dragon's cave. ___ he set out from the castle. ___ he returned home a hero.",
                               "1 set out from the castle (First), 2 crossed the river (Then), 3 saw the dragon's cave (Suddenly), 4 returned home a hero (Finally).", lines=3)]),
     S("Plan Your Story", [OR("Your story is about a young person in King Arthur's time who faces a challenge. Beginning (character, setting, problem):", "Answers vary.", lines=3),
                           OR("Middle (two or three events):", "Answers vary.", lines=4), OR("End (solution):", "Answers vary.", lines=2),
                           OR("List five strong words you plan to use:", "Answers vary.", lines=1)]),
     S("Exit Ticket", [OR("Write the first sentence of your story. Introduce the character and setting.", "Answers vary.", lines=2)])],
    TE("Students plan a narrative with sequence and transitions.", "Write narratives to develop imagined experiences using a clear event sequence and transitional words.", "Workbook Lesson 1.14",
       eflow("Retell a legend in three parts.", "Reread the end of Chapter 4.", ["Teach beginning-middle-end and transitions.", "Model planning the squire story."], "Students plan their own story."),
       ["Stories with no problem."], ["Ask: What goes wrong?"], ["Plan a sequel to Chapter 4."]),
    summary="Plan beginning, middle, and end; connect events with transition words.")

L15 = Lesson("1.15", "Drafting a Narrative Scene",
    "I can draft a narrative that uses dialogue, description, and precise words.", "W.4.3b, W.4.3d",
    [("dialogue", "The words characters say to each other, shown in quotation marks."), ("draft", "A first version of a piece of writing.")],
    "How can a writer show that a character is nervous without writing “he was nervous”?",
    [Text("Good narratives <b>show</b> instead of just <b>tell</b>. Use dialogue, actions, and sensory details. Instead of “Will was nervous,” write: <i>Will's hands shook as he tightened the strap. “Please hold,” he whispered.</i>"),
     Example("Show, don't tell", "Tell: The forest was scary.", ["What would you see? Twisted branches, dark shadows.", "Hear? An owl hooting, twigs cracking.", "Feel? Cold air, heart pounding."],
             "Twisted branches clawed at the sky. Somewhere an owl hooted, and a twig cracked behind me. My heart pounded."),
     Bullets(["Put a character's exact words inside quotation marks.", "Start a new paragraph each time a new person speaks.", "Put the comma or end mark inside the closing quotation mark: “Wait,” said Will."]),
     KeyIdea("Show feelings with actions, dialogue, and details. Use this week's precise words.")],
    [Problem("Show “The king was angry” with an action.", "e.g. The king slammed his fist on the table."), Problem("Punctuate: Hurry said the squire", "“Hurry,” said the squire."), Problem("Show “It was cold” with a sensory detail.", "e.g. Frost crunched under my boots and my breath made clouds.")],
    [S("Warm-Up", [SA("Punctuate: Stop shouted Kay", "“Stop!” shouted Kay."), SA("When do you start a new paragraph in dialogue?", "when a new person speaks")], cols=2),
     S("Show, Don't Tell", [OR(f"Tell: {q} Show it:", "Answers vary; must use actions, dialogue, or sensory details.", lines=2) for q in ["The squire was tired.", "The feast was delicious.", "The knight was brave."]]),
     S("Draft Your Story", [OR("Use your plan from Lesson 1.14. Write your story. Include dialogue, at least three strong words, and transitions.", "Answers vary; see narrative checklist in the Teacher Edition.", lines=18,
                               note="Look for: clear beginning-middle-end, a problem and solution, dialogue punctuated correctly, transitions, precise words.")])],
    TE("Students draft a narrative scene.", "Use dialogue and description to develop experiences and events; use concrete words and sensory details.", "Student plans from Lesson 1.14, workbook Lesson 1.15",
       eflow("Show vs tell sentences.", "Read a dialogue section aloud from the reader.", ["Teach show-don't-tell.", "Teach dialogue punctuation."], "Students draft; conference while they write.", "Finish the draft.", "Share a favorite sentence."),
       ["Dialogue without quotation marks.", "All telling, no showing."], ["Provide sentence starters for dialogue."], ["Add a second scene."]),
    summary="Show, don't tell: use dialogue, actions, and sensory details.")

L16 = Lesson("1.16", "Revising, Editing, and Publishing",
    "I can revise my writing for word choice and edit for capitalization, punctuation, and spelling.", "W.4.5, L.4.2",
    [("revise", "Improve the ideas, order, and word choice of writing."), ("edit", "Fix mistakes in capitalization, punctuation, grammar, and spelling."), ("publish", "Share a final, clean copy with readers.")],
    "What's the difference between making your writing <i>better</i> and making it <i>correct</i>?",
    [Text("<b>Revising</b> makes writing better: clearer order, stronger words, more details. <b>Editing</b> makes writing correct: capitals, punctuation, spelling. Do both before you publish."),
     Figure(lambda t: table(t, [["Revising checklist", "Editing checklist"], ["Does my story have a clear beginning, middle, and end?", "Do sentences begin with capital letters?"],
                                ["Did I use transition words?", "Do sentences end with . ? or !"], ["Did I replace tired words with precise ones?", "Is dialogue in quotation marks?"],
                                ["Did I show feelings with actions and dialogue?", "Are words spelled correctly?"]], [W * 0.48, W * 0.48], width=W * 0.96)),
     Example("Revise and edit", "the knight went to the castle he was tired", ["Revise: “went” → “trudged”; add a detail.", "Edit: capitalize The; split the run-on with a period."], "The knight trudged up the hill to the castle. He was so tired that his armor felt like a mountain on his shoulders."),
     KeyIdea("Revise for ideas and words; edit for correctness. Then publish a clean copy.")],
    [Problem("Edit: sir kay lost his sword", "Sir Kay lost his sword."), Problem("Revise: The dragon was big.", "e.g. The enormous dragon blocked the cave."), Problem("Is fixing spelling revising or editing?", "editing")],
    [S("Warm-Up", [SA("Edit: arthur pulled the sword", "Arthur pulled the sword."), SA("Revise: The sword was nice.", "e.g. The gleaming sword sparkled.")], cols=2),
     S("Edit These Sentences", [SA(q, a) for q, a in [("merlin was a wise wizard", "Merlin was a wise wizard."), ("where is excalibur asked the king", "“Where is Excalibur?” asked the king."),
                                                       ("the knights rode to camelot", "The knights rode to Camelot."), ("arthur was brave he was kind", "Arthur was brave. He was kind. (or Arthur was brave and kind.)")]], cols=1),
     S("Revise and Edit Your Story", [OR("Use both checklists on your draft. List two revisions you made.", "Answers vary.", lines=3), OR("List two edits you made.", "Answers vary.", lines=2),
                                      OR("Publish: copy your final story neatly on separate paper or type it. Then write one sentence about what you are proudest of.", "Answers vary.", lines=2)])],
    TE("Students revise, edit, and publish a narrative.", "With guidance, develop and strengthen writing by planning, revising, and editing; use correct capitalization and punctuation.", "Student drafts, workbook Lesson 1.16, Unit 1 Review",
       eflow("Better vs correct.", "Read one student draft aloud (with permission).", ["Teach the two checklists.", "Model revising and editing."], "Students revise and edit with a partner or parent.", "Workbook Lesson 1.16 and the Unit 1 Review.", "Read the published story aloud. Tomorrow: Unit 1 Test."),
       ["Only fixing spelling and calling it revision."], ["Do one checklist item at a time."], ["Illustrate the published story."]),
    summary="Revise for ideas and words, edit for correctness, then publish.")

# ================================================================= checks
C1 = Check("Weekly Check 1: Word Parts", [S("Read and answer", [
    SA("<i>careless</i> means…", "without care"), SA("<i>misplaced</i> means…", "put in the wrong place; lost"), SA("<i>displeased</i> means…", "not pleased"),
    SA("<i>repay</i> means…", "pay back"), SA("<i>thoughtful</i> means…", "full of thought; considerate"), SA("<i>unbreakable</i> means…", "not able to be broken"),
    MC("The root <i>port</i> in <i>portable</i> means…", ["see", "carry", "hear", "write"], 1),
    OR("Why did Mr. Chen say Ava's promise was unbreakable? Use a detail.", "She kept it: she walked dogs every afternoon for three weeks and paid for the books.", lines=2)], cols=2, passage=P_C1)], minutes=20)

C2 = Check("Weekly Check 2: Context Clues", [S("Read and answer", [
    MC("What is a <i>falconer</i>? Which type of clue helps?", ["a bird; example clue", "a person who trains falcons; definition clue", "a castle; antonym clue"], 1),
    OR("What does <i>patience</i> mean? Which words helped?", "waiting calmly without hurrying; “waited for hours, never hurrying”", lines=2),
    MC("<i>Docile</i> means…", ["wild", "calm and gentle", "fast"], 1, note="Antonym clue: “but wild with strangers.”"),
    OR("What does <i>plummeted</i> mean? What clue helped?", "dropped straight down quickly; restatement clue “dropping straight down like a stone”", lines=2),
    MC("“Elaine waited for the falcon to <i>land</i>.” Which meaning of <i>land</i> fits?", ["the ground of a country", "come down to rest", "to get a job"], 1),
    SA("Guide words <i>fall</i> – <i>far</i>. Is <i>falcon</i> on the page?", "Yes")], passage=P_C2)], minutes=20)

C3 = Check("Weekly Check 3: Figurative Language and Word Choice", [S("Read and answer", [
    OR("“The world outside my window was a giant white blanket.” Simile or metaphor? What does it mean?", "metaphor; snow covered everything", lines=2),
    OR("Find a simile in paragraph 1 and explain it.", "“Snowflakes danced like tiny ballerinas”: the snow fell gracefully, twirling.", lines=2),
    OR("What does “It's raining cats and dogs” usually mean? Why is the brother's use of it funny?", "raining very hard; it's snowing, so he jokes about snow cats and dogs", lines=2),
    OR("“My fingers were icicles.” What does this metaphor mean?", "Her fingers were very cold.", lines=1),
    MC("Which word is strongest?", ["chilly", "cool", "freezing"], 2),
    MC("What does “Look before you leap” mean?", ["Watch where you jump", "Think before you act", "Look at the snow"], 1)], passage=P_C3)], minutes=20)

REVIEW = Check("Unit 1 Review", [
    S("Word parts", [SA(w, a) for w, a in [("unfriendly", "not friendly"), ("reheat", "heat again"), ("powerless", "without power"), ("visitor", "a person who visits"), ("audible", "able to be heard"), ("telescope", "tool to see far")]], cols=2),
    S("Context and meaning", [OR("The <i>sentry</i>, a soldier who stood guard, watched the gate all night. What is a sentry? What kind of clue?", "a soldier who stands guard; definition clue", lines=1),
                              OR("Unlike the <i>dull</i> knife, the new sword was sharp. What does dull mean?", "not sharp", lines=1),
                              OR("“Her voice was music to my ears.” What does this mean?", "I was very happy to hear it.", lines=1),
                              OR("Rewrite with precise words: “The man walked into the room and said hello.”", "e.g. The old blacksmith shuffled into the hall and muttered, “Good evening.”", lines=2)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 1 Test", [
    S("Part A · Vocabulary in context (1 point each)", [
        MC("In paragraph 1, a <i>squire</i> is…", ["a knight", "a knight's helper in training", "a horse"], 1),
        MC("Which type of context clue helps you with <i>squire</i>?", ["definition (after a comma)", "antonym", "example"], 0),
        OR("What does <i>frayed</i> mean in paragraph 3? What clue helped?", "worn and coming apart; restatement “its threads worn and coming apart”", lines=2),
        MC("In paragraph 1, <i>careless</i> means…", ["full of care", "without care", "able to care"], 1),
        MC("In paragraph 4, the word <i>replaced</i> has the prefix <i>re-</i>. It means…", ["placed wrongly", "put a new one in place of the old", "placed before"], 1),
        MC("In paragraph 4, <i>hesitate</i> means…", ["to stop and wait before acting", "to run fast", "to shout"], 0, note="Inference: he immediately ran, so he did not wait.")], passage=P_TEST),
    S("Part B · Figurative language (1 point each)", [
        OR("“The field was a sea of colorful tents.” Simile or metaphor? Meaning?", "metaphor; there were so many tents they spread out like an ocean", lines=2),
        OR("“Banners snapped in the wind like flags on a ship.” Simile or metaphor?", "simile", lines=1),
        OR("“Will's face glowed like the sunrise.” What does this show about how Will felt?", "He was very happy and proud.", lines=1),
        OR("What does Sir Owen mean by “A knight is only as good as his squire”?", "A knight's success depends on his helper's work.", lines=2)]),
    S("Part C · Word study (1 point each)", [SA(w, a) for w, a in [("disappoint (prefix + meaning)", "dis- : not; to fail to please"), ("quickly (suffix + meaning)", "-ly : in a quick way"),
                                                                   ("audience (root + meaning)", "aud : hear; people who listen/watch"), ("Stronger word for <i>happy</i>", "thrilled, overjoyed, ecstatic")]], cols=2),
    S("Part D · Writing (4 points)", [OR("Write a short scene (5–7 sentences) about what happens after the tournament. Use dialogue, a transition word, a simile or metaphor, and at least two precise words.",
                                         "Answers vary. 1 point each: dialogue correctly punctuated; transition; simile or metaphor; precise words and clear sequence.", lines=10, points=4)])],
    kind="test", minutes=45, rubric=[["16–18 (85%+)", "Mastered."], ["13–15", "Proficient; review missed skills."], ["Below 13", "Reteach word parts or context clues and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-10-12", "2026-10-19", "2026-10-26", "2026-11-02"], CHECKS, REVIEW, TEST)

UNIT = Unit(1, "Word Power", "Word parts, context clues, figurative language, and precise words, with King Arthur and the Round Table, Chapters 1–4.",
    "Strong readers figure out new words on their own, and strong writers choose words carefully. In this unit you will use prefixes, suffixes, roots, and context clues to unlock word meanings, explore similes, metaphors, and idioms, and write your own legend-style story while you read the first chapters of King Arthur and the Round Table.",
    ["Use prefixes, suffixes, and Greek and Latin roots to figure out word meanings.", "Use context clues: definitions, synonyms, antonyms, examples, and inference.",
     "Explain similes, metaphors, idioms, and proverbs.", "Choose precise words and write a narrative with dialogue and transitions."],
    [("RL.4.1, RL.4.3", "Refer to details in a text; describe characters, settings, and events."), ("RL.4.4", "Determine the meaning of words and phrases, including figurative language."),
     ("L.4.4a–c", "Use context, affixes and roots, and reference materials to determine word meaning."), ("L.4.5a–c", "Understand figurative language, word relationships, and nuances."),
     ("L.4.6", "Acquire and use academic and domain-specific words."), ("W.4.3, W.4.5", "Write narratives; plan, revise, and edit writing.")],
    [("prefix", "A word part at the beginning of a word."), ("suffix", "A word part at the end of a word."), ("root", "The main part of a word."), ("context clue", "A hint in the text about a word's meaning."),
     ("simile", "A comparison using like or as."), ("metaphor", "A comparison saying one thing is another."), ("idiom", "A phrase with a meaning different from its words.")],
    ["Reading grade-level text independently.", "Writing complete sentences with capitals and end marks."],
    ["King Arthur and the Round Table Reader (Chapters 1–4)", "Dictionary and thesaurus (print or online)", "Index cards for word study"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Every time you meet a new word in a book, a game, or a science lesson, you can use word parts and context to figure it out without stopping to ask.",
    family_note="At dinner, play “Word Detective”: one person says a word with a prefix or suffix, and others guess its meaning from the parts.",
    weeks=WEEKS)
