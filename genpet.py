#!/usr/bin/env python3
"""Generate the pure-CSS pixel cat (+ mouse) for chiruu12.github.io. v3.

Sprites are ASCII grids; each '#' is one box-shadow pixel of PX px.
Detail layers (glowing eyes, nose, inner ears) are separate box-shadow
lists painted over the silhouette. Run, eyeball the printed frames,
splice /tmp/pet.css into style.css.

Canvas: 28x18, paws on row 17 (the shared ground line).
"""

PX = 4   # cat pixel size
MPX = 3  # mouse pixel size

# ---------------------------------------------------------------- shared parts (facing right)
TAIL = {
    3: "#...........................",
    4: "##..........................",
    5: ".##.........................",
    6: "..##........................",
    7: "...##.......................",
    8: "....##......................",
}

HEAD = {
    2: "...................##..##.......",
    3: "..................###..###......",
    4: "..................########......",
    5: ".................#########......",
    6: ".................##########.....",
    7: ".................##########.....",
    8: "...............#########........",
}

BODY = {
    9:  ".....#############..............",
    10: "....###############.............",
    11: "....###############.............",
    12: "....###############.............",
    13: ".....#############..............",
}

def compose(extra_rows):
    grid = ["............................"] * 0
    rows = {}
    for src in (TAIL, HEAD, BODY, extra_rows):
        for r, line in src.items():
            base = rows.get(r, "............................")
            merged = list(base)
            for i, ch in enumerate(line.rstrip("\n")):
                if i < 28 and ch == "#":
                    merged[i] = "#"
            rows[r] = "".join(merged)
    return [rows.get(r, "............................")[:28] for r in range(18)]

# ---------------------------------------------------------------- walk: 4-frame gait (A contact, B passing, C contact opposite)
LEGS_WALK_A = {
    14: "......##........##............",
    15: ".....##..........##...........",
    16: "....##............##..........",
    17: "...####..........###..........",
}
LEGS_WALK_B = {
    14: ".......##......##.............",
    15: ".......##......##.............",
    16: ".......##......##.............",
    17: "......###......###............",
}
LEGS_WALK_C = {
    14: "......##........##............",
    15: ".......##......##.............",
    16: "........##....##..............",
    17: "......####...####.............",
}

WALK_A = compose(LEGS_WALK_A)
WALK_B = compose(LEGS_WALK_B)
WALK_C = compose(LEGS_WALK_C)

# ---------------------------------------------------------------- run: gallop (stretched / gathered)
LEGS_RUN_A = {
    14: "......##........##............",
    15: "....###..........###..........",
    16: "..###..............###........",
    17: ".###................###.......",
}
LEGS_RUN_B = {
    14: ".......##......##.............",
    15: "......###......###............",
    16: ".....####......####...........",
    17: ".....##..........##...........",
}
RUN_A = compose(LEGS_RUN_A)
RUN_B = compose(LEGS_RUN_B)

# ---------------------------------------------------------------- sit (facing forward)
SIT = [
    "............................",
    "............................",
    "...........##...##..........",
    "..........###..###..........",
    "..........#########.........",
    "..........#########.........",
    "..........#########.........",
    "...........#######..........",
    "..........#########.........",
    "..........##########........",
    ".........############.......",
    "........##############......",
    ".......################.....",
    "......#################.....",
    "....###################.....",
    "...########..##########.....",
    "..########....##########....",
    "..#####################.....",
]

SIT_BLINK = list(SIT)  # eyes are on the detail layer; blink = detail drops eyes
SIT_TAIL = list(SIT)
SIT_TAIL[16] = "..########....###########."
SIT_TAIL[17] = "..##################......"

