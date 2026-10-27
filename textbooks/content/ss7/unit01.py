"""Grade 7 Social Studies · Unit 1: Early Humans and Mesopotamia — historians' tools, early humans, the Agricultural
Revolution, the first cities, Mesopotamia, Sumer, cuneiform, and the first empires and laws (Oct 12 – Nov 6, 2026; Tue/Thu)."""
from engine import *
from content.sskit import S, MC, OR, SA, DRAW, tss, make_test, weeks_for, check, review
from geomap import geo_map

SITES = {"Ur": (46.10, 30.96), "Uruk": (45.64, 31.32), "Babylon": (44.42, 32.54), "Nineveh": (43.15, 36.36), "Jericho": (35.44, 31.87), "Çatalhöyük": (32.83, 37.67)}


def crescent(t, sites=("Ur", "Uruk", "Babylon", "Nineveh"), width=None, title="The Fertile Crescent"):
    labs = [(n, *SITES[n], "city", -6 if n in ("Uruk",) else 0, 0) for n in sites]
    labs += [("MESOPOTAMIA", 43.6, 34.2, "region"), ("Tigris R.", 44.9, 35.3, "water"), ("Euphrates R.", 41.2, 34.9, "water"), ("Persian Gulf", 50.3, 27.6, "water"),
             ("Mediterranean Sea", 33.3, 34.0, "water"), ("Nile R.", 31.0, 27.5, "water"), ("ARABIAN DESERT", 41.5, 29.5, "plain"), ("ZAGROS MTS.", 47.8, 33.6, "plain")]
    return geo_map(t, (29, 52, 25, 39.5), width=width or W * 0.78, rivers=("Tigris", "Euphrates", "Nile", "Jordan"), labels=labs, title=title, scale_miles=200)


P_HAMMURABI = Passage("From the Code of Hammurabi", [
    "196. If a man put out the eye of another man, his eye shall be put out.",
    "198. If he put out the eye of a freed man, or break the bone of a freed man, he shall pay one gold mina.",
    "199. If he put out the eye of a man's slave, or break the bone of a man's slave, he shall pay one-half of its value.",
    "229. If a builder build a house for some one, and does not construct it properly, and the house which he built fall in and kill its owner, then that builder shall be put to death.",
], source="Babylon, about 1754 BCE. Translated by L. W. King (1910). Public domain.", genre="Primary source", numbered=False)

# ================================================================= Week 1 · Historians' tools and early humans
L1 = Lesson("1.1", "How Historians Know the Past",
    "I can distinguish primary and secondary sources, explain how archaeologists learn about the past, and read a BCE/CE timeline.", "C3 D2.His.9.6-8, D2.His.10.6-8",
    [("primary source", "A source created by someone who was there at the time."), ("secondary source", "A source created later by someone studying the past."),
     ("artifact", "An object made or used by people in the past."), ("archaeologist", "A scientist who studies the past by digging up and examining artifacts and remains."),
     ("BCE / CE", "“Before the Common Era” and “Common Era”: the years before and after year 1.")],
    "Imagine someone in 5,000 years digs up your bedroom. What would your things tell them about you, and what would they get wrong?",
    [Text("Historians are detectives. They gather evidence from <b>primary sources</b> (letters, laws, inscriptions, photographs, artifacts) and <b>secondary sources</b> (textbooks, articles, documentaries). For times before writing, <b>archaeologists</b> study <b>artifacts</b>, bones, seeds, and buildings. Scientists can estimate the age of once-living material using <b>radiocarbon dating</b>."),
     Text("Every source has limits. A king's inscription may brag. Artifacts made of stone and clay survive, but cloth, wood, and memories usually don't. Good historians ask: <i>Who made this? When? Why? What might be missing?</i>"),
     Text("Dates before year 1 are written <b>BCE</b> and count <b>down</b> toward year 1: 3000 BCE is earlier than 2000 BCE. Dates after are <b>CE</b> and count up. There is no year 0."),
     Figure(lambda t: timeline_fig(t, [("10,000 BCE", "farming begins"), ("3200 BCE", "writing in Sumer"), ("1754 BCE", "Hammurabi's Code"), ("1 CE", "start of the Common Era"), ("2026 CE", "today")], height=74)),
     Example("Count across the BCE/CE line", "How many years passed between 500 BCE and 500 CE?",
             ["From 500 BCE to 1 BCE is 499 years; then 1 BCE to 1 CE is 1 year.", "From 1 CE to 500 CE is 499 years.", "499 + 1 + 499 = 999."],
             "999 years (because there is no year 0)."),
     Investigate("Time Capsule Detectives", "What can objects tell us, and what can't they?", ["a box of 6–8 everyday objects chosen by your teacher (receipt, toy, coin, photo, tool, food wrapper)"],
                 ["Examine each object as if you were an archaeologist in the year 7026.", "For each, write one inference about the people who used it.", "Sort the objects into primary sources and secondary sources (if any).", "Write what these objects can't tell you about the family."],
                 record="an evidence chart: Object | What it suggests | Questions it raises."),
     KeyIdea("Historians use primary and secondary sources, ask who made a source and why, and recognize that evidence is always incomplete.")],
    [Problem("Primary or secondary: a clay tablet written in 2000 BCE", "primary"), Problem("Primary or secondary: a website about ancient Sumer", "secondary"), Problem("Which is earlier, 2500 BCE or 1800 BCE?", "2500 BCE")],
    [S("Warm-Up", [SA("An object made by people long ago", "artifact"), SA("A source made by an eyewitness", "primary source")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Primary or secondary: a diary from 1863", "primary"), ("Primary or secondary: your history textbook", "secondary"), ("Primary or secondary: a stone tool", "primary (artifact)"),
                                          ("Order from earliest: 1200 BCE, 3500 BCE, 200 CE, 500 BCE", "3500 BCE, 1200 BCE, 500 BCE, 200 CE"), ("Years from 3000 BCE to 1000 BCE", "2,000 years"),
                                          ("Years from 200 BCE to 300 CE", "499 years")]] +
                   [OR("A king's victory monument says he never lost a battle. Why should a historian be careful with this source?", "It was made to praise the king, so it may exaggerate or leave out defeats.", lines=3)], cols=1),
     S("Exit Ticket", [OR("Name one strength and one limit of using artifacts as evidence.", "Strength: real objects from the time. Limit: only durable items survive; they don't explain thoughts or events.", lines=2)])],
    tss("Students classify sources and read BCE/CE timelines.", "Classify sources; detect limitations of the historical record.", "Box of everyday objects, workbook Lesson 1.1",
        "Bedroom in 5,000 years.", "Read the lesson.", ["Model source questions.", "Model counting across BCE/CE."], "Check Your Understanding 1–3.",
        ["Treating BCE dates like CE (thinking larger numbers are later)."], ["Number line with BCE to the left."], ["Interview a grandparent: an oral history is a primary source."]),
    summary="Historians use primary and secondary sources; BCE counts down, CE counts up.")

