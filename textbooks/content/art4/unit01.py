"""Grade 4 Art · Unit 1: The Elements of Art — looking like an artist, line, shape and form, proportion, color, value and contrast,
composition, and revision (Oct 12 – Nov 6, 2026; Mon/Wed)."""
from engine import *
from content.artkit import S, MC, OR, SA, DRAW, tart, sketchbook, review, portfolio, weeks_for

# ================================================================= Week 1 · Looking and line
L1 = Lesson("1.1", "Looking Like an Artist",
    "I can look closely at artwork and describe what I see using the elements of art.", "NCAS VA:Re7, VA:Re8",
    [("elements of art", "The building blocks artists use: line, shape, form, color, value, texture, and space."), ("observe", "To look closely and carefully."),
     ("artwork", "Something an artist makes, such as a painting, sculpture, or print.")],
    "Look at any picture on your wall for one whole minute without talking. What did you notice in the last 30 seconds that you missed at first?",
    [Text("Artists are expert lookers. Before they make art, they spend a lot of time <b>observing</b>: noticing shapes, colors, and tiny details most people walk past. When we talk about art, we use the <b>elements of art</b>, the building blocks every artist uses."),
     Figure(lambda t: table(t, [["Element", "What it is"], ["line", "a mark that moves from one point to another"], ["shape", "a flat area with edges (2-D)"], ["form", "a shape with depth, like a ball or box (3-D)"],
                                ["color", "what we see when light reflects off something: red, blue, yellow, and more"], ["value", "how light or dark something is"], ["texture", "how something feels, or looks like it would feel"],
                                ["space", "the area around, between, and inside things"]], [1.3 * inch, 4.4 * inch], width=5.7 * inch)),
     Text("<b>Walter Anderson</b> (1903–1965) was an artist from Ocean Springs, Mississippi. He rowed a small boat out to Horn Island in the Gulf of Mexico and spent days drawing and painting the birds, crabs, plants, and waves he found there. He looked so closely that his watercolors seem to move. He's a great example of an artist who learned by observing."),
     Example("See, Think, Wonder", "Use these three steps to look at any artwork.",
             ["<b>See:</b> What do you see? Name only what is really there (colors, lines, objects).", "<b>Think:</b> What do you think is going on? Why?", "<b>Wonder:</b> What questions do you have?"],
             "Slow, careful looking first; ideas and questions second."),
     Investigate("Nature Observation Sketch", "How much can you notice in 10 minutes?", ["pencil", "sketchbook or paper", "a leaf, flower, shell, or pinecone"],
                 ["Set your object in front of you.", "Look for one full minute before you draw.", "Draw it slowly, looking at the object more than at your paper.", "Add three labels for details you noticed (veins, spots, edges)."],
                 record="your sketch with three labeled details."),
     KeyIdea("Artists look closely first. The elements of art (line, shape, form, color, value, texture, space) give us words for what we see.")],
    [Problem("Name three elements of art.", "any three of line, shape, form, color, value, texture, space"), Problem("Where did Walter Anderson go to draw nature?", "Horn Island, in the Gulf of Mexico"),
     Problem("What are the three steps of See, Think, Wonder?", "see what's there, think about what's going on, wonder (ask questions)")],
    [S("Warm-Up", [SA("To look closely and carefully", "observe"), SA("How light or dark something is", "value")], cols=2),
     S("Look and Describe", [OR("Choose an artwork (a book illustration, a museum website, or art in your home). Write one See, one Think, and one Wonder.", "Answers vary.", lines=4)]),
     S("Sketch", [DRAW("Draw your nature object from observation. Label three details.", "Look for careful observation and three labeled details.", space=260)]),
     S("Exit Ticket", [OR("Which element of art did you notice most in your object? Why?", "Answers vary.", lines=2)])],
    tart("Students observe closely and describe art using the elements.", "Perceive and analyze artistic work; interpret intent and meaning.", "Sketchbook, pencils, natural objects, workbook Lesson 1.1",
         "One-minute silent looking.", ["Introduce the seven elements.", "Model See, Think, Wonder with any artwork."], "Nature Observation Sketch.",
         ["Drawing from memory instead of observation."], ["Use a viewfinder (a paper frame) to focus on one part."], ["Draw the same object from three angles."]),
    summary="Look closely; use the elements of art to describe what you see.")

