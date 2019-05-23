#!/usr/bin/python3

# imports
import time
import pygame
import random

import audio as a
import config

from tkinter import messagebox
from enum import Enum

class GameStatus(Enum):
    WAITING_FOR_DICE_ROLL = 1
    WAITING_FOR_TOKEN_SELECTION = 2

# Ludo Functions
class Ludo:
    def __init__(self, screen, gameDisplay, bg):
        
        self.screen = screen
        self.gameDisplay = gameDisplay
        self.bg = bg
        self.sound = a.Audio()
        self.topMessage = "Start the game."
        self.bottomMessage = ""

        self.gameStatus = GameStatus.WAITING_FOR_DICE_ROLL
        self.currentHasMoved = True
        self.dice = 0
        
        self.imgdiceEffect = [
            pygame.image.load("resources/img-ludo/dice_0_1.png"),
            pygame.image.load("resources/img-ludo/dice_0_2.png"),
            pygame.image.load("resources/img-ludo/dice_0_3.png"),
            pygame.image.load("resources/img-ludo/dice_0_4.png"),
        ]
        
        self.imgdice = [
            self.imgdiceEffect[0],
            pygame.image.load("resources/img-ludo/dice_1.png"),
            pygame.image.load("resources/img-ludo/dice_2.png"),
            pygame.image.load("resources/img-ludo/dice_3.png"),
            pygame.image.load("resources/img-ludo/dice_4.png"),
            pygame.image.load("resources/img-ludo/dice_5.png"),
            pygame.image.load("resources/img-ludo/dice_6.png"),
        ]
        
        self.font = pygame.font.SysFont("comicsansms", 20)


    def refreshDisplay(self):
        self.displayTokens()
        self.renderMessages()
        self.DisplayCurrentDice()
        
    def print(self, text = "", text2 = ""):
        return print("[TacTik]: " +str(text)+ " " +str(text2))


    def setTopMessage(self, text = ""):
        self.topMessage = text

    def setBottomMessage(self, text = ""):
        self.bottomMessage = text

    def renderMessages(self):
        renderedText = self.font.render(self.topMessage, True, (0, 60, 0))
        self.screen.blit(renderedText, (config.CENTER_Pos[0], config.CENTER_Pos[1] - 40))
        renderedText = self.font.render(self.bottomMessage, True, (255, 0, 0))
        self.screen.blit(renderedText, (config.CENTER_Pos[0], config.CENTER_Pos[1] + 40))


    def DisplayCurrentDice(self):
        self.screen.blit(self.imgdice[self.dice], (325, 325))
        
    def incrementPlayer(self):
        config.CurrentPos += 1   
        if (config.CurrentPos >= len(config.Players)):
            config.CurrentPos = 0
        
        player = config.Players[config.CurrentPos]
        self.setTopMessage("It's his turn: " + str(player.color))
        
    def getCurrentPlayer(self):
        return config.Players[config.CurrentPos]
        

    # Click function
    def Click_Event(self, event):
        self.setBottomMessage("")
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.print("     ------------ a CLICK was made --------------------------")
            x, y = pygame.mouse.get_pos()
            # Waiting on the DICE
            if (self.gameStatus == GameStatus.WAITING_FOR_DICE_ROLL):
                # Check the dice
                if (x >= 295 and x < 405 and y >= 295 and y < 405):
                    self.Play()
                    self.print ("You clicked on the dice, with result: ", self.dice)
                    self.checkValidMoves()
                else:
                    self.print ("You didn't click on the dice")
                    self.setBottomMessage("Please hit the dice!")
            # Waiting on a TOKEN
            elif (self.gameStatus == GameStatus.WAITING_FOR_TOKEN_SELECTION):
                for token in config.TOKENS_BY_COLOR[self.getCurrentPlayer().color]:
                    pX = token.coord[0]
                    pY = token.coord[1]
                    if (x >= pX and x < pX + 35 and y >= pY and y < pY + 35):
                        self.print ("Found a token you clicked on!")
                        self.Click_Pion(token)
                        return
                self.setBottomMessage("Please click on one of your team's tokens. They're " + self.getCurrentPlayer().color + "...")
                self.print ("You didn't click on any of your team's tokens.")
            else:
                raise ValueError("Unknown game status: " + self.gameStatus)

    def Key_Event(self):
        self.print("     ------------ a KEY was pressed --------------------------")
        self.Play()
        self.print ("[Space] You dared with the dice: ", self.dice)
        self.checkValidMoves()

        #time.sleep(0.5)

    def displayTokens(self):
        for tokens in config.TOKENS_BY_COLOR.values():
            for token in tokens:
                self.screen.blit(token.tokenImage, (token.coord[0], token.coord[1]))
    
    def Play(self):
        if (self.currentHasMoved == True):
            # move to next player
            self.incrementPlayer()

            self.sound.PlayDice()
            self.dice = random.randint(1, 6)
            self.print("Random dice roll yielded: " + str(self.dice))
            self.gameStatus = GameStatus.WAITING_FOR_TOKEN_SELECTION

            self.currentHasMoved = False
        else:
            self.print("Waiting for: " + str(config.Players[config.CurrentPos].color))

    def checkValidMoves(self):
        player = self.getCurrentPlayer()

        if (self.dice < 6):
            # checking whether all tokens are at the start point
            allTokensForPlayer = config.TOKENS_BY_COLOR[player.color]
            
            allInYard = True
            for token in allTokensForPlayer:
                allInYard = allInYard and token.isInTheYard()
                    
            if (allInYard):
                self.print(player.color + ": There are no moves available, all tokens are in the yard.")
                self.currentHasMoved = True
                self.gameStatus = GameStatus.WAITING_FOR_DICE_ROLL
                return False
            else:
                self.print(player.color + ": Has some tokens out")
        
        else:
            self.print("Dice " + str(self.dice))
            return False


    def Click_Pion(self, token):
        if (self.currentHasMoved == True):
            self.print("[Click_Pion] The selected pawn cannot be moved.")
            return 0

        if (token.isInTheYard() and self.dice == 6):
            token.moveToFirstPosition()
            self.sound.PlayStart()
            self.print("[Click_Pion] " + token.player.color + ": The pawn came out of the house.")
            self.currentHasMoved = True
            self.gameStatus = GameStatus.WAITING_FOR_DICE_ROLL
            return 0
        else:
            self.print("[Click_Pion] " + token.player.color + ": try", self.dice)
            self.MoveToNext(token)
            self.gameStatus = GameStatus.WAITING_FOR_DICE_ROLL

        self.print("")

    def MoveToNext(self, token):
        x = token.coord[0]
        y = token.coord[1]

        currentIndexInMap = -1
        for i in range(0, len(config.MAP)):
            if (config.MAP[i][0] == x and config.MAP[i][1] == y):
                currentIndexInMap = i

        if (currentIndexInMap == -1):
            self.print("The selected pawn cannot be moved (didn't find it in the map).")
            return 0
        
        if (currentIndexInMap + self.dice >= len(config.MAP)):
            self.print("The token has exceeded the map, goes back around for a loop!")
            nextIndexInMap = currentIndexInMap + self.dice - len(config.MAP)
            self.print("CurrentIndex " + str(currentIndexInMap) + " dice " + str(self.dice) + " length " + str(len(config.MAP)) + " ---> next index " + str(nextIndexInMap))
        else:
            nextIndexInMap = currentIndexInMap + self.dice

        print("Moving token from " + str(token.coord) + " to " + str(config.MAP[nextIndexInMap]))
        token.moveTo(config.MAP[nextIndexInMap])
        self.sound.PlayMove()
        self.currentHasMoved = True

    def Unlock_Move(self):
        if (self.currentHasMoved == False):
            self.print("Next PLAYER.")
            self.currentHasMoved = True
            

    