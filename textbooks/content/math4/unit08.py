"""Grade 4 Math · Unit 8: Geometry, Angles, and Line Plots (Apr 26 – May 21, 2027)."""
from fractions import Fraction as Fr
from engine import *
from content.mathkit import c, F, MX
from content.te import TE, flow
from content.sched import schedule

CW = 205
SQ = [(0, 0), (1, 0), (1, 1), (0, 1)]
RECT = [(0, 0.15), (1, 0.15), (1, 0.85), (0, 0.85)]
TRI_EQ = [(0, 0), (1, 0), (0.5, 0.9)]
TRI_RT = [(0, 0), (1, 0), (0, 1)]
TRI_OB = [(0, 0), (1, 0), (-0.05, 0.55)]
PARA = [(0, 0), (0.7, 0), (1, 1), (0.3, 1)]
TRAP = [(0, 0), (1, 0), (0.75, 0.8), (0.25, 0.8)]
RHOM = [(0.5, 0), (1, 0.5), (0.5, 1), (0, 0.5)]


def S(title, problems, intro=None, cols=2):
    return Section(title, problems, intro, cols)


def poly(pts, **kw):
    return lambda t: polygon_fig(t, pts, width=kw.pop("width", 130), height=kw.pop("height", 90), **kw)


def ang(d, **kw):
    return lambda t: angle_fig(t, d, width=kw.pop("width", CW), **kw)


def akind(d):
    return "right" if d == 90 else "acute" if d < 90 else "straight" if d == 180 else "obtuse"