L2 = Lesson("1.2", "Early Humans: Hunter-Gatherers",
    "I can describe how early humans lived as hunter-gatherers and spread across the world.", "C3 D2.His.1.6-8, D2.Geo.6.6-8",
    [("hunter-gatherer", "A person who gets food by hunting animals and gathering wild plants."), ("nomad", "A person who moves from place to place instead of living in one settlement."),
     ("Paleolithic", "The Old Stone Age, when people made stone tools and lived as hunter-gatherers."), ("migration", "Movement of people from one place to another.")],
    "If you had no stores, farms, or metal tools, how would you get food and stay warm?",
    [Text("Fossils show that our species, <i>Homo sapiens</i>, appeared in Africa roughly 300,000 years ago. Over many thousands of years, groups <b>migrated</b> out of Africa into Asia, Europe, Australia, and eventually the Americas."),
     Text("For almost all of human history, people lived as <b>hunter-gatherers</b> during the <b>Paleolithic</b>, or Old Stone Age. Small groups of related families moved with the seasons, following herds and ripening plants. They made tools of stone, bone, and wood, used fire to cook and stay warm, made clothing from hides, and painted animals on cave walls, such as the famous paintings at Lascaux, France, made about 17,000 years ago."),
     Figure(lambda t: table(t, [["Need", "How hunter-gatherers met it"], ["food", "hunting, fishing, gathering nuts, roots, berries"], ["shelter", "caves, huts of branches, bones, and hides"],
                                ["tools", "stone blades and scrapers, spears, needles of bone"], ["communication and art", "spoken language, cave paintings, carvings, music"]], [1.8 * inch, 4.1 * inch], width=5.9 * inch)),
     Investigate("What's in the Pack?", "What would a nomadic family carry?", ["paper", "pencil"],
                 ["Your band of 25 is moving to its winter camp. Everything must be carried.", "List the 8 most important items you would take and why.", "Compare your list with a family member's and agree on a final list."],
                 record="your final list with a reason for each item."),
     KeyIdea("For most of human history, people were nomadic hunter-gatherers who used stone tools and fire and spread from Africa across the world.")],
    [Problem("Where did Homo sapiens first appear?", "Africa"), Problem("Why did hunter-gatherers move often?", "to follow herds and seasonal plants"), Problem("Name one Paleolithic technology.", "stone tools, fire, bone needles, spears")],
    [S("Warm-Up", [SA("Old Stone Age", "Paleolithic"), SA("A person who moves from place to place", "nomad")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Why did groups stay small?", "An area could only feed a small group; easier to move."), ("What do cave paintings suggest about early people?", "They had art, beliefs, and close knowledge of animals."),
                                          ("How did fire change life?", "warmth, cooking, protection, light")]] +
                   [OR("Explain why archaeologists know more about Paleolithic tools than Paleolithic clothing.", "Stone tools survive for thousands of years; hides and plant fibers usually rot away.", lines=3)], cols=1),
     S("Exit Ticket", [OR("Describe one advantage and one challenge of the hunter-gatherer way of life.", "Advantage: varied diet, freedom to move. Challenge: food could be scarce; constant travel.", lines=2)])],
    tss("Students describe Paleolithic life and migration.", "Analyze connections among events; explain how humans spread.", "Workbook Lesson 1.2",
        "No stores or farms.", "Read the lesson.", ["Discuss needs chart; evidence for early life."], "Check Your Understanding 1–3.",
        ["Picturing “cavemen” as unintelligent."], ["Picture walk of artifacts."], ["Research the Lascaux cave paintings."], independent="Workbook. Weekly Check Friday."),
    summary="Early humans were nomadic hunter-gatherers who spread out of Africa.")

