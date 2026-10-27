"""Grade 4 ELA · Unit 2: Reading Closely — text evidence, inference, theme and main idea, and summary.
Anchor reading: King Arthur and the Round Table Reader, Chapters 5–8 (Nov 9 – Dec 11, 2026)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule
from content.ela4.unit01 import S, MC, OR, SA, READER

# ================================================================= passages (original)
P_CHIVALRY = Passage("The Code of Chivalry", [
    "In the Middle Ages, knights were expected to follow a set of rules called the <b>code of chivalry</b>. The code told knights how to behave in battle and in everyday life.",
    "First, a knight was supposed to be loyal. He promised to serve his lord and protect the people who lived on his lord's land. Breaking that promise was one of the worst things a knight could do.",
    "Second, a knight was expected to be brave. He had to face danger instead of running away, even when he was afraid.",
    "Third, a knight was supposed to show courtesy, or good manners. He was to be polite to everyone and to protect people who could not protect themselves, such as children and the poor.",
    "Not every knight followed the code. Some were greedy or cruel. Still, the code of chivalry gave people an idea of what a good knight should be, and that idea lives on in stories such as the legends of King Arthur.",
], source="An original informational text", genre="Informational text")

P_BREAD = Passage("The Missing Bread", [
    "When Grandma came into the kitchen, the loaf of bread she had left cooling on the counter was gone. Only a few crumbs were left on the plate.",
    "She looked around. The back door was open a crack. On the floor, a trail of tiny crumbs led toward it. Next to the door was a muddy paw print, about the size of a coin.",
    "Grandma followed the trail outside. Under the porch, she heard a soft crunching sound. She knelt down and peeked. Two shiny eyes blinked back at her, and a fluffy striped tail swished.",
    "Grandma laughed. “Well,” she said, “I guess I'll be baking another loaf.”",
], source="An original story", genre="Realistic fiction")

P_RECITAL = Passage("Mira's Recital", [
    "Mira sat on the edge of her chair backstage, twisting the hem of her dress. Every few seconds she peeked through the curtain at the rows of people. Her stomach felt like it was full of butterflies.",
    "When her name was called, she walked slowly to the piano. Her fingers trembled above the keys. She took a deep breath, closed her eyes for a moment, and began to play.",
    "The first notes were shaky, but soon the music flowed. By the last chord, Mira was smiling. When the audience clapped, she bowed so low her braid almost touched the floor.",
    "Backstage, her teacher hugged her. “I knew you could do it,” he said. Mira grinned. “Can I play two songs next year?”",
], source="An original story", genre="Realistic fiction")

P_BEES = Passage("Honeybees in Winter", [
    "Many insects die or sleep through the winter, but honeybees stay busy. When the weather turns cold, the bees gather in a tight ball inside their hive called a <b>winter cluster</b>.",
    "Bees in the center of the cluster shiver their wing muscles without flapping their wings. This shivering makes heat. The bees take turns moving from the cold outside of the cluster to the warm center.",
    "All winter, the bees eat honey they stored during the summer. A strong hive may eat 50 pounds of honey before spring. Beekeepers who take too much honey in the fall may find an empty hive when the flowers bloom again.",
], source="An original informational text", genre="Informational text")

P_ANTS = Passage("The Grasshopper and the Ants", [
    "All summer long, a grasshopper played his fiddle in the warm grass. Nearby, a line of ants marched back and forth, carrying seeds to their nest.",
    "“Why work so hard?” laughed the grasshopper. “Come and sing with me! There is plenty of food everywhere.”",
    "“We are storing food for the winter,” said one ant, never putting down her seed. “You should do the same.”",
    "The grasshopper only played louder. Then winter came. Snow covered the grass, and the grasshopper could find nothing to eat. Shivering and hungry, he knocked at the ants' door.",
    "The ants shared a little food with him, and the grasshopper said, “Next summer, I will play <i>and</i> work.”",
], source="An original retelling of an Aesop fable", genre="Fable")

P_GARDENS = Passage("The Two Gardens", [
    "Ruby and her neighbor Sam each planted a garden in the spring. Sam bought the biggest plants at the store and put them in the ground all at once. Ruby planted tiny seeds and watered them every morning.",
    "In May, Sam's garden looked wonderful, and Ruby's looked like a patch of dirt. Sam teased her. “Your garden is invisible!”",
    "But Sam forgot to water. By July, his plants were brown and drooping. Meanwhile, Ruby's seeds had grown into tall tomato vines and bright zinnias.",
    "In August, Ruby brought Sam a basket of tomatoes. “Maybe next year,” he said with an embarrassed smile, “you can teach me how to garden.”",
], source="An original story", genre="Realistic fiction")

P_LEAVES = Passage("Why Leaves Change Color", [
    "Every fall, trees in many parts of the country turn red, orange, and gold. The colors are not new. Many of them were inside the leaves all along.",
    "During spring and summer, leaves are full of a green chemical called <b>chlorophyll</b>. Chlorophyll helps the tree use sunlight to make food. There is so much of it that it hides the other colors.",
    "When days get shorter and cooler, the tree stops making chlorophyll. As the green fades, yellow and orange colors that were hidden begin to show. Some trees, like maples, also make new red colors in the fall.",
    "Finally, the leaves dry up and fall. The tree rests through the winter and grows new green leaves in the spring.",
], source="An original informational text", genre="Informational text")

P_LIGHTHOUSE = Passage("The Lighthouse Keeper's Daughter", [
    "Nell lived with her father in a lighthouse on a rocky island. Every night, her father climbed the tower to light the great lamp that warned ships away from the rocks.",
    "One stormy night, her father slipped on the wet stairs and hurt his ankle. He could not climb. Through the window, Nell saw the lights of a fishing boat heading straight for the rocks.",
    "Nell grabbed the lantern and climbed the hundred winding stairs. The wind shook the tower, and rain lashed the glass. With trembling hands, she lit the great lamp. Its beam swept across the dark water.",
    "The fishing boat turned just in time. The next morning, the fishermen rowed to the island to thank the brave girl who had saved their lives.",
], source="An original story", genre="Historical fiction")

P_PRESS = Passage("The Printing Press", [
    "Before the 1450s, books in Europe were copied by hand. A single book could take a monk months to finish, so books were rare and very expensive.",
    "Around 1450, a German metalworker named Johannes Gutenberg built a printing press with metal letters that could be moved and reused. Workers arranged the letters, inked them, and pressed paper on top. They could print hundreds of pages a day.",
    "Books became cheaper, and more people learned to read. Ideas about science, religion, and government spread quickly from city to city.",
    "Today, historians call the printing press one of the most important inventions in history.",
], source="An original informational text", genre="Informational text")

P_C4 = Passage("Pigeons with a Job", [
    "For thousands of years, people have used homing pigeons to carry messages. A homing pigeon can find its way back to its home from hundreds of miles away.",
    "During wars, pigeons carried notes when other ways of sending messages did not work. One famous pigeon, Cher Ami, delivered a message in 1918 that helped save almost 200 soldiers, even though she had been injured.",
    "Scientists are still not completely sure how pigeons find their way. Some think the birds use the sun. Others think they can sense the earth's magnetic field, like a built-in compass.",
], source="An original informational text", genre="Informational text")

P_C5 = Passage("The New Kid", [
    "Jamal stood at the edge of the playground, his hands stuffed in his pockets. He watched a group of kids playing soccer. Every time the ball rolled near him, he took a step forward, then stopped.",
    "A girl with a ponytail jogged over. “We need one more player,” she said. “Want to be on my team?”",
    "Jamal's face lit up. He pulled his hands out of his pockets and ran onto the field so fast he almost tripped.",
], source="An original story", genre="Realistic fiction")

P_C6 = Passage("The Lion and the Mouse", [
    "A tiny mouse ran across a sleeping lion's paw. The lion woke and trapped the mouse. “Please let me go,” squeaked the mouse. “Someday I may help you.” The lion laughed at the idea, but he let the mouse go.",
    "Weeks later, the lion was caught in a hunter's net. He roared, but he could not get free. The mouse heard him, ran over, and chewed through the ropes until the lion was free.",
    "“You laughed at me,” said the mouse, “but even a little friend can be a big help.”",
], source="An original retelling of an Aesop fable", genre="Fable")

P_TEST = Passage("The Bridge at Millbrook", [
    "The old wooden bridge at Millbrook had stood for a hundred years. Every morning, farmers drove their wagons across it to sell vegetables in town, and children ran across it on their way to school.",
    "One spring, after a week of heavy rain, the river rose higher than anyone could remember. Muddy water crashed against the bridge's legs. Ten-year-old Ada noticed that the middle of the bridge was sagging, and one of the wooden posts had cracked.",
    "Ada knew the morning wagons would come soon. She ran to the mayor's house, but no one answered. Without wasting another minute, she dragged her family's old red blanket to the end of the bridge and tied it to the railing like a flag. Then she stood beside it, waving her arms.",
    "When the first farmer arrived, he grumbled at being stopped. But when he saw the cracked post, his face went pale. Minutes later, with a loud groan, the middle of the bridge fell into the river.",
    "The town built a new stone bridge that summer. On the first day it opened, the mayor tied a red ribbon across it. Instead of cutting it himself, he handed the scissors to Ada.",
], source="An original story", genre="Historical fiction")


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


# ================================================================= Week 1 · Find text evidence (Chapter 5)
L1 = Lesson("2.1", "Text Evidence: Quoting and Paraphrasing",
    "I can support my answers by quoting or paraphrasing the text.", "RL.4.1",
    [("text evidence", "Words or details from a text that support an answer."), ("quote", "Copy the author's exact words inside quotation marks."),
     ("paraphrase", "Retell the author's idea in your own words.")],
    "Your friend says the Round Table was special. How could you prove it using the book?",
    [ReaderAssign(READER, "Chapter 5: The Marriage of Arthur and the Founding of the Round Table", "Look for details that explain why the Round Table was important."),
     Text("When you answer a question about a text, you need <b>text evidence</b>. You can <b>quote</b> (use the exact words in quotation marks) or <b>paraphrase</b> (put the idea in your own words). Either way, the evidence must come from the text."),
     Figure(lambda t: table(t, [["Quote", "Paraphrase"], ["Copies the exact words", "Uses your own words"], ["Needs quotation marks", "No quotation marks"],
                                ["Best for a word or line that matters", "Best for a longer idea or event"]], [W * 0.46, W * 0.46], width=W * 0.92)),
     Example("Quote and paraphrase", "Why was the table round?",
             ["Find the part of Chapter 5 that explains the shape.", "Paraphrase: A round table has no head, so no knight sat in a more important seat than another.", "Add the source: “In Chapter 5…”"],
             "In Chapter 5, the table is round so that no knight is more important than another; everyone sits as an equal."),
     KeyIdea("Every answer needs proof. Quote exact words with quotation marks, or paraphrase in your own words, and tell where the evidence came from.")],
    [Problem("What is the difference between a quote and a paraphrase?", "A quote copies exact words in quotation marks; a paraphrase uses your own words."),
     Problem("Paraphrase: “The knights vowed to protect the weak and to be true to the king.”", "e.g. The knights promised to help people who couldn't protect themselves and to stay loyal to Arthur."),
     Problem("Name one event from Chapter 5.", "Answers vary: Arthur marries Guinevere; the Round Table is founded; knights take their places.")],
    [S("Warm-Up", [SA("What is text evidence?", "details from a text that support an answer"), SA("What punctuation does a quote need?", "quotation marks")], cols=2),
     S("Quote or Paraphrase?", [SA(q, a) for q, a in [("“The table could seat many knights.”", "quote"), ("The author says lots of knights could sit there.", "paraphrase"),
                                                       ("Arthur wanted his knights to be equal.", "paraphrase"), ("“No seat was higher than another.”", "quote")]], cols=2),
     S("Read and Respond: Chapter 5", [
         OR("Why was the Round Table important? Support your answer with a paraphrase from Chapter 5.", "So all knights were equal; no seat was more important. Evidence from the chapter.", lines=4,
            note="Accept supported answers; evidence must come from Chapter 5."),
         OR("Copy one sentence from Chapter 5 that tells something about Guinevere or the wedding. Use quotation marks.", "Answers vary; must be an exact quote in quotation marks.", lines=3)]),
     S("Exit Ticket", [OR("Paraphrase this sentence: “The knight rode swiftly through the dark forest, afraid of what waited ahead.”", "e.g. The knight hurried through the forest because he was scared of what was coming.", lines=2)])],
    te("Students quote and paraphrase text evidence.", "Refer to details and examples in a text when explaining what it says and when drawing inferences.", "King Arthur Reader (Chapter 5), workbook Lesson 2.1",
       "Ask: How could you prove the Round Table was special?", "Read Chapter 5 together.", ["Teach quote vs paraphrase.", "Say: An answer without proof is only an opinion.", "Model the round-table example."], "Your Turn 1–3.",
       ["Quoting without quotation marks.", "Paraphrasing by changing one word."], ["Cover the text, then retell it aloud before writing."], ["Find the strongest quote in the chapter and defend your choice."]),
    summary="Support answers with evidence: quote exact words or paraphrase in your own words.")

L2 = Lesson("2.2", "Text Evidence in Informational Text",
    "I can find details in an informational text that answer a question.", "RI.4.1",
    [("informational text", "Writing that gives facts about a real topic."), ("detail", "A fact or example that supports a bigger idea.")],
    "If someone asked, “What were knights supposed to be like?”, where would you look for the answer?",
    [Text("In informational text, the answer to a question is often spread across several paragraphs. Look for <b>key words</b> from the question, then read the sentences around them."),
     P_CHIVALRY,
     Example("Find the evidence", "What did the code say about people who could not protect themselves?", ["Key words: protect themselves.", "Find them in paragraph 4.", "Paraphrase the detail."],
             "Knights were supposed to protect people who could not protect themselves, such as children and the poor (paragraph 4)."),
     KeyIdea("Find key words from the question in the text. Use the paragraph number to show where your evidence is.")],
    [Problem("What three things did the code expect of knights?", "to be loyal, brave, and courteous (paragraphs 2–4)"), Problem("Did every knight follow the code? Give evidence.", "No; paragraph 5 says some were greedy or cruel."),
     Problem("What does <i>courtesy</i> mean? Which paragraph?", "good manners; paragraph 4")],
    [S("Warm-Up", [SA("Is the passage fiction or informational?", "informational"), SA("What is a detail?", "a fact or example that supports an idea")], cols=2),
     S("Find the Evidence", [
         OR("According to paragraph 2, what was one of the worst things a knight could do?", "break his promise of loyalty to his lord", lines=2),
         OR("What did bravery mean for a knight? Quote the text.", "“He had to face danger instead of running away, even when he was afraid.”", lines=2),
         MC("Which sentence BEST supports the idea that the code still matters today?", ["“Some were greedy or cruel.”", "“That idea lives on in stories such as the legends of King Arthur.”", "“First, a knight was supposed to be loyal.”"], 1)],
       passage=P_CHIVALRY),
     S("Think Deeper", [OR("Which rule of chivalry do you think is most important today? Use evidence from the passage and your own reasons.", "Answers vary; must cite the passage.", lines=4)]),
     S("Exit Ticket", [OR("Which knight in Chapter 5 shows one part of the code? Give one detail.", "Answers vary.", lines=2)])],
    te("Students find evidence in informational text.", "Refer to details and examples in a text when explaining what it says explicitly.", "Workbook Lesson 2.2",
       "Ask: Where would you look?", "Read “The Code of Chivalry.”", ["Teach key-word searching.", "Model the protection question."], "Your Turn 1–3.",
       ["Answering from memory instead of the text."], ["Highlight key words in the question and the text."], ["Write a modern “code” for your family."]),
    summary="Use key words to find evidence; cite the paragraph.")

L3 = Lesson("2.3", "Choosing the Best Evidence",
    "I can choose the evidence that best supports an answer.", "RL.4.1, RI.4.1",
    [("relevant", "Connected to the question."), ("strongest evidence", "The detail that most clearly proves the answer.")],
    "Two details are both true. How do you decide which one proves your point better?",
    [Text("Not all evidence is equally strong. The best evidence is <b>relevant</b> (it is about the question) and <b>specific</b> (it clearly proves the answer). Weak evidence is true but doesn't really prove the point."),
     Example("Compare evidence", "Claim: The ants in a fable are hardworking. Which evidence is strongest?",
             ["A. The ants lived in a nest. (true, but not about working)", "B. The ants marched back and forth all summer carrying seeds. (shows hard work)", "C. The ants shared food. (shows kindness, not hard work)"], "B is the strongest evidence."),
     KeyIdea("Ask: Does this detail prove my answer, or is it just true? Choose the most specific, relevant detail.")],
    [Problem("Claim: Merlin is wise. Strong or weak? “Merlin had a long beard.”", "weak"), Problem("Claim: Merlin is wise. Strong or weak? “Merlin knew what would happen before it happened.”", "strong"),
     Problem("Why is the first detail weak?", "A long beard doesn't prove someone is wise.")],
    [S("Warm-Up", [SA("What does <i>relevant</i> mean?", "connected to the question"), SA("Is every true detail strong evidence?", "No")], cols=2),
     S("Strongest Evidence", [
         MC("Claim: The knights in the code of chivalry were expected to be polite. Strongest evidence:", ["“Knights were expected to follow a set of rules.”", "“He was to be polite to everyone.”", "“Breaking that promise was one of the worst things.”"], 1),
         MC("Claim: Honeybees work together in winter. Strongest evidence:", ["“Many insects die or sleep through the winter.”", "“The bees take turns moving from the cold outside of the cluster to the warm center.”", "“A strong hive may eat 50 pounds of honey.”"], 1),
         MC("Claim: Mira grows more confident during the recital. Strongest evidence:", ["“Her fingers trembled.”", "“By the last chord, Mira was smiling.”", "“Mira sat on the edge of her chair.”"], 1)]),
     S("Your Evidence", [OR("Claim: Arthur is a good king. Write the strongest piece of evidence you can find in Chapter 5, and explain why it is strong.", "Answers vary; evidence should directly show good leadership.", lines=4)]),
     S("Exit Ticket", [OR("Explain the difference between true evidence and strong evidence.", "Strong evidence clearly proves the claim; true evidence may be unrelated.", lines=2)])],
    te("Students choose the strongest evidence.", "Refer to details and examples when explaining what a text says.", "Workbook Lesson 2.3",
       "Two true details: which proves more?", "Reread part of Chapter 5.", ["Teach relevant and specific.", "Model the ant evidence."], "Your Turn 1–3.",
       ["Choosing the first detail they find."], ["Ask: Does this prove it?"], ["Debate the strongest evidence with a sibling."]),
    summary="The best evidence is relevant and specific: it clearly proves the answer.")

L4 = Lesson("2.4", "Writing with Evidence: The ACE Paragraph",
    "I can write a paragraph that answers a question and supports it with evidence.", "W.4.9, W.4.1b",
    [("ACE", "Answer the question, Cite evidence, Explain how the evidence supports your answer.")],
    "What makes an answer in writing convincing?",
    [Text("A strong written response follows <b>ACE</b>: <b>A</b>nswer the question in a complete sentence, <b>C</b>ite evidence from the text, and <b>E</b>xplain how the evidence proves your answer."),
     Figure(lambda t: table(t, [["Step", "Sentence starters"], ["Answer", "I think… / The answer is… / In Chapter 5, …"], ["Cite", "The text says, “…” / In paragraph 3, the author explains… / For example, …"],
                                ["Explain", "This shows that… / This proves… / This means…"]], [1.0 * inch, W - 1.2 * inch], width=W - 0.2 * inch)),
     Example("An ACE paragraph", "Question: Why did knights follow the code of chivalry?",
             ["Answer: Knights followed the code because it told them how a good knight should act.", "Cite: The passage says the code “told knights how to behave in battle and in everyday life.”", "Explain: This shows that the code was a guide that helped knights know what was right."],
             "Knights followed the code because it told them how a good knight should act. The passage says the code “told knights how to behave in battle and in everyday life.” This shows the code was a guide for doing what was right."),
     KeyIdea("Answer, Cite, Explain. The Explain sentence connects the evidence to your answer.")],
    [Problem("What does the C in ACE stand for?", "Cite evidence"), Problem("Write an Explain starter.", "This shows that…"), Problem("Why do you need the Explain step?", "It tells how the evidence proves the answer.")],
    [S("Warm-Up", [SA("A in ACE", "Answer"), SA("E in ACE", "Explain")], cols=2),
     S("Label the Parts", [OR("Label each sentence A, C, or E: (1) “This shows Mira was scared at first.” (2) “Mira was nervous before she played.” (3) “Her fingers trembled above the keys.”", "1 = E, 2 = A, 3 = C", lines=1)]),
     S("Write an ACE Paragraph", [OR("How did the Round Table show that Arthur wanted his knights to be equal? Write an ACE paragraph using Chapter 5.", "Answers vary; must include an answer, evidence from Chapter 5, and an explanation.", lines=8,
                                     note="Score 1 point each for A, C, and E; 1 point for clear, complete sentences.")]),
     S("Exit Ticket", [OR("Check your paragraph. Underline your Answer, put a box around your Citation, and circle your Explanation.", "Student self-check.", lines=1)])],
    te("Students write ACE paragraphs.", "Draw evidence from literary or informational texts to support analysis; provide reasons supported by facts and details.", "Workbook Lesson 2.4",
       "What makes writing convincing?", "Reread the code passage.", ["Teach ACE with the starters chart.", "Model the chivalry paragraph."], "Label the Mira sentences together.",
       ["Skipping the Explain step.", "Citing evidence that doesn't fit."], ["Use sentence starters."], ["Write an ACE paragraph about a different question."], independent="Write the ACE paragraph."),
    summary="ACE: Answer, Cite evidence, Explain.")

# ================================================================= Week 2 · Make supported inferences (Chapter 6)
L5 = Lesson("2.5", "Making Inferences",
    "I can make an inference by combining text clues with what I already know.", "RL.4.1",
    [("inference", "A smart guess based on clues in the text and what you already know."), ("clue", "A detail that hints at something the author doesn't say directly.")],
    "Your friend walks in with a wet umbrella and muddy boots. What can you figure out without asking?",
    [ReaderAssign(READER, "Chapter 6: Sir Lancelot", "What does the author show about Lancelot without saying it directly?"),
     Text("Authors don't tell readers everything. Readers make <b>inferences</b>: <i>Text clues + What I know = Inference.</i>"),
     P_BREAD,
     Example("Make an inference", "Who took the bread?", ["Clues: crumbs lead to the door; a small paw print; a fluffy striped tail under the porch.", "What I know: raccoons have striped tails and steal food.", "Inference: an animal, probably a raccoon, took the bread."],
             "A raccoon took the bread. The striped tail, the small paw print, and the crumb trail are the clues."),
     KeyIdea("Text clues + what I know = inference. An inference must be supported by clues.")],
    [Problem("How does Grandma feel at the end? What clue tells you?", "amused, not angry; she laughs"), Problem("What did the animal use to get in?", "the back door that was open a crack"),
     Problem("What will Grandma do next?", "bake another loaf")],
    [S("Warm-Up", [SA("Text clues + ___ = inference", "what I know"), SA("Is an inference a wild guess?", "No, it's based on clues")], cols=2),
     S("Infer", [OR(q, a, lines=2) for q, a in [("Sam yawned, rubbed his eyes, and put his head on his desk. How does Sam feel?", "tired; clues: yawned, rubbed eyes, head down"),
                                                 ("The crowd groaned when the ball rolled out of bounds. How did the crowd feel?", "disappointed"),
                                                 ("Lena put on her coat, hat, and two pairs of mittens before going out. What is the weather like?", "very cold")]]),
     S("Use the Passage", [OR("Find two clues that the thief was small. What do they tell you?", "small paw print the size of a coin; hid under the porch; it was a small animal", lines=3)], passage=P_BREAD),
     S("Exit Ticket", [OR("Make one inference about Lancelot from Chapter 6. Write the clue that supports it.", "Answers vary; must include a supporting clue.", lines=2)])],
    te("Students make inferences from clues.", "Draw inferences from the text, referring to details.", "King Arthur Reader (Chapter 6), workbook Lesson 2.5",
       "The wet umbrella.", ["Read Chapter 6.", "Read “The Missing Bread.”"], ["Teach the inference formula.", "Model the bread mystery."], "Your Turn 1–3.",
       ["Guessing without clues."], ["Use a two-column clue/what-I-know chart."], ["Write your own mystery with clues."]),
    summary="Inference = text clues + what I know.")

L6 = Lesson("2.6", "Inferring Characters' Feelings and Motives",
    "I can infer how characters feel and why they act as they do, using their words and actions.", "RL.4.3, RL.4.1",
    [("motive", "The reason a character does something."), ("trait", "A word that describes what a character is like, such as brave or selfish.")],
    "How can you tell someone is nervous even if they don't say so?",
    [Text("Authors show feelings and motives through what characters <b>say</b>, <b>do</b>, <b>think</b>, and how others react. Look closely at body language and dialogue."),
     P_RECITAL,
     Example("Infer a feeling", "How does Mira feel before she plays?", ["Actions: twists her dress, peeks at the audience.", "Body: butterflies in her stomach, trembling fingers."], "Mira is nervous."),
     Example("Infer a change", "How does Mira feel at the end? Why does she ask to play two songs?", ["She smiles and grins.", "Wanting more shows she enjoyed it."], "Proud and confident; she wants to perform again."),
     KeyIdea("Use what characters say, do, and think to infer feelings, traits, and motives.")],
    [Problem("What does “closed her eyes for a moment” suggest?", "She was calming herself down."), Problem("What trait does Mira show by playing anyway?", "courage, bravery"), Problem("How does her teacher feel? Evidence?", "proud; he hugs her and says “I knew you could do it.”")],
    [S("Warm-Up", [SA("What is a motive?", "the reason for an action"), SA("Name a character trait.", "brave, kind, etc.")], cols=2),
     S("Infer Feelings and Traits", [
         OR("How does Mira feel in paragraph 1? Give two clues.", "nervous; twisting her dress, butterflies, peeking at the audience", lines=2),
         OR("How do Mira's feelings change from beginning to end? Use evidence.", "From nervous to proud and confident; trembling fingers at first, smiling and bowing at the end.", lines=3),
         MC("Why does Mira ask to play two songs next year?", ["She was forced to play.", "She enjoyed performing and feels confident.", "She forgot a song."], 1)], passage=P_RECITAL),
     S("Chapter 6 Connection", [OR("What is one of Lancelot's character traits? What does he do or say that shows it?", "Answers vary, e.g. brave/skilled: he defeats many knights.", lines=3)]),
     S("Exit Ticket", [OR("What is one motive Lancelot has for something he does in Chapter 6?", "Answers vary; supported by the chapter.", lines=2)])],
    te("Students infer characters' feelings, traits, and motives.", "Describe a character in depth, drawing on specific details (thoughts, words, actions).", "Workbook Lesson 2.6",
       "How can you tell someone is nervous?", "Read “Mira's Recital.”", ["Teach say/do/think clues.", "Model Mira's feelings."], "Your Turn 1–3.",
       ["Naming a feeling without evidence."], ["Act out the actions and name the feeling."], ["Trace Lancelot's traits across the chapter."]),
    summary="Characters' words, actions, and thoughts reveal feelings, traits, and motives.")

L7 = Lesson("2.7", "Inferences in Informational Text",
    "I can make inferences from facts in an informational text.", "RI.4.1",
    [("conclude", "Decide something based on evidence.")],
    "If a text says bees eat honey all winter, what can you infer about why they make so much honey in summer?",
    [Text("Informational texts give facts, but readers still make inferences by connecting facts that the author doesn't connect directly."),
     P_BEES,
     Example("Connect facts", "Why might beekeepers who take too much honey find an empty hive?", ["Fact: bees eat stored honey all winter.", "Fact: a hive may eat 50 pounds.", "Connect: without enough honey, the bees starve or leave."],
             "If the beekeeper takes too much honey, the bees won't have enough food for winter and may die."),
     KeyIdea("Connect two or more facts to infer something the author does not say directly.")],
    [Problem("Why do bees take turns in the center?", "so every bee gets to warm up and no bee freezes"), Problem("Infer: Why do bees store honey in summer?", "to have food in winter when there are no flowers"),
     Problem("What can you infer about bees' shivering?", "It uses energy, so they need honey for fuel.")],
    [S("Warm-Up", [SA("What does <i>conclude</i> mean?", "decide using evidence"), SA("Do informational texts need inferences?", "Yes")], cols=2),
     S("Connect the Facts", [
         OR("Paragraph 2 says the bees shiver to make heat. Why don't they flap their wings?", "Flapping would move air and lose heat / they need to stay in the cluster.", lines=2,
            note="Accept reasonable, supported inferences."),
         OR("What can you infer about what happens to a hive that is very small in winter?", "It may not make enough heat and the bees could freeze.", lines=2),
         MC("Which conclusion is best supported by the passage?", ["Bees hate winter.", "Teamwork helps honeybees survive the cold.", "Beekeepers should take all the honey."], 1)], passage=P_BEES),
     S("Exit Ticket", [OR("Write one fact from the passage and one inference you can make from it.", "Answers vary.", lines=2)])],
    te("Students infer from informational text.", "Explain what the text says explicitly and draw inferences.", "Workbook Lesson 2.7",
       "Bee question.", "Read “Honeybees in Winter.”", ["Model connecting facts."], "Your Turn 1–3.",
       ["Stating facts instead of inferences."], ["Use the frame: Because ___ and ___, I can infer ___."], ["Research another animal's winter survival."]),
    summary="Connect facts to infer what the author doesn't state.")

L8 = Lesson("2.8", "Writing to Support an Inference",
    "I can write a paragraph that states an inference and supports it with clues.", "W.4.9a, RL.4.1",
    [],
    "How would you convince someone your inference is right?",
    [Text("When you write about an inference, use ACE: <b>Answer</b> with your inference, <b>Cite</b> at least two clues, and <b>Explain</b> how the clues plus what you know lead to the inference."),
     Example("Inference paragraph", "Question: What kind of worker is Tom in “The Blacksmith's Apprentice” (Lesson 1.5)?",
             ["Answer: Tom is hardworking and takes pride in his work.", "Cite: After a week, “Tom's arms ached and his face was smudged with soot,” but he “felt as proud as a king.”",
              "Explain: Aching arms and soot show how hard he worked, and feeling proud shows he cared about doing the job well."],
             "Tom is hardworking and takes pride in his work. After his first week, his arms ached and his face was covered in soot, yet he felt as proud as a king. His aching arms show how hard he worked, and his pride shows he cared about doing a good job."),
     KeyIdea("An inference paragraph needs at least two clues and an explanation of how they connect.")],
    [Problem("How many clues should an inference paragraph include?", "at least two"), Problem("What goes in the Explain part?", "how the clues and what I know lead to the inference"), Problem("Can an inference be wrong?", "Yes, if the clues don't support it.")],
    [S("Warm-Up", [SA("Clue + know = ?", "inference"), SA("ACE: C =", "Cite")], cols=2),
     S("Write an Inference Paragraph", [OR("What does Lancelot want most in Chapter 6? Write an ACE paragraph with at least two clues from the chapter.", "Answers vary; must include two clues and explanation.", lines=9,
                                         note="1 point each: clear inference; two clues; explanation; complete sentences.")]),
     S("Exit Ticket", [OR("Swap paragraphs with a family member. Write one thing they did well.", "Answers vary.", lines=2)])],
    te("Students write inference paragraphs.", "Draw evidence from texts to support analysis.", "Workbook Lesson 2.8",
       "How to convince someone.", "Reread Chapter 6 sections about Lancelot.", ["Model the Jamal paragraph."], "Plan the Lancelot paragraph together.",
       ["Only one clue."], ["Two-clue organizer."], ["Write about a second character."], independent="Write the paragraph."),
    summary="State the inference, cite two clues, and explain the connection.")

# ================================================================= Week 3 · Central idea and theme (Chapter 7)
L9 = Lesson("2.9", "Theme in Stories",
    "I can determine the theme of a story from the characters' actions and what they learn.", "RL.4.2",
    [("theme", "The message or lesson about life that a story teaches."), ("topic", "What a story is about in one or two words, like friendship.")],
    "What lesson does a story like “The Tortoise and the Hare” teach?",
    [ReaderAssign(READER, "Chapter 7: Sir Tristram", "What lessons about love, loyalty, or choices could this chapter teach?"),
     Text("The <b>theme</b> is the big message about life. It is usually not stated. To find it, ask: <i>What does the main character learn? What happens because of the character's choices?</i> Write the theme as a full sentence."),
     P_ANTS,
     Example("Find the theme", "What is the theme of “The Grasshopper and the Ants”?", ["The grasshopper plays instead of preparing.", "In winter he is hungry; he learns to work.", "Life lesson: preparing for the future matters."],
             "It is wise to prepare today for what you will need tomorrow."),
     WatchOut("A topic is one or two words (hard work). A theme is a sentence about life (Hard work today helps you tomorrow)."),
     KeyIdea("Theme = what the character learns, written as a lesson for everyone.")],
    [Problem("Topic of the fable", "hard work / planning ahead"), Problem("What does the grasshopper learn?", "He should work and prepare, not only play."), Problem("Write another way to say the theme.", "Plan ahead. / Work now so you are ready later.")],
    [S("Warm-Up", [SA("Topic or theme? “friendship”", "topic"), SA("Topic or theme? “True friends help each other.”", "theme")], cols=2),
     S("Use the Fable", [
         OR("How do the ants and the grasshopper act differently in summer? Use evidence.", "Ants carry seeds to store food; the grasshopper plays his fiddle and laughs at them.", lines=3),
         OR("What does the grasshopper's last line show he learned?", "He will balance fun and work, preparing for winter.", lines=2),
         MC("Which is the best theme statement?", ["Grasshoppers play music.", "It is wise to prepare for the future.", "Winter is cold."], 1)], passage=P_ANTS),
     S("Exit Ticket", [OR("What might be a theme of Chapter 7? Give one event that supports it.", "Answers vary, e.g. loyalty can be tested; supported by an event.", lines=3)])],
    te("Students determine theme.", "Determine a theme of a story from details in the text; summarize the text.", "King Arthur Reader (Chapter 7), workbook Lesson 2.9",
       "Tortoise and the Hare lesson.", ["Read Chapter 7.", "Read the fable."], ["Teach topic vs theme.", "Model finding the theme."], "Your Turn 1–3.",
       ["Writing one-word themes.", "Retelling the plot as the theme."], ["Use the frame: The character learns that ___. So the theme is ___."], ["Find the theme of a favorite movie."]),
    summary="Theme is the life lesson; find it in what the character learns.")

L10 = Lesson("2.10", "How Characters Reveal Theme",
    "I can explain how a character's choices and changes reveal the theme.", "RL.4.2, RL.4.3",
    [("conflict", "A problem or struggle in a story."), ("resolution", "How the problem is solved.")],
    "Think of a character who made a mistake and learned from it. How did the mistake teach a lesson?",
    [Text("Themes grow out of <b>conflict</b> and <b>resolution</b>. Notice what a character chooses, what happens because of the choice, and how the character changes."),
     P_GARDENS,
     Example("Trace the theme", "How do Sam's choices reveal the theme?", ["Choice: Sam buys big plants and forgets to water.", "Result: his plants die.", "Change: he asks Ruby to teach him."],
             "Theme: Patience and steady effort pay off more than quick, easy shortcuts."),
     KeyIdea("Choices → results → changes. The lesson the character learns points to the theme.")],
    [Problem("What is the conflict?", "Ruby's garden looks empty and Sam teases her; Sam neglects his garden."), Problem("How is it resolved?", "Ruby's garden grows; she shares tomatoes; Sam asks to learn."), Problem("How does Sam change?", "from teasing and careless to humble and willing to learn")],
    [S("Warm-Up", [SA("What is a conflict?", "a problem or struggle"), SA("What is a resolution?", "how the problem is solved")], cols=2),
     S("Use the Story", [
         OR("What does Ruby do differently from Sam? Give two details.", "plants seeds and waters every morning; Sam buys big plants and forgets to water", lines=3),
         OR("Why does Ruby bring Sam tomatoes instead of teasing him back? What does this show?", "She is kind and forgiving; she doesn't brag.", lines=2),
         OR("Write the theme of “The Two Gardens” and explain how Sam's change shows it.", "Patience and steady effort pay off; Sam's failed garden and request to learn show he learned this.", lines=3)], passage=P_GARDENS),
     S("Exit Ticket", [OR("How does a choice made by a character in Chapter 7 connect to a lesson?", "Answers vary.", lines=2)])],
    te("Students connect characters' choices to theme.", "Determine a theme from details; describe a character in depth.", "Workbook Lesson 2.10",
       "A character who learned.", "Read “The Two Gardens.”", ["Choices → results → changes chart.", "Model Sam."], "Your Turn 1–3.",
       ["Theme statements that only fit this story (“Sam should water his plants”)."], ["Ask: What lesson would help anyone?"], ["Compare the two fables' themes."]),
    summary="A character's choices and changes reveal the theme.")

L11 = Lesson("2.11", "Main Idea and Key Details",
    "I can determine the main idea of an informational text and explain how key details support it.", "RI.4.2",
    [("main idea", "The most important point of an informational text."), ("key details", "Facts and examples that support the main idea.")],
    "If you had to tell a friend what a science article was about in one sentence, what would you say?",
    [Text("In informational text, the <b>main idea</b> is the most important point. <b>Key details</b> support it. The main idea might be stated in the first or last paragraph, or you may need to figure it out from the details."),
     P_LEAVES,
     Example("Find the main idea", "What is the main idea of “Why Leaves Change Color”?", ["Detail: chlorophyll hides other colors in summer.", "Detail: in fall, chlorophyll fades and hidden colors show.", "Detail: maples make new red colors.", "These all explain why leaves change."],
             "Leaves change color in the fall because the green chlorophyll fades, letting other colors show."),
     KeyIdea("Main idea = the point all the key details support. Check: does every important detail connect to it?")],
    [Problem("Key detail from paragraph 2", "Chlorophyll helps the tree make food and hides other colors."), Problem("Key detail from paragraph 3", "When chlorophyll fades, yellow and orange show."), Problem("Is “Maples are trees” a key detail? Why?", "No; it doesn't explain the color change.")],
    [S("Warm-Up", [SA("What is a main idea?", "the most important point"), SA("What do key details do?", "support the main idea")], cols=2),
     S("Use the Passage", [
         MC("Which sentence BEST states the main idea?", ["Trees rest in winter.", "Leaves change color because chlorophyll fades and other colors show.", "Chlorophyll is green."], 1),
         OR("List two key details that support the main idea.", "Chlorophyll hides other colors; shorter days stop chlorophyll; yellow and orange show; maples make red.", lines=3),
         OR("Find the main idea of “Honeybees in Winter” (Lesson 2.7).", "Honeybees survive winter by working together in a cluster and eating stored honey.", lines=2)], passage=P_LEAVES),
     S("Exit Ticket", [OR("What is the difference between a theme and a main idea?", "Theme: life lesson in a story; main idea: most important point of an informational text.", lines=2)])],
    te("Students determine main idea and key details.", "Determine the main idea of a text and explain how it is supported by key details; summarize the text.", "Workbook Lesson 2.11",
       "One-sentence summary.", "Read “Why Leaves Change Color.”", ["Teach main idea vs details (table-top and legs model).", "Model the leaves passage."], "Your Turn 1–3.",
       ["Choosing an interesting detail as the main idea."], ["Table model: main idea = tabletop, details = legs."], ["Find the main idea of a news article."]),
    summary="The main idea is supported by every key detail.")

L12 = Lesson("2.12", "Comparing Themes Across Stories",
    "I can compare how two stories share or differ in theme.", "RL.4.9",
    [("compare", "Tell how things are alike."), ("contrast", "Tell how things are different.")],
    "Can two very different stories teach the same lesson?",
    [Text("Stories from different times and places often share themes. When you compare, name the theme each story teaches, then show how each story's events teach it."),
     Example("Compare themes", "“The Grasshopper and the Ants” and “The Two Gardens”",
             ["Fable: the grasshopper didn't prepare and went hungry.", "Garden story: Sam didn't take care of his plants and they died.", "Same theme: steady work and preparation pay off.", "Different: one has animal characters and talking; the other is realistic."],
             "Both stories teach that steady effort and preparation pay off, but one uses talking animals and the other uses real-life neighbors."),
     Figure(lambda t: table(t, [["", "Grasshopper and the Ants", "The Two Gardens"], ["Characters", "grasshopper, ants", "Ruby, Sam"], ["Genre", "fable", "realistic fiction"],
                                ["Lesson learned", "work and prepare", "patience and effort"], ["Shared theme", "Effort today pays off later.", "Effort today pays off later."]],
                            [1.3 * inch, 2.1 * inch, 2.1 * inch], width=5.5 * inch)),
     KeyIdea("Compare themes by naming the lesson in each story and the events that teach it.")],
    [Problem("How are the two stories alike?", "same theme: effort and preparation pay off"), Problem("How are they different?", "fable with animals vs realistic story with people"), Problem("Which character in each story learns the lesson?", "the grasshopper; Sam")],
    [S("Warm-Up", [SA("Compare =", "tell how alike"), SA("Contrast =", "tell how different")], cols=2),
     S("Compare", [OR("Compare the theme of Chapter 7 (Sir Tristram) with “The Two Gardens.” Are they alike or different? Explain with one event from each.", "Answers vary; must name each theme and an event.", lines=6)]),
     S("Venn Diagram", [OR("List two ways the grasshopper and Sam are alike and one way they are different.", "Alike: both didn't prepare; both learned a lesson. Different: grasshopper is an animal in a fable; Sam is a person.", lines=4)]),
     S("Exit Ticket", [OR("Write a theme that could fit both fables you read this week.", "e.g. Small or patient efforts can make a big difference.", lines=2)])],
    te("Students compare themes.", "Compare and contrast the treatment of similar themes in stories.", "Workbook Lesson 2.12",
       "Same lesson, different stories?", "Reread both short stories.", ["Model the comparison table."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Comparing plots instead of themes."], ["Use the theme table."], ["Find a movie with the same theme."]),
    summary="Different stories can share a theme; compare the lesson and how events teach it.")

# ================================================================= Week 4 · Summarize and explain development (Chapter 8)
L13 = Lesson("2.13", "Summarizing a Story",
    "I can summarize a story using the most important events.", "RL.4.2",
    [("summary", "A short retelling of the most important parts of a text, in your own words.")],
    "If your friend missed a movie, how would you tell them about it in under a minute?",
    [ReaderAssign(READER, "Chapter 8: The End of Merlin", "What are the most important events? What happens to Merlin?"),
     Text("A <b>summary</b> tells only the most important events, in order, in your own words. It leaves out small details and opinions. One helpful frame is <b>Somebody–Wanted–But–So–Then</b>."),
     P_LIGHTHOUSE,
     Example("Summarize with SWBST", "“The Lighthouse Keeper's Daughter”",
             ["Somebody: Nell", "Wanted: to keep ships safe when her father couldn't light the lamp", "But: there was a storm and he hurt his ankle", "So: she climbed the tower and lit the lamp herself", "Then: the boat turned in time and the fishermen thanked her"],
             "When her father hurt his ankle during a storm, Nell climbed the lighthouse tower and lit the lamp herself. The fishing boat turned just in time, and the fishermen thanked her for saving their lives."),
     KeyIdea("A summary is short, in order, in your own words, and includes only the most important events.")],
    [Problem("Should a summary include “rain lashed the glass”?", "No; it's a small detail."), Problem("Should a summary include your opinion?", "No"), Problem("Who is the Somebody in Chapter 8?", "Merlin (or Arthur)")],
    [S("Warm-Up", [SA("SWBST: S =", "Somebody"), SA("Is a summary long?", "No, short")], cols=2),
     S("Summarize", [OR("Use SWBST to summarize “Mira's Recital” (Lesson 2.6).", "Mira wanted to play well, but she was nervous, so she breathed deeply and played; then the audience clapped and she wanted to play more.", lines=4),
                     OR("Use SWBST to summarize Chapter 8.", "Answers vary; must include the main events of the chapter in order.", lines=5)]),
     S("Exit Ticket", [OR("Cross out the detail that does NOT belong in a summary of the lighthouse story: (a) Nell lit the lamp. (b) The stairs were winding. (c) The boat turned in time.", "(b)", lines=1)])],
    te("Students summarize stories.", "Summarize the text.", "King Arthur Reader (Chapter 8), workbook Lesson 2.13",
       "Tell a movie in a minute.", ["Read Chapter 8.", "Read the lighthouse story."], ["Teach SWBST.", "Model it."], "Your Turn 1–3.",
       ["Retelling every detail.", "Adding opinions."], ["Limit to 3–4 sentences."], ["Summarize the whole book so far in one paragraph."]),
    summary="Summaries are short, in order, in your own words. Use Somebody–Wanted–But–So–Then.")

L14 = Lesson("2.14", "Summarizing Informational Text",
    "I can summarize an informational text using the main idea and key details.", "RI.4.2",
    [],
    "How is summarizing an article different from summarizing a story?",
    [Text("An informational summary starts with the <b>main idea</b>, then gives the most important <b>key details</b>, in your own words. There are no characters or plot, so SWBST doesn't fit."),
     P_PRESS,
     Example("Summarize", "“The Printing Press”", ["Main idea: Gutenberg's printing press changed the world by making books cheaper and more common.", "Key details: before, books were copied by hand; the press used movable metal letters; more people read and ideas spread."],
             "Gutenberg's printing press, built around 1450, changed the world. Before it, books were copied by hand and were rare. The press used movable metal letters to print hundreds of pages a day, so books became cheaper, more people learned to read, and ideas spread quickly."),
     KeyIdea("Informational summary = main idea + two or three key details, in your own words.")],
    [Problem("Main idea of the passage", "The printing press made books cheaper and helped ideas spread."), Problem("One key detail", "Books were copied by hand before; the press printed hundreds of pages a day; more people learned to read."),
     Problem("Should a summary include the exact year?", "It can, if it's important; keep it short.")],
    [S("Warm-Up", [SA("Does an informational summary use SWBST?", "No"), SA("What comes first in an informational summary?", "the main idea")], cols=2),
     S("Summarize", [OR("Summarize “Why Leaves Change Color” (Lesson 2.11) in 2–3 sentences.", "In fall, trees stop making green chlorophyll. As it fades, hidden yellow and orange colors show, and some trees make red. Then the leaves fall.", lines=4),
                     OR("Summarize “The Code of Chivalry” (Lesson 2.2) in 2–3 sentences.", "Knights were expected to follow a code of loyalty, bravery, and courtesy. Not all did, but the code shaped ideas of a good knight that live on in stories.", lines=4)]),
     S("Exit Ticket", [OR("What two things must an informational summary include?", "main idea and key details", lines=1)])],
    te("Students summarize informational texts.", "Determine the main idea and summarize the text.", "Workbook Lesson 2.14",
       "Story vs article summaries.", "Read “The Printing Press.”", ["Model the summary."], "Your Turn 1–3.",
       ["Copying sentences instead of paraphrasing."], ["Cover the text before writing."], ["Summarize a science chapter."]),
    summary="Informational summary: main idea plus key details in your own words.")

L15 = Lesson("2.15", "How Events Develop: Cause and Effect in a Plot",
    "I can explain how one event in a story leads to another.", "RL.4.3",
    [("plot", "The sequence of events in a story."), ("cause", "Why something happens."), ("effect", "What happens as a result.")],
    "In a chain of dominoes, how does the first one make the last one fall?",
    [Text("Events in a plot are connected like dominoes: one <b>cause</b> leads to an <b>effect</b>, which can cause another effect. Signal words: <i>because</i>, <i>so</i>, <i>as a result</i>, <i>since</i>, <i>therefore</i>."),
     Example("Trace a chain", "“The Lighthouse Keeper's Daughter”",
             ["Cause: Father hurts his ankle → Effect: he can't climb to light the lamp.", "Cause: The lamp isn't lit → Effect: the boat heads for the rocks.", "Cause: Nell lights the lamp → Effect: the boat turns in time."],
             "Each event causes the next: the injury leads Nell to climb the tower, which saves the boat."),
     KeyIdea("Explain how events connect: this happened because of that. Use signal words.")],
    [Problem("Why did the fishermen row to the island?", "to thank Nell for saving them"), Problem("Why did Nell climb the tower?", "Her father hurt his ankle and could not light the lamp."), Problem("Name a cause-effect signal word.", "because, so, as a result")],
    [S("Warm-Up", [SA("What is a cause?", "why something happens"), SA("What is an effect?", "what happens as a result")], cols=2),
     S("Cause and Effect", [SA(f"Cause: {c} Effect?", e) for c, e in [("The grasshopper played all summer.", "He had no food in winter."), ("Sam forgot to water.", "His plants turned brown."),
                                                                         ("Mira practiced and stayed brave.", "She played well and the audience clapped."), ("The ants stored seeds.", "They had food in winter.")]], cols=1),
     S("Chapter 8", [OR("Explain how one event in Chapter 8 leads to another. Use a signal word.", "Answers vary; must show a cause-effect link from the chapter.", lines=4)]),
     S("Exit Ticket", [OR("Write a two-sentence cause-and-effect chain about your morning.", "Answers vary.", lines=2)])],
    te("Students explain how events develop.", "Describe in depth an event, drawing on specific details.", "Workbook Lesson 2.15",
       "Domino chain.", "Reread the lighthouse story.", ["Teach signal words.", "Model the chain."], "Your Turn 1–3.",
       ["Listing events without explaining the connection."], ["Draw arrows between events."], ["Make a cause-effect chain for Chapters 5–8."]),
    summary="Plot events connect through cause and effect.")

L16 = Lesson("2.16", "Writing a Summary Paragraph",
    "I can write a well-organized summary paragraph and review the unit.", "W.4.2, RL.4.2",
    [("topic sentence", "The first sentence that tells what the paragraph is about.")],
    "What makes a summary paragraph easy to follow?",
    [Text("A summary paragraph begins with a <b>topic sentence</b> naming the text and its main idea or theme, gives the important events or details in order with transitions, and ends with a concluding sentence."),
     Example("Summary paragraph", "Summarize Chapters 5–8 of King Arthur.",
             ["Topic sentence: In Chapters 5–8, Arthur's kingdom grows strong, but trouble begins.", "Middle: the Round Table is founded; great knights such as Lancelot and Tristram arrive; Merlin's story ends.", "Concluding sentence: tie it together."],
             "A paragraph with a topic sentence, three to four key events in order with transitions, and a conclusion."),
     KeyIdea("Topic sentence → events or details in order → concluding sentence.")],
    [Problem("Where does the topic sentence go?", "at the beginning"), Problem("Name two transitions for a summary.", "first, next, then, finally"), Problem("Should a summary include every event?", "No, only the most important ones.")],
    [S("Warm-Up", [SA("What is a topic sentence?", "the first sentence that tells what the paragraph is about"), SA("Last sentence is the ___ sentence.", "concluding")], cols=2),
     S("Write", [OR("Write a summary paragraph of Chapters 5–8 of King Arthur and the Round Table. Use a topic sentence, transitions, and a concluding sentence.", "Answers vary.", lines=12,
                    note="1 point each: topic sentence; key events in order; transitions; concluding sentence; own words.")]),
     S("Exit Ticket", [OR("Which skill from this unit (evidence, inference, theme, summary) is easiest for you? Which needs practice?", "Answers vary.", lines=2)])],
    te("Students write a summary paragraph and review.", "Write informative texts that convey ideas clearly; summarize.", "Workbook Lesson 2.16, Unit 2 Review",
       "What makes a summary easy to follow?", "Skim Chapters 5–8.", ["Model the paragraph structure."], "Plan the paragraph together.",
       ["No topic sentence."], ["Paragraph frame."], ["Illustrate a timeline of the chapters."], independent="Write the summary; then the Unit 2 Review.", exit_="Exit Ticket. Tomorrow: Unit 2 Test."),
    summary="Summary paragraph: topic sentence, events in order, concluding sentence.")

# ================================================================= checks
C1 = Check("Weekly Check 4: Text Evidence", [S("Read and answer", [
    OR("What is a homing pigeon able to do? Quote the text.", "“A homing pigeon can find its way back to its home from hundreds of miles away.”", lines=2),
    OR("Paraphrase what Cher Ami did.", "She carried a message in 1918 that helped save almost 200 soldiers, even though she was hurt.", lines=2),
    MC("Which detail BEST supports the idea that pigeons were important in wars?", ["“Some think the birds use the sun.”", "“Cher Ami delivered a message in 1918 that helped save almost 200 soldiers.”", "“People have used homing pigeons for thousands of years.”"], 1),
    OR("Write an ACE answer: Are scientists sure how pigeons find their way?", "No. Paragraph 3 says scientists “are still not completely sure.” This shows there are different ideas, such as the sun or a magnetic sense.", lines=4, points=3)], passage=P_C4)], minutes=20)

C2 = Check("Weekly Check 5: Inference", [S("Read and answer", [
    OR("How does Jamal feel in paragraph 1? Give two clues.", "nervous or shy and left out; hands in pockets, standing at the edge, steps forward then stops", lines=2),
    OR("What does Jamal want? How do you know?", "to play soccer; he steps forward whenever the ball comes near", lines=2),
    OR("How does Jamal feel at the end? Clue?", "happy and excited; his face lit up and he ran so fast he almost tripped", lines=2),
    MC("What can you infer about the girl with the ponytail?", ["She is unkind.", "She is friendly and welcoming.", "She doesn't like soccer."], 1)], passage=P_C5)], minutes=20)

C3 = Check("Weekly Check 6: Theme and Main Idea", [S("Read and answer", [
    MC("Why does the lion let the mouse go?", ["He is scared of the mouse.", "He finds the mouse's promise funny but is kind enough to release it.", "The mouse bites him."], 1),
    OR("How does the mouse help the lion?", "It chews through the hunter's net to free him.", lines=2),
    OR("Write the theme of the fable as a sentence.", "Even small friends can be a big help; kindness is repaid.", lines=2),
    OR("How does the lion's change show the theme?", "He laughed at the mouse but was saved by it, showing size doesn't decide who can help.", lines=2),
    MC("Which is a TOPIC, not a theme?", ["kindness", "Kindness is often returned.", "Never judge someone by size."], 0)], passage=P_C6)], minutes=20)

REVIEW = Check("Unit 2 Review", [
    S("Skills", [SA("Quote or paraphrase: “The night was dark.”", "quote"), SA("Inference formula", "clues + what I know"), SA("Theme or topic: “courage”", "topic"),
                 SA("SWBST stands for", "Somebody, Wanted, But, So, Then"), SA("Main idea is for ___ text.", "informational"), SA("ACE stands for", "Answer, Cite, Explain")], cols=2),
    S("Apply", [OR("Reread “Honeybees in Winter.” Write its main idea and two key details.", "Bees survive winter by working together; they form a cluster, shiver to make heat, eat stored honey.", lines=3),
                OR("Reread “The Two Gardens.” Summarize it in 2–3 sentences.", "Sam planted big plants but forgot to water, while Ruby patiently grew seeds. By August Ruby's garden thrived; she shared tomatoes and Sam asked her to teach him.", lines=3)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 2 Test", [
    S("Part A · Evidence and inference (1 point each)", [
        MC("Why did people cross the bridge every morning?", ["to fish", "to sell vegetables and go to school", "to see the mayor"], 1),
        OR("What did Ada notice about the bridge? Quote the text.", "“the middle of the bridge was sagging, and one of the wooden posts had cracked”", lines=2),
        OR("Why did Ada tie the blanket to the railing? Make an inference and give a clue.", "To warn people to stop; she knew the wagons were coming and the bridge was unsafe.", lines=2),
        OR("How did the farmer feel when he saw the cracked post? Clue?", "scared/shocked; “his face went pale”", lines=2),
        MC("What does “Without wasting another minute” show about Ada?", ["She was lazy.", "She acted quickly in an emergency.", "She was confused."], 1)], passage=P_TEST),
    S("Part B · Theme and summary (1 point each)", [
        OR("What is a theme of “The Bridge at Millbrook”?", "e.g. One brave person who acts quickly can protect many people.", lines=2),
        OR("Why did the mayor give Ada the scissors? What does this show?", "to honor her for saving people; she was a hero", lines=2),
        OR("Explain one cause-and-effect relationship in the story.", "Heavy rain caused the river to rise, which cracked the bridge; Ada's warning caused the farmer to stop, so no one fell.", lines=2),
        MC("Which detail does NOT belong in a summary?", ["Ada warned people about the bridge.", "The blanket was red.", "The bridge fell into the river."], 1)]),
    S("Part C · Write (5 points)", [OR("Write a summary paragraph of “The Bridge at Millbrook” with a topic sentence, the key events in order, and a concluding sentence. Then add one sentence stating the theme.",
                                       "Answers vary. Rubric: topic sentence (1); key events in order (1); own words (1); concluding sentence (1); theme stated (1).", lines=12, points=5)])],
    kind="test", minutes=45, rubric=[["12–14 (85%+)", "Mastered."], ["10–11", "Proficient; review missed skills."], ["Below 10", "Reteach evidence or summary and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2026-11-09", "2026-11-16", "2026-11-30", "2026-12-07"], CHECKS, REVIEW, TEST)

UNIT = Unit(2, "Reading Closely", "Text evidence, inference, theme and main idea, and summary, with King Arthur and the Round Table, Chapters 5–8.",
    "Good readers don't just read the words; they find evidence, read between the lines, discover the lessons stories teach, and retell what matters most. In this unit you will practice all four skills with the legends of the Round Table, fables, and informational articles.",
    ["Quote and paraphrase text evidence; choose the strongest evidence.", "Make and support inferences about characters and facts.",
     "Determine themes in stories and main ideas in informational texts.", "Summarize stories and articles and explain how events connect."],
    [("RL.4.1, RI.4.1", "Refer to details and examples when explaining a text and drawing inferences."), ("RL.4.2, RI.4.2", "Determine theme or main idea; summarize."),
     ("RL.4.3", "Describe characters, settings, and events in depth."), ("RL.4.9", "Compare and contrast the treatment of similar themes."), ("W.4.9", "Draw evidence from texts to support analysis.")],
    [("text evidence", "Details from a text that support an answer."), ("inference", "Clues + what I know."), ("theme", "A story's life lesson."), ("main idea", "The most important point of an informational text."),
     ("summary", "A short retelling of the most important parts.")],
    ["Unit 1 vocabulary skills.", "Writing complete sentences and paragraphs."], ["King Arthur and the Round Table Reader (Chapters 5–8)", "Highlighters or colored pencils"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Evidence and inference help you everywhere: deciding whether an ad is telling the truth, figuring out how a friend feels, or explaining your ideas to others.",
    family_note="After reading or a movie, ask “How do you know?” and “What's the lesson?” Make it a habit to back up opinions with evidence.",
    weeks=WEEKS)
