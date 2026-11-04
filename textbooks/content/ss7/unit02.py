"""Grade 7 Social Studies · Unit 2: River Valley Civilizations — ancient Egypt and Kush, the Indus Valley, Hinduism,
Buddhism, and the Maurya Empire, ancient China from the Shang to the Han, and comparing the first civilizations (Tue/Thu)."""
from engine import *
from content.sskit import S, MC, OR, SA, tss, make_test, weeks_for, check, review
from geomap import geo_map


def nile(t, width=None, title="The Nile Valley"):
    labs = [("Giza", 31.13, 29.98, "city"), ("Memphis", 31.25, 29.85, "city", 0, -10), ("Thebes", 32.64, 25.70, "city"), ("Napata", 31.82, 18.53, "city"), ("Meroë", 33.75, 16.94, "city"),
            ("LOWER EGYPT", 30.0, 31.0, "region"), ("UPPER EGYPT", 33.6, 26.6, "region"), ("KUSH", 34.9, 18.2, "region"), ("Mediterranean Sea", 29.0, 33.0, "water"),
            ("Red Sea", 37.4, 22.6, "water"), ("Nile R.", 30.7, 24.0, "water"), ("SAHARA", 27.0, 22.0, "plain")]
    return geo_map(t, (24, 40, 14, 33.5), width=width or W * 0.42, rivers=("Nile",), labels=labs, title=title, scale_miles=200)


def indus(t, width=None, title="The Indus and Ganges valleys"):
    labs = [("Harappa", 72.86, 30.63, "city"), ("Mohenjo-daro", 68.14, 27.33, "city"), ("Pataliputra", 85.14, 25.6, "city"), ("Indus R.", 70.4, 25.2, "water"),
            ("Ganges R.", 81.5, 26.6, "water"), ("HIMALAYAS", 82.5, 31.3, "plain"), ("Arabian Sea", 64.5, 20.5, "water"), ("Bay of Bengal", 89.0, 19.0, "water")]
    return geo_map(t, (60, 92, 17, 37), width=width or W * 0.75, rivers=("Indus", "Ganges"), labels=labs, title=title, scale_miles=300)


def huang(t, width=None, title="Ancient China"):
    labs = [("Anyang", 114.35, 36.1, "city"), ("Chang'an (Xi'an)", 108.94, 34.34, "city"), ("Luoyang", 112.45, 34.62, "city", 0, -10), ("Huang He (Yellow R.)", 107.0, 39.2, "water"),
            ("Chang Jiang (Yangtze R.)", 111.5, 29.4, "water"), ("Yellow Sea", 123.0, 35.5, "water"), ("GOBI DESERT", 104.0, 42.5, "plain"), ("TIBETAN PLATEAU", 92.0, 33.0, "plain")]
    return geo_map(t, (86, 126, 26, 44), width=width or W * 0.75, rivers=("Huang", "Yangtze"), labels=labs, title=title, scale_miles=300)


P_ANALECTS = Passage("From the Analects of Confucius", [
    "The Master said, “He who exercises government by means of his virtue may be compared to the north polar star, which keeps its place and all the stars turn towards it.” (2.1)",
    "The Master said, “When you know a thing, to hold that you know it; and when you do not know a thing, to allow that you do not know it; this is knowledge.” (2.17)",
    "The Master said, “What you do not want done to yourself, do not do to others.” (15.23)",
], source="Sayings of Confucius (551–479 BCE), recorded by his students. Translated by James Legge (1861). Public domain.", genre="Primary source", numbered=False)


