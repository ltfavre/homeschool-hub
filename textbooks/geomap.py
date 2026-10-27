"""Maps drawn from Natural Earth data (public domain) in geo/geo.json.

geo_map(theme, bounds, ...) returns a Draw flowable. bounds = (west, east, south, north) in degrees."""
import json, math, os
from reportlab.lib import colors
from engine import Draw, W, INK, MUTED, IVORY, text

_GEO = None
WATER = colors.HexColor("#DCEAF2"); LAND = colors.HexColor("#F4EFE6"); BORDER = colors.HexColor("#B9AF9F")
RIVER = colors.HexColor("#5E95BD"); LAKE = colors.HexColor("#C9DFEC")

# U.S. regions as used in the Grade 4 book (the five-region model common in elementary social studies)
US_REGIONS = {
    "Northeast": ["Maine", "New Hampshire", "Vermont", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Pennsylvania",
                  "Delaware", "Maryland"],
    "Southeast": ["West Virginia", "Virginia", "Kentucky", "Tennessee", "North Carolina", "South Carolina", "Georgia", "Florida", "Alabama",
                  "Mississippi", "Louisiana", "Arkansas"],
    "Midwest": ["Ohio", "Michigan", "Indiana", "Illinois", "Wisconsin", "Minnesota", "Iowa", "Missouri", "North Dakota", "South Dakota",
                "Nebraska", "Kansas"],
    "Southwest": ["Oklahoma", "Texas", "New Mexico", "Arizona"],
    "West": ["Colorado", "Wyoming", "Montana", "Idaho", "Utah", "Nevada", "California", "Oregon", "Washington", "Alaska", "Hawaii"],
}


def geo():
    global _GEO
    if _GEO is None:
        _GEO = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo", "geo.json")))
    return _GEO


def place(name):
    """Coordinates for a populated place, e.g. 'Jackson, Mississippi'."""
    return geo()["places"][name]


def geo_map(theme, bounds, width=None, height=None, states=False, focus=None, countries=True, country_borders=False,
            rivers=(), lakes=True, labels=(), title=None, compass=True, scale_miles=None, legend=None, focus_countries=None,
            dim_outside=None, legend_pos="tl"):
    """focus: {state name: color} fills; focus_countries: {country: color}. labels: (text, lon, lat[, style[, dx, dy]]);
    styles: city (dot + label), capital (star + label), region, water (italic blue), big (serif), plain.
    legend: list of (color, label). scale_miles: draw a scale bar of that many miles."""
    w0, e0, s0, n0 = bounds
    width = width or W * 0.92
    k_lat = math.cos(math.radians((s0 + n0) / 2))
    aspect = ((n0 - s0)) / ((e0 - w0) * k_lat)
    height = height or width * aspect
    G = geo()

    def fn(c, w, h):
        top = 18 if title else 0
        mh = h - top
        sx = w / ((e0 - w0) * k_lat); sy = mh / (n0 - s0)

        def P(lon, lat): return (lon - w0) * k_lat * sx, (lat - s0) * sy

        def poly(ring, fill=None, stroke=None, lw=0.5, close=True):
            p = c.beginPath(); x, y = P(*ring[0]); p.moveTo(x, y)
            for q in ring[1:]: p.lineTo(*P(*q))
            if close: p.close()
            if fill is not None: c.setFillColor(fill)
            if stroke is not None: c.setStrokeColor(stroke); c.setLineWidth(lw)
            c.drawPath(p, fill=1 if fill is not None else 0, stroke=1 if stroke is not None else 0)

        def inview(ring):
            xs = [q[0] for q in ring]; ys = [q[1] for q in ring]
            return not (max(xs) < w0 - 1 or min(xs) > e0 + 1 or max(ys) < s0 - 1 or min(ys) > n0 + 1)

        c.saveState()
        if title: text(c, w / 2, h - 12, title, "BodySemi", 10, theme.dark, "c")
        clip = c.beginPath(); clip.rect(0, 0, w, mh); c.clipPath(clip, stroke=0, fill=0)
        c.setFillColor(WATER); c.rect(0, 0, w, mh, fill=1, stroke=0)
        fc = focus_countries or {}
        if countries:
            for name, rs in G["countries"].items():
                for r in rs:
                    if inview(r): poly(r, fc.get(name, LAND), BORDER if country_borders else None, 0.5)
        if states:
            fo = focus or {}
            for name, rs in G["states"].items():
                for r in rs:
                    if inview(r): poly(r, fo.get(name, LAND if not dim_outside else dim_outside), BORDER, 0.5)
            # strengthen focus outlines
            for name in fo:
                for r in G["states"].get(name, []):
                    if inview(r): poly(r, None, theme.dark, 1.1)
        if lakes:
            for name, rs in G["lakes"].items():
                for r in rs:
                    if inview(r): poly(r, LAKE, RIVER, 0.3)
        for rv in rivers:
            for r in G["rivers"].get(rv, []):
                if inview(r): poly(r, None, RIVER, 1.3, close=False)
        c.restoreState()
        c.saveState()
        # labels
        for lab in labels:
            txt, lon, lat = lab[:3]; style = lab[3] if len(lab) > 3 else "city"; dx = lab[4] if len(lab) > 4 else 0; dy = lab[5] if len(lab) > 5 else 0
            x, y = P(lon, lat); y += 0
            if style == "city":
                c.setFillColor(INK); c.circle(x, y, 2.3, fill=1, stroke=0)
                text(c, x + 5 + dx, y - 3 + dy, txt, "BodyMed", 7.5, INK, "l" if dx >= 0 else "r")
            elif style == "capital":
                c.setFillColor(theme.dark); c.setStrokeColor(WHITE_); c.setLineWidth(0.6); star(c, x, y, 5)
                text(c, x + 7 + dx, y - 3 + dy, txt, "BodySemi", 8, INK, "l" if dx >= 0 else "r")
            elif style == "water":
                text(c, x + dx, y + dy, txt, "DisplayIt", 9, colors.HexColor("#2F6B93"), "c")
            elif style == "region":
                text(c, x + dx, y + dy, txt, "BodyBold", 8.5, theme.dark, "c")
            elif style == "big":
                text(c, x + dx, y + dy, txt, "Display", 12, theme.dark, "c")
            else:
                text(c, x + dx, y + dy, txt, "Body", 7.5, MUTED, "c")
        c.setStrokeColor(theme.dark); c.setLineWidth(0.8); c.rect(0, 0, w, mh, fill=0, stroke=1)
        if compass:
            cx, cy = w - 18, mh - 26
            c.setFillColor(theme.dark); p = c.beginPath(); p.moveTo(cx, cy + 12); p.lineTo(cx + 5, cy - 4); p.lineTo(cx, cy); p.lineTo(cx - 5, cy - 4); p.close()
            c.drawPath(p, fill=1, stroke=0); text(c, cx, cy + 15, "N", "BodyBold", 8, theme.dark, "c")
        if scale_miles:
            km = scale_miles * 1.609; deg = km / 111.0      # degrees of latitude
            L = deg * sy; x0, y0 = 10, 10
            c.setFillColor(colors.Color(1, 1, 1, alpha=0.85)); c.rect(x0 - 4, y0 - 4, L + 52, 16, fill=1, stroke=0)
            c.setStrokeColor(INK); c.setLineWidth(1.2); c.line(x0, y0, x0 + L, y0); c.line(x0, y0 - 2, x0, y0 + 3); c.line(x0 + L, y0 - 2, x0 + L, y0 + 3)
            text(c, x0 + L + 5, y0 - 3, f"{scale_miles} miles", "Body", 7, INK)
        if legend:
            bw = max(len(l) for _, l in legend) * 4.6 + 26
            lx, ly = (8, mh - 14) if legend_pos == "tl" else (w - bw - 4, 13 * len(legend) - 2)
            c.setFillColor(colors.Color(1, 1, 1, alpha=0.9)); c.rect(lx - 3, ly - 13 * len(legend) + 9, bw, 13 * len(legend) + 2, fill=1, stroke=0)
            for i, (col, l) in enumerate(legend):
                c.setFillColor(col); c.setStrokeColor(BORDER); c.rect(lx, ly - i * 13, 10, 8, fill=1, stroke=1)
                text(c, lx + 15, ly - i * 13 + 1, l, "Body", 7.5, INK)
        c.restoreState()
    return Draw(width, height + (18 if title else 0), fn)


