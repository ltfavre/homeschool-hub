"""Grade 4 Social Studies · Unit 1: Mississippi: Land and Regions — map skills, location, landforms and waterways,
Mississippi's regions, natural resources, and regional economies (Oct 12 – Nov 6, 2026; Tue/Thu)."""
from engine import *
from content.sskit import S, MC, OR, SA, DRAW, tss, make_test, weeks_for, check, review
from geomap import geo_map, mississippi_map, place

MS_REGION_LABELS = [("THE DELTA", -90.55, 33.55, "region"), ("LOESS BLUFFS", -91.05, 31.75, "region"), ("NORTH CENTRAL HILLS", -89.55, 34.05, "region"),
                    ("TENNESSEE RIVER HILLS", -88.45, 34.85, "region"), ("BLACK PRAIRIE", -88.55, 33.35, "region"), ("PINEY WOODS", -89.25, 31.45, "region"),
                    ("GULF COAST", -88.95, 30.62, "region")]


def ms_regions(t, width=None):
    return mississippi_map(t, width=width or W * 0.48, cities=False, extra_labels=MS_REGION_LABELS, rivers=("Mississippi", "Pearl", "Tombigbee"))


def ms_in_us(t, width=None):
    return geo_map(t, (-125, -66.5, 24, 50), width=width or W * 0.8, states=True, focus={"Mississippi": t.main},
                   labels=[("Gulf of Mexico", -90, 26.2, "water"), ("Atlantic Ocean", -71, 33, "water"), ("Pacific Ocean", -120.5, 30.5, "water")], scale_miles=500)


# ================================================================= Week 1 · Map skills and location
L1 = Lesson("1.1", "Maps and Globes",
    "I can use a map's title, compass rose, key, and scale to read a map.", "C3 D2.Geo.1.3-5",
    [("globe", "A model of Earth shaped like a ball."), ("compass rose", "A symbol that shows directions on a map."), ("map key", "A box that explains the symbols on a map (also called a legend)."),
     ("map scale", "A line that shows how distance on the map compares with real distance.")],
    "If you had to give a friend directions from your house to a park, what would you draw?",
    [Text("A <b>globe</b> is a model of Earth, so it shows shapes and distances correctly, but it's hard to carry and you can only see half at a time. A <b>map</b> is a flat drawing of a place. Maps can show a whole country or one small neighborhood."),
     Figure(lambda t: table(t, [["Map part", "What it tells you"], ["title", "what the map shows"], ["compass rose", "directions: north (N), south (S), east (E), west (W), and in-between directions like northeast (NE)"],
                                ["map key (legend)", "what each symbol, line, or color means"], ["scale", "how far apart places really are"]], [1.6 * inch, 4.2 * inch], width=5.8 * inch)),
     Beside(lambda t: mississippi_map(t, width=W * 0.4, title="Cities of Mississippi"),
            ["This map's <b>title</b> tells you it shows cities of Mississippi. The <b>star</b> marks Jackson, the state capital, and dots mark other cities.",
             "The <b>compass rose</b> in the top corner points north. The <b>scale bar</b> at the bottom stands for 50 miles. Rivers are drawn in blue.",
             "Notice that the Mississippi River traces most of the state's western edge, and the southern coast meets the Gulf of Mexico."]),
     Example("Use the scale", "About how far is it from Jackson to Gulfport?",
             ["Measure the distance on the map with a strip of paper.", "Compare it with the scale bar (50 miles).", "The distance is about three scale bars long."],
             "about 150 miles"),
     Investigate("Map My Room", "Can you make a map someone else could use?", ["paper", "ruler", "colored pencils"],
                 ["Draw your bedroom or kitchen as if you were looking down from the ceiling.", "Add a title and a compass rose (find north with a compass app or the sunrise in the east).",
                  "Make a key with at least four symbols.", "Add a scale such as “1 inch = 2 feet.”"],
                 record="your finished map; trade with a family member and ask them to find something using only the map."),
     KeyIdea("Read the title, check the compass rose, use the key, and measure with the scale.")],
    [Problem("Which map part explains symbols?", "the map key (legend)"), Problem("Which direction is between north and east?", "northeast"), Problem("Which city is the state capital?", "Jackson")],
    [S("Warm-Up", [SA("The four cardinal directions", "north, south, east, west"), SA("A round model of Earth", "globe")], cols=2),
     S("Read the Map", [Problem("Use the map for questions 3–7. Which city is farthest north?", "Southaven", space=0, wide=True, fig=lambda t: mississippi_map(t, width=W * 0.42))] +
                       [SA(q, a) for q, a in [ ("Which two cities are on the Gulf of Mexico?", "Gulfport and Biloxi"),
                                              ("In which direction would you travel from Jackson to Meridian?", "east"), ("In which direction from Tupelo is Hattiesburg?", "south (slightly southwest)"),
                                              ("Which river forms Mississippi's western border?", "the Mississippi River")]], cols=1, passage=None),
     S("Exit Ticket", [OR("Name the four map parts and tell what each one does.", "Title: what the map shows; compass rose: directions; key: symbols; scale: distance.", lines=3)])],
    tss("Students use map parts to read a map.", "Construct maps and other representations of familiar places.", "Workbook Lesson 1.1, paper, ruler, colored pencils",
        "Directions to a park.", "Read the lesson and the Mississippi map.", ["Model each map part.", "Measure Jackson to Gulfport with the scale."], "Check Your Understanding 1–3.",
        ["Assuming north is always “up” on every map without checking the compass rose."], ["Map-part sticky labels."], ["Map your neighborhood."]),
    summary="Title, compass rose, key, and scale help you read any map.")