# ================================================================= Week 1 · Egypt
L1 = Lesson("2.1", "Egypt: Gift of the Nile",
    "I can explain how the Nile River shaped where and how ancient Egyptians lived.", "C3 D2.Geo.4.6-8, D2.His.1.6-8",
    [("delta", "The flat, fan-shaped land where a river splits and flows into the sea."), ("silt", "Fine, rich soil carried and left behind by water."),
     ("inundation", "The yearly flood of the Nile."), ("cataract", "A stretch of rocky rapids in a river."), ("unify", "To bring together into one.")],
    "Egypt gets almost no rain, yet it fed millions of people for thousands of years. How is that possible?",
    [Beside(lambda t: nile(t),
            ["The Greek writer Herodotus called Egypt “the gift of the Nile.” The Nile is the world's longest river, about 4,100 miles. Unlike most rivers, it flows <b>north</b>, from the mountains of East Africa to the Mediterranean Sea.",
             "Almost all Egyptians lived on a narrow green strip along the river. Beyond it lay the Sahara, the “red land” of desert that also protected Egypt from invaders.",
             "Because the Nile flows north, <b>Upper Egypt</b> is in the south and <b>Lower Egypt</b> is in the north, around the <b>delta</b>."], fig_w=0.44),
     Text("Every summer, rains far to the south made the Nile rise. During the <b>inundation</b>, the river spread over its banks. When the water went down in the fall, it left a layer of black <b>silt</b>, and farmers planted wheat, barley, and flax in the “black land.” Farmers used a <b>shaduf</b>, a bucket on a pole, to lift water into irrigation canals. Rocky rapids called <b>cataracts</b> to the south made boat travel difficult there."),
     Figure(lambda t: table(t, [["Feature of the Nile", "How it helped Egyptians"], ["yearly flood and silt", "rich soil for crops and a food surplus"], ["flows north; winds blow south", "boats could float north and sail south: easy trade"],
                                ["papyrus reeds along the banks", "paper, rope, sandals, and boats"], ["deserts on both sides", "natural protection from invaders"]],
                            [2.4 * inch, 3.5 * inch], width=5.9 * inch, font_size=9.5)),
     Text("Around 3100 BCE, a king of Upper Egypt, traditionally called <b>Narmer</b> or Menes, <b>unified</b> Upper and Lower Egypt into one kingdom. Egyptian history is divided into the Old, Middle, and New Kingdoms, with more than 30 ruling families, or dynasties, over about 3,000 years."),
     Investigate("Flood Model", "How did the inundation make farmland?", ["a long pan or tray", "soil", "a cup of muddy water", "a spoon"],
                 ["Spread dry soil in the tray and press a groove for the river.", "Slowly pour the muddy water down the groove until it spills over the banks.", "Let it sit, then pour off the extra water.", "Look at what is left on the “fields.”"],
                 record="a labeled sketch and two sentences explaining how flood silt helped Egyptian farmers."),
     WatchOut("On maps, “Upper” Egypt is at the bottom and “Lower” Egypt is at the top. The names come from the river's flow: upriver is south."),
     KeyIdea("The Nile's yearly flood left rich silt for farming, its current and winds made trade easy, and the deserts protected Egypt. Egypt was unified around 3100 BCE.")],
    [Problem("In which direction does the Nile flow?", "north"), Problem("What did the inundation leave behind?", "rich black silt"), Problem("Why is Upper Egypt in the south?", "It is upriver; the Nile flows north from the south.")],
    [S("Warm-Up", [SA("The yearly Nile flood", "inundation"), SA("Rich soil left by water", "silt")], intro="Write the word for each description.", cols=2),
     S("Practice", [SA(q, a) for q, a in [("What did Egyptians call the desert?", "the red land"), ("What tool lifted water into canals?", "the shaduf"),
                                          ("Name two uses of papyrus.", "e.g. paper, rope, sandals, boats"), ("Who traditionally unified Egypt, and about when?", "Narmer (Menes), about 3100 BCE")]] +
                   [OR("Compare the Nile with the Tigris and Euphrates (Unit 1). Give one similarity and one difference.", "Similar: floods left rich soil and supported farming. Different: the Nile's flood was regular and predictable; Mesopotamia's floods were unpredictable.", lines=3)],
       intro="Answer each question. Use the lesson, the map, and the chart."),
     S("Exit Ticket", [OR("Explain why Herodotus called Egypt “the gift of the Nile.” Use two details.", "e.g. the flood's silt made farming possible in a desert; the river gave water, transport, and papyrus.", lines=3)],
       intro="Answer in complete sentences.")],
    tss("Students explain how the Nile shaped Egyptian civilization.", "Explain how physical geography shaped settlement and economic activity.", "Tray, soil, muddy water, workbook Lesson 2.1",
        "Feeding millions with no rain.", "Read the lesson; study the map.", ["Model the flood cycle.", "Compare with Mesopotamia."], "Check Your Understanding 1–3.",
        ["Upper/Lower Egypt reversed on the map."], ["Flood-cycle diagram: flood, silt, plant, harvest."], ["Research the Aswan High Dam and how it ended the inundation."]),
    summary="The Nile's flood, current, and deserts made Egypt rich, connected, and safe.")

L2 = Lesson("2.2", "Pharaohs, Pyramids, and the Afterlife",
    "I can explain how Egyptian beliefs about pharaohs and the afterlife shaped their government, art, and buildings.", "C3 D2.His.2.6-8, D2.Civ.6.6-8",
    [("pharaoh", "The ruler of ancient Egypt, believed to be a god on Earth."), ("theocracy", "A government ruled by religious leaders or a ruler seen as divine."),
     ("mummy", "A body preserved so it will last a long time."), ("hieroglyphics", "Egyptian writing that used pictures and symbols."),
     ("afterlife", "Life after death.")],
    "Why would people spend 20 years building one tomb?",
    [Text("Egyptians believed their king, the <b>pharaoh</b>, was a god on Earth who kept <i>ma'at</i>: order, truth, and balance. Because the ruler was divine, Egypt was a <b>theocracy</b>. The pharaoh owned all the land, led the army, and ran the government through officials called viziers and scribes."),
     Text("Egyptians were <b>polytheists</b> who worshiped many gods, such as Ra, the sun god, and Osiris, god of the <b>afterlife</b>. They believed the dead needed their bodies in the next life, so priests made <b>mummies</b>, a 70-day process of drying and wrapping the body. Tombs held food, furniture, and treasures for the journey."),
     Text("Old Kingdom pharaohs built <b>pyramids</b> as tombs. The Great Pyramid at <b>Giza</b>, built for the pharaoh <b>Khufu</b> around 2560 BCE, used more than two million stone blocks. Archaeologists have found that it was built by paid, skilled workers and farm laborers during the flood season, not by enslaved armies. Later pharaohs were buried in hidden tombs in the <b>Valley of the Kings</b>, such as the tomb of Tutankhamun, found in 1922."),
     Text("Egyptians wrote with <b>hieroglyphics</b>, more than 700 picture symbols, on stone and papyrus. For centuries no one could read them. Then, in 1799, French soldiers found the <b>Rosetta Stone</b>, carved with the same message in hieroglyphics, a later Egyptian script, and Greek. In 1822, Jean-François Champollion used the Greek to decode the hieroglyphs."),
     Example("Use evidence to make an inference", "Tombs were filled with bread, jars of beer, furniture, games, and small statues of servants.",
             ["Evidence: the objects are things people use in daily life.", "Background: Egyptians believed in an afterlife.", "Inference: they expected the dead to need these things in the next life."],
             "Tomb goods show that Egyptians believed the afterlife was much like life on Earth."),
     Investigate("Cartouche", "How did hieroglyphs represent sounds?", ["paper", "pencil and markers", "a hieroglyph alphabet chart (print one from a museum website)"],
                 ["Draw a long oval with a line at one end: a cartouche, which held a pharaoh's name.", "Spell your name with the hieroglyph sound chart, from top to bottom.", "Decorate the border.", "Trade with a family member and have them decode it."],
                 record="your cartouche and one sentence explaining why the Rosetta Stone mattered."),
     KeyIdea("Egyptians saw the pharaoh as a god, so religion and government were joined. Belief in the afterlife led to mummies, tomb goods, and pyramids. The Rosetta Stone unlocked hieroglyphics.")],
    [Problem("Why was Egypt a theocracy?", "The pharaoh was believed to be a god and ruled the government."), Problem("Why did Egyptians make mummies?", "They believed the dead needed their bodies in the afterlife."),
     Problem("How did the Rosetta Stone help scholars read hieroglyphics?", "It had the same text in Greek, which scholars could read.")],
    [S("Warm-Up", [SA("Life after death", "afterlife"), SA("Egyptian picture writing", "hieroglyphics")], intro="Write the word for each description.", cols=2),
     S("Practice", [SA(q, a) for q, a in [("What was ma'at?", "order, truth, and balance"), ("Which god ruled the afterlife?", "Osiris"),
                                          ("For which pharaoh was the Great Pyramid built?", "Khufu"), ("Who decoded hieroglyphics, and when?", "Champollion, 1822")]] +
                   [OR("What does the way the Great Pyramid was built tell us about Egypt's government and economy? Give two details.", "A strong government could organize and feed thousands of workers; the food surplus from the Nile paid them.", lines=3)],
       intro="Answer each question. Use the lesson."),
     S("Exit Ticket", [OR("How were religion and government connected in ancient Egypt?", "The pharaoh was seen as a god, so obeying the government was a religious duty.", lines=2)], intro="Answer in complete sentences.")],
    tss("Students connect Egyptian beliefs to government, art, and architecture.", "Explain how belief systems shaped governments and cultures.", "Paper, markers, hieroglyph chart, workbook Lesson 2.2",
        "Twenty years for one tomb.", "Read the lesson.", ["Model the tomb-goods inference.", "Discuss who built the pyramids and how we know."], "Check Your Understanding 1–3.",
        ["Believing pyramids were built by enslaved armies."], ["Cause-and-effect organizer: belief → practice."], ["Take a virtual tour of the Giza pyramids."], independent="Workbook. The Weekly Check comes next."),
    summary="Egyptians believed the pharaoh was divine and planned for the afterlife with mummies and pyramids.")

