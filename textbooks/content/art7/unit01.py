"""Grade 7 Art · Unit 1: The Elements of Art — critique method, line and mark-making, form and light, proportion, color schemes,
value and chiaroscuro, composition, and revision with an artist statement (Oct 12 – Nov 6, 2026; Mon/Wed)."""
from engine import *
from content.artkit import S, MC, OR, SA, DRAW, tart, sketchbook, review, portfolio, weeks_for

# ================================================================= Week 1 · Looking and mark-making
L1 = Lesson("1.1", "Looking Closely: The Four-Step Critique",
    "I can analyze an artwork using describe, analyze, interpret, and judge.", "NCAS VA:Re7, VA:Re8, VA:Re9",
    [("elements of art", "Line, shape, form, color, value, texture, and space."), ("principles of design", "How artists arrange the elements: balance, contrast, emphasis, movement, pattern, rhythm, unity, and proportion."),
     ("critique", "A structured, thoughtful discussion of an artwork."), ("interpret", "To explain what an artwork means or expresses.")],
    "Why do people disagree about whether an artwork is “good”? Can an opinion about art be supported with evidence?",
    [Text("Art critic Edmund Feldman described a four-step method that moves from facts to opinions, so judgments rest on evidence:"),
     Figure(lambda t: flow_fig(t, ["Describe: what do you see? (facts only)", "Analyze: how are the elements and principles used?", "Interpret: what does it mean or express?", "Judge: is it successful? Why?"], height=62)),
     Text("Practice on <b>The Migration Series</b> (1940–41) by <b>Jacob Lawrence</b>, a set of 60 small paintings about the Great Migration of African Americans from the rural South to Northern cities, the same history you read about in ELA. Lawrence used a limited palette of bold, flat colors and repeated shapes, so the whole series reads like one story. Many panels can be viewed online through the Phillips Collection and the Museum of Modern Art, which each own half of the series."),
     Example("Critique one panel", "Choose any panel from The Migration Series.",
             ["Describe: list figures, objects, colors, and words in the caption.", "Analyze: find repeated shapes, strong diagonals, or the limited color palette.", "Interpret: what feeling or message does the panel express about the migration?",
              "Judge: does it communicate that message well? Give evidence from steps 1–3."],
             "A judgment that grows from description and analysis is persuasive, even if others disagree."),
     Investigate("Critique Practice", "Can you support an opinion about art with evidence?", ["internet access or an art book", "sketchbook"],
                 ["Choose one Migration Series panel.", "Write two sentences for each critique step.", "Make a quick thumbnail sketch of the panel's composition (just the main shapes)."],
                 record="your four-step critique and thumbnail."),
     KeyIdea("Describe, analyze, interpret, judge: build opinions about art on evidence.")],
    [Problem("Which critique step lists facts only?", "describe"), Problem("Which step explains meaning?", "interpret"), Problem("What did The Migration Series depict?", "the Great Migration of African Americans from the South to Northern cities")],
    [S("Warm-Up", [SA("A structured discussion of art", "critique"), SA("Name two principles of design.", "e.g. balance, contrast, emphasis, rhythm")], cols=2),
     S("Critique", [OR("Write your four-step critique of one Migration Series panel.", "Answers vary; each step must be present and judgments supported by evidence.", lines=8),
                    DRAW("Thumbnail of the panel's main shapes.", "Simplified composition sketch.", space=140)]),
     S("Exit Ticket", [OR("Why does the critique save “judge” for last?", "So the opinion is based on careful looking and analysis instead of a first impression.", lines=2)])],
    tart("Students apply the four-step critique.", "Perceive, interpret, and evaluate artwork.", "Online access to The Migration Series, sketchbooks, workbook Lesson 1.1",
         "Can art opinions use evidence?", ["Introduce the elements and principles.", "Model a four-step critique on one panel."], "Critique Practice.",
         ["Jumping to judgment.", "Describing with interpretations (“sad”) instead of facts."], ["Sentence frames for each step."], ["Compare two panels' compositions."]),
    summary="Describe, analyze, interpret, judge.")