L2 = Lesson("1.2", "Where in the World Is Mississippi?",
    "I can describe Mississippi's location using relative location, hemispheres, and latitude and longitude.", "C3 D2.Geo.2.3-5",
    [("relative location", "Where a place is compared with other places."), ("absolute location", "The exact location of a place, given by latitude and longitude."),
     ("latitude", "Imaginary lines that run east and west and measure distance north or south of the equator."), ("longitude", "Imaginary lines that run north and south and measure distance east or west of the prime meridian."),
     ("hemisphere", "Half of Earth.")],
    "How would you describe where you live to someone on the other side of the world?",
    [Text("<b>Relative location</b> describes a place by what is near it. Mississippi is in the southern United States. It borders <b>Tennessee</b> to the north, <b>Alabama</b> to the east, the <b>Gulf of Mexico</b> and <b>Louisiana</b> to the south, and <b>Louisiana</b> and <b>Arkansas</b> to the west, across the Mississippi River."),
     Figure(lambda t: ms_in_us(t), caption="Mississippi is highlighted."),
     Beside(lambda t: geo_map(t, (-92.5, -87.0, 29.5, 35.5), width=W * 0.4, states=True, focus={"Mississippi": t.wash}, rivers=("Mississippi",),
                              labels=[("Jackson", *place("Jackson, Mississippi"), "capital"), ("32° N", -92.3, 32.05, "plain", 14, 0), ("34° N", -92.3, 34.05, "plain", 14, 0),
                                      ("90° W", -90.0, 29.7, "plain"), ("88° W", -88.0, 29.7, "plain")]),
            ["<b>Absolute location</b> uses a grid of imaginary lines. Lines of <b>latitude</b> measure degrees north or south of the equator. Lines of <b>longitude</b> measure degrees east or west of the prime meridian.",
             "Because Mississippi is north of the equator and west of the prime meridian, it is in the <b>Northern</b> and <b>Western Hemispheres</b>. Jackson is at about 32° N, 90° W."],
            caption="Latitude labels at left; longitude labels at bottom."),
     Investigate("Grid Hunt", "Can you find places using latitude and longitude?", ["a globe or world map with latitude and longitude lines", "notebook"],
                 ["Find 30° N, 90° W. What place is near there?", "Find the equator and the prime meridian.", "Find a place in each of the four hemispheres.", "Make up two coordinates and challenge a family member to find them."],
                 record="each coordinate and the place you found."),
     KeyIdea("Relative location compares places; absolute location uses latitude and longitude. Mississippi is in the Northern and Western Hemispheres.")],
    [Problem("Which state borders Mississippi to the east?", "Alabama"), Problem("Which body of water is south of Mississippi?", "the Gulf of Mexico"), Problem("Which hemispheres is Mississippi in?", "Northern and Western")],
    [S("Warm-Up", [SA("Lines that run east–west", "latitude"), SA("Half of Earth is a…", "hemisphere")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("State north of Mississippi", "Tennessee"), ("Two states west of Mississippi", "Louisiana and Arkansas"), ("Jackson's approximate latitude", "32° N"),
                                          ("Is Mississippi north or south of the equator?", "north"), ("Relative or absolute: “Jackson is about 32° N, 90° W.”", "absolute"),
                                          ("Relative or absolute: “Gulfport is on the Gulf of Mexico.”", "relative")]], cols=1),
     S("Exit Ticket", [OR("Describe Mississippi's relative location in two sentences.", "e.g. Mississippi is in the southern U.S. between Louisiana and Alabama, with Tennessee to the north and the Gulf of Mexico to the south.", lines=2)])],
    tss("Students describe relative and absolute location.", "Use maps to explain relationships between locations of places.", "Globe or world map, workbook Lesson 1.2",
        "Describe home to someone far away.", "Read the lesson; examine both maps.", ["Teach latitude/longitude and hemispheres."], "Check Your Understanding 1–3.",
        ["Mixing up latitude and longitude."], ["“Lat is flat” memory trick."], ["Find the coordinates of a favorite vacation spot."], independent="Workbook. Weekly Check Friday."),
    summary="Mississippi is in the southern U.S., in the Northern and Western Hemispheres, around 32° N, 90° W.")

