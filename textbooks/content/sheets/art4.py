"""Studio Sheets for Grade 4 Art."""
from content.labkit import T, CER, BOX, LN, GRAPH, Take

SHEETS = {
    "1.1": [Take("Sketch")],
    "1.2": [Take("Sketch"), BOX("Draw the same simple landscape twice: calm lines on the left, stormy lines on the right.", 150),
            LN("Which lines did you choose for each landscape, and why?", 2)],
    "1.3": [BOX("Draw a flat circle and a shaded sphere side by side. Show where the light comes from.", 140), Take("Sketch")],
    "1.4": [Take("Sketch"), LN("What did the guidelines help you get right?", 2)],
    "1.5": [Take("Create"), LN("Which colors were hardest to mix? What did you do?", 2)],
    "1.6": [Take("Create")],
    "1.7": [Take("Sketch"), LN("Why is the thumbnail you circled the strongest?", 2)],
    "1.8": [BOX("Draft: sketch your plan here.", 150),
            T("Feedback I got", "What I will change", rows=2, row_h=36),
            Take("Create")],
    "2.1": [Take("Plan"), LN("What does each symbol on your mask mean?", 2)],
    "2.2": [Take("Create"), T("Color or symbol", "What it means", rows=3, row_h=24, label="Make a key for your pattern cloth.")],
    "2.3": [Take("Create"), LN("Which character came out best? What made it work?", 2)],
    "2.4": [Take("Sketch"), LN("How did you show the three values in your finished scroll?", 2)],
    "2.5": [Take("Plan"), LN("What was hardest about pinching the pot? What would you do differently?", 2)],
    "2.6": [Take("Plan"), T("Attribute", "What it tells about the person", rows=3, row_h=24)],
    "2.7": [BOX("Draw your building front. Make it symmetrical. Label the column style and give it a name.", 230)],
    "2.8": [T("Artwork", "Where it hangs", rows=5, row_h=22, label="Plan your gallery: list each piece and where you'll hang it."),
            Take("Labels", "Artist Statement")],
}