L2 = Lesson("1.2", "Line",
    "I can create different kinds of lines and use them to show movement and feeling.", "NCAS VA:Cr1, VA:Cr2",
    [("line", "A mark that moves from one point to another."), ("contour line", "A line that shows the outside edge of a shape."), ("implied line", "A line we imagine, like the path your eye follows.")],
    "Draw a line that looks calm. Now draw a line that looks excited. What's different?",
    [Text("Line is the first element most artists use. Lines can be straight, curved, zigzag, wavy, spiral, dotted, thick, or thin. Lines also carry <b>feelings</b>: flat <b>horizontal</b> lines feel calm and restful, tall <b>vertical</b> lines feel strong, and slanted <b>diagonal</b> lines feel full of movement."),
     Figure(lambda t: Draw(W * 0.85, 92, lambda c, w, h: _line_sampler(c, w, h, t))),
     Text("In <b>The Starry Night</b> (1889), Vincent van Gogh used thick, swirling, curving lines to make the night sky look like it is moving. Find a picture of it online or in a library book and trace the swirls with your finger."),
     Investigate("Line Sampler and Line Feelings", "How can lines show feelings?", ["pencil", "black marker", "paper"],
                 ["Fold a paper into eight boxes.", "Fill each box with a different kind of line (straight, curved, zigzag, wavy, spiral, dotted, thick, thin).", "On a new paper, draw a simple landscape using only lines that feel calm.",
                  "Draw the same landscape again using only lines that feel stormy."], record="both landscapes and a sentence about which lines you chose."),
     KeyIdea("Lines can be many kinds, and their direction and shape carry feeling: horizontal = calm, vertical = strong, diagonal = movement.")],
    [Problem("What feeling do horizontal lines often show?", "calm, rest"), Problem("What kind of line shows the outside edge of a shape?", "contour line"), Problem("What kind of lines did van Gogh use in the sky?", "swirling, curving lines")],
    [S("Warm-Up", [SA("Lines that slant", "diagonal"), SA("Lines that go straight up and down", "vertical")], cols=2),
     S("Sketch", [DRAW("Line sampler: fill each part of this space with a different kind of line. Label each one.", "At least eight labeled line types.", space=200),
                  DRAW("Draw a tree using only zigzag and spiral lines.", "Creative use of the two line types.", space=200)]),
     S("Exit Ticket", [OR("Which kind of line would you use to show a race car? Why?", "Diagonal or zigzag lines, because they show speed and movement.", lines=2)])],
    tart("Students create and use expressive lines.", "Generate and develop artistic ideas.", "Pencils, markers, paper, workbook Lesson 1.2",
         "Calm line vs excited line.", ["Demonstrate eight kinds of line.", "Discuss line direction and feeling; show The Starry Night."], "Line Sampler and Line Feelings.",
         ["Pressing too hard so lines can't vary."], ["Show thick vs thin by changing pressure."], ["Make a line drawing of music as it plays."]),
    summary="Lines vary in type and direction, and they carry feeling.")


