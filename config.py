#!/usr/bin/python3

import pygame


# ------------------------------------------
# Token images
# ------------------------------------------

YELLOW_TOKEN_IMAGE = pygame.image.load("resources/img/token/YellowToken.png")
BLUE_TOKEN_IMAGE = pygame.image.load("resources/img/token/BlueToken.png")
RED_TOKEN_IMAGE = pygame.image.load("resources/img/token/RedToken.png")
GREEN_TOKEN_IMAGE = pygame.image.load("resources/img/token/GreenToken.png")

def _getColorTokenImage(color):
    if (color == "green"):
        return GREEN_TOKEN_IMAGE
    elif (color == "red"):
        return RED_TOKEN_IMAGE
    elif (color == "blue"):
        return BLUE_TOKEN_IMAGE
    elif (color == "yellow"):
        return YELLOW_TOKEN_IMAGE
    else:
        raise ValueError("Not a supported color: " + color)

# ------------------------------------------
# Player and token classes
# ------------------------------------------

def areCoordsEqual(coords, otherCoords):
    return coords[0] == otherCoords[0] and coords[1] == otherCoords[1]

class Player:
    def __init__(self, color):
        self.color = color
        
    def allTokensInTheYard(self):
        allTokensForPlayer = TOKENS_BY_COLOR[self.color]
            
        allInYard = True
        for token in allTokensForPlayer:
            allInYard = allInYard and token.isInTheYard()
                
        return allInYard
    
    def getColorPrefix(self):
        return "[" + "{:<7}".format(self.color) + "] "
    
class Token:
    def __init__(self, player, coord, backHome):
        self.player = player
        self.coord = [coord[0], coord[1]]
        self.backHome = backHome
        self.tokenImage = _getColorTokenImage(player.color)
        
    def isInTheYard(self):
        for coords in START_STORAGE_COORDS[self.player.color]:
            if areCoordsEqual(self.coord, coords):
                return True
        
        return False

    def moveToFirstPosition(self):
        self.coord[0] = START_POSITION_COORDS[self.player.color][0]
        self.coord[1] = START_POSITION_COORDS[self.player.color][1]

    def moveTo(self, coord):
        self.coord[0] = coord[0]
        self.coord[1] = coord[1]

    def moveToYard(self):
        # find the first free yard spot
        for yardCoord in START_STORAGE_COORDS[self.player.color]:
            positionTaken = False
            for teamToken in TOKENS_BY_COLOR[self.player.color]:
                if areCoordsEqual(teamToken.coord, yardCoord):
                     positionTaken = True
                     break

            if not positionTaken:
                self.moveTo(yardCoord)
                return
            
        raise ValueError(self.player.getColorPrefix() + "You're asking to move to the yard but there are no free spots in the yard. ")
        
                
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
    newX = CENTER_Pos[0] - y
    newY = CENTER_Pos[1] + x
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
]
BLUE_TRACK = rotateTrack(YELLOW_TRACK)
RED_TRACK = rotateTrack(BLUE_TRACK)
GREEN_TRACK = rotateTrack(RED_TRACK)

START_STORAGE_COORDS = {
    "yellow": YELLOW_Start_Storage,
    "blue": BLUE_Start_Storage,
    "red": RED_Start_Storage,
    "green": GREEN_Start_Storage
    }

START_POSITION_COORDS = {
    "yellow": YELLOW_Start,
    "blue": BLUE_Start,
    "red": RED_Start,
    "green": GREEN_Start
    }

MAP = YELLOW_TRACK + BLUE_TRACK + RED_TRACK + GREEN_TRACK

Players = [
    Player("yellow"),
    Player("blue"),
    Player("red"),
    Player("green"), 
]

TOKENS_BY_COLOR = {
    "yellow": [],
    "blue": [],
    "red": [],
    "green": [],
    }
 
for player in Players:
    for coord in START_STORAGE_COORDS[player.color]:
        TOKENS_BY_COLOR[player.color].append(Token(player, coord, False))

CurrentPos = -1