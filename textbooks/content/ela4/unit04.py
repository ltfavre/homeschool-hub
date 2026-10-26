"""Grade 4 ELA · Unit 4: The Writer's Craft — words and phrases, text structure, purpose and point of view, comparing craft.
Anchor reading: Treasure Island Reader, Chapters 1–4 (Jan 25 – Feb 19, 2027)."""
from engine import *
from content.te import TE, eflow
from content.sched import schedule
from content.ela4.unit01 import S, MC, OR, SA

TI = "Treasure Island Reader"


def te(obj, std, mat, warm, read, teach, guided, mis, sup, ext, **k):
    return TE(obj, std, mat, eflow(warm, read, teach, guided, **k), mis, sup, ext)


# ================================================================= passages
P_OPENING = Passage("From Treasure Island, Chapter 1 (original 1883 text)", [
    "Squire Trelawney, Dr. Livesey, and the rest of these gentlemen having asked me to write down the whole particulars about Treasure Island, from the beginning to the end, keeping nothing back but the bearings of the island, and that only because there is still treasure not yet lifted, I take up my pen in the year of grace 17—, and go back to the time when my father kept the Admiral Benbow inn, and the brown old seaman, with the sabre cut, first took up his lodging under our roof.",
    "I remember him as if it were yesterday, as he came plodding to the inn door, his sea-chest following behind him in a hand-barrow—a tall, strong, heavy, nut-brown man, his tarry pigtail falling over the shoulder of his soiled blue coat, his hands ragged and scarred, with black, broken nails, and the sabre cut across one cheek, a dirty, livid white.",
], source="Robert Louis Stevenson, Treasure Island (1883). Public domain.", genre="Classic novel excerpt")

P_MYTH = Passage("A Herculean Task", [
    "Cleaning the garage was a <b>Herculean</b> task. Boxes were stacked to the ceiling, and Dad said nobody had swept the floor since before I was born.",
    "My sister Zoe opened a dusty trunk in the corner. “Don't!” I warned. “That could be a <b>Pandora's box</b>.” Sure enough, a cloud of moths flew out, and Zoe screamed.",
    "Dad is great at fixing things, but organizing is his <b>Achilles' heel</b>. He kept every broken lamp and bent bicycle wheel, “just in case.”",
    "By evening, the garage was spotless. Mom walked in and said we must have the <b>Midas touch</b>, because we had found forty dollars in old coins in a coffee can.",
], source="An original story", genre="Realistic fiction")

P_SHIP = Passage("Life Aboard a Sailing Ship", [
    "In the 1700s, sailing ships carried goods, passengers, and sometimes treasure across the oceans. A ship's crew had to know many special words.",
    "The front of the ship was the <b>bow</b>, and the back was the <b>stern</b>. Facing the bow, the left side was called <b>port</b> and the right side was <b>starboard</b>. Tall poles called <b>masts</b> held up the sails.",
    "Sailors slept below the <b>deck</b> in hammocks, cloth beds that swung from the ceiling. Food was cooked in the <b>galley</b>, the ship's kitchen. It was usually hard biscuits and salted meat, because fresh food spoiled on long voyages.",
    "Each sailor had a job. Some climbed the <b>rigging</b>, the ropes that held up the masts and sails. Others steered, cooked, or mended sails. The captain was in charge of everyone, and disobeying an order could mean harsh punishment.",
], source="An original informational text", genre="Informational text")

P_POEM = Passage("The Sea Chest", [
    "> The old sea chest sat by the door,\\nIts lid all cracked and worn;\\nIt smelled of salt and tar and rope\\nAnd stormy seas at morn.",
    "> What secrets did the sailor keep\\nBeneath that rusty lock?\\nA compass, coins, a faded map,\\nA single, tangled sock?",
    "> I'll never know, for on the night\\nThe sailor sailed away,\\nHe took his chest and all his tales\\nTo some far-distant bay.",
], source="An original poem", genre="Poem", numbered=False)

P_PLAY = Passage("The Captain's Warning: A Scene", [
    "<b>CHARACTERS:</b> JIM, a boy who works at the inn · THE CAPTAIN, an old sailor · MOTHER, Jim's mother",
    "<i>(The Admiral Benbow inn. Night. Wind howls outside. THE CAPTAIN sits by the fire, gripping his mug.)</i>",
    "<b>CAPTAIN:</b> <i>(in a low voice)</i> Jim, come here, lad. You keep your weather-eye open, you hear?",
    "<b>JIM:</b> For what, Captain?",
    "<b>CAPTAIN:</b> For a seafaring man with one leg. If you see him, you tell me first. I'll pay you a silver fourpenny every month.",
    "<b>MOTHER:</b> <i>(entering with a tray)</i> Jim! Stop bothering the guest and fetch more wood.",
    "<b>JIM:</b> <i>(to the audience)</i> But I couldn't stop thinking about that one-legged man. That night, I dreamed of him chasing me across the moor.",
], source="An original scene inspired by Treasure Island", genre="Drama", numbered=False)

P_STRUCT = {
    "Chronological": "The pirate Blackbeard began sailing around 1716. By 1717, he had captured a large French ship and renamed it <i>Queen Anne's Revenge</i>. In 1718, he blockaded the port of Charleston. Later that year, he was defeated in a battle off the coast of North Carolina.",
    "Compare and contrast": "Pirates and navy sailors both lived on ships and faced storms and disease. However, navy sailors worked for a government and were paid regular wages. Pirates, on the other hand, often voted for their captain and shared the treasure they stole.",
    "Cause and effect": "Because sailors ate few fruits and vegetables on long voyages, many developed a disease called scurvy. As a result, their gums bled and they grew weak. When sailors began carrying limes and lemons, scurvy became much less common.",
    "Problem and solution": "Ships often wrecked on rocky coasts at night. To solve this problem, people built lighthouses with bright lamps on high towers. The light warned sailors to steer away from danger.",
}
P_STRUCTS = Passage("Four Paragraphs About Life at Sea", list(P_STRUCT.values()), source="Original informational paragraphs", genre="Informational text")

P_FIRST = Passage("Account A: “The Storm Hit Our Town”", [
    "I was nine years old when the hurricane hit our town. I remember the wind screaming like a train all night long. My brother and I huddled in the bathtub with a mattress over our heads while Mom held a flashlight.",
    "In the morning, I stepped outside and couldn't believe my eyes. Our big oak tree was lying across the street, and the Johnsons' roof was in our yard. I felt lucky and scared at the same time.",
], source="An original firsthand account", genre="Firsthand account")
P_SECOND = Passage("Account B: “Hurricane Strikes Coastal Town”", [
    "On September 12, a powerful hurricane struck the coastal town of Bayview. Winds reached 120 miles per hour, according to the National Weather Service.",
    "More than 200 homes were damaged, and thousands of trees fell. Officials reported that no one was seriously injured, largely because most residents followed instructions to take shelter. Repairs are expected to take several months.",
], source="An original secondhand account (news article)", genre="Secondhand account")

P_AD = Passage("WANTED: Brave Sailors!", [
    "Are you tired of boring work on land? Join the crew of the finest ship in Bristol, the <i>Hispaniola</i>!",
    "Our ship is fast, our captain is fair, and our cook makes the best stew on the seven seas. Every sailor will be paid well, and the voyage will be the adventure of a lifetime.",
    "Don't miss this chance. Only the bravest need apply. Sign up at the docks today!",
], source="An original advertisement", genre="Persuasive text")