# ================================================================= Week 2 · Agricultural Revolution
L3 = Lesson("1.3", "The Agricultural Revolution",
    "I can explain how farming began and how it changed human life.", "C3 D2.His.2.6-8, D2.Geo.4.6-8",
    [("domestication", "Taming plants and animals so they can be raised by people."), ("Neolithic", "The New Stone Age, when farming began."),
     ("surplus", "More than is needed to survive."), ("Agricultural Revolution", "The shift from hunting and gathering to farming.")],
    "Would you rather move every season to find food, or stay in one place and grow it? What would you gain and lose?",
    [Text("Beginning around 10,000 BCE in the <b>Fertile Crescent</b> of Southwest Asia, people began planting wild wheat and barley and herding goats and sheep. This change, called the <b>Agricultural Revolution</b>, took thousands of years. Farming also began on its own in other places: rice and millet in China, corn in Mexico, potatoes in South America."),
     Figure(lambda t: crescent(t, sites=("Jericho", "Çatalhöyük"), title="Early farming villages in the Fertile Crescent")),
     Figure(lambda t: table(t, [["Before farming", "After farming"], ["nomadic", "settled villages"], ["small bands", "larger populations"], ["food found or hunted", "food grown and stored; surplus"],
                                ["few possessions", "houses, pottery, tools for farming"], ["most people did the same work", "some people specialized in other jobs"]], [2.9 * inch, 2.9 * inch], width=5.8 * inch)),
     Text("Farming brought problems too. People worked long hours, ate fewer kinds of food, and could starve if crops failed. Living close together and near animals spread disease. Still, food <b>surplus</b> allowed populations to grow and set the stage for cities."),
     Investigate("Gains and Losses", "Was farming an improvement?", ["paper"],
                 ["Make a T-chart: Gains | Losses.", "List at least four of each from the lesson.", "Decide: for an ordinary person, was life better or worse? Write a claim with two pieces of evidence."],
                 record="your T-chart and claim."),
     KeyIdea("Domesticating plants and animals let people settle, grow surpluses, and build larger communities, with new benefits and new problems.")],
    [Problem("Where did farming first begin?", "the Fertile Crescent (Southwest Asia)"), Problem("What is a surplus?", "more than is needed"), Problem("Name one problem farming created.", "e.g. disease, harder work, crop failure")],
    [S("Warm-Up", [SA("New Stone Age", "Neolithic"), SA("Taming plants and animals", "domestication")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Two crops first domesticated in the Fertile Crescent", "wheat and barley"), ("A crop first domesticated in Mexico", "corn (maize)"),
                                          ("Why did farming lead to settled villages?", "Farmers had to stay near their fields."), ("How did surplus lead to new jobs?", "Not everyone had to farm, so some could specialize.")]] +
                   [OR("Write a claim: Was the Agricultural Revolution good for humans? Support it with two pieces of evidence.", "Answers vary; must use evidence from both lists.", lines=4)], cols=1),
     S("Exit Ticket", [OR("Why do historians call farming a “revolution” even though it took thousands of years?", "It completely changed how humans lived.", lines=2)])],
    tss("Students analyze the Agricultural Revolution.", "Analyze change and continuity; human–environment interaction.", "Workbook Lesson 1.3",
        "Move or stay?", "Read the lesson; study the map.", ["Discuss before/after chart; costs of farming."], "Check Your Understanding 1–3.",
        ["Thinking farming happened suddenly everywhere."], ["Before/after picture cards."], ["Sprout wheat or barley seeds in a cup."]),
    summary="Farming let people settle and grow surpluses, changing human life.")