# ================================================================= Week 2 · Kush and the Indus Valley
L3 = Lesson("2.3", "Egypt and Kush: Trade and Power",
    "I can describe how Egypt and Kush influenced each other through trade, conquest, and culture.", "C3 D2.His.2.6-8, D2.Eco.15.6-8",
    [("Nubia", "The region along the Nile south of Egypt, in today's Sudan."), ("Kush", "A powerful African kingdom in Nubia."),
     ("cultural diffusion", "The spread of ideas and customs from one group to another."), ("export", "A good sent to another place to be sold.")],
    "Two neighbors trade, fight, and borrow ideas from each other for 2,000 years. How might each one change?",
    [Text("South of Egypt, past the cataracts, lay <b>Nubia</b>, home of the kingdom of <b>Kush</b>. Nubia was rich in gold, ebony wood, ivory, and incense. Egypt traded with Kush, and at times New Kingdom pharaohs conquered it. Kushites adopted Egyptian gods, writing, and pyramid tombs: this is <b>cultural diffusion</b>."),
     Text("Egyptian trade reached far. The female pharaoh <b>Hatshepsut</b> (ruled about 1479–1458 BCE) sent a famous trading expedition to the land of Punt, returning with incense trees, gold, and animals. <b>Ramses II</b> (ruled about 1279–1213 BCE) expanded Egypt's power with wars and huge monuments."),
     Text("Then the tables turned. Around 750 BCE, the Kushite king <b>Piye</b> conquered Egypt, and Kushite kings ruled as pharaohs for nearly a century. Later, Kush moved its capital south to <b>Meroë</b>, which became a center of iron-making and trade. Meroë's kings built more than 200 steep pyramids, more than in all of Egypt."),
     Figure(lambda t: table(t, [["", "Egypt", "Kush"], ["location", "lower Nile, north of the cataracts", "upper Nile, in Nubia"], ["exports", "grain, linen, papyrus", "gold, ivory, ebony, iron, incense"],
                                ["capital cities", "Memphis, Thebes", "Napata, then Meroë"], ["shared culture", "gods, pyramids, hieroglyphs", "adopted Egyptian gods, pyramids, and writing; later its own Meroitic script"]],
                            [1.4 * inch, 2.15 * inch, 2.35 * inch], width=5.9 * inch, font_size=9.5)),
     Investigate("Trade Map", "What moved between Egypt and Kush?", ["a copy of the Nile Valley map", "colored pencils"],
                 ["Trace the Nile from Meroë to the delta.", "Draw arrows for goods moving north (from Kush) and south (from Egypt), using the chart.", "Label each arrow with two goods.", "Add a symbol for one idea that spread by cultural diffusion."],
                 record="your labeled trade map."),
     KeyIdea("Egypt and Kush traded, fought, and shared ideas for centuries. Kush adopted Egyptian ways, conquered Egypt around 750 BCE, and later thrived at Meroë as an iron-making center.")],
    [Problem("Name two goods Kush traded.", "e.g. gold, ivory, ebony, iron, incense"), Problem("Which Kushite king conquered Egypt around 750 BCE?", "Piye"),
     Problem("Give an example of cultural diffusion between Egypt and Kush.", "e.g. Kush adopted Egyptian gods, pyramids, and hieroglyphs.")],
    [S("Warm-Up", [SA("The spread of ideas between groups", "cultural diffusion"), SA("A good sent elsewhere to be sold", "export")], intro="Write the word for each description.", cols=2),
     S("Practice", [SA(q, a) for q, a in [("Where was Kush?", "in Nubia, south of Egypt along the Nile"), ("Where did Hatshepsut send a trade expedition?", "the land of Punt"),
                                          ("What was Meroë known for?", "iron-making, trade, and many pyramids"), ("Which kingdom built more pyramids?", "Kush")]] +
                   [OR("How did the relationship between Egypt and Kush change over time? Give two examples.", "e.g. Egypt traded with and conquered Kush; later Kush conquered Egypt and ruled as pharaohs.", lines=3)],
       intro="Answer each question. Use the lesson and the chart."),
     S("Exit Ticket", [OR("Why do you think Kush adopted so many Egyptian customs?", "e.g. long contact through trade and conquest; Egyptian ideas showed power and prestige.", lines=2)], intro="Answer in complete sentences.")],
    tss("Students analyze Egypt–Kush interactions.", "Explain how trade and conquest spread ideas.", "Nile maps, colored pencils, workbook Lesson 2.3",
        "Neighbors over 2,000 years.", "Read the lesson and chart.", ["Model cultural diffusion examples.", "Show photos of Meroë's pyramids."], "Check Your Understanding 1–3.",
        ["Thinking Kush was only a part of Egypt."], ["Two-way trade arrows organizer."], ["Research Queen Amanirenas of Kush and her war with Rome."]),
    summary="Egypt and Kush traded, fought, and shared culture; Kush later ruled Egypt and thrived at Meroë.")

