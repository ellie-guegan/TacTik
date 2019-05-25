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

# Tactik Functions
class TacTik:
    def __init__(self, screen, gameDisplay, bg):
        
        self.screen = screen
        self.gameDisplay = gameDisplay
        self.bg = bg
        self.sound = a.Audio()
        
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
        
        # Initial game status
        self.dice = 0
        self.diceImgCounter = 0
        self.setMessage("Start the game.")
        self.incrementPlayer()

    # ------------------------------------------------------------------------------------
    # Display of images
    # ------------------------------------------------------------------------------------

    def refreshDisplay(self):
        self.gameDisplay.blit(self.bg, (0, 0))
        self.displayTokens()
        self.renderMessage()
        self.displayCurrentDice()
        pygame.display.flip()

    def displayTokens(self):
        for tokens in config.TOKENS_BY_COLOR.values():
            for token in tokens:
                self.screen.blit(token.tokenImage, (token.coord[0], token.coord[1]))
                
    def displayCurrentDice(self):
        self.screen.blit(self._getDiceImage(), (325, 325))

    def _getDiceImage(self):
        if (self.dice == 0):
            self.diceImgCounter += 1
            return self.imgdiceEffect[self.diceImgCounter // 5 % 4]
            #return random.choice(self.imgdiceEffect)
        else:
            return self.imgdice[self.dice]

    # ------------------------------------------------------------------------------------
    # Print-outs
    # ------------------------------------------------------------------------------------
    
    def print(self, text = "", text2 = ""):
        return print("[TacTik] " + self.getCurrentTeamColorPrefix() + str(text)+ " " +str(text2))

    def getCurrentTeamColorPrefix(self):
        return "[" + self.getCurrentPlayer().color + "] "

    def setMessage(self, text = ""):
        if (text != "" and config.CurrentPos != -1):
            text = self.getCurrentTeamColorPrefix() + text
        self.message = text

    def renderMessage(self):
        renderedText = self.font.render(self.message, True, (0, 60, 0))
        self.screen.blit(renderedText, (config.CENTER_Pos[0], config.CENTER_Pos[1] - 40))
        
    # ------------------------------------------------------------------------------------
    # Player
    # ------------------------------------------------------------------------------------
    def _waitSomeTime(self, nbSecs):
        current_time = pygame.time.get_ticks()
        exit_time = current_time + nbSecs * 1000
        keepWaiting = True

        while keepWaiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitGame()
            current_time = pygame.time.get_ticks()
            if current_time >= exit_time:
                keepWaiting = False
    
            #clock.tick(5)        
    
    def incrementPlayer(self):
        self.refreshDisplay()
        self._waitSomeTime(1)
        config.CurrentPos += 1
        if (config.CurrentPos >= len(config.Players)):
            config.CurrentPos = 0

        self.waitForDiceRoll()
        
    def getCurrentPlayer(self):
        if (config.CurrentPos == -1):
            raise ValueError("Do not try and get a current player when none was set yet.")
        
        return config.Players[config.CurrentPos]
    
    # ------------------------------------------------------------------------------------
    # Dice
    # ------------------------------------------------------------------------------------
    def rollDice(self):
        self.sound.PlayDice()
        self.dice = random.randint(1, 6)
        self.print("Random dice roll yielded: " + str(self.dice))
        self.gameStatus = GameStatus.WAITING_FOR_TOKEN_SELECTION

    def waitForDiceRoll(self):
        self.setMessage("It's your turn.")
        self.dice = 0
        self.gameStatus = GameStatus.WAITING_FOR_DICE_ROLL

    def playDiceRoll(self):
        self.rollDice()
        self.print ("You rolled the dice, with result: ", self.dice)
        
        # check whether the current player has any valid moves
        if (self.hasValidMoves()):
            # if so, then wait for them to select their token
            self.gameStatus == GameStatus.WAITING_FOR_TOKEN_SELECTION
        else:
            # if not, move on to the next player
            self.setMessage("You have no valid moves.")
            self.incrementPlayer()

    # ------------------------------------------------------------------------------------
    # Event handling
    # ------------------------------------------------------------------------------------
    def Click_Event(self, event):
        # TODO: replace with weird python switch type thingy...
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.print("     ------------ a CLICK was made --------------------------")
            x, y = pygame.mouse.get_pos()
            # Waiting on the DICE
            if (self.gameStatus == GameStatus.WAITING_FOR_DICE_ROLL):
                # Check the dice
                if (x >= 295 and x < 405 and y >= 295 and y < 405):
                    self.playDiceRoll()
                else:
                    self.print("[Click_Event] You didn't click on the dice")
                    self.setMessage("Please click on the dice.")
            # Waiting on a TOKEN
            elif (self.gameStatus == GameStatus.WAITING_FOR_TOKEN_SELECTION):
                foundATeamToken = False
                for token in config.TOKENS_BY_COLOR[self.getCurrentPlayer().color]:
                    pX = token.coord[0]
                    pY = token.coord[1]
                    if (x >= pX and x < pX + 35 and y >= pY and y < pY + 35):
                        # TODO: be more precise with coordinates
                        self.print ("[Click_Event] Found a token you clicked on! " + str(token.coord))
                        foundATeamToken = True
                        self.moveSelectedToken(token)
                        break

                if (not foundATeamToken):
                    self.setMessage("Please click on one of your team's tokens.")
                    self.print("[Click_Event] Please click on one of your team's tokens.")
            else:
                raise ValueError("Unknown game status: " + self.gameStatus)
        else:
            # TODO: Should probably just ignore these
            raise ValueError("Unhandled event of type: " + str(event.type))
    
    def Key_Event(self, event):
        self.print("     ------------ a KEY was pressed --------------------------")
        if (event.key == pygame.K_SPACE):
            self.print("The space key was pressed.")
            if (self.gameStatus == GameStatus.WAITING_FOR_TOKEN_SELECTION):
                self.setMessage("Please click on a token to play your turn.")
                self.print ("[Key_Event] You pressed a key but we're waiting on a token.")
            elif (self.gameStatus == GameStatus.WAITING_FOR_DICE_ROLL):
                self.playDiceRoll()
            else:
                raise ValueError("Unknown game status: " + self.gameStatus)
        else:
            self.print("A key that is not the space key was pressed... ignore!")

    # ------------------------------------------------------------------------------------
    # Token movement
    # ------------------------------------------------------------------------------------
    def hasValidMoves(self):
        player = self.getCurrentPlayer()

        if (self.dice < 5):
            # checking whether all tokens are at the start point
            if (player.allTokensInTheYard()):
                self.print(player.color + ": There are no moves available, all tokens are in the yard.")
                return False
            else:
                self.print(player.color + ": Has some tokens out")
                # TODO: should check whether they can legally move. right now they always can, but later...
                return True
        else:
            # TODO: same as above. Having tokens out will not always guarantee a legal move
            return True

    def moveSelectedToken(self, token):
        # TODO:should only be allowed to get here by clicking on an allowed token...
        if (token.isInTheYard()):
            if (self.dice == 6 or self.dice == 5):
                token.moveToFirstPosition()
                self.sound.PlayStart()
                self.setMessage("You got out of the yard!")
                self.print("[MoveSelectedToken] The pawn came out of the house.")
                self.incrementPlayer()
            else:
                self.print("[MoveSelectedToken] The chosen token is in the yard and needs a 6 to get out. Please pick another.")
                self.setMessage("The chosen token is in the yard and needs a 6 to get out. Please pick another.")
        else:
            self.print("[MoveSelectedToken] trying to move by ", self.dice)
            hasMoved = self.moveToNext(token)
            if (hasMoved):
                # the token had a valid move and was moved - go to next player
                self.setMessage("Onward you go!")
                self.print("[MoveSelectedToken] Good choice of token, then.")
                self.incrementPlayer()
            else:
                # the token didn't have a valid move, but we know the player has some valid moves
                # so tell them to pick a valid token
                # TODO: highlight valid tokens?
                # right now it'll always have valid moves...
                self.print("[MoveSelectedToken] The chosen token cannot played. Please pick another.")
                self.setMessage("The chosen token cannot be played. Please pick another.")

    def moveToNext(self, token):
        x = token.coord[0]
        y = token.coord[1]

        currentIndexInMap = -1
        for i in range(0, len(config.MAP)):
            if (config.MAP[i][0] == x and config.MAP[i][1] == y):
                currentIndexInMap = i

        if (currentIndexInMap == -1):
            self.print("[moveToNext] The selected token " + str(token.coord) + " cannot be moved (didn't find on in the map).")
            raise ValueError("Couldn't find token " + str(token.coord) + " of color " + token.player.color + " on the map.")
        
        nextIndexInMap = (currentIndexInMap + self.dice) % len(config.MAP)
        
        self.print("[moveToNext] Moving token from " + str(token.coord) + " to " + str(config.MAP[nextIndexInMap]))
        token.moveTo(config.MAP[nextIndexInMap])
        self.sound.PlayMove()
        return True
            

    