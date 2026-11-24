#!/usr/bin/env python3
"""Build the 1024x1024 'world news of 23 Nov 2026 in one image' artwork.

Deterministic: pure PIL drawing, fixed geometry, no randomness, no clock.
Output: world-news-2026-11-23.png next to this script.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "world-news-2026-11-23.png")

W = H = 1024
PAPER = (247, 243, 234)
INK = (20, 24, 38)
MUTED = (92, 96, 110)
CARD = (255, 255, 255)
ACCENT = (178, 34, 52)      # headline red
SEA = (23, 78, 122)
SAND = (233, 220, 194)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def centered(text, font, y, fill=INK):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


# ---------- masthead ----------
centered("THE WORLD IN ONE IMAGE", F(SERIF_B, 58), 26)
centered("Monday, 23 November 2026  ·  The day's biggest stories, in a single picture",
         F(SANS, 24), 102, MUTED)
d.line([(36, 148), (W - 36, 148)], fill=INK, width=4)
d.line([(36, 156), (W - 36, 156)], fill=INK, width=1)

# ---------- lead story ----------
lead = (36, 168, W - 36, 424)
d.rounded_rectangle(lead, radius=14, fill=CARD, outline=INK, width=3)
# sea scene (left)
sx0, sy0, sx1, sy1 = 56, 188, 356, 404
d.rectangle((sx0, sy0, sx1, sy1), fill=(196, 224, 238))
# sky sun
d.ellipse((sx0 + 18, sy0 + 14, sx0 + 62, sy0 + 58), fill=(244, 183, 64))
# warship silhouette
ship_y = sy0 + 118
d.polygon([(sx0 + 40, ship_y), (sx0 + 240, ship_y), (sx0 + 218, ship_y + 26),
           (sx0 + 62, ship_y + 26)], fill=(52, 58, 71))
d.rectangle((sx0 + 96, ship_y - 22, sx0 + 168, ship_y), fill=(52, 58, 71))
d.rectangle((sx0 + 122, ship_y - 40, sx0 + 142, ship_y - 22), fill=(52, 58, 71))
d.line([(sx0 + 196, ship_y - 30), (sx0 + 196, ship_y)], fill=(52, 58, 71), width=4)
# sea drone approaching
drone_y = ship_y + 62
d.polygon([(sx0 + 196, drone_y), (sx0 + 252, drone_y), (sx0 + 240, drone_y + 14),
           (sx0 + 206, drone_y + 14)], fill=ACCENT)
d.rectangle((sx0 + 216, drone_y - 10, sx0 + 232, drone_y), fill=ACCENT)
# waves
for r in range(3):
    wy = sy1 - 44 + r * 14
    for wx in range(sx0 + 8, sx1 - 30, 46):
        d.arc((wx, wy, wx + 30, wy + 12), 0, 180, fill=SEA, width=3)
d.rectangle((sx0, sy0, sx1, sy1), outline=INK, width=2)
# lead text
tx = 380
d.text((tx, 186), "WAR AT SEA", font=F(SANS_B, 22), fill=ACCENT)
lh = F(SERIF_B, 37)
y = 216
for line in wrap("Ukraine's sea drones sink Russian warships near Libya", lh, W - 36 - tx - 18):
    d.text((tx, y), line, font=lh, fill=INK)
    y += 45
y += 6
ls = F(SANS, 22)
for line in wrap("Kyiv confirms the strikes, and a Russian cargo ship with "
                 "military ties is also hit in the Baltic.", ls, W - 36 - tx - 18):
    d.text((tx, y), line, font=ls, fill=MUTED)
    y += 28

# ---------- grid panels ----------
panels = [
    ("CLIMATE", ACCENT, "COP31 talks collapse with no deal",
     "Summit ends without agreement after the draft drops language on fossil fuels."),
    ("TECH & MARKETS", (16, 110, 60), "Nvidia brings back Jensen Huang",
     "The board reinstates its co-founder as CEO; shares jump about 30% and stocks surge."),
    ("CRYPTO", (196, 124, 22), "Bitcoin rebounds to $61K",
     "A bounce off a weekend plunge to a two-year low, after its second-longest losing streak ever."),
    ("MIDDLE EAST", (120, 60, 140), "Iran warns US over Hormuz blockade",
     "Tehran threatens to respond 'by every means' to the US naval blockade."),
    ("INDONESIA", (178, 34, 52), "Factory fire: search for the missing",
     "Rescuers keep searching for 34 people missing after a blaze at a candy factory."),
    ("SPORT", (16, 110, 60), "UK to host 2035 Women's World Cup",
     "FIFA confirms the UK as 2035 host; the US will co-host the 2031 edition."),
]
gx0, gy0 = 36, 434
gw, gh, gap = 468, 176, 12
for i, (kicker, kc, head, sub) in enumerate(panels):
    cx = gx0 + (i % 2) * (gw + gap)
    cy = gy0 + (i // 2) * (gh + gap)
    d.rounded_rectangle((cx, cy, cx + gw, cy + gh), radius=12, fill=CARD, outline=INK, width=2)
    d.text((cx + 18, cy + 12), kicker, font=F(SANS_B, 19), fill=kc)
    hy = cy + 40
    hf = F(SANS_B, 25)
    for line in wrap(head, hf, gw - 36):
        d.text((cx + 18, hy), line, font=hf, fill=INK)
        hy += 28
    sf = F(SANS, 19)
    for line in wrap(sub, sf, gw - 36)[:3]:
        d.text((cx + 18, hy + 2), line, font=sf, fill=MUTED)
        hy += 24

# ---------- footer ----------
fy = gy0 + 3 * gh + 2 * gap + 14
d.line([(36, fy), (W - 36, fy)], fill=INK, width=1)
centered("Compiled from the day's wire reports — BBC, Al Jazeera, CoinDesk and UK broadcast coverage.",
         F(SANS, 16), fy + 8, MUTED)

img.save(OUT, format="PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
