"""Grade 4 ELA · Unit 6: Sources and Evidence — comparing sources, reasons and evidence, opinion writing, visual information, and a short research report.
Anchor reading: Treasure Island Reader, Chapters 8–9, “The Schooner,” and “The Voyage” (Mar 29 – Apr 23, 2027)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule
from content.ela4.unit01 import S, MC, OR, SA
from content.ela4.unit04 import TI


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


# ================================================================= passages
P_LOG = Passage("Source 1: A Ship's Log, 1789 (adapted)", [
    "<b>May 3.</b> Wind from the northeast. Sighted a large whale off the starboard bow at noon. Crew in good health. Our water barrels are half full.",
    "<b>May 4.</b> Heavy rain. Two sailors sick with fever. Caught fresh rainwater in the sails and filled three barrels.",
    "<b>May 5.</b> Clear skies. Land sighted at dawn. All hands cheered.",
], source="A primary source, adapted for young readers (invented for this lesson)", genre="Primary source", numbered=False)
P_ARTICLE = Passage("Source 2: Life on Long Voyages", [
    "Sailors on long voyages in the 1700s faced many dangers. Fresh water often ran low, so crews collected rainwater whenever they could. Illness spread quickly in the crowded spaces below deck.",
    "Historians learn about these voyages by studying ships' logs, letters, and maps written by the sailors themselves.",
], source="A secondary source (original informational text)", genre="Secondary source")

P_HOMEWORK = Passage("Should Fourth Graders Have Homework?", [
    "Many people argue about homework. I believe fourth graders should have a small amount of homework, about twenty minutes a night.",
    "First, homework helps students practice. When students practice math facts or reading at home, they remember them better. A teacher at my school said her students' test scores rose after she assigned ten minutes of nightly reading.",
    "Second, homework teaches responsibility. Students learn to plan their time and finish work without someone reminding them.",
    "However, too much homework can be harmful. Children need time to play, rest, and be with their families. That is why twenty minutes is the right amount: enough to practice, but not so much that it takes over the evening.",
], source="An original opinion piece", genre="Opinion writing")

P_SCHOONER = Passage("The Schooner", [
    "The <i>Hispaniola</i> in <i>Treasure Island</i> is a <b>schooner</b>, a sailing ship with two or more masts. Schooners were popular in the 1700s and 1800s because they were fast and needed a smaller crew than larger ships.",
    "Unlike square-rigged ships, whose sails hung across the ship, a schooner's main sails ran along its length, from front to back. This let schooners sail closer to the direction the wind was coming from.",
    "A triangular sail called a <b>jib</b> stretched forward from the front mast toward the bow. Sailors adjusted the sails using the <b>rigging</b>, and a <b>rudder</b> at the stern steered the ship.",
], source="An original informational text", genre="Informational text")

P_STEAM = Passage("From Sail to Steam", [
    "For thousands of years, ships depended on wind. In the 1800s, inventors began building ships powered by steam engines. Steamships could travel even when the wind died, and they kept to schedules.",
    "At first, many ships used both sails and steam. By 1900, steamships carried most passengers and cargo across the oceans, and the great age of sail was ending.",
], source="An original informational text", genre="Informational text")

P_ISLANDMAP = Passage("Reading the Map of Skeleton Island", [
    "Maps use symbols to stand for real features. A <b>key</b> (or legend) explains what each symbol means. A <b>compass rose</b> shows directions, and a <b>scale</b> shows how distances on the map compare to real distances.",
    "On the map below, the stockade is in the western part of the island. The hills rise near the center, and a swamp lies to the east. The X marks the spot where the treasure was buried, and the anchor symbol shows where ships could anchor safely.",
], source="An original informational text", genre="Informational text")

P_C16A = Passage("Source A: Diary of Ruth, 1849 (invented for this check)", [
    "We have been walking beside the wagons for three weeks. My shoes have holes, and the dust gets into everything, even the bread. Today we crossed a river, and our wagon nearly tipped. Mother held my hand so tightly it hurt.",
], source="A primary source written for this check", genre="Primary source", numbered=False)
P_C16B = Passage("Source B: The Oregon Trail", [
    "Between 1840 and 1860, hundreds of thousands of people traveled west on the Oregon Trail. The 2,000-mile journey took four to six months. Most travelers walked beside their wagons to keep the load light. River crossings were among the most dangerous parts of the trip.",
], source="A secondary source (original informational text)", genre="Secondary source", numbered=False)

P_C17 = Passage("Our Town Needs a Dog Park", [
    "Our town should build a dog park. Dogs need exercise, and many families live in apartments without yards. A study in another city found that dog parks reduced the number of dogs running loose on the streets.",
    "Dog parks also bring people together. Neighbors meet and talk while their dogs play. And dog parks are fun! Everyone loves dogs.",
], source="An original opinion piece", genre="Opinion writing")

P_TEST = Passage("Why Bees Matter", [
    "<b>Tiny Workers, Big Job</b>",
    "Bees are much more than insects that buzz and sting. As they collect nectar, bees carry pollen from flower to flower. This process, called <b>pollination</b>, helps plants make fruits and seeds.",
    "<b>Food on Our Tables</b>",
    "Scientists estimate that about one out of every three bites of food we eat depends on pollinators such as bees. Apples, almonds, blueberries, and cucumbers all need pollination.",
    "<b>Bees in Trouble</b>",
    "In recent years, the number of honeybee colonies in some areas has dropped. Scientists point to several causes, including the loss of wildflowers, harmful chemicals, and diseases.",
    "<b>How You Can Help</b>",
    "People can help by planting flowers, avoiding chemicals that harm bees, and leaving some wild areas in their yards. Even a single pot of flowers on a balcony can feed bees.",
], source="An original informational text", genre="Informational text", numbered=False)

# ================================================================= Week 1 · Compare related sources (Chapter 8)
L1 = Lesson("6.1", "Primary and Secondary Sources",
    "I can tell the difference between primary and secondary sources and explain what each offers.", "RI.4.6, RI.4.9",
    [("primary source", "A source created by someone who was there at the time, such as a diary, letter, photo, or ship's log."),
     ("secondary source", "A source created later by someone who studied primary sources, such as a textbook or article.")],
    "If you wanted to know what it was really like on a sailing ship in 1789, what would be the best thing to read?",
    [ReaderAssign(TI, "Chapter 8: My Life Hangs in the Balance", "What danger is Jim in? How does he get out of it?"),
     Text("A <b>primary source</b> comes from the time and place being studied. A <b>secondary source</b> explains or summarizes events later. Primary sources give details and feelings from the moment; secondary sources give background and the big picture."),
     P_LOG, P_ARTICLE,
     Example("Compare", "What do Source 1 and Source 2 both show?", ["Source 1: “Caught fresh rainwater in the sails”; “Two sailors sick with fever.”", "Source 2: crews collected rainwater; illness spread quickly."],
             "Both show that water ran low and illness was a danger. The log gives specific day-by-day details; the article explains the big picture."),
     KeyIdea("Primary = from the time (firsthand). Secondary = written later (explains). Use both.")],
    [Problem("Is a ship's log primary or secondary?", "primary"), Problem("Is a textbook chapter about pirates primary or secondary?", "secondary"), Problem("What does Source 2 say historians study?", "logs, letters, and maps written by sailors")],
    [S("Warm-Up", [SA("Primary source example", "diary, letter, photo, log"), SA("Secondary source example", "textbook, encyclopedia, article")], cols=2),
     S("Sort the Sources", [SA(q, a) for q, a in [("a photograph taken in 1900", "primary"), ("an encyclopedia article on the Titanic", "secondary"), ("a letter from a soldier", "primary"),
                                                  ("a biography of Abraham Lincoln written in 2010", "secondary"), ("Grandma's diary from 1965", "primary"), ("a website explaining volcanoes", "secondary")]], cols=2),
     S("Compare", [OR("What can you learn from the ship's log that the article doesn't tell?", "exact days, weather, the whale, three barrels filled, land sighted, the crew cheering", lines=3),
                   OR("What does the article tell that the log doesn't?", "that this was common on many voyages; why illness spread; how historians learn about voyages", lines=2)]),
     S("Exit Ticket", [OR("Is Jim's narration in Treasure Island like a primary source? Explain.", "It is written like a firsthand account by someone who was there, but the book is fiction.", lines=2)])],
    te("Students distinguish primary and secondary sources.", "Compare firsthand and secondhand accounts; integrate information from two texts.", "Treasure Island Reader (Chapter 8), workbook Lesson 6.1",
       "What would you read?", ["Read Chapter 8.", "Read Sources 1 and 2."], ["Teach primary vs secondary.", "Model the comparison."], "Your Turn 1–3.",
       ["Thinking old means primary."], ["Ask: Was the creator there at the time?"], ["Find a family primary source (photo, letter)."]),
    summary="Primary sources come from the time; secondary sources explain later.")

L2 = Lesson("6.2", "Comparing Sources on the Same Topic",
    "I can compare what two sources say about the same topic and notice agreements and differences.", "RI.4.9",
    [("corroborate", "Confirm a fact with another source.")],
    "If two websites disagree about a fact, what should you do?",
    [Text("When sources <b>agree</b>, you can feel more confident. When they <b>disagree</b>, check who wrote them, when, and why, and look for a third source."),
     P_SCHOONER, P_STEAM,
     Example("Find agreement", "Do both texts agree that sailing ships depended on wind?", ["Schooner text: sails let the ship move with the wind.", "Steam text: “ships depended on wind.”"], "Yes; they corroborate each other."),
     KeyIdea("Facts confirmed by two reliable sources are stronger. When sources disagree, investigate.")],
    [Problem("What advantage did schooners have?", "fast and needed a smaller crew; sailed closer to the wind"), Problem("What advantage did steamships have?", "could travel without wind and keep schedules"), Problem("What does corroborate mean?", "confirm with another source")],
    [S("Warm-Up", [SA("Corroborate means…", "confirm with another source"), SA("If sources disagree, look for…", "a third source / check the authors")], cols=2),
     S("Compare", [OR("What topic do both texts share?", "ships / how ships moved", lines=1),
                   OR("How does each text help explain why the age of sail ended?", "Schooner text: ships needed wind; Steam text: steamships didn't, so they replaced sailing ships by 1900.", lines=3),
                   OR("Write one fact the two texts corroborate.", "Sailing ships depended on wind.", lines=1)]),
     S("Exit Ticket", [OR("Why is it smart to check more than one source?", "One source could be wrong or incomplete.", lines=2)])],
    te("Students compare sources.", "Integrate information from two texts on the same topic.", "Workbook Lesson 6.2",
       "Disagreeing websites.", "Read both texts.", ["Teach corroboration."], "Your Turn 1–3.",
       ["Accepting the first source as true."], ["Agree/disagree chart."], ["Find two sources on a topic and compare."]),
    summary="Compare sources; corroborate facts; investigate disagreements.")

L3 = Lesson("6.3", "Is This Source Reliable?",
    "I can judge whether a source is reliable.", "W.4.8, RI.4.8",
    [("reliable", "Trustworthy and accurate."), ("credentials", "Training or experience that makes someone an expert.")],
    "Would you trust a website about sharks written by a marine biologist or by an anonymous fan site?",
    [Text("Ask these questions about any source:"),
     Figure(lambda t: table(t, [["Question", "Why it matters"], ["Who wrote it? Are they an expert?", "Experts are more likely to be accurate."], ["When was it written?", "Science and news change; newer may be better."],
                                ["Why was it written?", "Ads and opinion pieces may leave out facts."], ["Does it give evidence and sources?", "Facts should be backed up."], ["Do other reliable sources agree?", "Corroboration builds trust."]],
                            [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     Example("Judge a source", "A site called “Bees R Awesome” with no author says bees “never sting.”", ["No author or credentials.", "Claim is not backed by evidence.", "Other sources say bees can sting."], "Not reliable."),
     KeyIdea("Check the author, date, purpose, evidence, and whether other sources agree.")],
    [Problem("More reliable: a museum website or an anonymous blog?", "museum website"), Problem("Why check the date?", "information may be outdated"), Problem("Why be careful with an ad?", "its purpose is to sell, so it may leave out facts")],
    [S("Warm-Up", [SA("Reliable means…", "trustworthy"), SA("Credentials are…", "training or experience")], cols=2),
     S("Reliable or Not?", [OR(q, a, lines=2) for q, a in [
         ("A 1965 encyclopedia article about space exploration", "partly reliable; written by experts but outdated"), ("A National Park Service page about Yellowstone", "reliable; government experts, current"),
         ("A video by a toy company saying its toy is “the best ever”", "not reliable for facts; its purpose is to sell"), ("A book on sharks by a marine biologist, published last year", "reliable; expert and recent")]]),
     S("Exit Ticket", [OR("Write two questions you'll ask about any website you use for research.", "e.g. Who wrote it? When was it written?", lines=2)])],
    te("Students judge source reliability.", "Gather relevant information from print and digital sources.", "Workbook Lesson 6.3",
       "Shark site.", "Discuss sample sources.", ["Teach the five questions."], "Your Turn 1–3.",
       ["Trusting anything that looks professional."], ["Checklist bookmark."], ["Evaluate two real websites with a parent."]),
    summary="Check author, date, purpose, evidence, and agreement.")

L4 = Lesson("6.4", "Taking Notes from Sources",
    "I can take notes in my own words and record where each fact came from.", "W.4.8",
    [("note card", "A card or box with one fact or idea and its source."), ("plagiarism", "Using someone else's words or ideas as your own.")],
    "Why shouldn't you copy sentences straight from a book into your report?",
    [Text("Good notes are short, in your own words, and labeled with the source. Copying whole sentences is <b>plagiarism</b>. Write key words, not full sentences, then turn them into your own sentences later."),
     Example("From text to notes", "Text: “Schooners were popular in the 1700s and 1800s because they were fast and needed a smaller crew than larger ships.”",
             ["Key words: schooners, 1700s–1800s, fast, small crew.", "Note: Schooners: popular 1700s–1800s; fast; small crew.", "Source: “The Schooner.”"], "Schooners: popular 1700s–1800s, fast, small crew. (Source: “The Schooner”)"),
     KeyIdea("Key words in your own words + the source = a good note.")],
    [Problem("What is plagiarism?", "using someone else's words or ideas as your own"), Problem("Should notes be full sentences?", "No, key words"), Problem("What must every note include?", "the source")],
    [S("Warm-Up", [SA("Notes should be in…", "your own words"), SA("Each note needs a…", "source")], cols=2),
     S("Take Notes", [OR("Take two notes from “From Sail to Steam.” Include the source.", "e.g. Steamships 1800s; didn't need wind; kept schedules (From Sail to Steam). By 1900 steam carried most cargo (From Sail to Steam).", lines=3),
                      OR("Take two notes from Source 2, “Life on Long Voyages.”", "e.g. water ran low; collected rainwater; illness spread (Life on Long Voyages).", lines=3)]),
     S("Exit Ticket", [OR("Turn one note into a sentence in your own words.", "Answers vary.", lines=2)])],
    te("Students take source-labeled notes.", "Take notes and categorize information; provide a list of sources.", "Note cards, workbook Lesson 6.4",
       "Why not copy?", "Reread the schooner text.", ["Model key-word notes."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Copying full sentences."], ["Cover the text while writing notes."], ["Take notes on Chapter 8."]),
    summary="Key words, own words, source labeled.")

# ================================================================= Week 2 · Reasons and evidence (Chapter 9)
L5 = Lesson("6.5", "Claims, Reasons, and Evidence",
    "I can identify an author's claim, reasons, and evidence.", "RI.4.8",
    [("claim", "The author's main opinion or argument."), ("reason", "Why the author believes the claim."), ("evidence", "Facts, examples, or expert ideas that support a reason.")],
    "If you want your parents to agree to something, how do you convince them?",
    [ReaderAssign(TI, "Chapter 9: The Adventure Comes to an End", "How does the story end? Who gets the treasure?"),
     Text("Persuasive authors state a <b>claim</b>, give <b>reasons</b>, and support each reason with <b>evidence</b>. A reason answers <i>why?</i>; evidence answers <i>how do you know?</i>"),
     P_HOMEWORK,
     Figure(lambda t: table(t, [["Claim", "Fourth graders should have about twenty minutes of homework a night."], ["Reason 1", "Homework helps students practice."],
                                ["Evidence", "A teacher's students' scores rose with ten minutes of nightly reading."], ["Reason 2", "Homework teaches responsibility."], ["Evidence", "(none given; only explanation)"]],
                            [1.0 * inch, 4.6 * inch], width=5.6 * inch, header=False)),
     KeyIdea("Claim → reasons (why) → evidence (how do you know).")],
    [Problem("What is the author's claim?", "Fourth graders should have about twenty minutes of homework a night."), Problem("Which reason has evidence?", "Reason 1 (practice): the teacher's test scores"), Problem("What counterargument does the author address?", "too much homework is harmful")],
    [S("Warm-Up", [SA("A claim is…", "the author's main opinion"), SA("Evidence answers…", "how do you know?")], cols=2),
     S("Analyze", [OR("List the author's two reasons.", "Homework helps students practice; homework teaches responsibility.", lines=2),
                   OR("Which reason is better supported? Why?", "Reason 1, because it has evidence (test scores). Reason 2 has only explanation.", lines=3),
                   OR("How does paragraph 4 make the argument stronger?", "It admits too much homework is bad and explains why twenty minutes balances both.", lines=2)], passage=P_HOMEWORK),
     S("Exit Ticket", [OR("What evidence could the author add to support Reason 2?", "e.g. a survey of teachers, an example of a student learning to plan", lines=2)])],
    te("Students identify claims, reasons, and evidence.", "Explain how an author uses reasons and evidence to support particular points.", "Treasure Island Reader (Chapter 9), workbook Lesson 6.5",
       "Convincing parents.", ["Read Chapter 9.", "Read the homework piece."], ["Teach claim-reason-evidence.", "Model the chart."], "Your Turn 1–3.",
       ["Calling every sentence evidence."], ["Ask: Why? / How do you know?"], ["Analyze a real letter to the editor."]),
    summary="Claim, reasons (why), evidence (how do you know).")

L6 = Lesson("6.6", "Evaluating Evidence",
    "I can decide whether evidence is relevant and strong enough to support a reason.", "RI.4.8",
    [("relevant", "Connected to the reason."), ("sufficient", "Enough to convince a reader.")],
    "Is “Everyone loves dogs” good evidence for building a dog park?",
    [Text("Strong evidence is <b>relevant</b> (it connects to the reason) and <b>sufficient</b> (there's enough of it). Weak evidence includes opinions disguised as facts, exaggerations (<i>everyone</i>, <i>always</i>), and unrelated details."),
     Example("Evaluate", "Claim: Our school needs a garden. Evidence: “Gardens are pretty.”", ["Relevant? Somewhat, but it's an opinion.", "Stronger: “Students who garden eat more vegetables, according to a university study.”"],
             "The first is weak (opinion); the second is strong (a fact from a study)."),
     KeyIdea("Strong evidence: relevant facts, examples, or expert information. Weak: opinions, exaggerations, unrelated details.")],
    [Problem("Strong or weak: “All kids hate broccoli.”", "weak (exaggeration)"), Problem("Strong or weak: “A survey of 200 students found 80% wanted longer recess.”", "strong"), Problem("Why is “everyone” a warning word?", "It's usually an exaggeration.")],
    [S("Warm-Up", [SA("Relevant means…", "connected"), SA("A warning word for exaggeration", "everyone, always, never")], cols=2),
     S("Strong or Weak?", [OR(q, a, lines=1) for q, a in [
         ("Claim: Bikes are good exercise. Evidence: Doctors say biking strengthens the heart.", "strong: expert, relevant"), ("Claim: Our town needs a library. Evidence: Libraries are cool.", "weak: opinion"),
         ("Claim: Recycling helps. Evidence: Our town recycled 2 tons of paper last year, saving about 34 trees.", "strong: fact"), ("Claim: Cats are the best pets. Evidence: My cat is orange.", "weak: unrelated")]]),
     S("Exit Ticket", [OR("Rewrite this weak evidence to be stronger: “Reading is fun, so kids should read every day.”", "e.g. Studies show students who read 20 minutes daily learn more words.", lines=2)])],
    te("Students evaluate evidence.", "Explain how an author uses reasons and evidence.", "Workbook Lesson 6.6",
       "Everyone loves dogs?", "Review the homework piece.", ["Teach relevant and sufficient.", "Model the garden example."], "Your Turn 1–3.",
       ["Accepting exaggerations."], ["Circle warning words."], ["Find weak evidence in an ad."]),
    summary="Strong evidence is relevant, factual, and sufficient.")

L7 = Lesson("6.7", "Opinion Writing: Claims and Reasons",
    "I can state an opinion and support it with reasons and evidence.", "W.4.1a, W.4.1b",
    [("opinion piece", "Writing that states and supports an opinion.")],
    "Was Jim Hawkins brave or reckless? How would you prove your opinion?",
    [Text("An opinion piece begins with an introduction that states your <b>opinion</b> clearly. Each body paragraph gives a <b>reason</b> with <b>evidence</b> from the text."),
     Figure(lambda t: table(t, [["Part", "What to include"], ["Introduction", "Hook + clear opinion"], ["Reason 1", "Reason + evidence from the text + explanation"], ["Reason 2", "Reason + evidence + explanation"], ["Conclusion", "Restate opinion + final thought"]],
                            [1.4 * inch, 4.2 * inch], width=5.6 * inch)),
     Example("Plan", "Opinion: Jim was brave, not reckless.", ["Reason 1: He faced danger to protect others.", "Evidence: a moment from the Reader where Jim takes a risk to help his friends.", "Reason 2: His choices helped the good side win.", "Evidence: an event from Chapters 8–9."],
             "A plan with an opinion, two reasons, and evidence for each."),
     KeyIdea("Opinion → reasons → evidence from the text.")],
    [Problem("Where is the opinion stated?", "in the introduction"), Problem("What should each reason have?", "evidence and explanation"), Problem("Write an opinion statement about Long John Silver.", "Answers vary; must state an opinion.")],
    [S("Warm-Up", [SA("An opinion piece starts with…", "a hook and an opinion"), SA("Each reason needs…", "evidence")], cols=2),
     S("Plan Your Opinion Piece", [OR("Prompt: Was Jim Hawkins brave or reckless? Your opinion:", "Answers vary.", lines=2),
                                   OR("Reason 1 and evidence from the Reader:", "Answers vary.", lines=3), OR("Reason 2 and evidence:", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Write a hook for your opinion piece.", "Answers vary.", lines=2)])],
    te("Students plan opinion writing.", "Introduce a topic and state an opinion; provide reasons supported by facts and details.", "Workbook Lesson 6.7",
       "Brave or reckless?", "Skim Chapters 7–9 for evidence.", ["Teach the structure.", "Model the plan."], "Plan together.",
       ["Reasons without evidence."], ["Evidence sticky notes."], ["Argue the opposite side too."]),
    summary="State an opinion; support it with reasons and text evidence.")

L8 = Lesson("6.8", "Opinion Writing: Linking Words and Conclusions",
    "I can link my opinion and reasons with transitions and write a strong conclusion.", "W.4.1c, W.4.1d",
    [("linking words", "Words that connect opinions and reasons, such as because, for instance, in addition.")],
    "How do linking words make an argument easier to follow?",
    [Text("Use linking words: <i>because, therefore, since, for example, for instance, in addition, another reason, most importantly</i>. End with a conclusion that restates your opinion in new words and leaves the reader thinking."),
     Example("Conclusion", "Opinion: Jim was brave.", ["Restate in new words.", "Final thought."], "In the end, Jim's courage made the difference. He was young and often afraid, but he never let fear stop him from doing what was right."),
     KeyIdea("Linking words connect reasons; conclusions restate and leave a final thought.")],
    [Problem("Linking word for an example", "for example, for instance"), Problem("Linking word for a second reason", "in addition, another reason"), Problem("What does a conclusion restate?", "the opinion")],
    [S("Warm-Up", [SA("Linking word that shows cause", "because, since"), SA("Linking word for the strongest reason", "most importantly")], cols=2),
     S("Write", [OR("Write your opinion piece: Was Jim Hawkins brave or reckless? Use your plan from Lesson 6.7, linking words, and a conclusion.", "Answers vary.", lines=22,
                    note="1 point each: clear opinion; two reasons; evidence for each; linking words; conclusion.")])],
    te("Students write opinion pieces.", "Link opinion and reasons using words and phrases; provide a concluding statement.", "Plans, workbook Lesson 6.8",
       "Linking words.", "Reread the homework piece's linking words.", ["Model a conclusion."], "Draft.",
       ["Conclusions that only repeat the introduction."], ["Final-thought starters: In the end… / That's why…"], ["Read the piece aloud to the family."], independent="Finish the opinion piece. Weekly Check tomorrow."),
    summary="Link reasons with transitions; conclude with a restated opinion and final thought.")

# ================================================================= Week 3 · Integrate text and visual information (The Schooner)
L9 = Lesson("6.9", "Reading Labeled Diagrams",
    "I can use a labeled diagram to understand a text.", "RI.4.7",
    [("diagram", "A drawing that shows the parts of something or how it works."), ("label", "A word naming a part of a diagram.")],
    "How would you explain the parts of a ship without a picture?",
    [ReaderAssign(TI, "Text and diagrams: The Schooner", "Match each part named in the text to the diagram."),
     Text("A <b>diagram</b> shows what words describe. Read the text and the diagram together: find each labeled part and connect it to the sentence that explains it."),
     P_SCHOONER,
     Figure(lambda t: ship_diagram(t), caption="Diagram: Parts of a Schooner"),
     Example("Connect text and diagram", "Where is the jib?", ["Text: a triangular sail that stretched forward toward the bow.", "Diagram: the triangle sail at the front."], "The jib is the triangular sail at the front, reaching toward the bow."),
     KeyIdea("Match words in the text to labels in the diagram. The diagram helps you picture what the words explain.")],
    [Problem("How many masts does the schooner have?", "two"), Problem("Where is the rudder?", "at the stern"), Problem("What does the rigging do?", "holds up and adjusts the masts and sails")],
    [S("Warm-Up", [SA("A label is…", "a word naming a part"), SA("A diagram shows…", "parts or how something works")], cols=2),
     S("Use the Diagram", [OR("Explain how a schooner's sails were different from a square-rigged ship's sails. How does the diagram help?", "Schooner sails ran front to back; square sails hung across. The diagram shows sails running along the ship.", lines=3),
                           OR("Explain how a sailor would steer and adjust the ship, using three labels.", "Rudder at the stern steers; rigging adjusts the sails on the masts.", lines=3)]),
     S("Exit Ticket", [OR("Which is more helpful for you: the text or the diagram? Why?", "Answers vary.", lines=2)])],
    te("Students use labeled diagrams.", "Interpret information presented visually and explain how it contributes.", "Treasure Island Reader (The Schooner), workbook Lesson 6.9",
       "Explaining without a picture.", ["Read the Reader's schooner pages.", "Read the text and diagram here."], ["Model matching text to labels."], "Your Turn 1–3.",
       ["Ignoring the diagram."], ["Point to each label as you read."], ["Draw and label a diagram of something at home."]),
    summary="Match text to labels; diagrams help you picture explanations.")

L10 = Lesson("6.10", "Reading Maps",
    "I can use a map's key, compass rose, and scale to answer questions.", "RI.4.7",
    [("key / legend", "Explains what map symbols mean."), ("compass rose", "Shows north, south, east, and west."), ("scale", "Shows how map distance compares to real distance.")],
    "How did Jim and his friends know where to find the treasure?",
    [P_ISLANDMAP,
     Figure(lambda t: island_map(t), caption="Map: Skeleton Island (an invented map in the style of Treasure Island)"),
     Example("Use the map", "In which direction would you walk from the stockade to the treasure?", ["Stockade: west side. Treasure X: east of the hills.", "Compass rose: east is to the right."], "east (toward the right side of the map)"),
     KeyIdea("Use the key for symbols, the compass rose for direction, and the scale for distance.")],
    [Problem("What does the □ symbol stand for?", "the stockade"), Problem("Is the swamp north or south of the X?", "south"), Problem("About how wide is the island, using the scale?", "about 4 miles (accept reasonable estimates)")],
    [S("Warm-Up", [SA("What shows directions?", "compass rose"), SA("What explains symbols?", "key / legend")], cols=2),
     S("Use the Map", [SA(q, a) for q, a in [("Where can ships anchor?", "near the anchor symbol, southwest"), ("What lies near the center?", "hills"), ("Direction from the hills to the swamp", "southeast"), ("Direction from the treasure to the stockade", "west")]], cols=2),
     S("Explain", [OR("How would this map help a treasure hunter? Use two map features.", "Key shows where the X and hazards are; compass and scale give direction and distance.", lines=3)]),
     S("Exit Ticket", [Problem("Draw a small map of your room or yard with a key and compass rose.", "Answers vary.", space=150, wide=True)])],
    te("Students read maps.", "Interpret information presented visually.", "Workbook Lesson 6.10",
       "How did they find the treasure?", "Read the map text.", ["Model key, compass, scale."], "Your Turn 1–3.",
       ["Assuming up is always north without checking."], ["Find N on the compass rose first."], ["Make a treasure map for a sibling to follow."]),
    summary="Key, compass rose, and scale unlock a map.")

L11 = Lesson("6.11", "Reading Graphs in Informational Text",
    "I can explain what a graph shows and how it supports the text.", "RI.4.7",
    [("bar graph", "A graph that compares amounts using bars.")],
    "Why might an author show numbers in a graph instead of a sentence?",
    [Text("A graph shows patterns at a glance. Read the title, the labels on each axis, and the scale. Then ask what pattern the graph shows and how it supports the text."),
     P_STEAM,
     Figure(lambda t: bar_graph(t, ["1820", "1850", "1880", "1900"], [5, 20, 55, 80], title="Percent of Ocean Cargo Carried by Steamships (approximate)", ylabel="percent", step=20, height=180),
            caption="Graph: an illustrative graph for this lesson; values are rounded estimates."),
     Example("Read the graph", "What pattern does the graph show?", ["Read the title and axes.", "Compare bars: 5, 20, 55, 80."], "Steamships carried more and more cargo over time, supporting the text's point that steam replaced sail."),
     KeyIdea("Title → labels → scale → pattern → connection to the text.")],
    [Problem("About what percent did steamships carry in 1880?", "about 55%"), Problem("Between which years was the biggest increase?", "1850 to 1880"), Problem("How does the graph support the text?", "It shows steamships carrying most cargo by 1900.")],
    [S("Warm-Up", [SA("Read a graph's ___ first.", "title"), SA("What does the y-axis show here?", "percent")], cols=2),
     S("Use the Graph", [SA(q, a) for q, a in [("Percent in 1820", "about 5%"), ("Percent in 1900", "about 80%"), ("Increase from 1850 to 1900", "about 60 percentage points"), ("Did sailing ships still carry some cargo in 1900?", "Yes, about 20%")]], cols=2),
     S("Explain", [OR("Write two sentences explaining how the graph and the text work together.", "The text says steamships replaced sail by 1900; the graph shows their share growing from 5% to about 80%.", lines=3)])],
    te("Students read graphs.", "Interpret information presented visually and explain how it contributes to understanding.", "Workbook Lesson 6.11",
       "Graph vs sentence.", "Read “From Sail to Steam.”", ["Model reading the graph."], "Your Turn 1–3.",
       ["Reading bars without the scale."], ["Trace from the bar to the axis with a finger."], ["Make a bar graph of family favorite foods."]),
    summary="Read the title, labels, and scale; connect the pattern to the text.")

L12 = Lesson("6.12", "Adding Visuals to Your Writing",
    "I can add a diagram, map, chart, or graph to my own informational writing.", "W.4.2a",
    [("caption", "A sentence that explains a visual.")],
    "What visual would help a reader understand your favorite hobby?",
    [Text("Writers add visuals to make information clearer. Choose the right type, give it a title and labels, write a caption, and refer to it in your writing (<i>see the diagram</i>)."),
     Figure(lambda t: table(t, [["If you want to show…", "use a…"], ["parts of something", "labeled diagram"], ["where things are", "map"], ["events over time", "timeline"], ["amounts or comparisons", "bar graph or chart"], ["steps", "numbered flowchart"]],
                            [2.6 * inch, 2.2 * inch], width=4.8 * inch)),
     KeyIdea("Choose the visual that fits, label it, caption it, and mention it in your writing.")],
    [Problem("Best visual for the steps of making bread", "flowchart"), Problem("Best visual for the parts of a bicycle", "labeled diagram"), Problem("What does a caption do?", "explains the visual")],
    [S("Warm-Up", [SA("Visual for events over time", "timeline"), SA("Visual for amounts", "bar graph")], cols=2),
     S("Create", [Problem("Choose a topic you know well. Create a visual for it with a title, labels, and a caption.", "Answers vary.", space=200, wide=True),
                  OR("Write three sentences about the topic that refer to your visual.", "Answers vary.", lines=3)])],
    te("Students add visuals to writing.", "Include formatting, illustrations, and multimedia to aid comprehension.", "Colored pencils, workbook Lesson 6.12",
       "Hobby visual.", "Review the four visuals in this unit.", ["Teach the visual-choice chart."], "Create the visual.",
       ["Visuals with no labels."], ["Label checklist."], ["Make a poster."], independent="Finish the visual and sentences. Weekly Check tomorrow."),
    summary="Pick the right visual; title, label, caption, and refer to it.")

# ================================================================= Week 4 · Synthesize sources in writing (The Voyage)
L13 = Lesson("6.13", "Starting a Research Project",
    "I can choose a research question and find sources to answer it.", "W.4.7",
    [("research question", "A question you investigate by gathering information.")],
    "What is something about ships, the sea, or the 1700s that you've wondered about?",
    [ReaderAssign(TI, "Informational selection: The Voyage", "Take notes on facts about long ocean voyages."),
     Text("Good research questions are specific and can't be answered with yes or no. <i>What were ships like?</i> is too broad. <i>How did sailors stay healthy on long voyages?</i> is focused."),
     Figure(lambda t: table(t, [["Too broad", "Focused"], ["Tell about the ocean.", "How do whales communicate?"], ["Pirates", "How did pirate crews make decisions?"], ["Ships", "How did sailors navigate without GPS?"]],
                            [2.6 * inch, 2.8 * inch], width=5.4 * inch)),
     KeyIdea("Ask a focused question, then find two or three reliable sources.")],
    [Problem("Broad or focused: “Animals”", "broad"), Problem("Broad or focused: “How do sea turtles find the beach where they hatched?”", "focused"), Problem("How many sources should you use?", "two or three (at least two)")],
    [S("Warm-Up", [SA("A research question should be…", "focused"), SA("Can it be answered with yes or no?", "No")], cols=2),
     S("Plan", [OR("Write your research question about ships, the sea, or life in the 1700s.", "Answers vary.", lines=2),
                OR("List two or three sources you could use (texts in this book, the Reader, library books, reliable websites). Use the Lesson 6.3 questions.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Why is your question focused enough?", "Answers vary.", lines=2)])],
    te("Students choose research questions.", "Conduct short research projects that build knowledge.", "Treasure Island Reader (The Voyage), library books, workbook Lesson 6.13",
       "What do you wonder?", "Read “The Voyage.”", ["Teach broad vs focused."], "Your Turn 1–3.",
       ["Questions too broad."], ["Narrow with who/how/why."], ["Interview an expert."]),
    summary="Focused research questions and reliable sources.")

L14 = Lesson("6.14", "Organizing Research Notes",
    "I can sort my notes into categories that will become paragraphs.", "W.4.8, W.4.2a",
    [("category", "A group of related facts.")],
    "If you had twenty notes, how would you organize them?",
    [Text("Sort notes into two or three <b>categories</b>. Each category becomes a body paragraph. Give each category a heading."),
     Example("Sort notes", "Question: How did sailors stay healthy on long voyages?", ["Category 1: Food and water (rainwater, limes, salted meat).", "Category 2: Illness (scurvy, fever, crowded spaces).", "Category 3: Solutions (citrus fruit, fresh air)."],
             "Three categories = three body paragraphs."),
     KeyIdea("Group notes into categories; each category becomes a paragraph.")],
    [Problem("What does each category become?", "a body paragraph"), Problem("How many categories?", "two or three"), Problem("Category for “limes prevented scurvy”", "solutions (or food)")],
    [S("Warm-Up", [SA("A category is…", "a group of related facts"), SA("Each category becomes…", "a paragraph")], cols=2),
     S("Organize", [OR("Write at least six notes for your research question (with sources).", "Answers vary.", lines=7), OR("Sort them into two or three categories with headings.", "Answers vary.", lines=6)])],
    te("Students organize notes into categories.", "Gather information, take notes, and categorize it.", "Notes, workbook Lesson 6.14",
       "Twenty notes.", "Gather notes from sources.", ["Model sorting."], "Sort notes.",
       ["Categories that overlap."], ["Color-code notes."], ["Add a fourth category."], independent="Finish notes and categories."),
    summary="Sort notes into categories for paragraphs.")

L15 = Lesson("6.15", "Drafting a Research Report",
    "I can draft a short research report from my notes and list my sources.", "W.4.2, W.4.7, W.4.8",
    [("bibliography", "A list of the sources used in a report.")],
    "How does a research report sound different from a story?",
    [Text("A research report has an introduction that states the topic and question, body paragraphs (one per category) with facts in your own words, a conclusion, and a <b>source list</b>."),
     Example("Source list", "How to list a source", ["Book: Author. <i>Title</i>. Year.", "Article in this book: “Title.” <i>Grade 4 ELA Textbook</i>, Lesson number.", "Website: “Page Title.” Website name. Date you used it."],
             "Example: “From Sail to Steam.” Grade 4 ELA Textbook, Lesson 6.2."),
     KeyIdea("Introduction, body paragraphs by category, conclusion, source list. Use your own words.")],
    [Problem("What goes at the end of a report?", "a source list (bibliography)"), Problem("How many body paragraphs?", "one per category"), Problem("Can you copy sentences from sources?", "No; use your own words.")],
    [S("Warm-Up", [SA("A bibliography is…", "a source list"), SA("A report's facts should be in…", "your own words")], cols=2),
     S("Draft", [OR("Draft your research report.", "Answers vary.", lines=22, note="Look for: introduction with topic/question; body paragraphs by category; facts in own words; conclusion."),
                 OR("Source list:", "Answers vary.", lines=4)])],
    te("Students draft research reports.", "Write informative texts; conduct short research; provide a list of sources.", "Notes, workbook Lesson 6.15",
       "Report vs story.", "Review notes.", ["Model an introduction and source list."], "Draft.",
       ["No source list."], ["Paragraph frames."], ["Add a visual from Lesson 6.12."], independent="Finish the draft."),
    summary="Introduction, category paragraphs, conclusion, sources.")

L16 = Lesson("6.16", "Revising and Presenting Research",
    "I can revise my report and present it to an audience.", "W.4.5, SL.4.4",
    [],
    "How can you share your research so others learn from it?",
    [Figure(lambda t: table(t, [["Report checklist", "✓"], ["My introduction states the topic and question.", ""], ["Each paragraph has one category of facts.", ""], ["Facts are in my own words.", ""],
                                ["I included a visual with a caption.", ""], ["My conclusion answers the research question.", ""], ["My source list is complete.", ""], ["I edited capitals, punctuation, and spelling.", ""]],
                            [W * 0.8, W * 0.12], width=W * 0.92)),
     KeyIdea("Revise with the checklist, then present clearly with your visual.")],
    [Problem("What should the conclusion do?", "answer the research question"), Problem("Name a presentation skill.", "eye contact, clear voice, steady pace"), Problem("What should you show during the talk?", "your visual")],
    [S("Warm-Up", [SA("Conclusion answers the…", "research question"), SA("Present with a…", "visual")], cols=2),
     S("Revise and Present", [OR("List two revisions you made.", "Answers vary.", lines=3), OR("Present your report. Ask your audience one question afterward. What did they ask you?", "Answers vary.", lines=2)]),
     S("Exit Ticket", [OR("What was the most interesting thing you learned in your research?", "Answers vary.", lines=2)])],
    te("Students revise and present research.", "Revise writing; report on a topic with facts and details; speak clearly.", "Drafts, workbook Lesson 6.16, Unit 6 Review",
       "Sharing research.", "Read the checklist.", ["Model a 1-minute presentation."], "Revise.",
       ["Reading the report word for word."], ["Note cards."], ["Present to grandparents by video call."], independent="Revise and present; then the Unit 6 Review.", exit_="Exit Ticket. Tomorrow: Unit 6 Test."),
    summary="Revise with a checklist; present clearly with a visual.")

# ================================================================= checks
C1 = Check("Weekly Check 16: Sources", [S("Read Source A", [], passage=P_C16A), S("Read Source B, then answer", [
    MC("Source A is a…", ["primary source", "secondary source"], 0),
    OR("How do you know?", "It's a diary written at the time by someone on the trail.", lines=1),
    OR("Write one fact Source B gives that Source A doesn't.", "e.g. 2,000 miles; four to six months; hundreds of thousands of travelers", lines=2),
    OR("What do both sources show about river crossings?", "They were dangerous (wagon nearly tipped; among the most dangerous parts).", lines=2),
    OR("Take a note from Source B in your own words with the source.", "e.g. Trail 2,000 mi, 4–6 months; most walked (The Oregon Trail).", lines=2)], passage=P_C16B)], minutes=20)

C2 = Check("Weekly Check 17: Reasons and Evidence", [S("Read and answer", [
    OR("What is the author's claim?", "Our town should build a dog park.", lines=1),
    OR("List the two reasons.", "Dogs need exercise; dog parks bring people together.", lines=2),
    OR("Which piece of evidence is strongest? Why?", "The study showing fewer loose dogs; it's a fact from research.", lines=2),
    OR("Which piece of evidence is weakest? Why?", "“Everyone loves dogs”: an exaggeration and opinion.", lines=2),
    OR("Suggest one piece of stronger evidence for Reason 2.", "e.g. a survey of neighbors at an existing park", lines=1)], passage=P_C17)], minutes=20)

C3 = Check("Weekly Check 18: Visual Information", [S("Use the graph and answer", [
    Problem("Which month had the most visitors?", "July", fig=lambda t: bar_graph(t, ["May", "Jun", "Jul", "Aug"], [300, 550, 700, 450], title="Lighthouse Museum Visitors", ylabel="visitors", step=100, width=W * 0.7, height=170), space=0, wide=True),
    SA("About how many visitors in June?", "550"), SA("How many more in July than in May?", "400"),
    OR("What pattern does the graph show?", "Visitors increased through July, then dropped in August.", lines=2),
    OR("Write a caption for the graph.", "e.g. The museum was busiest in midsummer.", lines=1)], cols=1)], minutes=20)

REVIEW = Check("Unit 6 Review", [
    S("Skills", [SA("Primary or secondary: a letter from 1850", "primary"), SA("A claim is…", "the main opinion"), SA("Evidence answers…", "how do you know?"),
                 SA("What does a map key do?", "explains symbols"), SA("Visual for parts of something", "labeled diagram"), SA("A bibliography is…", "a source list")], cols=2),
    S("Apply", [OR("Is this strong evidence? “Our class should get a fish tank because fish are pretty.” Explain and improve it.", "Weak opinion; e.g. caring for fish teaches responsibility, according to our science teacher.", lines=3),
                OR("Write a focused research question about bees.", "e.g. How do bees communicate where flowers are?", lines=1)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 6 Test", [
    S("Part A · Information and features (1 point each)", [
        OR("What is pollination?", "Bees carry pollen from flower to flower, helping plants make fruits and seeds.", lines=2),
        OR("Under which heading would you find ways to help bees?", "How You Can Help", lines=1),
        OR("What evidence shows bees matter to people's food?", "About one in three bites depends on pollinators; apples, almonds, blueberries, cucumbers.", lines=2),
        OR("List two causes of the drop in honeybee colonies.", "loss of wildflowers, harmful chemicals, diseases", lines=1),
        MC("This text is a…", ["primary source", "secondary source"], 1)], passage=P_TEST),
    S("Part B · Reasons and evidence (1 point each)", [
        OR("The author claims people can help bees. What evidence or examples support this?", "planting flowers, avoiding chemicals, leaving wild areas; even one pot of flowers helps", lines=2),
        OR("What visual could the author add, and why?", "e.g. a bar graph of colonies over time; a diagram of pollination", lines=2),
        OR("Write one note from the text in your own words with the source.", "e.g. 1 in 3 bites depend on pollinators (Why Bees Matter).", lines=2)]),
    S("Part C · Opinion writing (6 points)", [OR("Should every family plant flowers for bees? Write an opinion paragraph with a clear opinion, two reasons with evidence from the text, linking words, and a conclusion.",
                                                 "Rubric: opinion (1); reason 1 + evidence (1); reason 2 + evidence (1); explanation (1); linking words (1); conclusion (1).", lines=14, points=6)])],
    kind="test", minutes=45, rubric=[["12–14 (85%+)", "Mastered."], ["10–11", "Proficient; review missed skills."], ["Below 10", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-03-29", "2027-04-05", "2027-04-12", "2027-04-19"], CHECKS, REVIEW, TEST)

UNIT = Unit(6, "Sources and Evidence", "Primary and secondary sources, reasons and evidence, opinion writing, diagrams, maps, graphs, and a short research report, with Treasure Island Chapters 8–9.",
    "Jim Hawkins's adventure ends, but yours as a researcher begins. You'll compare sources, judge which ones to trust, weigh reasons and evidence, read diagrams, maps, and graphs, and write both an opinion piece and your own short research report.",
    ["Compare primary and secondary sources and judge reliability.", "Identify and evaluate claims, reasons, and evidence.", "Write an opinion piece with reasons, evidence, linking words, and a conclusion.",
     "Use and create diagrams, maps, and graphs.", "Research a focused question, organize notes, and write a report with sources."],
    [("RI.4.6, RI.4.9", "Compare accounts; integrate information from two texts."), ("RI.4.7", "Interpret visual information."), ("RI.4.8", "Explain how authors use reasons and evidence."),
     ("W.4.1", "Write opinion pieces."), ("W.4.2, W.4.7, W.4.8", "Write informative texts; conduct short research; take notes; list sources."), ("SL.4.4", "Report on a topic.")],
    [("primary source", "Created at the time by someone who was there."), ("secondary source", "Written later to explain."), ("claim", "The main opinion."), ("evidence", "Facts that support a reason."),
     ("bibliography", "A list of sources.")],
    ["Unit 5: comparing texts and essays."], ["Treasure Island Reader (Chapters 8–9, The Schooner, The Voyage)", "Library books or approved websites", "Note cards, colored pencils"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Every day you see claims online and in ads. Knowing how to check sources and evidence helps you decide what to believe.",
    family_note="When you see a claim in an ad or online, ask together: Who said it? What's the evidence? Do other sources agree?",
    weeks=WEEKS)