# ================================================================= Week 2 · Landforms and waterways
L3 = Lesson("1.3", "Mississippi's Land and Water",
    "I can identify Mississippi's major landforms and waterways and explain why they matter.", "C3 D2.Geo.2.3-5",
    [("landform", "A natural shape of the land, such as a hill, plain, or valley."), ("plain", "A large area of flat land."), ("river basin", "All the land drained by a river and the streams that flow into it."),
     ("bluff", "A high, steep bank, often along a river."), ("tributary", "A smaller river or stream that flows into a larger one.")],
    "Most of Mississippi's rivers flow toward the south. Why do you think that is?",
    [Text("Mississippi is mostly low, rolling hills and flat plains. Its highest point is <b>Woodall Mountain</b> in the far northeast, about 806 feet above sea level. Its lowest point is sea level along the Gulf of Mexico. Because the land is generally higher in the north and lower in the south, most rivers flow south toward the Gulf."),
     Figure(lambda t: table(t, [["Waterway", "Fact"], ["Mississippi River", "Forms most of the state's western border; one of the longest rivers in North America"], ["Yazoo River", "Flows through the Delta into the Mississippi at Vicksburg"],
                                ["Pearl River", "Flows past Jackson to the Gulf; part of it forms the border with Louisiana"], ["Tombigbee River", "Flows south through eastern Mississippi into Alabama"],
                                ["Pascagoula River", "Flows into the Gulf at Pascagoula"], ["Gulf of Mexico", "Mississippi's southern coast, about 44 miles long"]],
                            [1.6 * inch, 4.3 * inch], width=5.9 * inch, font_size=9.5)),
     Beside(lambda t: mississippi_map(t, width=W * 0.4, cities=False, rivers=("Mississippi", "Pearl", "Tombigbee"),
                                      extra_labels=[("Mississippi R.", -91.45, 33.6, "water"), ("Pearl R.", -89.25, 31.9, "water"), ("Tombigbee R.", -88.2, 33.8, "water"), ("Gulf of Mexico", -89.0, 30.1, "water"),
                                                    ("Woodall Mtn.", -88.24, 34.79, "city")], title="Major rivers"),
            ["Waterways have always mattered to people here. Rivers provided fish, water, and travel routes for American Indian nations.",
             "Later, steamboats carried cotton and goods on the Mississippi River.",
             "Today, barges still move goods on the Mississippi and on the <b>Tennessee-Tombigbee Waterway</b>, a canal system opened in 1985 that connects the Tennessee River to the Tombigbee."]),
     Investigate("Which Way Does Water Flow?", "How does the slope of land decide where rivers go?", ["a baking sheet or tray", "a towel to tilt it", "a cup of water", "a few pebbles"],
                 ["Raise one end of the tray to make “high land” in the north.", "Slowly pour water at the high end.", "Watch which way it flows and where it collects.", "Add pebbles as “hills” and observe how the water's path changes."],
                 record="a sketch showing high land, low land, and the water's path, and an explanation linked to Mississippi's rivers."),
     KeyIdea("Mississippi's land is higher in the north and lower in the south, so most rivers flow south to the Gulf. Rivers have shaped travel, trade, and settlement.")],
    [Problem("What is Mississippi's highest point?", "Woodall Mountain (about 806 feet)"), Problem("Which river forms most of the western border?", "the Mississippi River"), Problem("Why do most rivers flow south?", "The land is higher in the north and lower in the south.")],
    [S("Warm-Up", [SA("A large area of flat land", "plain"), SA("A smaller river that flows into a larger one", "tributary")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Which river flows past Jackson?", "the Pearl River"), ("Where does the Yazoo River join the Mississippi?", "at Vicksburg"),
                                          ("What canal system connects the Tennessee and Tombigbee rivers?", "the Tennessee-Tombigbee Waterway"), ("What is Mississippi's lowest elevation?", "sea level")]] +
                   [OR("Explain two ways rivers have been important to people in Mississippi.", "e.g. fish and water; travel and trade by boat and barge.", lines=3)], cols=1),
     S("Exit Ticket", [OR("Use the tray investigation to explain why the Pearl River flows to the Gulf.", "Water flows downhill; the land slopes down toward the Gulf in the south.", lines=2)])],
    tss("Students identify landforms and waterways.", "Use maps to explain relationships between places and environmental characteristics.", "Tray, towel, water, pebbles, workbook Lesson 1.3",
        "Rivers flow south.", "Read the lesson; trace rivers on the map.", ["Discuss elevation and flow; waterways and trade."], "Check Your Understanding 1–3.",
        ["Thinking rivers always flow “down” the map (south) everywhere."], ["Highlight each river a different color."], ["Research a Mississippi river's source."]),
    summary="Most Mississippi rivers flow south to the Gulf; waterways shape travel and trade.")