L4 = Lesson("2.4", "The Indus Valley Civilization",
    "I can describe the planned cities of the Indus Valley and explain what archaeologists still don't know about them.", "C3 D2.His.10.6-8, D2.Geo.2.6-8",
    [("subcontinent", "A large landmass that is part of a continent, such as India."), ("monsoon", "A seasonal wind that brings heavy rain."),
     ("citadel", "A fortress or raised area in a city."), ("standardized", "Made the same everywhere, such as weights or bricks.")],
    "What would a city need to keep 40,000 people healthy and clean, without any electricity?",
    [Figure(lambda t: indus(t), caption="The Indus and Ganges rivers flow from the Himalayas."),
     Text("Around 2600 BCE, a civilization grew along the Indus River in what is now Pakistan and northwestern India. Snow melting from the Himalayas and summer <b>monsoon</b> rains flooded the river and left rich silt, like the Nile. Its largest cities, <b>Harappa</b> and <b>Mohenjo-daro</b>, may each have held tens of thousands of people."),
     Text("Indus cities were carefully planned. Streets ran in straight lines in a grid. Houses were built of baked bricks of the same size. Many homes had bathrooms, and covered drains carried waste away under the streets, a system more advanced than many cities had thousands of years later. A raised <b>citadel</b> held large buildings, such as the Great Bath at Mohenjo-daro. Traders used <b>standardized</b> stone weights and carved seals, some of which have been found as far away as Mesopotamia."),
     Text("Much about this civilization is still a mystery. Its writing, found on more than 4,000 small seals, has never been <b>deciphered</b>, so we can't read their own words. Around 1900 BCE, the cities declined. Historians think climate change, shifting rivers, and failing trade may have played a part."),
     Example("What evidence can and can't tell us", "Archaeologists found no grand palaces or royal tombs at Mohenjo-daro.",
             ["Evidence: large public buildings, but no palaces or rich royal tombs.", "Possible inference: power may have been shared, or rulers did not display wealth.", "Limit: without readable writing, we can't confirm who ruled."],
             "Artifacts suggest a well-organized society, but historians must say “may” until the script is read."),
     Investigate("Plan a City", "Can you design a city as organized as Mohenjo-daro?", ["graph paper", "a pencil and ruler"],
                 ["Draw a grid of streets running north–south and east–west.", "Add a raised citadel with one public building.", "Draw homes and a drain line under every street that leads away from the city.", "Add a market and a granary."],
                 record="your city plan with a key and two sentences comparing it with Mohenjo-daro."),
     KeyIdea("The Indus Valley civilization built planned grid cities with drains and standardized bricks and weights. Its writing hasn't been deciphered, so much remains a mystery.")],
    [Problem("Name two cities of the Indus Valley.", "Harappa and Mohenjo-daro"), Problem("Name one sign that Indus cities were planned.", "e.g. grid streets, drains, same-size bricks"),
     Problem("Why do historians know less about the Indus Valley than about Egypt?", "Its writing has never been deciphered.")],
    [S("Warm-Up", [SA("A seasonal wind that brings heavy rain", "monsoon"), SA("Made the same everywhere", "standardized")], intro="Write the word for each description.", cols=2),
     S("Practice", [SA(q, a) for q, a in [("In which modern countries was the Indus Valley civilization?", "Pakistan and northwestern India"), ("What carried waste away under the streets?", "covered drains"),
                                          ("Where have Indus seals been found far from home?", "Mesopotamia"), ("About when did the cities decline?", "around 1900 BCE")]] +
                   [OR("What does the use of standardized weights suggest about Indus trade and government? Explain.", "Fair, organized trade; some authority set and enforced the standards.", lines=3)],
       intro="Answer each question. Use the lesson and the map."),
     S("Exit Ticket", [OR("Write one thing historians know about the Indus Valley and one thing they don't. Explain why the second is uncertain.", "e.g. know: grid cities and drains; don't know: who ruled, because the script is unread.", lines=3)],
       intro="Answer in complete sentences.")],
    tss("Students describe Indus Valley cities and the limits of evidence.", "Explain the limitations of historical sources; use maps to explain places.", "Graph paper, rulers, workbook Lesson 2.4",
        "Keeping 40,000 people clean.", "Read the lesson; study the map.", ["Model the evidence-and-limits example."], "Check Your Understanding 1–3.",
        ["Stating guesses about the Indus as facts."], ["Know / Think / Don't-know chart."], ["Look at photos of Indus seals and invent a guess about their meaning."], independent="Workbook. The Weekly Check comes next."),
    summary="Indus cities were planned with grids and drains; their unread script keeps much a mystery.")