L1 = Lesson("8.1", "Points, Lines, Segments, and Rays",
    "I can draw and identify points, lines, line segments, and rays.", "4.G.1",
    [("point", "An exact location, shown with a dot."), ("line", "A straight path that goes on forever in both directions."),
     ("line segment", "Part of a line with two endpoints."), ("ray", "Part of a line with one endpoint that goes on forever in one direction.")],
    "A flashlight beam starts at the flashlight and shines out. A piece of string has two ends. A railroad track seems to go on forever. How are these alike and different?",
    [Text("Geometry has its own vocabulary for straight paths. The difference is in the <b>endpoints</b>."),
     Figure(lambda t: Table([[line_kind(t, "point", ("A",)), line_kind(t, "segment", ("A", "B")), line_kind(t, "ray", ("C", "D")), line_kind(t, "line", ("E", "F"))]],
                            colWidths=[W / 4] * 4)),
     Figure(lambda t: table(t, [["Name", "Endpoints", "How to write it"], ["point A", "—", "A"], ["line segment AB", "2", "AB with a bar on top"],
                                ["ray CD", "1 (C)", "CD with an arrow on top (start at the endpoint)"], ["line EF", "0", "EF with arrows both ways on top"]],
                            [1.5 * inch, 1.1 * inch, 3.4 * inch], width=6.0 * inch)),
     Example("Name it", "A path starts at point G, goes through H, and keeps going forever. What is it?", ["It has one endpoint (G).", "It goes on forever in one direction."], "ray GH"),
     KeyIdea("Line: no endpoints. Ray: one endpoint. Segment: two endpoints.")],
    [Problem("How many endpoints does a ray have?", "1"), Problem("A pencil's edge from tip to eraser is like a ___.", "line segment"), Problem("Name the figure: two arrows, through points P and Q.", "line PQ")],
    [S("Warm-Up", [Problem("How many sides does a triangle have?", "3"), Problem("Name a shape with 4 sides.", "square, rectangle, …")]),
     S("Name each figure", [Problem("", "line segment", fig=lambda t: line_kind(t, "segment", ("J", "K"), width=CW), space=0),
                            Problem("", "ray", fig=lambda t: line_kind(t, "ray", ("M", "N"), width=CW), space=0),
                            Problem("", "line", fig=lambda t: line_kind(t, "line", ("R", "S"), width=CW), space=0),
                            Problem("", "point", fig=lambda t: line_kind(t, "point", ("T",), width=CW), space=0)]),
     S("Draw", [Problem("Draw line segment XY.", "segment with endpoints X and Y", space=40), Problem("Draw ray BA.", "ray starting at B through A", space=40)]),
     S("Exit Ticket", [Problem("Explain the difference between a ray and a line segment.", "A ray has one endpoint and goes on forever; a segment has two endpoints.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students identify and draw points, lines, segments, and rays.", "Draw points, lines, line segments, rays, angles, and perpendicular and parallel lines; identify these in two-dimensional figures.",
       "Ruler, string, flashlight, workbook Lesson 8.1",
       flow("Name shapes.", "Read Let's Explore. Shine a flashlight; hold a string.", ["Draw each figure with a ruler and label it.", "Say: Count the endpoints."], "Try It 1–3."),
       ["Naming a ray from the wrong end."], ["Use a flashlight for rays."], ["Find 5 real-world examples of each."]),
    summary="Line: no endpoints. Ray: one endpoint. Segment: two endpoints.")

L2 = Lesson("8.2", "Parallel and Perpendicular Lines",
    "I can identify and draw parallel, perpendicular, and intersecting lines.", "4.G.1",
    [("parallel lines", "Lines that never cross and are always the same distance apart."), ("perpendicular lines", "Lines that cross to make square corners (right angles)."),
     ("intersecting lines", "Lines that cross at a point.")],
    "Look at a notebook page and a window frame. Which lines never meet? Which lines meet in square corners?",
    [Figure(lambda t: Table([[line_pair(t, "parallel"), line_pair(t, "perpendicular"), line_pair(t, "intersecting")],
                             [P("parallel", t.small), P("perpendicular", t.small), P("intersecting", t.small)]], colWidths=[W / 3] * 3)),
     Text("<b>Parallel</b> lines are like railroad tracks: they never meet. <b>Perpendicular</b> lines meet at a square corner, marked with a small square. "
          "All perpendicular lines are intersecting, but not all intersecting lines are perpendicular."),
     Example("Find them in a shape", "In a rectangle, which sides are parallel? Which are perpendicular?", ["Opposite sides never meet: parallel.", "Sides that meet at corners make right angles: perpendicular."],
             "Opposite sides are parallel; touching sides are perpendicular.", fig=poly(RECT, right_angles=[0, 1, 2, 3], width=170)),
     KeyIdea("Parallel: never meet. Perpendicular: meet at right angles.")],
    [Problem("Are the two rails of a ladder parallel or perpendicular?", "parallel"), Problem("The corner of a book shows ___ lines.", "perpendicular"), Problem("Can parallel lines intersect?", "No")],
    [S("Warm-Up", [Problem("How many endpoints does a line have?", "0"), Problem("Draw a ray.", "ray", space=24)]),
     S("Parallel, perpendicular, or intersecting?", [Problem("", k, fig=(lambda k=k: (lambda t: line_pair(t, k, width=CW, height=64)))(), space=0) for k in ["perpendicular", "parallel", "intersecting", "parallel"]]),
     S("Find in the real world", [Problem("Name something with parallel lines.", "e.g. railroad tracks, notebook lines", lines=1, space=0), Problem("Name something with perpendicular lines.", "e.g. window corner, plus sign", lines=1, space=0)]),
     S("Exit Ticket", [Problem("Draw two parallel lines and a third line perpendicular to both.", "Like a ladder rung across rails", space=60, wide=True)], cols=1)],
    TE("Students identify and draw parallel, perpendicular, and intersecting lines.", "Draw and identify perpendicular and parallel lines.", "Ruler, index card (for right angles), workbook Lesson 8.2",
       flow("Endpoints review.", "Read Let's Explore. Look around the room.", ["Draw each pair. Use an index card corner to check right angles."], "Try It 1–3."),
       ["Thinking any crossing lines are perpendicular."], ["Index card corner as a right-angle checker."], ["Find perpendicular lines in letters of the alphabet."]),
    summary="Parallel lines never meet. Perpendicular lines meet at right angles.")

L3 = Lesson("8.3", "Classifying Triangles and Quadrilaterals",
    "I can sort triangles and quadrilaterals by their sides and angles.", "4.G.2",
    [("right triangle", "A triangle with one right angle."), ("parallelogram", "A quadrilateral with two pairs of parallel sides."),
     ("trapezoid", "A quadrilateral with at least one pair of parallel sides."), ("rhombus", "A parallelogram with four equal sides.")],
    "A square is a rectangle. Is a rectangle always a square?",
    [Heading("Triangles"),
     Figure(lambda t: Table([[polygon_fig(t, TRI_RT, width=120, height=90, right_angles=[0]), polygon_fig(t, TRI_EQ, width=120, height=90, ticks=[(0, 1), (1, 1), (2, 1)]), polygon_fig(t, TRI_OB, width=120, height=90)],
                             [P("right triangle (one right angle)", t.small), P("equilateral (all sides equal; all angles acute)", t.small), P("obtuse triangle (one obtuse angle)", t.small)]], colWidths=[W / 3] * 3)),
     Heading("Quadrilaterals"),
     Figure(lambda t: Table([[polygon_fig(t, SQ, width=80, height=80, right_angles=[0, 1, 2, 3]), polygon_fig(t, RECT, width=110, height=80, right_angles=[0, 1, 2, 3]),
                              polygon_fig(t, PARA, width=110, height=80), polygon_fig(t, RHOM, width=90, height=80, ticks=[(0, 1), (1, 1), (2, 1), (3, 1)]), polygon_fig(t, TRAP, width=110, height=80)],
                             [P("square", t.small), P("rectangle", t.small), P("parallelogram", t.small), P("rhombus", t.small), P("trapezoid", t.small)]], colWidths=[W / 5] * 5)),
     Text("Shapes can belong to more than one group. A <b>square</b> has 4 right angles (so it is a rectangle), 4 equal sides (so it is a rhombus), and 2 pairs of parallel sides (so it is a parallelogram)."),
     KeyIdea("Classify by sides (equal? parallel? perpendicular?) and by angles (right, acute, obtuse).")],
    [Problem("Name a quadrilateral with 4 right angles and 4 equal sides.", "square"), Problem("Does a trapezoid always have parallel sides?", "Yes, at least one pair"), Problem("Is every rectangle a square?", "No")],
    [S("Warm-Up", [Problem("What do perpendicular lines make?", "right angles"), Problem("How many sides does a quadrilateral have?", "4")]),
     S("Name each shape (give the most exact name)", [Problem("", "right triangle", fig=poly(TRI_RT, right_angles=[0]), space=0), Problem("", "parallelogram", fig=poly(PARA), space=0),
                                                       Problem("", "trapezoid", fig=poly(TRAP), space=0), Problem("", "rhombus", fig=poly(RHOM, ticks=[(0, 1), (1, 1), (2, 1), (3, 1)]), space=0)]),
     S("True or false?", [Problem("Every square is a rectangle.", "True", choices=["True", "False"]), Problem("Every rhombus is a square.", "False", choices=["True", "False"]),
                          Problem("A triangle can have two right angles.", "False", choices=["True", "False"]), Problem("A rectangle has 2 pairs of parallel sides.", "True", choices=["True", "False"])]),
     S("Exit Ticket", [Problem("Draw a quadrilateral that is a parallelogram but not a rectangle.", "A slanted parallelogram", space=60, wide=True)], cols=1)],
    TE("Students classify triangles and quadrilaterals.", "Classify two-dimensional figures based on parallel or perpendicular lines and angles of a specified size; recognize right triangles.",
       "Paper shapes or pattern blocks, workbook Lesson 8.3",
       flow("Review.", "Read Let's Explore.", ["Sort paper shapes into groups. Discuss shapes that fit more than one group.", "Say: Which features does it have?"], "Try It 1–3."),
       ["Thinking a square is not a rectangle."], ["Use a feature checklist."], ["Make a Venn diagram of rectangles and rhombuses."]),
    summary="Sort shapes by their sides and angles. Some shapes have more than one name.")

L4 = Lesson("8.4", "Lines of Symmetry",
    "I can find and draw lines of symmetry.", "4.G.3",
    [("line of symmetry", "A line that folds a figure into two matching halves."), ("line-symmetric", "Having at least one line of symmetry.")],
    "Fold a paper heart in half. Do the two halves match exactly?",
    [Text("If you can fold a figure so the two halves match exactly, the fold line is a <b>line of symmetry</b>."),
     Figure(lambda t: Table([[polygon_fig(t, RECT, width=130, height=90, sym=((0.5, 0.05), (0.5, 0.95))), polygon_fig(t, TRI_EQ, width=130, height=90, sym=((0.5, -0.02), (0.5, 0.95))),
                              polygon_fig(t, PARA, width=130, height=90)],
                             [P("rectangle: 2 lines (one shown)", t.small), P("equilateral triangle: 3 lines (one shown)", t.small), P("parallelogram: no lines of symmetry", t.small)]], colWidths=[W / 3] * 3)),
     Example("Count lines of symmetry", "How many lines of symmetry does a square have?", ["Fold top to bottom: match.", "Fold left to right: match.", "Fold along both diagonals: match."], "4"),
     WatchOut("A diagonal fold of a rectangle (that isn't a square) does <b>not</b> make matching halves."),
     KeyIdea("Imagine folding. If the halves match exactly, it's a line of symmetry.")],
    [Problem("How many lines of symmetry does the letter A have?", "1"), Problem("Does the letter Z have a line of symmetry?", "No"), Problem("How many lines of symmetry does a circle have?", "infinitely many")],
    [S("Warm-Up", [Problem("Every square is a ___.", "rectangle (and rhombus)"), Problem("Name a shape with no right angles.", "e.g. equilateral triangle")]),
     S("Is the dashed line a line of symmetry?", [Problem("", "Yes", fig=poly(SQ, sym=((0, 0), (1, 1)), width=90, height=90), choices=["Yes", "No"], space=0), Problem("", "No", fig=poly(RECT, sym=((0, 0.15), (1, 0.85))), choices=["Yes", "No"], space=0),
                                                  Problem("", "Yes", fig=poly(TRAP, sym=((0.5, -0.05), (0.5, 0.9))), choices=["Yes", "No"], space=0), Problem("", "No", fig=poly(PARA, sym=((0.5, -0.05), (0.5, 1.05))), choices=["Yes", "No"], space=0)]),
     S("How many lines of symmetry?", [Problem("letter H", "2"), Problem("letter B", "1"), Problem("letter N", "0"), Problem("regular hexagon", "6")]),
     S("Exit Ticket", [Problem("Draw a shape with exactly one line of symmetry. Draw the line.", "e.g. a heart or an isosceles triangle", space=60, wide=True)], cols=1)],
    TE("Students identify and draw lines of symmetry.", "Recognize a line of symmetry; identify line-symmetric figures and draw lines of symmetry.", "Paper shapes to fold, mirror (optional), workbook Lesson 8.4",
       flow("Review.", "Read Let's Explore. Fold paper shapes.", ["Fold a rectangle both ways and on the diagonal.", "Say: If it matches exactly, it's symmetric."], "Try It 1–3. Weekly Check tomorrow."),
       ["Thinking the diagonal of a rectangle is a line of symmetry."], ["Fold paper."], ["Find symmetry in nature: leaves, butterflies."]),
    summary="A line of symmetry folds a figure into matching halves.")

L5 = Lesson("8.5", "Angles: Right, Acute, and Obtuse",
    "I can identify right, acute, obtuse, and straight angles.", "4.G.1, 4.G.2",
    [("angle", "Two rays that share an endpoint."), ("vertex", "The shared endpoint of an angle."), ("right angle", "A square corner, 90°."),
     ("acute angle", "Smaller than a right angle."), ("obtuse angle", "Larger than a right angle but smaller than a straight angle."), ("straight angle", "A straight line, 180°.")],
    "Open a book a little, then wider, then flat on the table. How does the corner between the covers change?",
    [Text("An <b>angle</b> is made of two rays with a shared endpoint called the <b>vertex</b>. We compare angles to a right angle (a square corner)."),
     Figure(lambda t: Table([[angle_fig(t, 50, width=130, show=False), angle_fig(t, 90, width=130, show=False), angle_fig(t, 130, width=130, show=False), angle_fig(t, 180, width=130, show=False)],
                             [P("acute", t.small), P("right", t.small), P("obtuse", t.small), P("straight", t.small)]], colWidths=[W / 4] * 4)),
     Example("Classify", "A clock shows 3:00. What kind of angle do the hands make?", ["The hands point to 12 and 3.", "That is a square corner."], "right angle"),
     KeyIdea("Use the corner of a paper as a right-angle tester: smaller is acute, bigger is obtuse.")],
    [Problem("The hands of a clock at 1:00 make what kind of angle?", "acute"), Problem("At 6:00?", "straight"), Problem("At 4:00?", "obtuse")],
    [S("Warm-Up", [Problem("What do perpendicular lines make?", "right angles"), Problem("How many lines of symmetry does a square have?", "4")]),
     S("Classify each angle", [Problem("", akind(d), fig=ang(d, show=False), space=0) for d in [35, 120, 90, 160, 70, 180]]),
     S("Exit Ticket", [Problem("Draw an acute angle and an obtuse angle. Label the vertex of each.", "drawings", space=60, wide=True)], cols=1)],
    TE("Students classify angles by comparing to a right angle.", "Draw angles; classify figures by angles.", "Index card, clock, workbook Lesson 8.5",
       flow("Review.", "Read Let's Explore with a book.", ["Make each angle with arms or two pencils. Test with an index card corner."], "Try It 1–3."),
       ["Judging angles by the length of the rays."], ["Index card corner."], ["Find each type of angle in the house."]),
    summary="Acute < right (90°) < obtuse < straight (180°).")

L6 = Lesson("8.6", "Angles and Turns",
    "I can explain angles as turns and fractions of a full circle (360°).", "4.MD.5",
    [("degree (°)", f"A unit for measuring angles. A full turn is 360°; one degree is {F(1, 360)} of a turn.")],
    "A skateboarder does a “180” and a “360.” What do those numbers mean?",
    [Text(f"An angle measures a <b>turn</b>. A full turn all the way around is 360 degrees (360°). A half turn is 180°. A quarter turn is 90°: a right angle."),
     Figure(lambda t: table(t, [["Turn", "Fraction of a circle", "Degrees"], ["quarter turn", F(1, 4), "90°"], ["half turn", F(1, 2), "180°"], ["three-quarter turn", F(3, 4), "270°"], ["full turn", "1", "360°"]],
                            [1.9 * inch, 1.8 * inch, 1.2 * inch], width=4.9 * inch)),
     Example("Fraction to degrees", f"How many degrees is {F(1, 3)} of a full turn?", ["360 ÷ 3 = 120."], "120°"),
     KeyIdea("A full circle is 360°. Find a fraction of 360 to find the angle.")],
    [Problem("How many degrees in a half turn?", "180°"), Problem(f"{F(1, 6)} of a turn is how many degrees?", "60°"), Problem("A clock's minute hand moves 15 minutes. How many degrees?", "90°")],
    [S("Warm-Up", [Problem("360 ÷ 4", "90"), Problem("360 ÷ 2", "180")]),
     S("How many degrees?", [Problem(f"{F(n, d)} turn", f"{360 * n // d}°") for n, d in [(1, 4), (3, 4), (1, 8), (1, 10), (2, 3), (1, 12)]]),
     S("Solve", [Problem("A ceiling fan blade turns 2 full turns. How many degrees?", "720°", space=30), Problem("A clock's minute hand moves from 12 to 2. How many degrees?", "60°", space=30)]),
     S("Exit Ticket", [Problem("Explain why a right angle is 90°.", "It is a quarter of a full 360° turn: 360 ÷ 4 = 90.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students relate angles to turns and degrees.", "Recognize angles as geometric shapes formed wherever two rays share a common endpoint; understand angle measurement relative to a circle.", "Paper plate with a brad and two strips, workbook Lesson 8.6",
       flow("360 ÷ 4.", "Read Let's Explore.", ["Turn your body a quarter, half, full turn.", "Build an angle maker with a paper plate."], "Try It 1–3."), ["Thinking a full turn is 100°."], ["Body turns."], ["How many degrees does the hour hand move in 1 hour? (30°)"]),
    summary="A full turn is 360°. Angles are fractions of a full turn.")

L7 = Lesson("8.7", "Estimating Angle Measures",
    "I can estimate the measure of an angle using benchmark angles of 45°, 90°, 135°, and 180°.", "4.MD.5",
    [("benchmark angle", "A familiar angle like 45°, 90°, or 180° used to estimate.")],
    "Without a tool, about how many degrees is the angle a door makes when it is half open?",
    [Text("Use benchmarks: a right angle is 90°. Half of a right angle is 45°. A right angle plus 45° is 135°. A straight line is 180°."),
     Figure(lambda t: Table([[angle_fig(t, 45, width=115), angle_fig(t, 90, width=115), angle_fig(t, 135, width=115), angle_fig(t, 180, width=115)]], colWidths=[W / 4] * 4)),
     Example("Estimate", "An angle is a bit bigger than a right angle but much smaller than a straight angle.", ["Between 90° and 180°.", "Close to the 135° benchmark? It looks a little less."], "about 120°"),
     KeyIdea("Compare to 45°, 90°, 135°, and 180° to estimate.")],
    [Problem("Is a 40° angle closer to 45° or 90°?", "45°"), Problem("Estimate an angle a little less than a straight angle.", "about 170°"), Problem("Which benchmark is closest to 100°?", "90°")],
    [S("Warm-Up", [Problem("90 ÷ 2", "45"), Problem("90 + 45", "135")]),
     S("Estimate each angle (accept within 15°)", [Problem("", f"about {d}°", fig=ang(d, show=False), space=0) for d in [45, 150, 30, 100]]),
     S("Exit Ticket", [Problem("Draw an angle of about 135°. Explain how you made it.", "A right angle plus half a right angle", space=60, wide=True)], cols=1)],
    TE("Students estimate angle measures with benchmarks.", "Understand angle measure in degrees.", "Paper plate angle maker, workbook Lesson 8.7",
       flow("90 ÷ 2.", "Read Let's Explore.", ["Fold a paper corner in half to make 45°."], "Try It 1–3."), ["Confusing acute and obtuse estimates."], ["Fold benchmark angles from paper."], ["Estimate angles in the letters of your name."]),
    summary="Estimate angles using 45°, 90°, 135°, and 180° benchmarks.")

L8 = Lesson("8.8", "Classifying Shapes by Angles",
    "I can sort shapes by their angles and tell how many right, acute, or obtuse angles they have.", "4.G.2",
    [("acute triangle", "A triangle with three acute angles."), ("obtuse triangle", "A triangle with one obtuse angle.")],
    "Can a triangle have two obtuse angles?",
    [Text("Look at each angle in a shape and classify it. Triangles are named by their largest angle."),
     Figure(lambda t: table(t, [["Triangle", "Angles"], ["acute triangle", "3 acute angles"], ["right triangle", "1 right angle, 2 acute"], ["obtuse triangle", "1 obtuse angle, 2 acute"]],
                            [2.0 * inch, 3.0 * inch], width=5.0 * inch)),
     Example("Try to draw it", "Can a triangle have two obtuse angles?", ["If two sides spread wider than a square corner at both ends, they can never meet to close the triangle."], "No"),
     KeyIdea("Every triangle has at least two acute angles.")],
    [Problem("How many right angles does a rectangle have?", "4"), Problem("A triangle has angles of 60°, 60°, 60°. What kind of triangle?", "acute (and equilateral)"), Problem("Can a triangle have 2 right angles?", "No")],
    [S("Warm-Up", [Problem("Is 95° acute or obtuse?", "obtuse"), Problem("Is 89° acute or obtuse?", "acute")]),
     S("Classify each triangle by its angles", [Problem("", "right", fig=poly(TRI_RT, right_angles=[0]), space=0), Problem("", "acute", fig=poly(TRI_EQ), space=0), Problem("", "obtuse", fig=poly(TRI_OB), space=0),
                                                Problem("Angles 30°, 60°, 90°", "right")]),
     S("Count the angles", [Problem("How many obtuse angles does a regular hexagon have?", "6 (each 120°)"), Problem("How many acute angles does a parallelogram like the one in Lesson 8.3 have?", "2")]),
     S("Exit Ticket", [Problem("Draw a quadrilateral with exactly 2 right angles.", "e.g. a right trapezoid", space=60, wide=True)], cols=1)],
    TE("Students classify shapes by angle types.", "Classify two-dimensional figures based on angles of a specified size.", "Workbook Lesson 8.8",
       flow("Acute or obtuse?", "Read Let's Explore.", ["Try to draw a triangle with two obtuse angles. Discuss why it fails."], "Try It 1–3. Weekly Check tomorrow."), ["Naming a triangle by its smallest angle."], ["Index card test for each angle."], ["Sort 8 drawn shapes by angles."]),
    summary="Name triangles by their largest angle. Every triangle has at least two acute angles.")

L9 = Lesson("8.9", "Measuring Angles with a Protractor",
    "I can use a protractor to measure angles in whole degrees.", "4.MD.6",
    [("protractor", "A tool for measuring angles in degrees.")],
    "How can we find the exact size of an angle?",
    [Text("A <b>protractor</b> is a half circle marked from 0° to 180°."),
     Bullets(["Put the center point of the protractor on the vertex.", "Line up the 0° line with one ray.", "Read where the other ray crosses the scale. Use the scale that starts at 0 on your first ray."]),
     Figure(lambda t: protractor_fig(t, 60), "This angle measures 60°."),
     WatchOut("Most protractors have two scales. If your angle is obviously acute but you read 120°, you used the wrong scale."),
     KeyIdea("Center on the vertex, zero on one ray, read the other ray. Check with an estimate.")],
    [Problem("An angle looks a little smaller than a right angle. The protractor shows 80° and 100°. Which is it?", "80°"), Problem("Where does the protractor's center go?", "on the vertex"), Problem("A straight angle measures ___.", "180°")],
    [S("Warm-Up", [Problem("Estimate a 'square corner' in degrees.", "90°"), Problem("Is 140° acute or obtuse?", "obtuse")]),
     S("Read the protractor", [Problem("", f"{d}°", fig=(lambda d=d: (lambda t: protractor_fig(t, d, width=CW)))(), space=0) for d in [40, 110, 75, 150]]),
     S("Measure with your protractor", [Problem("Draw any angle and measure it.", "Answers vary", space=60), Problem("Measure the corner of this page.", "90°", space=20)]),
     S("Exit Ticket", [Problem("Explain how you know which scale to read.", "Use the scale that starts at 0 on the first ray; check with an estimate.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students measure angles with a protractor.", "Measure angles in whole-number degrees using a protractor.", "Protractor, workbook Lesson 8.9",
       flow("Estimates.", "Read Let's Explore.", ["Model protractor placement slowly three times.", "Say: Center, zero, read."], "Try It 1–3."), ["Reading the wrong scale.", "Not putting the center on the vertex."], ["Estimate first."], ["Measure angles in a picture."]),
    summary="Center on the vertex, line up zero with one ray, and read the other ray.")

L10 = Lesson("8.10", "Drawing Angles",
    "I can draw an angle of a given measure using a protractor.", "4.MD.6",
    [],
    "How would you draw an angle of exactly 65°?",
    [Bullets(["Draw a ray. Its endpoint is the vertex.", "Place the protractor's center on the vertex and line up 0° with the ray.", "Make a dot at 65° on the scale.", "Draw a ray from the vertex through the dot. Label the angle."]),
     Figure(lambda t: protractor_fig(t, 65), "Drawing a 65° angle."),
     KeyIdea("Draw a ray, place the protractor, mark the degree, connect.")],
    [Problem("Draw a 30° angle.", "drawing"), Problem("Draw a 120° angle.", "drawing"), Problem("Draw a 90° angle. What is another name for it?", "right angle")],
    [S("Warm-Up", [Problem("Read: center, zero, ___", "read the other ray"), Problem("Is 65° acute?", "Yes")]),
     S("Draw each angle with a protractor", [Problem(f"{d}°", f"{d}° angle drawn ({akind(d)})", space=80) for d in [45, 70, 125, 160]]),
     S("Exit Ticket", [Problem("Draw a 100° angle. Is it acute, right, or obtuse?", "obtuse", space=80, wide=True)], cols=1)],
    TE("Students draw angles of specified measures.", "Sketch angles of specified measure.", "Protractor, ruler, workbook Lesson 8.10", flow("Review measuring.", "Read Let's Explore.", ["Model the four steps."], "Try It 1–3."),
       ["Drawing from the wrong side of 0."], ["Check: does it look acute or obtuse as expected?"], ["Draw a 'pie chart' with angles 90°, 120°, 150°."]), summary="Draw a ray, place the protractor, mark the degree, and draw the second ray.")

L11 = Lesson("8.11", "Adding Angle Measures",
    "I can find the measure of an angle made of smaller angles by adding.", "4.MD.7",
    [("additive", "An angle made of non-overlapping parts has a measure equal to the sum of the parts.")],
    "Two slices of pie meet at the center. One slice makes a 40° angle and the next makes 50°. What angle do they make together?",
    [Text("When an angle is split into parts that don't overlap, the whole angle equals the sum of the parts. 40° + 50° = 90°."),
     Figure(lambda t: Table([[angle_fig(t, 40, width=150), angle_fig(t, 50, width=150, start=40, label="50°")]], colWidths=[W / 2.2] * 2)),
     Example("Add parts", "An angle is split into parts of 35°, 25°, and 60°. What is the whole angle?", ["35 + 25 + 60 = 120."], "120°"),
     KeyIdea("Angle measures are additive: whole = sum of the parts.")],
    [Problem("30° + 45°", "75°"), Problem("Three 30° angles side by side make ___.", "90°"), Problem("Two right angles together make ___.", "180° (a straight angle)")],
    [S("Warm-Up", [Problem("45 + 45", "90"), Problem("180 − 90", "90")]),
     S("Find the whole angle", [Problem(" + ".join(f"{p}°" for p in ps), f"{sum(ps)}°") for ps in [(20, 70), (55, 35), (40, 40, 40), (90, 45), (15, 60, 30), (100, 80)]]),
     S("Exit Ticket", [Problem("Four equal angles fill a right angle. How big is each?", "22.5° (accept 22 ½°)", wide=True)], cols=1)],
    TE("Students add angle measures.", "Recognize angle measure as additive.", "Paper angles to cut and combine, workbook Lesson 8.11",
       flow("45 + 45.", "Read Let's Explore with paper pie slices.", ["Combine two paper angles and measure the total."], "Try It 1–3."), ["Overlapping the parts."], ["Paper wedges."], ["Make 360° from 5 different angles."]),
    summary="When angles don't overlap, add their measures to get the whole angle.")

L12 = Lesson("8.12", "Finding Unknown Angles",
    "I can find an unknown angle by adding or subtracting.", "4.MD.7",
    [],
    "A right angle is split into two parts. One part is 35°. How big is the other part?",
    [Example("Subtract from 90°", "Right angle: 35° + ? = 90°", ["90 − 35 = 55."], "55°"),
     Example("Subtract from 180°", "A straight angle is split into 110° and ?.", ["180 − 110 = 70."], "70°"),
     KeyIdea("Write an equation with a letter for the unknown: 35 + x = 90.")],
    [Problem("Right angle split into 60° and x. Find x.", "30°"), Problem("Straight angle split into 45° and x.", "135°"), Problem("Full turn split into 100°, 120°, and x.", "140°")],
    [S("Warm-Up", [Problem("90 − 25", "65"), Problem("180 − 75", "105")]),
     S("Find the unknown angle", [Problem("Right angle: 40° and x", "50°"), Problem("Right angle: 72° and x", "18°"), Problem("Straight angle: 65° and x", "115°"),
                                  Problem("Straight angle: 90°, 30°, and x", "60°"), Problem("360°: 90°, 150°, and x", "120°"), Problem("An angle of 125° is split in two. One part is 80°. The other?", "45°")]),
     S("Solve", [Problem("A ramp meets the ground at 25°. What angle does it make on the other side of the ground line (a straight angle)?", "155°", space=40, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write and solve an equation: a straight angle is split into two parts, 48° and x.", "48 + x = 180; x = 132°", space=30, wide=True)], cols=1)],
    TE("Students find unknown angles.", "Solve addition and subtraction problems to find unknown angles on a diagram; use an equation with a symbol for the unknown.", "Workbook Lesson 8.12",
       flow("90 − 25.", "Read Let's Explore.", ["Work both examples. Write equations."], "Try It 1–3. Weekly Check tomorrow."), ["Subtracting from 100 instead of 90."], ["Label 90° or 180° on the diagram first."], ["Find angles in a clock face."]),
    summary="Use 90°, 180°, or 360° and subtract the known parts to find the unknown angle.")

WORMS = [Fr(1, 4), Fr(1, 2), Fr(1, 2), Fr(3, 4), Fr(3, 4), Fr(3, 4), Fr(1), Fr(5, 4), Fr(1, 2), Fr(1)]
L13 = Lesson("8.13", "Line Plots with Fractions",
    f"I can make a line plot to show measurements in fractions of a unit ({F(1, 2)}, {F(1, 4)}, {F(1, 8)}).", "4.MD.4",
    [("line plot", "A number line with X marks that shows how many times each value appears."), ("data", "Information collected, such as measurements.")],
    "Ellie measured 10 earthworms after it rained. How can she show all the lengths in one picture?",
    [Text(f"A <b>line plot</b> shows data on a number line. Each X stands for one measurement."),
     Figure(lambda t: table(t, [["Worm lengths (inches)"], [P(", ".join(F(v.numerator, v.denominator) if v.denominator > 1 else str(v.numerator) for v in WORMS), ParagraphStyle('x', fontName='Body', fontSize=12, leading=18))]], [4.8 * inch], width=4.8 * inch)),
     Figure(lambda t: line_plot(t, WORMS, 0, Fr(3, 2), 4, title="Earthworm lengths (inches)")),
     Bullets(["Draw a number line that covers the smallest to the largest value.", "Mark it in the right fraction (here, fourths).", "Put an X above the value for each measurement.", "Give it a title and units."]),
     KeyIdea("Each X is one data value. Tall stacks show the most common values.")],
    [Problem("How many worms were 3/4 inch?".replace("3/4", F(3, 4)), "3"), Problem("What was the longest worm?", MX(1, 1, 4) + " inches"), Problem("How many worms were longer than 1/2 inch?".replace("1/2", F(1, 2)), "6")],
    [S("Warm-Up", [Problem(f"{F(2, 4)} = {F(1, '?')}", "2"), Problem(f"{F(4, 8)} = {F('?', 4)}", "2")]),
     S("Make a line plot", [Problem(f"Pencil lengths (inches): 5, {MX(5, 1, 2)}, {MX(5, 1, 4)}, 6, {MX(5, 1, 2)}, {MX(5, 3, 4)}, {MX(5, 1, 2)}, 6. Make a line plot from 5 to 6 in fourths.",
                                    f"X's: 5 (1), {MX(5, 1, 4)} (1), {MX(5, 1, 2)} (3), {MX(5, 3, 4)} (1), 6 (2)", space=100, wide=True)], cols=1),
     S("Read your line plot", [Problem("Which length is most common?", MX(5, 1, 2) + " in."), Problem("How many pencils are there?", "8")]),
     S("Exit Ticket", [Problem("Why is a line plot useful for measurements?", "It shows all values at once and which are most common.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students create line plots with fractional measurements.", "Make a line plot to display a data set of measurements in fractions of a unit (1/2, 1/4, 1/8).", "Rulers, small objects to measure, workbook Lesson 8.13",
       flow("Equivalent fractions.", "Read Let's Explore.", ["Measure 8 pencils or crayons to the nearest ¼ inch together and make a line plot."], "Try It 1–3."), ["Uneven spacing on the number line."], ["Label every tick."], ["Make a line plot of family members' shoe lengths."]),
    summary="A line plot shows each measurement as an X above a number line marked in fractions.")

L14 = Lesson("8.14", "Solving Problems with Line Plots",
    "I can add and subtract fractions to answer questions about a line plot.", "4.MD.4",
    [],
    "What is the difference between the longest and shortest earthworm? What is the total length of all the 3/4-inch worms?".replace("3/4", F(3, 4)),
    [Figure(lambda t: line_plot(t, WORMS, 0, Fr(3, 2), 4, title="Earthworm lengths (inches)")),
     Example("Difference", "Longest − shortest", [f"Longest: {MX(1, 1, 4)} = {F(5, 4)}. Shortest: {F(1, 4)}.", f"{F(5, 4)} − {F(1, 4)} = {F(4, 4)} = 1."], "1 inch"),
     Example("Total of a group", f"Total length of the {F(3, 4)}-inch worms", [f"There are 3 of them: 3 × {F(3, 4)} = {F(9, 4)} = {MX(2, 1, 4)}."], MX(2, 1, 4) + " inches"),
     KeyIdea("Use the line plot to find the values, then add, subtract, or multiply fractions.")],
    [Problem(f"Total length of the {F(1, 2)}-inch worms?", MX(1, 2, 4) + f" = {MX(1, 1, 2)} inches"), Problem("How many worms in all?", "10"), Problem(f"How much longer is the longest worm than a {F(1, 2)}-inch worm?", F(3, 4) + " inch")],
    [S("Warm-Up", [Problem(f"3 × {F(1, 4)}", F(3, 4)), Problem(f"{F(7, 8)} − {F(3, 8)}", F(4, 8))]),
     S("Use the line plot of ribbon pieces", [
         Problem("How many ribbon pieces are there?", "9", fig=lambda t: line_plot(t, [Fr(1, 8), Fr(3, 8), Fr(3, 8), Fr(1, 2), Fr(5, 8), Fr(5, 8), Fr(5, 8), Fr(7, 8), Fr(1)], 0, 1, 8, width=W - 40, title="Ribbon pieces (yards)"), space=20, wide=True),
         Problem("What is the difference between the longest and shortest piece?", F(7, 8) + " yard", space=24, wide=True),
         Problem(f"What is the total length of the {F(5, 8)}-yard pieces?", F(15, 8) + " = " + MX(1, 7, 8) + " yards", space=24, wide=True),
         Problem(f"If all the {F(3, 8)}-yard pieces are joined, how long is the new piece?", F(6, 8) + " yard", space=24, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write your own question about the ribbon line plot and answer it.", "Answers vary.", lines=2, space=0, wide=True)], cols=1)],
    TE("Students solve problems using line plot data.", "Solve problems involving addition and subtraction of fractions using information in line plots.", "Workbook Lesson 8.14",
       flow("3 × 1/4.", "Read Let's Explore.", ["Work both examples."], "Try It 1–3."), ["Counting X's wrong."], ["Cross off X's as you use them."], ["Make and answer 3 questions about your own data."]),
    summary="Read values from the line plot, then compute with fractions.")

L15 = Lesson("8.15", "Geometry Review: Attributes of Shapes",
    "I can describe shapes using lines, angles, and symmetry.", "4.G.1, 4.G.2, 4.G.3",
    [("attribute", "A feature of a shape, such as number of sides or types of angles.")],
    "Play “Guess My Shape”: I have 4 sides, 2 pairs of parallel sides, no right angles, and 4 equal sides. What am I?",
    [Text("Describe shapes by their <b>attributes</b>: number of sides, parallel and perpendicular sides, types of angles, equal sides, and lines of symmetry."),
     Example("Guess my shape", "4 sides, 2 pairs of parallel sides, no right angles, 4 equal sides.", ["Parallelogram with equal sides.", "No right angles, so not a square."], "rhombus"),
     KeyIdea("Use exact vocabulary: parallel, perpendicular, acute, right, obtuse, symmetric.")],
    [Problem("I have 3 sides and one right angle. What am I?", "right triangle"), Problem("I have 4 right angles and 2 lines of symmetry, and my sides are not all equal.", "rectangle"),
     Problem("I have exactly one pair of parallel sides.", "trapezoid")],
    [S("Warm-Up", [Problem("90° + 45°", "135°"), Problem("Is a square a rhombus?", "Yes")]),
     S("Describe each shape: parallel sides, right angles, lines of symmetry", [
         Problem("square", "2 pairs parallel, 4 right angles, 4 lines", lines=1, space=0, wide=True), Problem("equilateral triangle", "0 parallel, 0 right angles, 3 lines", lines=1, space=0, wide=True),
         Problem("rectangle (not a square)", "2 pairs parallel, 4 right angles, 2 lines", lines=1, space=0, wide=True), Problem("parallelogram (not a rectangle or rhombus)", "2 pairs parallel, 0 right angles, 0 lines", lines=1, space=0, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Write a ‘Guess My Shape’ riddle with at least 3 clues.", "Answers vary.", lines=3, space=0, wide=True)], cols=1)],
    TE("Students describe shapes using geometric attributes.", "4.G.1–3 review.", "Paper shapes, workbook Lesson 8.15",
       flow("Review.", "Read Let's Explore.", ["Play Guess My Shape with paper shapes."], "Try It 1–3."), ["Using informal words like ‘slanty’."], ["Word bank."], ["Write riddles for a sibling."]),
    summary="Describe shapes by sides, parallel and perpendicular lines, angles, and symmetry.")

L16 = Lesson("8.16", "Geometry and Data Problem Solving",
    "I can solve problems with angles, shapes, and line plots.", "4.MD.4, 4.MD.7, 4.G.2",
    [],
    "Design a kite: it must have one line of symmetry and two pairs of equal sides. What angles might it have?",
    [Text("Today you'll use everything from this unit to solve design and data problems."),
     Example("Kite angles", "A kite has angles of 110°, 70°, 110°, and x°. The four angles of a quadrilateral add to 360°.", ["110 + 70 + 110 = 290.", "360 − 290 = 70."], "x = 70°"),
     KeyIdea("Use angle facts (90°, 180°, 360°), shape attributes, and line plot data together.")],
    [Problem("Three angles of a quadrilateral are 90°, 90°, and 120°. Find the fourth.", "60°"), Problem("How many lines of symmetry does a kite have?", "1"), Problem("Can a trapezoid have a right angle?", "Yes")],
    [S("Warm-Up", [Problem("360 − 250", "110"), Problem("Name an obtuse angle measure.", "e.g. 120°")]),
     S("Solve", [Problem("A pizza is cut into 8 equal slices. What angle does each slice make at the center?", "45°", space=40, wide=True),
                 Problem("A triangle's angles add to 180°. Two angles are 50° and 60°. Find the third and classify the triangle.", "70°; acute triangle", space=40, wide=True),
                 Problem(f"Seed growth (inches): {F(1, 8)}, {F(3, 8)}, {F(3, 8)}, {F(1, 2)}, {F(5, 8)}, {F(3, 8)}. Make a line plot. What is the difference between the most and least growth?", F(4, 8) + " = " + F(1, 2) + " inch", space=90, wide=True)], cols=1),
     S("Exit Ticket", [Problem("Draw a shape with exactly one right angle and one line of symmetry.", "e.g. isosceles right triangle", space=60, wide=True)], cols=1)],
    TE("Students solve mixed geometry and data problems.", "4.MD.4, 4.MD.7, 4.G review.", "Workbook Lesson 8.16, Unit 8 Review",
       flow("360 − 250.", "Read Let's Explore. Sketch a kite.", ["Work the example."], "Try It 1–3.", "Workbook Lesson 8.16 and the Unit 8 Review.", "Check. Tomorrow: Unit 8 Test."), ["Forgetting angle totals."], ["Reference card: 90°, 180°, 360°."], ["Design and build a real kite."]),
    summary="Use angle totals, shape attributes, and line plots to solve problems.")

C1 = Check("Weekly Check 18: Lines and Shapes", [S("Show what you know", [
    Problem("Name the figure.", "ray", fig=lambda t: line_kind(t, "ray", ("P", "Q"), width=CW), space=0), Problem("Parallel, perpendicular, or intersecting?", "perpendicular", fig=lambda t: line_pair(t, "perpendicular", width=CW, height=60), space=0),
    Problem("Name the shape.", "trapezoid", fig=poly(TRAP), space=0), Problem("How many lines of symmetry does a rectangle have?", "2"),
    Problem("Is every square a rhombus?", "Yes"), Problem("Draw a right triangle.", "drawing", space=50)])], minutes=15)
C2 = Check("Weekly Check 19: Angles", [S("Show what you know", [
    Problem("Classify the angle.", "obtuse", fig=ang(130, show=False), space=0), Problem("Classify the angle.", "acute", fig=ang(40, show=False), space=0),
    Problem(f"{F(1, 4)} of a full turn = ___°", "90"), Problem(f"{F(1, 3)} of a full turn = ___°", "120"), Problem("Estimate: about how many degrees?", "about 45°", fig=ang(45, show=False), space=0), Problem("A straight angle = ___°", "180")])], minutes=15)
C3 = Check("Weekly Check 20: Measuring Angles", [S("Show what you know", [
    Problem("Read the protractor.", "130°", fig=lambda t: protractor_fig(t, 130, width=CW), space=0), Problem("Draw a 70° angle.", "drawing", space=60),
    Problem("35° + 55° = ?", "90°"), Problem("Right angle split into 28° and x. Find x.", "62°"), Problem("Straight angle split into 95° and x. Find x.", "85°"), Problem("360° split into 90°, 90°, 100°, and x.", "80°")])], minutes=20)

REVIEW = Check("Unit 8 Review", [
    S("Lines, shapes, symmetry", [Problem("How many endpoints does a line segment have?", "2"), Problem("Name a quadrilateral with exactly one pair of parallel sides.", "trapezoid"),
                                  Problem("How many lines of symmetry does a square have?", "4"), Problem("Can a triangle have two obtuse angles?", "No")]),
    S("Angles", [Problem(f"{F(1, 6)} turn = ___°", "60"), Problem("Classify a 91° angle.", "obtuse"), Problem("Right angle: 47° + x. Find x.", "43°"), Problem("Read the protractor.", "20°", fig=lambda t: protractor_fig(t, 20, width=CW), space=0)]),
    S("Line plots", [Problem(f"Plant heights: {MX(2, 1, 4)}, {MX(2, 1, 2)}, {MX(2, 1, 2)}, {MX(2, 3, 4)}, 3. Make a line plot and find the difference between the tallest and shortest.", F(3, 4) + " inch", space=90, wide=True)], cols=1)],
    kind="review", minutes=35, teacher_note="Homework or a study session before the test. Students need a protractor.")

TEST = Check("Unit 8 Test", [
    S("Part A · Lines and shapes (1 point each)", [Problem("Name the figure.", "line segment", fig=lambda t: line_kind(t, "segment", ("C", "D"), width=CW), space=0),
        Problem("Name the lines.", "parallel", fig=lambda t: line_pair(t, "parallel", width=CW, height=56), space=0), Problem("Name the shape.", "rhombus", fig=poly(RHOM, ticks=[(0, 1), (1, 1), (2, 1), (3, 1)]), space=0),
        Problem("Classify the triangle by angles.", "obtuse", fig=poly(TRI_OB), space=0), Problem("How many lines of symmetry does an equilateral triangle have?", "3"), Problem("True or false: every rectangle is a parallelogram.", "True")]),
    S("Part B · Angles (1 point each)", [Problem("Classify a 150° angle.", "obtuse"), Problem(f"{F(1, 2)} turn = ___°", "180"), Problem("Read the protractor.", "55°", fig=lambda t: protractor_fig(t, 55, width=CW), space=0),
        Problem("40° + 75° = ?", "115°"), Problem("Right angle split into 64° and x.", "26°"), Problem("Straight angle split into 30°, 60°, and x.", "90°")]),
    S("Part C · Draw (2 points each)", [Problem("Use a protractor to draw a 115° angle.", "drawing within 2°", space=80, points=2), Problem("Draw a quadrilateral with 2 pairs of parallel sides and no right angles.", "parallelogram/rhombus", space=80, points=2)]),
    S("Part D · Line plot (3 points)", [Problem(f"Bead lengths (inches): {F(1, 4)}, {F(1, 2)}, {F(1, 2)}, {F(3, 4)}, {F(1, 2)}, 1. Make a line plot. How much longer is the longest bead than the shortest? What is the total length of the {F(1, 2)}-inch beads?",
                                          f"{F(3, 4)} inch longer; total {MX(1, 2, 4)} = {MX(1, 1, 2)} inches", space=100, wide=True, points=3)], cols=1)],
    kind="test", minutes=45, teacher_note="Students need a protractor and ruler.", rubric=[["17–19 (85%+)", "Mastered."], ["14–16", "Proficient; correct missed items."], ["Below 14", "Reteach and retest."]])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16]
CHECKS = [C1, C2, C3]
WEEKS = schedule(LESSONS, ["2027-04-26", "2027-05-03", "2027-05-10", "2027-05-17"], CHECKS, REVIEW, TEST)

UNIT = Unit(8, "Geometry, Angles, and Line Plots", "Lines and rays, classifying shapes, symmetry, measuring and drawing angles, and line plots with fractions.",
    "Geometry is the math of shapes and space. You will name lines and angles, sort shapes by their attributes, find lines of symmetry, measure angles with a protractor, and show measurement data on line plots.",
    ["Draw and identify points, lines, segments, rays, and angles.", "Identify parallel and perpendicular lines.", "Classify triangles and quadrilaterals; find lines of symmetry.",
     "Measure, draw, add, and find unknown angles.", "Make and use line plots with fractional measurements."],
    [("4.G.1", "Draw points, lines, line segments, rays, angles, and perpendicular and parallel lines."), ("4.G.2", "Classify two-dimensional figures by lines and angles; recognize right triangles."),
     ("4.G.3", "Recognize and draw lines of symmetry."), ("4.MD.4", "Make a line plot of measurements in fractions of a unit; solve problems with it."),
     ("4.MD.5", "Understand angles and angle measurement in degrees."), ("4.MD.6", "Measure and sketch angles with a protractor."), ("4.MD.7", "Recognize angle measure as additive; find unknown angles.")],
    [("angle", "Two rays with a shared endpoint."), ("degree", "Unit for measuring angles."), ("parallel", "Never meet."), ("perpendicular", "Meet at right angles."),
     ("line of symmetry", "Folds a figure into matching halves."), ("line plot", "Number line with X marks for data.")],
    ["Shapes (Grade 3).", "Fractions and fraction operations (Units 5–6)."], ["Protractor", "Ruler", "Index cards (right-angle testers)", "Paper shapes", "Paper plate angle maker"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Builders check right angles, designers use symmetry, skateboarders talk in degrees, and scientists use line plots to show measurements.",
    family_note="Hunt for angles and symmetry at home and outside: roof lines, letters on signs, leaves, and tiles.",
    weeks=WEEKS)
