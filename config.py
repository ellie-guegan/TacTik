#!/usr/bin/python3


# Function For Track Coordinates Calculations
def rotateTrack(track):
    newTrack = []
    for i in track:
        newTrack.append(rotateCoord(i))
    return newTrack

def rotateCoord(coord):
    x = coord[0] - CENTER_Pos[0]
    y = coord[1] - CENTER_Pos[1]
    newX = CENTER_Pos[0]-y
    newY = CENTER_Pos[1]+x
    return [newX, newY]

CENTER_Pos = [330, 335]

# 1 -> Yellow
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

# 2 -> Blue
BLUE_Pos = rotateTrack(YELLOW_Pos)
BLUE_Start = rotateCoord(YELLOW_Start)

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

# 3 -> Red
RED_Pos = rotateTrack(BLUE_Pos)
RED_Start = rotateCoord(BLUE_Start)

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

# 4 -> Green
GREEN_Pos = rotateTrack(RED_Pos)
GREEN_Start = rotateCoord(RED_Start)

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

YELLOW_TRACK = [
    YELLOW_Start,
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
    [247, 542]
]
BLUE_TRACK = rotateTrack(YELLOW_TRACK)
RED_TRACK = rotateTrack(BLUE_TRACK)
GREEN_TRACK = rotateTrack(RED_TRACK)


MAP = YELLOW_TRACK + BLUE_TRACK + RED_TRACK + GREEN_TRACK

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

    