def _line_sampler(c, w, h, t):
    kinds = ["straight", "curved", "zigzag", "wavy", "spiral", "dotted", "thick", "thin"]
    cw = w / 8
    for i, k in enumerate(kinds):
        x0 = i * cw + 6; x1 = (i + 1) * cw - 6; y = h / 2 + 6
        c.setStrokeColor(INK); c.setLineWidth(4 if k == "thick" else (0.6 if k == "thin" else 1.6)); c.setDash()
        if k in ("straight", "thick", "thin"): c.line(x0, y, x1, y)
        elif k == "dotted": c.setDash(1, 4); c.line(x0, y, x1, y); c.setDash()
        elif k == "curved":
            p = c.beginPath(); p.moveTo(x0, y - 10); p.curveTo(x0 + 10, y + 25, x1 - 10, y + 25, x1, y - 10); c.drawPath(p, stroke=1, fill=0)
        elif k == "zigzag":
            p = c.beginPath(); p.moveTo(x0, y)
            for j in range(1, 6): p.lineTo(x0 + (x1 - x0) * j / 5, y + (12 if j % 2 else -12))
            c.drawPath(p, stroke=1, fill=0)
        elif k == "wavy":
            p = c.beginPath()
            for j in range(41):
                xx = x0 + (x1 - x0) * j / 40; yy = y + 8 * math.sin(j / 40 * 4 * math.pi); (p.moveTo if j == 0 else p.lineTo)(xx, yy)
            c.drawPath(p, stroke=1, fill=0)
        elif k == "spiral":
            p = c.beginPath(); cx = (x0 + x1) / 2
            for j in range(120):
                a = j / 120 * 6 * math.pi; r = 1 + j / 120 * 16; (p.moveTo if j == 0 else p.lineTo)(cx + r * math.cos(a), y + r * math.sin(a))
            c.drawPath(p, stroke=1, fill=0)
        text(c, (x0 + x1) / 2, 6, k, "BodySemi", 8, t.accent, "c")


# ================================================================= Week 2 · Shape, form, proportion
L3 = Lesson("1.3", "Shape and Form",
    "I can tell shapes from forms, sort shapes as geometric or organic, and use shading to make a shape look 3-D.", "NCAS VA:Cr2",
    [("geometric shape", "A shape with exact, regular edges, like a circle, square, or triangle."), ("organic shape", "A free-flowing shape like those found in nature, such as a leaf or a puddle."),
     ("form", "An object with three dimensions: height, width, and depth."), ("shading", "Adding darker values to show where light doesn't reach.")],
    "Is a circle the same as a ball? How could you draw a circle so it looks like a ball?",
    [Text("<b>Shapes</b> are flat (two-dimensional). <b>Geometric shapes</b> have exact edges; <b>organic shapes</b> are free and irregular, like things in nature. <b>Forms</b> are three-dimensional: a circle becomes a sphere, a square becomes a cube, a triangle becomes a cone or pyramid."),
     Figure(lambda t: table(t, [["Shape (2-D)", "Form (3-D)"], ["circle", "sphere (ball)"], ["square", "cube (box)"], ["rectangle", "cylinder or rectangular prism"], ["triangle", "cone or pyramid"]],
                            [2.6 * inch, 2.6 * inch], width=5.2 * inch)),
     Text("In his last years, <b>Henri Matisse</b> “drew with scissors,” cutting bold organic shapes from painted paper, as in <b>The Snail</b> (1953). Artists can also turn a flat shape into a form by <b>shading</b>: darker values on the side away from the light."),
     Figure(lambda t: shaded_sphere(t, width=W * 0.6, labels=False), caption="Shading turns a flat circle into a round form."),
     Investigate("From Shape to Form", "How can shading make a shape look three-dimensional?", ["pencil", "paper", "a ball or orange and a lamp or window light"],
                 ["Draw a circle. Decide where the light is coming from.", "Shade the side away from the light darker, blending smoothly.", "Leave a small bright spot (highlight) near the light side.", "Add a shadow on the ground under the ball."],
                 record="your shaded sphere and a flat circle side by side."),
     KeyIdea("Shapes are flat; forms have depth. Shading on the side away from the light turns a shape into a form.")],
    [Problem("Geometric or organic: a leaf", "organic"), Problem("What form does a circle become?", "a sphere"), Problem("Where does shading go?", "on the side away from the light")],
    [S("Warm-Up", [SA("Flat, with edges", "shape"), SA("Has height, width, and depth", "form")], cols=2),
     S("Sort", [SA(q, a) for q, a in [("puddle", "organic"), ("stop sign", "geometric"), ("cloud", "organic"), ("window", "geometric")]], cols=2),
     S("Sketch", [DRAW("Draw and shade a sphere, a cube, and a cylinder. Show where the light comes from.", "Shading consistent with one light source.", space=220)]),
     S("Exit Ticket", [OR("Why did Matisse's cut-outs use mostly organic shapes, do you think?", "Answers vary; e.g., they feel lively and natural, like plants and sea creatures.", lines=2)])],
    tart("Students distinguish shape and form and shade forms.", "Organize and develop artistic ideas and work.", "Pencils, paper, ball, lamp, workbook Lesson 1.3",
         "Circle vs ball.", ["Demonstrate shading a sphere.", "Show Matisse cut-outs."], "From Shape to Form.",
         ["Shading all around the edge evenly (looks flat)."], ["Mark the light source with an arrow first."], ["Make a Matisse-style cut-paper collage."]),
    summary="Shapes are flat; shading makes forms look 3-D.")

