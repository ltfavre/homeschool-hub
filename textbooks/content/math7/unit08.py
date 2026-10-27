"""Grade 7 Math · Unit 8: Scale Drawings and Geometric Figures (May 24 – Jun 18, 2027)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import F, RD, RF
from content.te import TE, flow
from content.sched import schedule

CW = 205


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def N(x):
    """Exact number: integer, terminating decimal, or mixed number."""
    x = Fr(x)
    if x.denominator == 1: return f"{x.numerator:,}"
    d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    return RD(float(x)) if d == 1 else RF(x)


def tri_ok(a, b, c):
    a, b, c = sorted((a, b, c)); return a + b > c


def scale_pts(pts, k): return [(x * k, y * k) for x, y in pts]


L_SHAPE = [(0, 0), (3, 0), (3, 2), (1, 2), (1, 4), (0, 4)]
ARROW = [(0, 1), (2, 1), (2, 0), (4, 2), (2, 4), (2, 3), (0, 3)]


def side(pts, i):
    (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % len(pts)]
    return abs(x2 - x1) + abs(y2 - y1)   # axis-aligned edges only


L1 = Lesson("8.1", "Scaled Copies",
    "I can tell whether one figure is a scaled copy of another.", "7.G.1",
    [("scaled copy", "A copy of a figure in which every length is multiplied by the same number."), ("corresponding parts", "Matching sides or angles in a figure and its copy.")],
    "Ellie draws a 3-by-4 rectangle, then a 6-by-8 rectangle and a 5-by-6 rectangle. Which one is a scaled copy?",
    [Text("In a <b>scaled copy</b>, every length is multiplied by the same number and every angle stays the same. Adding the same amount to each side does not make a scaled copy."),
     Figure(lambda t: Table([[grid_poly(t, L_SHAPE, 5, 5), grid_poly(t, scale_pts(L_SHAPE, 2), 9, 9), grid_poly(t, [(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)], 9, 9)],
                             [P("Original", t.small), P("Copy A: every length × 2", t.small), P("Copy B: not scaled", t.small)]], colWidths=[W / 3] * 3)),
     Example("Check the rectangles", "3 × 4 vs 6 × 8 and 5 × 6", ["6 ÷ 3 = 2 and 8 ÷ 4 = 2: same factor.", f"5 ÷ 3 = {F(5, 3)} but 6 ÷ 4 = {F(3, 2)}: different."], "6 × 8 is a scaled copy; 5 × 6 is not"),
     KeyIdea("Scaled copy: all lengths multiplied by the same factor, all angles unchanged.")],
    [Problem("Is a 4 × 10 rectangle a scaled copy of 2 × 5?", "Yes (× 2)"), Problem("Is a 5 × 7 rectangle a scaled copy of 3 × 5?", "No"), Problem("Is any square a scaled copy of any other square?", "Yes")],
    [S("Warm-Up", [Problem("6 ÷ 3", "2"), Problem("8 ÷ 4", "2")]),
     S("Scaled copy? Write yes or no.", [Problem(f"{a} × {b} and {c} × {d}", "Yes" if Fr(c, a) == Fr(d, b) else "No") for a, b, c, d in [(2, 3, 6, 9), (4, 6, 6, 8), (5, 10, 1, 2), (3, 7, 9, 14), (8, 12, 2, 3), (1, 4, 3, 7)]]),
     S("Draw a scaled copy of the L-shape with every length × 3.", [Problem("", "Sides 9, 6, 6, 6, 3, 12 (each original side × 3)", fig=lambda t: grid_poly(t, None, 22, 13, size=12), space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Lillie adds 2 to every side of a triangle. Is the new triangle a scaled copy? Explain.", "No; adding changes the ratios, so lengths are not multiplied by one factor.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students identify scaled copies.", "Solve problems involving scale drawings of geometric figures.", "Grid paper, workbook Lesson 8.1",
       flow("Division warm-up.", "Discuss Let's Explore.", ["Compare the L-shapes.", "Say: Multiply, don't add."], "Try It 1–3."),
       ["Thinking adding the same amount makes a scaled copy."], ["Compute side ratios."], ["Enlarge a favorite drawing on grid paper."]),
    summary="Scaled copies multiply every length by one factor; angles stay the same.")

L2 = Lesson("8.2", "Scale Factors",
    "I can find and use a scale factor.", "7.G.1",
    [("scale factor", "The number every length is multiplied by to make a scaled copy.")],
    "A photo 4 in. by 6 in. is enlarged so the short side is 10 in. How long is the long side?",
    [Example("Find the factor", "4 in. → 10 in.", [f"Scale factor = 10 ÷ 4 = {N(Fr(10, 4))}."], N(Fr(10, 4))),
     Example("Use the factor", f"Long side: 6 × {N(Fr(10, 4))}", [f"6 × {N(Fr(10, 4))} = {N(6 * Fr(10, 4))}."], f"{N(6 * Fr(10, 4))} in."),
     Text("A scale factor greater than 1 makes an <b>enlargement</b>. A scale factor between 0 and 1 makes a <b>reduction</b>. A scale factor of 1 makes a same-size copy."),
     KeyIdea("Scale factor = copy length ÷ original length.")],
    [Problem("Original 5 cm, copy 15 cm. Scale factor?", "3"), Problem("Original 12 ft, copy 3 ft. Scale factor?", F(1, 4)), Problem("Side 8 m, scale factor 0.75. Copy length?", "6 m")],
    [S("Warm-Up", [Problem("10 ÷ 4", "2.5"), Problem("6 × 2.5", "15")]),
     S("Find the scale factor", [Problem(f"{a} → {b}", N(Fr(b, a))) for a, b in [(3, 12), (10, 4), (6, 9), (20, 5), (8, 8), (4, 14)]]),
     S("Find the missing length", [Problem(f"Original {a} cm, scale factor {N(k)}", f"{N(a * k)} cm") for a, k in [(6, Fr(3)), (12, Fr(1, 3)), (9, Fr(5, 3)), (14, Fr(1, 2)), (10, Fr(3, 2)), (16, Fr(3, 4))]]),
     S("Exit Ticket", [Problem("A triangle has sides 6, 8, 10. A copy's shortest side is 9. Find the other two sides.", "12 and 15 (factor 1.5)", wide=True)], cols=1)],
    TE("Students find and apply scale factors.", "Compute lengths in scale drawings.", "Workbook Lesson 8.2",
       flow("Warm-up.", "Read Let's Explore.", ["Find the factor, then use it.", "Enlargement vs reduction."], "Try It 1–3."),
       ["Dividing original by copy."], ["Say: copy ÷ original."], ["Resize a photo on a computer and record the factor."]),
    summary="Scale factor = copy ÷ original; multiply each length by it.")

L3 = Lesson("8.3", "Scale Factors and Area",
    "I can find how area changes when a figure is scaled.", "7.G.1",
    [],
    "A 2-by-3 rectangle is scaled by a factor of 2. Does its area double?",
    [Figure(lambda t: Table([[grid_poly(t, [(0, 0), (3, 0), (3, 2), (0, 2)], 4, 3), grid_poly(t, [(0, 0), (6, 0), (6, 4), (0, 4)], 7, 5)],
                             [P("Area 6", t.small), P("Area 24", t.small)]], colWidths=[W / 2] * 2)),
     Text("No! The original area is 6 square units; the copy is 4 × 6 = 24 square units, which is 4 times as much. Length and width both doubled, so area is multiplied by 2 × 2."),
     Example("Factor 3", "Area 10 cm², scale factor 3", ["Area factor: 3² = 9.", "10 × 9 = 90."], "90 cm²"),
     Example("Reduction", f"Area 48 in², scale factor {F(1, 2)}", [f"Area factor: ({F(1, 2)})² = {F(1, 4)}.", f"48 × {F(1, 4)} = 12."], "12 in²"),
     KeyIdea("If lengths are multiplied by k, area is multiplied by k².")],
    [Problem("Area 5, scale factor 4. New area?", "80"), Problem(f"Area 36, scale factor {F(1, 3)}", "4"), Problem("Area changed from 7 to 63. Scale factor?", "3")],
    [S("Warm-Up", [Problem("2²", "4"), Problem(f"({F(1, 2)})²", F(1, 4))]),
     S("Find the new area", [Problem(f"Area {a}, scale factor {N(k)}", N(a * k * k)) for a, k in [(8, Fr(2)), (6, Fr(5)), (50, Fr(1, 5)), (12, Fr(3, 2)), (20, Fr(1, 2)), (3, Fr(10))]]),
     S("Solve", [Problem("A garden 4 m by 5 m is redesigned with every length × 1.5. Find the new area.", f"{N(4 * Fr(3, 2) * 5 * Fr(3, 2))} m²", space=24, wide=True),
                 Problem("A poster's area is 9 times a flyer's area. What is the scale factor?", "3", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Lillie says scaling by 3 triples the area. Explain her mistake.", "Area is multiplied by 3² = 9, not 3.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students relate scale factor to area.", "Compute actual areas from a scale drawing.", "Grid paper, workbook Lesson 8.3",
       flow("Square warm-up.", "Count squares in both rectangles.", ["Show k × k squares fit in each original square."], "Try It 1–3."),
       ["Multiplying area by k instead of k²."], ["Draw it and count."], ["Volume scales by k³: try with cubes."]),
    summary="Lengths × k means area × k².")

L4 = Lesson("8.4", "Scale Drawings",
    "I can use a scale to find actual lengths from a scale drawing.", "7.G.1",
    [("scale drawing", "A drawing that represents a real object with lengths in proportion."), ("scale", "A ratio that compares drawing length to actual length, such as 1 in. : 8 ft.")],
    "A floor plan uses the scale 1 in. : 8 ft. A bedroom measures 1.5 in. by 1.75 in. on the plan. How big is the real room?",
    [Example("Use the scale", "1.5 in. by 1.75 in.; 1 in. : 8 ft", ["1.5 × 8 = 12 ft.", "1.75 × 8 = 14 ft."], "12 ft by 14 ft"),
     Figure(lambda t: double_line(t, ["0", "1", "1.5", "1.75", "2"], ["0", "8", "12", "14", "16"], "Drawing (in.)", "Actual (ft)")),
     KeyIdea("Multiply drawing lengths by the scale's actual-per-unit value.")],
    [Problem("Scale 1 cm : 5 m. Drawing 7 cm. Actual?", "35 m"), Problem("Scale 1 in. : 20 mi. Drawing 3.5 in. Actual?", "70 mi"), Problem("Scale 2 cm : 1 m. Drawing 9 cm. Actual?", "4.5 m")],
    [S("Warm-Up", [Problem("1.5 × 8", "12"), Problem("1.75 × 8", "14")]),
     S("Find the actual length", [Problem(f"Scale {sc}; drawing {d}", a) for sc, d, a in [("1 in. : 6 ft", "4 in.", "24 ft"), ("1 cm : 3 m", "8.5 cm", "25.5 m"), ("1 in. : 50 mi", "2.25 in.", "112.5 mi"),
                                                                                          ("1 cm : 10 km", "6.3 cm", "63 km"), ("2 in. : 5 ft", "6 in.", "15 ft"), (f"{F(1, 4)} in. : 1 ft", "3 in.", "12 ft")]]),
     S("Exit Ticket", [Problem("A model car uses 1 in. : 2 ft. The model is 7 in. long. How long is the real car?", "14 ft", wide=True)], cols=1)],
    TE("Students use scales to find actual lengths.", "Solve problems involving scale drawings.", "Ruler, workbook Lesson 8.4",
       flow("Warm-up.", "Read Let's Explore.", ["Double number line for the scale."], "Try It 1–3. Weekly Check tomorrow."),
       ["Dividing instead of multiplying."], ["Double number line."], ["Find the scale on a real map or floor plan."]),
    summary="Drawing length × actual-per-unit = actual length.")

L5 = Lesson("8.5", "Finding Drawing Lengths",
    "I can find the length on a scale drawing for a given actual length.", "7.G.1",
    [],
    "A soccer field is 100 m long. Using 1 cm : 5 m, how long is it on the drawing?",
    [Example("Divide by the scale", "100 m with 1 cm : 5 m", ["100 ÷ 5 = 20."], "20 cm"),
     Example("Scale with a fraction", f"A 30-ft wall with {F(1, 2)} in. : 3 ft", [f"30 ÷ 3 = 10 groups of 3 ft.", f"10 × {F(1, 2)} in. = 5 in."], "5 in."),
     KeyIdea("To go from actual to drawing, divide by how much 1 drawing unit represents.")],
    [Problem("Scale 1 in. : 4 ft. Actual 22 ft. Drawing?", "5.5 in."), Problem("Scale 1 cm : 20 km. Actual 130 km. Drawing?", "6.5 cm"), Problem("Scale 2 cm : 3 m. Actual 12 m. Drawing?", "8 cm")],
    [S("Warm-Up", [Problem("100 ÷ 5", "20"), Problem(f"10 × {F(1, 2)}", "5")]),
     S("Find the drawing length", [Problem(f"Scale {sc}; actual {a}", d) for sc, a, d in [("1 in. : 10 ft", "45 ft", "4.5 in."), ("1 cm : 2 m", "15 m", "7.5 cm"), ("1 in. : 25 mi", "175 mi", "7 in."),
                                                                                        ("1 cm : 50 km", "325 km", "6.5 cm"), ("3 cm : 1 m", "4 m", "12 cm"), (f"{F(1, 4)} in. : 1 ft", "18 ft", "4.5 in.")]]),
     S("Plan a room", [Problem("Lillie's room is 12 ft by 10 ft. Draw it using the scale 1 square : 2 ft. What are the drawing dimensions?", "6 squares by 5 squares", fig=lambda t: grid_poly(t, None, 18, 10, size=12), space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("A 60-ft tree is drawn with 1 in. : 15 ft. How tall is the drawing?", "4 in.", wide=True)], cols=1)],
    TE("Students find drawing lengths from actual lengths.", "Solve problems involving scale drawings.", "Grid paper, ruler, workbook Lesson 8.5",
       flow("Warm-up.", "Read Let's Explore.", ["Divide by the scale value."], "Try It 1–3."),
       ["Multiplying instead of dividing."], ["Ask: should the drawing be smaller?"], ["Draw your room to scale."]),
    summary="Actual ÷ actual-per-unit = drawing length.")


L6 = Lesson("8.6", "Area in Scale Drawings",
    "I can find actual areas from scale drawings.", "7.G.1",
    [],
    "A park drawing is 4 cm by 6 cm with 1 cm : 50 m. What is the park's actual area?",
    [Example("Convert lengths first", "4 cm by 6 cm; 1 cm : 50 m", ["Actual: 4 × 50 = 200 m and 6 × 50 = 300 m.", "Area: 200 × 300 = 60,000 m²."], "60,000 m²"),
     Example("Area factor", "Same park", ["Drawing area: 24 cm².", "Each cm² represents 50 × 50 = 2,500 m².", "24 × 2,500 = 60,000."], "60,000 m²"),
     WatchOut("Do not multiply the drawing area by 50. Each square centimeter stands for 50 m × 50 m."),
     KeyIdea("Convert each length first, then compute the area. Or multiply drawing area by (scale)².")],
    [Problem("Drawing 3 in. × 5 in.; 1 in. : 4 ft. Actual area?", "240 ft²"), Problem("Drawing 2 cm × 2 cm; 1 cm : 10 m. Actual area?", "400 m²"), Problem("Drawing area 6 in²; 1 in. : 3 ft. Actual area?", "54 ft²")],
    [S("Warm-Up", [Problem("200 × 300", "60,000"), Problem("50 × 50", "2,500")]),
     S("Find the actual area", [Problem(f"Drawing {a} × {b} {u}; 1 {u} : {k} {U}", f"{N(a * k * b * k)} {U}²") for a, b, u, k, U in [(2, 3, "in.", 5, "ft"), (5, 8, "cm", 2, "m"), (Fr(3, 2), 4, "in.", 6, "ft"), (Fr(5, 2), Fr(7, 2), "cm", 10, "m")]]),
     S("Solve", [Problem("A rectangular rug on a plan (1 in. : 2 ft) measures 2.5 in. by 4 in. Carpet costs $3 per ft². Cost of the rug?", f"${N(Fr(5, 2) * 2 * 4 * 2 * 3)}", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("A plan uses 1 cm : 3 m. A room is 4 cm by 5 cm on the plan. Find the actual area.", "180 m²", wide=True)], cols=1)],
    TE("Students compute actual areas from scale drawings.", "Compute actual lengths and areas from a scale drawing.", "Workbook Lesson 8.6",
       flow("Warm-up.", "Read Let's Explore.", ["Two methods."], "Try It 1–3."),
       ["Multiplying area by the scale once."], ["Convert lengths first."], ["Estimate the cost of flooring for a room at home."]),
    summary="Convert lengths first, or multiply the drawing area by the scale squared.")

L7 = Lesson("8.7", "Maps and Scale",
    "I can use a map scale to find real distances and travel times.", "7.G.1, 7.RP.2",
    [],
    "On a map with scale 1 cm : 25 km, two cities are 7.2 cm apart. How far apart are they? How long would a 90 km/h drive take?",
    [Example("Distance", "7.2 cm; 1 cm : 25 km", ["7.2 × 25 = 180."], "180 km"),
     Example("Time", "180 km at 90 km/h", ["180 ÷ 90 = 2."], "2 hours"),
     Example("Scale without units", "Scale 1 : 50,000. Map distance 6 cm.", ["Actual = 6 × 50,000 = 300,000 cm.", "300,000 cm = 3,000 m = 3 km."], "3 km"),
     KeyIdea("A scale like 1 : 50,000 has no units: 1 of any unit on the map is 50,000 of the same unit in real life.")],
    [Problem("Map 1 in. : 30 mi. Distance 4.5 in.?", "135 mi"), Problem("Scale 1 : 100,000. Map 4 cm. Actual km?", "4 km"), Problem("150 mi at 60 mph: hours?", "2.5 hours")],
    [S("Warm-Up", [Problem("7.2 × 25", "180"), Problem("300,000 cm in km", "3 km")]),
     S("Find the actual distance", [Problem(f"Scale {sc}; map {m}", a) for sc, m, a in [("1 cm : 40 km", "3.5 cm", "140 km"), ("1 in. : 15 mi", "6 in.", "90 mi"), ("1 : 25,000", "8 cm", "2 km"), ("1 : 200,000", "5 cm", "10 km")]]),
     S("Solve", [Problem("On a map (1 in. : 50 mi), Ellie's trip is 4.8 in. She drives 60 mph. How long is the drive?", "240 mi; 4 hours", space=30, wide=True),
                 Problem("A hiking map is 1 : 24,000. A trail is 15 cm on the map. How many kilometers is it?", "3.6 km", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Two towns are 75 km apart. With 1 cm : 15 km, how far apart on the map?", "5 cm", wide=True)], cols=1)],
    TE("Students use map scales.", "Solve problems involving scale drawings; use proportional reasoning.", "A real road map (optional), workbook Lesson 8.7",
       flow("Warm-up.", "Read Let's Explore.", ["Distance, then time.", "Unitless scales."], "Try It 1–3."),
       ["Forgetting to convert cm to km."], ["Write the unit at every step."], ["Plan a trip using a real map."]),
    summary="Multiply map distance by the scale; convert units if needed.")

L8 = Lesson("8.8", "Changing the Scale",
    "I can reproduce a scale drawing at a different scale.", "7.G.1",
    [],
    "A garden plan uses 1 cm : 2 m and is 10 cm by 6 cm. Redraw it at 1 cm : 4 m. What size is the new drawing?",
    [Example("Find actual, then redraw", "10 cm × 6 cm at 1 cm : 2 m", ["Actual: 20 m by 12 m.", "New drawing at 1 cm : 4 m: 20 ÷ 4 = 5 cm; 12 ÷ 4 = 3 cm."], "5 cm by 3 cm"),
     Example("Compare scales", "1 cm : 2 m vs 1 cm : 4 m", ["Each cm now stands for twice as much.", f"So the new drawing is {F(1, 2)} the size."], f"drawing lengths × {F(1, 2)}"),
     KeyIdea("Find actual lengths first, then convert to the new scale.")],
    [Problem("Plan 8 in. at 1 in. : 5 ft; redraw at 1 in. : 10 ft", "4 in."), Problem("Plan 3 cm at 1 cm : 6 m; redraw at 1 cm : 2 m", "9 cm"), Problem("Plan 12 cm at 1 cm : 1 m; redraw at 1 cm : 3 m", "4 cm")],
    [S("Warm-Up", [Problem("10 × 2", "20"), Problem("20 ÷ 4", "5")]),
     S("Redraw at the new scale", [Problem(f"{d} at {s1}; new scale {s2}", a) for d, s1, s2, a in [("6 in.", "1 in. : 4 ft", "1 in. : 8 ft", "3 in."), ("5 cm", "1 cm : 10 m", "1 cm : 5 m", "10 cm"),
                                                                                                ("9 in.", "1 in. : 2 ft", "1 in. : 3 ft", "6 in."), ("4 cm", "1 cm : 3 m", "1 cm : 2 m", "6 cm")]]),
     S("Exit Ticket", [Problem("A rectangle 8 cm × 4 cm uses 1 cm : 3 m. Redraw it at 1 cm : 6 m on the grid (1 square = 1 cm).", "4 squares by 2 squares", fig=lambda t: grid_poly(t, None, 12, 6, size=12), space=0, wide=True)], cols=1)],
    TE("Students redraw at a different scale.", "Reproduce a scale drawing at a different scale.", "Grid paper, workbook Lesson 8.8",
       flow("Warm-up.", "Read Let's Explore.", ["Actual first, then redraw."], "Try It 1–3. Weekly Check tomorrow."),
       ["Scaling the wrong direction."], ["Ask: does each cm represent more or less now?"], ["Redraw a floor plan for a smaller sheet of paper."]),
    summary="Find actual lengths, then convert to the new scale.")


TRIS = [(3, 4, 5), (2, 3, 6), (5, 5, 10), (4, 7, 9), (1, 1, 1), (6, 2, 3)]
L9 = Lesson("8.9", "Triangle Side Lengths",
    "I can decide whether three side lengths can form a triangle.", "7.G.2",
    [("Triangle Inequality", "The sum of any two side lengths of a triangle is greater than the third side.")],
    "Can you make a triangle with straws 2 in., 3 in., and 6 in. long?",
    [Text("No! The two short straws together reach only 5 in., which is shorter than 6 in. They can't meet."),
     Figure(lambda t: Table([[polygon_fig(t, [(0, 0), (1, 0), (0.25, 0.9)], width=150, height=100, edge_labels=["5", "4", "3"]),
                              Draw(180, 100, lambda c, w, h: (c.setStrokeColor(t.dark), c.setLineWidth(2), c.line(10, 20, 170, 20), c.line(10, 20, 40, 60), c.line(170, 20, 120, 75),
                                                              text(c, 90, 6, "6", "Mono", 8.5, INK, "c"), text(c, 16, 44, "2", "Mono", 8.5, INK, "c"), text(c, 152, 52, "3", "Mono", 8.5, INK, "c")))],
                             [P("3, 4, 5: forms a triangle", t.small), P("2, 3, 6: the sides can't meet", t.small)]], colWidths=[W / 2] * 2)),
     Example("Test", "4, 7, 9", ["Shortest two: 4 + 7 = 11.", "11 > 9 ✓."], "Yes, a triangle"),
     Example("Test", "5, 5, 10", ["5 + 5 = 10, not greater than 10."], "No triangle (it lies flat)"),
     KeyIdea("Check only the two shortest sides: their sum must be greater than the longest side.")],
    [Problem("3, 3, 5", "Yes" if tri_ok(3, 3, 5) else "No"), Problem("1, 2, 4", "Yes" if tri_ok(1, 2, 4) else "No"), Problem("8, 8, 8", "Yes" if tri_ok(8, 8, 8) else "No")],
    [S("Warm-Up", [Problem("2 + 3", "5"), Problem("Is 5 > 6?", "No")]),
     S("Triangle? Write yes or no.", [Problem(f"{a}, {b}, {c}", "Yes" if tri_ok(a, b, c) else "No") for a, b, c in [(5, 6, 7), (2, 2, 5), (10, 4, 7), (3, 9, 6), (12, 5, 13), (1.5, 2.5, 3.5)]]),
     S("Find the range", [Problem("Two sides are 5 cm and 8 cm. What lengths could the third side be?", "between 3 cm and 13 cm", space=24, wide=True),
                          Problem("Two sides are 10 in. and 4 in. Can the third side be 6 in.? 7 in.?", "6: no; 7: yes", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Explain why 4, 5, 10 cannot form a triangle.", "4 + 5 = 9, which is less than 10.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students apply the triangle inequality.", "Draw geometric shapes with given conditions; notice when conditions determine a unique triangle, more than one, or none.", "Straws or strips of paper, ruler, scissors, workbook Lesson 8.9",
       flow("Warm-up.", "Build triangles from straws (cut to 2, 3, 6 and 3, 4, 5 in.).", ["State the rule."], "Try It 1–3."),
       ["Checking only one pair of sides."], ["Sort the lengths first."], ["Find all whole-number triangles with perimeter 12."]),
    summary="The two shorter sides must add to more than the longest side.")

L10 = Lesson("8.10", "Triangle Angles",
    "I can use the angle sum of a triangle to decide whether angles can form a triangle.", "7.G.2",
    [("angle sum", "The angles in any triangle add up to 180°.")],
    "Can a triangle have angles of 90°, 60°, and 40°?",
    [Text("Tear the three corners off any paper triangle and line them up: they always form a straight angle, 180°."),
     Example("Check", "90°, 60°, 40°", ["90 + 60 + 40 = 190 ≠ 180."], "No triangle"),
     Example("Missing angle", "Two angles are 48° and 75°", ["180 − 48 − 75 = 57."], "57°"),
     Example("How many triangles?", "Angles 50°, 60°, 70°", ["They sum to 180°.", "Triangles of many sizes have these angles (scaled copies)."], "Many triangles"),
     KeyIdea("Angles alone can't fix a triangle's size: three angles that sum to 180° give infinitely many triangles.")],
    [Problem("30°, 60°, 90°: triangle?", "Yes"), Problem("Two angles 110° and 80°: triangle?", "No (190° already)"), Problem("Missing angle: 35°, 35°, ?", "110°")],
    [S("Warm-Up", [Problem("180 − 48 − 75", "57"), Problem("90 + 60 + 40", "190")]),
     S("Find the missing angle", [Problem(f"{a}° and {b}°", f"{180 - a - b}°") for a, b in [(60, 60), (90, 25), (120, 35), (45, 45), (100, 47), (15, 82)]]),
     S("Can these be the angles of a triangle?", [Problem(f"{a}°, {b}°, {c}°", "Yes" if a + b + c == 180 else "No") for a, b, c in [(70, 70, 40), (90, 90, 10), (100, 40, 50), (33, 57, 90)]]),
     S("Exit Ticket", [Problem("A right triangle has one 38° angle. Find the third angle.", "52°", wide=True)], cols=1)],
    TE("Students use the triangle angle sum.", "Notice when conditions determine one triangle, more than one, or none.", "Paper triangles, scissors, workbook Lesson 8.10",
       flow("Warm-up.", "Tear corners off a triangle.", ["Missing-angle examples; AAA gives many triangles."], "Try It 1–3."),
       ["Forgetting the right angle is 90°."], ["Label all three angles."], ["Can a triangle have two obtuse angles? Why not?"]),
    summary="Triangle angles sum to 180°; angles alone don't fix the size.")

L11 = Lesson("8.11", "Drawing Triangles from Conditions",
    "I can draw triangles with a ruler and protractor and tell whether the conditions give one, many, or no triangles.", "7.G.2",
    [("unique", "Exactly one; any triangle drawn with those conditions is the same shape and size.")],
    "Draw a triangle with sides 5 cm and 7 cm and a 40° angle between them. Will your triangle match a classmate's?",
    [Text("Yes. When two sides and the angle between them are given, there is only one possible third side, so the triangle is <b>unique</b>."),
     Figure(lambda t: table(t, [["Given", "Example", "How many triangles?"], ["3 sides (that pass the inequality)", "5, 6, 7 cm", "one"], ["2 sides + angle between them", "5 cm, 40°, 7 cm", "one"],
                                ["2 angles + side between them", "50°, 6 cm, 60°", "one"], ["3 angles that sum to 180°", "50°, 60°, 70°", "many"], ["Conditions that break a rule", "2, 3, 6 cm; or 100°, 90°", "none"]],
                            [2.4 * inch, 1.7 * inch, 1.4 * inch], width=5.5 * inch)),
     Example("Steps to draw SAS", "5 cm, 40°, 7 cm", ["Draw a 7 cm segment.", "At one end, measure 40° with a protractor and draw a ray.", "Mark 5 cm on the ray.", "Connect the endpoints."], "one triangle"),
     KeyIdea("SSS, SAS, and ASA give one triangle. AAA gives many. Broken rules give none.")],
    [Problem("Sides 4, 4, 4 cm", "one"), Problem("Angles 45°, 45°, 90°", "many"), Problem("Angles 100°, 100°, ?", "none")],
    [S("Warm-Up", [Problem("Is 5 + 6 > 7?", "Yes"), Problem("50 + 60 + 70", "180")]),
     S("One, many, or none?", [Problem(g, a) for g, a in [("sides 3, 4, 8 cm", "none"), ("sides 6, 8, 10 cm", "one"), ("angles 30°, 60°, 90°", "many"), ("sides 5 and 9 cm with a 70° angle between", "one"),
                                                          ("angles 40° and 80° with a 6 cm side between", "one"), ("angles 95°, 95°, ?", "none")]]),
     S("Draw it", [Problem("Use a ruler and protractor to draw a triangle with sides 6 cm and 4 cm and a 60° angle between them. Measure the third side.", "about 5.3 cm", space=110, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Why do three angles not give a unique triangle?", "Scaled copies have the same angles but different sizes.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students draw triangles from conditions.", "Draw triangles from three measures of angles or sides; notice when conditions determine a unique triangle.", "Ruler, protractor, workbook Lesson 8.11",
       flow("Warm-up.", "Draw the SAS triangle; compare.", ["Teach the table.", "Model drawing ASA."], "Try It 1–3."),
       ["Measuring the angle from the wrong scale on the protractor."], ["Start from 0 on the baseline."], ["Explore SSA: two sides and a non-included angle can give two triangles!"]),
    summary="SSS, SAS, ASA → one triangle; AAA → many; broken rules → none.")

_s = (95 ** 2 - 80 ** 2) ** 0.5   # rhombus: side 95 px, height 80 px
RHOMBUS = [(0, 0), (95 / (95 + _s), 0), (1, 1), (_s / (95 + _s), 1)]
L12 = Lesson("8.12", "Drawing Quadrilaterals with Conditions",
    "I can draw quadrilaterals with given conditions and decide whether they are unique.", "7.G.2",
    [],
    "Draw a quadrilateral with all sides 4 cm. Is there only one?",
    [Text("No: a square works, but so does any rhombus with 4 cm sides. Push a square's corner and it leans into a rhombus. Quadrilaterals need more conditions than triangles to be unique."),
     Figure(lambda t: Table([[polygon_fig(t, [(0, 0), (1, 0), (1, 1), (0, 1)], width=100, height=100, right_angles=[0, 1, 2, 3], ticks=[(0, 1), (1, 1), (2, 1), (3, 1)]),
                              polygon_fig(t, RHOMBUS, width=166, height=100, ticks=[(0, 1), (1, 1), (2, 1), (3, 1)])],
                             [P("square", t.small), P("rhombus", t.small)]], colWidths=[W / 2] * 2)),
     Example("Unique?", "A rectangle 5 cm by 3 cm", ["Right angles fix the shape; lengths fix the size."], "one rectangle"),
     KeyIdea("Side lengths alone don't fix a quadrilateral. Angles help.")],
    [Problem("Rectangle with sides 6 and 2: how many?", "one"), Problem("Parallelogram with sides 6 and 2: how many?", "many"), Problem("Square with sides 3 cm: how many?", "one")],
    [S("Warm-Up", [Problem("Angles in a rectangle", "four 90°"), Problem("Angle sum of a quadrilateral", "360°")]),
     S("One or many?", [Problem(g, a) for g, a in [("square, side 5 cm", "one"), ("rhombus, side 5 cm", "many"), ("rectangle, 4 cm by 7 cm", "one"), ("quadrilateral with sides 3, 4, 5, 6 cm", "many")]]),
     S("Draw it", [Problem("Draw a parallelogram with sides 5 cm and 3 cm and a 60° angle. Is it unique?", "Yes; the angle fixes the shape", space=110, wide=True)], cols=1),
     S("Exit Ticket", [Problem("A quadrilateral has angles 90°, 90°, 90°, and ? Find the fourth angle.", "90°", wide=True)], cols=1)],
    TE("Students draw quadrilaterals with conditions.", "Draw geometric shapes with given conditions.", "Ruler, protractor, straws and pipe cleaners (optional), workbook Lesson 8.12",
       flow("Warm-up.", "Push a straw square into a rhombus.", ["Work examples."], "Try It 1–3. Weekly Check tomorrow."),
       ["Thinking 4 equal sides means a square."], ["Build with straws."], ["Which conditions make a kite unique?"]),
    summary="Quadrilaterals need angle conditions to be unique.")

def SF(kind, cut, w=96): return lambda t: solid_fig(t, kind, cut, width=w, height=w)

L13 = Lesson("8.13", "Cross Sections of Prisms",
    "I can describe the cross sections made by slicing a rectangular prism.", "7.G.3",
    [("cross section", "The two-dimensional shape made when a plane slices through a solid."), ("plane", "A flat surface that extends forever.")],
    "Slice a block of cheese straight across, parallel to the bottom. What shape is the cut face?",
    [Figure(lambda t: Table([[solid_fig(t, "prism", "h", 130, 120), solid_fig(t, "prism", "v", 130, 120)],
                             [P("Parallel to the base: a rectangle the same size as the base", t.small), P("Perpendicular to the base: a rectangle", t.small)]], colWidths=[W / 2] * 2)),
     Example("Slice a cube", "Cube, slice parallel to a face", ["The cut matches the face."], "a square"),
     Example("Slanted slice", "Cube, slice through one corner", ["Cutting off one corner makes three cut edges."], "a triangle"),
     KeyIdea("Slices of a rectangular prism parallel or perpendicular to the base are rectangles. Slanted slices can make triangles and other polygons.")],
    [Problem("Slice of a 4 × 6 × 10 box parallel to the 4 × 6 base", "4 × 6 rectangle"), Problem("Vertical slice of a cube", "square"), Problem("Slice cutting off one corner of a cube", "triangle")],
    [S("Warm-Up", [Problem("How many faces does a cube have?", "6"), Problem("Shape of each face of a cube", "square")]),
     S("Name the cross section", [Problem(g, a) for g, a in [("A box 3 × 5 × 8, sliced parallel to the 3 × 5 face", "3 × 5 rectangle"), ("A cube sliced diagonally from one top edge to the opposite bottom edge", "rectangle"),
                                                            ("A loaf of bread sliced like usual", "rectangle (the loaf's end shape)"), ("A triangular prism sliced parallel to its triangle base", "triangle")]], cols=1),
     S("Exit Ticket", [Problem("Can a slice of a cube be a pentagon? Try to sketch one.", "Yes, a slanted plane through 5 faces", lines=2, space=40, wide=True)], cols=1)],
    TE("Students describe prism cross sections.", "Describe the two-dimensional figures that result from slicing three-dimensional figures.", "Clay or a block of cheese and a plastic knife (optional), workbook Lesson 8.13",
       flow("Warm-up.", "Slice a clay block.", ["Parallel vs perpendicular slices."], "Try It 1–3."),
       ["Naming a 3-D shape instead of the 2-D face."], ["Look at the cut face only."], ["Find a hexagonal slice of a cube."]),
    summary="Prism slices parallel or perpendicular to the base are rectangles (or the base shape).")

L14 = Lesson("8.14", "Cross Sections of Pyramids",
    "I can describe the cross sections made by slicing a pyramid.", "7.G.3",
    [],
    "Slice a square pyramid parallel to its base. What shape is the cut? What if you slice straight down through the top?",
    [Figure(lambda t: Table([[solid_fig(t, "pyramid", "h", 130, 130), solid_fig(t, "pyramid", "v", 130, 130)],
                             [P("Parallel to the base: a smaller square", t.small), P("Perpendicular through the top: a triangle", t.small)]], colWidths=[W / 2] * 2)),
     Example("Size changes", "Slice parallel to the base, halfway up", ["Each side of the cut is half the base side."], "a square half as wide"),
     KeyIdea("Parallel slices of a pyramid have the base's shape but get smaller toward the top. Vertical slices through the top are triangles.")],
    [Problem("Square pyramid, horizontal slice", "square"), Problem("Triangular pyramid, slice parallel to base", "triangle"), Problem("Square pyramid, vertical slice not through the top", "trapezoid")],
    [S("Warm-Up", [Problem("Shape of a square pyramid's base", "square"), Problem("Shape of its side faces", "triangles")]),
     S("Name the cross section", [Problem(g, a) for g, a in [("Square pyramid, slice parallel to the base near the top", "small square"), ("Square pyramid, vertical slice through the apex", "triangle"),
                                                            ("Rectangular pyramid, horizontal slice", "rectangle"), ("Triangular pyramid, horizontal slice", "triangle")]], cols=1),
     S("Exit Ticket", [Problem("A square pyramid's base is 10 in. on a side. A slice halfway up and parallel to the base: what shape and size?", "a 5 in. by 5 in. square", wide=True)], cols=1)],
    TE("Students describe pyramid cross sections.", "Describe plane sections of right rectangular pyramids.", "Clay pyramid (optional), workbook Lesson 8.14",
       flow("Warm-up.", "Slice a clay pyramid.", ["Horizontal vs vertical."], "Try It 1–3."),
       ["Thinking the slice is the same size as the base."], ["Compare with the base."], ["Sketch slices at 1/4 and 3/4 height."]),
    summary="Horizontal slices: base shape, smaller; vertical slices through the apex: triangles.")

L15 = Lesson("8.15", "Cross Sections of Cylinders and Cones",
    "I can describe the cross sections of cylinders and cones.", "7.G.3",
    [],
    "What shape do you see when you cut a can straight across? Straight down the middle?",
    [Figure(lambda t: Table([[solid_fig(t, "cylinder", "h", 105, 120), solid_fig(t, "cylinder", "v", 105, 120), solid_fig(t, "cone", "h", 105, 120), solid_fig(t, "cone", "v", 105, 120)],
                             [P("circle", t.small), P("rectangle", t.small), P("smaller circle", t.small), P("triangle", t.small)]], colWidths=[W / 4] * 4)),
     KeyIdea("Horizontal slices of cylinders and cones are circles. Vertical slices through the center are rectangles (cylinder) or triangles (cone).")],
    [Problem("Slice of a cylinder parallel to the base", "circle"), Problem("Vertical slice of a cone through its tip", "triangle"), Problem("Vertical slice of a cylinder through its center", "rectangle")],
    [S("Warm-Up", [Problem("Shape of a cylinder's bases", "circles"), Problem("Shape of a cone's base", "circle")]),
     S("Name the cross section", [Problem(g, a) for g, a in [("Cylinder, horizontal", "circle"), ("Cylinder, vertical through center", "rectangle"), ("Cone, horizontal", "circle"), ("Cone, vertical through tip", "triangle"),
                                                            ("Cylinder (r = 3, h = 10), vertical through center: dimensions", "6 × 10 rectangle"), ("Sphere, any slice", "circle")]]),
     S("Exit Ticket", [Problem("A cylinder has diameter 4 in. and height 9 in. Describe its vertical cross section through the center.", "a rectangle 4 in. by 9 in.", wide=True)], cols=1)],
    TE("Students describe cross sections of round solids.", "Describe the two-dimensional figures that result from slicing three-dimensional figures.", "Clay, a can, an ice-cream cone (optional), workbook Lesson 8.15",
       flow("Warm-up.", "Slice clay cylinders and cones.", ["Name each cut."], "Try It 1–3."),
       ["Calling a circle a sphere."], ["The cut face is flat."], ["What slice of a cylinder makes an oval?"]),
    summary="Round solids: horizontal slices are circles; vertical slices are rectangles or triangles.")

L16 = Lesson("8.16", "Scale Drawing Project",
    "I can create a scale drawing of a real space and use it to solve problems.", "7.G.1",
    [],
    "Design a scale floor plan of your bedroom or kitchen.",
    [Text("Measure the room and its furniture. Choose a scale that fits your paper (for example, 1 in. : 2 ft or 1 cm : 50 cm). Draw the room and furniture to scale, and label each length."),
     Example("Sample", "A room 14 ft by 12 ft on 8.5 × 11 in. paper", ["1 in. : 2 ft gives 7 in. by 6 in.: fits!", "A 6 ft bed becomes 3 in."], "Scale 1 in. : 2 ft"),
     Figure(lambda t: table(t, [["Object", "Actual size", "Drawing size (1 in. : 2 ft)"], ["Room", "14 ft × 12 ft", "7 in. × 6 in."], ["Bed", "6 ft × 3.5 ft", "3 in. × 1.75 in."], ["Desk", "4 ft × 2 ft", "2 in. × 1 in."]],
                            [1.3 * inch, 1.7 * inch, 2.4 * inch], width=5.4 * inch)),
     KeyIdea("Choose a scale so the biggest length fits your paper.")],
    [Problem("Rug 5 ft × 8 ft at 1 in. : 2 ft", "2.5 in. × 4 in."), Problem("Window 3 ft wide at 1 in. : 2 ft", "1.5 in."), Problem("Area of the room above", "168 ft²")],
    [S("Warm-Up", [Problem("14 ÷ 2", "7"), Problem("14 × 12", "168")]),
     S("Project", [Problem("Measure your room. Length and width:", "Answers vary.", lines=1, space=0, wide=True), Problem("Choose a scale:", "Answers vary.", lines=1, space=0, wide=True),
                   Problem("Draw your room and at least three objects on the grid.", "Drawing", fig=lambda t: grid_poly(t, None, 34, 20, size=12.5), space=0, wide=True),
                   Problem("Find the floor area of your room.", "Answers vary.", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Why did you choose your scale?", "Answers vary: the room fits the paper.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students create a scale drawing of a real room.", "Solve problems involving scale drawings; reproduce a drawing at a scale.", "Tape measure, ruler, grid paper, workbook Lesson 8.16, Unit 8 Review",
       flow("Warm-up.", "Measure the room together.", ["Choose a scale; draw."], "Project parts 1–4.", "Workbook Lesson 8.16 and the Unit 8 Review.", "Present the drawing. Tomorrow: Unit 8 Test."),
       ["Choosing a scale that doesn't fit."], ["Check the largest length first."], ["Redesign the room layout with cut-out furniture."]),
    summary="Measure, pick a scale that fits, draw, and label.")


C1 = Check("Weekly Check 22: Scale Factors", [S("Show what you know", [
    Problem("Is 6 × 15 a scaled copy of 2 × 5?", "Yes"), Problem("Original 8 cm, copy 20 cm. Scale factor?", "2.5"), Problem(f"Side 12 in., scale factor {F(2, 3)}", "8 in."),
    Problem("Area 7, scale factor 3. New area?", "63"), Problem("Scale 1 in. : 5 ft; drawing 6.4 in. Actual?", "32 ft"), Problem("Scale 1 cm : 4 m; drawing 3.5 cm. Actual?", "14 m")])], minutes=15)
C2 = Check("Weekly Check 23: Scale Drawings and Maps", [S("Show what you know", [
    Problem("Scale 1 in. : 8 ft; actual 36 ft. Drawing?", "4.5 in."), Problem("Drawing 3 cm × 4 cm; 1 cm : 5 m. Actual area?", "300 m²"), Problem("Map 1 cm : 30 km; 4.5 cm. Actual?", "135 km"),
    Problem("Scale 1 : 50,000; map 4 cm. Actual km?", "2 km"), Problem("Drawing 10 cm at 1 cm : 2 m. Redraw at 1 cm : 5 m.", "4 cm"), Problem("180 mi at 45 mph: hours?", "4 hours")])], minutes=15)
C3 = Check("Weekly Check 24: Triangles and Quadrilaterals", [S("Show what you know", [
    Problem("Triangle? 4, 6, 11", "No"), Problem("Triangle? 7, 8, 12", "Yes"), Problem("Missing angle: 64° and 71°", "45°"),
    Problem("Angles 50°, 60°, 70°: one, many, or none?", "many"), Problem("Sides 5 cm, 7 cm with 45° between: one, many, or none?", "one"), Problem("Rhombus with side 4 cm: one or many?", "many")])], minutes=15)

REVIEW = Check("Unit 8 Review", [
    S("Scale", [Problem("Scale factor from 15 to 6", "0.4"), Problem("Area 20, scale factor 1.5", "45"), Problem("Plan 1 in. : 3 ft; room 5 in. × 4.5 in. Actual size?", "15 ft × 13.5 ft"),
                Problem("Same room: actual area?", f"{N(15 * Fr(27, 2))} ft²"), Problem("Map 1 : 100,000; 7.5 cm. Actual km?", "7.5 km"), Problem("Redraw 9 cm at 1 cm : 4 m using 1 cm : 6 m", "6 cm")]),
    S("Geometry", [Problem("Two sides 6 and 9: possible third sides", "between 3 and 15"), Problem("Missing angle: 90° and 27°", "63°"), Problem("ASA: one, many, or none?", "one"),
                   Problem("Cross section of a cylinder, horizontal", "circle"), Problem("Cross section of a square pyramid through the apex, vertical", "triangle"), Problem("Cross section of a 2 × 3 × 7 box parallel to the 2 × 3 face", "2 × 3 rectangle")])],
    kind="review", minutes=40, teacher_note="Homework or a study session before the test.")

TEST = Check("Unit 8 Test", [
    S("Part A · Scale (1 point each)", [Problem("Is 9 × 12 a scaled copy of 3 × 4?", "Yes"), Problem("Scale factor from 10 to 25", "2.5"), Problem(f"Side 18 cm, scale factor {F(1, 3)}", "6 cm"),
        Problem("Area 12, scale factor 2", "48"), Problem("Scale 1 in. : 6 ft; drawing 4.5 in. Actual?", "27 ft"), Problem("Scale 1 cm : 25 km; actual 200 km. Drawing?", "8 cm")]),
    S("Part B · Triangles and figures (1 point each)", [Problem("Triangle? 3, 5, 9", "No"), Problem("Missing angle: 38° and 106°", "36°"), Problem("Sides 6, 8, 10: one, many, or none?", "one"),
        Problem("Angles 45°, 45°, 90°: one, many, or none?", "many"), Problem("Cone, horizontal slice", "circle"), Problem("Cube, slice parallel to a face", "square")]),
    S("Part C · Problem solving (3 points each)", [
        Problem("A floor plan uses 1 in. : 4 ft. A living room is 5 in. by 3.5 in. on the plan. Find the actual dimensions and area. Carpet costs $2.50 per square foot: how much to carpet the room?",
                f"20 ft × 14 ft; 280 ft²; ${N(280 * Fr(5, 2))}", space=70, wide=True, points=3),
        Problem("A map uses 1 cm : 20 km. Two towns are 9 cm apart. Ellie drives 60 km/h. How long is the drive? Show your work.", "180 km; 3 hours", space=60, wide=True, points=3),
        Problem("Use a ruler and protractor to draw a triangle with a 6 cm side between angles of 50° and 70°. Find the third angle. Is the triangle unique?", "60°; yes (ASA)", space=100, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, rubric=[["18–21 (85%+)", "Mastered."], ["15–17", "Proficient; correct missed items."], ["Below 15", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-05-24", "2027-05-31", "2027-06-07", "2027-06-14"], CHECKS, REVIEW, TEST)

UNIT = Unit(8, "Scale Drawings and Geometric Figures", "Scaled copies, scale drawings and maps, drawing triangles from conditions, and cross sections.",
    "Architects, mapmakers, and game designers all work with scale. In this unit you will make and use scale drawings and maps, discover which measurements determine a triangle, and imagine slicing solids to see what shapes appear.",
    ["Find and use scale factors, including their effect on area.", "Use scales to find actual lengths, areas, and distances.", "Redraw scale drawings at a new scale.", "Decide when conditions give one, many, or no triangles.", "Describe cross sections of prisms, pyramids, cylinders, and cones."],
    [("7.G.1", "Solve problems involving scale drawings, including computing actual lengths and areas and reproducing a drawing at a different scale."),
     ("7.G.2", "Draw geometric shapes with given conditions; focus on triangles from three measures of angles or sides."), ("7.G.3", "Describe the two-dimensional figures that result from slicing three-dimensional figures.")],
    [("scale factor", "Multiplier for every length."), ("scale", "Drawing length : actual length."), ("triangle inequality", "Two sides sum to more than the third."), ("cross section", "The shape of a slice.")],
    ["Ratios and proportional relationships (Unit 1).", "Angles and the protractor (Grade 4 and 5)."], ["Ruler, protractor, grid paper", "Straws, clay, plastic knife", "Tape measure"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Blueprints, road maps, model trains, and CT scans (which are cross sections of the body!) all use the ideas in this unit.",
    family_note="Look at a road map or a floor plan together and ask your student to find a real distance using the scale.",
    weeks=WEEKS)
