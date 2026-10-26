"""Grade 4 Art, block 1 week 1 (Mon Oct 26 2026): one-lesson overview of medieval art and architecture.
Writes downloads/integrated/grade4-art-medieval-{teacher,student}.pdf (teacher copy adds the answer page)."""
import math
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, Flowable, KeepTogether, PageBreak, CondPageBreak)

G = "/usr/share/fonts/truetype/google-fonts/"
C = "/usr/share/fonts/truetype/crosextra/"
pdfmetrics.registerFont(TTFont("Body", G + "Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("BodyMed", G + "Poppins-Medium.ttf"))
pdfmetrics.registerFont(TTFont("BodyBold", G + "Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("BodyIt", G + "Poppins-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Head", C + "Caladea-Bold.ttf"))
pdfmetrics.registerFont(TTFont("HeadIt", C + "Caladea-Italic.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Body", normal="Body", bold="BodyBold", italic="BodyIt", boldItalic="BodyBold")

GREEN = colors.HexColor("#24503b")
GREEN_L = colors.HexColor("#eef4ef")
CREAM = colors.HexColor("#fbf7ee")
GOLD = colors.HexColor("#b8892b")
RED = colors.HexColor("#a63d32")
BLUE = colors.HexColor("#2f5d8a")
INK = colors.HexColor("#22302a")
MUTED = colors.HexColor("#5b6b62")
STONE = colors.HexColor("#c9c2b2")
STONE_D = colors.HexColor("#8f8778")

body = ParagraphStyle("body", fontName="Body", fontSize=11.5, leading=17.5, textColor=INK, spaceAfter=7)
small = ParagraphStyle("small", parent=body, fontSize=9.5, leading=13.5, textColor=MUTED, spaceAfter=3)
h1 = ParagraphStyle("h1", fontName="Head", fontSize=30, leading=33, textColor=GREEN, spaceAfter=4)
sub = ParagraphStyle("sub", fontName="HeadIt", fontSize=15, leading=19, textColor=MUTED, spaceAfter=12)
h2 = ParagraphStyle("h2", fontName="Head", fontSize=20, leading=24, textColor=GREEN, spaceBefore=10, spaceAfter=6)
h3 = ParagraphStyle("h3", fontName="BodyBold", fontSize=12.5, leading=17, textColor=RED, spaceBefore=6, spaceAfter=3)
eyebrow = ParagraphStyle("eyebrow", fontName="BodyBold", fontSize=8.5, leading=11, textColor=GOLD, spaceAfter=2)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=16, bulletIndent=4, spaceAfter=3)
cap = ParagraphStyle("cap", parent=small, alignment=TA_CENTER, fontName="BodyIt")
boxtext = ParagraphStyle("boxtext", parent=body, spaceAfter=4)

W = letter[0] - 1.5 * inch  # frame width


def P(t, s=body):
    return Paragraph(t, s)


def bullets(items, s=bullet):
    return [Paragraph(i, s, bulletText="•") for i in items]


def box(flowables, bg=GREEN_L, border=GREEN, pad=12):
    t = Table([[flowables]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("BOX", (0, 0), (-1, -1), 1, border),
                           ("LEFTPADDING", (0, 0), (-1, -1), pad), ("RIGHTPADDING", (0, 0), (-1, -1), pad),
                           ("TOPPADDING", (0, 0), (-1, -1), pad - 2), ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 4)]))
    return t


class Drawing(Flowable):
    def __init__(self, h, fn, w=None):
        super().__init__(); self.h = h; self.fn = fn; self.w = w or W

    def wrap(self, aw, ah):
        return self.w, self.h

    def draw(self):
        self.fn(self.canv, self.w, self.h)


def label(c, x, y, text, size=9, color=INK, font="BodyMed", align="c"):
    c.setFillColor(color); c.setFont(font, size)
    {"c": c.drawCentredString, "l": c.drawString, "r": c.drawRightString}[align](x, y, text)


# ---------- diagrams ----------
def stones_wall(c, x, y, w, h):
    c.setFillColor(STONE); c.setStrokeColor(STONE_D); c.setLineWidth(0.6)
    c.rect(x, y, w, h, fill=1, stroke=1)
    row = 9
    c.setStrokeColor(STONE_D); c.setLineWidth(0.4)
    yy = y + row
    i = 0
    while yy < y + h:
        c.line(x, yy, x + w, yy)
        off = 0 if i % 2 else 9
        xx = x + off
        while xx < x + w:
            c.line(xx, yy - row, xx, yy)
            xx += 18
        yy += row; i += 1


def arches(c, w, h):
    # Romanesque (round) arch, left; Gothic (pointed) arch, right
    def wall_with_hole(cx, base, ow, oh, pointed):
        ww, wh = ow + 70, oh + 46
        x0 = cx - ww / 2
        stones_wall(c, x0, base, ww, wh)
        p = c.beginPath()
        r = ow / 2
        p.moveTo(cx - r, base); p.lineTo(cx - r, base + oh - (r if not pointed else ow * 0.85))
        if not pointed:
            p.arcTo(cx - r, base + oh - 2 * r, cx + r, base + oh, startAng=180, extent=-180)
        else:
            spring = base + oh - ow * 0.85
            # two arcs meeting in a point, each with radius = opening width
            p.curveTo(cx - r, spring + ow * 0.5, cx - r * 0.45, spring + ow * 0.75, cx, base + oh)
            p.curveTo(cx + r * 0.45, spring + ow * 0.75, cx + r, spring + ow * 0.5, cx + r, spring)
        p.lineTo(cx + r, base); p.close()
        c.setFillColor(colors.white if not pointed else colors.HexColor("#dbe7f3")); c.setStrokeColor(INK); c.setLineWidth(1.2)
        c.drawPath(p, fill=1, stroke=1)
        return x0, ww, wh

    base = 30
    x0, ww, wh = wall_with_hole(w * 0.25, base, 64, 96, False)
    label(c, w * 0.25, base - 16, "ROMANESQUE: round arch", 10, GREEN, "BodyBold")
    label(c, w * 0.25, base + wh + 8, "thick walls, small windows", 8.5, MUTED, "Body")
    x1, ww1, wh1 = wall_with_hole(w * 0.75, base, 52, 120, True)
    label(c, w * 0.75, base - 16, "GOTHIC: pointed arch", 10, GREEN, "BodyBold")
    label(c, w * 0.75, base + wh1 + 8, "taller, thinner, more light", 8.5, MUTED, "Body")


def buttress(c, w, h):
    base = 22
    cx = w / 2
    # nave walls
    c.setLineWidth(1); c.setStrokeColor(INK)
    c.setFillColor(STONE)
    nave_w, wall_t, wall_h = 120, 12, 150
    lx, rx = cx - nave_w / 2 - wall_t, cx + nave_w / 2
    c.rect(lx, base, wall_t, wall_h, fill=1); c.rect(rx, base, wall_t, wall_h, fill=1)
    # roof
    c.setFillColor(colors.HexColor("#7a5b45"))
    p = c.beginPath(); p.moveTo(lx - 6, base + wall_h); p.lineTo(cx, base + wall_h + 62); p.lineTo(rx + wall_t + 6, base + wall_h); p.close()
    c.drawPath(p, fill=1, stroke=1)
    # stained glass windows on the walls
    c.setFillColor(colors.HexColor("#6f9fd0"))
    for x in (lx, rx):
        c.rect(x + 2.5, base + 60, wall_t - 5, 60, fill=1, stroke=0)
    # side aisles roofs
    c.setFillColor(STONE)
    for side in (-1, 1):
        px = cx + side * (nave_w / 2 + 70)  # pier center
        pier_w, pier_h = 22, 112
        c.setFillColor(STONE); c.rect(px - pier_w / 2, base, pier_w, pier_h, fill=1)
        # pinnacle
        p = c.beginPath(); p.moveTo(px - pier_w / 2, base + pier_h); p.lineTo(px, base + pier_h + 26); p.lineTo(px + pier_w / 2, base + pier_h); p.close()
        c.drawPath(p, fill=1, stroke=1)
        # flying arch from pier top to the wall
        wall_x = lx if side < 0 else rx + wall_t
        inner = px + (-side) * pier_w / 2
        p = c.beginPath()
        p.moveTo(inner, base + pier_h - 6)
        p.curveTo(inner + (-side) * 25, base + pier_h + 18, wall_x + side * 18, base + 128, wall_x, base + 128)
        p.lineTo(wall_x, base + 116)
        p.curveTo(wall_x + side * 22, base + 112, inner + (-side) * 18, base + pier_h - 2, inner, base + pier_h - 24)
        p.close()
        c.setFillColor(colors.HexColor("#b6ae9c")); c.drawPath(p, fill=1, stroke=1)
    c.setStrokeColor(INK); c.line(20, base, w - 20, base)
    # labels with arrows
    def arrow(x1, y1, x2, y2):
        c.setStrokeColor(RED); c.setLineWidth(1.2); c.line(x1, y1, x2, y2)
        a = math.atan2(y2 - y1, x2 - x1)
        c.setFillColor(RED)
        p = c.beginPath(); p.moveTo(x2, y2)
        p.lineTo(x2 - 7 * math.cos(a - 0.4), y2 - 7 * math.sin(a - 0.4))
        p.lineTo(x2 - 7 * math.cos(a + 0.4), y2 - 7 * math.sin(a + 0.4)); p.close(); c.drawPath(p, fill=1, stroke=0)
    rpx = cx + nave_w / 2 + 70
    label(c, rpx + 60, base + 168, "flying buttress", 10, RED, "BodyBold", "l")
    arrow(rpx + 58, base + 166, rpx - 28, base + 126)
    label(c, cx - nave_w / 2 - 200, base + 168, "tall, thin wall", 10, RED, "BodyBold", "l")
    arrow(cx - nave_w / 2 - 125, base + 165, lx - 2, base + 140)
    label(c, cx, base + 95, "inside the", 9, INK, "Body")
    label(c, cx, base + 83, "cathedral", 9, INK, "Body")
    label(c, w / 2, base - 15, "The stone arms push in and hold the high walls up, so the walls can be full of windows.", 9, MUTED, "BodyIt")


def rose_window(c, cx, cy, r, filled=True):
    pal = [colors.HexColor(x) for x in ("#2f5d8a", "#a63d32", "#d6a531", "#3d7a52", "#6a4a8c", "#2f5d8a", "#a63d32", "#d6a531")]
    c.setLineWidth(2.2 if filled else 1.6); c.setStrokeColor(INK)
    c.setFillColor(colors.white)
    c.circle(cx, cy, r, fill=1)
    n = 12
    for i in range(n):
        a1 = 2 * math.pi * i / n; a2 = 2 * math.pi * (i + 1) / n
        for (ri, ro, k) in ((r * 0.32, r * 0.68, 0), (r * 0.68, r, 1)):
            p = c.beginPath()
            p.moveTo(cx + ri * math.cos(a1), cy + ri * math.sin(a1))
            p.lineTo(cx + ro * math.cos(a1), cy + ro * math.sin(a1))
            p.arcTo(cx - ro, cy - ro, cx + ro, cy + ro, math.degrees(a1), 360 / n)
            p.lineTo(cx + ri * math.cos(a2), cy + ri * math.sin(a2))
            p.arcTo(cx - ri, cy - ri, cx + ri, cy + ri, math.degrees(a2), -360 / n)
            p.close()
            c.setFillColor(pal[(i + k * 3) % len(pal)] if filled else colors.white)
            c.drawPath(p, fill=1, stroke=1)
    # petals in the middle
    for i in range(6):
        a = 2 * math.pi * i / 6
        c.setFillColor(pal[(i * 2) % len(pal)] if filled else colors.white)
        c.circle(cx + r * 0.17 * math.cos(a), cy + r * 0.17 * math.sin(a), r * 0.12, fill=1)
    c.setFillColor(colors.HexColor("#d6a531") if filled else colors.white)
    c.circle(cx, cy, r * 0.1, fill=1)


def castle(c, w, h):
    base = 40
    # moat
    c.setFillColor(colors.HexColor("#8fb5d6")); c.setStrokeColor(colors.HexColor("#5f88ad"))
    c.rect(30, base - 14, w - 60, 14, fill=1)
    def tower(x, tw, th):
        c.setFillColor(STONE); c.setStrokeColor(INK); c.setLineWidth(1)
        c.rect(x, base, tw, th, fill=1)
        mw = tw / 5
        for k in range(0, 5, 2):
            c.rect(x + k * mw, base + th, mw, 8, fill=1)
        c.setFillColor(INK); c.rect(x + tw / 2 - 2, base + th * 0.6, 4, 12, fill=1, stroke=0)  # arrow slit
    cx = w / 2
    # curtain wall
    c.setFillColor(STONE); c.setStrokeColor(INK)
    c.rect(cx - 150, base, 300, 70, fill=1)
    for k in range(15):
        if k % 2 == 0: c.rect(cx - 150 + k * 20, base + 70, 20, 8, fill=1)
    tower(cx - 175, 44, 105); tower(cx + 131, 44, 105)
    tower(cx - 40, 80, 150)  # keep
    c.setFillColor(RED); c.setStrokeColor(INK)
    c.line(cx, base + 158, cx, base + 185)
    p = c.beginPath(); p.moveTo(cx, base + 185); p.lineTo(cx + 22, base + 179); p.lineTo(cx, base + 173); p.close(); c.drawPath(p, fill=1)
    # gate and drawbridge
    c.setFillColor(colors.HexColor("#4a3a2c"))
    p = c.beginPath(); p.moveTo(cx - 18, base); p.lineTo(cx - 18, base + 30); p.arcTo(cx - 18, base + 12, cx + 18, base + 48, 180, -180); p.lineTo(cx + 18, base); p.close(); c.drawPath(p, fill=1)
    c.setFillColor(colors.HexColor("#9c7a52")); c.rect(cx - 18, base - 14, 36, 14, fill=1)
    def tag(x, y, tx, ty, t):
        c.setStrokeColor(RED); c.setLineWidth(1); c.line(x, y, tx, ty)
        c.setFillColor(RED); c.circle(tx, ty, 2, fill=1, stroke=0)
        label(c, x + (4 if x > tx else -4), y - 3, t, 9.5, RED, "BodyBold", "l" if x > tx else "r")
    tag(cx + 95, base + 165, cx + 40, base + 140, "keep (strongest tower)")
    tag(cx - 215, base + 135, cx - 165, base + 109, "battlements")
    tag(cx + 230, base + 60, cx + 160, base + 70, "tower")
    tag(cx + 110, base - 30, cx + 20, base - 8, "drawbridge")
    tag(cx - 110, base - 30, cx - 70, base - 8, "moat")


def initial(c, w, h):
    # an illuminated letter "M"
    s = 96
    x, y = 6, (h - s) / 2
    c.setFillColor(BLUE); c.setStrokeColor(GOLD); c.setLineWidth(4)
    c.roundRect(x, y, s, s, 6, fill=1, stroke=1)
    c.setStrokeColor(colors.HexColor("#d6a531")); c.setLineWidth(1)
    for i in range(6):  # vine swirls
        c.circle(x + 14 + i * 14, y + 12, 4, fill=0)
        c.circle(x + 14 + i * 14, y + s - 12, 4, fill=0)
    c.setFillColor(colors.HexColor("#e8c25a")); c.setFont("Head", 72)
    c.drawCentredString(x + s / 2, y + 22, "M")


def blank_initial(c, w, h):
    s = min(h - 10, 210)
    x, y = (w - s) / 2, 5
    c.setStrokeColor(INK); c.setLineWidth(2); c.rect(x, y, s, s)
    c.setDash(3, 3); c.setLineWidth(0.8); c.rect(x + 14, y + 14, s - 28, s - 28); c.setDash()


# ---------- page decorations ----------
def on_page(c, doc):
    c.saveState()
    c.setFillColor(GREEN); c.rect(0, letter[1] - 10, letter[0], 10, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(0, letter[1] - 13, letter[0], 3, fill=1, stroke=0)
    c.setFont("Body", 8); c.setFillColor(MUTED)
    c.drawString(0.75 * inch, 0.5 * inch, "VenvLearning  ·  Grade 4 Art & Art History  ·  Medieval Art and Architecture")
    c.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"Page {doc.page}")
    c.restoreState()


story = []
story += [P("GRADE 4  ·  ART &amp; ART HISTORY  ·  ONE LESSON", eyebrow),
          P("Castles, Cathedrals &amp; Colorful Glass", h1),
          P("Art and architecture of the Middle Ages", sub)]

glance = Table([
    [P("<b>Time</b><br/>About 45–60 minutes", boxtext), P("<b>You will need</b><br/>Colored pencils or markers, a gold or yellow crayon, a ruler", boxtext)],
    [P("<b>Big idea</b><br/>People in the Middle Ages used art and buildings to stay safe, to worship, and to tell stories.", boxtext),
     P("<b>By the end, I can…</b><br/>• tell how castles kept people safe<br/>• compare Romanesque and Gothic churches<br/>• name three kinds of medieval art", boxtext)],
], colWidths=[W / 2, W / 2])
glance.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GREEN_L), ("BOX", (0, 0), (-1, -1), 1, GREEN),
                            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#c5d8cb")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8)]))
story += [glance, Spacer(1, 10)]

story += [box([P("<b>Warm-up:</b> Think of the biggest building you have ever been inside. How do you think people built giant buildings 800 years ago, with no cranes, trucks, or electricity? Talk about it for one minute.", boxtext)], bg=CREAM, border=GOLD)]

story += [P("What were the Middle Ages?", h2),
          P("The <b>Middle Ages</b> (also called the <b>medieval</b> period) lasted about 1,000 years, from around the year 500 to around 1500. They are called the “middle” ages because they came <i>between</i> the time of ancient Rome and the modern world."),
          P("In Europe, most people were farmers. Kings and lords ruled the land, and knights fought for them. The Christian Church was at the center of almost everyone’s life. Very few people could read, so <b>pictures were a way to tell stories</b>, and art was everywhere: on walls, in windows, and in books.")]

story += [P("Castles: built to stay safe", h2),
          P("Lords and kings built <b>castles</b> to protect their families, soldiers, and land. At first castles were made of wood. Later they were made of stone, which was much harder to burn or knock down."),
          Drawing(232, castle),
          Spacer(1, 4)]
story += bullets(["A <b>moat</b> was a deep ditch, often filled with water, that kept attackers away from the walls.",
                  "The <b>drawbridge</b> could be pulled up to close the gate.",
                  "<b>Battlements</b> are the up-and-down shapes on top of the walls. Soldiers could hide behind the high parts and shoot arrows through the gaps.",
                  "The <b>keep</b> was the tallest, strongest tower, the last safe place if enemies got inside."])

story += [CondPageBreak(3.2 * inch), P("Cathedrals: buildings that reach for the sky", h2),
          P("A <b>cathedral</b> is a large, important church. Building one could take 100 years or more, so the workers who started it often never saw it finished. Medieval churches were built in two main styles."),
          P("Romanesque style (about 1000–1150)", h3),
          P("Romanesque churches have <b>round arches</b>, very thick walls, and small windows. They look strong and heavy, almost like a fortress, and they are often dark inside. The walls had to be thick to hold up the heavy stone roof."),
          P("Gothic style (starting about 1140)", h3),
          P("Builders in France found new tricks. <b>Pointed arches</b> push the weight of the roof down more steeply, so the buildings could be much taller. Stone arms on the outside called <b>flying buttresses</b> helped hold up the walls. Because the walls no longer had to carry all the weight, builders could fill them with huge, colorful windows. Famous Gothic cathedrals include <b>Notre-Dame de Paris</b> and <b>Chartres Cathedral</b> in France."),
          KeepTogether([Drawing(185, arches), P("Look closely: which arch looks taller and lighter?", cap)]),
          Spacer(1, 6),
          KeepTogether([Drawing(250, buttress)]),
          Spacer(1, 4),
          box([P("<b>Fun fact: gargoyles</b><br/>Many Gothic cathedrals have stone creatures called <b>gargoyles</b> on the roof. They have a real job! Rainwater runs through them and spouts out of their mouths, away from the walls.", boxtext)], bg=CREAM, border=GOLD)]

story += [PageBreak(), P("Art that tells stories", h2),
          P("Most medieval art had a job to do: to teach a story, to honor God, or to show important events. Here are four kinds of art you would have seen."),
          ]

def rose(c, w, h): rose_window(c, w / 2, h / 2, h / 2 - 4, True)
glass = Table([[Drawing(130, rose, 140), [P("Stained glass", h3),
          P("Artists cut small pieces of colored glass and held them together with strips of lead, like a puzzle. When sunlight shines through, the whole church glows with color. Windows showed Bible stories so people who could not read could still “read” the pictures. A big round window like this is called a <b>rose window</b>.")]]],
          colWidths=[150, W - 150])
glass.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
story += [glass]

manu = Table([[Drawing(110, initial, 110), [P("Illuminated manuscripts", h3),
          P("Before printing machines, every book was copied <b>by hand</b>, often by monks. They wrote on <b>parchment</b>, made from animal skin, and decorated the pages with bright paint and real gold. The gold made the pages seem to glow, or “light up.” That is why they are called <b>illuminated</b>. The first letter of a page was often huge and fancy, like this M. One famous example is the <b>Book of Kells</b>, made in Ireland around the year 800.")]]],
          colWidths=[120, W - 120])
manu.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
story += [manu]

story += [P("Tapestries and embroidery", h3),
          P("Big cloth pictures hung on cold stone castle walls. They looked beautiful and helped keep rooms warm. The <b>Bayeux Tapestry</b> is about 230 feet long, as long as two and a half basketball courts! It tells the story of a famous battle in the year 1066, a bit like a giant comic strip sewn with wool thread."),
          P("Mosaics", h3),
          P("A <b>mosaic</b> is a picture made from tiny pieces of colored stone or glass. In the Byzantine Empire, the eastern part of the old Roman world, churches such as the <b>Hagia Sophia</b> in Constantinople (today Istanbul, Turkey) were covered with shining gold mosaics.")]

story += [box([P("<b>Around the world at the same time</b>", boxtext),
               P("The Middle Ages were not only happening in Europe. Muslim artists and builders created amazing places too, like the <b>Alhambra</b> palace in Spain. Instead of pictures of people, they often used <b>geometric patterns</b>, shapes that repeat again and again, and beautiful handwriting called <b>calligraphy</b>.", boxtext)])]

# Vocabulary
story += [CondPageBreak(3.5 * inch), P("Words to know", h2)]
vocab = [("medieval", "having to do with the Middle Ages, about 500–1500"),
         ("cathedral", "a large, important church"),
         ("Romanesque", "a building style with round arches, thick walls, and small windows"),
         ("Gothic", "a building style with pointed arches, tall walls, and big windows"),
         ("flying buttress", "a stone arm on the outside of a building that helps hold up its walls"),
         ("stained glass", "colored glass pieces joined together to make a picture"),
         ("illuminated manuscript", "a hand-written book decorated with bright colors and gold"),
         ("tapestry", "a large picture made with thread on cloth"),
         ("mosaic", "a picture made of tiny pieces of stone or glass")]
vt = Table([[P(f"<b>{a}</b>", boxtext), P(b, boxtext)] for a, b in vocab], colWidths=[1.85 * inch, W - 1.85 * inch])
vt.setStyle(TableStyle([("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, GREEN_L]), ("BOX", (0, 0), (-1, -1), 0.8, GREEN),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 5), ("LEFTPADDING", (0, 0), (-1, -1), 8)]))
story += [vt]

# Check
story += [Spacer(1, 10), P("Check what you learned", h2)]
qs = ["Name two parts of a castle and tell how each one kept people safe.",
      "How is a Romanesque church different from a Gothic church? Give two differences.",
      "What job did a flying buttress do?",
      "Why were stained-glass windows so important for people who could not read?",
      "Why do you think monks used real gold in illuminated manuscripts?"]
for i, q in enumerate(qs, 1):
    story += [KeepTogether([P(f"<b>{i}.</b> {q}", body), Spacer(1, 30 if i < 5 else 30)])]
    # writing lines
    def lines(c, w, h):
        c.setStrokeColor(colors.HexColor("#c5cfc8")); c.setLineWidth(0.7)
        for k in range(2): c.line(14, h - 2 - k * 26, w, h - 2 - k * 26)
    story[-1] = KeepTogether([P(f"<b>{i}.</b> {q}", body), Drawing(52, lines)])

story += [Spacer(1, 8), P("Be an artist: choose one", h2)]
act = Table([[ [P("<b>A. Illuminate your initial</b>", h3),
                P("Draw the first letter of your name in the square. Make it big and fancy. Fill the space around it with vines, animals, or patterns. Use yellow or gold to make it “glow.”", boxtext)],
               [P("<b>B. Design a rose window</b>", h3),
                P("Color the rose window on the next page. Repeat your colors in a pattern all the way around the circle, the way medieval glassmakers did. Outline every piece with a dark line for the lead.", boxtext)] ]],
             colWidths=[W / 2, W / 2])
act.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (0, 0), 1, GOLD), ("BOX", (1, 0), (1, 0), 1, GOLD),
                         ("BACKGROUND", (0, 0), (-1, -1), CREAM), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10)]))