L2 = Lesson("1.2", "Line and Mark-Making",
    "I can use contour, gesture, hatching, cross-hatching, and stippling to describe form and value.", "NCAS VA:Cr2",
    [("contour drawing", "A drawing of an object's edges, made with careful, continuous line."), ("gesture drawing", "A quick drawing that captures movement and pose."),
     ("hatching", "Parallel lines that create value; cross-hatching layers them in different directions."), ("stippling", "Dots that create value; closer dots look darker.")],
    "How can a drawing made only of black lines show light and shadow?",
    [Text("Line can describe edges, movement, and even value. A <b>contour</b> line traces edges slowly. A <b>blind contour</b>, drawn without looking at the paper, trains your eye to see. A <b>gesture</b> drawing captures movement in seconds. To build value with line, artists use <b>hatching</b>, <b>cross-hatching</b>, and <b>stippling</b>."),
     Figure(lambda t: Draw(W * 0.85, 80, lambda c, w, h: _marks(c, w, h, t))),
     Text("The German artist <b>Albrecht Dürer</b> (1471–1528) was a master of hatching in engravings and woodcuts. In his woodcut <b>Rhinoceros</b> (1515), patterns of lines create both texture and value, even though Dürer never saw the animal; he worked from a written description and a sketch by someone else."),
     Investigate("Mark-Making Value Studies", "Which technique makes the smoothest value change?", ["fine black pen or sharp pencil", "sketchbook"],
                 ["Draw three rectangles divided into five boxes.", "Fill one with hatching, one with cross-hatching, and one with stippling, light to dark.", "Draw a 2-minute blind contour of your hand.", "Draw your hand again, looking, and shade it with one technique."],
                 record="the three value strips and two hand drawings."),
     KeyIdea("Line can describe edges (contour), movement (gesture), and value (hatching, cross-hatching, stippling).")],
    [Problem("What is hatching?", "parallel lines that create value"), Problem("Which technique uses dots?", "stippling"), Problem("Why do blind contours?", "to train your eye to look closely at edges")],
    [S("Warm-Up", [SA("Quick drawing of movement", "gesture"), SA("Layered hatching in different directions", "cross-hatching")], cols=2),
     S("Create", [DRAW("Three value strips: hatching, cross-hatching, stippling (5 steps each).", "Even steps from light to dark in all three.", space=150),
                  DRAW("Shaded hand drawing.", "Accurate contour; value with one technique.", space=230)]),
     S("Exit Ticket", [OR("Which technique would best show rough tree bark? Why?", "Cross-hatching or hatching that follows the bark's direction shows rough texture and dark grooves.", lines=2)])],
    tart("Students use line techniques for form and value.", "Organize and develop artistic work.", "Fine pens, pencils, sketchbooks, workbook Lesson 1.2",
         "Black lines showing light?", ["Demonstrate each mark-making technique."], "Mark-Making Value Studies.",
         ["Uneven spacing that makes muddy values."], ["Practice strips with guide lines."], ["Make a stippled portrait of a pet."]),
    summary="Contour, gesture, hatching, cross-hatching, stippling.")


def _marks(c, w, h, t):
    names = ["hatching", "cross-hatching", "stippling"]
    import random
    rnd = random.Random(3); cw = w / 3
    for i, nm in enumerate(names):
        x0, x1, y0, y1 = i * cw + 10, (i + 1) * cw - 10, 18, h - 6
        c.setStrokeColor(INK); c.setLineWidth(0.6); c.rect(x0, y0, x1 - x0, y1 - y0, fill=0, stroke=1)
        for k in range(5):
            bx0 = x0 + (x1 - x0) * k / 5; bx1 = x0 + (x1 - x0) * (k + 1) / 5; sp = 7 - k * 1.3
            if nm in ("hatching", "cross-hatching"):
                x = bx0
                while x < bx1: c.line(x, y0, min(x + 8, bx1), y1); x += sp
                if nm == "cross-hatching" and k >= 2:
                    x = bx0
                    while x < bx1: c.line(min(x + 8, bx1), y0, x, y1); x += sp
            else:
                for _ in range(10 + k * 30):
                    c.setFillColor(INK); c.circle(rnd.uniform(bx0 + 1, bx1 - 1), rnd.uniform(y0 + 1, y1 - 1), 0.6, fill=1, stroke=0)
        text(c, (x0 + x1) / 2, 4, nm, "BodySemi", 8, t.accent, "c")