# ================================================================= Week 3 · India's beliefs; early China
L5 = Lesson("2.5", "Hinduism, Buddhism, and the Maurya Empire",
    "I can explain the main beliefs of Hinduism and Buddhism and how Ashoka spread Buddhist ideas.", "C3 D2.His.2.6-8, D2.His.4.6-8",
    [("Vedas", "Ancient sacred hymns and teachings, the oldest texts of Hinduism."), ("karma", "The idea that a person's actions decide what happens to them in the future."),
     ("reincarnation", "The belief that the soul is reborn in a new body after death."), ("caste system", "A system of social groups people were born into."),
     ("enlightenment", "In Buddhism, a state of perfect understanding and freedom from suffering.")],
    "If you believed every action you took would come back to you, how would you act?",
    [Text("After the Indus cities declined, new ways of life spread across northern India, especially in the Ganges River valley. Sacred hymns called the <b>Vedas</b> were memorized and passed down for centuries. From these traditions grew <b>Hinduism</b>, one of the world's oldest religions."),
     Text("Hindus believe in <b>dharma</b> (one's duty), <b>karma</b> (actions bring results), and <b>reincarnation</b> (the soul is reborn many times). Society was organized into a <b>caste system</b> of four main groups, or varnas: priests (Brahmins), rulers and warriors, merchants and farmers, and laborers. Some people were placed outside the system entirely and treated unfairly. India's constitution outlawed caste discrimination in 1950."),
     Text("Around 2,500 years ago, a prince named <b>Siddhartha Gautama</b> gave up his wealth to understand why people suffer. After years of searching, he reached <b>enlightenment</b> and became known as the <b>Buddha</b>, the “awakened one.” He taught the <b>Four Noble Truths</b>: life includes suffering; suffering comes from desire; suffering can end; and the way to end it is the <b>Eightfold Path</b> of right thinking and right living. Buddhism welcomed people of every caste."),
     Text("The <b>Maurya Empire</b> united most of India in the 300s BCE. Its greatest ruler, <b>Ashoka</b>, conquered the kingdom of Kalinga around 261 BCE in a war that killed many thousands. Horrified, Ashoka became a Buddhist. He carved edicts on stone pillars across his empire urging kindness, honesty, and respect for all religions, and he sent teachers who spread Buddhism to other lands."),
     Figure(lambda t: table(t, [["", "Hinduism", "Buddhism"], ["began", "grew over centuries from the Vedas", "teachings of the Buddha, about 2,500 years ago"],
                                ["key beliefs", "dharma, karma, reincarnation; many forms of the divine", "Four Noble Truths; Eightfold Path; karma and rebirth"],
                                ["goal", "moksha: release from the cycle of rebirth", "nirvana: freedom from suffering"], ["caste", "society organized by caste", "open to people of every caste"]],
                            [1.1 * inch, 2.4 * inch, 2.4 * inch], width=5.9 * inch, font_size=9.5)),
     KeyIdea("Hinduism teaches dharma, karma, and reincarnation. Buddhism teaches the Four Noble Truths and the Eightfold Path. The Maurya emperor Ashoka spread Buddhist ideas of peace and kindness.")],
    [Problem("What is karma?", "the idea that actions decide what happens to a person in the future"), Problem("Who became the Buddha?", "Siddhartha Gautama"),
     Problem("Why did Ashoka become a Buddhist?", "He was horrified by the killing in his war against Kalinga.")],
    [S("Warm-Up", [SA("Belief that the soul is reborn", "reincarnation"), SA("The oldest Hindu texts", "the Vedas")], intro="Write the word for each description.", cols=2),
     S("Practice", [SA(q, a) for q, a in [("What does dharma mean?", "one's duty"), ("What is the Buddhist goal of freedom from suffering called?", "nirvana"),
                                          ("What path did the Buddha teach to end suffering?", "the Eightfold Path"), ("How did Ashoka share his ideas?", "edicts carved on stone pillars; he sent teachers")]] +
                   [OR("Name one way Hinduism and Buddhism are alike and one way they differ.", "Alike: karma and rebirth. Different: Buddhism rejected caste; Hinduism organized society by caste.", lines=3)],
       intro="Answer each question. Use the lesson and the chart."),
     S("Exit Ticket", [OR("How did Ashoka change after the war with Kalinga, and why does it matter?", "He turned to Buddhism and ruled by kindness and tolerance, spreading Buddhism beyond India.", lines=3)], intro="Answer in complete sentences.")],
    tss("Students explain Hindu and Buddhist beliefs and Ashoka's reign.", "Explain how belief systems developed and spread.", "Workbook Lesson 2.5",
        "Actions come back to you.", "Read the lesson and comparison chart.", ["Present each religion respectfully, in its own terms.", "Discuss Ashoka's change of heart."], "Check Your Understanding 1–3.",
        ["Describing living religions only in the past tense."], ["Two-column belief organizer."], ["Read a translated edict of Ashoka and summarize it."]),
    summary="Hinduism and Buddhism shaped India; Ashoka spread Buddhist ideas of peace.")

L6 = Lesson("2.6", "China: The Huang He and the Shang Dynasty",
    "I can explain how geography shaped early China and describe the achievements of the Shang dynasty.", "C3 D2.Geo.4.6-8, D2.His.1.6-8",
    [("dynasty", "A series of rulers from the same family."), ("loess", "Fine yellow soil blown by the wind."), ("oracle bone", "A bone or shell used to ask questions of the gods and ancestors."),
     ("ancestor", "A family member who lived long ago.")],
    "A river that feeds you and also floods your village every few years: would you call it a friend or an enemy?",
    [Figure(lambda t: huang(t), caption="China's first civilizations grew along the Huang He."),
     Text("China's first civilization grew along the <b>Huang He</b>, or Yellow River, named for the yellow <b>loess</b> soil it carries. The soil was rich, but the river flooded so often and so violently that it was called “China's Sorrow.” Farmers built dikes and canals to control it. Mountains, deserts, and the sea cut China off from other early civilizations, so its culture developed largely on its own."),
     Text("The <b>Shang dynasty</b> (about 1600–1046 BCE) is China's first dynasty with written records. Shang kings ruled from cities such as Anyang. Skilled workers cast beautiful bronze vessels for ceremonies, and farmers grew millet and raised silkworms."),
     Text("Shang kings asked their <b>ancestors</b> and gods for advice with <b>oracle bones</b>. A priest carved a question, such as “Will the harvest be good?” on a turtle shell or ox bone, then touched it with a hot rod until it cracked. The cracks were read as the answer. These carvings are the oldest Chinese writing, and modern Chinese characters grew from them."),
     Investigate("Oracle Bone Question", "How did the Shang record questions for their ancestors?", ["a paper plate or a piece of cardboard cut like a shell", "a pencil"],
                 ["Write a yes-or-no question a Shang king might ask (harvest, weather, war, or a journey).", "Draw three pictograph characters to stand for key words.", "Draw crack lines across the “shell.”", "On the back, explain why the Shang kept these records."],
                 record="your oracle bone and explanation."),
     KeyIdea("The Huang He gave China rich loess soil but deadly floods. The Shang dynasty cast bronze and wrote on oracle bones, the oldest Chinese writing.")],
    [Problem("Why was the Huang He called “China's Sorrow”?", "It flooded often and violently."), Problem("What is a dynasty?", "a series of rulers from the same family"),
     Problem("What were oracle bones used for?", "to ask questions of ancestors and gods; they hold the oldest Chinese writing")],
    [S("Warm-Up", [SA("Fine yellow wind-blown soil", "loess"), SA("Rulers from one family", "dynasty")], intro="Write the word for each description.", cols=2),
     S("Practice", [SA(q, a) for q, a in [("What does Huang He mean?", "Yellow River"), ("Name one natural barrier around China.", "e.g. mountains, the Gobi Desert, the sea"),
                                          ("About when did the Shang rule?", "about 1600–1046 BCE"), ("What metal did Shang artisans cast?", "bronze")]] +
                   [OR("How did China's geography make its culture develop differently from Egypt's and Mesopotamia's?", "Natural barriers cut China off, so its culture developed largely on its own.", lines=3)],
       intro="Answer each question. Use the lesson and the map."),
     S("Exit Ticket", [OR("Was the Huang He more of a friend or an enemy to early China? Defend your answer with two details.", "Answers vary; must use details such as rich soil and floods.", lines=3)], intro="Answer in complete sentences.")],
    tss("Students explain geography's role in early China and Shang achievements.", "Explain how physical geography shaped civilizations.", "Paper plates, workbook Lesson 2.6",
        "Friend or enemy river.", "Read the lesson; study the map.", ["Discuss natural barriers.", "Model reading an oracle bone question."], "Check Your Understanding 1–3.",
        ["Thinking China had contact with Egypt or Sumer."], ["Map labeling of barriers."], ["Compare an oracle-bone character with its modern form."], independent="Workbook. The Weekly Check comes next."),
    summary="The Huang He shaped early China; the Shang cast bronze and wrote on oracle bones.")