story += [KeepTogether([act, Spacer(1, 8), Drawing(200, blank_initial), P("Your illuminated initial", cap)])]

def blank_rose(c, w, h): rose_window(c, w / 2, h / 2 + 4, min(w, h) / 2 - 12, False)
story += [PageBreak(), P("Rose window coloring page", h2),
          P("Gothic cathedrals like Notre-Dame de Paris have giant rose windows. Color yours with a repeating pattern.", body),
          Drawing(470, blank_rose)]

# Answer key
story += [PageBreak(), P("FOR THE TEACHER", eyebrow), P("Answer guide and teaching notes", h2)]
keys = ["<b>1.</b> Any two: moat (kept attackers away from the walls), drawbridge (could be raised to close the gate), battlements (soldiers hid behind them and shot through the gaps), keep (strongest tower, last place of safety), thick stone walls (hard to burn or break).",
        "<b>2.</b> Romanesque: round arches, thick heavy walls, small windows, darker inside. Gothic: pointed arches, taller and thinner walls, flying buttresses, large stained-glass windows, brighter inside.",
        "<b>3.</b> It pushed against the high walls from outside to hold them up, so the walls could be thinner and hold big windows.",
        "<b>4.</b> The pictures told Bible stories and other lessons, so people could learn them by looking.",
        "<b>5.</b> Accept reasoned answers: to make the book glow, to show the words were precious or holy, to honor God, to show wealth."]