# ================================================================= Week 2 · Form, light, proportion
L3 = Lesson("1.3", "Form and Light",
    "I can render a form using a consistent light source with highlight, midtone, core shadow, reflected light, and cast shadow.", "NCAS VA:Cr2, VA:Cr3",
    [("light source", "The direction light comes from."), ("highlight", "The brightest spot, where light hits most directly."), ("core shadow", "The darkest part on the form, turned away from the light."),
     ("reflected light", "Dim light bounced back onto the shadow side from nearby surfaces."), ("cast shadow", "The shadow an object throws onto another surface.")],
    "Shine a flashlight on a ball in a dark room. Where is it brightest? Where is it darkest? Is the edge of the shadow side completely black?",
    [Text("Realistic drawing depends on <b>light logic</b>: every form in a picture is lit from the same direction. On a sphere, value changes gradually from the <b>highlight</b> through the <b>midtones</b> to the <b>core shadow</b>. Near the edge of the shadow side, light bounces back from the table as <b>reflected light</b>. The darkest dark is usually the <b>cast shadow</b> right where the object touches the surface."),
     Figure(lambda t: shaded_sphere(t, width=W * 0.85, height=165)),
     Investigate("Still Life with One Light", "Can you render three forms lit the same way?", ["a ball, a box, and a can or cup", "flashlight or desk lamp", "pencils (2H, HB, 4B if you have them)", "blending stump or tissue"],
                 ["Arrange the objects and light them from one side in a dim room.", "Lightly draw their shapes and the cast shadows.", "Squint to see the value groups; shade from light to dark.", "Check: is the light coming from the same side on every object?"],
                 record="your rendered still life with the light direction marked by an arrow."),
     KeyIdea("Keep one light source. Render highlight, midtone, core shadow, reflected light, and cast shadow.")],
    [Problem("Where is the darkest part of a cast shadow?", "where the object touches the surface"), Problem("Why is reflected light dimmer than the lit side?", "it's bounced light, not direct light"), Problem("What goes wrong with two light directions?", "the forms look flat or confusing")],
    [S("Warm-Up", [SA("Brightest spot", "highlight"), SA("Shadow thrown onto the table", "cast shadow")], cols=2),
     S("Create", [DRAW("Render a sphere and a cube lit from the upper right. Label the five parts of light on the sphere.", "Consistent light source; five labeled parts.", space=230)]),
     S("Exit Ticket", [OR("Why do artists squint at their subject?", "Squinting blurs detail and makes the big value groups easier to see.", lines=2)])],
    tart("Students render forms with consistent light.", "Develop and refine artistic work.", "Objects, lamp, graded pencils, blending tools, workbook Lesson 1.3",
         "Flashlight and ball.", ["Demonstrate the five parts of light on a sphere."], "Still Life with One Light.",
         ["Outlining forms with dark lines; shading the edge evenly."], ["Value finder: a card with a hole."], ["Render an egg on white paper (white on white)."]),
    summary="One light source; five parts of light on every form.")