P_SUSPENSE = Passage("The Footsteps", [
    "Ana was alone in the library after closing. The lights buzzed. Rain tapped the tall windows.",
    "Then she heard it: a footstep. Then another. Slow. Heavy. Coming closer.",
    "She held her breath and crouched behind the shelf of atlases. The footsteps stopped right beside her. A shadow stretched across the floor.",
    "“Ana?” said a familiar voice. It was Mr. Diaz, the custodian, holding an umbrella. “Your mom is waiting outside.” Ana let out her breath in a laugh so loud it echoed off the ceiling.",
], source="An original story", genre="Realistic fiction")

P_PIRATES = Passage("Real Pirates of the Golden Age", [
    "From about 1690 to 1730, so many pirates sailed the oceans that historians call it the Golden Age of Piracy. Pirates attacked ships carrying gold, silver, sugar, and cloth.",
    "Real pirates were very different from the pirates in stories. Most did not bury their treasure; they spent it quickly. There is little evidence that pirates made prisoners walk the plank. And treasure maps marked with an X were mostly invented by writers.",
    "Pirate ships often had written rules. Crews voted on important decisions, and treasure was divided by shares. A captain who was unfair could be voted out.",
    "Life as a pirate was dangerous and usually short. Many pirates were captured and punished. By 1730, navies had driven most pirates from the seas.",
], source="An original informational text", genre="Informational text")

P_C10 = Passage("The Lighthouse at Gull Point", [
    "Gull Point Lighthouse stood like a giant candle at the edge of the cliff. Its beam swept the black water, a white finger pointing ships to safety.",
    "Mr. Fenn, the keeper, had a heart of gold, but his temper was a volcano. When the gulls stole his sandwiches, he roared so loudly that the whole island heard him.",
    "Still, every night for forty years, he climbed the 120 stairs to light the lamp. It was a Herculean job, but he never missed a night.",
], source="An original story", genre="Realistic fiction")

P_C11 = Passage("Moving Day", [
    "<i>(A kitchen full of boxes. MAYA, age 10, sits on a box, arms crossed. DAD tapes another box shut.)</i>",
    "<b>DAD:</b> Maya, can you hand me the markers?",
    "<b>MAYA:</b> <i>(not moving)</i> I don't want to move. All my friends are here.",
    "<b>DAD:</b> <i>(sitting down beside her)</i> I know. I was scared to move when I was your age, too. But I met my best friend in the new town.",
    "<b>MAYA:</b> <i>(uncrossing her arms)</i> Really? <i>(pause)</i> Okay. Which box do the markers go in?",
], source="An original scene", genre="Drama", numbered=False)

P_C12 = Passage("Ellie's Journal: The Science Fair", [
    "March 3. Today was the science fair! I was so nervous my hands shook while I set up my volcano. When I poured in the vinegar, the lava bubbled over perfectly, and the judges laughed and clapped.",
    "I won second place! I can't wait to tell Grandma. Next year, I want to build a robot.",
], source="An original firsthand account", genre="Journal")

P_TEST = Passage("Ghost Ship of the Fog", [
    "The fog rolled in thick and gray, swallowing the harbor whole. On the deck of the fishing boat <i>Mary Bell</i>, Captain Rosa squinted into the mist. Her crew had gone silent.",
    "Then, out of the fog, a ship appeared. Its sails hung in rags, and its wooden sides were green with moss. No lanterns burned on its deck. No sailors called out. It drifted toward them without a sound.",
    "“A ghost ship,” whispered Tomás, the youngest sailor, gripping the rail so tightly his knuckles turned white. “My grandmother told me about them.”",
    "Captain Rosa's heart pounded, but her voice was steady. “Hard to starboard!” she ordered. The <i>Mary Bell</i> turned, and the old ship slid past, so close that Rosa could read the faded name on its stern: <i>Restless</i>.",
    "The next day, Rosa learned the truth. The <i>Restless</i> was an old ship that had broken loose from its anchor in a storm. With no crew aboard, it had drifted for weeks. It wasn't haunted after all, though Tomás never quite believed that.",
], source="An original story", genre="Adventure story")

# ================================================================= Week 1 · Interpret words and phrases (Chapter 1)
L1 = Lesson("4.1", "Reading Old-Fashioned Language",
    "I can figure out the meaning of words and phrases in an older text.", "RL.4.4, L.4.4a",
    [("classic", "A book that has been read and admired for a long time."), ("archaic", "Old-fashioned; no longer commonly used.")],
    "Have you ever read something that sounded old-fashioned? What made it sound that way?",
    [ReaderAssign(TI, "Chapter 1: The Old Seadog and the Black Spot", "Who is the old seaman? Why is everyone afraid of him?"),
     Text("<i>Treasure Island</i> was written by Robert Louis Stevenson in 1883. Your Reader retells it in modern words, but the original uses long sentences and <b>archaic</b> words. Use context clues, word parts, and the whole sentence to figure them out."),
     P_OPENING,
     Example("Understand an old phrase", "“keeping nothing back but the bearings of the island”", ["<i>Keeping nothing back</i> = telling everything.", "<i>Bearings</i> = directions or location (a sailing word).", "Why keep them back? “there is still treasure not yet lifted.”"],
             "Jim will tell everything except the island's exact location, because treasure is still there."),
     KeyIdea("Read old-fashioned sentences in chunks. Use context, word parts, and what you know about the story.")],
    [Problem("Who is telling the story?", "Jim Hawkins (the narrator, “I”), the son of the innkeeper"), Problem("What is a “sabre cut”?", "a scar from a sword"), Problem("What does “took up his lodging under our roof” mean?", "came to live at the inn")],
    [S("Warm-Up", [SA("What is a classic?", "a book read and admired for a long time"), SA("When was Treasure Island written?", "1883")], cols=2),
     S("Old Words, New Meanings", [
         OR("Paragraph 2: list four details that describe the seaman. What kind of person does he seem to be?", "tall, strong, heavy; tarry pigtail; ragged, scarred hands; sabre cut; he seems rough and dangerous.", lines=3),
         OR("What does “plodding” mean? Which clue helps?", "walking slowly and heavily; he is heavy and his chest follows in a hand-barrow", lines=2),
         MC("“The year of grace 17—” tells us the story happened…", ["in the future", "in the 1700s", "last year"], 1)], passage=P_OPENING),
     S("Chapter 1", [OR("What is the black spot, and why does it frighten the captain?", "A pirate's warning or summons; it means the pirates are coming for him.", lines=3)]),
     S("Exit Ticket", [OR("Rewrite paragraph 2 in one modern sentence.", "e.g. I clearly remember the big, scarred old sailor dragging his sea chest to the inn door.", lines=2)])],
    te("Students interpret old-fashioned language.", "Determine the meaning of words and phrases as they are used in a text.", "Treasure Island Reader (Chapter 1), workbook Lesson 4.1",
       "Old-fashioned language examples.", ["Read Chapter 1 in the Reader.", "Read Stevenson's original opening aloud."], ["Model chunking the long sentence."], "Your Turn 1–3.",
       ["Giving up on long sentences."], ["Break the sentence at commas."], ["Compare more of the original text to the Reader."]),
    summary="Chunk old-fashioned sentences and use context to understand archaic words.")