L4 = Lesson("1.4", "From Villages to Civilizations",
    "I can identify the features of a civilization and explain how surplus led to cities.", "C3 D2.His.1.6-8",
    [("civilization", "A complex society with cities, government, specialized jobs, social classes, and record keeping."), ("specialization", "Doing one kind of job and trading for other needs."),
     ("social class", "A group of people with similar wealth or status.")],
    "What makes a city different from a village?",
    [Text("Some farming villages grew into towns. <b>Jericho</b>, near the Jordan River, had a stone wall and tower by about 8000 BCE. <b>Çatalhöyük</b> in Anatolia (modern Turkey) was home to thousands of people around 7000 BCE; its houses were built so close together that people walked across the rooftops and entered through openings in the roofs."),
     Text("Historians use several features to describe a <b>civilization</b>:"),
     Figure(lambda t: table(t, [["Feature", "Why it appears"], ["cities", "food surplus supports many people in one place"], ["organized government", "leaders manage water, defense, and laws"],
                                ["specialized jobs", "potters, weavers, priests, soldiers, traders"], ["social classes", "some people gain more wealth or power"], ["religion and public buildings", "temples unite people around shared beliefs"],
                                ["writing and record keeping", "track harvests, taxes, and trade"], ["technology and art", "new tools, buildings, and crafts"]], [2.0 * inch, 3.9 * inch], width=5.9 * inch)),
     Figure(lambda t: flow_fig(t, ["Farming", "Food surplus", "Population grows", "Specialized jobs and trade", "Cities and government"], height=54)),
     Investigate("Village to City Simulation", "How does a surplus change a community?", ["20 dried beans (grain)", "role cards: farmer, potter, priest, guard, trader"],
                 ["Each farmer 'grows' 5 beans per season but needs only 3 to eat.", "Decide how the 2 extra beans per farmer can support people with other jobs.", "Add one more job each round as the surplus grows."],
                 record="how many non-farmers your surplus could support, and the new problems (who decides? who guards the beans?)."),
     KeyIdea("Food surplus led to larger populations, specialized jobs, and the features of civilization.")],
    [Problem("Name three features of a civilization.", "e.g. cities, government, specialized jobs, social classes, writing"), Problem("What made specialization possible?", "food surplus"), Problem("How did people enter houses at Çatalhöyük?", "through openings in the roofs")],
    [S("Warm-Up", [SA("A complex society with cities and writing", "civilization"), SA("Doing one kind of job", "specialization")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Why might a growing town need a government?", "to organize water, defense, and laws"), ("Why did record keeping develop?", "to track harvests, taxes, and trade"),
                                          ("Put in order: cities, surplus, farming, specialization", "farming, surplus, specialization, cities")]] +
                   [OR("Is your community a civilization by the historians' definition? Use three features as evidence.", "Answers vary.", lines=3)], cols=1),
     S("Exit Ticket", [OR("Explain the chain from farming to cities.", "Farming → surplus → population growth → specialized jobs and trade → cities and government.", lines=2)])],
    tss("Students identify the features of civilization.", "Analyze connections among events and developments.", "Dried beans, role cards, workbook Lesson 1.4",
        "City vs village.", "Read the lesson.", ["Discuss features chart; flow chart."], "Check Your Understanding 1–3.",
        ["Thinking “civilized” means “better.”"], ["Features checklist."], ["Research how Çatalhöyük was excavated."], independent="Workbook. Weekly Check Friday."),
    summary="Surplus → population → specialization → cities and government.")

