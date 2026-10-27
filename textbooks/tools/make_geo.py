"""Extract a compact map dataset (textbooks/geo/geo.json) from Natural Earth GeoJSON (public domain).

python3 textbooks/tools/make_geo.py /path/to/natural-earth-vector/geojson
Source: https://github.com/nvkelso/natural-earth-vector (Natural Earth, public domain)."""
import json, os, sys, math

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "geo", "geo.json")

RIVERS = ["Mississippi", "Missouri", "Ohio", "Tennessee", "Pearl", "Tombigbee", "Arkansas", "Red", "Colorado", "Rio Grande",
          "Columbia", "Hudson", "Nile", "Tigris", "Euphrates", "Indus", "Ganges", "Huang", "Yangtze", "Chang Jiang", "Niger",
          "Rhine", "Danube", "Rhône", "Seine", "Thames", "Volga", "Jordan", "Congo", "Senegal", "Po", "Tiber", "Amazon", "Sacramento"]


def dp(pts, tol):
    """Douglas–Peucker simplification."""
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]; dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1e-12
    imax, dmax = 0, 0.0
    for i in range(1, len(pts) - 1):
        p = pts[i]
        d = abs(dy * p[0] - dx * p[1] + b[0] * a[1] - b[1] * a[0]) / L if (dx or dy) else math.hypot(p[0] - a[0], p[1] - a[1])
        if d > dmax: imax, dmax = i, d
    if dmax <= tol: return [a, b]
    return dp(pts[:imax + 1], tol)[:-1] + dp(pts[imax:], tol)


def rings(geom):
    if geom["type"] == "Polygon": return [geom["coordinates"][0]]
    if geom["type"] == "MultiPolygon": return [p[0] for p in geom["coordinates"]]
    if geom["type"] == "LineString": return [geom["coordinates"]]
    if geom["type"] == "MultiLineString": return geom["coordinates"]
    return []


def pack(geom, tol, min_pts=3):
    out = []
    for r in rings(geom):
        s = dp([(round(x, 3), round(y, 3)) for x, y in r], tol)
        if len(s) >= min_pts: out.append([[round(x, 2), round(y, 2)] for x, y in s])
    return out


def load(name): return json.load(open(os.path.join(SRC, name)))


data = {"source": "Natural Earth (public domain), naturalearthdata.com", "states": {}, "countries": {}, "rivers": {}, "lakes": {}, "places": {}}
for f in load("ne_50m_admin_1_states_provinces.geojson")["features"]:
    p = f["properties"]
    if p.get("iso_a2") == "US": data["states"][p["name"]] = pack(f["geometry"], 0.02)
for f in load("ne_50m_admin_0_countries.geojson")["features"]:
    p = f["properties"]; data["countries"][p["NAME"]] = pack(f["geometry"], 0.04)
for f in load("ne_10m_rivers_lake_centerlines.geojson")["features"]:
    n = f["properties"].get("name")
    if n in RIVERS: data["rivers"].setdefault(n, []).extend(pack(f["geometry"], 0.02, 2))
for f in load("ne_50m_lakes.geojson")["features"]:
    n = f["properties"].get("name")
    if n: data["lakes"].setdefault(n, []).extend(pack(f["geometry"], 0.03))
for f in load("ne_10m_populated_places_simple.geojson")["features"]:
    p = f["properties"]
    if p.get("adm0name") == "United States of America" and (p.get("adm1name") == "Mississippi" or p.get("adm0cap") or p.get("rank_max", 0) >= 11 or p.get("featurecla") == "Admin-1 capital"):
        data["places"][f"{p['name']}, {p['adm1name']}"] = [round(p["longitude"], 3), round(p["latitude"], 3)]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(data, open(OUT, "w"), separators=(",", ":"))
print(OUT, os.path.getsize(OUT) // 1024, "KB", len(data["states"]), "states", len(data["countries"]), "countries", sorted(data["rivers"]))