WHITE_ = colors.white


def star(c, x, y, r):
    p = c.beginPath()
    for i in range(10):
        a = math.radians(90 + i * 36); rr = r if i % 2 == 0 else r * 0.45
        (p.moveTo if i == 0 else p.lineTo)(x + rr * math.cos(a), y + rr * math.sin(a))
    p.close(); c.drawPath(p, fill=1, stroke=1)


REGION_COLORS = {"Northeast": colors.HexColor("#E7C7A6"), "Southeast": colors.HexColor("#F0B58A"), "Midwest": colors.HexColor("#E9D79A"),
                 "Southwest": colors.HexColor("#D9A38E"), "West": colors.HexColor("#C9D2A4")}


def us_regions_map(theme, highlight=None, width=None, labels=True, title=None):
    """Contiguous U.S. colored by region. highlight: one region name to emphasize (others pale)."""
    focus = {}
    for reg, sts in US_REGIONS.items():
        col = REGION_COLORS[reg]
        if highlight and reg != highlight: col = colors.HexColor("#EFE9DF")
        for s in sts: focus[s] = col
    labs = []
    if labels:
        pos = {"Northeast": (-74.5, 43.6), "Southeast": (-84.5, 33.5), "Midwest": (-92.5, 43.0), "Southwest": (-104.5, 33.0), "West": (-115.5, 42.5)}
        labs = [(r.upper(), *xy, "region") for r, xy in pos.items() if not highlight or r == highlight]
    return geo_map(theme, (-125, -66.5, 24, 50), width=width, states=True, focus=focus, labels=labs, title=title,
                   legend=None if highlight else [(REGION_COLORS[r], r) for r in US_REGIONS], scale_miles=500, legend_pos="br")


def mississippi_map(theme, width=None, cities=True, rivers=("Mississippi", "Pearl", "Tombigbee"), extra_labels=(), title=None, height=None,
                    focus_fill=None):
    names = ["Jackson", "Tupelo", "Hattiesburg", "Gulfport", "Biloxi", "Meridian", "Vicksburg", "Natchez", "Greenville", "Southaven"]
    labs = []
    if cities:
        for n in names:
            lon, lat = place(f"{n}, Mississippi")
            dx = -10 if n == "Gulfport" else 0
            labs.append((n, lon, lat, "capital" if n == "Jackson" else "city", dx, -8 if n == "Biloxi" else 0))
    labs += list(extra_labels)
    return geo_map(theme, (-92.2, -87.6, 29.9, 35.3), width=width or W * 0.55, height=height, states=True,
                   focus={"Mississippi": focus_fill or theme.wash}, rivers=rivers, labels=labs, title=title, scale_miles=50,
                   dim_outside=colors.HexColor("#EDE8DF"))