L4 = Lesson("1.4", "Reading Physical and Political Maps",
    "I can tell physical and political maps apart and use each to answer questions.", "C3 D2.Geo.1.3-5",
    [("physical map", "A map that shows natural features such as rivers, mountains, and elevation."), ("political map", "A map that shows human-made boundaries, states, counties, and cities."),
     ("elevation", "How high land is above sea level."), ("county", "One of the parts a state is divided into for local government.")],
    "What's the difference between a map of the rivers in Mississippi and a map of its cities?",
    [Text("A <b>physical map</b> shows what nature made: rivers, hills, coastlines, and elevation, often with colors (green for low land, tan or brown for higher land). A <b>political map</b> shows what people decided: state and county boundaries, capitals, and cities. Mississippi is divided into <b>82 counties</b>."),
     Figure(lambda t: table(t, [["Question", "Better map"], ["Where is the state capital?", "political"], ["Where is the land highest?", "physical"], ["Which county is Tupelo in?", "political"], ["Which way does the Pearl River flow?", "physical"]],
                            [3.6 * inch, 1.6 * inch], width=5.2 * inch)),
     Example("Use two maps together", "Why did cities like Vicksburg and Natchez grow where they did?",
             ["Physical map: both sit on high bluffs beside the Mississippi River.", "Political map: both are cities in western Mississippi.", "Put them together: the high bluffs were safe from floods, and the river brought trade."],
             "They grew on bluffs above the river, where people could trade by boat but stay above floodwaters."),
     Investigate("Salt Dough Relief Map", "Can you build a physical map of Mississippi?", ["outline of Mississippi traced on cardboard", "salt dough (2 cups flour, 1 cup salt, about 3/4 cup water)", "paint", "toothpick flags"],
                 ["Spread a thin layer of dough over the outline.", "Build it a little higher in the northeast and keep the Delta and coast flat.", "Press a groove for the Mississippi and Pearl rivers.", "When dry, paint low land green and higher land tan, and add flags for Jackson and your town."],
                 record="a photo or sketch of your map with a key."),
     KeyIdea("Physical maps show natural features; political maps show boundaries and cities. Using both explains why places are where they are.")],
    [Problem("Which kind of map shows county lines?", "political"), Problem("Which kind shows elevation?", "physical"), Problem("How many counties does Mississippi have?", "82")],
    [S("Warm-Up", [SA("Height above sea level", "elevation"), SA("Map that shows cities", "political map")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Find the route of the Yazoo River. Which map?", "physical"), ("Find the boundary between Mississippi and Alabama. Which map?", "political"),
                                          ("Find the flattest region. Which map?", "physical"), ("Find the nearest city to your home. Which map?", "political")]] +
                   [OR("Why might a city grow on a bluff next to a river?", "Safe from floods but close to the river for water and trade.", lines=2)], cols=1),
     S("Exit Ticket", [OR("Write one question a physical map can answer and one a political map can answer.", "Answers vary.", lines=2)])],
    tss("Students compare physical and political maps.", "Construct maps and other graphic representations.", "Salt dough materials, workbook Lesson 1.4",
        "Rivers vs cities.", "Read the lesson; compare the maps.", ["Model using two maps together."], "Check Your Understanding 1–3.",
        ["Thinking one map shows everything."], ["Sort questions into physical/political."], ["Find your county on a Mississippi county map."], independent="Workbook. Weekly Check Friday."),
    summary="Physical maps show nature; political maps show boundaries and cities.")