story += [P(k) for k in keys]
story += [P("Teaching notes", h3)]
story += bullets(["<b>Pacing:</b> warm-up 5 min · read and discuss pages 1–4, about 20–25 min · check questions 10 min · art activity 15–20 min.",
                  "<b>Hands-on demo:</b> Hold a sheet of paper upright: it falls. Lean a book against each side and it stands. That is what a buttress does.",
                  "<b>Look it up together:</b> search for photos of Chartres Cathedral’s windows, the Book of Kells, the Bayeux Tapestry, and the Alhambra, and compare them with the drawings in this lesson.",
                  "<b>Extension:</b> Ask students which they would rather build, a castle or a cathedral, and why. Have them write 3–4 sentences."])

import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEACHER = os.path.join(ROOT, "downloads/integrated/grade4-art-medieval-teacher.pdf")
STUDENT = os.path.join(ROOT, "downloads/integrated/grade4-art-medieval-student.pdf")
doc = BaseDocTemplate(TEACHER,
                      pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.7 * inch, bottomMargin=0.8 * inch,
                      title="Castles, Cathedrals & Colorful Glass: Medieval Art and Architecture (Grade 4)", author="VenvLearning")
doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")], onPage=on_page)])
doc.build(story)
# Student copy: everything except the final teacher answer page.
from pypdf import PdfReader, PdfWriter
reader = PdfReader(TEACHER); writer = PdfWriter()
for page in reader.pages[:-1]: writer.add_page(page)
writer.add_metadata({"/Title": "Castles, Cathedrals & Colorful Glass: Medieval Art and Architecture (Grade 4, student)", "/Author": "VenvLearning"})
with open(STUDENT, "wb") as f: writer.write(f)
print(len(reader.pages), "teacher pages,", len(reader.pages) - 1, "student pages")
