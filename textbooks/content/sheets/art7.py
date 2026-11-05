"""Studio Sheets for Grade 7 Art."""
from content.labkit import T, CER, BOX, LN, GRAPH, Take

SHEETS = {
    "1.1": [Take("Critique")],
    "1.2": [Take("Create")],
    "1.3": [Take("Create"), BOX("Thumbnail of your still life. Mark the light direction with an arrow.", 130)],
    "1.4": [Take("Measure", "Create")],
    "1.5": [Take("Create"), LN("How did the mood change between the two versions?", 2)],
    "1.6": [Take("Create")],
    "1.7": [Take("Create"), LN("Why did you choose that thumbnail?", 2)],
    "1.8": [BOX("Plan your final piece: sketch the composition.", 150), Take("Critique Notes", "Artist Statement")],
    "2.1": [LN("Write the dream sentence that inspired your sketch.", 2), BOX("Dream journal sketch.", 200)],
    "2.2": [Take("Exquisite Corpse", "Plan"), LN("Title for your collage:", 1)],
    "2.3": [LN("Feeling I want to show:", 1), BOX("Practice gestures: try five quick marks that show the feeling.", 120), Take("Reflect")],
    "2.4": [T("", "Study 1", "Study 2", first=["Colors I used", "Mood it creates"], row_h=40, label_w=1.3 * 72), Take("Analyze")],
    "2.5": [LN("Song I chose:", 1), Take("Sketch"), LN("How did you create rhythm and balance?", 2)],
    "2.6": [T("Realistic", "Simplified", "Pattern", rows=1, row_h=150, label="Draw all three versions side by side."), Take("Reflect")],
    "2.7": [BOX("Floor plan (view from above). Label each room.", 170), BOX("Outside view. Label two features that respond to the site.", 170), Take("Design")],
    "2.8": [Take("Select", "Artist Statement")],
}
