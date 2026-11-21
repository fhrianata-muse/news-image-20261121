#!/usr/bin/env python3
"""Draw the entry image for news-image-20261121.

One newspaper front page that sums up the world news of
Saturday 21 November 2026. Every headline below was reported on
21 November 2026 (checked that morning against the day's news
wires and daily roundups). The picture is drawn with Pillow on a
1024 x 1024 canvas: flat colours, big serif headlines, short
labels, so it still reads when shrunk to about 300 pixels wide.

Run:  python3 draw.py   (writes entry.png beside this file)
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024

PAPER = (247, 241, 227)
INK = (20, 20, 20)
RED = (179, 32, 42)
NAVY = (29, 62, 110)
WHITE = (255, 255, 255)
GREY = (92, 88, 80)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w, word by word."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- frame -------------------------------------------------------------
d.rectangle([10, 10, W - 10, H - 10], outline=INK, width=4)
d.rectangle([20, 20, W - 20, H - 20], outline=INK, width=1)

# ---- masthead ----------------------------------------------------------
centered(d, 28, "THE WORLD IN ONE PAGE", font(SERIF_B, 56), INK)
centered(d, 94, "All the day's news that fits on one front page",
         font(SERIF, 21), GREY)

# ---- date banner --------------------------------------------------------
d.rectangle([20, 128, W - 20, 190], fill=RED)
centered(d, 139, "SATURDAY  21 NOVEMBER 2026", font(SANS_B, 40), WHITE)

# ---- lead story ----------------------------------------------------------
LX, LY = 44, 206
d.text((LX, LY), "EUROPE  •  CONFLICT", font=font(SANS_B, 23), fill=RED)
lead_head = font(SERIF_B, 43)
y = text_block(d, LX, LY + 34,
               "Russian missiles land in Poland; NATO cries foul",
               lead_head, INK, 600, 50)
y = text_block(d, LX, y + 10,
               "Two missiles and a suspected drone came down in Poland "
               "amid a heavy barrage on Ukraine. Tusk: deliberate "
               "provocation.",
               font(SANS, 22), INK, 600, 29)

# lead schematic panel: two labelled country boxes, impacts marked
PX, PY, PW, PH = 676, 206, 304, 208
d.rectangle([PX, PY, PX + PW, PY + PH], fill=NAVY)
d.text((PX + 16, PY + 12), "THE LEAD", font=font(SANS_B, 20), fill=WHITE)
d.rectangle([PX + 16, PY + 48, PX + 128, PY + 126], outline=WHITE, width=3)
d.text((PX + 25, PY + 96), "POLAND", font=font(SANS_B, 20), fill=WHITE)
d.rectangle([PX + 146, PY + 48, PX + 288, PY + 126], outline=WHITE, width=3)
d.text((PX + 155, PY + 96), "UKRAINE", font=font(SANS_B, 20), fill=WHITE)
for cx, cy in [(34, 62), (118, 62), (262, 62)]:
    d.ellipse([PX + cx - 8, PY + cy - 8, PX + cx + 8, PY + cy + 8], fill=RED)
    d.line([PX + cx + 22, PY + cy - 24, PX + cx + 4, PY + cy - 4],
           fill=WHITE, width=3)
d.text((PX + 16, PY + 142), "Missiles + drone down",
       font=font(SANS_B, 22), fill=WHITE)
d.text((PX + 16, PY + 172), "in NATO airspace",
       font=font(SANS_B, 22), fill=WHITE)

d.line([44, 450, W - 44, 450], fill=INK, width=3)

# ---- story grid: 3 columns x 3 rows --------------------------------------
CARDS = [
    ("THE HAGUE • JUSTICE", "World Court: Myanmar committed genocide",
     "First state held responsible for genocide; Rohingya to return."),
    ("SHENZHEN • SUMMIT", "Trump, Xi, Putin hold first joint summit",
     "Joint declaration issued, but few concrete results, analysts say."),
    ("NEW YORK • MARKETS", "Wall Street slumps into correction",
     "S&P -3.7%, Nasdaq -5%+ as AI stocks plunge; Nvidia -14%."),
    ("BRUSSELS • POLITICS", "UK and EU sign food, carbon, youth deals",
     "PM Burnham seals three pacts at the Brussels summit."),
    ("HORMUZ • IRAN WAR", "Iran war nears 9th month; tanker ablaze",
     "Trump in no rush to decide; tanker on fire near Hormuz."),
    ("RIYADH • CONFLICT", "Saudis down 3 Houthi missiles on Riyadh",
     "Coalition then strikes Hodeidah port; UN urges calm."),
    ("UNITED STATES • HEALTH", "Pill breakthrough for pancreatic cancer",
     "Trial drug halted tumours in nearly all patients."),
    ("LOS ANGELES • COURTS", "Jury convicts Palisades Fire arsonist",
     "Rinderknecht guilty of starting the deadly blaze."),
    ("TURKIYE • CLIMATE", "COP31 climate talks enter final stage",
     "Fossil fuels and finance top the closing agenda."),
]

GX, GY = 44, 466
CW, CH = 301, 124
GAP = 16
kick_f = font(SANS_B, 19)
head_f = font(SERIF_B, 23)
body_f = font(SANS, 18)
for i, (kick, head, body) in enumerate(CARDS):
    cx = GX + (i % 3) * (CW + GAP)
    cy = GY + (i // 3) * CH
    if i % 3:
        d.line([cx - GAP // 2, cy + 4, cx - GAP // 2, cy + CH - 12],
               fill=GREY, width=1)
    d.text((cx, cy), kick, font=kick_f, fill=RED)
    yy = text_block(d, cx, cy + 23, head, head_f, INK, CW, 26)
    text_block(d, cx, yy + 2, body, body_f, INK, CW, 22)

# ---- bottom row: weather + sport -----------------------------------------
BY = GY + 3 * CH + 12
d.line([44, BY - 8, W - 44, BY - 8], fill=INK, width=3)
half = (W - 88 - GAP) // 2
d.text((44, BY), "ODISHA • WEATHER", font=kick_f, fill=RED)
yy = text_block(d, 44, BY + 23, "Cyclone Akvan lashes Odisha coast",
                head_f, INK, half, 26)
text_block(d, 44, yy + 2,
           "Landfall near Gopalpur: wind, heavy rain.",
           body_f, INK, half, 22)
sx = 44 + half + GAP
d.line([sx - GAP // 2, BY + 4, sx - GAP // 2, BY + 72], fill=GREY, width=1)
d.text((sx, BY), "LAS VEGAS • SPORT", font=kick_f, fill=RED)
yy = text_block(d, sx, BY + 23, "Russell leads Mercedes 1-2",
                head_f, INK, half, 26)
text_block(d, sx, yy + 2,
           "Antonelli 2nd, Norris 3rd in final practice.",
           body_f, INK, half, 22)

# ---- footer ticker ---------------------------------------------------------
FY = H - 84
d.rectangle([20, FY, W - 20, H - 20], fill=INK)
d.text((40, FY + 10),
       "MARKETS  Nikkei -5.06%  •  Gold -4%  •  Brent near $90  •  Sensex +898 pts",
       font=font(SANS_B, 21), fill=WHITE)
d.text((40, FY + 38),
       "ALSO TODAY  EU gives 1bn euros in aid to Ukraine  •  Four nations urge Gaza aid access",
       font=font(SANS, 20), fill=WHITE)

out = Path(__file__).with_name("entry.png")
img.save(out, optimize=True)
print("wrote", out, out.stat().st_size, "bytes")