L4 = Lesson("1.4", "Proportion and the Human Figure",
    "I can use proportion guidelines to draw a face and a standing figure.", "NCAS VA:Cr2, VA:Cn11",
    [("proportion", "Size relationships between parts and the whole."), ("canon of proportion", "A set of rules for ideal body proportions."), ("foreshortening", "Drawing an object that points toward the viewer so it looks shorter.")],
    "How many of your head-heights tall do you think you are? Guess, then measure with a partner.",
    [Text("Artists have measured the body for thousands of years. Around 1490, <b>Leonardo da Vinci</b> drew the <b>Vitruvian Man</b>, a figure inside a circle and a square, based on the Roman architect Vitruvius's ideas about ideal proportions. Today artists often use the head as a unit: an adult is roughly <b>7½ heads tall</b> (fashion and comic illustrators often stretch it to 8 or more)."),
     Beside(lambda t: face_guide(t, width=140, height=180),
            ["On the face, the eyes sit about <b>halfway</b> down the head.", "The bottom of the nose is about halfway between the eyes and the chin; the mouth is about a third of the way from nose to chin.",
             "The tops of the ears line up with the brow; the bottoms with the nose.", "On the body, the hips are near the halfway point, and the fingertips reach mid-thigh."], fig_w=0.45),
     Investigate("Measured Portrait and Figure", "Do proportion rules match real people?", ["pencil", "measuring tape", "mirror", "a partner or a photo"],
                 ["Measure a partner's head height and total height; divide to find “heads tall.”", "Draw a proportional face with guidelines from the mirror.", "Draw a standing figure 7½ heads tall using stacked ovals as a guide.", "Compare the rule with your measurements."],
                 record="measurements, the face, and the figure."),
     KeyIdea("Use the head as a unit: eyes halfway down the head, an adult about 7½ heads tall. Measure real people to test the rules.")],
    [Problem("About how many heads tall is an adult?", "about 7½"), Problem("Who drew the Vitruvian Man?", "Leonardo da Vinci"), Problem("Where do the ears line up?", "between the brow and the bottom of the nose")],
    [S("Warm-Up", [SA("Rules for ideal proportions", "canon of proportion"), SA("Eyes are about ___ down the head.", "halfway")], cols=2),
     S("Measure", [SA("Partner's head height (cm)", "Answers vary."), SA("Partner's total height ÷ head height =", "Answers vary (about 6.5–7.5 for teens).")], cols=2),
     S("Create", [DRAW("Proportional figure, 7½ heads tall, with head-unit marks.", "Correct head units; hips near middle.", space=280)]),
     S("Exit Ticket", [OR("Why might a teen measure fewer “heads tall” than an adult?", "Heads are proportionally larger in younger people; bodies grow more than heads.", lines=2)])],
    tart("Students apply proportion guidelines.", "Develop artistic work; relate art to cultural and historical context.", "Measuring tapes, mirrors, pencils, workbook Lesson 1.4",
         "Heads tall?", ["Show the Vitruvian Man; demonstrate face and figure guides."], "Measured Portrait and Figure.",
         ["Drawing eyes too high; heads too large on figures."], ["Pre-marked figure templates."], ["Draw a figure in action with foreshortening."]),
    summary="The head is the unit: eyes halfway, adult about 7½ heads.")

