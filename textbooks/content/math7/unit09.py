"""Grade 7 Math · Unit 9: Angles, Circles, Area, Surface Area, and Volume + Year Review (Jun 21 – Jul 16, 2027)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import F, RD, RF
from content.te import TE, flow
from content.sched import schedule

CW = 205
PI = Fr("3.14")


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def N(x):
    """Exact number: integer (with commas), terminating decimal, or mixed number."""
    x = Fr(x)
    if x.denominator == 1: return f"{x.numerator:,}"
    d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    return RD(float(x)) if d == 1 else RF(x)


def circ_d(d): return N(PI * d)
def circ_r(r): return N(PI * 2 * r)
def area_r(r): return N(PI * r * r)
def trap(b1, b2, h): return N(Fr(b1 + b2, 2) * h)
def box_sa(l, w, h): return N(2 * (l * w + l * h + w * h))
def box_v(l, w, h): return N(Fr(l) * w * h)


# ------------------------------- Week 1 -------------------------------
L1 = Lesson("9.1", "Angle Relationships",
    "I can identify complementary, supplementary, vertical, and adjacent angles.", "7.G.5",
    [("complementary angles", "Two angles whose measures add to 90°."), ("supplementary angles", "Two angles whose measures add to 180°."),
     ("vertical angles", "Opposite angles formed by two intersecting lines. They are equal."), ("adjacent angles", "Angles that share a vertex and a side but do not overlap.")],
    "Two straight roads cross. One angle at the corner measures 60°. What are the other three angles?",
    [Figure(lambda t: Table([[rays_fig(t, [0, 60, 180, 240], ["60°", "120°", "60°", "120°"], full=True, width=150, height=150),
                              rays_fig(t, [0, 130, 180], ["130°", "50°"], width=190, height=100), rays_fig(t, [0, 35, 90], ["35°", "55°"], width=150, height=100)],
                             [P("Vertical angles are equal; neighbors are supplementary.", t.small), P("Supplementary: 130° + 50° = 180°", t.small), P("Complementary: 35° + 55° = 90°", t.small)]],
                            colWidths=[W / 3] * 3)),
     Example("Crossing roads", "One angle is 60°", ["The vertical angle is also 60°.", "Each neighbor is 180° − 60° = 120°."], "60°, 120°, 60°, 120°"),
     KeyIdea("Complementary → 90°. Supplementary → 180°. Vertical angles are equal.")],
    [Problem("Complement of 28°", "62°"), Problem("Supplement of 28°", "152°"), Problem("Two lines cross; one angle is 75°. Its vertical angle?", "75°")],
    [S("Warm-Up", [Problem("90 − 35", "55"), Problem("180 − 130", "50")]),
     S("Find the angle", [Problem(e, a) for e, a in [("Complement of 40°", "50°"), ("Supplement of 40°", "140°"), ("Complement of 72°", "18°"), ("Supplement of 115°", "65°"),
                                                     ("Vertical angle to 33°", "33°"), ("Neighbor (adjacent, on a line) of 33°", "147°")]]),
     S("Name the relationship", [Problem("", "vertical angles (∠1 and ∠3); ∠1 and ∠2 are supplementary", fig=lambda t: rays_fig(t, [0, 70, 180, 250], ["1", "2", "3", "4"], full=True, width=140, height=140), space=0),
                                 Problem("Can two angles be both complementary and vertical? Explain.", "Yes, if each is 45°", lines=3, space=0)]),
     S("Exit Ticket", [Problem("Two angles are supplementary. One is 4 times the other. Find both.", "36° and 144°", wide=True)], cols=1)],
    TE("Students identify angle relationships.", "Use facts about supplementary, complementary, vertical, and adjacent angles.", "Protractor, two pencils, workbook Lesson 9.1",
       flow("Subtraction warm-up.", "Cross two pencils and measure the four angles.", ["Define each pair.", "Say: Vertical angles are across from each other."], "Try It 1–3."),
       ["Mixing up complementary (90) and supplementary (180)."], ["C comes before S, and 90 before 180."], ["Find angle pairs in the house: scissors, doors, roads on a map."]),
    summary="Complementary sum to 90°, supplementary to 180°; vertical angles are equal.")

L2 = Lesson("9.2", "Solving for Unknown Angles",
    "I can write and solve equations to find unknown angles.", "7.G.5, 7.EE.4a",
    [],
    "Two adjacent angles form a straight line. One is (2x + 10)° and the other is 70°. Find x.",
    [Example("Supplementary", "(2x + 10) + 70 = 180", ["2x + 80 = 180.", "2x = 100, so x = 50.", "The angle is 2(50) + 10 = 110°."], "x = 50"),
     Example("Vertical", "Vertical angles 3x° and 105°", ["3x = 105."], "x = 35"),
     Example("Complementary", "Angles x° and 2x° are complementary", ["x + 2x = 90; 3x = 90."], "x = 30; angles 30° and 60°"),
     KeyIdea("Write an equation from the relationship (sum to 90°, sum to 180°, or equal), then solve.")],
    [Problem("x + 48 = 90", "x = 42"), Problem("Vertical angles (4x − 20)° and 60°", "x = 20"), Problem("Supplementary: 5x and 4x", "x = 20")],
    [S("Warm-Up", [Problem("2x + 80 = 180", "x = 50"), Problem("3x = 105", "x = 35")]),
     S("Write an equation and solve", [Problem(e, a) for e, a in [("Complementary: x° and 64°", "x + 64 = 90; x = 26"), ("Supplementary: (x + 30)° and 2x°", "3x + 30 = 180; x = 50"),
                                                                 ("Vertical: (5x − 10)° and 80°", "5x − 10 = 80; x = 18"), ("Complementary: (3x)° and (x + 10)°", "4x + 10 = 90; x = 20"),
                                                                 ("Three angles on a line: 40°, x°, and 2x°", f"3x + 40 = 180; x = {RF(Fr(140, 3))}"),
                                                                 ("Angles around a point: 90°, 150°, and x°", "x = 120")]], cols=1),
     S("Exit Ticket", [Problem("Two vertical angles measure (6x + 4)° and (4x + 20)°. Find x and the angle.", "x = 8; 52°", wide=True)], cols=1)],
    TE("Students solve for unknown angles.", "Write and solve simple equations for an unknown angle in a figure.", "Workbook Lesson 9.2",
       flow("Equation warm-up.", "Read Let's Explore.", ["Name the relationship first, then write the equation."], "Try It 1–3."),
       ["Stopping at x instead of finding the angle."], ["Underline what the question asks for."], ["Write your own angle puzzle."]),
    summary="Relationship → equation → solve → check the angle.")

L3 = Lesson("9.3", "Circles and Circumference",
    "I can find the circumference of a circle from its radius or diameter.", "7.G.4",
    [("circumference", "The distance around a circle."), ("diameter", "A segment across a circle through its center; d = 2r."), ("radius", "A segment from the center to the circle."),
     ("pi (π)", "The ratio of any circle's circumference to its diameter, about 3.14.")],
    "Measure around a can and across its top. Divide. Try another circle. What do you notice?",
    [Text("For every circle, circumference ÷ diameter is the same number, <b>π</b> (about 3.14). So <b>C = πd</b>, or <b>C = 2πr</b>. In this book use 3.14 for π unless told otherwise."),
     Figure(lambda t: Table([[circle_fig(t, r_label="r = 7 cm", width=130), circle_fig(t, d_label="d = 10 in.", width=130, show="d")]], colWidths=[W / 2] * 2)),
     Example("Diameter", "d = 10 in.", [f"C = 3.14 × 10 = {circ_d(10)}."], f"{circ_d(10)} in."),
     Example("Radius", "r = 7 cm", [f"d = 14; C = 3.14 × 14 = {circ_r(7)}."], f"{circ_r(7)} cm"),
     Example("Work backward", "C = 62.8 m", [f"d = 62.8 ÷ 3.14 = {N(Fr('62.8') / PI)}."], f"d = {N(Fr('62.8') / PI)} m"),
     KeyIdea("C = πd = 2πr. Use π ≈ 3.14.")],
    [Problem("C when d = 6 ft", f"{circ_d(6)} ft"), Problem("C when r = 3 m", f"{circ_r(3)} m"), Problem("d when C = 31.4 cm", "10 cm")],
    [S("Warm-Up", [Problem("3.14 × 10", "31.4"), Problem("2 × 7", "14")]),
     S("Find the circumference", [Problem(f"{k} = {v} {u}", f"{circ_d(v) if k == 'd' else circ_r(v)} {u}") for k, v, u in [("d", 4, "cm"), ("r", 5, "in."), ("d", 20, "ft"), ("r", 12, "m"), ("d", Fr(5, 2), "cm"), ("r", 50, "mm")]]),
     S("Solve", [Problem("A bike wheel has diameter 26 in. How far does it roll in one turn? In 100 turns?", f"{circ_d(26)} in.; {N(PI * 26 * 100)} in.", space=30, wide=True),
                 Problem("A circular track is 314 m around. What is its diameter?", "100 m", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("A circle has radius 9 cm. Find its circumference.", f"{circ_r(9)} cm", wide=True)], cols=1)],
    TE("Students find circumference.", "Know the formula for the circumference of a circle and use it to solve problems.", "String, ruler, 3 round objects, workbook Lesson 9.3",
       flow("Warm-up.", "Measure C and d of three circles; divide.", ["Discover π; derive C = πd."], "Try It 1–3."),
       ["Using the radius in C = πd."], ["Write d = 2r first."], ["Measure the circumference of a car tire; how many turns per mile?"]),
    summary="C = πd = 2πr, with π ≈ 3.14.")

L4 = Lesson("9.4", "Area of a Circle",
    "I can find the area of a circle.", "7.G.4",
    [],
    "Cut a paper circle into 16 wedges and rearrange them. What shape do they almost make?",
    [Text("The wedges form a shape that is almost a parallelogram. Its base is half the circumference (πr) and its height is the radius (r). So its area is πr × r = <b>πr²</b>."),
     Example("Radius", "r = 5 cm", [f"A = 3.14 × 5² = 3.14 × 25 = {area_r(5)}."], f"{area_r(5)} cm²"),
     Example("Diameter", "d = 8 in.", [f"r = 4; A = 3.14 × 16 = {area_r(4)}."], f"{area_r(4)} in²"),
     WatchOut("Square the radius before multiplying by π. And use the radius, not the diameter."),
     KeyIdea("A = πr².")],
    [Problem("A when r = 10 m", f"{area_r(10)} m²"), Problem("A when d = 6 ft", f"{area_r(3)} ft²"), Problem("A when r = 1.5 cm", f"{area_r(Fr(3, 2))} cm²")],
    [S("Warm-Up", [Problem("5²", "25"), Problem("3.14 × 25", "78.5")]),
     S("Find the area", [Problem(f"{k} = {v} {u}", f"{area_r(v if k == 'r' else Fr(v, 2))} {u}²") for k, v, u in [("r", 2, "cm"), ("r", 7, "in."), ("d", 10, "ft"), ("d", 12, "m"), ("r", 20, "yd"), ("d", 3, "cm")]]),
     S("Solve", [Problem("A sprinkler waters a circle of radius 15 ft. What area does it water?", f"{area_r(15)} ft²", space=24, wide=True),
                 Problem("A 12-in. pizza (diameter) costs $12. A 16-in. pizza costs $18. Which is the better deal per square inch?", f"16-in. pizza: {area_r(8)} in² for $18 (about 9¢ per in²) beats {area_r(6)} in² for $12 (about 11¢ per in²)", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Find the area of a circle with diameter 14 cm.", f"{area_r(7)} cm²", wide=True)], cols=1)],
    TE("Students find the area of a circle.", "Know the formula for the area of a circle; give an informal derivation of the relationship between circumference and area.", "Paper circle, scissors, workbook Lesson 9.4",
       flow("Warm-up.", "Cut and rearrange the wedges.", ["Derive A = πr²."], "Try It 1–3. Weekly Check tomorrow."),
       ["Using the diameter in A = πr².", "Computing (πr)²."], ["Circle the r before you start."], ["Compare pizza deals at a real restaurant."]),
    summary="A = πr²: square the radius, then multiply by π.")


# ------------------------------- Week 2 -------------------------------
SEMI_A = 10 * 6 + PI * 5 * 5 / 2
SEMI_P = 10 + 6 + 6 + PI * 10 / 2
L5 = Lesson("9.5", "Problems with Circles",
    "I can find areas and perimeters of figures made from parts of circles.", "7.G.4",
    [("semicircle", "Half of a circle.")],
    "A window is a 10 m by 6 m rectangle topped by a semicircle. How much glass does it need? How much trim goes around it?",
    [Figure(lambda t: rect_semi(t, 10, 6, "m", width=200, height=150)),
     Example("Area", "Rectangle + half circle (r = 5)", ["Rectangle: 10 × 6 = 60.", f"Half circle: 3.14 × 25 ÷ 2 = {N(PI * 25 / 2)}.", f"Total: 60 + {N(PI * 25 / 2)}."], f"{N(SEMI_A)} m²"),
     Example("Perimeter", "Three sides of the rectangle + half the circumference", ["10 + 6 + 6 = 22.", f"Half of 3.14 × 10 = {N(PI * 5)}.", f"22 + {N(PI * 5)}."], f"{N(SEMI_P)} m"),
     KeyIdea("Break the figure into rectangles and circle parts. Include only the edges on the outside for perimeter.")],
    [Problem("Area of a semicircle, r = 4 cm", f"{N(PI * 16 / 2)} cm²"), Problem("Area of a quarter circle, r = 10 ft", f"{N(PI * 100 / 4)} ft²"), Problem("Perimeter of a semicircle, d = 10 in. (curve + diameter)", f"{N(PI * 5 + 10)} in.")],
    [S("Warm-Up", [Problem("3.14 × 25 ÷ 2", "39.25"), Problem("3.14 × 10 ÷ 2", "15.7")]),
     S("Find the area", [Problem("Semicircle, r = 6 m", f"{N(PI * 36 / 2)} m²"), Problem("Quarter circle, r = 2 cm", f"{N(PI * 4 / 4)} cm²"),
                         Problem("Square 8 × 8 with a circle (d = 8) cut out", f"{N(64 - PI * 16)} square units"), Problem("Rectangle 12 × 4 with semicircles on both short ends", f"{N(48 + PI * 4)} square units")]),
     S("Solve", [Problem("A running track is a 100 m by 60 m rectangle with semicircles on both 60 m ends. Find the distance around the track.", f"{N(200 + PI * 60)} m", space=36, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Find the area of the window above if the rectangle is 4 ft by 3 ft (semicircle on the 4 ft side).", f"{N(12 + PI * 2)} ft²", wide=True)], cols=1)],
    TE("Students solve problems with parts of circles.", "Solve real-world problems involving area and circumference of circles.", "Workbook Lesson 9.5",
       flow("Warm-up.", "Read Let's Explore.", ["Area: add parts.", "Perimeter: only outside edges."], "Try It 1–3."),
       ["Including the dashed inside segment in the perimeter."], ["Trace the outside with a finger."], ["Design a garden with curved edges and find its area."]),
    summary="Split the figure into rectangles and circle parts; perimeter uses only outside edges.")

LS = (12, 9, 5, 4)   # l_shape: full width 12, full height 9, top part width 5, bottom height 4
LS_A = LS[0] * LS[3] + LS[2] * (LS[1] - LS[3])
L6 = Lesson("9.6", "Area of Composite Figures",
    "I can find the area of composite figures made of triangles, rectangles, and trapezoids.", "7.G.6",
    [("composite figure", "A figure made of two or more simple shapes.")],
    "A garden is shaped like an L. How can you find its area without a formula for L-shapes?",
    [Figure(lambda t: Table([[l_shape(t, *LS, unit="ft", width=200, height=140), polygon_fig(t, [(0, 0), (1, 0), (0.75, 1), (0.25, 1)], width=170, height=100, edge_labels=["10 m", "", "5 m", ""])],
                             [P("Split into two rectangles.", t.small), P("Trapezoid, height 4 m", t.small)]], colWidths=[W / 2] * 2)),
     Example("L-shape", "Split into rectangles", [f"Bottom: {LS[0]} × {LS[3]} = {LS[0] * LS[3]}.", f"Top: {LS[2]} × {LS[1] - LS[3]} = {LS[2] * (LS[1] - LS[3])}."], f"{LS_A} ft²"),
     Example("Trapezoid", "Bases 10 m and 5 m, height 4 m", [f"A = (10 + 5) ÷ 2 × 4 = {trap(10, 5, 4)}."], f"{trap(10, 5, 4)} m²"),
     Figure(lambda t: table(t, [["Shape", "Area formula"], ["rectangle", "A = lw"], ["triangle", P(f"A = {F(1, 2)}bh", t.cell)], ["parallelogram", "A = bh"], ["trapezoid", P(f"A = {F(1, 2)}(b₁ + b₂)h", t.cell)]],
                            [2.0 * inch, 2.4 * inch], width=4.4 * inch)),
     KeyIdea("Decompose into shapes you know, find each area, and add (or subtract cut-out parts).")],
    [Problem("Triangle, b = 9, h = 6", "27"), Problem("Trapezoid, bases 7 and 11, h = 5", trap(7, 11, 5)), Problem("Rectangle 10 × 8 with a 3 × 3 square cut out", "71")],
    [S("Warm-Up", [Problem("12 × 4 + 5 × 5", "73"), Problem("(10 + 5) ÷ 2 × 4", "30")]),
     S("Find the area", [Problem("L-shape: full width 10, full height 8, top width 4, bottom height 3", f"{10 * 3 + 4 * 5}", fig=lambda t: l_shape(t, 10, 8, 4, 3, width=CW, height=110), space=0),
                         Problem("Trapezoid: bases 6 and 14, height 5", trap(6, 14, 5)), Problem("A rectangle 8 × 5 with a triangle (base 8, height 3) on top", f"{40 + 12}"),
                         Problem("Parallelogram b = 12, h = 7", "84")]),
     S("Solve", [Problem("A deck is a 16 ft by 12 ft rectangle with a 4 ft by 4 ft square cut out for a tree. Stain covers 50 ft² per can. How many cans?", f"{16 * 12 - 16} ft²; 4 cans", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Find the area: a 10 × 6 rectangle with a right triangle (legs 6 and 4) attached to the right side.", f"{60 + 12}", wide=True)], cols=1)],
    TE("Students find areas of composite figures.", "Solve real-world problems involving area of two-dimensional objects composed of triangles, quadrilaterals, and polygons.", "Workbook Lesson 9.6",
       flow("Warm-up.", "Discuss Let's Explore.", ["Decompose the L two ways; same answer."], "Try It 1–3."),
       ["Double-counting overlap."], ["Shade each part a different color."], ["Find the area of a room with an alcove."]),
    summary="Split, find each area, then add or subtract.")

L7 = Lesson("9.7", "Surface Area of Prisms",
    "I can find the surface area of rectangular and triangular prisms.", "7.G.6",
    [("surface area", "The total area of all the faces of a solid."), ("net", "A flat pattern that folds into a solid.")],
    "How much cardboard does a 5 in. by 3 in. by 4 in. box need?",
    [Figure(lambda t: Table([[prism_fig(t, 5, 3, 4, "in.", width=190, height=130), tri_prism(t, 6, 8, 12, "cm", width=210, height=130)],
                             [P("Rectangular prism", t.small), P("Triangular prism: legs 6 and 8, hypotenuse 10, length 12", t.small)]], colWidths=[W / 2] * 2)),
     Example("Rectangular prism", "5 × 3 × 4", ["Top and bottom: 2 × (5 × 3) = 30.", "Front and back: 2 × (5 × 4) = 40.", "Sides: 2 × (3 × 4) = 24."], f"{box_sa(5, 3, 4)} in²"),
     Example("Triangular prism", "Legs 6 and 8, hypotenuse 10, length 12", [f"Two triangles: 2 × {F(1, 2)} × 6 × 8 = 48.", "Three rectangles: (6 + 8 + 10) × 12 = 288."], "336 cm²"),
     KeyIdea("Surface area = the sum of the areas of all faces. A net helps you see every face.")],
    [Problem("Cube with edge 3 cm", "54 cm²"), Problem("Box 10 × 2 × 4", f"{box_sa(10, 2, 4)}"), Problem("Box 6 × 6 × 1", f"{box_sa(6, 6, 1)}")],
    [S("Warm-Up", [Problem("2 × (15 + 20 + 12)", "94"), Problem(f"{F(1, 2)} × 6 × 8", "24")]),
     S("Find the surface area", [Problem(f"Box {l} × {w} × {h}", box_sa(l, w, h)) for l, w, h in [(4, 4, 4), (8, 3, 2), (10, 5, 6), (Fr(3, 2), 2, 4)]]
                               + [Problem("Triangular prism: legs 3 and 4, hypotenuse 5, length 10", f"{2 * 6 + 12 * 10}"), Problem("Triangular prism: legs 5 and 12, hypotenuse 13, length 8", f"{2 * 30 + 30 * 8}")]),
     S("Solve", [Problem("Lillie wraps a gift box 12 in. × 8 in. × 3 in. How much wrapping paper covers it exactly?", f"{box_sa(12, 8, 3)} in²", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Find the surface area of a box 7 cm × 2 cm × 5 cm.", f"{box_sa(7, 2, 5)} cm²", wide=True)], cols=1)],
    TE("Students compute surface area of prisms.", "Solve real-world problems involving surface area of objects composed of triangles, quadrilaterals, and prisms.", "Empty cereal box (to cut into a net), workbook Lesson 9.7",
       flow("Warm-up.", "Unfold a cereal box into a net.", ["Pair the faces.", "Triangular prism: two triangles + three rectangles."], "Try It 1–3."),
       ["Counting only three faces."], ["Use the net; check off each face."], ["Find the SA of a real box at home."]),
    summary="Add the areas of every face; nets help.")

L8 = Lesson("9.8", "Volume of Prisms",
    "I can find the volume of any right prism using V = Bh.", "7.G.6",
    [("volume", "The amount of space inside a solid, in cubic units."), ("base area (B)", "The area of the prism's base.")],
    "How many 1-inch cubes fill a 5 in. by 3 in. by 4 in. box?",
    [Text("The base holds 5 × 3 = 15 cubes per layer, and there are 4 layers: 60 cubes. For any prism, <b>V = Bh</b>, where B is the area of the base and h is the prism's height (the distance between the bases)."),
     Example("Rectangular prism", "5 × 3 × 4", ["B = 15; h = 4."], f"{box_v(5, 3, 4)} in³"),
     Example("Triangular prism", "Base triangle legs 6 and 8; length 12", [f"B = {F(1, 2)} × 6 × 8 = 24.", "V = 24 × 12."], "288 cm³"),
     Example("Trapezoid base", "Bases 4 and 6, height 3; prism length 10", [f"B = {trap(4, 6, 3)}.", f"V = {trap(4, 6, 3)} × 10."], f"{N(Fr(4 + 6, 2) * 3 * 10)} cubic units"),
     KeyIdea("V = Bh for every right prism. Volume is measured in cubic units.")],
    [Problem("Box 6 × 2 × 5", box_v(6, 2, 5)), Problem("Cube edge 4", "64"), Problem("Prism with B = 18 cm², h = 7 cm", "126 cm³")],
    [S("Warm-Up", [Problem("5 × 3 × 4", "60"), Problem("24 × 12", "288")]),
     S("Find the volume", [Problem(f"Box {l} × {w} × {h}", box_v(l, w, h)) for l, w, h in [(9, 2, 3), (Fr(5, 2), 4, 6), (10, 10, Fr(1, 2))]]
                         + [Problem("Triangular prism: legs 3 and 4, length 10", "60"), Problem("Trapezoid base (bases 5, 9; height 2), length 6", N(Fr(14, 2) * 2 * 6)), Problem("B = 32.5 in², h = 4 in.", "130 in³")]),
     S("Solve", [Problem("A fish tank is 30 in. × 12 in. × 16 in. One gallon is about 231 in³. About how many gallons does it hold?", f"{30 * 12 * 16:,} in³; about {round(30 * 12 * 16 / 231)} gallons", space=30, wide=True)], cols=1),
     S("Exit Ticket", [Problem("A prism's base is a triangle with base 10 cm and height 6 cm. The prism is 9 cm long. Find its volume.", "270 cm³", wide=True)], cols=1)],
    TE("Students find volumes of prisms.", "Solve real-world problems involving volume of right prisms.", "Unit cubes (optional), workbook Lesson 9.8",
       flow("Warm-up.", "Build the box with layers of cubes.", ["V = Bh for any prism."], "Try It 1–3. Weekly Check tomorrow."),
       ["Using a side length instead of the base area for B."], ["Shade the base first."], ["Compare the volumes of two cereal boxes."]),
    summary="V = Bh: base area × height.")

# ------------------------------- Week 3 -------------------------------
L9 = Lesson("9.9", "Volume and Surface Area in Context",
    "I can decide whether a problem needs volume or surface area and solve it.", "7.G.6",
    [],
    "A sandbox is 6 ft by 4 ft by 1 ft. You want to fill it with sand and paint its outside walls. Which needs volume? Which needs area?",
    [Example("Fill → volume", "6 × 4 × 1", ["V = 24."], "24 ft³ of sand"),
     Example("Paint → area", "Four outside walls (no top or bottom)", ["2 × (6 × 1) + 2 × (4 × 1) = 12 + 8."], "20 ft² of paint"),
     Figure(lambda t: table(t, [["Volume (cubic units)", "Surface area (square units)"], ["fill, hold, pour, pack inside", "wrap, cover, paint, label outside"]], width=5.4 * inch)),
     KeyIdea("Filling uses volume; covering uses surface area. Decide which faces are included.")],
    [Problem("Water to fill a pool", "volume"), Problem("Tiles to line the pool's walls and floor", "surface area"), Problem("Label around a soup can", "surface area (lateral)")],
    [S("Warm-Up", [Problem("6 × 4 × 1", "24"), Problem("2 × 6 + 2 × 4", "20")]),
     S("Volume or surface area? Then solve.", [
         Problem("How much soil fills a planter 3 ft × 2 ft × 1.5 ft?", "volume; 9 ft³", space=24, wide=True),
         Problem("How much fabric covers a cube-shaped ottoman, 2 ft edges, all faces except the bottom?", "surface area; 20 ft²", space=24, wide=True),
         Problem("An open-top box (no lid) is 10 cm × 8 cm × 5 cm. How much cardboard?", f"surface area; {10 * 8 + 2 * 10 * 5 + 2 * 8 * 5} cm²", space=24, wide=True),
         Problem("Ice cubes are 2 cm on each edge. How many fit in a 10 cm × 8 cm × 6 cm tray (exactly packed)?", f"volume; {(10 // 2) * (8 // 2) * (6 // 2)} cubes", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Paint covers 350 ft² per gallon. Walls of a room total 1,050 ft². How many gallons?", "3 gallons", wide=True)], cols=1)],
    TE("Students choose volume or surface area.", "Solve real-world problems involving area, volume, and surface area.", "Workbook Lesson 9.9",
       flow("Warm-up.", "Discuss the sandbox.", ["Sort situations: fill vs cover."], "Try It 1–3."),
       ["Including the top when the box is open."], ["Sketch which faces count."], ["Plan a raised garden bed: soil and wood."]),
    summary="Fill → volume; cover → surface area.")

L10 = Lesson("9.10", "Composite Solids",
    "I can find the volume and surface area of solids made from prisms.", "7.G.6",
    [],
    "A set of steps is made of two boxes: a bottom box 6 ft × 3 ft × 1 ft and a top box 3 ft × 3 ft × 1 ft on one end. How much concrete is needed?",
    [Example("Volume", "Add the boxes", [f"Bottom: {box_v(6, 3, 1)}. Top: {box_v(3, 3, 1)}."], f"{6 * 3 + 3 * 3} ft³"),
     Example("Another solid", "A 10 × 10 × 10 cube with a 2 × 2 × 10 hole drilled through", ["Cube: 1,000. Hole: 40."], "960 cubic units"),
     KeyIdea("Volume of a composite solid: add the parts, or subtract the parts removed.")],
    [Problem("Two cubes, edges 3 and 2, stacked", "35"), Problem("Box 8 × 5 × 4 with a 2 × 2 × 4 hole", f"{160 - 16}"), Problem("Box 5 × 5 × 5 plus a 5 × 5 × 2 box on top", f"{125 + 50}")],
    [S("Warm-Up", [Problem("6 × 3 × 1 + 3 × 3 × 1", "27"), Problem("1,000 − 40", "960")]),
     S("Find the volume", [Problem(e, a) for e, a in [("L-shaped block: 10 × 4 × 2 plus 4 × 4 × 2", f"{80 + 32}"), ("Box 12 × 6 × 6 minus a cube of edge 3", f"{432 - 27}"),
                                                     ("Triangular prism (legs 4, 6; length 10) on a box 6 × 10 × 2", f"{120 + 120}"), ("Three stacked boxes: 6 × 6 × 1, 4 × 4 × 1, 2 × 2 × 1", f"{36 + 16 + 4}")]], cols=1),
     S("Exit Ticket", [Problem("A planter is a 4 ft × 2 ft × 2 ft box with a 4 ft × 1 ft × 1 ft box attached on the side. How much soil does it hold?", f"{16 + 4} ft³", wide=True)], cols=1)],
    TE("Students find volumes of composite solids.", "Solve real-world problems involving volume of composite objects.", "Unit cubes, workbook Lesson 9.10",
       flow("Warm-up.", "Build the steps with cubes.", ["Add or subtract parts."], "Try It 1–3."),
       ["Forgetting to subtract a hole."], ["Sketch each part."], ["Find the volume of a room with a closet."]),
    summary="Add the parts, or subtract what is removed.")

L11 = Lesson("9.11", "Comparing Volume and Surface Area",
    "I can compare solids with the same volume but different surface areas.", "7.G.6",
    [],
    "Boxes 8 × 1 × 1, 4 × 2 × 1, and 2 × 2 × 2 all hold 8 cubes. Which uses the least cardboard?",
    [Figure(lambda t: table(t, [["Box", "Volume", "Surface area"]] + [[f"{l} × {w} × {h}", box_v(l, w, h), box_sa(l, w, h)] for l, w, h in [(8, 1, 1), (4, 2, 1), (2, 2, 2)]], width=4.6 * inch)),
     Text("All three hold the same amount, but the cube uses the least material. The closer a box is to a cube, the less surface area it needs for its volume."),
     KeyIdea("Same volume can have different surface areas. Cube-like shapes use the least surface area.")],
    [Problem("SA of 12 × 1 × 1", box_sa(12, 1, 1)), Problem("SA of 3 × 2 × 2", box_sa(3, 2, 2)), Problem("Both have volume 12. Which uses less material?", "3 × 2 × 2")],
    [S("Warm-Up", [Problem("8 × 1 × 1", "8"), Problem("2 × 2 × 2", "8")]),
     S("Volume 24: find the surface area", [Problem(f"{l} × {w} × {h}", box_sa(l, w, h)) for l, w, h in [(24, 1, 1), (12, 2, 1), (6, 4, 1), (4, 3, 2)]]),
     S("Explain", [Problem("A company wants a box that holds 24 cubes and uses the least cardboard. Which box above should it choose? Why?", "4 × 3 × 2; it is the most cube-like, with the least surface area (52)", lines=2, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Can two boxes have the same surface area but different volumes? Give an example.", f"Yes: 1 × 1 × 5 (SA {box_sa(1, 1, 5)}, V 5) and 2 × 1 × 3 (SA {box_sa(2, 1, 3)}, V 6)", lines=2, space=0, wide=True)], cols=1)],
    TE("Students compare volume and surface area.", "Solve real-world and mathematical problems involving volume and surface area.", "Unit cubes, workbook Lesson 9.11",
       flow("Warm-up.", "Build all boxes from 8 cubes.", ["Table of V and SA."], "Try It 1–3."),
       ["Thinking same volume means same SA."], ["Build them."], ["Why are many animals in cold climates round and compact?"]),
    summary="Same volume can have different surface areas; cubes use the least.")

L12 = Lesson("9.12", "Geometry Problem Solving",
    "I can choose and use the right geometry formulas to solve multi-step problems.", "7.G.4, 7.G.5, 7.G.6",
    [],
    "A circular pool (diameter 20 ft) is surrounded by a 3 ft wide concrete path. What is the area of the path?",
    [Example("Ring area", "Outer radius 13 ft, inner radius 10 ft", [f"Outer: 3.14 × 169 = {area_r(13)}.", f"Inner: 3.14 × 100 = {area_r(10)}.", "Subtract."], f"{N(PI * (169 - 100))} ft²"),
     Figure(lambda t: table(t, [["Measure", "Formula"], ["Circumference", "C = πd = 2πr"], ["Circle area", "A = πr²"], ["Triangle area", P(f"A = {F(1, 2)}bh", t.cell)], ["Trapezoid area", P(f"A = {F(1, 2)}(b₁ + b₂)h", t.cell)],
                                ["Prism volume", "V = Bh"], ["Surface area", "sum of all face areas"]], [2.0 * inch, 2.6 * inch], width=4.6 * inch)),
     KeyIdea("Plan: draw, label, choose the formula, compute, and check the units.")],
    [Problem("Circumference of the pool", f"{circ_d(20)} ft"), Problem("Outer edge of the path", f"{circ_d(26)} ft"), Problem("Volume of a 1 ft deep layer of water in the pool", f"{area_r(10)} ft³")],
    [S("Warm-Up", [Problem("13²", "169"), Problem("169 − 100", "69")]),
     S("Solve", [
         Problem("A circular table has diameter 4 ft. A cloth hangs 1 ft over the edge all around. What is the cloth's area?", f"r = 3; {area_r(3)} ft²", space=30, wide=True),
         Problem("Two angles are supplementary. One is 24° more than the other. Find both.", "78° and 102°", space=30, wide=True),
         Problem("A tent is a triangular prism: triangle base 6 ft, height 4 ft, length 8 ft. Find the space inside.", "96 ft³", space=30, wide=True),
         Problem("A cylindrical-looking hay bale is wrapped with a band around its 5 ft diameter. How long is the band?", f"{circ_d(5)} ft", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write your own two-step geometry problem and solve it.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students solve mixed geometry problems.", "Solve real-world and mathematical problems involving angle measure, area, surface area, and volume.", "Formula card, workbook Lesson 9.12",
       flow("Warm-up.", "Read Let's Explore.", ["Model the plan: draw, label, choose, compute, check."], "Try It 1–3. Weekly Check tomorrow."),
       ["Picking the wrong formula."], ["Use the formula table."], ["Measure and solve a real geometry problem at home."]),
    summary="Draw, label, choose a formula, compute, and check units.")

# ------------------------------- Week 4: Year Review -------------------------------
L13 = Lesson("9.13", "Year Review: Ratios, Proportions, and Percents",
    "I can solve problems with unit rates, proportional relationships, and percents.", "7.RP.1–3",
    [],
    "Which is the better buy: 3 lb of apples for $4.47 or 5 lb for $7.25?",
    [Example("Unit rates", "$4.47 ÷ 3 vs $7.25 ÷ 5", ["$1.49 per lb vs $1.45 per lb."], "5 lb for $7.25"),
     Example("Percent change", "Price rises from $80 to $100", ["Change: 20.", "20 ÷ 80 = 0.25."], "25% increase"),
     KeyIdea("Unit rates compare; proportions scale; percent = part ÷ whole × 100.")],
    [Problem(f"Unit rate: {F(3, 4)} mi in {F(1, 4)} hr", "3 mph"), Problem("y is proportional to x; y = 10 when x = 4. Find k.", "2.5"), Problem("20% off $65", "$52")],
    [S("Warm-Up", [Problem("4.47 ÷ 3", "1.49"), Problem("7.25 ÷ 5", "1.45")]),
     S("Review: Units 1–2", [Problem(e, a) for e, a in [("Ellie reads 45 pages in 1.5 hours. Pages per hour?", "30"), (f"Solve: {F(6, 15)} = {F('<i>x</i>', 40)}", "x = 16"),
                                                       ("Is y = 4x + 1 proportional?", "No"), ("15% tip on $48", "$7.20"), ("Price $120 → $90: percent change", "25% decrease"), ("Simple interest: $500 at 4% for 3 years", "$60"),
                                                       ("6% tax on $35", "$2.10"), ("Map: 2 cm : 15 km. 7 cm?", "52.5 km")]]),
     S("Exit Ticket", [Problem("A recipe uses 3 cups flour for 2 dozen cookies. How much for 5 dozen?", "7.5 cups", wide=True)], cols=1)],
    TE("Review Units 1–2.", "Analyze proportional relationships and use them to solve problems.", "Workbook Lesson 9.13",
       flow("Warm-up.", "Better buy.", ["Review unit rates, k, percent change."], "Try It 1–3."),
       ["Dividing the wrong way for unit rate."], ["Label units."], ["Compare real grocery prices."]),
    summary="Unit rates, proportions, and percents.")

L14 = Lesson("9.14", "Year Review: Rational Numbers",
    "I can add, subtract, multiply, and divide rational numbers.", "7.NS.1–3",
    [],
    "The temperature was −6°F at dawn and rose 14°F by noon, then fell 9°F by night. What was the night temperature?",
    [Example("Integer steps", "−6 + 14 − 9", ["−6 + 14 = 8.", "8 − 9 = −1."], "−1°F"),
     Example("Fractions", f"−{F(3, 4)} ÷ {F(1, 2)}", [f"−{F(3, 4)} × 2 = −{F(6, 4)}."], f"−{RF(Fr(3, 2))}"),
     KeyIdea("Same signs multiply/divide to positive; different signs to negative. Subtracting means adding the opposite.")],
    [Problem("−7 + 12", "5"), Problem("−3 − (−8)", "5"), Problem("−2.5 × 4", "−10")],
    [S("Warm-Up", [Problem("−6 + 14", "8"), Problem("8 − 9", "−1")]),
     S("Review: Units 3–5", [Problem(e, a) for e, a in [("−15 + (−9)", "−24"), ("4 − 11", "−7"), ("−1.2 + 3.5", "2.3"), ("(−6)(−7)", "42"), ("−48 ÷ 6", "−8"), (f"{F(2, 3)} × (−{F(9, 10)})", f"−{F(3, 5)}"),
                                                       (f"Write {F(5, 8)} as a decimal", "0.625"), (f"Write {F(2, 3)} as a decimal", "0.6 repeating"), ("(−2)³", "−8"), ("|−9| − |4|", "5")]]),
     S("Exit Ticket", [Problem("A diver at −40 ft rises 15 ft, then descends 28 ft. Where is she?", "−53 ft", wide=True)], cols=1)],
    TE("Review Units 3–5.", "Apply operations with rational numbers.", "Workbook Lesson 9.14",
       flow("Warm-up.", "Temperature story.", ["Review sign rules."], "Try It 1–3."),
       ["Sign errors in subtraction."], ["Number line."], ["Make a sign-rule poster."]),
    summary="Sign rules for all four operations.")

L15 = Lesson("9.15", "Year Review: Expressions, Equations, and Inequalities",
    "I can simplify expressions and solve equations and inequalities.", "7.EE.1–4",
    [],
    "A gym charges $20 to join and $15 per month. Lillie has $110. How many months can she afford?",
    [Example("Inequality", "20 + 15m ≤ 110", ["15m ≤ 90.", "m ≤ 6."], "at most 6 months"),
     Example("Simplify", "3(x − 4) + 2x", ["3x − 12 + 2x."], "5x − 12"),
     KeyIdea("Undo operations in reverse order; flip the inequality when multiplying or dividing by a negative.")],
    [Problem("Factor 18y + 12", "6(3y + 2)"), Problem("4x − 7 = 21", "x = 7"), Problem("−3x + 5 > 17", "x < −4")],
    [S("Warm-Up", [Problem("110 − 20", "90"), Problem("90 ÷ 15", "6")]),
     S("Review: Unit 6", [Problem(e, a) for e, a in [("Simplify 5a − 2(a + 3)", "3a − 6"), (f"Simplify {F(1, 2)}(8x − 6) + x", "5x − 3"), ("Evaluate 2x² − x when x = −3", "21"), ("−2(x + 3) = 10", "x = −8"),
                                                    (f"{F(1, 2)}x − 2 = 4", "x = 12"), ("0.4n + 1.2 = 3.6", "n = 6"), ("−4y ≥ 20", "y ≤ −5"), ("2x − 9 < 7", "x < 8")]]),
     S("Exit Ticket", [Problem("Write and solve: three times a number, minus 8, is 25.", "3n − 8 = 25; n = 11", wide=True)], cols=1)],
    TE("Review Unit 6.", "Solve equations and inequalities.", "Workbook Lesson 9.15",
       flow("Warm-up.", "Gym problem.", ["Review distributing, factoring, solving."], "Try It 1–3."),
       ["Forgetting to flip the inequality."], ["Test a value."], ["Write equations for family budgets."]),
    summary="Simplify, solve, and interpret.")

L16 = Lesson("9.16", "Year Review: Statistics, Probability, and Geometry",
    "I can solve problems using statistics, probability, and geometry.", "7.SP, 7.G",
    [],
    "In a random sample of 40 students, 14 walk to school. About how many of the 600 students walk?",
    [Example("Inference", "14 of 40; 600 students", [f"{F(14, 40)} = 35%; 0.35 × 600."], "about 210"),
     Example("Probability", "Two number cubes: P(sum is 8)", ["(2,6), (3,5), (4,4), (5,3), (6,2): 5 outcomes of 36."], F(5, 36)),
     KeyIdea("Use the right tool: proportions for samples, sample spaces for probability, formulas for geometry.")],
    [Problem("P(heads, then heads)", F(1, 4)), Problem("Area of a circle, r = 6", area_r(6)), Problem("Missing angle in a triangle: 50°, 75°", "55°")],
    [S("Warm-Up", [Problem("0.35 × 600", "210"), Problem("6 × 6", "36")]),
     S("Review: Units 7–9", [Problem(e, a) for e, a in [(f"Mean and MAD of 4, 6, 8, 10, 12", "mean 8, MAD 2.4"), ("Bag: 3 red, 5 blue, 2 green. P(not blue)", F(1, 2)), ("Outfits: 4 shirts, 3 pants", "12"),
                                                       ("Scale 1 in. : 6 ft. Drawing 3.5 in.?", "21 ft"), ("Triangle? 3, 4, 8", "No"), ("Supplement of 47°", "133°"), ("Circumference, d = 15 cm", f"{circ_d(15)} cm"),
                                                       ("Volume, box 6 × 4 × 2.5", box_v(6, 4, Fr(5, 2))), ("Surface area, box 6 × 4 × 2", box_sa(6, 4, 2)), ("Cross section of a cylinder, horizontal", "circle")]]),
     S("Exit Ticket", [Problem("Which topic from this year do you feel strongest in? Which one will you review before the test?", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Review Units 7–9.", "Use sampling, probability, and geometry to solve problems.", "Workbook Lesson 9.16, Year-End Review",
       flow("Warm-up.", "Sampling example.", ["Review probability and geometry formulas."], "Try It 1–3.", "Workbook Lesson 9.16 and the Year-End Review.", "Check. Tomorrow: Year-End Test."),
       ["Mixing up area and circumference formulas."], ["Use the formula table in Lesson 9.12."], ["Celebrate the year!"]),
    summary="Pull together statistics, probability, and geometry.")

C1 = Check("Weekly Check 25: Angles and Circles", [S("Show what you know", [
    Problem("Complement of 37°", "53°"), Problem("Vertical angles (3x + 6)° and 51°: x?", "x = 15"), Problem("Supplementary: x° and (2x + 30)°", "x = 50"),
    Problem("Circumference, r = 5 in.", f"{circ_r(5)} in."), Problem("Area, d = 10 cm", f"{area_r(5)} cm²"), Problem("Diameter if C = 47.1 m", f"{N(Fr('47.1') / PI)} m")])], minutes=15)
C2 = Check("Weekly Check 26: Area, Surface Area, and Volume", [S("Show what you know", [
    Problem("Semicircle area, r = 10", f"{N(PI * 50)}"), Problem("Trapezoid: bases 8 and 12, height 5", trap(8, 12, 5)), Problem("Surface area, box 4 × 3 × 2", box_sa(4, 3, 2)),
    Problem("Volume, box 4 × 3 × 2", box_v(4, 3, 2)), Problem("Volume, triangular prism: legs 5, 6; length 10", "150"), Problem("SA, cube edge 5", "150")])], minutes=15)
C3 = Check("Weekly Check 27: Geometry Problem Solving", [S("Show what you know", [
    Problem("Filling a tank: volume or SA?", "volume"), Problem("Open box 5 × 4 × 3: cardboard", f"{5 * 4 + 2 * 5 * 3 + 2 * 4 * 3}"), Problem("Box 6 × 6 × 6 minus a 2 × 2 × 6 hole", f"{216 - 24}"),
    Problem("Which has less SA: 6 × 1 × 1 or 3 × 2 × 1?", "3 × 2 × 1"), Problem("Ring: outer r = 5, inner r = 3", f"{N(PI * 16)}"), Problem("Two complementary angles; one is twice the other", "30° and 60°")])], minutes=15)

REVIEW = Check("Year-End Review", [
    S("Ratios, percents, and rational numbers", [Problem("Unit price: 6 for $8.70", "$1.45 each"), Problem("y = kx; y = 21 when x = 3. Find y when x = 8.", "56"), Problem("35% of 240", "84"), Problem("Price $60 → $75: percent change", "25% increase"),
                                                 Problem("−8 − (−3) + 12", "7"), Problem(f"−{F(5, 6)} × {F(3, 10)}", f"−{F(1, 4)}"), Problem("−3.6 ÷ (−0.4)", "9"), Problem(f"{F(7, 20)} as a decimal", "0.35")]),
    S("Algebra", [Problem("Simplify 4(2x − 1) − 3x", "5x − 4"), Problem("−5x + 8 = −17", "x = 5"), Problem("3(n − 2) = 15", "n = 7"), Problem("6 − 2x ≥ 14", "x ≤ −4")]),
    S("Statistics, probability, and geometry", [Problem("18 of 60 sampled like a show; estimate for 2,500", "750"), Problem("Coin + cube: P(T and even)", F(1, 4)),
                                                 Problem("Area, circle r = 4", area_r(4)), Problem("Volume, triangular prism: legs 4 and 9, length 5", "90"), Problem("Scale 1 cm : 8 m; 6.5 cm", "52 m"), Problem("Missing angle: 90° and 34° in a triangle", "56°")])],
    kind="review", minutes=50, teacher_note="Spread over the week as homework, or use as a study session before the Year-End Test.")

TEST = Check("Grade 7 Year-End Test", [
    S("Part A · Ratios and percents (1 point each)", [Problem("Unit rate: 150 miles in 2.5 hours", "60 mph"), Problem("y = kx passes through (5, 35). Find k.", "7"),
        Problem("30% of 90", "27"), Problem("A $40 shirt is 15% off. Sale price?", "$34"), Problem("Price $50 → $65: percent change", "30% increase")]),
    S("Part B · Rational numbers (1 point each)", [Problem("−14 + 9", "−5"), Problem("6 − (−11)", "17"), Problem("(−4)(−2.5)", "10"), Problem(f"−{F(2, 3)} ÷ {F(4, 9)}", f"−{RF(Fr(3, 2))}"), Problem(f"Write {F(3, 8)} as a decimal", "0.375")]),
    S("Part C · Expressions, equations, inequalities (1 point each)", [Problem("Simplify 2(3x − 5) + 4x", "10x − 10"), Problem("Factor 24n − 16", "8(3n − 2)"), Problem("−6x + 4 = 40", "x = −6"),
        Problem("5(y + 2) = −15", "y = −5"), Problem("−2k + 7 ≤ 15", "k ≥ −4")]),
    S("Part D · Statistics and probability (1 point each)", [Problem("A random sample of 50 has 12 left-handed people. Estimate for 1,500.", "360"), Problem("Mean of 3, 7, 8, 10, 12", "8"),
        Problem("Bag: 4 red, 6 blue. P(blue)", F(3, 5)), Problem("Two coins: P(at least one head)", F(3, 4)), Problem("Two number cubes: P(sum is 10)", F(1, 12))]),
    S("Part E · Geometry (1 point each)", [Problem("Scale 1 in. : 12 ft; 3.5 in. Actual?", "42 ft"), Problem("Supplement of 68°", "112°"), Problem("Circumference, d = 12 m", f"{circ_d(12)} m"),
        Problem("Area, r = 9 cm", f"{area_r(9)} cm²"), Problem("Volume, box 7 × 3 × 4", "84"), Problem("Surface area, box 7 × 3 × 4", box_sa(7, 3, 4))]),
    S("Part F · Problem solving (3 points each)", [
        Problem("A phone plan costs $25 per month plus $0.10 per text. Ellie can spend at most $40 per month. Write and solve an inequality for the number of texts. Interpret.", "25 + 0.10t ≤ 40; t ≤ 150; at most 150 texts", space=60, wide=True, points=3),
        Problem("A circular garden has diameter 14 ft. Find its area. Edging costs $2 per foot: how much to edge it? Show your work.", f"{area_r(7)} ft²; C = {circ_d(14)} ft; cost ${N(PI * 14 * 2)}", space=60, wide=True, points=3)], cols=1)],
    kind="test", minutes=60, rubric=[["28–32 (85%+)", "Mastered: ready for Grade 8 math."], ["24–27", "Proficient: review missed strands over the summer."], ["Below 24", "Review missed strands, then retest those parts."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-06-21", "2027-06-28", "2027-07-05", "2027-07-12"], CHECKS, REVIEW, TEST)

UNIT = Unit(9, "Angles, Circles, Area, and Volume", "Angle relationships, circles, composite area, surface area and volume of prisms, and a review of the whole year.",
    "Geometry is everywhere: wheels, windows, pools, and boxes. In this final unit you will use angle facts to find unknown angles, discover π, find areas of composite figures, and measure the surface area and volume of prisms. The last week reviews the whole year.",
    ["Use complementary, supplementary, vertical, and adjacent angles to find unknowns.", "Find the circumference and area of circles.", "Find areas of composite figures.",
     "Find surface area and volume of prisms.", "Review and connect every unit from the year."],
    [("7.G.4", "Know and use the formulas for the area and circumference of a circle."), ("7.G.5", "Use facts about supplementary, complementary, vertical, and adjacent angles."),
     ("7.G.6", "Solve problems involving area, volume, and surface area of two- and three-dimensional objects.")],
    [("supplementary", "Sum to 180°."), ("complementary", "Sum to 90°."), ("circumference", "C = πd."), ("area of a circle", "A = πr²."), ("volume of a prism", "V = Bh.")],
    ["Equations (Unit 6).", "Scale and cross sections (Unit 8).", "Area of rectangles and triangles (Grade 6)."], ["String, ruler, protractor, round objects", "Paper circle and scissors", "Empty boxes, unit cubes"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Builders, engineers, and designers use these formulas daily: pizza sizes, pool covers, paint, packaging, and concrete all depend on area and volume.",
    family_note="This is the final unit of Grade 7! Ask your student to estimate how much paint a room needs or how much water a container holds.",
    weeks=WEEKS)
