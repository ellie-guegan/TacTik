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
YELLOW_Start = [550, 418]
YELLOW_Start_Storage = [
    [619, 352],
    [619, 386],
    [619, 418],
    [619, 457],
]
YELLOW_End_Storage = [
    [503, 417],
    [503, 467],
    [503, 517],
    [503, 566],
]

YELLOW_Play = 0

# 2 -> Blue
BLUE_Start = rotateCoord(YELLOW_Start)
BLUE_Start_Storage = rotateTrack(YELLOW_Start_Storage)
BLUE_End_Storage = rotateTrack(YELLOW_End_Storage)

BLUE_Play = 0

# 3 -> Red
RED_Start = rotateCoord(BLUE_Start)
RED_Start_Storage = rotateTrack(BLUE_Start_Storage)
RED_End_Storage = rotateTrack(BLUE_End_Storage)

RED_Play = 0

# 4 -> Green
GREEN_Start = rotateCoord(RED_Start)
GREEN_Start_Storage = rotateTrack(RED_Start_Storage)
GREEN_End_Storage = rotateTrack(RED_End_Storage)

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
    ["GREEN", GREEN_Start_Storage[0][0], GREEN_Start_Storage[0][1], False],
    ["GREEN", GREEN_Start_Storage[1][0], GREEN_Start_Storage[1][1], False],
    ["GREEN", GREEN_Start_Storage[2][0], GREEN_Start_Storage[2][1], False],
    ["GREEN", GREEN_Start_Storage[3][0], GREEN_Start_Storage[3][1], False],

    ["RED", RED_Start_Storage[0][0], RED_Start_Storage[0][1], False],
    ["RED", RED_Start_Storage[1][0], RED_Start_Storage[1][1], False],
    ["RED", RED_Start_Storage[2][0], RED_Start_Storage[2][1], False],
    ["RED", RED_Start_Storage[3][0], RED_Start_Storage[3][1], False],

    ["BLUE", BLUE_Start_Storage[0][0], BLUE_Start_Storage[0][1], False],
    ["BLUE", BLUE_Start_Storage[1][0], BLUE_Start_Storage[1][1], False],
    ["BLUE", BLUE_Start_Storage[2][0], BLUE_Start_Storage[2][1], False],
    ["BLUE", BLUE_Start_Storage[3][0], BLUE_Start_Storage[3][1], False],

    ["YELLOW", YELLOW_Start_Storage[0][0], YELLOW_Start_Storage[0][1], False],
    ["YELLOW", YELLOW_Start_Storage[1][0], YELLOW_Start_Storage[1][1], False],
    ["YELLOW", YELLOW_Start_Storage[2][0], YELLOW_Start_Storage[2][1], False],
    ["YELLOW", YELLOW_Start_Storage[3][0], YELLOW_Start_Storage[3][1], False],
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