# ================================================================= Week 3 · Mesopotamia
L5 = Lesson("1.5", "Mesopotamia: The Land Between the Rivers",
    "I can explain how the geography of Mesopotamia shaped early civilization there.", "C3 D2.Geo.2.6-8, D2.Geo.4.6-8",
    [("Mesopotamia", "Greek for “land between the rivers”; the region between the Tigris and Euphrates."), ("irrigation", "Bringing water to crops through canals or ditches."),
     ("silt", "Fine, rich soil carried and left behind by rivers."), ("levee", "A raised bank that keeps a river from flooding.")],
    "Mesopotamia had hot, dry summers and almost no rain in the south, yet it became home to the world's first cities. How?",
    [Figure(lambda t: crescent(t)),
     Text("<b>Mesopotamia</b> lies between the <b>Tigris</b> and <b>Euphrates</b> rivers in modern Iraq. Each spring, snow melting in the northern mountains made the rivers flood, spreading rich <b>silt</b> over the plain. But the floods were unpredictable: some years they were too small, other years they destroyed fields and villages. Summers were hot and rainfall was low."),
     Text("Farmers solved these problems by working together. They dug <b>irrigation</b> canals to carry river water to fields, built <b>levees</b> to hold back floods, and stored water for dry months. Organizing these big projects required leaders and laws. The region had few trees and little stone, so people built with sun-dried mud bricks and traded grain and cloth for wood, stone, and metal."),
     Figure(lambda t: table(t, [["Geographic challenge", "Human solution"], ["unpredictable floods", "levees and drainage ditches"], ["little rain in summer", "irrigation canals and storage basins"],
                                ["few trees or stone", "mud bricks; trade for resources"], ["flat land, open to invaders", "city walls and armies"]], [2.8 * inch, 3.0 * inch], width=5.8 * inch)),
     Investigate("Irrigation Model", "How can canals bring water to fields?", ["a baking pan with soil or sand", "a cup of water", "a craft stick"],
                 ["Shape a “river” along one side of the pan.", "Use the stick to carve canals from the river to three “fields.”", "Pour water into the river at the high end. Where does it go?", "Add a small dirt bank (levee) and test it again."],
                 record="a labeled sketch of your irrigation system and what worked."),
     KeyIdea("Mesopotamia's rivers gave rich soil and water, but floods and dry summers forced people to cooperate on irrigation and levees.")],
    [Problem("What does “Mesopotamia” mean?", "land between the rivers"), Problem("Name the two rivers.", "Tigris and Euphrates"), Problem("Why did Mesopotamians build with mud brick?", "There were few trees and little stone.")],
    [S("Warm-Up", [SA("Rich soil left by floods", "silt"), SA("Bringing water to crops", "irrigation")], cols=2),
     S("Map and Analyze", [Problem("Use the map. Which body of water do the Tigris and Euphrates flow into?", "the Persian Gulf", space=0, wide=True, fig=lambda t: crescent(t, width=W * 0.7)),
                           SA("In which modern country is most of Mesopotamia?", "Iraq"), SA("Which city on the map is farthest south?", "Ur"),
                           OR("Explain how a geographic challenge led to cooperation and government.", "Unpredictable floods and dry summers required large irrigation and levee projects that needed leaders and rules.", lines=3)], cols=1),
     S("Exit Ticket", [OR("Were the rivers more helpful or harmful to Mesopotamians? Explain.", "Answers vary; rich soil and water vs destructive floods.", lines=2)])],
    tss("Students analyze geography's effect on Mesopotamia.", "Use maps; explain how environment influences cultural patterns.", "Pan, soil, water, craft stick, workbook Lesson 1.5",
        "First cities in a dry land.", "Read the lesson; study the map.", ["Discuss challenge/solution chart."], "Check Your Understanding 1–3.",
        ["Thinking the floods were gentle and regular like the Nile's."], ["Challenge → solution cards."], ["Compare with Mississippi Delta flooding and levees."]),
    summary="Rivers gave Mesopotamia rich soil, but floods and drought required irrigation and cooperation.")

L6 = Lesson("1.6", "Sumer: City-States, Ziggurats, and Society",
    "I can describe Sumerian city-states, religion, and social classes.", "C3 D2.His.1.6-8, D2.Civ.6.6-8",
    [("city-state", "A city and the farmland around it with its own government."), ("ziggurat", "A large stepped temple tower in a Sumerian city."),
     ("polytheism", "Belief in many gods."), ("scribe", "A person trained to read and write and keep records.")],
    "If your town had its own king, army, and gods, how would you feel about the next town over?",
    [Text("By about 3500 BCE, the people of <b>Sumer</b>, in southern Mesopotamia, had built some of the world's first cities, including <b>Ur</b> and <b>Uruk</b>. Each was a <b>city-state</b> with its own ruler, army, and patron god. City-states often fought over water and land."),
     Text("Sumerians practiced <b>polytheism</b>. They believed gods controlled nature and that people must serve them. At the center of each city stood a <b>ziggurat</b>, a huge stepped tower of mud brick with a temple on top. Priests were powerful, and at first they helped manage the city's grain. Over time, war leaders became kings, who claimed to rule with the gods' approval."),
     Figure(lambda t: table(t, [["Social class", "Who"], ["upper class", "kings, priests, and nobles"], ["middle class", "merchants, artisans, scribes, farmers who owned land"], ["lower class", "farm workers and laborers"],
                                ["enslaved people", "often prisoners of war or people in debt"]], [1.7 * inch, 4.2 * inch], width=5.9 * inch)),
     Text("Women in Sumer could own property and run businesses, and some were priestesses, but most power belonged to men."),
     Investigate("Design a Ziggurat", "What did a ziggurat show about Sumerian values?", ["sugar cubes or building blocks", "paper"],
                 ["Build a three-level stepped tower with a shrine on top.", "Add a ramp or stairway.", "Write two sentences explaining why the temple was the tallest building in the city."],
                 record="a sketch and your explanation."),
     KeyIdea("Sumer was made of independent city-states centered on ziggurats, ruled by kings and priests, with clear social classes.")],
    [Problem("Name two Sumerian city-states.", "Ur and Uruk (also Lagash, Kish)"), Problem("What was a ziggurat?", "a stepped temple tower"), Problem("Why did city-states fight?", "over water and land")],
    [S("Warm-Up", [SA("Belief in many gods", "polytheism"), SA("A city with its own government", "city-state")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Who was at the top of Sumerian society?", "kings, priests, nobles"), ("Name one right Sumerian women had.", "own property, run businesses"),
                                          ("Why were scribes respected?", "Few people could read and write.")]] +
                   [OR("What does the location and size of the ziggurat suggest about the role of religion in Sumer?", "Religion was central and powerful; the temple dominated the city.", lines=3)], cols=1),
     S("Exit Ticket", [OR("Compare a Sumerian city-state with a modern U.S. city.", "Answers vary; e.g. both have government and jobs; Sumer had kings, its own army, and patron gods.", lines=2)])],
    tss("Students describe Sumerian society.", "Analyze connections; describe government and social structure.", "Blocks or sugar cubes, workbook Lesson 1.6",
        "Town with its own king.", "Read the lesson.", ["Discuss social pyramid; religion and power."], "Check Your Understanding 1–3.",
        ["Assuming all ancient women had no rights."], ["Social pyramid diagram."], ["Research the Royal Tombs of Ur."], independent="Workbook. Weekly Check Friday."),
    summary="Sumer's city-states centered on ziggurats with kings, priests, and social classes.")