# ---------------------------------------------------------------- stretch (play bow, facing right)
# butt up with straight hind legs, back sloping down, chin resting over
# front paws extended forward, ears up. Nose tip pink (14,26).
STRETCH_SEGS = {
    2:  [(1, 1)],
    3:  [(1, 2)],
    4:  [(2, 3)],
    5:  [(2, 4)],
    6:  [(2, 7)],
    7:  [(2, 9)],
    8:  [(2, 10)],
    9:  [(2, 11)],
    10: [(2, 12)],
    11: [(2, 13), (20, 20), (24, 24)],
    12: [(3, 14), (19, 21), (23, 25)],
    13: [(3, 16), (18, 25)],
    14: [(3, 17), (18, 26)],
    15: [(3, 5), (19, 26)],
    16: [(3, 5), (17, 25)],
    17: [(3, 6), (16, 22), (24, 27)],
}
STRETCH = []
for r in range(18):
    row = ["."] * 28
    for a, b in STRETCH_SEGS.get(r, []):
        for c in range(a, b + 1):
            row[c] = "#"
    STRETCH.append("".join(row))

# ---------------------------------------------------------------- sleep (loaf, paws at row 17)
SLEEP = [
    "............................",
    "............................",
    "............................",
    "............................",
    "............................",
    "............................",
    "............................",
    "............................",
    "................##..........",
    "...............####.........",
    ".....##.......######........",
    "....####.....########.......",
    "...####################.....",
    "..#####################.....",
    ".#######################....",
    ".#######################....",
    ".#######################....",
    "..#####################.....",
]

# ---------------------------------------------------------------- mouse (facing right), 12x7 at MPX
MOUSE_A = [
    "............",
    ".....#..#...",
    "....#######.",
    ".#########..",
    "#.########..",
    "..#..##..#..",
    "............",
]
MOUSE_B = [
    "............",
    ".....#..#...",
    "....#######.",
    ".#########..",
    "#.########..",
    "...#..##..#.",
    "............",
]

# ---------------------------------------------------------------- detail overlays (cell coords)
GREEN = "#39ff14"
PINK = "#ff6b9d"
RED = "#ff5555"

def px(x, y, color, blur=0):
    b = f" {blur}px" if blur else " 0"
    return f"{x*PX}px {y*PX}px{b} 0 {color}"

# walk/run face: eyes (6,19)+(6,23), nose (7,26), inner ears (3,19)+(3,23)
FACE = (
    [px(19, 6, GREEN), px(19, 6, GREEN, 6), px(23, 6, GREEN), px(23, 6, GREEN, 6)]
    + [px(26, 7, PINK)]
    + [px(19, 3, PINK), px(23, 3, PINK)]
)

# sit face: eyes (5,12)+(5,16), nose (6,14), inner ears (3,11)+(3,16)
SIT_FACE = (
    [px(12, 5, GREEN), px(12, 5, GREEN, 6), px(16, 5, GREEN), px(16, 5, GREEN, 6)]
    + [px(14, 6, PINK)]
    + [px(11, 3, PINK), px(16, 3, PINK)]
)
SIT_FACE_CLOSED = [e for e in SIT_FACE if GREEN not in e]

# stretch face: nose (14,26), inner ears (12,20)+(12,24)
STRETCH_FACE = [px(26, 14, PINK), px(20, 12, PINK), px(24, 12, PINK)]

MOUSE_EYE = f"{8*MPX}px {2*MPX}px 0 0 {RED}"


def shadows(frame, p=PX, color="var(--pet-color)"):
    out = []
    for y, row in enumerate(frame):
        for x, ch in enumerate(row):
            if ch == "#":
                out.append(f"{x*p}px {y*p}px 0 0 {color}")
    return out


def join(lst, indent="      "):
    return (",\n" + indent).join(lst)


def show(name, frame):
    print(f"--- {name} ({len(frame[0])}x{len(frame)}) ---")
    print("   " + "".join(str(i % 10) for i in range(len(frame[0]))))
    for i, row in enumerate(frame):
        print(f"{i:2} {row}")
    print()