# ================================================================= Week 3 · Regions
L5 = Lesson("1.5", "Mississippi's Natural Regions",
    "I can identify Mississippi's natural regions and describe the land in each.", "C3 D2.Geo.2.3-5",
    [("region", "An area with features that make it different from other areas."), ("fertile", "Able to grow many plants; rich soil."), ("alluvial", "Made of soil left behind by rivers.")],
    "If you drove from Tupelo to Greenville to Gulfport, how might the land outside your window change?",
    [Beside(lambda t: ms_regions(t, width=W * 0.46),
            ["Geographers divide Mississippi into natural <b>regions</b> by land, soil, and plants.",
             "Regions don't have sharp edges; one blends into the next. The labels on the map show where each region generally is.",
             "As you read the chart below, find each region on the map."], fig_w=0.48, caption="General locations of Mississippi's natural regions."),
     Figure(lambda t: table(t, [["Region", "What the land is like"], ["The Delta", "very flat, fertile alluvial soil left by Mississippi and Yazoo river floods; northwest"], ["Loess Bluffs", "steep bluffs of fine wind-blown soil along the east edge of the Mississippi River valley"],
                                ["North Central Hills", "rolling hills with red clay soil"], ["Tennessee River Hills", "the highest, most rugged land, in the far northeast"],
                                ["Black Prairie", "gently rolling land with dark, rich soil in the northeast"], ["Piney Woods", "rolling hills with sandy soil and pine forests in the south"],
                                ["Gulf Coast", "low, flat land with beaches, marshes, and bays along the Gulf of Mexico"]], [1.6 * inch, 4.3 * inch], width=5.9 * inch, font_size=9.5)),
     Investigate("Region Postcards", "What would you see in each region?", ["index cards", "colored pencils"],
                 ["Choose three regions.", "On each card, draw a scene showing the land, plants, and one way people use the land.", "On the back, write a short message describing the region to a friend."],
                 record="three postcards with accurate details."),
     KeyIdea("Mississippi's regions include the Delta, Loess Bluffs, the hills, the Black Prairie, the Piney Woods, and the Gulf Coast, each with its own land and soil.")],
    [Problem("Which region is flattest and most fertile?", "the Delta"), Problem("Which region has pine forests?", "the Piney Woods"), Problem("Which region has the highest land?", "the Tennessee River Hills")],
    [S("Warm-Up", [SA("Region =", "an area with shared features"), SA("Soil left by rivers is…", "alluvial")], cols=2),
     S("Match the Region", [SA(q, a) for q, a in [("beaches and marshes", "Gulf Coast"), ("dark, rich soil in the northeast", "Black Prairie"), ("wind-blown soil bluffs", "Loess Bluffs"),
                                                  ("red clay hills", "North Central Hills"), ("flat land between two rivers", "the Delta"), ("sandy soil and pines", "Piney Woods")]], cols=2),
     S("Exit Ticket", [OR("Which region do you live in or nearest to? Describe its land.", "Answers vary.", lines=2)])],
    tss("Students identify Mississippi's natural regions.", "Explain relationships between locations of places and regions and their environmental characteristics.", "Index cards, workbook Lesson 1.5",
        "Road trip changes.", "Read the lesson; locate regions on the map.", ["Discuss each region's land and soil."], "Check Your Understanding 1–3.",
        ["Thinking regions have sharp borders."], ["Color-coded region chart."], ["Find photos of each region."]),
    summary="Each region of Mississippi has its own land, soil, and plants.")

L6 = Lesson("1.6", "Comparing the Delta and the Piney Woods",
    "I can compare two regions and explain how land affects the way people live and work.", "C3 D2.Geo.4.3-5",
    [("compare", "To tell how things are alike."), ("contrast", "To tell how things are different."), ("timber", "Trees cut for wood and wood products.")],
    "How might growing up on a Delta farm be different from growing up in a Piney Woods town?",
    [Text("<b>The Delta</b> is a broad, flat plain in northwestern Mississippi between the Mississippi and Yazoo rivers. For thousands of years, floods left layers of rich soil. Today the Delta is known for large farms of cotton, soybeans, corn, and rice, and for catfish farming in ponds. Towns are spread out across wide fields. The Delta is also famous as a birthplace of the blues."),
     Text("<b>The Piney Woods</b> covers much of southeastern Mississippi. Its sandy soil is less fertile for crops, but it is excellent for growing pine trees. Lumber and paper mills grew up around cities such as Hattiesburg and Laurel. Forests here also support hunting, outdoor recreation, and wildlife."),
     Figure(lambda t: table(t, [["", "The Delta", "Piney Woods", "Both"], ["land", "very flat", "rolling hills", "part of Mississippi; rivers"], ["soil", "rich alluvial soil", "sandy soil", ""],
                                ["main uses", "row crops, catfish farms", "timber, paper, outdoor recreation", "agriculture is important"], ["places", "Greenville, Clarksdale", "Hattiesburg, Laurel", ""]],
                            [1.0 * inch, 1.6 * inch, 1.65 * inch, 1.6 * inch], width=5.85 * inch, font_size=9.5)),
     Investigate("Venn Diagram", "How are the two regions alike and different?", ["paper", "two colored pencils"],
                 ["Draw two overlapping circles labeled Delta and Piney Woods.", "Write at least four details in each outer part.", "Write at least two shared details in the middle.", "Write a summary sentence."],
                 record="your Venn diagram and summary."),
     KeyIdea("The land and soil of a region shape how people earn a living there.")],
    [Problem("Why is the Delta good for crops?", "Floods left rich alluvial soil on flat land."), Problem("What grows well in the Piney Woods?", "pine trees (timber)"), Problem("Name a Piney Woods city.", "Hattiesburg or Laurel")],
    [S("Warm-Up", [SA("To tell how things differ", "contrast"), SA("Trees cut for wood", "timber")], cols=2),
     S("Compare", [SA(q, a) for q, a in [("Delta land shape", "flat"), ("Piney Woods soil", "sandy"), ("One Delta product", "cotton, soybeans, rice, corn, or catfish"), ("One Piney Woods product", "lumber or paper")]] +
                  [OR("Write a paragraph comparing the two regions. Use a compare word (both, similarly) and a contrast word (however, but).", "Answers vary; include land, soil, and work.", lines=5)], cols=1),
     S("Exit Ticket", [OR("Explain how soil affects the jobs people have in each region.", "Rich Delta soil supports crops; sandy Piney Woods soil supports pine forests and timber.", lines=2)])],
    tss("Students compare two regions.", "Explain how people modify and adapt to their environments.", "Workbook Lesson 1.6",
        "Delta farm vs Piney Woods town.", "Read both descriptions.", ["Model one Venn entry each."], "Check Your Understanding 1–3.",
        ["Listing facts without comparing."], ["Compare/contrast word bank."], ["Interview a relative who lived in another region."], independent="Workbook. Weekly Check Friday."),
    summary="The Delta's rich soil supports crops; the Piney Woods' sandy soil supports forests.")