# ================================================================= Week 4 · Writing, empires, and law
L7 = Lesson("1.7", "Cuneiform and the Invention of Writing",
    "I can explain how and why writing developed in Sumer and how it changed society.", "C3 D2.His.1.6-8",
    [("cuneiform", "Sumerian writing made of wedge-shaped marks pressed into clay."), ("stylus", "A pointed tool used to write on clay."), ("epic", "A long poem about a hero's deeds.")],
    "How would your life change if nothing could be written down?",
    [Text("Around 3200 BCE, Sumerians in cities like Uruk began keeping records on clay tablets. At first they drew small pictures to count grain, sheep, and taxes. Over time the pictures became wedge-shaped marks pressed with a reed <b>stylus</b>: <b>cuneiform</b>, from the Latin word for “wedge.” Cuneiform was used for more than 3,000 years and for many languages."),
     Text("Writing was hard to learn, so <b>scribes</b> trained for years in schools. They wrote contracts, laws, letters, medical texts, prayers, and literature, including the <b>Epic of Gilgamesh</b>, one of the oldest stories in the world. It tells of Gilgamesh, a king of Uruk, who searches for the secret of living forever and learns that every human life must end."),
     Figure(lambda t: flow_fig(t, ["Tokens and pictures to count goods", "Pictographs on clay", "Wedge-shaped symbols for sounds and words", "Laws, letters, literature"], height=56)),
     Text("Other Sumerian innovations include the wheel (used for pottery and carts), the plow, sailboats, and a number system based on 60, which is why we still have 60 minutes in an hour and 360 degrees in a circle."),
     Investigate("Clay Tablet Scribe", "What was it like to write in cuneiform?", ["air-dry clay or play dough", "a craft stick cut to a wedge point or a chopstick"],
                 ["Flatten the clay into a tablet.", "Press wedge shapes to record a “receipt”: 5 sheep and 3 jars of barley (invent symbols).", "Trade tablets with a partner and try to read each other's record."],
                 record="your symbol key and two problems a scribe would face."),
     KeyIdea("Writing began as record keeping, became cuneiform, and let people keep laws, history, and literature.")],
    [Problem("What was cuneiform first used for?", "keeping records of goods, trade, and taxes"), Problem("What does cuneiform mean?", "wedge-shaped"), Problem("Who was Gilgamesh?", "a king of Uruk, hero of the epic")],
    [S("Warm-Up", [SA("Tool used to write on clay", "stylus"), SA("A long poem about a hero", "epic")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("About when did writing begin in Sumer?", "about 3200 BCE"), ("Why did scribes train for years?", "Cuneiform had hundreds of signs and was hard to learn."),
                                          ("Name a Sumerian idea we still use.", "60 minutes in an hour / 360 degrees in a circle / the wheel")]] +
                   [OR("Explain how writing helped governments become more powerful.", "Rulers could record taxes, laws, and property, and send orders across distances.", lines=3)], cols=1),
     S("Exit Ticket", [OR("Which Sumerian invention do you think was most important? Defend your choice.", "Answers vary.", lines=2)])],
    tss("Students explain the development of writing.", "Analyze connections among developments.", "Clay, craft sticks, workbook Lesson 1.7",
        "No writing.", "Read the lesson.", ["Discuss stages of writing; Gilgamesh summary."], "Check Your Understanding 1–3.",
        ["Thinking writing was invented for stories first."], ["Picture → symbol chart."], ["Look up your name in a cuneiform chart."]),
    summary="Cuneiform began as record keeping and grew into laws and literature.")