L2 = Lesson("4.2", "Words from Mythology",
    "I can explain words and phrases that come from mythology.", "RL.4.4, L.4.5",
    [("allusion", "A reference to a well-known story, person, or event."), ("mythology", "Ancient stories about gods and heroes.")],
    "If someone says a job is “Herculean,” what do you think it means?",
    [Text("Many English expressions come from Greek myths. Knowing the myth helps you understand the word."),
     Figure(lambda t: table(t, [["Word or phrase", "The myth", "Meaning today"], ["Herculean", "Hercules completed twelve nearly impossible labors.", "needing huge strength or effort"],
                                ["Pandora's box", "Pandora opened a box that released troubles into the world.", "something that causes many problems once started"],
                                ["Achilles' heel", "Achilles could be hurt only on his heel.", "a weak spot"], ["Midas touch", "Everything King Midas touched turned to gold.", "the ability to make money or succeed easily"],
                                ["echo", "Echo was a nymph who could only repeat others' words.", "a repeated sound"]], [1.3 * inch, 2.6 * inch, 1.9 * inch], width=5.8 * inch, font_size=9)),
     P_MYTH,
     Example("Explain an allusion", "“Organizing is his Achilles' heel.”", ["Myth: Achilles' only weak spot was his heel.", "Context: Dad is great at fixing but keeps everything."], "Organizing is Dad's weakness."),
     KeyIdea("Learn the myth behind the phrase, then apply its meaning to the sentence.")],
    [Problem("Why was cleaning the garage Herculean?", "It was a huge, hard job."), Problem("Why call the trunk a Pandora's box?", "Opening it might let out trouble (moths)."), Problem("Why did they have the Midas touch?", "They found money while cleaning.")],
    [S("Warm-Up", [SA("What is an allusion?", "a reference to a well-known story"), SA("Who was Hercules?", "a strong hero who did twelve labors")], cols=2),
     S("Use the Allusion", [MC(q, ch, k) for q, ch, k in [
         ("Spelling is my Achilles' heel. This means spelling is…", ["my best subject", "my weak spot", "very easy"], 1),
         ("Starting that argument opened a Pandora's box. This means…", ["it caused many problems", "it was a gift", "it was fun"], 0),
         ("Moving the piano was a Herculean task. This means…", ["it was easy", "it needed great strength", "it was musical"], 1),
         ("Grandpa has the Midas touch with his business. This means…", ["his business fails", "he is good at making money", "he likes gold jewelry"], 1)]]),
     S("Write", [OR("Write two sentences of your own using two of the allusions.", "Answers vary; used correctly.", lines=3)]),
     S("Exit Ticket", [OR("Which allusion describes the captain in Chapter 1? Explain.", "e.g. Achilles' heel: his weakness is his fear of the pirates / the black spot.", lines=2)])],
    te("Students explain mythological allusions.", "Determine meanings of words and phrases, including those that allude to significant characters found in mythology.", "Workbook Lesson 4.2",
       "Herculean?", "Read “A Herculean Task.”", ["Tell each short myth.", "Model Achilles' heel."], "Your Turn 1–3.",
       ["Taking allusions literally."], ["Picture the myth, then the meaning."], ["Read a children's version of the Twelve Labors of Hercules."]),
    summary="Allusions to myths: Herculean, Pandora's box, Achilles' heel, Midas touch.")

L3 = Lesson("4.3", "Sensory Language and Mood",
    "I can explain how sensory words create a mood.", "RL.4.4, RL.4.3",
    [("sensory language", "Words that appeal to sight, sound, smell, taste, or touch."), ("mood", "The feeling a reader gets from a text, such as spooky, peaceful, or tense.")],
    "Close your eyes. What sounds, smells, and sights would you notice in an old inn by the sea at night?",
    [Text("Writers use <b>sensory language</b> to make readers feel something. The feeling is the <b>mood</b>. Find the sensory words, then ask: <i>How do they make me feel?</i>"),
     P_POEM,
     Example("Find the mood", "“It smelled of salt and tar and rope / And stormy seas at morn.”", ["Smell words: salt, tar, rope.", "Sight/feeling: stormy seas.", "They make the chest seem old, adventurous, and a bit mysterious."], "The mood is mysterious and adventurous."),
     KeyIdea("Sensory words → pictures and feelings → mood. Name the mood with an exact word.")],
    [Problem("Which sense does “cracked and worn” appeal to?", "sight (and touch)"), Problem("What mood does the second stanza create?", "curious, mysterious"), Problem("How does the last stanza feel?", "a little sad / wistful; the mystery is never solved")],
    [S("Warm-Up", [SA("Five senses", "sight, sound, smell, taste, touch"), SA("A mood word", "spooky, peaceful, tense, cheerful")], cols=2),
     S("Use the Poem", [OR("List three sensory details from the poem and the sense each appeals to.", "salt/tar/rope (smell), cracked and worn (sight/touch), rusty lock (sight).", lines=3),
                        OR("The poet ends the second stanza with “A single, tangled sock?” How does this line change the mood?", "It adds humor; the mood becomes playful.", lines=2)], passage=P_POEM),
     S("Chapter 1", [OR("Find a sensory detail in Chapter 1 that creates a scary or tense mood. Explain.", "Answers vary, e.g. Blind Pew's tapping stick.", lines=3)]),
     S("Exit Ticket", [OR("Write two sentences describing the Admiral Benbow inn at night with a spooky mood. Use two senses.", "Answers vary.", lines=3)])],
    te("Students explain sensory language and mood.", "Determine the meaning of words and phrases, including figurative language.", "Workbook Lesson 4.3",
       "Close-your-eyes inn.", "Read “The Sea Chest” poem aloud twice.", ["Five-senses chart.", "Model the mood."], "Your Turn 1–3.",
       ["Naming a mood as “good” or “bad.”"], ["Mood word bank."], ["Write a poem about another object from Chapter 1."]),
    summary="Sensory words create mood; name the mood precisely.")