# ================================================================= Week 4 · Resources and economy
L7 = Lesson("1.7", "Natural Resources",
    "I can identify Mississippi's natural resources and classify them as renewable or nonrenewable.", "C3 D2.Eco.3.3-5",
    [("natural resource", "Something from nature that people use."), ("renewable resource", "A resource that can be replaced naturally or by people in a reasonable time."),
     ("nonrenewable resource", "A resource that cannot be replaced once it is used up, or takes millions of years to form."), ("conservation", "Careful use and protection of resources.")],
    "Look around the room. What came from nature: from soil, trees, water, or underground?",
    [Text("Mississippi is rich in <b>natural resources</b>. Some are <b>renewable</b>: forests can be replanted, and fish and farm crops can grow again if they are managed well. Others are <b>nonrenewable</b>: oil and natural gas, found underground in parts of southern Mississippi and offshore in the Gulf, took millions of years to form."),
     Figure(lambda t: table(t, [["Resource", "Renewable?", "Used for"], ["fertile soil", "renewable if cared for", "growing crops"], ["forests", "renewable (replanting)", "lumber, paper, furniture"],
                                ["water (rivers, groundwater)", "renewable", "drinking, farming, fishing, transportation"], ["fish and shellfish (Gulf)", "renewable if not overfished", "food"],
                                ["oil and natural gas", "nonrenewable", "fuel, energy"], ["sand, gravel, and clay", "nonrenewable", "building roads and bricks"]],
                            [1.9 * inch, 1.7 * inch, 2.3 * inch], width=5.9 * inch, font_size=9.5)),
     Text("<b>Conservation</b> helps resources last. Foresters replant trees after harvests, farmers protect soil from erosion, and fishing seasons and limits help keep Gulf fish and shrimp populations healthy."),
     Investigate("Resource Hunt", "Where do the things in your home come from?", ["notebook"],
                 ["Find ten objects in your home.", "For each, name the natural resource it came from (wood, cotton, oil/plastic, metal, sand/glass).", "Label each resource renewable or nonrenewable.", "Circle one item you could reuse or recycle."],
                 record="a three-column chart: Object | Natural resource | Renewable or nonrenewable."),
     KeyIdea("Natural resources come from nature. Renewable resources can be replaced; nonrenewable ones cannot. Conservation helps them last.")],
    [Problem("Is a pine forest renewable or nonrenewable?", "renewable"), Problem("Is natural gas renewable?", "no, nonrenewable"), Problem("Name one way to conserve a resource.", "e.g. replant trees, recycle, fishing limits")],
    [S("Warm-Up", [SA("Something from nature people use", "natural resource"), SA("Careful use of resources", "conservation")], cols=2),
     S("Sort", [SA(q, a) for q, a in [("cotton", "renewable"), ("oil", "nonrenewable"), ("shrimp", "renewable (if managed)"), ("gravel", "nonrenewable"), ("water", "renewable"), ("timber", "renewable")]], cols=2),
     S("Apply", [OR("Choose one Mississippi resource. Explain how people use it and one way to conserve it.", "Answers vary.", lines=3)]),
     S("Exit Ticket", [OR("Why is it important to conserve even renewable resources?", "They can run out if used faster than they are replaced.", lines=2)])],
    tss("Students classify natural resources.", "Identify resources used to produce goods and services.", "Workbook Lesson 1.7",
        "Room scan.", "Read the lesson and table.", ["Model classifying resources."], "Check Your Understanding 1–3.",
        ["Thinking renewable means unlimited."], ["Picture sort."], ["Visit a recycling center or tree farm."]),
    summary="Renewable resources can be replaced; nonrenewable ones cannot; conservation helps both.")

