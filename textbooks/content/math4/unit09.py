"""Grade 4 Math · Unit 9: Measurement, Area, and Perimeter (May 24 – Jun 18, 2027)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import c, F, MX
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def R(l, w, unit="", grid=False, **kw):
    return lambda t: rect_fig(t, l, w, unit, grid=grid, width=kw.pop("width", CW), **kw)


def AP(l, w, u):
    return f"P = {2 * (l + w)} {u}, A = {l * w} sq {u}"


L1 = Lesson("9.1", "Perimeter",
    "I can find the perimeter of a shape by adding the lengths of its sides.", "4.MD.3",
    [("perimeter", "The distance around a figure.")],
    "Dad is putting a fence around a garden that is 12 feet long and 8 feet wide. How much fencing does he need?",
    [Text("<b>Perimeter</b> is the distance <b>around</b> a shape. Add the lengths of all the sides."),
     Figure(R(12, 8, "ft", width=260), "A garden 12 ft by 8 ft."),
     Example("Add the sides", "Find the perimeter of the garden.", ["A rectangle has two lengths and two widths.", "12 + 8 + 12 + 8 = 40."], "40 feet of fencing"),
     Example("Any polygon", "A triangle has sides 7 cm, 9 cm, and 5 cm. Find the perimeter.", ["7 + 9 + 5 = 21."], "21 cm"),
     KeyIdea("Perimeter: add all the side lengths. The answer is in units (cm, ft), not square units.")],
    [Problem("Rectangle 10 m by 4 m: perimeter?", "28 m"), Problem("Square with 6-inch sides: perimeter?", "24 in."), Problem("Pentagon with all sides 3 ft: perimeter?", "15 ft")],
    [S("Warm-Up", [Problem("12 + 8 + 12 + 8", "40"), Problem("4 × 9", "36")]),
     S("Find the perimeter", [Problem("", f"{2 * (l + w)} {u}", fig=R(l, w, u), space=0) for l, w, u in [(9, 4, "cm"), (15, 6, "in."), (7, 7, "m"), (20, 11, "ft")]]),
     S("Solve", [Problem("A picture frame is 14 inches by 10 inches. How much wood goes around the edge?", "48 inches", space=40, wide=True),
                 Problem("A square tile has a perimeter of 32 cm. How long is each side?", "8 cm", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Draw a rectangle with a perimeter of 18 units.", "e.g. 5 × 4 or 6 × 3 or 7 × 2", space=50, wide=True)], cols=1)],
    TE("Students find perimeter.", "Apply the area and perimeter formulas for rectangles in real-world and mathematical problems.", "Ruler, string, workbook Lesson 9.1",
       flow("Addition warm-up.", "Read Let's Explore.", ["Walk around a rug or table and count steps: that's perimeter.", "Work both examples."], "Try It 1–3."),
       ["Adding only two sides of a rectangle."], ["Label every side before adding."], ["Find the perimeter of your bedroom."]),
    summary="Perimeter is the distance around: add all the side lengths.")

L2 = Lesson("9.2", "Area",
    "I can find the area of a rectangle by counting square units and by multiplying.", "4.MD.3",
    [("area", "The number of square units that cover a flat surface."), ("square unit", "A square 1 unit long on each side, like a square inch or square meter.")],
    "How many 1-foot square tiles cover a floor that is 6 feet long and 4 feet wide?",
    [Text("<b>Area</b> measures how much surface a shape <b>covers</b>. We count square units."),
     Figure(R(6, 4, "ft", grid=True, width=260), "4 rows of 6 squares = 24 square feet."),
     Text("The tiles form an array: 4 rows of 6. Multiplication is faster than counting: 6 × 4 = 24 square feet."),
     Example("Multiply", "Find the area of a rectangle 9 m long and 7 m wide.", ["Area = length × width.", "9 × 7 = 63."], "63 square meters"),
     WatchOut("Area is in <b>square</b> units (sq ft, sq m). Perimeter is in plain units (ft, m)."),
     KeyIdea("Area of a rectangle = length × width.")],
    [Problem("Rectangle 8 in. by 5 in.: area?", "40 sq in."), Problem("Square with 9 cm sides: area?", "81 sq cm"), Problem("A room 12 ft by 10 ft: area?", "120 sq ft")],
    [S("Warm-Up", [Problem("6 × 4", "24"), Problem("Perimeter of a 6 × 4 rectangle", "20")]),
     S("Count the squares (each square is 1 sq unit)", [Problem("", f"{l * w} sq units", fig=R(l, w, grid=True), space=0) for l, w in [(5, 3), (7, 2), (4, 4), (6, 3)]]),
     S("Find the area", [Problem(f"{l} {u} by {w} {u}", f"{l * w} sq {u}") for l, w, u in [(10, 6, "m"), (12, 4, "ft"), (25, 3, "in."), (14, 11, "cm")]]),
     S("Exit Ticket", [Problem("A rug is 7 feet by 5 feet. What is its area? What is its perimeter?", "35 sq ft; 24 ft", space=40, wide=True)], cols=1)],
    TE("Students find area of rectangles.", "Apply the area formula for rectangles.", "Square tiles or grid paper, workbook Lesson 9.2",
       flow("6 × 4.", "Read Let's Explore. Cover a rectangle with tiles.", ["Show rows × columns = area.", "Read the Watch Out."], "Try It 1–3."),
       ["Mixing up area and perimeter.", "Forgetting square units."], ["Tiles."], ["Find the area of a book cover."]),
    summary="Area counts square units: length × width.")

L3 = Lesson("9.3", "Area and Perimeter Formulas",
    "I can use the formulas P = 2 × l + 2 × w and A = l × w.", "4.MD.3",
    [("formula", "A rule written with symbols, like A = l × w.")],
    "Is there a shortcut for adding 2 lengths and 2 widths?",
    [Text("Mathematicians write rules as <b>formulas</b>. For a rectangle with length l and width w:"),
     Figure(lambda t: table(t, [["Measure", "Formula", "Example: 9 × 5"], ["Perimeter", "P = 2 × l + 2 × w", "2 × 9 + 2 × 5 = 28"], ["Area", "A = l × w", "9 × 5 = 45"]],
                            [1.4 * inch, 2.2 * inch, 2.2 * inch], width=5.8 * inch)),
     Example("Use both formulas", "A garden is 16 ft by 9 ft. Find P and A.", ["P = 2 × 16 + 2 × 9 = 32 + 18 = 50.", "A = 16 × 9 = 144."], "P = 50 ft, A = 144 sq ft"),
     KeyIdea("P = 2 × l + 2 × w. A = l × w.")],
    [Problem("13 cm by 6 cm", AP(13, 6, "cm")), Problem("20 m by 15 m", AP(20, 15, "m")), Problem("Square, 11 in. sides", AP(11, 11, "in."))],
    [S("Warm-Up", [Problem("2 × 16 + 2 × 9", "50"), Problem("16 × 9", "144")]),
     S("Find the perimeter and area", [Problem(f"{l} by {w} {u}", AP(l, w, u), space=30) for l, w, u in [(8, 3, "ft"), (12, 7, "cm"), (25, 10, "m"), (9, 9, "in."), (30, 18, "yd"), (45, 20, "ft")]]),
     S("Exit Ticket", [Problem("A basketball court is 94 ft by 50 ft. Find its perimeter and area.", AP(94, 50, "ft"), space=40, wide=True)], cols=1)],
    TE("Students apply perimeter and area formulas.", "Apply the area and perimeter formulas for rectangles.", "Workbook Lesson 9.3", flow("Warm-up.", "Read Let's Explore.", ["Write the formulas on a card. Work the example."], "Try It 1–3."),
       ["Using A = 2 × l + 2 × w."], ["Formula card."], ["Write a formula for the perimeter of a square (P = 4 × s)."]), summary="P = 2 × l + 2 × w and A = l × w.")

L4 = Lesson("9.4", "Same Perimeter, Different Area",
    "I can show that rectangles with the same perimeter can have different areas.", "4.MD.3",
    [],
    "You have 24 feet of fence for a rabbit pen. Which rectangle gives the rabbit the most room?",
    [Figure(lambda t: table(t, [["Length", "Width", "Perimeter", "Area"]] + [[str(l), str(12 - l), "24 ft", f"{l * (12 - l)} sq ft"] for l in range(1, 7)],
                            [1.1 * inch] * 4, width=4.4 * inch)),
     Text("All these pens use 24 feet of fence, but the areas are very different. The 6 × 6 square gives the most room: 36 square feet."),
     KeyIdea("For a fixed perimeter, the closer the rectangle is to a square, the bigger its area.")],
    [Problem("Two rectangles have perimeter 16. One is 7 × 1, one is 4 × 4. Which has more area?", "4 × 4 (16 vs 7)"), Problem("A rectangle has area 12. Name two possible perimeters.", "e.g. 14 (3 × 4), 16 (2 × 6), 26 (1 × 12)"),
     Problem("Same area 36: which has the smaller perimeter, 9 × 4 or 6 × 6?", "6 × 6 (24 vs 26)")],
    [S("Warm-Up", [Problem("Perimeter of 5 × 3", "16"), Problem("Area of 5 × 3", "15")]),
     S("Perimeter 20 units: complete the table", [Problem(f"Length {l}, width ___, area ___", f"width {10 - l}, area {l * (10 - l)}") for l in [1, 2, 3, 4, 5, 6]]),
     S("Exit Ticket", [Problem("Which rectangle with perimeter 20 has the greatest area? Why?", "5 × 5 = 25; closest to a square", lines=2, space=0, wide=True)], cols=1)],
    TE("Students explore how area changes with fixed perimeter.", "Apply area and perimeter in real-world problems.", "String loop of 24 inches, grid paper, workbook Lesson 9.4",
       flow("Perimeter and area of 5 × 3.", "Read Let's Explore.", ["Make rectangles with a 24-inch string loop on grid paper; record each area."], "Try It 1–3. Weekly Check tomorrow."),
       ["Thinking same perimeter means same area."], ["Use grid paper."], ["Same area 24: find all rectangles and their perimeters."]),
    summary="Rectangles with the same perimeter can have different areas; squares give the most area.")

L5 = Lesson("9.5", "Finding an Unknown Side",
    "I can find a missing side length when I know the area or perimeter.", "4.MD.3",
    [],
    "A rectangle has an area of 48 square feet and a length of 8 feet. How wide is it?",
    [Example("From area", "A = 48 sq ft, l = 8 ft. Find w.", ["8 × w = 48.", "48 ÷ 8 = 6."], "6 feet"),
     Example("From perimeter", "P = 30 m, l = 9 m. Find w.", ["Two lengths: 2 × 9 = 18.", "30 − 18 = 12 for the two widths.", "12 ÷ 2 = 6."], "6 m"),
     KeyIdea("Write the formula with a letter for the unknown, then use the inverse operation.")],
    [Problem("A = 56 sq in., l = 7 in. Find w.", "8 in."), Problem("P = 26 cm, l = 8 cm. Find w.", "5 cm"), Problem("Square with A = 64 sq m. Side?", "8 m")],
    [S("Warm-Up", [Problem("48 ÷ 8", "6"), Problem("30 − 18", "12")]),
     S("Find the unknown side", [Problem("A = 72 sq ft, l = 9 ft", "w = 8 ft"), Problem("A = 90 sq cm, w = 6 cm", "l = 15 cm"), Problem("P = 40 m, l = 12 m", "w = 8 m"),
                                 Problem("P = 50 in., w = 10 in.", "l = 15 in."), Problem("Square, P = 36 ft", "side = 9 ft"), Problem("A = 120 sq yd, l = 12 yd", "w = 10 yd")]),
     S("Solve", [Problem("A patio has an area of 96 square feet. It is 12 feet long. How wide is it? What is its perimeter?", "8 ft wide; 40 ft", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("A rectangle has P = 34 cm and l = 11 cm. Find w and the area.", "w = 6 cm; A = 66 sq cm", space=40, wide=True)], cols=1)],
    TE("Students find unknown side lengths.", "Apply the area and perimeter formulas, e.g., find the width given the area and length.", "Workbook Lesson 9.5", flow("48 ÷ 8.", "Read Let's Explore.", ["Work both examples with equations."], "Try It 1–3."),
       ["Dividing the perimeter by the length."], ["Draw and label the rectangle."], ["Garden design with a set area."]), summary="Use the formula and the inverse operation to find a missing side.")

L6 = Lesson("9.6", "Area of Combined Rectangles",
    "I can find the area of a shape made of rectangles by breaking it apart.", "4.MD.3",
    [("composite figure", "A shape made by joining simpler shapes.")],
    "An L-shaped room needs new carpet. How can we find its area?",
    [Text("Break the shape into rectangles, find each area, and add."),
     Figure(lambda t: l_shape(t, 10, 8, 4, 3, "ft", width=260, height=150), "An L-shaped room"),
     Example("Break it apart", "Find the area of the L-shape.", ["Bottom rectangle: 10 × 3 = 30.", "Top rectangle: 4 × (8 − 3) = 4 × 5 = 20.", "Add: 30 + 20 = 50."], "50 sq ft"),
     KeyIdea("Split into rectangles, find each area, add. Find missing side lengths by subtracting.")],
    [Problem("Two rectangles: 5 × 4 and 3 × 2. Total area?", "26 sq units"), Problem("A 10 × 10 square with a 2 × 2 corner cut out. Area?", "96 sq units"), Problem("L-shape: bottom 8 × 2, top 3 × 4. Area?", "28 sq units")],
    [S("Warm-Up", [Problem("10 × 3 + 4 × 5", "50"), Problem("8 − 3", "5")]),
     S("Find the area", [Problem("", "48 sq m (12 × 3 + 3 × 4)", fig=lambda t: l_shape(t, 12, 7, 3, 3, "m", width=CW, height=110), space=40),
                         Problem("", "34 sq ft (6 × 4 + 2 × 5)", fig=lambda t: l_shape(t, 6, 9, 2, 4, "ft", width=CW, height=110), space=40),
                         Problem("", "70 sq cm (10 × 5 + 4 × 5)", fig=lambda t: l_shape(t, 10, 10, 4, 5, "cm", width=CW, height=110), space=40),
                         Problem("", "45 sq yd (9 × 3 + 6 × 3)", fig=lambda t: l_shape(t, 9, 6, 6, 3, "yd", width=CW, height=110), space=40)]),
     S("Exit Ticket", [Problem("Draw an L-shape, label its sides, and find its area.", "Answers vary.", space=70, wide=True)], cols=1)],
    TE("Students find the area of composite rectilinear figures.", "Apply area formulas to real-world problems (rectilinear figures; supports 3.MD.7d).", "Grid paper, workbook Lesson 9.6",
       flow("Warm-up.", "Read Let's Explore.", ["Cut an L-shape from grid paper into two rectangles.", "Say: Break it, find each area, add."], "Try It 1–3."),
       ["Using the wrong side lengths for the smaller rectangle."], ["Shade each part a different color."], ["Find the area of your home's floor plan."]),
    summary="Break a combined shape into rectangles, find each area, and add.")

L7 = Lesson("9.7", "Area and Perimeter Word Problems",
    "I can solve real-world problems with area and perimeter.", "4.MD.3",
    [],
    "Tile costs $3 per square foot. How much does it cost to tile a 9-foot by 6-foot bathroom?",
    [Example("Area, then cost", "Tile a 9 ft × 6 ft room at $3 per sq ft.", ["Area: 9 × 6 = 54 sq ft.", "Cost: 54 × 3 = 162."], "$162"),
     Example("Perimeter, then cost", "Border trim costs $2 per foot. Trim the same room.", ["Perimeter: 2 × 9 + 2 × 6 = 30 ft.", "Cost: 30 × 2 = 60."], "$60"),
     KeyIdea("Covering → area. Going around → perimeter.")],
    [Problem("Carpet for a 12 ft × 10 ft room at $4 per sq ft?", "$480"), Problem("Fence around a 20 m × 15 m field at $5 per meter?", "$350"), Problem("How many 1-ft tiles for a 7 ft × 8 ft floor?", "56 tiles")],
    [S("Warm-Up", [Problem("54 × 3", "162"), Problem("30 × 2", "60")]),
     S("Solve", [Problem("Grass seed covers 100 square feet per bag. A yard is 30 ft by 20 ft. How many bags?", "6 bags", space=50, wide=True),
                 Problem("Lillie puts ribbon around a 16 in. × 12 in. poster. Ribbon costs $1 per 4 inches. How much does it cost?", "$14 (56 in.)", space=50, wide=True),
                 Problem("A garden 15 ft × 8 ft has a 3 ft × 4 ft shed in it. How much of the garden can be planted?", "108 sq ft", space=50, wide=True),
                 Problem("Mom paints a wall 12 ft by 9 ft with a 3 ft by 4 ft window. How many square feet does she paint?", "96 sq ft", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write your own area or perimeter word problem and solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve area and perimeter word problems.", "Apply area and perimeter formulas in real-world problems.", "Workbook Lesson 9.7", flow("Warm-up.", "Read Let's Explore.", ["Work both examples. Ask: covering or going around?"], "Try It 1–3."),
       ["Using perimeter for covering problems."], ["Draw the shape."], ["Plan and price a real room makeover."]), summary="Decide: covering (area) or going around (perimeter)? Then compute.")

L8 = Lesson("9.8", "Area or Perimeter?",
    "I can decide whether a problem needs area or perimeter and explain why.", "4.MD.3",
    [],
    "Are you finding area or perimeter when you put a frame on a picture? When you paint the picture?",
    [Figure(lambda t: table(t, [["Situation", "Area or perimeter?"], ["fence around a yard", "perimeter"], ["carpet for a room", "area"], ["trim around a door", "perimeter"],
                                ["paint for a wall", "area"], ["lace around a pillow", "perimeter"], ["grass seed for a lawn", "area"]], [3.0 * inch, 2.0 * inch], width=5.0 * inch)),
     KeyIdea("Covering a surface → area (square units). Edge or border → perimeter (units).")],
    [Problem("A border of tape around a table top", "perimeter"), Problem("Wrapping paper to cover a box's top", "area"), Problem("A path around a pond", "perimeter")],
    [S("Warm-Up", [Problem("Area of 8 × 7", "56"), Problem("Perimeter of 8 × 7", "30")]),
     S("Area or perimeter? Then solve.", [Problem("Tiles for a 5 ft × 5 ft floor", "area; 25 sq ft", space=24), Problem("Fence for a 10 m × 6 m garden", "perimeter; 32 m", space=24),
                                          Problem("Rug for a 9 ft × 12 ft room", "area; 108 sq ft", space=24), Problem("Frame for a 8 in. × 10 in. photo", "perimeter; 36 in.", space=24)]),
     S("Exit Ticket", [Problem("Explain the difference between area and perimeter using your bedroom.", "Area: floor covering; perimeter: baseboard around the room.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students choose between area and perimeter.", "Apply area and perimeter formulas.", "Workbook Lesson 9.8", flow("Warm-up.", "Read Let's Explore.", ["Sort situation cards into area/perimeter."], "Try It 1–3. Weekly Check tomorrow."),
       ["Using key words without visualizing."], ["Act it out with a finger: trace (perimeter) or rub (area)."], ["Find 3 area and 3 perimeter jobs at home."]), summary="Covering → area. Edge or border → perimeter.")

L9 = Lesson("9.9", "Customary Length",
    "I can convert between inches, feet, yards, and miles.", "4.MD.1",
    [("convert", "To change a measurement to a different unit."), ("customary units", "Units used in the U.S.: inches, feet, yards, miles, ounces, pounds, cups, gallons.")],
    "Lillie is 4 feet 6 inches tall. How many inches tall is she?",
    [Figure(lambda t: table(t, [["Unit", "Equals"], ["1 foot (ft)", "12 inches (in.)"], ["1 yard (yd)", "3 feet = 36 inches"], ["1 mile (mi)", "5,280 feet"]], [2.0 * inch, 3.0 * inch], width=5.0 * inch)),
     Text("To change a <b>larger</b> unit to a <b>smaller</b> unit, multiply. There are more of the small units."),
     Example("Feet and inches to inches", "4 ft 6 in. = ___ in.", ["4 × 12 = 48 inches.", "48 + 6 = 54."], "54 inches"),
     Example("Make a table", "Yards to feet", ["Multiply by 3: 1 → 3, 2 → 6, 3 → 9, 4 → 12."], "yards × 3 = feet"),
     KeyIdea("Big unit → small unit: multiply by how many small units are in one big unit.")],
    [Problem("5 ft = ___ in.", "60"), Problem("7 yd = ___ ft", "21"), Problem("2 mi = ___ ft", "10,560")],
    [S("Warm-Up", [Problem("12 × 6", "72"), Problem("3 × 9", "27")]),
     S("Convert", [Problem("3 ft = ___ in.", "36"), Problem("8 ft = ___ in.", "96"), Problem("4 yd = ___ ft", "12"), Problem("10 yd = ___ ft", "30"),
                   Problem("2 yd = ___ in.", "72"), Problem("3 ft 4 in. = ___ in.", "40"), Problem("6 ft 2 in. = ___ in.", "74"), Problem("3 mi = ___ ft", "15,840")]),
     S("Complete the table", [Problem("Feet: 1, 2, 3, 4, 5 → Inches", "12, 24, 36, 48, 60", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which is longer: 2 yards or 70 inches? Explain.", "2 yards (72 in.) > 70 in.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students convert customary length units.", "Know relative sizes of measurement units; express larger units in terms of smaller units; record in a two-column table.", "Ruler, yardstick, tape measure, workbook Lesson 9.9",
       flow("12 × 6.", "Read Let's Explore. Measure each other.", ["Show 1 ft on a ruler, 1 yd on a yardstick.", "Say: Big to small, multiply."], "Try It 1–3."), ["Dividing instead of multiplying."], ["Conversion card."], ["Measure a room in feet and convert to inches."]),
    summary="1 ft = 12 in., 1 yd = 3 ft, 1 mi = 5,280 ft. Big to small: multiply.")

L10 = Lesson("9.10", "Customary Weight and Capacity",
    "I can convert ounces and pounds, and cups, pints, quarts, and gallons.", "4.MD.1",
    [("weight", "How heavy something is."), ("capacity", "How much a container holds.")],
    "A recipe needs 3 quarts of water. How many cups is that?",
    [Figure(lambda t: table(t, [["Weight", "Capacity"], ["1 pound (lb) = 16 ounces (oz)", "1 pint (pt) = 2 cups (c)"], ["", "1 quart (qt) = 2 pints = 4 cups"], ["", "1 gallon (gal) = 4 quarts = 16 cups"]],
                            [2.6 * inch, 3.0 * inch], width=5.6 * inch)),
     Example("Quarts to cups", "3 qt = ___ c", ["1 qt = 4 c.", "3 × 4 = 12."], "12 cups"),
     Example("Pounds to ounces", "2 lb 5 oz = ___ oz", ["2 × 16 = 32.", "32 + 5 = 37."], "37 oz"),
     KeyIdea("Learn the facts: 16 oz = 1 lb; 2 c = 1 pt; 2 pt = 1 qt; 4 qt = 1 gal.")],
    [Problem("4 lb = ___ oz", "64"), Problem("2 gal = ___ qt", "8"), Problem("5 pt = ___ c", "10")],
    [S("Warm-Up", [Problem("16 × 3", "48"), Problem("4 × 4", "16")]),
     S("Convert", [Problem("3 lb = ___ oz", "48"), Problem("1 lb 8 oz = ___ oz", "24"), Problem("6 qt = ___ c", "24"), Problem("3 gal = ___ qt", "12"),
                   Problem("4 qt = ___ pt", "8"), Problem("1 gal = ___ c", "16"), Problem("7 pt = ___ c", "14"), Problem("5 lb = ___ oz", "80")]),
     S("Solve", [Problem("A jug holds 1 gallon of tea. How many 1-cup glasses can it fill?", "16 glasses", space=30, wide=True),
                 Problem("A puppy weighs 4 lb 3 oz. How many ounces is that?", "67 oz", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which is more: 3 quarts or 10 cups? Explain.", "3 quarts (12 cups) > 10 cups", lines=2, space=0, wide=True)], cols=1)],
    TE("Students convert customary weight and capacity.", "Express larger units in terms of smaller units within one system.", "Measuring cups, pint/quart/gallon containers, kitchen scale, workbook Lesson 9.10",
       flow("16 × 3.", "Read Let's Explore.", ["Pour water: 2 cups into a pint, 2 pints into a quart, 4 quarts into a gallon.", "Weigh a 1-lb item."], "Try It 1–3."), ["Confusing fluid ounces with ounces of weight."], ["Kitchen measuring."], ["Gallon creature drawing (G with Q's, P's, C's)."]),
    summary="16 oz = 1 lb; 2 c = 1 pt; 2 pt = 1 qt; 4 qt = 1 gal.")

L11 = Lesson("9.11", "Metric Units",
    "I can convert metric units of length, mass, and capacity.", "4.MD.1",
    [("metric units", "Units based on 10s: meters, grams, liters."), ("mass", "The amount of matter in an object, measured in grams and kilograms.")],
    "A race is 5 kilometers long. How many meters is that?",
    [Figure(lambda t: table(t, [["Length", "Mass", "Capacity"], ["1 cm = 10 mm", "1 kg = 1,000 g", "1 L = 1,000 mL"], ["1 m = 100 cm", "", ""], ["1 km = 1,000 m", "", ""]],
                            [1.9 * inch, 1.9 * inch, 1.9 * inch], width=5.7 * inch)),
     Text("Metric units use place value: kilo- means 1,000, centi- means one hundredth, milli- means one thousandth."),
     Example("Kilometers to meters", "5 km = ___ m", ["1 km = 1,000 m.", "5 × 1,000 = 5,000."], "5,000 m"),
     KeyIdea("Metric conversions multiply by 10, 100, or 1,000.")],
    [Problem("3 m = ___ cm", "300"), Problem("4 kg = ___ g", "4,000"), Problem("2 L = ___ mL", "2,000")],
    [S("Warm-Up", [Problem("6 × 1,000", "6,000"), Problem("8 × 100", "800")]),
     S("Convert", [Problem("7 m = ___ cm", "700"), Problem("2 km = ___ m", "2,000"), Problem("9 cm = ___ mm", "90"), Problem("6 kg = ___ g", "6,000"),
                   Problem("5 L = ___ mL", "5,000"), Problem("3 m 25 cm = ___ cm", "325"), Problem("1 kg 500 g = ___ g", "1,500"), Problem("4 km 20 m = ___ m", "4,020")]),
     S("Solve", [Problem("A water bottle holds 750 mL. How many mL do 4 bottles hold? Is that more than 3 L?", "3,000 mL; equal to 3 L", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which is longer: 2 m or 150 cm? Explain.", "2 m (200 cm)", lines=2, space=0, wide=True)], cols=1)],
    TE("Students convert metric units.", "Express larger units in terms of smaller units within the metric system.", "Meter stick, liter bottle, kitchen scale, workbook Lesson 9.11",
       flow("6 × 1,000.", "Read Let's Explore.", ["Show cm and m on a meter stick; a 1 L bottle; a 1 kg bag."], "Try It 1–3."), ["Using 12 or 16 for metric."], ["Place-value chart for metric."], ["Measure your height in cm and m."]),
    summary="Metric units convert by 10, 100, or 1,000: 1 m = 100 cm, 1 km = 1,000 m, 1 kg = 1,000 g, 1 L = 1,000 mL.")

L12 = Lesson("9.12", "Time Conversions",
    "I can convert hours, minutes, seconds, days, and weeks.", "4.MD.1",
    [],
    "Ellie's soccer practice is 90 minutes. Is that more or less than 2 hours?",
    [Figure(lambda t: table(t, [["Unit", "Equals"], ["1 minute", "60 seconds"], ["1 hour", "60 minutes"], ["1 day", "24 hours"], ["1 week", "7 days"], ["1 year", "12 months = 52 weeks (about) = 365 days"]],
                            [1.6 * inch, 3.8 * inch], width=5.4 * inch)),
     Example("Hours and minutes", "2 hours = ___ minutes", ["2 × 60 = 120."], "120 minutes, so 90 minutes is less"),
     Example("Mixed units", "1 hr 25 min = ___ min", ["60 + 25 = 85."], "85 minutes"),
     KeyIdea("60 seconds = 1 minute; 60 minutes = 1 hour; 24 hours = 1 day; 7 days = 1 week.")],
    [Problem("3 hr = ___ min", "180"), Problem("4 min = ___ sec", "240"), Problem("2 weeks = ___ days", "14")],
    [S("Warm-Up", [Problem("60 × 3", "180"), Problem("24 × 2", "48")]),
     S("Convert", [Problem("5 min = ___ sec", "300"), Problem("4 hr = ___ min", "240"), Problem("3 days = ___ hr", "72"), Problem("6 weeks = ___ days", "42"),
                   Problem("2 hr 15 min = ___ min", "135"), Problem("1 min 40 sec = ___ sec", "100"), Problem("1 day 6 hr = ___ hr", "30"), Problem("3 years = ___ months", "36")]),
     S("Exit Ticket", [Problem("Which is longer: 200 minutes or 3 hours? By how much?", "200 min, by 20 min", lines=2, space=0, wide=True)], cols=1)],
    TE("Students convert units of time.", "Know relative sizes of units of time; express larger units in smaller units.", "Clock, calendar, workbook Lesson 9.12", flow("60 × 3.", "Read Let's Explore.", ["Work the examples on a clock."], "Try It 1–3. Weekly Check tomorrow."),
       ["Using 100 minutes per hour."], ["Clock."], ["How many seconds are in a day? (86,400)"]), summary="60 sec = 1 min; 60 min = 1 hr; 24 hr = 1 day; 7 days = 1 week.")

L13 = Lesson("9.13", "Elapsed Time",
    "I can find how much time has passed and find start or end times.", "4.MD.2",
    [("elapsed time", "The amount of time that passes from the start to the end of an event.")],
    "A movie starts at 2:45 p.m. and ends at 4:20 p.m. How long is the movie?",
    [Text("Count up from the start time in friendly jumps: to the next hour, then whole hours, then minutes."),
     Figure(lambda t: number_line(t, 0, 95, 5, 15, points=[(0, "2:45"), (15, "3:00"), (75, "4:00"), (95, "4:20")], tick_labels=False, hops=[(0, 15, "15 min"), (15, 75, "1 hr"), (75, 95, "20 min")])),
     Example("Count up", "2:45 to 4:20", ["2:45 → 3:00 is 15 minutes.", "3:00 → 4:00 is 1 hour.", "4:00 → 4:20 is 20 minutes.", "Total: 1 hr 35 min."], "1 hour 35 minutes"),
     Example("Find the end time", "Start 9:30 a.m., lasts 2 hr 45 min.", ["9:30 + 2 hr = 11:30.", "11:30 + 45 min = 12:15 p.m."], "12:15 p.m."),
     KeyIdea("Jump to the next hour, then by hours, then by minutes. Watch for a.m. and p.m.")],
    [Problem("1:20 p.m. to 3:50 p.m.", "2 hr 30 min"), Problem("Start 10:15, 1 hr 50 min later?", "12:05"), Problem("Ends 5:00 p.m., lasted 2 hr 20 min. Start?", "2:40 p.m.")],
    [S("Warm-Up", [Problem("60 − 45", "15"), Problem("1 hr 35 min = ___ min", "95")]),
     S("Find the elapsed time", [Problem("8:15 a.m. to 11:00 a.m.", "2 hr 45 min"), Problem("12:40 p.m. to 2:10 p.m.", "1 hr 30 min"), Problem("3:25 p.m. to 6:05 p.m.", "2 hr 40 min"), Problem("10:50 a.m. to 1:15 p.m.", "2 hr 25 min")]),
     S("Find the end or start time", [Problem("Start 7:45 a.m., lasts 1 hr 30 min", "9:15 a.m."), Problem("Start 4:20 p.m., lasts 2 hr 55 min", "7:15 p.m."), Problem("End 3:30 p.m., lasted 45 min", "2:45 p.m."), Problem("End 11:10 a.m., lasted 3 hr 25 min", "7:45 a.m.")]),
     S("Exit Ticket", [Problem("School starts at 8:30 a.m. and ends at 2:15 p.m. How long is the school day?", "5 hr 45 min", space=30, wide=True)], cols=1)],
    TE("Students solve elapsed time problems.", "Solve word problems involving intervals of time using number line diagrams.", "Clock, workbook Lesson 9.13", flow("60 − 45.", "Read Let's Explore.", ["Model counting up on a time number line."], "Try It 1–3."),
       ["Subtracting times like whole numbers (420 − 245)."], ["Time number lines."], ["Plan a day's schedule with elapsed times."]), summary="Count up from the start time to the next hour, then by hours, then minutes.")

L14 = Lesson("9.14", "Measurement Problems with Fractions and Decimals",
    "I can solve measurement problems that use fractions and decimals.", "4.MD.2",
    [],
    f"A recipe needs {F(3, 4)} cup of milk per batch. How much for 3 batches? How many pints is that?",
    [Example("Fractions", "3 batches of 3/4 cup".replace("3/4", F(3, 4)), [f"3 × {F(3, 4)} = {F(9, 4)} = {MX(2, 1, 4)} cups.", f"2 cups = 1 pint, so it is a little more than 1 pint."], MX(2, 1, 4) + " cups"),
     Example("Decimals", "A bottle holds 1.5 L. How many mL?", ["1 L = 1,000 mL. 1.5 L = 1,000 + 500."], "1,500 mL"),
     KeyIdea("Convert to the same unit, then compute with fractions or decimals.")],
    [Problem(f"{F(1, 2)} ft = ___ in.", "6"), Problem(f"{F(1, 4)} hour = ___ minutes", "15"), Problem("2.5 m = ___ cm", "250")],
    [S("Warm-Up", [Problem(f"4 × {F(1, 4)}", "1"), Problem(f"{F(1, 2)} of 60", "30")]),
     S("Convert", [Problem(f"{F(1, 2)} hr = ___ min", "30"), Problem(f"{F(3, 4)} ft = ___ in.", "9"), Problem(f"{F(1, 4)} lb = ___ oz", "4"), Problem("0.5 kg = ___ g", "500")]),
     S("Solve", [Problem(f"Ellie runs {F(3, 4)} mile each day for 6 days. How far does she run?", MX(4, 2, 4) + " miles", space=40, wide=True),
                 Problem("A ribbon 3.5 m long is cut into two pieces. One is 1.25 m. How long is the other?", "2.25 m", space=40, wide=True),
                 Problem(f"Dad's workout is {MX(1, 1, 2)} hours. How many minutes is that?", "90 minutes", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem(f"Which is longer: {F(2, 3)} hour or 35 minutes?", f"{F(2, 3)} hour (40 min)", lines=1, space=0, wide=True)], cols=1)],
    TE("Students solve measurement problems with fractions and decimals.", "Solve word problems involving measurements with simple fractions or decimals.", "Workbook Lesson 9.14", flow("4 × 1/4.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."),
       ["Converting fractions of hours using 100."], ["Clock face fractions."], ["Double a recipe with fractions."]), summary="Convert to the same unit, then compute with fractions or decimals.")

L15 = Lesson("9.15", "Multi-Step Measurement Problems",
    "I can solve multi-step problems with measurement and conversions.", "4.MD.2",
    [],
    "Lillie needs 3 pieces of rope, each 2 feet 4 inches long. She has a 9-foot rope. Is it enough?",
    [Example("Convert, multiply, compare", "3 pieces of 2 ft 4 in. from 9 ft", ["2 ft 4 in. = 28 in.", "3 × 28 = 84 in.", "9 ft = 108 in.", "108 − 84 = 24 in. left."], "Yes, with 2 feet left"),
     KeyIdea("Change to the smallest unit first. Then solve step by step.")],
    [Problem("4 boards of 1 ft 6 in. Total in feet?", "6 ft"), Problem("A 2-gallon jug fills how many 1-cup glasses?", "32"), Problem("3 movies of 1 hr 40 min. Total time?", "5 hr")],
    [S("Warm-Up", [Problem("2 ft 4 in. = ___ in.", "28"), Problem("9 ft = ___ in.", "108")]),
     S("Solve", [Problem("A baby weighed 7 lb 8 oz at birth and gained 1 lb 12 oz. How much does she weigh now?", "9 lb 4 oz", space=50, wide=True),
                 Problem("Ellie practices piano 25 minutes a day for 2 weeks. How many hours and minutes is that?", "5 hr 50 min (350 min)", space=50, wide=True),
                 Problem("A 2-liter bottle fills glasses of 250 mL. How many glasses?", "8 glasses", space=50, wide=True),
                 Problem("A hike is 3 miles. Lillie has walked 9,240 feet. How many more feet? (1 mi = 5,280 ft)", "6,600 feet", space=50, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write and solve a two-step measurement problem.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve multi-step measurement problems.", "Use the four operations to solve word problems involving distances, time, volume, mass, and money.", "Workbook Lesson 9.15",
       flow("Conversions.", "Read Let's Explore.", ["Work the example: convert first."], "Try It 1–3."), ["Mixing units in one computation."], ["Convert first."], ["Plan a road trip with distances and times."]),
    summary="Convert to one unit first, then solve step by step.")

L16 = Lesson("9.16", "Measurement Problem Solving",
    "I can solve a variety of measurement, area, and perimeter problems.", "4.MD.1, 4.MD.2, 4.MD.3",
    [],
    "Design a garden: 20 feet of fence, the biggest area possible, and a 2-hour planting job starting at 9:45 a.m. What do you need?",
    [Example("Garden design", "20 ft of fence, biggest area.", ["Perimeter 20: try 5 × 5 = 25 sq ft (largest).", "Planting: 9:45 + 2 hr = 11:45 a.m."], "5 ft × 5 ft garden; done at 11:45 a.m."),
     KeyIdea("Use formulas, conversions, and elapsed time together.")],
    [Problem("Area of a 15 ft × 4 ft garden", "60 sq ft"), Problem("6 qt = ___ gal ___ qt", "1 gal 2 qt"), Problem("Start 1:50, end 4:05. Elapsed?", "2 hr 15 min")],
    [S("Warm-Up", [Problem("Perimeter of 7 × 3", "20"), Problem("Area of 7 × 3", "21")]),
     S("Mixed practice", [Problem("A = 63 sq m, l = 9 m. Find w.", "7 m"), Problem("P of a square with 13 in. sides", "52 in."), Problem("4 ft 9 in. = ___ in.", "57"),
                          Problem("3 kg = ___ g", "3,000"), Problem("7:35 a.m. + 2 hr 40 min", "10:15 a.m."), Problem("2 gal = ___ c", "32")]),
     S("Solve", [Problem("A rectangular pool is 25 m by 10 m. A rope goes around it. Tiles cover the bottom. How much rope? How many square meters of tile?", "70 m of rope; 250 sq m of tile", space=60, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Which measurement skill from this unit do you use most at home? Give an example.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students apply measurement skills in problem solving.", "4.MD.1–3 review.", "Workbook Lesson 9.16, Unit 9 Review",
       flow("Warm-up.", "Read Let's Explore.", ["Work the garden example."], "Try It 1–3.", "Workbook Lesson 9.16 and the Unit 9 Review.", "Check. Tomorrow: Unit 9 Test."), ["Mixing up area and perimeter."], ["Formula and conversion cards."], ["Measure and plan a real garden bed."]),
    summary="Combine formulas, conversions, and elapsed time to solve real problems.")

C1 = Check("Weekly Check 21: Area and Perimeter", [S("Show what you know", [Problem("Perimeter?", "26 cm", fig=R(9, 4, "cm"), space=0), Problem("Area?", "36 sq cm", fig=R(9, 4, "cm"), space=0),
    Problem("Square with 7 ft sides: perimeter and area", "28 ft; 49 sq ft"), Problem("Rectangle 12 m × 5 m: P and A", AP(12, 5, "m")),
    Problem("Perimeter 16: which has more area, 7 × 1 or 4 × 4?", "4 × 4"), Problem("Area or perimeter: fence around a yard?", "perimeter")])], minutes=15)
C2 = Check("Weekly Check 22: Area Problems", [S("Show what you know", [Problem("A = 54 sq ft, l = 9 ft. Find w.", "6 ft"), Problem("P = 28 cm, l = 9 cm. Find w.", "5 cm"),
    Problem("Area of the L-shape", "39 sq m (9 × 3 + 3 × 4)", fig=lambda t: l_shape(t, 9, 7, 3, 3, "m", width=CW, height=110), space=30),
    Problem("Carpet for 10 ft × 8 ft at $3 per sq ft", "$240"), Problem("Area or perimeter: paint for a wall?", "area"), Problem("Trim around all 4 sides of a 6 ft × 4 ft window", "20 ft")])], minutes=20)
C3 = Check("Weekly Check 23: Converting Units", [S("Convert", [Problem("6 ft = ___ in.", "72"), Problem("5 yd = ___ ft", "15"), Problem("3 lb = ___ oz", "48"), Problem("2 gal = ___ qt", "8"),
    Problem("4 m = ___ cm", "400"), Problem("3 L = ___ mL", "3,000"), Problem("2 hr 10 min = ___ min", "130"), Problem("3 weeks = ___ days", "21")])], minutes=15)

REVIEW = Check("Unit 9 Review", [
    S("Area and perimeter", [Problem("Rectangle 14 in. × 6 in.: P and A", AP(14, 6, "in.")), Problem("A = 80 sq ft, w = 8 ft. Find l.", "10 ft"),
                             Problem("Area of the L-shape", "44 sq ft (8 × 4 + 3 × 4)", fig=lambda t: l_shape(t, 8, 8, 3, 4, "ft", width=CW, height=110), space=30)]),
    S("Conversions and time", [Problem("7 ft = ___ in.", "84"), Problem("4 qt = ___ c", "16"), Problem("5 kg = ___ g", "5,000"), Problem("9:40 a.m. to 12:15 p.m.", "2 hr 35 min")]),
    S("Problem solving", [Problem(f"A dog walk is {F(3, 4)} mile, twice a day, for 7 days. How many miles in all?", MX(10, 2, 4) + " miles", space=40, wide=True)], cols=1)],
    kind="review", minutes=35, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 9 Test", [
    S("Part A · Area and perimeter (1 point each)", [Problem("Perimeter?", "34 ft", fig=R(11, 6, "ft"), space=0), Problem("Area?", "66 sq ft", fig=R(11, 6, "ft"), space=0),
        Problem("A = 42 sq cm, l = 7 cm. Find w.", "6 cm"), Problem("P = 30 m, l = 10 m. Find w.", "5 m"), Problem("Area or perimeter: grass for a lawn?", "area"),
        Problem("Area of the L-shape", "48 sq in. (10 × 3 + 3 × 6)", fig=lambda t: l_shape(t, 10, 9, 3, 3, "in.", width=CW, height=110), space=30)]),
    S("Part B · Conversions (1 point each)", [Problem("9 ft = ___ in.", "108"), Problem("4 yd = ___ ft", "12"), Problem("2 lb 3 oz = ___ oz", "35"), Problem("3 gal = ___ qt", "12"),
        Problem("6 m = ___ cm", "600"), Problem("2 kg = ___ g", "2,000"), Problem("4 hr = ___ min", "240"), Problem("1 min 15 sec = ___ sec", "75")]),
    S("Part C · Time (1 point each)", [Problem("10:35 a.m. to 1:10 p.m.", "2 hr 35 min"), Problem("Start 6:50 p.m., lasts 1 hr 45 min. End?", "8:35 p.m.")]),
    S("Part D · Problem solving (3 points each)", [
        Problem("A room is 12 ft by 11 ft. Carpet costs $5 per square foot. Baseboard costs $2 per foot. What is the total cost of carpet and baseboard?", "$752 ($660 carpet + $92 baseboard)", space=80, wide=True, points=3),
        Problem("Ellie needs 4 pieces of ribbon, each 1 ft 9 in. long. Ribbon comes in 2-yard rolls. Is one roll enough? Explain.", "No. 4 × 21 in. = 84 in., but 2 yd = 72 in., so one roll is not enough (12 in. short).", space=80, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["19–22 (85%+)", "Mastered."], ["16–18", "Proficient; correct missed items."], ["Below 16", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-05-24", "2027-05-31", "2027-06-07", "2027-06-14"], CHECKS, REVIEW, TEST)

UNIT = Unit(9, "Measurement, Area, and Perimeter", "Perimeter and area of rectangles, combined shapes, unit conversions, and elapsed time.",
    "Measurement connects math to everyday life. You will find perimeter and area, solve for unknown sides, convert units of length, weight, capacity, and time, and solve real problems with measurements.",
    ["Find perimeter and area with formulas.", "Find unknown side lengths.", "Find the area of combined rectangles.", "Convert customary, metric, and time units.", "Solve elapsed time and multi-step measurement problems."],
    [("4.MD.1", "Know relative sizes of measurement units within one system; express larger units in smaller units; record conversions in a table."),
     ("4.MD.2", "Use the four operations to solve word problems involving distances, intervals of time, liquid volumes, masses, and money, including fractions and decimals."),
     ("4.MD.3", "Apply the area and perimeter formulas for rectangles in real-world and mathematical problems.")],
    [("perimeter", "Distance around a figure."), ("area", "Square units that cover a surface."), ("convert", "Change to a different unit."), ("elapsed time", "Time that passes between start and end.")],
    ["Multiplication and division (Units 2–3).", "Fractions and decimals (Units 5–7)."], ["Ruler, yardstick, meter stick", "Measuring cups and containers", "Kitchen scale", "Clock", "Grid paper and square tiles"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Carpenters, cooks, gardeners, nurses, and pilots all measure and convert units every day.",
    family_note="Cook, build, and garden together this unit. Let your child do the measuring and converting.",
    weeks=WEEKS)