# ================================================================= Week 3 · Color and value
L5 = Lesson("1.5", "Color Theory and Color Schemes",
    "I can describe hue, saturation, and value, and use color schemes to create mood.", "NCAS VA:Cr2, VA:Re8",
    [("hue", "The name of a color on the wheel (red, blue-green)."), ("saturation", "How intense or dull a color is (also called intensity)."),
     ("complementary", "Colors opposite on the wheel."), ("analogous", "Colors next to each other on the wheel."), ("triadic", "Three colors evenly spaced around the wheel.")],
    "Why do sunsets feel warm and oceans feel calm? Is it the color, or what we associate with it?",
    [Text("Every color has three properties: <b>hue</b> (its name), <b>value</b> (light or dark), and <b>saturation</b> (bright or dull). Mixing a color with its complement lowers saturation, making it duller or grayer. Artists choose <b>color schemes</b> to set a mood."),
     Figure(lambda t: color_wheel(t, size=170, highlight=["blue", "orange"]), caption="Blue and orange are complements: opposite on the wheel."),
     Figure(lambda t: table(t, [["Scheme", "Colors", "Effect"], ["monochromatic", "tints and shades of one hue", "unified, calm"], ["analogous", "3–4 neighbors (yellow, yellow-green, green)", "harmonious, natural"],
                                ["complementary", "opposites (blue and orange)", "high contrast, energetic"], ["split-complementary", "one hue + the two neighbors of its complement", "contrast with less tension"],
                                ["triadic", "three evenly spaced hues (red, yellow, blue)", "lively, balanced"], ["warm / cool", "reds, oranges, yellows / blues, greens, violets", "warm advances; cool recedes"]],
                            [1.4 * inch, 2.4 * inch, 2.0 * inch], width=5.8 * inch, font_size=9)),
     Investigate("One Image, Two Moods", "How does a color scheme change meaning?", ["colored pencils, markers, or paint", "two copies of a simple line drawing"],
                 ["Draw a simple scene (a house and tree) and trace it twice.", "Color one in an analogous warm scheme.", "Color the other in a complementary or cool scheme.", "Write the mood of each."],
                 record="both versions and a sentence about how mood changed."),
     KeyIdea("Hue, value, and saturation describe any color. Color schemes control harmony, contrast, and mood.")],
    [Problem("Complement of red", "green"), Problem("Analogous colors are…", "neighbors on the wheel"), Problem("How do you lower a color's saturation?", "mix in its complement (or gray)")],
    [S("Warm-Up", [SA("A color's name", "hue"), SA("Brightness or dullness of a color", "saturation")], cols=2),
     S("Practice", [SA(q, a) for q, a in [("Triad including red", "red, yellow, blue"), ("Split-complement of blue", "blue with yellow-orange and red-orange"), ("Analogous to violet", "e.g. red-violet, violet, blue-violet"),
                                          ("Do warm colors seem to advance or recede?", "advance")]], cols=2),
     S("Create", [DRAW("Your scene in two color schemes (side by side).", "Correct schemes and a stated mood for each.", space=220)]),
     S("Exit Ticket", [OR("Which scheme would you use for a poster about a calm library? Why?", "Analogous cool or monochromatic blue: harmonious and calm.", lines=2)])],
    tart("Students apply color theory and schemes.", "Develop artistic work; interpret meaning.", "Color media, workbook Lesson 1.5",
         "Warm sunsets, calm oceans.", ["Teach hue/value/saturation; demonstrate desaturating with a complement."], "One Image, Two Moods.",
         ["Confusing analogous and complementary."], ["Color wheel to point at while choosing."], ["Find each scheme in film posters."]),
    summary="Hue, value, saturation; schemes create mood.")

L6 = Lesson("1.6", "Value, Contrast, and Chiaroscuro",
    "I can make a nine-step value scale and use strong contrast (chiaroscuro) for drama.", "NCAS VA:Cr2, VA:Re7",
    [("value scale", "A sequence of even steps from white to black."), ("chiaroscuro", "Italian for “light-dark”: strong contrast between light and shadow."), ("tenebrism", "Extreme chiaroscuro, with figures emerging from deep darkness.")],
    "Watch a scary movie scene with the sound off. How does lighting create the mood?",
    [Text("A <b>value scale</b> is a ruler for darkness. Artists train by making even steps from white to black, then use that control to model forms."),
     Figure(lambda t: value_scale(t, steps=9)),
     Text("Italian painters of the Renaissance and Baroque periods used <b>chiaroscuro</b> to make figures look solid and dramatic. <b>Caravaggio</b> (1571–1610) pushed it to extremes, called <b>tenebrism</b>: in <b>The Calling of Saint Matthew</b> (about 1600), a beam of light cuts across a dark room and lands on the faces of the men at the table. <b>Rembrandt</b> later used warm, glowing light against deep shadow in his portraits."),
     Investigate("Dramatic Light Study", "How does strong side lighting change an object?", ["one object (a mug, an apple, a toy)", "flashlight", "dark paper and white charcoal or chalk, or pencil on white paper"],
                 ["Make a nine-step value scale.", "Light your object from one low side in a dark room.", "Draw it, pushing the darks very dark and saving the lights.", "Compare with a drawing of the same object in flat, even light."],
                 record="value scale and both drawings."),
     KeyIdea("Control value with even steps; strong light-dark contrast (chiaroscuro) creates drama and solidity.")],
    [Problem("What does chiaroscuro mean?", "light-dark"), Problem("Which artist is known for tenebrism?", "Caravaggio"), Problem("How many steps in the class value scale?", "nine")],
    [S("Warm-Up", [SA("Even steps from white to black", "value scale"), SA("Extreme chiaroscuro", "tenebrism")], cols=2),
     S("Create", [DRAW("Nine-step value scale.", "Nine even, distinct steps.", space=80), DRAW("Dramatic light study of one object.", "Strong contrast; clear light direction.", space=220)]),
     S("Exit Ticket", [OR("How would The Calling of Saint Matthew feel different with even lighting?", "Less dramatic; the moment of being called would lose emphasis.", lines=2)])],
    tart("Students control value and use chiaroscuro.", "Develop artistic work; perceive and analyze.", "Flashlights, objects, charcoal or pencils, workbook Lesson 1.6",
         "Lighting in movies.", ["Demonstrate a 9-step scale.", "Discuss Caravaggio and Rembrandt."], "Dramatic Light Study.",
         ["Not going dark enough."], ["Value finder card."], ["Photograph a still life in dramatic light and draw from the photo."]),
    summary="Even value steps; chiaroscuro for drama.")

