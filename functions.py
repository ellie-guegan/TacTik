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

        self.move = True
        self.zar = 0
        
        self.imgZarEffect = [
            pygame.image.load("resources/img-ludo/dice_0_1.png"),
            pygame.image.load("resources/img-ludo/dice_0_2.png"),
            pygame.image.load("resources/img-ludo/dice_0_3.png"),
            pygame.image.load("resources/img-ludo/dice_0_4.png"),
        ]
        
        self.imgZar = [
            self.imgZarEffect[0],
            pygame.image.load("resources/img-ludo/dice_1.png"),
            pygame.image.load("resources/img-ludo/dice_2.png"),
            pygame.image.load("resources/img-ludo/dice_3.png"),
            pygame.image.load("resources/img-ludo/dice_4.png"),
            pygame.image.load("resources/img-ludo/dice_5.png"),
            pygame.image.load("resources/img-ludo/dice_6.png"),
        ]
        
        self.font = pygame.font.SysFont("comicsansms", 20)
        
        self.bkItemPos = self.cf.ITEMS_Pos

        self.print("test 245")


    def print(self, text = "", text2 = ""):
        return print("[Ludo]: " +str(text)+ " " +str(text2))

    def CurrentPlayer(self):
        if (self.cf.CurrentPos == -1):
            text = self.font.render("Start the game.", True, (0, 60, 0))
        else:
            player = self.cf.PList[self.cf.CurrentPos]
            text = self.font.render("It's his turn: " + str(player), True, (0, 60, 0))

        self.screen.blit(text, (78, 640))

        info = self.font.render("I have no moves.", True, (255, 0, 0))
        self.screen.blit(info, (78, 680))

    def CurrentZar(self):
        self.screen.blit(self.imgZar[self.zar], (325, 325))

    
    # Click function
    def Click_Event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # Click Pion
            found = -1
            player = self.cf.PList[self.cf.CurrentPos]
            for i in range(0, len(self.cf.ITEMS_Pos)):
                pColor = self.cf.ITEMS_Pos[i][0]
                pX = self.cf.ITEMS_Pos[i][1]
                pY = self.cf.ITEMS_Pos[i][2]
                if (player == pColor and x >= pX and x < pX + 35 and y >= pY and y < pY + 35):
                    found = i
                    break
            if (found > -1):
                self.print ("You pushed a pawn: " + self.cf.ITEMS_Pos[i][0])
                self.Click_Pion(found)

            # Check the dice
            if (x >= 295 and x < 405 and y >= 295 and y < 405):
                self.Play()

                self.print (" [Click] You dared with the dice: ", self.zar)

                self.PlayerMove()

            # Click No Move
            if (x >= 78 and x < 200 and y >= 680 and y < 700):
                self.Unlock_Move()

         
    def Key_Event(self):
        
        self.Play()
        
        self.print (" [Space] You dared with the dice: ", self.zar)
        
        self.PlayerMove()

        #time.sleep(0.5)

    def Pions(self):
        for i in range(0, len(self.cf.ITEMS_Pos)):
            self.screen.blit(self.cf.getPlayerToken(self.cf.ITEMS_Pos[i][0]), (self.cf.ITEMS_Pos[i][1], self.cf.ITEMS_Pos[i][2]))
    
    def Number(self):
        return random.randint(1, 6)
    
    def Play(self):
        if (self.move == True):   
            self.cf.CurrentPos += 1   
            if (self.cf.CurrentPos >= self.cf.MaxPos):
                self.cf.CurrentPos = 0

            self.print("It's his turn: " + str(self.cf.PList[self.cf.CurrentPos]))

            self.sound.PlayDice()
            self.zar = self.Number()


            self.move = False
        else:
            self.print("Waiting for: " + str(self.cf.PList[self.cf.CurrentPos]))

    def PlayerMove(self):
        player = self.cf.PList[self.cf.CurrentPos]

        if (self.zar < 6):
            
            if ( player == "GREEN"):
                if (
                    self.cf.ITEMS_Pos[0][1] == self.cf.GREEN_Start_Storage[0][0] and self.cf.ITEMS_Pos[0][2] == self.cf.GREEN_Start_Storage[0][1] and
                    self.cf.ITEMS_Pos[1][1] == self.cf.GREEN_Start_Storage[1][0] and self.cf.ITEMS_Pos[1][2] == self.cf.GREEN_Start_Storage[1][1] and
                    self.cf.ITEMS_Pos[2][1] == self.cf.GREEN_Start_Storage[2][0] and self.cf.ITEMS_Pos[2][2] == self.cf.GREEN_Start_Storage[2][1] and
                    self.cf.ITEMS_Pos[3][1] == self.cf.GREEN_Start_Storage[3][0] and self.cf.ITEMS_Pos[3][2] == self.cf.GREEN_Start_Storage[3][1]
                ):
                    self.print("GREEN: There are no moves available.")
                    self.move = True
                    return False
                else:
                    self.print("GREEN: Something")
            elif ( player == "RED" ):
                if (
                    self.cf.ITEMS_Pos[4][1] == self.cf.RED_Start_Storage[0][0] and self.cf.ITEMS_Pos[4][2] == self.cf.RED_Start_Storage[0][1] and
                    self.cf.ITEMS_Pos[5][1] == self.cf.RED_Start_Storage[1][0] and self.cf.ITEMS_Pos[5][2] == self.cf.RED_Start_Storage[1][1] and
                    self.cf.ITEMS_Pos[6][1] == self.cf.RED_Start_Storage[2][0] and self.cf.ITEMS_Pos[6][2] == self.cf.RED_Start_Storage[2][1] and
                    self.cf.ITEMS_Pos[7][1] == self.cf.RED_Start_Storage[3][0] and self.cf.ITEMS_Pos[7][2] == self.cf.RED_Start_Storage[3][1]
                ):
                    self.print("RED: There are no moves available.")
                    self.move = True
                    return False
                else:
                    self.print("RED: Something")
            elif ( player == "BLUE" ):
                if (
                    self.cf.ITEMS_Pos[8][1] == self.cf.BLUE_Start_Storage[0][0] and self.cf.ITEMS_Pos[8][2] == self.cf.BLUE_Start_Storage[0][1] and
                    self.cf.ITEMS_Pos[9][1] == self.cf.BLUE_Start_Storage[1][0] and self.cf.ITEMS_Pos[9][2] == self.cf.BLUE_Start_Storage[1][1] and
                    self.cf.ITEMS_Pos[10][1] == self.cf.BLUE_Start_Storage[2][0] and self.cf.ITEMS_Pos[10][2] == self.cf.BLUE_Start_Storage[2][1] and
                    self.cf.ITEMS_Pos[11][1] == self.cf.BLUE_Start_Storage[3][0] and self.cf.ITEMS_Pos[11][2] == self.cf.BLUE_Start_Storage[3][1]
                ):
                    self.print("BLUE: There are no moves available.")
                    self.move = True
                    return False
                else:
                    self.print("BLUE: Something")
            elif ( player == "YELLOW" ):
                if (
                    self.cf.ITEMS_Pos[12][1] == self.cf.YELLOW_Start_Storage[0][0] and self.cf.ITEMS_Pos[12][2] == self.cf.YELLOW_Start_Storage[0][1] and
                    self.cf.ITEMS_Pos[13][1] == self.cf.YELLOW_Start_Storage[1][0] and self.cf.ITEMS_Pos[13][2] == self.cf.YELLOW_Start_Storage[1][1] and
                    self.cf.ITEMS_Pos[14][1] == self.cf.YELLOW_Start_Storage[2][0] and self.cf.ITEMS_Pos[14][2] == self.cf.YELLOW_Start_Storage[2][1] and
                    self.cf.ITEMS_Pos[15][1] == self.cf.YELLOW_Start_Storage[3][0] and self.cf.ITEMS_Pos[15][2] == self.cf.YELLOW_Start_Storage[3][1]
                ):
                    self.print("YELLOW: There are no moves available.")
                    self.move = True
                    return False
                else:
                    self.print("YELLOW: Something")
            else:
                self.print("Unknown Player: {" +str(player)+ "}.")
        else:
            self.print("Dice " + str(self.zar))
            #self.move = True
            return False


    def Click_Pion(self, pos):
        if (self.move == True):
            self.print("The selected pawn cannot be moved.")
            return 0

        player = self.cf.PList[self.cf.CurrentPos]

        if ( player == "GREEN"):
            if (pos >=0 and pos <= 3):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.GREEN_Start_Storage[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.GREEN_Start_Storage[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.GREEN_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.GREEN_Start[1]
                        self.sound.PlayStart()
                        self.print("GREEN: The pawn came out of the house.")
                        self.move = True
                        return 0

                self.print("GREEN: try", self.zar)
                self.MoveToNext(pos)

        elif ( player == "RED" ):
            if (pos >= 4 and pos <= 7):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.RED_Start_Storage[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.RED_Start_Storage[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.RED_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.RED_Start[1]
                        self.sound.PlayStart()
                        self.print("RED: The pawn came out of the house.")
                        self.move = True
                        return 0

                self.print("RED: try", self.zar)
                self.MoveToNext(pos)

        elif ( player == "BLUE" ):
            if (pos >= 8 and pos <= 11):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.BLUE_Start_Storage[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.BLUE_Start_Storage[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.BLUE_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.BLUE_Start[1]
                        self.sound.PlayStart()
                        self.print("BLUE: The pawn came out of the house.")
                        self.move = True
                        return 0
                    
                self.print("BLUE: try", self.zar)
                self.MoveToNext(pos)

        elif ( player == "YELLOW" ):
            if (pos >= 12 and pos <= 15):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.YELLOW_Start_Storage[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.YELLOW_Start_Storage[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.YELLOW_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.YELLOW_Start[1]
                        self.sound.PlayStart()
                        self.print("YELLOW: The pawn came out of the house.")
                        self.move = True
                        return 0

                self.print("YELLOW: try", self.zar)
                self.MoveToNext(pos)

        else:
            self.print("Unknown Player: {" +str(player)+ "}.")
        self.print("")

    def MoveToNext(self, pos):
        x = self.cf.ITEMS_Pos[pos][1]
        y = self.cf.ITEMS_Pos[pos][2]

        currentIndexInMap = -1
        for i in range(0, len(self.cf.MAP)):
            if (self.cf.MAP[i][0] == x and self.cf.MAP[i][1] == y):
                currentIndexInMap = i

        if (currentIndexInMap == -1):
            self.print("The selected pawn can not be moved (didn't find it in the map).")
            return 0
        
        if (currentIndexInMap + self.zar >= len(self.cf.MAP)):
            self.print("The token has exceeded the map, goes back around for a loop!")
            nextIndexInMap = currentIndexInMap + self.zar - len(self.cf.MAP)
        else:
            nextIndexInMap = currentIndexInMap + self.zar

        player = self.cf.PList[self.cf.CurrentPos]

        print("Moving token from " + str(self.cf.ITEMS_Pos[pos]) + " to " + str(self.cf.MAP[nextIndexInMap]))
        self.cf.ITEMS_Pos[pos][1] = self.cf.MAP[nextIndexInMap][0]
        self.cf.ITEMS_Pos[pos][2] = self.cf.MAP[nextIndexInMap][1]
        self.sound.PlayMove()
        self.move = True

    def Unlock_Move(self):
        if (self.move == False):
            self.print("Next PLAYER.")
            self.move = True