L4 = Lesson("1.4", "Proportion",
    "I can use proportion to draw a face with parts in the right size and place.", "NCAS VA:Cr2, VA:Cr3",
    [("proportion", "How the sizes of parts compare with each other and with the whole."), ("scale", "The size of something compared with something else."), ("portrait", "A picture of a person, often the face.")],
    "Where are your eyes on your head: near the top, or halfway down? Make a guess, then check in a mirror with a ruler.",
    [Text("<b>Proportion</b> means the size relationships between parts. Most people draw eyes too high! On most faces, the eyes are about <b>halfway</b> between the top of the head and the chin. Artists use guidelines to place features."),
     Beside(lambda t: face_guide(t, width=140, height=180),
            ["<b>Face guide:</b> draw an oval. A line halfway down shows where the eyes go.", "The bottom of the nose is about halfway between the eyes and the chin.", "The mouth is about one-third of the way from the nose to the chin.",
             "Eyes are about one eye-width apart."], fig_w=0.45),
     Text("Artists sometimes break proportion on purpose. Cartoonists draw big heads and huge eyes to look cute or funny. That's called <b>exaggeration</b>."),
     Investigate("Proportional Self-Portrait", "Can guidelines help you draw a face that looks right?", ["pencil", "eraser", "mirror", "paper"],
                 ["Draw a large oval. Lightly draw the halfway line and a center line.", "Place the eyes on the halfway line, one eye-width apart.", "Add the nose and mouth using the guide.", "Look in the mirror to add hair, ears (between the eye line and nose line), and details.", "Erase the guidelines."],
                 record="your self-portrait."),
     KeyIdea("Proportion is size relationships. Eyes sit about halfway down the head.")],
    [Problem("Where are the eyes on most faces?", "about halfway down the head"), Problem("Where do the ears usually line up?", "between the eye line and the bottom of the nose"), Problem("What is exaggeration?", "changing proportion on purpose for effect")],
    [S("Warm-Up", [SA("A picture of a person", "portrait"), SA("Size relationships between parts", "proportion")], cols=2),
     S("Sketch", [DRAW("Draw a face using the face guide steps.", "Eyes at halfway line; nose and mouth placed with guides.", space=260)]),
     S("Exit Ticket", [OR("What surprised you about where facial features go?", "Answers vary; most notice eyes are lower than expected.", lines=2)])],
    tart("Students use proportion guidelines to draw a face.", "Develop and refine artistic work.", "Pencils, erasers, mirrors, workbook Lesson 1.4",
         "Where are your eyes?", ["Demonstrate the face guide step by step."], "Proportional Self-Portrait.",
         ["Drawing eyes high on the head; drawing guidelines too dark."], ["Pre-drawn ovals with guidelines."], ["Draw a family member using the same guide."]),
    summary="Use guidelines: eyes halfway, nose and mouth below.")