# ================================================================= Week 4 · Composition and revision
L7 = Lesson("1.7", "Composition: Thirds, Leading Lines, and Balance",
    "I can plan a composition using the rule of thirds, leading lines, emphasis, and asymmetrical balance.", "NCAS VA:Cr1, VA:Cr2",
    [("rule of thirds", "Dividing an image into thirds and placing key elements on the lines or crossings."), ("leading lines", "Lines that guide the eye toward the focal point."),
     ("negative space", "The empty space around and between objects."), ("asymmetrical balance", "Different elements arranged so visual weight feels even.")],
    "Where does your eye go first in a movie poster? What tricks get it there?",
    [Beside(lambda t: rule_of_thirds(t, width=190, height=125, focal=(1, 2)),
            ["Strong compositions guide the viewer. The <b>rule of thirds</b> places the focal point near one of four crossing points instead of dead center.",
             "<b>Leading lines</b> (roads, rivers, arms, edges) point the eye to it. <b>Asymmetrical balance</b> keeps the picture interesting, and <b>negative space</b> gives the subject room to breathe."], fig_w=0.4),
     Text("In <b>The Great Wave off Kanagawa</b> (about 1831), Katsushika Hokusai builds a powerful asymmetrical composition: the giant wave fills the left and top, its claw-like crest leads the eye across to tiny Mount Fuji, and the boats curve along the wave's path. The small mountain balances the huge wave."),
     Investigate("Four Thumbnails", "Which composition tells your idea best?", ["pencil", "sketchbook"],
                 ["Choose a subject that matters to you.", "Draw four thumbnails: centered, rule of thirds, strong leading lines, and lots of negative space.", "Shade each in three values (light, middle, dark) only.", "Pick the strongest and write why."],
                 record="four value thumbnails and your choice."),
     KeyIdea("Place the focal point thoughtfully, lead the eye to it, balance asymmetrically, and use negative space.")],
    [Problem("What are leading lines?", "lines that guide the eye to the focal point"), Problem("What balances the great wave in Hokusai's print?", "small Mount Fuji (and the boats)"), Problem("Why value-only thumbnails?", "to test the composition's light-dark pattern before color")],
    [S("Warm-Up", [SA("Empty space around objects", "negative space"), SA("Different elements with even visual weight", "asymmetrical balance")], cols=2),
     S("Create", [DRAW("Four value thumbnails of one subject; circle the strongest.", "Four distinct compositions with three values each; reasoned choice.", space=260)]),
     S("Exit Ticket", [OR("Find leading lines in a photo you've taken or a poster. Describe them.", "Answers vary.", lines=2)])],
    tart("Students plan compositions with design strategies.", "Generate and organize artistic ideas.", "Sketchbooks, workbook Lesson 1.7",
         "Movie posters.", ["Analyze The Great Wave's composition."], "Four Thumbnails.",
         ["Detail-heavy thumbnails."], ["Thumbnail frames pre-drawn at 2 × 3 inches."], ["Re-crop a photo three ways to change the focal point."]),
    summary="Thirds, leading lines, balance, negative space.")