if __name__ == "__main__":
    for n, f in [("WALK_A", WALK_A), ("WALK_B", WALK_B), ("WALK_C", WALK_C),
                 ("RUN_A", RUN_A), ("RUN_B", RUN_B),
                 ("SIT", SIT), ("SIT_TAIL", SIT_TAIL),
                 ("STRETCH", STRETCH), ("SLEEP", SLEEP),
                 ("MOUSE_A", MOUSE_A), ("MOUSE_B", MOUSE_B)]:
        show(n, f)

    css = []
    css.append("/* generated by genpet.py - pixel lists, do not hand-edit */")

    css.append(f".s-walk {{\n    box-shadow: {join(shadows(WALK_A), '    ')};\n  }}")
    css.append(
        "@keyframes walk-frames {\n"
        f"    0%, 24.99% {{ box-shadow: {join(shadows(WALK_A))}; transform: translateY(0); }}\n"
        f"    25%, 49.99% {{ box-shadow: {join(shadows(WALK_B))}; transform: translateY(-2px); }}\n"
        f"    50%, 74.99% {{ box-shadow: {join(shadows(WALK_C))}; transform: translateY(0); }}\n"
        f"    75%, 100% {{ box-shadow: {join(shadows(WALK_B))}; transform: translateY(-2px); }}\n"
        "  }"
    )

    css.append(f".s-run {{\n    box-shadow: {join(shadows(RUN_A), '    ')};\n  }}")
    css.append(
        "@keyframes run-frames {\n"
        f"    0%, 49.99% {{ box-shadow: {join(shadows(RUN_A))}; transform: translateY(0); }}\n"
        f"    50%, 100% {{ box-shadow: {join(shadows(RUN_B))}; transform: translateY(-3px); }}\n"
        "  }"
    )

    css.append(f".d-face {{\n    box-shadow: {join(FACE, '    ')};\n  }}")

    css.append(f".s-sit {{\n    box-shadow: {join(shadows(SIT), '    ')};\n  }}")
    css.append(
        "@keyframes sit-frames {\n"
        f"    0%, 34.99% {{ box-shadow: {join(shadows(SIT))}; }}\n"
        f"    35%, 69.99% {{ box-shadow: {join(shadows(SIT_TAIL))}; }}\n"
        f"    70%, 100% {{ box-shadow: {join(shadows(SIT))}; }}\n"
        "  }"
    )

    css.append(f".d-sit {{\n    box-shadow: {join(SIT_FACE, '    ')};\n  }}")
    css.append(
        "@keyframes sit-face-frames {\n"
        f"    0%, 86.99% {{ box-shadow: {join(SIT_FACE)}; }}\n"
        f"    87%, 100% {{ box-shadow: {join(SIT_FACE_CLOSED)}; }}\n"
        "  }"
    )

    css.append(f".s-stretch {{\n    box-shadow: {join(shadows(STRETCH), '    ')};\n  }}")
    css.append(f".d-stretch {{\n    box-shadow: {join(STRETCH_FACE, '    ')};\n  }}")

    css.append(f".s-sleep {{\n    box-shadow: {join(shadows(SLEEP), '    ')};\n  }}")

    css.append(f".pet-mouse-body {{\n    box-shadow: {join(shadows(MOUSE_A, MPX, 'var(--pet-mouse-color)') + [MOUSE_EYE], '    ')};\n  }}")
    css.append(
        "@keyframes mouse-frames {\n"
        f"    0%, 49.99% {{ box-shadow: {join(shadows(MOUSE_A, MPX, 'var(--pet-mouse-color)') + [MOUSE_EYE])}; transform: translateY(0); }}\n"
        f"    50%, 100% {{ box-shadow: {join(shadows(MOUSE_B, MPX, 'var(--pet-mouse-color)') + [MOUSE_EYE])}; transform: translateY(-1px); }}\n"
        "  }"
    )

    with open("/tmp/pet.css", "w") as fh:
        fh.write("\n\n  ".join(css) + "\n")
    print("wrote /tmp/pet.css")
