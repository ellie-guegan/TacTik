#!/usr/bin/python3

import pygame

# ------------------------------------------
# Track coordinates calculations
# ------------------------------------------
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

# ------------------------------------------
# Background hardcoded coordinates
# ------------------------------------------

CENTER_Pos = [330, 335]

# 1 -> Yellow
YELLOW_Pos = [
    [503, 417],
    [503, 467],
    [503, 517],
    [503, 566],
]
YELLOW_Start = [550, 418]
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
    ["GREEN", GREEN_Pos[3][0], GREEN_Pos[3][1], False],

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

# ------------------------------------------
# Token images
# ------------------------------------------

YELLOW_TOKEN_IMAGE = pygame.image.load("resources/img-ludo/pion_yellow0.png")
BLUE_TOKEN_IMAGE = pygame.image.load("resources/img-ludo/pion_blue0.png")
RED_TOKEN_IMAGE = pygame.image.load("resources/img-ludo/pion_red0.png")
GREEN_TOKEN_IMAGE = pygame.image.load("resources/img-ludo/pion_green0.png")

def getPlayerToken(color):
    if (color == "GREEN"):
        return GREEN_TOKEN_IMAGE
    elif (color == "RED"):
        return RED_TOKEN_IMAGE
    elif (color == "BLUE"):
        return BLUE_TOKEN_IMAGE
    else:
        return YELLOW_TOKEN_IMAGE