L8 = Lesson("1.8", "Empires and the Code of Hammurabi",
    "I can describe the first empires and analyze Hammurabi's Code as a primary source.", "C3 D2.Civ.3.6-8, D2.His.10.6-8",
    [("empire", "Many lands and peoples ruled by one government."), ("code of law", "A written set of laws."), ("stele", "A tall carved stone slab.")],
    "Why might it matter that laws are written down for everyone to see?",
    [Text("Around 2334 BCE, <b>Sargon of Akkad</b> conquered the Sumerian city-states and created what many historians call the world's first <b>empire</b>. Later, <b>Hammurabi</b>, king of Babylon (ruled about 1792–1750 BCE), united much of Mesopotamia. About 1754 BCE he had 282 laws carved on a tall stone <b>stele</b> for public display. The stele is now in the Louvre museum in Paris."),
     P_HAMMURABI,
     Example("Analyze a primary source", "What do Laws 196, 198, and 199 reveal about Babylonian society?",
             ["Law 196: harming another man means the same harm in return (“an eye for an eye”).", "Law 198: harming a freed man means paying a fine (one gold mina) instead.", "Law 199: harming an enslaved person means paying the owner."],
             "Punishments depended on social class, so Babylonian law treated people unequally; laws protected property and order more than equal rights."),
     Text("Hammurabi's Code was not the first law code, but it is one of the best preserved. By writing laws in public, he showed that rules applied across his empire, and he claimed the gods gave him authority to rule justly."),
     Investigate("Fair or Unfair?", "Do these laws match our ideas of justice?", ["the source excerpt", "highlighters"],
                 ["Highlight each punishment.", "Rate each law from 1 (very unfair) to 5 (very fair) by today's standards.", "Find one idea in the code that is similar to modern law (for example, builders responsible for safe buildings)."],
                 record="your ratings and a paragraph comparing Hammurabi's Code with modern laws."),
     KeyIdea("Sargon built the first empire; Hammurabi's written code brought order but punished people differently by class.")],
    [Problem("Who created the first empire?", "Sargon of Akkad"), Problem("About when was Hammurabi's Code written?", "about 1754 BCE"), Problem("Did the code treat all people equally?", "No; punishments depended on social class.")],
    [S("Warm-Up", [SA("Many lands ruled by one government", "empire"), SA("A tall carved stone slab", "stele")], cols=2),
     S("Analyze the Source", [SA("What happens to a builder whose house collapses and kills the owner?", "The builder is put to death."),
                              SA("What is the punishment for putting out a freed man's eye?", "paying one gold mina"),
                              OR("Why would Hammurabi carve his laws in stone in a public place?", "So everyone knew the laws and they couldn't easily be changed; to show his authority.", lines=3),
                              OR("Name one way the code is like modern law and one way it is different.", "Like: builders responsible for safety. Different: unequal punishments by class; harsh physical punishments.", lines=3)], cols=1, passage=P_HAMMURABI),
     S("Exit Ticket", [OR("Why was writing laws down an important step for civilization?", "Written laws were public, consistent, and harder for rulers to change at will.", lines=2)])],
    tss("Students analyze the first empires and Hammurabi's Code.", "Examine the origins, purposes, and impact of laws; analyze primary sources.", "Highlighters, workbook Lesson 1.8, Unit 1 Review",
        "Written laws.", ["Read the lesson.", "Read the source excerpt aloud."], ["Model source analysis."], "Check Your Understanding 1–3.",
        ["Judging ancient law only by modern values without context."], ["Source-analysis questions: who, when, why, what's missing?"], ["Write a fair code of five family rules."],
        independent="Workbook; then the Unit 1 Review.", exit_="Tomorrow (Friday): Unit 1 Test."),
    summary="Sargon built the first empire; Hammurabi wrote laws for all to see.")

# ================================================================= checks
C1 = check("Weekly Check 1: Historians and Early Humans", [S("Show what you know", [
    SA("Primary or secondary: a photo taken in 1920", "primary"), SA("Primary or secondary: an encyclopedia article", "secondary"),
    SA("Which is earlier: 1500 BCE or 900 BCE?", "1500 BCE"), SA("Years between 300 BCE and 200 CE", "499"),
    SA("Where did Homo sapiens first appear?", "Africa"), OR("Why did hunter-gatherers move from place to place?", "to follow animals and seasonal plants for food", lines=2)], cols=1)])
C2 = check("Weekly Check 2: Farming and Civilization", [S("Show what you know", [
    SA("Where did farming first begin?", "the Fertile Crescent"), SA("What is a food surplus?", "more food than needed"),
    SA("Name two features of a civilization.", "e.g. cities, government, writing, specialized jobs"), SA("Name an early farming town.", "Jericho or Çatalhöyük"),
    OR("Explain how a food surplus led to specialized jobs.", "Not everyone had to farm, so some people could do other work.", lines=2)], cols=1)])
C3 = check("Weekly Check 3: Mesopotamia and Sumer", [S("Show what you know", [
    SA("The two rivers of Mesopotamia", "Tigris and Euphrates"), SA("Bringing water to crops through canals", "irrigation"), SA("A stepped temple tower", "ziggurat"),
    SA("Belief in many gods", "polytheism"), OR("Describe one geographic challenge in Mesopotamia and how people solved it.", "e.g. unpredictable floods → levees; dry summers → irrigation canals.", lines=2)], cols=1)])