L8 = Lesson("1.8", "Revision, Critique, and the Artist Statement",
    "I can revise a work using peer critique and write an artist statement explaining my choices.", "NCAS VA:Cr3, VA:Pr5, VA:Re9",
    [("artist statement", "A short text in which an artist explains their work, process, and choices."), ("peer critique", "Structured feedback from classmates or family.")],
    "Have you ever read the small card next to a painting in a museum? What makes one interesting to read?",
    [Text("Develop your best thumbnail into a finished piece. Midway, hold a short critique using three prompts: <b>I notice…</b> (description), <b>I wonder…</b> (a question), <b>What if…</b> (a suggestion). Then revise."),
     Text("Finish with an <b>artist statement</b> of 75–150 words: what you made, the elements and principles you used and why, what you changed after feedback, and what you want viewers to feel or think."),
     Example("Artist statement starter", "A charcoal drawing of a grandmother's hands",
             ["What: “This charcoal drawing shows my grandmother's hands holding a quilt square.”", "How: “I used chiaroscuro and a rule-of-thirds composition, with the quilt's lines leading to her hands.”",
              "Revision: “After feedback, I darkened the background so the hands stand out.”", "Meaning: “I want viewers to see how hands carry family stories.”"],
             "Clear, specific, and personal."),
     Investigate("Final Piece and Statement", "Can you finish, critique, revise, and explain a work?", ["your chosen thumbnail", "drawing paper", "your choice of media"],
                 ["Develop the thumbnail into a final work.", "Hold a critique with I notice / I wonder / What if.", "Revise.", "Write your artist statement."],
                 record="your final piece and statement for the portfolio."),
     KeyIdea("Critique with I notice / I wonder / What if; revise; explain your choices in an artist statement.")],
    [Problem("Name the three critique prompts.", "I notice, I wonder, What if"), Problem("How long is the artist statement?", "about 75–150 words"), Problem("Name two things an artist statement includes.", "what you made, your choices and why, revisions, intended meaning")],
    [S("Warm-Up", [SA("Text explaining an artist's work", "artist statement"), SA("Prompt for a suggestion", "What if…")], cols=2),
     S("Critique Notes", [OR("Record the feedback you received (I notice / I wonder / What if) and what you will revise.", "Answers vary.", lines=4)]),
     S("Artist Statement", [OR("Write your artist statement (75–150 words).", "Includes what, how, revision, and meaning.", lines=8)])],
    tart("Students revise with critique and write artist statements.", "Refine work; present and evaluate.", "Drawing materials, workbook Lesson 1.8, Unit 1 Review",
         "Museum labels.", ["Model a critique and a statement."], "Final Piece and Statement.",
         ["Statements that only describe, without choices or meaning."], ["Statement template."], ["Display the work at home with its statement."], reflect="Share statements; Friday: Unit 1 Portfolio Review."),
    summary="Critique, revise, and explain your choices.")

# ================================================================= checks
C1 = sketchbook("Sketchbook Check 1: Critique and Line", [S("Show what you know", [
    SA("The four critique steps in order", "describe, analyze, interpret, judge"), SA("Parallel lines that create value", "hatching"), SA("A quick drawing of movement", "gesture"),
    DRAW("Make three boxes of value: hatching, cross-hatching, stippling.", "Three techniques shown clearly.", space=100)], cols=1)])
C2 = sketchbook("Sketchbook Check 2: Light and Proportion", [S("Show what you know", [
    SA("Name the five parts of light on a sphere.", "highlight, midtone, core shadow, reflected light, cast shadow"), SA("An adult is about how many heads tall?", "7½"),
    DRAW("Render a sphere with a light source from the left.", "Consistent shading and cast shadow to the right.", space=130)], cols=1)])
C3 = sketchbook("Sketchbook Check 3: Color and Value", [S("Show what you know", [
    SA("Complement of yellow", "violet"), SA("Three colors evenly spaced on the wheel", "triadic"), SA("Italian for light-dark", "chiaroscuro"),
    SA("How to dull (desaturate) a color", "mix in its complement"), DRAW("Nine-step value scale.", "Nine even steps.", space=70)], cols=1)])