# ================================================================= Week 4 · Later China; comparing civilizations
L7 = Lesson("2.7", "Zhou, Qin, and Han: Confucius, the Great Wall, and the Silk Road",
    "I can explain the Mandate of Heaven, Confucius's teachings, and the achievements of the Qin and Han dynasties.", "C3 D2.His.2.6-8, D2.Civ.6.6-8",
    [("Mandate of Heaven", "The belief that heaven gave a ruler the right to rule, and could take it away from an unjust ruler."), ("filial piety", "Respect and duty toward one's parents and elders."),
     ("Confucianism", "Teachings of Confucius about respect, duty, and good government."), ("Silk Road", "Trade routes that linked China with lands to the west.")],
    "Should a ruler who governs badly be allowed to keep ruling? Who should decide?",
    [Text("The <b>Zhou dynasty</b> (1046–256 BCE) overthrew the Shang and explained why with a new idea: the <b>Mandate of Heaven</b>. A good ruler had heaven's blessing; floods, famine, or rebellion showed that a ruler had lost it, and a new dynasty could take power. This pattern of rise and fall is called the <b>dynastic cycle</b>."),
     Text("Late in the Zhou period, China fell into wars between states. A teacher named <b>Confucius</b> (551–479 BCE) taught that order would return if people behaved well in their relationships: rulers should be fair, children should show <b>filial piety</b>, and everyone should be honest and respectful. Another thinker, Laozi, taught <b>Daoism</b>, living simply and in harmony with nature."),
     P_ANALECTS,
     Text("In 221 BCE, <b>Qin Shi Huang</b> united China and called himself the First Emperor. He ruled harshly but standardized writing, money, weights, and even cart axles. He linked older walls into an early <b>Great Wall</b> to keep out northern invaders and was buried with an army of more than 7,000 life-size clay soldiers, the <b>Terracotta Army</b>."),
     Text("The <b>Han dynasty</b> (206 BCE–220 CE) ruled for about 400 years. Han emperors chose officials partly by testing their knowledge of Confucian ideas. The Han invented paper and opened the <b>Silk Road</b>, trade routes that carried Chinese silk west and brought horses, glass, and new ideas, including Buddhism, into China."),
     KeyIdea("The Zhou introduced the Mandate of Heaven; Confucius taught respect, duty, and fair government; the Qin unified and standardized China; the Han invented paper and opened the Silk Road.")],
    [Problem("What is the Mandate of Heaven?", "the belief that heaven gives a just ruler the right to rule and can take it away"), Problem("What is filial piety?", "respect and duty toward parents and elders"),
     Problem("Name one thing Qin Shi Huang standardized.", "e.g. writing, money, weights, cart axles")],
    [S("Warm-Up", [SA("Respect and duty toward parents", "filial piety"), SA("Trade routes linking China with the West", "the Silk Road")], intro="Write the word for each description.", cols=2),
     S("Primary Source", [SA(q, a) for q, a in [("In 2.1, what does Confucius compare a virtuous ruler to?", "the north polar star"), ("In your own words, what is knowledge according to 2.17?", "knowing what you know and admitting what you don't")]] +
                         [OR("Rewrite 15.23 in your own words. Where have you heard a similar idea?", "Don't treat others in ways you wouldn't want to be treated; similar to the Golden Rule.", lines=3)],
       intro="Reread the excerpt from the Analects in your textbook. Then answer each question.", cols=1, passage=P_ANALECTS),
     S("Practice", [SA(q, a) for q, a in [("Which dynasty introduced the Mandate of Heaven?", "the Zhou"), ("Who called himself the First Emperor?", "Qin Shi Huang"),
                                          ("What was buried with the First Emperor?", "the Terracotta Army"), ("Name one Han invention.", "paper")]], intro="Answer each question. Use the lesson.", cols=1),
     S("Exit Ticket", [OR("Choose Confucius or Qin Shi Huang. How did his ideas or actions bring order to China?", "Answers vary; Confucius through good behavior in relationships; Qin through force and standardization.", lines=3)], intro="Answer in complete sentences.")],
    tss("Students explain Chinese political ideas and dynastic achievements.", "Explain how ideas shaped government; analyze primary sources.", "Workbook Lesson 2.7",
        "Should a bad ruler keep ruling?", "Read the lesson and the Analects excerpt.", ["Model the dynastic cycle.", "Close-read the three sayings."], "Check Your Understanding 1–3.",
        ["Thinking the Great Wall was built all at once."], ["Dynastic-cycle diagram."], ["Research how Han paper was made."]),
    summary="The Mandate of Heaven, Confucius, the Qin, and the Han shaped China's government and culture.")