# ================================================================= Week 3 · Color, value, contrast
L5 = Lesson("1.5", "Color",
    "I can name primary, secondary, and tertiary colors and mix secondary colors.", "NCAS VA:Cr2",
    [("primary colors", "Red, yellow, and blue: colors that can't be made by mixing other paints."), ("secondary colors", "Orange, green, and violet: made by mixing two primary colors."),
     ("tertiary colors", "Colors made by mixing a primary and a neighboring secondary color, like blue-green."), ("color wheel", "A circle that shows how colors relate.")],
    "If you only had red, yellow, and blue paint, how many colors could you make?",
    [Text("The painter's color wheel starts with three <b>primary colors</b>: red, yellow, and blue. Mix two primaries to get a <b>secondary color</b>: red + yellow = orange, yellow + blue = green, blue + red = violet. Mix a primary with a neighboring secondary to get a <b>tertiary color</b>, such as yellow-green or red-violet."),
     Figure(lambda t: color_wheel(t, size=180)),
     Example("Mix a secondary color", "Make green.",
             ["Put a small puddle of yellow on your palette.", "Add a tiny bit of blue and mix. (Blue is strong; add it a little at a time.)", "Keep adding blue until you like the green."],
             "Start with the lighter color and add the darker color slowly."),
     Investigate("Paint a Color Wheel", "Can you make every color on the wheel from three primaries?", ["red, yellow, and blue paint", "brush", "water cup", "paper towel", "paper plate palette", "the workbook color wheel template"],
                 ["Paint the three primary colors in their spaces.", "Mix and paint the three secondary colors.", "Mix and paint the six tertiary colors.", "Clean your brush between colors."],
                 record="your finished 12-part color wheel."),
     KeyIdea("Primary colors mix to make secondary colors; primary + neighboring secondary makes tertiary colors.")],
    [Problem("Red + yellow = ?", "orange"), Problem("Name the three primary colors.", "red, yellow, blue"), Problem("Name a tertiary color.", "e.g. yellow-green, blue-violet, red-orange")],
    [S("Warm-Up", [SA("Yellow + blue =", "green"), SA("Blue + red =", "violet (purple)")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Primary or secondary: orange", "secondary"), ("Primary or secondary: blue", "primary"), ("Yellow + green =", "yellow-green (tertiary)"), ("Which primary is not in green?", "red")]], cols=2),
     S("Create", [DRAW("Color wheel template: paint or color all 12 parts in order.", "Correct order: yellow, yellow-orange, orange, red-orange, red, red-violet, violet, blue-violet, blue, blue-green, green, yellow-green.", space=230)]),
     S("Exit Ticket", [OR("Why should you add dark colors to light colors a little at a time?", "Dark colors are strong and can quickly overpower a light color.", lines=2)])],
    tart("Students identify and mix colors.", "Organize and develop artistic ideas and work.", "Red/yellow/blue paint, brushes, water, palettes, workbook Lesson 1.5",
         "How many colors from three?", ["Demonstrate mixing green and orange."], "Paint a Color Wheel.",
         ["Muddy colors from dirty brushes."], ["Pre-labeled wheel template."], ["Mix three different greens and compare them."]),
    summary="Primaries mix into secondaries and tertiaries on the color wheel.")

L6 = Lesson("1.6", "Value and Contrast",
    "I can make tints and shades, create a value scale, and use contrast to make something stand out.", "NCAS VA:Cr2, VA:Re7",
    [("value", "How light or dark a color is."), ("tint", "A color made lighter by adding white."), ("shade", "A color made darker by adding black."),
     ("contrast", "A big difference between parts, such as light next to dark."), ("complementary colors", "Colors opposite each other on the color wheel.")],
    "Why are stop signs red and white, and school buses yellow and black?",
    [Text("<b>Value</b> is lightness or darkness. Add white to make a <b>tint</b>; add black to make a <b>shade</b>. A <b>value scale</b> shows the steps from light to dark."),
     Figure(lambda t: value_scale(t, steps=7)), Figure(lambda t: value_scale(t, steps=7, color="#1F5FAD", labels=("tints", "shades")), caption="Tints and shades of blue."),
     Text("<b>Contrast</b> is a big difference, and it grabs attention. Light next to dark is high contrast. <b>Complementary colors</b>, which sit opposite each other on the color wheel (red and green, blue and orange, yellow and violet), also make strong contrast."),
     Investigate("High-Contrast Picture", "How can contrast make one thing stand out?", ["paint or colored pencils", "black and white paint or pencils", "paper"],
                 ["Make a 5-step value scale of one color, from tint to shade.", "Draw a simple subject (a fish, a flower, a rocket).", "Color the subject with one color and the background with its complement.", "Check: does your subject pop out?"],
                 record="your value scale and your high-contrast picture."),
     KeyIdea("Tints are lighter, shades are darker; contrast (light vs dark, or complements) makes things stand out.")],
    [Problem("What do you add to make a tint?", "white"), Problem("What is the complement of blue?", "orange"), Problem("Why are school buses yellow and black?", "high contrast is easy to see")],
    [S("Warm-Up", [SA("Lightness or darkness", "value"), SA("Color + black =", "shade")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Complement of red", "green"), ("Complement of yellow", "violet"), ("Pink is a ___ of red.", "tint"), ("Navy is a ___ of blue.", "shade")]], cols=2),
     S("Create", [DRAW("Make a 5-step value scale with your pencil, from lightest to darkest.", "Five clearly different, evenly stepped values.", space=90),
                  DRAW("Sketch a subject that stands out using contrast.", "Clear contrast between subject and background.", space=200)]),
     S("Exit Ticket", [OR("Name a place you see contrast used to get attention (a sign, a logo, a jersey).", "Answers vary.", lines=2)])],
    tart("Students create value scales and use contrast.", "Organize and develop artistic work; perceive artistic choices.", "Paint or colored pencils, workbook Lesson 1.6",
         "Stop signs and buses.", ["Demonstrate tints and shades.", "Show complements on the color wheel."], "High-Contrast Picture.",
         ["Big jumps between values instead of even steps."], ["Use only pencil pressure for value."], ["Paint a monochromatic (one-color) picture using only tints and shades."]),
    summary="Value is light and dark; contrast makes parts stand out.")

# ================================================================= Week 4 · Composition and revision
L7 = Lesson("1.7", "Composition",
    "I can plan a composition with a clear focal point and balance.", "NCAS VA:Cr1, VA:Cr2",
    [("composition", "How the parts of an artwork are arranged."), ("focal point", "The part of an artwork your eye goes to first."), ("balance", "How visual weight is spread out; symmetrical or asymmetrical."),
     ("thumbnail sketch", "A small, quick drawing to plan an idea.")],
    "When you take a photo, do you always put the main thing right in the middle? What happens if you don't?",
    [Text("<b>Composition</b> is how an artist arranges everything in the picture. A strong composition has a <b>focal point</b>, the spot your eye goes to first, and <b>balance</b>. Symmetrical balance is the same on both sides; asymmetrical balance uses different things that feel equally weighted."),
     Beside(lambda t: rule_of_thirds(t, width=190, height=125),
            ["Many artists place the focal point a little off center. Divide the picture into thirds both ways; the four places where the lines cross are strong spots for a focal point.",
             "In <b>The Great Wave off Kanagawa</b> (about 1831), the Japanese artist Katsushika Hokusai placed a huge curling wave on the left and a tiny Mount Fuji low in the middle, framed by the wave."], fig_w=0.4),
     Investigate("Thumbnail Planning", "Which arrangement makes the strongest picture?", ["pencil", "paper"],
                 ["Choose a subject: your pet, your house, or a favorite place.", "Draw four small boxes (thumbnails).", "Sketch the subject a different way in each: centered, off center, close up, far away.", "Circle the strongest one and explain why."],
                 record="four thumbnails with your choice circled."),
     KeyIdea("Plan the arrangement: choose a focal point (often off center), balance the picture, and try ideas small first.")],
    [Problem("What is a focal point?", "the part your eye goes to first"), Problem("What kind of balance is the same on both sides?", "symmetrical"), Problem("What is a thumbnail sketch?", "a small, quick planning drawing")],
    [S("Warm-Up", [SA("How parts are arranged", "composition"), SA("Balance that is different on each side but still feels even", "asymmetrical")], cols=2),
     S("Sketch", [DRAW("Draw four thumbnail sketches of one subject. Circle your best composition.", "Four varied thumbnails; one circled with a reason.", space=260)]),
     S("Exit Ticket", [OR("Why do artists make thumbnails before a final piece?", "To try ideas quickly and choose the strongest one before spending time on a final.", lines=2)])],
    tart("Students plan compositions using thumbnails.", "Generate and conceptualize artistic ideas.", "Pencils, paper, workbook Lesson 1.7",
         "Photos and the middle.", ["Show rule of thirds; discuss The Great Wave."], "Thumbnail Planning.",
         ["Making thumbnails too detailed."], ["Pre-drawn thumbnail boxes."], ["Take four photos of one object using different compositions."]),
    summary="Plan with thumbnails; choose a focal point and balance.")

L8 = Lesson("1.8", "Revision and Kind, Specific Feedback",
    "I can give and use kind, specific, helpful feedback to improve my artwork.", "NCAS VA:Cr3, VA:Re9",
    [("revise", "To change and improve your work."), ("feedback", "Comments that help someone improve."), ("critique", "A thoughtful discussion of artwork.")],
    "What's more helpful: “It's good!” or “The eyes look great; maybe make the background darker so your face stands out”?",
    [Text("Artists rarely get it right the first time. They make drafts, get <b>feedback</b>, and <b>revise</b>. Good feedback is <b>kind</b> (respectful), <b>specific</b> (names exactly what to look at), and <b>helpful</b> (gives an idea to try)."),
     Text("In a well-known video called <b>Austin's Butterfly</b>, a first grader named Austin draws a butterfly six times. After each draft, classmates give kind, specific feedback, and his final drawing is amazingly detailed. Watch it with your teacher if you can."),
     Figure(lambda t: table(t, [["Instead of…", "Try…"], ["“I like it.”", "“I like how your wavy lines make the water look like it's moving.”"], ["“It's bad.”", "“The house is small; could you make it bigger so it's the focal point?”"],
                                ["“Fix the colors.”", "“Try a complementary color behind the bird so it stands out.”"]], [2.0 * inch, 3.8 * inch], width=5.8 * inch)),
     Investigate("Draft, Feedback, Final", "How much can feedback improve a drawing?", ["your best thumbnail from Lesson 1.7", "paper", "colored pencils or paint"],
                 ["Make a larger draft from your thumbnail.", "Ask your teacher or a family member for one kind, specific, helpful comment.", "Revise based on the feedback.", "Add color, using value and contrast.", "Put your draft and final side by side."],
                 record="your draft, the feedback, and your final piece for your portfolio."),
     KeyIdea("Kind, specific, helpful feedback plus revision makes art (and everything else) better.")],
    [Problem("Name the three parts of good feedback.", "kind, specific, helpful"), Problem("What did Austin do to improve his butterfly?", "made several drafts and used classmates' feedback"), Problem("What does revise mean?", "to change and improve your work")],
    [S("Warm-Up", [SA("To change and improve", "revise"), SA("A thoughtful discussion of art", "critique")], cols=2),
     S("Practice", [OR("Rewrite “It's nice” as kind, specific, helpful feedback for a picture of a dog.", "e.g. I like the fluffy texture of the fur; maybe add a shadow under the dog so it looks like it's standing on the ground.", lines=3)]),
     S("Create", [DRAW("Final piece: draw your revised composition here (or attach your painting).", "Shows revision from draft; uses line, shape, color, value, and composition.", space=260)]),
     S("Exit Ticket", [OR("What feedback did you use, and how did it change your art?", "Answers vary.", lines=2)])],
    tart("Students give feedback and revise artwork.", "Refine and complete artistic work; apply criteria to evaluate work.", "Thumbnails, paper, color media, workbook Lesson 1.8, Unit 1 Review",
         "Helpful vs unhelpful comments.", ["Show Austin's Butterfly if available.", "Model kind, specific, helpful feedback."], "Draft, Feedback, Final.",
         ["Feedback that is only praise."], ["Feedback sentence starters."], ["Give feedback on a sibling's work."], reflect="Students compare draft and final; store both in the portfolio. Friday: Unit 1 Portfolio Review."),
    summary="Get kind, specific, helpful feedback, then revise.")

# ================================================================= checks
C1 = sketchbook("Sketchbook Check 1: Looking and Line", [S("Show what you know", [
    SA("Name four elements of art.", "any four of line, shape, form, color, value, texture, space"), SA("Feeling of horizontal lines", "calm"), SA("Feeling of diagonal lines", "movement"),
    DRAW("Draw three different kinds of lines and label them.", "Three correctly labeled line types.", space=110)], cols=1)])
C2 = sketchbook("Sketchbook Check 2: Shape, Form, and Proportion", [S("Show what you know", [
    SA("Geometric or organic: a flower", "organic"), SA("A circle as a form is a…", "sphere"), SA("Where are the eyes on most faces?", "about halfway down the head"),
    DRAW("Draw and shade a sphere with a light source.", "Shading opposite the light; highlight; cast shadow.", space=130)], cols=1)])
C3 = sketchbook("Sketchbook Check 3: Color and Value", [S("Show what you know", [
    SA("Blue + yellow =", "green"), SA("Complement of orange", "blue"), SA("Color + white =", "tint"), SA("Name a tertiary color.", "e.g. red-violet"),
    DRAW("Make a 5-step value scale.", "Even steps from light to dark.", space=80)], cols=1)])

REVIEW = review("Unit 1 Review", [
    S("Words", [SA(q, a) for q, a in [("line", "a mark from one point to another"), ("form", "3-D object"), ("proportion", "size relationships"), ("value", "lightness or darkness"),
                                      ("contrast", "a big difference, such as light vs dark"), ("focal point", "where the eye goes first")]], cols=2),
    S("Portfolio", [OR("Gather your best work from Unit 1. Which piece shows the most growth? Why?", "Answers vary.", lines=3)])])

TEST = portfolio("Unit 1 Portfolio Review", [
    S("Part A · Elements of art (1 point each)", [
        MC("Which is a form?", ["circle", "sphere", "square"], 1), MC("Red, yellow, and blue are…", ["secondary colors", "primary colors", "tertiary colors"], 1),
        SA("What does adding black make?", "a shade"), SA("Which line direction shows calm?", "horizontal"),
        SA("Name the complement of violet.", "yellow"), SA("Where should a focal point often go?", "a little off center (on a rule-of-thirds spot)")], cols=1),
    S("Part B · Look and describe (3 points)", [OR("Choose one artwork from this unit (The Starry Night, The Snail, The Great Wave, or a Walter Anderson painting). Describe how the artist used two elements of art.",
                                                   "Rubric: names two elements (1); accurate details from the artwork (1); explains the effect (1).", lines=5, points=3)]),
    S("Part C · Portfolio (6 points)", [OR("Choose your final piece from Lesson 1.8. Your teacher will score it with this rubric. Then write two sentences about your choices.",
                                           "Rubric (1 point each): clear focal point; varied line; shapes and forms; color mixing; value or contrast; evidence of revision from draft.", lines=4, points=6)])],
    labels=["Excellent: strong skills and thoughtful choices.", "Solid: revisit one technique.", "Redo one studio activity with support."])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
CHECKS = [C1, C2, C3]
WEEKS = weeks_for(1, LESSONS, CHECKS, REVIEW, TEST)

UNIT = Unit(1, "The Elements of Art", "Looking like an artist, line, shape and form, proportion, color, value and contrast, composition, and revision.",
    "Every artwork, from a cave painting to a cartoon, is built from the same ingredients: line, shape, form, color, value, texture, and space. In this unit you'll learn to look like an artist, then practice each element in your own work, plan a composition, and use feedback to make a finished piece for your portfolio.",
    ["Observe and describe art using the elements of art.", "Use line, shape, form, and proportion in drawings.", "Mix colors, make value scales, and use contrast.", "Plan compositions and revise with feedback."],
    [("NCAS VA:Cr1–3", "Generate, develop, and refine artwork."), ("NCAS VA:Re7–9", "Perceive, interpret, and evaluate art.")],
    [("elements of art", "Line, shape, form, color, value, texture, space."), ("proportion", "Size relationships."), ("primary colors", "Red, yellow, blue."), ("contrast", "A big difference that stands out."),
     ("composition", "How parts are arranged."), ("revise", "Change and improve.")],
    ["Using pencils, crayons, and paint."], ["Sketchbook and drawing pencils", "Red, yellow, blue, black, and white paint; brushes; palettes", "Colored pencils and markers", "Mirror", "Portfolio folder"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Designers, illustrators, architects, and photographers use the elements of art every day, and so does anyone who arranges a poster, a room, or a plate of food.",
    family_note="Visit the Walter Anderson Museum of Art in Ocean Springs, or look at his work online, and play See, Think, Wonder together.",
    weeks=WEEKS)