REVIEW = review("Unit 1 Review", [
    S("Vocabulary", [SA(q, a) for q, a in [("artifact", "object made by people in the past"), ("domestication", "taming plants and animals"), ("city-state", "a city with its own government"),
                                           ("cuneiform", "wedge-shaped writing"), ("empire", "many lands under one government"), ("surplus", "more than needed")]], cols=2),
    S("Big ideas", [OR("Explain how geography, farming, and writing each helped Sumer become a civilization.", "Rivers gave water and soil; farming gave surplus; writing allowed records and laws.", lines=4)])])

TEST = make_test("Unit 1 Test", [
    S("Part A · Historians' tools (1 point each)", [
        SA("Primary or secondary: a clay tablet from Ur", "primary"), SA("Primary or secondary: a documentary about Sumer", "secondary"),
        SA("Order from earliest: 1754 BCE, 3200 BCE, 2334 BCE", "3200 BCE, 2334 BCE, 1754 BCE"), SA("How many years from 2000 BCE to 1500 BCE?", "500")], cols=1),
    S("Part B · Early humans and farming (1 point each)", [
        MC("How did most Paleolithic people get food?", ["farming", "trading in cities", "hunting and gathering", "fishing fleets"], 2),
        SA("What is domestication?", "taming plants and animals for human use"), SA("Name one benefit and one problem of farming.", "e.g. surplus / disease or harder work"),
        MC("Which came first?", ["cities", "food surplus", "writing"], 1)], cols=1),
    S("Part C · Mesopotamia (1 point each)", [
        Problem("Use the map. Which labeled city is farthest south, closest to the Persian Gulf?", "Ur", space=0, wide=True, fig=lambda t: crescent(t, width=W * 0.6, title=None)),
        SA("Why did Mesopotamians need irrigation?", "Little rain in summer; needed to bring river water to crops."), SA("What was a ziggurat?", "a stepped temple tower"),
        SA("What was cuneiform first used for?", "keeping records (goods, taxes, trade)"), SA("Who created the first empire?", "Sargon of Akkad")], cols=1),
    S("Part D · Primary source (3 points)", [OR("Reread the excerpt from Hammurabi's Code. What does it show about justice and social class in Babylon? Use two laws as evidence.",
                                                "Rubric: claim that punishments depended on class (1); two laws cited accurately (1); explanation of what this reveals (1).", lines=6, points=3)], passage=P_HAMMURABI),
    S("Part E · Explain (4 points)", [OR("Explain how the geography of Mesopotamia led to the development of government and laws.",
                                         "Rubric: describes the rivers/floods/dry climate (1); explains irrigation and levee projects (1); connects cooperation to leaders and government (1); connects government to written laws (1).", lines=8, points=4)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
CHECKS = [C1, C2, C3]
WEEKS = weeks_for(1, LESSONS, CHECKS, REVIEW, TEST, "social")

UNIT = Unit(1, "Early Humans and Mesopotamia", "Historians' tools, early humans, the Agricultural Revolution, the first cities, Sumer, writing, and the first empires and laws.",
    "Ten thousand years ago, nearly everyone on Earth lived by hunting and gathering. Then, in a few river valleys, people began to farm, settle, and build cities. In this unit you'll learn how historians uncover the distant past, then follow humans from the Old Stone Age to Sumer, where people built the first cities, invented writing, and carved laws in stone.",
    ["Use primary and secondary sources and read BCE/CE timelines.", "Explain how the Agricultural Revolution changed human life.",
     "Analyze how Mesopotamia's geography shaped civilization.", "Describe Sumerian society, writing, and the first empires and laws."],
    [("C3 D2.His.1, 2, 9, 10", "Historical context; change and continuity; sources and their limitations."), ("C3 D2.Geo.2, 4", "Maps; human–environment interaction."),
     ("C3 D2.Civ.3", "Origins and purposes of laws.")],
    [("primary source", "Created at the time by a participant."), ("Agricultural Revolution", "The shift to farming."), ("civilization", "A complex society with cities and government."),
     ("irrigation", "Bringing water to crops."), ("cuneiform", "Sumerian wedge-shaped writing."), ("empire", "Many lands under one ruler.")],
    ["Basic map skills.", "Timelines."], ["Box of everyday objects", "Pan, soil, water", "Clay or play dough", "Dried beans", "World map or atlas"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Writing, cities, and written law all began in Mesopotamia. Every time you read a contract, check the time, or follow a posted rule, you're using ideas over 4,000 years old.",
    family_note="Look at a clock and a compass together and talk about how the Sumerian base-60 system still shapes how we measure time and angles.",
    weeks=WEEKS)