L8 = Lesson("1.8", "Resources and Work in Each Region",
    "I can explain how natural resources shape the goods, services, and jobs in different regions.", "C3 D2.Eco.3.3-5, D2.Geo.4.3-5",
    [("goods", "Things people make or grow to sell."), ("services", "Work people do for others."), ("economy", "The way people make, buy, sell, and use goods and services."),
     ("producer", "A person or business that makes goods or provides services.")],
    "A Delta farmer, a Piney Woods mill worker, and a Gulf Coast shrimper all earn a living. What does each one depend on?",
    [Text("The <b>economy</b> of each region grows from its resources. Farmers grow goods in fertile soil. Mill workers turn trees into lumber and paper. Gulf Coast workers catch seafood, build ships, and serve visitors. Agriculture is Mississippi's largest industry, and chickens raised for meat (broilers) are among its most valuable farm products."),
     Figure(lambda t: table(t, [["Region", "Key resources", "Goods and services"], ["The Delta", "rich soil, water", "cotton, soybeans, rice, corn, farm-raised catfish"], ["Piney Woods", "pine forests", "lumber, paper, wood products"],
                                ["Black Prairie and hills", "soil, pasture", "cattle, poultry, crops, manufacturing"], ["Gulf Coast", "the Gulf, beaches, ports", "seafood, shipbuilding, shipping, tourism"]],
                            [1.6 * inch, 1.6 * inch, 2.7 * inch], width=5.9 * inch, font_size=9.5)),
     Example("Trace a product", "A pine tree becomes a notebook",
             ["Natural resource: a pine tree grows in the Piney Woods.", "Producers: loggers harvest it; a paper mill turns it into paper.", "Services: truck drivers deliver it; a store sells it.", "Consumer: you buy the notebook."],
             "One resource creates many jobs on its way to you."),
     Investigate("Regional Economy Poster", "How does one region earn a living?", ["poster paper", "markers"],
                 ["Choose one region.", "Show its resources, two goods or services, and two jobs.", "Draw arrows from each resource to the goods it produces.", "Present your poster to your family."],
                 record="your poster and a two-sentence summary."),
     KeyIdea("Natural resources shape the goods, services, and jobs in each region.")],
    [Problem("Goods or service: a haircut", "service"), Problem("Goods or service: a bag of rice", "goods"), Problem("Which region is known for shipbuilding and seafood?", "the Gulf Coast")],
    [S("Warm-Up", [SA("Things made or grown to sell", "goods"), SA("Work done for others", "services")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("A catfish farm is in which region?", "the Delta"), ("A paper mill is likely in which region?", "the Piney Woods"),
                                          ("A tour guide provides a…", "service"), ("Lumber is a…", "good")]] +
                   [OR("Trace a product (cotton T-shirt or shrimp dinner) from resource to you. Name at least three producers.", "Answers vary.", lines=4)], cols=1),
     S("Exit Ticket", [OR("How does a region's land affect its economy? Give one example.", "e.g. Delta soil supports farming jobs.", lines=2)])],
    tss("Students connect resources to regional economies.", "Identify resources used to produce goods and services; how people adapt to environments.", "Poster paper, markers, workbook Lesson 1.8, Unit 1 Review",
        "Three workers.", "Read the lesson and table.", ["Model tracing a product."], "Check Your Understanding 1–3.",
        ["Confusing goods and services."], ["Goods = hold it; services = someone does it."], ["Visit a local farm, mill, or port online."],
        independent="Workbook; then the Unit 1 Review.", exit_="Tomorrow (Friday): Unit 1 Test."),
    summary="Each region's resources shape its goods, services, and jobs.")

# ================================================================= checks
C1 = check("Weekly Check 1: Maps and Location", [S("Show what you know", [
    SA("Which map part shows directions?", "compass rose"), SA("Which map part explains symbols?", "map key (legend)"), SA("What does a scale show?", "real distance"),
    SA("Which state is east of Mississippi?", "Alabama"), SA("Which hemispheres is Mississippi in?", "Northern and Western"),
    SA("Relative or absolute: “32° N, 90° W”", "absolute")], cols=1)])
C2 = check("Weekly Check 2: Land and Water", [S("Show what you know", [
    SA("Mississippi's highest point", "Woodall Mountain"), SA("River on the western border", "Mississippi River"), SA("River that flows past Jackson", "Pearl River"),
    SA("Map that shows elevation", "physical"), SA("Map that shows county lines", "political"),
    OR("Why do most Mississippi rivers flow south?", "The land is higher in the north and slopes down to the Gulf.", lines=2)], cols=1)])