L4 = Lesson("4.4", "Content Words in Informational Text",
    "I can figure out content words in an informational text.", "RI.4.4",
    [("bow", "The front of a ship."), ("stern", "The back of a ship."), ("port", "The left side of a ship (facing forward)."), ("starboard", "The right side of a ship (facing forward)."),
     ("galley", "A ship's kitchen."), ("rigging", "The ropes that hold up a ship's masts and sails.")],
    "Why do sailors have special words for the front, back, left, and right?",
    [Text("Informational texts use <b>content words</b> about the topic. Authors often define them in the text, show them in diagrams, or give clues. Use these words when you write about the topic."),
     P_SHIP,
     Example("Use the text's definition", "What are hammocks?", ["Paragraph 3 defines them right after a comma."], "cloth beds that swing from the ceiling"),
     KeyIdea("Look for definitions, diagrams, and context for content words, then use the words yourself.")],
    [Problem("Why might sailors say port instead of left?", "Left changes depending on which way you face; port always means the same side of the ship."), Problem("Where was food cooked?", "in the galley"), Problem("What did sailors eat? Why?", "hard biscuits and salted meat; fresh food spoiled")],
    [S("Warm-Up", [SA("Front of a ship", "bow"), SA("Back of a ship", "stern")], cols=2),
     S("Content Words", [SA(w, a) for w, a in [("port", "left side"), ("starboard", "right side"), ("mast", "tall pole holding sails"), ("deck", "floor of the ship"), ("galley", "kitchen"), ("rigging", "ropes holding masts and sails")]], cols=2),
     S("Label the Ship", [Problem("Draw a simple ship from above. Label the bow, stern, port, and starboard.", "Bow at front, stern at back; facing the bow, port on left, starboard on right.", space=150, wide=True,
                                  note="Check port is on the left when facing the bow.")]),
     S("Exit Ticket", [OR("Write two sentences about a sailor's day using three content words.", "Answers vary.", lines=3)])],
    te("Students learn content words.", "Determine the meaning of general academic and domain-specific words in a text.", "Workbook Lesson 4.4",
       "Why special words?", "Read “Life Aboard a Sailing Ship.”", ["Act out port and starboard facing the front of the room."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Mixing up port and starboard."], ["Port and left both have four letters."], ["Build a labeled model ship."]),
    summary="Content words like bow, stern, port, and starboard are defined by context and diagrams.")

# ================================================================= Week 2 · Analyze text structure (Chapter 2)
L5 = Lesson("4.5", "Poems, Drama, and Prose",
    "I can explain how poems, drama, and prose are structured differently.", "RL.4.5",
    [("prose", "Ordinary writing in sentences and paragraphs."), ("verse", "Lines of poetry."), ("stanza", "A group of lines in a poem."), ("rhyme", "Words that end with the same sound."),
     ("stage directions", "Notes in a play, usually in italics or parentheses, that tell actors what to do."), ("cast of characters", "The list of characters at the start of a play.")],
    "How would the same story look as a poem, a play, and a chapter?",
    [ReaderAssign(TI, "Chapter 2: The Sea Chest and the Blind Man", "What do Jim and his mother find in the chest? What happens when the pirates arrive?"),
     Text("Stories can be written as <b>prose</b> (sentences and paragraphs), <b>poems</b> (lines and stanzas, often with rhythm and rhyme), or <b>drama</b> (a cast list, dialogue after characters' names, and stage directions)."),
     P_PLAY,
     Figure(lambda t: table(t, [["", "Prose", "Poem", "Drama"], ["Organized in", "paragraphs", "lines and stanzas", "scenes and lines of dialogue"], ["Special features", "narrator", "rhythm, rhyme", "cast list, stage directions"],
                                ["Example", "Treasure Island Reader", "“The Sea Chest”", "“The Captain's Warning”"]], [1.2 * inch, 1.5 * inch, 1.5 * inch, 1.6 * inch], width=5.8 * inch, font_size=9)),
     Example("Find drama features", "“The Captain's Warning”", ["Cast of characters at the top.", "Stage directions in italics and parentheses: (in a low voice).", "Dialogue follows names in capitals; no quotation marks."], "It is drama."),
     KeyIdea("Prose = paragraphs. Poems = lines and stanzas. Drama = cast, dialogue, stage directions.")],
    [Problem("How many stanzas does “The Sea Chest” have?", "3"), Problem("Find a stage direction in the scene.", "(in a low voice), (entering with a tray), (to the audience)"), Problem("Do plays use quotation marks for dialogue?", "No")],
    [S("Warm-Up", [SA("A group of lines in a poem", "stanza"), SA("Notes telling actors what to do", "stage directions")], cols=2),
     S("Identify Structures", [SA(q, a) for q, a in [("Lines with rhyme in stanzas", "poem"), ("JIM: Who's there?", "drama"), ("Paragraphs with a narrator", "prose"), ("(She slams the door.)", "drama (stage direction)")]], cols=2),
     S("Compare", [OR("How does the scene show the captain's fear differently from a prose narrator? Use one stage direction.", "Stage directions like “(in a low voice)” and “gripping his mug” show his fear through action instead of a narrator telling us.", lines=3)], passage=P_PLAY),
     S("Exit Ticket", [OR("Write two lines of a play showing Jim and his mother opening the sea chest in Chapter 2. Include a stage direction.", "Answers vary; names, dialogue, stage direction in parentheses.", lines=3)])],
    te("Students compare poems, drama, and prose.", "Explain major differences between poems, drama, and prose and refer to their structural elements.", "Treasure Island Reader (Chapter 2), workbook Lesson 4.5",
       "Same story, three forms?", ["Read Chapter 2.", "Act out “The Captain's Warning.”"], ["Teach the structure chart."], "Your Turn 1–3.",
       ["Reading stage directions aloud as dialogue."], ["Highlight stage directions in a different color."], ["Perform the scene for the family."]),
    summary="Prose: paragraphs. Poems: lines, stanzas, rhyme. Drama: cast, dialogue, stage directions.")

L6 = Lesson("4.6", "Writing a Scene: From Story to Drama",
    "I can turn a scene from a story into drama.", "RL.4.5, W.4.3",
    [],
    "What changes when you turn a chapter into a play?",
    [Text("To turn prose into drama: list the cast, set the scene in stage directions, turn the narration into dialogue and actions, and remove the narrator's explanations."),
     Example("Prose to drama", "Prose: Jim's mother was frightened, but she insisted on taking only the money they were owed.",
             ["Cast: JIM, MOTHER.", "Stage direction: (Mother's hands shake as she counts coins.)", "Dialogue: MOTHER: I'm an honest woman. I'll take what's owed and not a penny more."],
             "MOTHER: (hands shaking as she counts coins) I'm an honest woman, Jim. I'll take what we're owed and not a penny more."),
     KeyIdea("In drama, show feelings through dialogue and stage directions instead of a narrator.")],
    [Problem("What replaces the narrator in a play?", "dialogue and stage directions"), Problem("Where do you list characters?", "at the top, in the cast of characters"), Problem("How do you show a character is scared in a play?", "stage directions (trembling) and dialogue")],
    [S("Warm-Up", [SA("Two parts of drama", "dialogue, stage directions"), SA("Punctuation for stage directions", "parentheses (and italics)")], cols=2),
     S("Write a Scene", [OR("Turn a moment from Chapter 2 into a short play scene (8–12 lines). Include a cast list, a setting stage direction, dialogue, and at least two more stage directions.",
                            "Answers vary.", lines=16, note="1 point each: cast list; setting; dialogue matches the chapter; two stage directions; correct format.")]),
     S("Exit Ticket", [OR("What was hardest about turning prose into drama?", "Answers vary.", lines=2)])],
    te("Students turn prose into drama.", "Explain differences between drama and prose; write narratives.", "Workbook Lesson 4.6",
       "What changes?", "Reread a key Chapter 2 moment.", ["Model prose-to-drama."], "Plan a scene together.",
       ["Keeping narrator sentences in the play."], ["Two-column prose/drama chart."], ["Perform the scenes."], independent="Write the scene."),
    summary="In drama, dialogue and stage directions do the narrator's job.")

L7 = Lesson("4.7", "Informational Text Structures",
    "I can identify how an informational text is organized.", "RI.4.5",
    [("text structure", "How an author organizes information."), ("chronological", "In time order."), ("cause and effect", "Shows why something happened and its results."),
     ("compare and contrast", "Shows how things are alike and different."), ("problem and solution", "Shows a problem and how it was solved.")],
    "Why might an author organize information in time order instead of by problem and solution?",
    [Text("Authors choose a <b>structure</b> that fits their purpose. Signal words help you identify it."),
     Figure(lambda t: table(t, [["Structure", "Signal words"], ["Chronological", "first, then, in 1716, later, finally"], ["Compare and contrast", "both, however, on the other hand, unlike, similarly"],
                                ["Cause and effect", "because, so, as a result, therefore"], ["Problem and solution", "problem, to solve, solution, fixed"]], [1.8 * inch, 3.6 * inch], width=5.4 * inch)),
     P_STRUCTS,
     Example("Identify the structure", "Paragraph 3", ["Signal words: Because, As a result, When…", "It explains why scurvy happened and what fixed it."], "Cause and effect"),
     KeyIdea("Find signal words, then ask: Is the author telling order, comparing, explaining causes, or solving a problem?")],
    [Problem("Structure of paragraph 1", "chronological"), Problem("Structure of paragraph 2", "compare and contrast"), Problem("Structure of paragraph 4", "problem and solution")],
    [S("Warm-Up", [SA("Signal word for contrast", "however, unlike"), SA("Signal word for cause", "because")], cols=2),
     S("Name the Structure", [MC(f"Paragraph {i}: Which structure?", ["chronological", "compare and contrast", "cause and effect", "problem and solution"], i - 1) for i in range(1, 5)], passage=P_STRUCTS),
     S("Signal Words", [OR("Copy two signal words from paragraph 2 and two from paragraph 1.", "Par. 2: both, however, on the other hand. Par. 1: by 1717, in 1718, later.", lines=2)]),
     S("Exit Ticket", [OR("Which structure does “How a Medieval Cathedral Was Built” (Lesson 3.6) mostly use? How do you know?", "chronological (sequence); first, next, then, finally", lines=2)])],
    te("Students identify text structures.", "Describe the overall structure of events, ideas, concepts, or information in a text.", "Workbook Lesson 4.7",
       "Why time order?", "Read the four paragraphs.", ["Teach structures and signal words."], "Your Turn 1–3.",
       ["Identifying structure from one word only."], ["Highlight signal words."], ["Find each structure in a science book."]),
    summary="Chronological, compare and contrast, cause and effect, problem and solution.")

L8 = Lesson("4.8", "Text Structures and Graphic Organizers",
    "I can use a graphic organizer that matches a text's structure to take notes.", "RI.4.5",
    [("graphic organizer", "A chart or diagram that organizes information.")],
    "What kind of chart would help you take notes on a timeline? On a comparison?",
    [Text("Each structure has a graphic organizer that fits: <b>timeline</b> (chronological), <b>Venn diagram</b> or T-chart (compare and contrast), <b>cause → effect arrows</b>, and <b>problem/solution boxes</b>."),
     Figure(lambda t: table(t, [["Pirates", "Both", "Navy sailors"], ["voted for captain; shared treasure", "lived on ships; faced storms and disease", "worked for a government; paid wages"]],
                            [W * 0.31] * 3, width=W * 0.93)),
     Example("Choose an organizer", "Notes on paragraph 1 (Blackbeard)", ["Structure: chronological.", "Organizer: timeline: 1716 → 1717 → 1718 → later 1718."], "A timeline"),
     KeyIdea("Match the organizer to the structure. It makes notes clear and easy to study.")],
    [Problem("Organizer for cause and effect", "cause → effect arrows (flowchart)"), Problem("Organizer for compare and contrast", "Venn diagram or T-chart"), Problem("Organizer for chronological", "timeline")],
    [S("Warm-Up", [SA("Organizer for problem/solution", "problem and solution boxes"), SA("Organizer for chronological", "timeline")], cols=2),
     S("Make Organizers", [OR("Make a cause → effect chain for paragraph 3 (scurvy).", "few fruits/vegetables → scurvy → bleeding gums, weakness; carrying limes/lemons → less scurvy", lines=4),
                           OR("Make problem/solution boxes for paragraph 4 (lighthouses).", "Problem: ships wrecked on rocky coasts at night. Solution: lighthouses with bright lamps warned sailors.", lines=3)]),
     S("Chapter 2", [OR("Make a timeline of three to four events in Chapter 2.", "Answers vary.", lines=4)]),
     S("Exit Ticket", [OR("Which organizer helps you study best? Why?", "Answers vary.", lines=2)])],
    te("Students use structure-based organizers.", "Describe the overall structure of information in a text.", "Workbook Lesson 4.8",
       "Which chart?", "Reread the four paragraphs.", ["Model a Venn diagram and timeline."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Using a timeline for a comparison."], ["Match structure first."], ["Make organizers for a history chapter."]),
    summary="Timeline, Venn diagram, cause → effect, problem → solution.")

# ================================================================= Week 3 · Purpose and viewpoint (Chapter 3)
L9 = Lesson("4.9", "Author's Purpose",
    "I can identify an author's purpose and explain how I know.", "RI.4.8, RL.4.6",
    [("author's purpose", "The reason an author writes: to persuade, inform, or entertain."), ("persuade", "Try to convince readers to think or do something.")],
    "Why would an author write an advertisement? A science article? A ghost story?",
    [ReaderAssign(TI, "Chapter 3: The Real Adventure Begins", "What do the doctor and squire find in the packet? What do they decide to do?"),
     Text("Authors write to <b>persuade</b>, <b>inform</b>, or <b>entertain</b> (P-I-E). Some texts have more than one purpose. Look at the type of text, word choice, and what the author wants you to do or know."),
     P_AD,
     Example("Identify the purpose", "“WANTED: Brave Sailors!”", ["Commands: Join! Sign up today!", "Positive opinion words: finest, fair, best, adventure of a lifetime.", "Goal: get readers to join."], "to persuade"),
     KeyIdea("Persuade → wants you to act or believe. Inform → teaches facts. Entertain → tells a story for enjoyment.")],
    [Problem("Purpose of “Life Aboard a Sailing Ship”", "inform"), Problem("Purpose of “The Footsteps”", "entertain"), Problem("Which words in the ad are opinions?", "finest, fair, best, adventure of a lifetime")],
    [S("Warm-Up", [SA("P-I-E stands for", "persuade, inform, entertain"), SA("Purpose of a recipe", "inform")], cols=2),
     S("What's the Purpose?", [SA(q, a) for q, a in [("A poster: “Vote for Maria for class president!”", "persuade"), ("An article on how volcanoes form", "inform"),
                                                      ("A funny story about a talking parrot", "entertain"), ("A letter asking the mayor to build a park", "persuade")]], cols=2),
     S("Use the Ad", [OR("What does the ad leave out that a sailor might want to know? Why might the writer leave it out?", "Dangers, hard food, harsh punishment; it would make people not want to join.", lines=3,
                         note="Connect to Lesson 4.4: harsh punishment, salted meat.")], passage=P_AD),
     S("Exit Ticket", [OR("What is the purpose of Treasure Island? Explain.", "to entertain; it's an exciting adventure story", lines=2)])],
    te("Students identify author's purpose.", "Explain how an author uses reasons and evidence to support points.", "Treasure Island Reader (Chapter 3), workbook Lesson 4.9",
       "Why write an ad?", ["Read Chapter 3.", "Read the ad."], ["Teach PIE.", "Model the ad."], "Your Turn 1–3.",
       ["Thinking a story with facts must be informational."], ["Ask: What does the author want me to do?"], ["Write an ad for the Hispaniola from Silver's viewpoint."]),
    summary="Authors write to persuade, inform, or entertain.")

L10 = Lesson("4.10", "Firsthand and Secondhand Accounts",
    "I can compare a firsthand and a secondhand account of the same event.", "RI.4.6",
    [("firsthand account", "Told by someone who was there (I, we)."), ("secondhand account", "Told by someone who learned about it from others or research.")],
    "Would you learn something different about a storm from a kid who lived through it than from a news report?",
    [Text("A <b>firsthand account</b> gives feelings and personal details. A <b>secondhand account</b> gives facts, numbers, and a bigger picture. Comparing both gives the fullest understanding."),
     P_FIRST, P_SECOND,
     Figure(lambda t: table(t, [["", "Account A (firsthand)", "Account B (secondhand)"], ["Point of view", "first person (I)", "third person"], ["Focus", "feelings, personal experience", "facts, numbers, the whole town"],
                                ["Example detail", "wind “screaming like a train”", "winds of 120 mph"]], [1.2 * inch, 2.2 * inch, 2.2 * inch], width=5.6 * inch)),
     KeyIdea("Firsthand: feelings and personal view. Secondhand: facts and the bigger picture.")],
    [Problem("Which account tells how the writer felt?", "Account A"), Problem("Which gives the wind speed?", "Account B"), Problem("Is a diary firsthand or secondhand?", "firsthand")],
    [S("Warm-Up", [SA("Pronouns in a firsthand account", "I, we"), SA("Is an encyclopedia firsthand?", "No, secondhand")], cols=2),
     S("Compare the Accounts", [OR("What does Account A tell you that Account B does not?", "personal feelings: fear, huddling in the tub, feeling lucky and scared", lines=2),
                                OR("What does Account B tell you that Account A does not?", "facts: date, wind speed, 200 homes damaged, no serious injuries, repairs take months", lines=2),
                                OR("Why is it useful to read both?", "Together they give feelings and facts, a full picture.", lines=2)]),
     S("Chapter 3", [OR("Is Treasure Island told as a firsthand or secondhand account? How do you know?", "Firsthand: Jim tells it as “I.”", lines=2)]),
     S("Exit Ticket", [OR("Write two sentences giving a firsthand account of something that happened this week.", "Answers vary; uses I/we.", lines=2)])],
    te("Students compare firsthand and secondhand accounts.", "Compare and contrast a firsthand and secondhand account of the same event; describe differences in focus.", "Workbook Lesson 4.10",
       "Kid vs news report.", "Read both accounts.", ["Model the comparison chart."], "Your Turn 1–3.",
       ["Thinking secondhand means less true."], ["Both can be true; they focus differently."], ["Interview a relative (firsthand) and compare with an article."]),
    summary="Firsthand accounts give feelings; secondhand accounts give facts and the big picture.")

L11 = Lesson("4.11", "Characters' Points of View",
    "I can explain how different characters see the same events differently.", "RL.4.6, RL.4.3",
    [("perspective", "How a character sees and feels about events.")],
    "If you and your sibling both describe the same argument, will your stories match?",
    [Text("Characters have different <b>perspectives</b> because of who they are, what they want, and what they know. Compare what each character says and does about the same event."),
     Example("Compare perspectives", "Chapter 3: the treasure map",
             ["Squire Trelawney: excited, wants to buy a ship and sail right away; talks openly about the treasure.", "Dr. Livesey: interested but cautious; warns the squire to keep quiet.", "Jim: thrilled to be going on an adventure."],
             "Each character reacts to the map differently because of his personality."),
     KeyIdea("Different characters see the same event in different ways. Use their words and actions as evidence.")],
    [Problem("How does Squire Trelawney feel about the map?", "very excited"), Problem("Why is Dr. Livesey worried about the squire?", "He talks too much and might tell the wrong people."), Problem("Whose perspective do readers mainly see in Treasure Island?", "Jim's")],
    [S("Warm-Up", [SA("What is perspective?", "how a character sees events"), SA("Narrator of Treasure Island", "Jim")], cols=2),
     S("Two Perspectives", [OR("Chapter 2: How might Jim's mother describe the night the pirates came differently from Jim?", "Answers vary, e.g. she would focus on protecting Jim and being honest about the money; Jim on the excitement and fear.", lines=3),
                            OR("Chapter 3: Compare how the squire and the doctor react to the treasure map. Give evidence for each.", "Answers vary; squire excited/talkative; doctor careful.", lines=4)]),
     S("Exit Ticket", [OR("Retell one event from Chapter 3 from the squire's point of view in two sentences.", "Answers vary; first person as the squire.", lines=3)])],
    te("Students compare characters' perspectives.", "Compare and contrast points of view; describe characters in depth.", "Workbook Lesson 4.11",
       "Sibling argument.", "Reread the map scene in Chapter 3.", ["Model comparing perspectives."], "Your Turn 1–3.",
       ["Assuming all characters think like the narrator."], ["Character feelings chart."], ["Write a diary entry as Dr. Livesey."]),
    summary="Characters' perspectives differ; use their words and actions as evidence.")

L12 = Lesson("4.12", "Facts, Opinions, and Persuasive Language",
    "I can tell facts from opinions and recognize persuasive techniques.", "RI.4.8",
    [("fact", "A statement that can be proved true."), ("opinion", "A statement of what someone thinks or feels."), ("loaded words", "Words with strong positive or negative feelings, used to persuade.")],
    "Is “Pizza is the best food” a fact or an opinion? How could you check?",
    [Text("A <b>fact</b> can be checked. An <b>opinion</b> tells a belief. Persuasive writers mix them and use <b>loaded words</b> (finest, terrible), <b>exaggeration</b>, and <b>calls to action</b> (Sign up now!)."),
     Example("Sort statements", "From the sailor ad", ["“Join the crew of the Hispaniola.”: a command (call to action).", "“Our cook makes the best stew on the seven seas.”: opinion with exaggeration.", "“The ship sails from Bristol.”: a fact (could be checked)."],
             "Most of the ad is opinion and persuasion, not fact."),
     KeyIdea("Ask: Can this be proved? Watch for loaded words, exaggeration, and calls to action.")],
    [Problem("Fact or opinion: Winds reached 120 mph.", "fact"), Problem("Fact or opinion: The Hispaniola is the finest ship.", "opinion"), Problem("Name a loaded word from the ad.", "finest, best, bravest")],
    [S("Warm-Up", [SA("Can a fact be proved?", "Yes"), SA("A call to action", "Sign up today!")], cols=2),
     S("Fact or Opinion?", [SA(q, a) for q, a in [("Treasure Island was published in 1883.", "fact"), ("Treasure Island is the most exciting book ever.", "opinion"),
                                                  ("Pirates attacked ships carrying gold.", "fact"), ("Pirates were the coolest people in history.", "opinion"), ("A ship's kitchen is called a galley.", "fact"),
                                                  ("Hard biscuits taste awful.", "opinion")]], cols=2),
     S("Write", [OR("Rewrite the sailor ad as an honest, informational notice with only facts.", "e.g. The Hispaniola, sailing from Bristol, needs sailors for a long voyage. Pay is offered. Apply at the docks.", lines=4)]),
     S("Exit Ticket", [OR("Write one fact and one opinion about Long John Silver.", "Answers vary.", lines=2)])],
    te("Students distinguish fact and opinion and persuasive techniques.", "Explain how an author uses reasons and evidence to support points.", "Workbook Lesson 4.12",
       "Pizza: fact or opinion?", "Reread the ad.", ["Teach persuasive techniques.", "Model sorting statements."], "Your Turn 1–3. Weekly Check tomorrow.",
       ["Calling any statement with a number a fact."], ["Ask: Could I check this?"], ["Analyze a real cereal box."]),
    summary="Facts can be proved; opinions can't. Persuasion uses loaded words and calls to action.")

# ================================================================= Week 4 · Compare craft and structure (Chapter 4)
L13 = Lesson("4.13", "How Authors Build Suspense",
    "I can explain how an author builds suspense with word choice and structure.", "RL.4.5, RL.4.4",
    [("suspense", "A feeling of worry or excitement about what will happen next."), ("cliffhanger", "An ending that leaves the reader in suspense.")],
    "What makes you want to keep turning pages?",
    [ReaderAssign(TI, "Chapter 4: What I Heard in the Apple Barrel", "What does Jim overhear? How does the author make this chapter tense?"),
     Text("Authors build <b>suspense</b> with short sentences, sensory details, slow pacing at tense moments, characters hiding or waiting, and <b>cliffhangers</b> at the ends of chapters."),
     P_SUSPENSE,
     Example("Find suspense techniques", "“Then she heard it: a footstep. Then another. Slow. Heavy. Coming closer.”", ["Short sentences and fragments slow the reader.", "Sound details (footsteps) build tension.", "“Coming closer” makes us worry."],
             "Short sentences and sound details build suspense."),
     KeyIdea("Short sentences, sensory details, hiding, waiting, and cliffhangers build suspense.")],
    [Problem("Why is the setting spooky?", "alone after closing; buzzing lights; rain"), Problem("How is the suspense released?", "The footsteps are Mr. Diaz, the custodian."), Problem("Why is Jim's hiding place in Chapter 4 suspenseful?", "If Silver finds him listening, he could be in danger.")],
    [S("Warm-Up", [SA("What is suspense?", "worry about what will happen next"), SA("What is a cliffhanger?", "an ending that leaves you in suspense")], cols=2),
     S("Use the Passage", [OR("List three techniques the author uses to build suspense. Give an example of each.", "short sentences (“Slow. Heavy.”), sensory details (lights buzzed, rain tapped), hiding (crouched behind the shelf), shadow", lines=4),
                           OR("Why does the author have Ana laugh at the end?", "to release the tension; she was relieved", lines=2)], passage=P_SUSPENSE),
     S("Chapter 4", [OR("What does Jim overhear in the apple barrel? How does the author make the moment tense?", "Silver plotting mutiny to take the treasure; Jim hiding, can't move, hearing dangerous plans.", lines=4)]),
     S("Exit Ticket", [OR("Write a two-sentence cliffhanger.", "Answers vary.", lines=2)])],
    te("Students analyze suspense.", "Explain how a series of chapters, scenes, or stanzas fits together; determine meaning of words and phrases.", "Treasure Island Reader (Chapter 4), workbook Lesson 4.13",
       "Page-turners.", ["Read Chapter 4.", "Read “The Footsteps.”"], ["Teach suspense techniques."], "Your Turn 1–3.",
       ["Saying “it's exciting” without naming techniques."], ["Technique checklist."], ["Rewrite a calm paragraph to add suspense."]),
    summary="Authors build suspense with short sentences, sensory details, hiding, and cliffhangers.")

L14 = Lesson("4.14", "Comparing Text and Illustration",
    "I can compare a text with an illustration or performance of it.", "RL.4.7",
    [("illustration", "A picture that goes with a text."), ("interpretation", "An artist's or performer's own way of showing a text.")],
    "Have you ever seen a movie of a book and thought, “That's not how I pictured it”?",
    [Text("Illustrators, actors, and filmmakers make choices about how characters look and sound. Compare what the text says with what the picture or performance shows. What did the artist add, change, or leave out?"),
     Example("Compare", "Text: the captain has “a tarry pigtail,” a “soiled blue coat,” and a “sabre cut across one cheek.” Look at the illustration of the captain in your Reader.",
             ["Check each detail: pigtail? blue coat? scar?", "What did the illustrator add (a hat? a parrot?)", "Does the picture match the mood?"], "Answers depend on the Reader's illustration; list matches and differences."),
     KeyIdea("Compare the text's details with the illustration or performance: what matches, what was added, what was left out?")],
    [Problem("Name two details from the text to look for in the illustration.", "pigtail, blue coat, sabre scar, sea chest"), Problem("What is an interpretation?", "an artist's own way of showing a text"), Problem("Why might an illustrator add details?", "to show mood or make the picture interesting")],
    [S("Warm-Up", [SA("What is an illustration?", "a picture that goes with a text"), SA("Movie of a book: does it always match?", "No")], cols=2),
     S("Compare", [OR("Choose an illustration from Chapters 1–4 of your Reader. List two details that match the text.", "Answers vary.", lines=3),
                   OR("List one thing the illustrator added or changed.", "Answers vary.", lines=2),
                   Problem("Draw your own picture of Long John Silver using details from Chapter 3 or 4. Label two details from the text.", "Answers vary; labeled details from the text.", space=170, wide=True)]),
     S("Exit Ticket", [OR("Listen to someone read part of Chapter 4 aloud with expression. What did their voice add that the page alone doesn't?", "Answers vary: mood, emotion, tension.", lines=2)])],
    te("Students compare text with illustrations and oral readings.", "Make connections between the text of a story and a visual or oral presentation of the text.", "Treasure Island Reader illustrations, workbook Lesson 4.14",
       "Movie vs book.", "Read the captain description; view the illustration.", ["Model a match/added/left-out chart."], "Your Turn 1–3.",
       ["Judging pictures only on whether they are “good.”"], ["Detail checklist from the text."], ["Listen to an audio version of a chapter and compare."]),
    summary="Compare a text with an illustration or performance: matches, additions, omissions.")

L15 = Lesson("4.15", "Comparing Fiction and Nonfiction on the Same Topic",
    "I can compare how a story and an informational text treat the same topic.", "RL.4.9, RI.4.9",
    [],
    "Are the pirates in Treasure Island like real pirates?",
    [Text("A story and an informational text can teach different things about the same topic. Fiction may exaggerate or invent details for excitement. Informational texts give facts."),
     P_PIRATES,
     Example("Compare", "Treasure maps", ["Treasure Island: the story centers on a treasure map with an X.", "Informational text: treasure maps “were mostly invented by writers.”", "Real pirates usually spent treasure quickly."],
             "Stevenson's story made treasure maps famous, but real pirates rarely buried treasure or drew maps."),
     KeyIdea("Compare fiction and nonfiction: What's the same? What did the story invent or exaggerate?")],
    [Problem("Did real pirates usually bury treasure?", "No; they spent it quickly."), Problem("How did pirate crews make decisions?", "They voted."), Problem("What did the story invent that real pirates rarely had?", "treasure maps marked with X / buried treasure")],
    [S("Warm-Up", [SA("Fiction or nonfiction: Treasure Island", "fiction"), SA("Fiction or nonfiction: “Real Pirates”", "nonfiction")], cols=2),
     S("Compare", [OR("How are Long John Silver's plans similar to what real pirates did?", "He plans to take over the ship and its treasure; real pirates attacked ships for treasure and voted on leaders.", lines=3),
                   OR("Name one way Treasure Island differs from real pirate history. Use evidence from the informational text.", "Buried treasure and a map; the text says most pirates did not bury treasure and maps were mostly invented.", lines=3)], passage=P_PIRATES),
     S("Exit Ticket", [OR("Why do you think writers invented buried treasure and treasure maps?", "They make stories more exciting and mysterious.", lines=2)])],
    te("Students compare fiction and nonfiction on a topic.", "Integrate information from two texts on the same topic.", "Workbook Lesson 4.15",
       "Real pirates?", "Read “Real Pirates of the Golden Age.”", ["Model the treasure-map comparison."], "Your Turn 1–3.",
       ["Assuming fiction details are real history."], ["T-chart: story vs facts."], ["Research a real pirate."]),
    summary="Stories may invent or exaggerate; informational texts give facts.")

L16 = Lesson("4.16", "Writing a Comparison Paragraph",
    "I can write a paragraph comparing two texts.", "W.4.9, W.4.2",
    [],
    "What words help readers follow a comparison?",
    [Text("A comparison paragraph has a topic sentence naming both texts and the point of comparison, details from each text, comparison transitions (<i>both, similarly, however, unlike, on the other hand</i>), and a conclusion."),
     Example("Comparison paragraph", "Compare pirates in Treasure Island and “Real Pirates of the Golden Age.”",
             ["Topic sentence: Both texts are about pirates, but they show them differently.", "Similar: both describe pirates who want treasure.", "Different: Treasure Island has a buried treasure map; real pirates rarely buried treasure.", "Conclusion."],
             "Both Treasure Island and “Real Pirates of the Golden Age” show pirates hunting for treasure. However, Treasure Island centers on a buried treasure and a map, while the informational text explains that real pirates usually spent their treasure quickly. The story makes pirates exciting, but the article shows they were real people with rules and dangerous lives."),
     KeyIdea("Name both texts, use comparison transitions, and give evidence from each.")],
    [Problem("Name two comparison transitions.", "both, similarly, however, unlike"), Problem("What must the topic sentence include?", "both texts and the point of comparison"), Problem("How many texts need evidence?", "both")],
    [S("Warm-Up", [SA("Transition for similarity", "both, similarly"), SA("Transition for difference", "however, unlike")], cols=2),
     S("Write", [OR("Compare Account A and Account B (Lesson 4.10) OR Treasure Island and “Real Pirates.” Write a comparison paragraph with evidence from both texts.", "Answers vary.", lines=12,
                    note="1 point each: topic sentence names both texts; evidence from text 1; evidence from text 2; comparison transitions; conclusion.")]),
     S("Exit Ticket", [OR("Which skill from this unit will help you most as a writer?", "Answers vary.", lines=2)])],
    te("Students write comparison paragraphs.", "Draw evidence from texts; write informative texts.", "Workbook Lesson 4.16, Unit 4 Review",
       "Comparison words.", "Reread the pirates text.", ["Model the paragraph."], "Plan together.",
       ["Writing about only one text."], ["Two-column plan."], ["Write a second comparison."], independent="Write the paragraph; then the Unit 4 Review.", exit_="Exit Ticket. Tomorrow: Unit 4 Test."),
    summary="Comparison paragraphs name both texts, use transitions, and give evidence from each.")

# ================================================================= checks
C1 = Check("Weekly Check 10: Words and Phrases", [S("Read and answer", [
    OR("“The lighthouse stood like a giant candle.” Simile or metaphor? What does it mean?", "simile; the lighthouse was tall and bright", lines=2),
    OR("What does “a heart of gold” mean?", "very kind", lines=1),
    OR("“His temper was a volcano.” What does this tell you about Mr. Fenn?", "He got very angry suddenly and loudly.", lines=1),
    OR("Why is climbing 120 stairs every night called “Herculean”?", "It took great strength and effort, like Hercules' labors.", lines=2),
    MC("What mood does the first paragraph create?", ["silly", "calm and steady", "angry"], 1)], passage=P_C10)], minutes=20)

C2 = Check("Weekly Check 11: Text Structure", [S("Read and answer", [
    MC("This text is an example of…", ["prose", "a poem", "drama"], 2),
    OR("Copy one stage direction.", "(not moving), (sitting down beside her), (uncrossing her arms), (pause)", lines=1),
    OR("How do the stage directions show Maya's feelings change?", "At first her arms are crossed and she won't move; at the end she uncrosses her arms and helps.", lines=3),
    OR("Why does Maya change her mind? Use evidence.", "Dad shares that he was scared to move too but met his best friend.", lines=2),
    MC("Which structure fits this sentence: “Because it rained, the game was canceled”?", ["chronological", "compare and contrast", "cause and effect"], 2)], passage=P_C11)], minutes=20)

C3 = Check("Weekly Check 12: Purpose and Point of View", [S("Read and answer", [
    MC("This journal is a…", ["firsthand account", "secondhand account"], 0),
    OR("What clue tells you?", "It uses I and tells the writer's own experience and feelings.", lines=1),
    OR("Write one fact and one opinion from the journal.", "Fact: I won second place / poured vinegar. Opinion: the lava bubbled over perfectly.", lines=2),
    MC("What is the main purpose of a journal entry?", ["to persuade", "to record and share personal experiences", "to sell something"], 1),
    OR("How would a newspaper article about the science fair be different?", "secondhand, third person, facts about all winners, no personal feelings", lines=2)], passage=P_C12)], minutes=20)

REVIEW = Check("Unit 4 Review", [
    S("Skills", [SA("Achilles' heel means", "a weak spot"), SA("Structure with “however” and “both”", "compare and contrast"), SA("Part of a play telling actors what to do", "stage directions"),
                 SA("PIE", "persuade, inform, entertain"), SA("Firsthand pronouns", "I, we"), SA("Two suspense techniques", "short sentences, cliffhangers")], cols=2),
    S("Apply", [OR("Reread “The Footsteps.” Turn the last paragraph into two lines of drama with a stage direction.", "e.g. MR. DIAZ: (holding an umbrella) Ana? Your mom is waiting outside. ANA: (laughing loudly) You scared me!", lines=3),
                OR("Write a topic sentence comparing how “The Footsteps” and “The Captain's Warning” build suspense.", "e.g. Both build suspense, but “The Footsteps” uses short sentences and sounds, while the play uses stage directions and the captain's warning.", lines=2)])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 4 Test", [
    S("Part A · Words and craft (1 point each)", [
        OR("“The fog rolled in thick and gray, swallowing the harbor whole.” What does “swallowing” mean here?", "covering it completely so it couldn't be seen", lines=1),
        OR("List two sensory details in paragraph 2 and the mood they create.", "sails in rags, green moss, no lanterns, no sound; spooky/eerie", lines=2),
        OR("Explain two techniques the author uses to build suspense in paragraphs 1–3.", "fog hiding things; silence; slow-drifting ship; Tomás's whisper and white knuckles", lines=2, points=2),
        MC("“Hard to starboard!” means turn the ship…", ["left", "right", "around backward"], 1),
        OR("What does Tomás's grip on the rail show?", "He was terrified.", lines=1)], passage=P_TEST),
    S("Part B · Structure and point of view (1 point each)", [
        MC("This story is told in…", ["first person", "third person"], 1),
        OR("How does the last paragraph change the mood?", "The mystery is explained; fear turns to relief (with a little humor about Tomás).", lines=2),
        OR("How do Captain Rosa and Tomás see the ship differently?", "Rosa is scared but stays calm and acts; Tomás believes it's a ghost ship.", lines=2),
        MC("What is the author's main purpose?", ["to persuade", "to inform", "to entertain"], 2)]),
    S("Part C · Write (5 points)", [OR("Rewrite paragraphs 3–4 as a short drama scene with a cast list, stage directions, and dialogue. Then write one sentence explaining what the stage directions show about the characters.",
                                       "Rubric: cast list (1); stage directions (1); dialogue faithful to the story (1); correct drama format (1); explanation sentence (1).", lines=14, points=5)])],
    kind="test", minutes=45, rubric=[["13–15 (85%+)", "Mastered."], ["10–12", "Proficient; review missed skills."], ["Below 10", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-01-25", "2027-02-01", "2027-02-08", "2027-02-15"], CHECKS, REVIEW, TEST)

UNIT = Unit(4, "The Writer's Craft", "Words and phrases, structure, purpose and point of view, and comparing texts, with Treasure Island Chapters 1–4.",
    "Every author makes choices: which words to use, how to organize ideas, whose eyes to tell the story through, and how to keep readers turning pages. In this unit you'll board the <i>Hispaniola</i> with Jim Hawkins and study the craft that makes <i>Treasure Island</i> one of the most famous adventure stories ever written.",
    ["Interpret old-fashioned language, allusions to mythology, and sensory language.", "Compare poems, drama, and prose; identify informational text structures.",
     "Identify author's purpose; compare firsthand and secondhand accounts and character perspectives.", "Analyze suspense and compare texts, illustrations, fiction, and nonfiction."],
    [("RL.4.4, RI.4.4", "Determine the meaning of words and phrases, including allusions and content words."), ("RL.4.5, RI.4.5", "Explain structural differences; describe text structures."),
     ("RL.4.6, RI.4.6", "Compare points of view; compare firsthand and secondhand accounts."), ("RL.4.7, RL.4.9, RI.4.8, RI.4.9", "Connect text to visuals; compare texts; evaluate reasons and evidence.")],
    [("allusion", "A reference to a well-known story."), ("mood", "The feeling a text creates."), ("stage directions", "Notes telling actors what to do."), ("text structure", "How information is organized."),
     ("firsthand account", "Told by someone who was there."), ("suspense", "Worry about what happens next.")],
    ["Unit 3: reading longer texts and point of view."], ["Treasure Island Reader (Chapters 1–4)", "Colored pencils for organizers"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Recognizing persuasion protects you from misleading ads, and understanding structure helps you study any textbook.",
    family_note="Watch or listen to a version of Treasure Island together and talk about what the filmmakers or narrators changed.",
    weeks=WEEKS)