L8 = Lesson("2.8", "Comparing River Valley Civilizations",
    "I can compare the first four civilizations and explain what they had in common.", "C3 D2.His.1.6-8, D2.Geo.4.6-8",
    [("compare", "To find how things are alike."), ("contrast", "To find how things are different."), ("common feature", "Something many examples share."),
     ("legacy", "Something handed down from the past.")],
    "Mesopotamia, Egypt, the Indus Valley, and China never planned together. Why did all four grow up beside rivers?",
    [Text("The world's first four civilizations each grew in a river valley: Mesopotamia on the Tigris and Euphrates, Egypt on the Nile, the Indus Valley on the Indus, and China on the Huang He. Rivers gave water, rich soil, and routes for trade. Farming made a food surplus, which let people take on special jobs, build cities, and form governments."),
     Figure(lambda t: table(t, [["", "Mesopotamia", "Egypt", "Indus Valley", "China"], ["river", "Tigris and Euphrates", "Nile", "Indus", "Huang He"],
                                ["floods", "unpredictable", "regular, gentle", "monsoon floods", "violent"], ["government", "city-states, then empires", "pharaoh (theocracy)", "unknown; organized cities", "dynasties; Mandate of Heaven"],
                                ["writing", "cuneiform", "hieroglyphics", "undeciphered script", "oracle-bone characters"], ["one legacy", "written laws", "pyramids", "city planning", "Confucian ideas"]],
                            [0.95 * inch, 1.25 * inch, 1.2 * inch, 1.25 * inch, 1.25 * inch], width=5.9 * inch, font_size=8.5)),
     Example("Write a comparison claim", "How were Egypt's and China's rivers different, and why did it matter?",
             ["Contrast: the Nile flooded gently on a regular schedule; the Huang He flooded violently.", "Effect: Egyptians could plan farming around the flood; Chinese farmers spent great effort on dikes.", "Claim: both rivers fed people, but the Huang He demanded more control."],
             "A strong comparison names a similarity or difference and explains why it matters."),
     Investigate("Museum Exhibit Card", "What is each civilization's greatest legacy?", ["four index cards", "colored pencils"],
                 ["Choose one achievement from each civilization.", "Draw it on the front of a card.", "On the back, write the civilization, the achievement, and why it still matters today.", "Rank your four cards from most to least important and explain your top choice."],
                 record="your four cards and a sentence explaining your top choice."),
     KeyIdea("All four first civilizations grew in river valleys, made food surpluses, built cities, developed governments, and created writing, but each had its own geography and legacy.")],
    [Problem("What did all four river valley civilizations have in common?", "e.g. rivers, farming surplus, cities, government, writing"), Problem("Which civilization's writing has not been deciphered?", "the Indus Valley"),
     Problem("Whose floods were most regular and predictable?", "Egypt's (the Nile)")],
    [S("Warm-Up", [SA("To find how things are different", "contrast"), SA("Something handed down from the past", "legacy")], intro="Write the word for each description.", cols=2),
     S("Compare", [SA(q, a) for q, a in [("Writing system of Mesopotamia", "cuneiform"), ("River of China's first civilization", "Huang He"), ("Government of Egypt", "a pharaoh; a theocracy"),
                                         ("Civilization known for planned grid cities", "the Indus Valley")]] +
                   [OR("Write a comparison claim about two civilizations. Name a similarity or difference and explain why it matters.", "Answers vary; must name two civilizations, a similarity/difference, and its importance.", lines=4)],
       intro="Answer each question. Use the comparison chart."),
     S("Exit Ticket", [OR("Why do you think civilizations began in river valleys and not in deserts or mountains?", "Rivers gave water, rich soil, and transportation, which made a food surplus and cities possible.", lines=2)], intro="Answer in complete sentences.")],
    tss("Students compare the four river valley civilizations.", "Compare historical developments in different places.", "Index cards, colored pencils, workbook Lesson 2.8, Unit 2 Review",
        "Why rivers?", "Review the comparison chart.", ["Model a comparison claim."], "Check Your Understanding 1–3.",
        ["Listing facts without comparing."], ["Claim sentence frames."], ["Add a fifth early civilization (such as the Olmec or Norte Chico) to the chart."],
        independent="Workbook; then the Unit 2 Review.", exit_="Next: Unit 2 Test."),
    summary="All four first civilizations grew beside rivers; each left its own legacy.")

# ================================================================= checks
C1 = check("Weekly Check 1: Ancient Egypt", [S("Show what you know", [
    SA("Direction the Nile flows", "north"), SA("The yearly Nile flood", "inundation"), SA("Egyptian picture writing", "hieroglyphics"),
    SA("Artifact that helped decode hieroglyphics", "the Rosetta Stone"), SA("Government led by a ruler seen as divine", "theocracy"),
    OR("How did the Nile make farming possible in a desert?", "Its yearly flood left rich silt and water for crops.", lines=2)],
    intro="Answer each question about ancient Egypt.", cols=1)])
C2 = check("Weekly Check 2: Kush and the Indus Valley", [S("Show what you know", [
    SA("Kingdom south of Egypt in Nubia", "Kush"), SA("Kushite city known for iron-making", "Meroë"), SA("The spread of ideas between groups", "cultural diffusion"),
    SA("Two Indus Valley cities", "Harappa and Mohenjo-daro"), SA("A sign of Indus city planning", "e.g. grid streets, drains, same-size bricks"),
    OR("Why is much about the Indus Valley still a mystery?", "Its writing has never been deciphered.", lines=2)],
    intro="Answer each question about Kush and the Indus Valley.", cols=1)])
