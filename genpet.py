#!/usr/bin/env python3
"""Generate the pure-CSS pixel cat (+ mouse) for chiruu12.github.io.

Sprites are ASCII grids; each '#' is one box-shadow pixel of PX px.
Detail layers (eyes, nose, inner ears) are separate box-shadow lists
drawn in their own colors on top of the silhouette. Run this, eyeball
the printed frames, then splice /tmp/pet.css into style.css.
"""

PX = 4  # cat pixel size
MPX = 3  # mouse pixel size

# ---------------------------------------------------------------- walk (facing right)
HEAD = [
    ".##.........##....##......",
    ".##........####..####.....",
    ".##........###########....",
    "..#........###.####.##....",
    "..#.......#############...",
    "..##......#############...",
    "..###....#############....",
    "...####..#############....",
]
BODY = [
    "....##################....",
    "....##################....",
    "....##################....",
    ".....################.....",
]

WALK_A = (
    ["..........................", ".#........................"]
    + HEAD + BODY +
    [
        ".....##..........##.......",
        "....##............##......",
        "....##............##......",
        "...####..........###......",
    ]
)

WALK_B = (
    ["..........................", ".#........................"]
    + HEAD + BODY +
    [
        "......##........##........",
        "......##........##........",
        "......##........##........",
        ".....###........###.......",
    ]
)

# gallop: A = stretched (front paws forward, back paws back), B = gathered
RUN_A = (
    ["..........................", ".#........................"]
    + HEAD + BODY +
    [
        ".....##..........##.......",
        "...###..............###...",
        ".###..................###.",
        "###....................###",
    ]
)

RUN_B = (
    ["..........................", ".#........................"]
    + HEAD + BODY +
    [
        "......##........##........",
        ".....###........###.......",
        "....####........####......",
        "....##............##......",
    ]
)

# ---------------------------------------------------------------- sit (facing forward), paws on ground at row 17
SIT = [
    "..........................",
    "..........................",
    "...........##...##........",
    "..........###..###........",
    "..........#########.......",
    "..........##.###.##.......",
    "..........#########.......",
    "...........#######........",
    "..........#########.......",
    "..........##########......",
    ".........############.....",
    "........##############....",
    ".......################...",
    "......#################...",
    "....###################...",
    "...########..##########...",
    "..########....##########..",
    "..#####################...",
]

def _blink(frame):
    return ["..........#########......." if i == 5 else r for i, r in enumerate(frame)]

SIT_BLINK = _blink(SIT)

# tail flick: right end of the ground tail curls up one row
SIT_TAIL = list(SIT)
SIT_TAIL[16] = "..########....###########."
SIT_TAIL[17] = "..##################......"

# ---------------------------------------------------------------- sleep (loaf, bottom at row 17)
SLEEP = [
    "..........................",
    "..........................",
    "..........................",
    "..........................",
    "..........................",
    "..........................",
    "..........................",
    "..........................",
    "................##........",
    "...............####.......",
    ".....##.......######......",
    "....####.....########.....",
    "...####################...",
    "..#####################...",
    ".#######################..",
    ".#######################..",
    ".#######################..",
    "..#####################...",
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

# walk/run face: eyes (5,13)+(5,18), nose (6,22), inner ears (3,11-12)+(3,17-18)
FACE = (
    [px(13, 5, GREEN), px(13, 5, GREEN, 6), px(18, 5, GREEN), px(18, 5, GREEN, 6)]
    + [px(22, 6, PINK)]
    + [px(11, 3, PINK), px(12, 3, PINK), px(17, 3, PINK), px(18, 3, PINK)]
)

# sit face: eyes (5,12)+(5,16), nose (6,14), inner ears (3,11)+(3,16)
SIT_FACE = (
    [px(12, 5, GREEN), px(12, 5, GREEN, 6), px(16, 5, GREEN), px(16, 5, GREEN, 6)]
    + [px(14, 6, PINK)]
    + [px(11, 3, PINK), px(16, 3, PINK)]
)
SIT_FACE_CLOSED = [e for e in SIT_FACE if GREEN not in e]

# mouse eye at (2,8)
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
    for n, f in [("WALK_A", WALK_A), ("WALK_B", WALK_B), ("RUN_A", RUN_A), ("RUN_B", RUN_B),
                 ("SIT", SIT), ("SIT_TAIL", SIT_TAIL), ("SIT_BLINK", SIT_BLINK),
                 ("SLEEP", SLEEP), ("MOUSE_A", MOUSE_A), ("MOUSE_B", MOUSE_B)]:
        show(n, f)

    css = []
    css.append("/* generated by genpet.py - pixel lists, do not hand-edit */")

    css.append(f".s-walk {{\n    box-shadow: {join(shadows(WALK_A), '    ')};\n  }}")
    css.append(
        "@keyframes walk-frames {\n"
        f"    0%, 49.99% {{ box-shadow: {join(shadows(WALK_A))}; transform: translateY(0); }}\n"
        f"    50%, 100% {{ box-shadow: {join(shadows(WALK_B))}; transform: translateY(-2px); }}\n"
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
        f"    70%, 86.99% {{ box-shadow: {join(shadows(SIT))}; }}\n"
        f"    87%, 100% {{ box-shadow: {join(shadows(SIT_BLINK))}; }}\n"
        "  }"
    )

    css.append(f".d-sit {{\n    box-shadow: {join(SIT_FACE, '    ')};\n  }}")
    css.append(
        "@keyframes sit-face-frames {\n"
        f"    0%, 86.99% {{ box-shadow: {join(SIT_FACE)}; }}\n"
        f"    87%, 100% {{ box-shadow: {join(SIT_FACE_CLOSED)}; }}\n"
        "  }"
    )

    css.append(f".s-sleep {{\n    box-shadow: {join(shadows(SLEEP), '    ')};\n  }}")

    css.append(f".pet-mouse {{\n    box-shadow: {join(shadows(MOUSE_A, MPX, 'var(--pet-mouse-color)') + [MOUSE_EYE], '    ')};\n  }}")
    css.append(
        "@keyframes mouse-frames {\n"
        f"    0%, 49.99% {{ box-shadow: {join(shadows(MOUSE_A, MPX, 'var(--pet-mouse-color)') + [MOUSE_EYE])}; transform: translateY(0); }}\n"
        f"    50%, 100% {{ box-shadow: {join(shadows(MOUSE_B, MPX, 'var(--pet-mouse-color)') + [MOUSE_EYE])}; transform: translateY(-1px); }}\n"
        "  }"
    )

    with open("/tmp/pet.css", "w") as fh:
        fh.write("\n\n  ".join(css) + "\n")
    print("wrote /tmp/pet.css")
