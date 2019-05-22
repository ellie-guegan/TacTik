#!/usr/bin/python3

# imports
import time
import pygame
import random

import audio as a

from tkinter import messagebox

# Ludo Functions
class Ludo:
    def __init__(self, config, screen, gameDisplay, bg):
        
        self.cf = config
        self.screen = screen
        self.gameDisplay = gameDisplay
        self.bg = bg
        self.sound = a.Audio()

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
        
        self.bkItemPos = self.cf.ITEMS_Pos


    def print(self, text = "", text2 = ""):
        return print("[Ludo]: " +str(text)+ " " +str(text2))


    def displayTopMessage(self, text = ""):
        renderedText = self.font.render(text, True, (0, 60, 0))
        self.screen.blit(renderedText, (78, 640))
        
    def displayBottomMessage(self, text = ""):
        renderedText = self.font.render(text, True, (255, 0, 0))
        self.screen.blit(renderedText, (78, 680))

    def PrintCurrentPlayer(self):
        if (self.cf.CurrentPos == -1):
            text = "Start the game."
        else:
            player = self.cf.PList[self.cf.CurrentPos]
            text = "It's his turn: " + str(player.color)
        self.displayTopMessage(text)

    def DisplayCurrentDice(self):
        self.screen.blit(self.imgdice[self.dice], (325, 325))

    # Click function
    def Click_Event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.print("     ------------ a CLICK was made --------------------------")
            x, y = pygame.mouse.get_pos()

            # Click Pion
            found = -1
            player = self.cf.PList[self.cf.CurrentPos]
            for i in range(0, len(self.cf.ITEMS_Pos)):
                pColor = self.cf.ITEMS_Pos[i].player.color
                pX = self.cf.ITEMS_Pos[i].coord[0]
                pY = self.cf.ITEMS_Pos[i].coord[1]
                if (player.color == pColor and x >= pX and x < pX + 35 and y >= pY and y < pY + 35):
                    found = i
                    break
            if (found > -1):
                self.print ("You clicked on a token of color " + self.cf.ITEMS_Pos[i].player.color)
                self.Click_Pion(found)

            # Check the dice
            if (x >= 295 and x < 405 and y >= 295 and y < 405):
                self.Play()

                self.print ("You clicked on the dice, with result: ", self.dice)

                self.checkValidMoves()

            # Click No Move
            if (x >= 78 and x < 200 and y >= 680 and y < 700):
                self.Unlock_Move()

         
    def Key_Event(self):
        self.print("     ------------ a KEY was pressed --------------------------")
        self.Play()
        self.print ("[Space] You dared with the dice: ", self.dice)
        self.checkValidMoves()

        #time.sleep(0.5)

    def displayTokens(self):
        for token in self.cf.ITEMS_Pos:
            self.screen.blit(token.tokenImage, (token.coord[0], token.coord[1]))
    
    def Play(self):
        if (self.currentHasMoved == True):
            # move to next player
            self.cf.CurrentPos += 1   
            if (self.cf.CurrentPos >= self.cf.MaxPos):
                self.cf.CurrentPos = 0

            self.print("It's his turn: " + self.cf.PList[self.cf.CurrentPos].color)

            self.sound.PlayDice()
            self.dice = random.randint(1, 6)
            self.print("Random dice roll yielded: " + str(self.dice))

            self.currentHasMoved = False
        else:
            self.print("Waiting for: " + str(self.cf.PList[self.cf.CurrentPos].color))

    def checkValidMoves(self):
        player = self.cf.PList[self.cf.CurrentPos]

        if (self.dice < 6):
            # checking whether all tokens are at the start point
            allTokensForPlayer = self.cf.TOKENS_BY_COLOR[player.color]
            
            allInYard = True
            for token in allTokensForPlayer:
                allInYard = allInYard and token.isInTheYard()
                    
            if (allInYard):
                self.print(player.color + ": There are no moves available, all tokens are in the yard.")
                self.currentHasMoved = True
                return False
            else:
                self.print(player.color + ": Has some tokens out")
        
        else:
            self.print("Dice " + str(self.dice))
            return False


    def Click_Pion(self, pos):
        if (self.currentHasMoved == True):
            self.print("[Click_Pion] The selected pawn cannot be moved.")
            return 0

        player = self.cf.PList[self.cf.CurrentPos]
        token = self.cf.ITEMS_Pos[pos]

        if (token.isInTheYard() and self.dice == 6):
            token.moveToFirstPosition()
            self.sound.PlayStart()
            self.print("[Click_Pion] " + player.color + ": The pawn came out of the house.")
            self.currentHasMoved = True
            return 0
        else:
            self.print("[Click_Pion] " + player.color + ": try", self.dice)
            self.MoveToNext(pos)

        self.print("")

    def MoveToNext(self, pos):
        x = self.cf.ITEMS_Pos[pos].coord[0]
        y = self.cf.ITEMS_Pos[pos].coord[1]

        currentIndexInMap = -1
        for i in range(0, len(self.cf.MAP)):
            if (self.cf.MAP[i][0] == x and self.cf.MAP[i][1] == y):
                currentIndexInMap = i

        if (currentIndexInMap == -1):
            self.print("The selected pawn cannot be moved (didn't find it in the map).")
            return 0
        
        if (currentIndexInMap + self.dice >= len(self.cf.MAP)):
            self.print("The token has exceeded the map, goes back around for a loop!")
            nextIndexInMap = currentIndexInMap + self.dice - len(self.cf.MAP)
        else:
            nextIndexInMap = currentIndexInMap + self.dice

        player = self.cf.PList[self.cf.CurrentPos]

        print("Moving token from " + str(self.cf.ITEMS_Pos[pos].coord) + " to " + str(self.cf.MAP[nextIndexInMap]))
        self.cf.ITEMS_Pos[pos].coord[0] = self.cf.MAP[nextIndexInMap][0]
        self.cf.ITEMS_Pos[pos].coord[1] = self.cf.MAP[nextIndexInMap][1]
        self.sound.PlayMove()
        self.currentHasMoved = True

    def Unlock_Move(self):
        if (self.currentHasMoved == False):
            self.print("Next PLAYER.")
            self.currentHasMoved = True
            

    