C3 = check("Weekly Check 3: India's Beliefs and Early China", [S("Show what you know", [
    SA("Actions decide your future", "karma"), SA("Founder of Buddhism", "Siddhartha Gautama (the Buddha)"), SA("Maurya emperor who spread Buddhism", "Ashoka"),
    SA("China's first river civilization", "the Huang He (Yellow River) valley"), SA("Shang objects with the oldest Chinese writing", "oracle bones"),
    OR("Name one way Buddhism was different from Hindu society.", "Buddhism welcomed people of every caste.", lines=2)],
    intro="Answer each question about ancient India and China.", cols=1)])

REVIEW = review("Unit 2 Review", [
    S("Vocabulary", [SA(q, a) for q, a in [("silt", "rich soil left by water"), ("pharaoh", "ruler of Egypt seen as a god"), ("cultural diffusion", "spread of ideas between groups"),
                                           ("monsoon", "seasonal wind that brings heavy rain"), ("dynasty", "rulers from one family"), ("Mandate of Heaven", "heaven's approval to rule")]],
      intro="Write what each word means.", cols=2),
    S("Big ideas", [OR("Choose two river valley civilizations. Explain how each river shaped the civilization that grew beside it.", "Answers vary; accurate river details and effects for both.", lines=5)],
      intro="Answer in a paragraph.")])

TEST = make_test("Unit 2 Test", [
    S("Part A · Egypt and Kush (1 point each)", [
        SA("Why is Upper Egypt in the south?", "It is upriver; the Nile flows north."), SA("Why did Egyptians make mummies?", "They believed the dead needed their bodies in the afterlife."),
        MC("Which helped scholars read hieroglyphics?", ["the Great Pyramid", "the Rosetta Stone", "oracle bones", "the Code of Hammurabi"], 1),
        SA("Name one way Kush and Egypt influenced each other.", "e.g. trade; conquest; Kush adopted Egyptian gods, pyramids, and writing")],
      intro="Answer each question. For questions with choices, circle the letter of the best answer.", cols=1),
    S("Part B · India (1 point each)", [
        SA("Name one feature of Indus Valley cities.", "e.g. grid streets, drains, baked bricks, citadel"),
        MC("Which is a Buddhist teaching?", ["the Mandate of Heaven", "the Four Noble Truths", "ma'at", "filial piety"], 1),
        SA("What is reincarnation?", "the belief that the soul is reborn in a new body"), SA("How did Ashoka spread his ideas?", "stone pillar edicts and teachers")],
      intro="Answer each question. For questions with choices, circle the letter of the best answer.", cols=1),
    S("Part C · China (1 point each)", [
        Problem("Use the map. Along which labeled river did the Shang dynasty rule?", "the Huang He (Yellow River)", space=0, wide=True, fig=lambda t: huang(t, width=W * 0.55, title=None)),
        SA("What did the Mandate of Heaven explain?", "why dynasties rose and fell; a just ruler had heaven's approval"), SA("Name one Han achievement.", "paper or the Silk Road"),
        MC("Who taught that rulers should be fair and children should honor parents?", ["Qin Shi Huang", "Laozi", "Confucius", "Ashoka"], 2)],
      intro="Answer each question. For questions with choices, circle the letter of the best answer.", cols=1),
    S("Part D · Primary source (3 points)", [OR("Reread the sayings of Confucius. What do they suggest about how Confucius thought people and rulers should behave? Use two sayings as evidence.",
                                                "Rubric: clear claim about virtue/respect (1); two sayings cited accurately (1); explanation linking them to behavior or government (1).", lines=6, points=3)],
      intro="Reread the excerpt. Then answer in a paragraph.", passage=P_ANALECTS),
    S("Part E · Explain (4 points)", [OR("Compare two river valley civilizations. Explain one similarity and one difference, and why each matters.",
                                         "Rubric: two civilizations named (1); accurate similarity (1); accurate difference (1); explains why it matters (1).", lines=8, points=4)],
      intro="Write a paragraph. Use details from this unit.")])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
CHECKS = [C1, C2, C3]
WEEKS = weeks_for(2, LESSONS, CHECKS, REVIEW, TEST, "social")

UNIT = Unit(2, "River Valley Civilizations", "Ancient Egypt and Kush, the Indus Valley, Hinduism and Buddhism, and ancient China from the Shang to the Han.",
    "Mesopotamia was not the only place where people built cities beside a river. In this unit you'll travel up the Nile to the pyramids of Egypt and Kush, walk the planned streets of the Indus Valley, learn the beliefs that shaped India, and follow China from oracle bones to the Great Wall and the Silk Road. Then you'll compare the first civilizations and decide what each one left the world.",
    ["Explain how rivers shaped Egypt, the Indus Valley, and China.", "Describe Egyptian and Kushite government, beliefs, and trade.",
     "Explain the main beliefs of Hinduism and Buddhism.", "Explain China's dynasties, the Mandate of Heaven, and Confucian ideas.", "Compare the four river valley civilizations."],
    [("C3 D2.His.1, 2, 4, 10", "Context; change and continuity; perspectives; limits of sources."), ("C3 D2.Geo.2, 4", "Maps; human–environment interaction."),
     ("C3 D2.Civ.6", "How political ideas shape government.")],
    [("silt", "Rich soil left by water."), ("pharaoh", "Egypt's ruler, seen as a god."), ("cultural diffusion", "The spread of ideas."), ("karma", "Actions decide the future."),
     ("dynasty", "Rulers from one family."), ("Mandate of Heaven", "Heaven's approval to rule.")],
    ["Unit 1: civilization, irrigation, cuneiform, and the Fertile Crescent."], ["Tray, soil, and muddy water", "Graph paper and ruler", "Paper plates", "Index cards", "World map or atlas"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Engineers who design flood control, city planners who lay out streets and sewers, and diplomats who study other cultures all build on lessons from the first river valley civilizations.",
    family_note="Find the Nile, Indus, and Huang He on a world map together, then look up one museum artifact from each civilization online.",
    weeks=WEEKS)
