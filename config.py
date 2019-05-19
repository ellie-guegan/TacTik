#!/usr/bin/python3

# 1 -> Green
GREEN_Pos = [
    [163, 123],
    [125, 161],
    [201, 161],
    [163, 199],
]
GREEN_Start = [106, 294]
GREEN_Win = [
    [106, 333],
    [144, 333],
    [182, 333],
    [220, 333],
    [258, 333],
]
GREEN_End = [
    [296, 355],
    [296, 340],
    [296, 325],
    [296, 310],
]
GREEN_Play = 0

# 2 -> Red
RED_Pos = [
    [506, 123],
    [468, 161],
    [544, 161],
    [506, 199],
]
RED_Start = [372, 104]
RED_Win = [
    [334, 104],
    [334, 142],
    [334, 180],
    [334, 218],
    [334, 256],
]
RED_End = [
    [300, 285],
    [320, 285],
    [340, 285],
    [372, 285],
]
RED_Play = 0

# 3 -> Blue
BLUE_Pos = [
    [506, 466],
    [468, 504],
    [544, 504],
    [506, 542],
]
BLUE_Start = [563, 371]
BLUE_Win = [
    [563, 333],
    [525, 333],
    [487, 333],
    [449, 333],
    [411, 333],
]
BLUE_End = [
    [372, 347],
    [372, 332],
    [372, 317],
    [372, 302],
]
BLUE_Play = 0

# 4 -> Yellow
YELLOW_Pos = [
    [503, 417],
    [503, 467],
    [503, 517],
    [503, 566],
]
YELLOW_Start = [550, 418]
YELLOW_Win = [
    [334, 561],
    [334, 523],
    [334, 485],
    [334, 447],
    [334, 409],
]
YELLOW_End = [
    [305, 370],
    [325, 370],
    [345, 370],
    [365, 370],
]
YELLOW_Play = 0


MAP = [
    GREEN_Start,     # START GREEN  [0]
    [144, 294],
    [182, 294],
    [220, 294],
    [258, 294],
    [296, 256],
    [296, 218],
    [296, 180],
    [296, 142],
    [296, 104],
    [296, 66],
    [334, 66],
    [372, 66],

    RED_Start,      # START RED  [13]
    [372, 142],
    [372, 180],
    [372, 218],
    [372, 256],
    [411, 294],
    [449, 294],
    [487, 294],
    [525, 294],
    [563, 294],
    [601, 294],
    [601, 333],
    [601, 371],

    BLUE_Start,     # START BLUE [27]
    [525, 371],
    [487, 371],
    [449, 371],
    [411, 371],
    [372, 409],
    [372, 447],
    [372, 485],
    [372, 523],
    [372, 561],
    [372, 599],
    [334, 599],
    [296, 599],

    YELLOW_Start,     # START YELLOW [40]
    [550, 468],
    [550, 518],
    [598, 518],
    [645, 518],
    [645, 567],
    [645, 617],
    [599, 637],
    [549, 637],
    [501, 637],
    [451, 637],
    [403, 637],
    [353, 637],
    [353, 592],
    [353, 542],
    [302, 542],
    [247, 542],
]

ITEMS_Pos = [
    ["GREEN", GREEN_Pos[0][0], GREEN_Pos[0][1], False],
    ["GREEN", GREEN_Pos[1][0], GREEN_Pos[1][1], False],
    ["GREEN", GREEN_Pos[2][0], GREEN_Pos[2][1], False],
    ["GREEN", GREEN_Pos[3][0], GREEN_Pos[3][1]],

    ["RED", RED_Pos[0][0], RED_Pos[0][1], False],
    ["RED", RED_Pos[1][0], RED_Pos[1][1], False],
    ["RED", RED_Pos[2][0], RED_Pos[2][1], False],
    ["RED", RED_Pos[3][0], RED_Pos[3][1], False],

    ["BLUE", BLUE_Pos[0][0], BLUE_Pos[0][1], False],
    ["BLUE", BLUE_Pos[1][0], BLUE_Pos[1][1], False],
    ["BLUE", BLUE_Pos[2][0], BLUE_Pos[2][1], False],
    ["BLUE", BLUE_Pos[3][0], BLUE_Pos[3][1], False],

    ["YELLOW", YELLOW_Pos[0][0], YELLOW_Pos[0][1], False],
    ["YELLOW", YELLOW_Pos[1][0], YELLOW_Pos[1][1], False],
    ["YELLOW", YELLOW_Pos[2][0], YELLOW_Pos[2][1], False],
    ["YELLOW", YELLOW_Pos[3][0], YELLOW_Pos[3][1], False],
]

CurrentPos = -1
MaxPos = 4

PList = [
    "GREEN", 
    "RED",
    "BLUE",
    "YELLOW",
]