C3 = check("Weekly Check 3: Regions", [S("Show what you know", [
    SA("Flat region with rich river soil", "the Delta"), SA("Region with sandy soil and pine forests", "Piney Woods"), SA("Region with beaches and marshes", "Gulf Coast"),
    SA("Region with dark, rich soil in the northeast", "Black Prairie"),
    OR("Name one way the Delta and Piney Woods are alike and one way they are different.", "Alike: both are Mississippi regions where natural resources support work. Different: Delta is flat with rich soil for crops; Piney Woods has sandy soil and pine forests.", lines=3)], cols=1)])

REVIEW = review("Unit 1 Review", [
    S("Maps", [SA("Four map parts", "title, compass rose, key, scale"), SA("Lines that run east–west", "latitude"), SA("Mississippi borders Tennessee to the…", "north")], cols=1),
    S("Regions and resources", [SA(q, a) for q, a in [("the Delta", "flat, fertile, crops"), ("Piney Woods", "pine forests, timber"), ("Gulf Coast", "seafood, shipbuilding, tourism"),
                                                      ("oil: renewable?", "no"), ("forests: renewable?", "yes"), ("a doctor's checkup: good or service?", "service")]], cols=2)])

TEST = make_test("Unit 1 Test", [
    S("Part A · Map skills (1 point each)", [
        SA("Which map part tells what symbols mean?", "map key (legend)"), SA("Which direction is between south and west?", "southwest"),
        Problem("Use the map's scale. About how far is Jackson from Gulfport?", "about 150 miles (accept 130–170)", space=0, wide=True, fig=lambda t: mississippi_map(t, width=W * 0.4)),
        MC("Which coordinates are closest to Jackson?", ["32° N, 90° W", "32° S, 90° E", "90° N, 32° W"], 0)], cols=1),
    S("Part B · Mississippi's land (1 point each)", [
        SA("Name the states that border Mississippi.", "Tennessee, Alabama, Louisiana, Arkansas"), SA("What body of water is on Mississippi's southern coast?", "Gulf of Mexico"),
        SA("Why do most rivers in Mississippi flow south?", "The land slopes down from north to south."), MC("Which kind of map would best show county boundaries?", ["physical", "political", "elevation"], 1)], cols=1),
    S("Part C · Regions and resources (1 point each)", [
        SA("Which region has rich alluvial soil?", "the Delta"), SA("Which region is known for pine forests?", "Piney Woods"), SA("Name one Gulf Coast job.", "e.g. shrimper, shipbuilder, tour guide"),
        MC("Which is a nonrenewable resource?", ["timber", "natural gas", "catfish"], 1), SA("Goods or service: delivering mail", "service"), SA("Name one way to conserve a natural resource.", "e.g. replant trees, recycle, fishing limits")], cols=1),
    S("Part D · Explain (4 points)", [OR("Choose two Mississippi regions. Compare their land and explain how the land affects the work people do there.",
                                         "Rubric: two regions correctly described (1); one similarity (1); one difference (1); clear link between land/resources and jobs (1).", lines=8, points=4)])])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
CHECKS = [C1, C2, C3]
WEEKS = weeks_for(1, LESSONS, CHECKS, REVIEW, TEST, "social")

UNIT = Unit(1, "Mississippi: Land and Regions", "Map skills, location, landforms and rivers, natural regions, resources, and regional economies.",
    "From the flat, fertile Delta to the pine forests and the Gulf Coast, Mississippi is a state of many landscapes. In this unit you'll learn to read maps like a geographer, find Mississippi's place in the world, explore its rivers and regions, and discover how its natural resources shape the way people live and work.",
    ["Read maps using the title, compass rose, key, and scale.", "Describe Mississippi's relative and absolute location.", "Identify landforms, waterways, and natural regions.",
     "Classify natural resources and explain how they shape regional economies."],
    [("C3 D2.Geo.1–4", "Maps; places and regions; human–environment interaction."), ("C3 D2.Eco.3", "Resources used to produce goods and services.")],
    [("compass rose", "Shows directions on a map."), ("latitude", "Lines measuring distance north or south of the equator."), ("region", "An area with shared features."),
     ("natural resource", "Something from nature people use."), ("goods", "Things made or grown to sell."), ("services", "Work done for others.")],
    ["Cardinal directions."], ["Globe or world map", "Mississippi road map (optional)", "Salt dough materials", "Index cards, poster paper"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Pilots, truck drivers, farmers, and city planners all depend on maps and on knowing what each region's land can do.",
    family_note="On your next drive, look at a map together before you leave and track your route, directions, and the rivers you cross.",
    weeks=WEEKS)