REVIEW = review("Unit 1 Review", [
    S("Vocabulary", [SA(q, a) for q, a in [("saturation", "intensity of a color"), ("analogous", "neighboring colors"), ("tenebrism", "extreme chiaroscuro"), ("leading lines", "lines guiding the eye"),
                                           ("cast shadow", "shadow thrown onto a surface"), ("artist statement", "text explaining your work")]], cols=2),
    S("Portfolio", [OR("Choose three Unit 1 works for your portfolio and write one sentence about each.", "Answers vary.", lines=4)])])

TEST = portfolio("Unit 1 Portfolio Review", [
    S("Part A · Concepts (1 point each)", [
        MC("Which critique step explains meaning?", ["describe", "analyze", "interpret", "judge"], 2),
        MC("Which scheme uses colors opposite each other?", ["analogous", "complementary", "monochromatic"], 1),
        SA("Where is the darkest value of a cast shadow?", "where the object meets the surface"), SA("Name one mark-making technique for value.", "hatching, cross-hatching, or stippling"),
        SA("Who painted The Calling of Saint Matthew?", "Caravaggio"), SA("What balances the wave in Hokusai's print?", "Mount Fuji (and the boats)")], cols=1),
    S("Part B · Critique (4 points)", [OR("Write a four-step critique of an artwork you didn't study in this unit (any museum website).",
                                          "Rubric: describe with facts (1); analyze elements/principles (1); interpret with evidence (1); judge with reasons (1).", lines=8, points=4)]),
    S("Part C · Portfolio (6 points)", [OR("Your teacher scores your Lesson 1.8 final piece and statement with this rubric. Note one goal for Unit 2.",
                                           "Rubric (1 point each): planned composition; consistent light/value; purposeful color or value scheme; skilled mark-making; evidence of revision; clear artist statement.", lines=3, points=6)])],
    labels=["Excellent: skilled, purposeful, and well explained.", "Solid: strengthen one technique.", "Redo one studio activity with support."])

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
CHECKS = [C1, C2, C3]
WEEKS = weeks_for(1, LESSONS, CHECKS, REVIEW, TEST)

UNIT = Unit(1, "The Elements of Art", "Critique, line and mark-making, form and light, proportion, color schemes, chiaroscuro, composition, and the artist statement.",
    "Skilled artists combine sharp eyes with deliberate choices. In this unit you'll learn a professional critique method, build drawing skills (mark-making, light logic, proportion), use color theory and dramatic value, plan strong compositions, and finish a revised work with an artist statement.",
    ["Critique art using describe, analyze, interpret, judge.", "Use contour, gesture, and value techniques; render light on forms.", "Apply proportion, color schemes, and chiaroscuro.", "Plan compositions, revise with critique, and write an artist statement."],
    [("NCAS VA:Cr1–3", "Generate, develop, and refine artwork."), ("NCAS VA:Pr5", "Prepare work for presentation."), ("NCAS VA:Re7–9", "Perceive, interpret, and evaluate."), ("NCAS VA:Cn11", "Relate art to context.")],
    [("critique", "Structured discussion of art."), ("hatching", "Parallel lines for value."), ("chiaroscuro", "Strong light-dark contrast."), ("analogous", "Neighboring colors."),
     ("rule of thirds", "Placing key elements on thirds."), ("artist statement", "Explanation of an artwork.")],
    ["Grade 6 art basics."], ["Sketchbook; graded pencils (2H, HB, 4B); fine pens; charcoal", "Color media", "Flashlight or lamp", "Measuring tape and mirror", "Portfolio folder"],
    LESSONS, CHECKS, REVIEW, TEST,
    real_world="Illustrators, game artists, photographers, and filmmakers use light, color, and composition to steer attention and emotion.",
    family_note="Look at The Migration Series together online and talk about how it connects to the Harlem Renaissance reading in ELA.",
    weeks=WEEKS)
