#!/usr/bin/python3

# imports
import time
import pygame
import random

import audio as a

from tkinter import messagebox

# Ludo Functions
class Ludo:
    def __init__(self, config, screen, gameDisplay, bg, pionsColor):
        
        self.cf = config
        
        self.screen = screen
        
        self.gameDisplay = gameDisplay
        
        self.bg = bg
        
        self.pionsColor = pionsColor

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
            text = self.font.render("Incepeti jocul.", True, (0, 60, 0))
        else:
            player = self.cf.PList[self.cf.CurrentPos]
            text = self.font.render("Este randul lui: " + str(player), True, (0, 60, 0))

        self.screen.blit(text, (78, 640))

        info = self.font.render("Nu am mutari.", True, (255, 0, 0))
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
                self.print ("Ai apasat pe un pion: " + self.cf.ITEMS_Pos[i][0])
                self.Click_Pion(found)

            # Verifica pizitia zarului
            if (x >= 295 and x < 405 and y >= 295 and y < 405):
                self.Play()

                self.print (" [Click] Ai dat cu zarul: ", self.zar)

                self.PlayerMove()

            # Click No Move
            if (x >= 78 and x < 200 and y >= 680 and y < 700):
                self.Unlock_Move()

         
    def Key_Event(self):
        
        self.Play()
        
        self.print (" [Space] Ai dat cu zarul: ", self.zar)
        
        self.PlayerMove()

        #time.sleep(0.5)
        

    def player(self, color):
        if (color == "GREEN"):
            return pygame.image.load("resources/img-ludo/pion_green" +str(self.pionsColor[0])+ ".png")
        elif (color == "RED"):
            return pygame.image.load("resources/img-ludo/pion_red" +str(self.pionsColor[1])+ ".png")
        elif (color == "BLUE"):
            return pygame.image.load("resources/img-ludo/pion_blue" +str(self.pionsColor[2])+ ".png")
        else:
            return pygame.image.load("resources/img-ludo/pion_yellow" +str(self.pionsColor[3])+ ".png")

    def Pions(self):
        for i in range(0, len(self.cf.ITEMS_Pos)):
            self.screen.blit(self.player(self.cf.ITEMS_Pos[i][0]), (self.cf.ITEMS_Pos[i][1], self.cf.ITEMS_Pos[i][2]))
    
    def Number(self):
        return random.randint(1, 6)
    
    def Play(self):
        if (self.move == True):   
            self.cf.CurrentPos += 1   
            if (self.cf.CurrentPos >= self.cf.MaxPos):
                self.cf.CurrentPos = 0

            self.print("Este randul lui: " + str(self.cf.PList[self.cf.CurrentPos]))

            self.sound.PlayDice()
            self.zar = self.Number()


            self.move = False
        else:
            self.print("Asteptam dupa: " + str(self.cf.PList[self.cf.CurrentPos]))

    def PlayerMove(self):
        player = self.cf.PList[self.cf.CurrentPos]

        if (self.zar < 6):
            
            if ( player == "GREEN"):
                if (
                    self.cf.ITEMS_Pos[0][1] == self.cf.GREEN_Pos[0][0] and self.cf.ITEMS_Pos[0][2] == self.cf.GREEN_Pos[0][1] and
                    self.cf.ITEMS_Pos[1][1] == self.cf.GREEN_Pos[1][0] and self.cf.ITEMS_Pos[1][2] == self.cf.GREEN_Pos[1][1] and
                    self.cf.ITEMS_Pos[2][1] == self.cf.GREEN_Pos[2][0] and self.cf.ITEMS_Pos[2][2] == self.cf.GREEN_Pos[2][1] and
                    self.cf.ITEMS_Pos[3][1] == self.cf.GREEN_Pos[3][0] and self.cf.ITEMS_Pos[3][2] == self.cf.GREEN_Pos[3][1]
                ):
                    self.print("GREEN: Nu sunt mutari disponibile.")
                    self.move = True
                    return False
                else:
                    self.print("GREEN: Something")
            elif ( player == "RED" ):
                if (
                    self.cf.ITEMS_Pos[4][1] == self.cf.RED_Pos[0][0] and self.cf.ITEMS_Pos[4][2] == self.cf.RED_Pos[0][1] and
                    self.cf.ITEMS_Pos[5][1] == self.cf.RED_Pos[1][0] and self.cf.ITEMS_Pos[5][2] == self.cf.RED_Pos[1][1] and
                    self.cf.ITEMS_Pos[6][1] == self.cf.RED_Pos[2][0] and self.cf.ITEMS_Pos[6][2] == self.cf.RED_Pos[2][1] and
                    self.cf.ITEMS_Pos[7][1] == self.cf.RED_Pos[3][0] and self.cf.ITEMS_Pos[7][2] == self.cf.RED_Pos[3][1]
                ):
                    self.print("RED: Nu sunt mutari disponibile.")
                    self.move = True
                    return False
                else:
                    self.print("RED: Something")
            elif ( player == "BLUE" ):
                if (
                    self.cf.ITEMS_Pos[8][1] == self.cf.BLUE_Pos[0][0] and self.cf.ITEMS_Pos[8][2] == self.cf.BLUE_Pos[0][1] and
                    self.cf.ITEMS_Pos[9][1] == self.cf.BLUE_Pos[1][0] and self.cf.ITEMS_Pos[9][2] == self.cf.BLUE_Pos[1][1] and
                    self.cf.ITEMS_Pos[10][1] == self.cf.BLUE_Pos[2][0] and self.cf.ITEMS_Pos[10][2] == self.cf.BLUE_Pos[2][1] and
                    self.cf.ITEMS_Pos[11][1] == self.cf.BLUE_Pos[3][0] and self.cf.ITEMS_Pos[11][2] == self.cf.BLUE_Pos[3][1]
                ):
                    self.print("BLUE: Nu sunt mutari disponibile.")
                    self.move = True
                    return False
                else:
                    self.print("BLUE: Something")
            elif ( player == "YELLOW" ):
                if (
                    self.cf.ITEMS_Pos[12][1] == self.cf.YELLOW_Pos[0][0] and self.cf.ITEMS_Pos[12][2] == self.cf.YELLOW_Pos[0][1] and
                    self.cf.ITEMS_Pos[13][1] == self.cf.YELLOW_Pos[1][0] and self.cf.ITEMS_Pos[13][2] == self.cf.YELLOW_Pos[1][1] and
                    self.cf.ITEMS_Pos[14][1] == self.cf.YELLOW_Pos[2][0] and self.cf.ITEMS_Pos[14][2] == self.cf.YELLOW_Pos[2][1] and
                    self.cf.ITEMS_Pos[15][1] == self.cf.YELLOW_Pos[3][0] and self.cf.ITEMS_Pos[15][2] == self.cf.YELLOW_Pos[3][1]
                ):
                    self.print("YELLOW: Nu sunt mutari disponibile.")
                    self.move = True
                    return False
                else:
                    self.print("YELLOW: Something")
            else:
                self.print("Unknown Player: {" +str(player)+ "}.")
        else:
            self.print("Zarul " + str(self.zar))
            #self.move = True
            return False


    def Click_Pion(self, pos):
        if (self.move == True):
            self.print("Pionul selectat nu poate fi mutat.")
            return 0

        player = self.cf.PList[self.cf.CurrentPos]

        if ( player == "GREEN"):
            if (pos >=0 and pos <= 3):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.GREEN_Pos[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.GREEN_Pos[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.GREEN_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.GREEN_Start[1]
                        self.sound.PlayStart()
                        self.print("GREEN: Pionul a iesit din casa.")
                        self.move = True
                        return 0

                for i in range(0, len(self.cf.GREEN_Win)):
                    if (self.cf.ITEMS_Pos[pos][1] ==  self.cf.GREEN_Win[i][0] and  self.cf.ITEMS_Pos[pos][2] == self.cf.GREEN_Win[i][1]):
                        self.print("GREEN: Ai ajuns intr-o zona finala.")

                        print ("Zar curent: " + str(self.zar) + " Pos: " + str(i))

                        #GREEN_Play
                        # GREEN_End
                        
                        self.MoveFinalEnd(i, pos, "GREEN",  self.cf.GREEN_End, self.cf.GREEN_Play, self.cf.GREEN_Win)

                        #self.move = True
                        return 0

                self.print("GREEN: try", self.zar)
                self.MoveToNext(pos)

        elif ( player == "RED" ):
            if (pos >= 4 and pos <= 7):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.RED_Pos[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.RED_Pos[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.RED_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.RED_Start[1]
                        self.sound.PlayStart()
                        self.print("RED: Pionul a iesit din casa.")
                        self.move = True
                        return 0

                for i in range(0, len(self.cf.RED_Win)):
                    if (self.cf.ITEMS_Pos[pos][1] ==  self.cf.RED_Win[i][0] and  self.cf.ITEMS_Pos[pos][2] == self.cf.RED_Win[i][1]):
                        self.print("RED: Ai ajuns intr-o zona finala.")

                        print ("Zar curent: " + str(self.zar) + " Pos: " + str(i))

                        self.MoveFinalEnd(i, pos, "RED",  self.cf.RED_End, self.cf.RED_Play, self.cf.RED_Win)

                        #self.move = True
                        return 0

                self.print("RED: try", self.zar)
                self.MoveToNext(pos)

        elif ( player == "BLUE" ):
            if (pos >= 8 and pos <= 11):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.BLUE_Pos[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.BLUE_Pos[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.BLUE_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.BLUE_Start[1]
                        self.sound.PlayStart()
                        self.print("BLUE: Pionul a iesit din casa.")
                        self.move = True
                        return 0

                for i in range(0, len(self.cf.BLUE_Win)):
                    if (self.cf.ITEMS_Pos[pos][1] ==  self.cf.BLUE_Win[i][0] and  self.cf.ITEMS_Pos[pos][2] == self.cf.BLUE_Win[i][1]):
                        self.print("BLUE: Ai ajuns intr-o zona finala.")

                        print ("Zar curent: " + str(self.zar) + " Pos: " + str(i))

                        self.MoveFinalEnd(i, pos, "BLUE",  self.cf.BLUE_End, self.cf.BLUE_Play, self.cf.BLUE_Win)

                        #self.move = True
                        return 0
                    
                self.print("BLUE: try", self.zar)
                self.MoveToNext(pos)

        elif ( player == "YELLOW" ):
            if (pos >= 12 and pos <= 15):
                for i in range(0, 4):
                    if (self.cf.ITEMS_Pos[pos][1] == self.cf.YELLOW_Pos[i][0] and self.cf.ITEMS_Pos[pos][2] == self.cf.YELLOW_Pos[i][1] and self.zar == 6):
                        self.cf.ITEMS_Pos[pos][1] = self.cf.YELLOW_Start[0]
                        self.cf.ITEMS_Pos[pos][2] = self.cf.YELLOW_Start[1]
                        self.sound.PlayStart()
                        self.print("YELLOW: Pionul a iesit din casa.")
                        self.move = True
                        return 0

                for i in range(0, len(self.cf.YELLOW_Win)):
                    if (self.cf.ITEMS_Pos[pos][1] ==  self.cf.YELLOW_Win[i][0] and  self.cf.ITEMS_Pos[pos][2] == self.cf.YELLOW_Win[i][1]):
                        self.print("YELLOW: Ai ajuns intr-o zona finala.")

                        print ("Zar curent: " + str(self.zar) + " Pos: " + str(i))

                        self.MoveFinalEnd(i, pos, "YELLOW",  self.cf.YELLOW_End, self.cf.YELLOW_Play, self.cf.YELLOW_Win)

                        #self.move = True
                        return 0

                self.print("YELLOW: try", self.zar)
                self.MoveToNext(pos)

        else:
            self.print("Unknown Player: {" +str(player)+ "}.")
        self.print("")

    def MoveFinalEnd(self, i, pos, Color,  ColorEnd, ColorPlay, ColorWin):
        
        print ("Si eu si eu", pos, Color, ColorEnd, ColorPlay, ColorWin)
        ifZar = 0
        iCheck = 5
        while (ifZar < 5):
            ifZar = ifZar + 1
            iCheck = iCheck - 1
            if (i == iCheck and self.zar == ifZar):

                self.cf.ITEMS_Pos[pos][1] = ColorEnd[ColorPlay][0]
                self.cf.ITEMS_Pos[pos][2] = ColorEnd[ColorPlay][1]
                self.sound.PlayMove()
                self.move = True

                WinGg = False

                if (Color == "GREEN"):
                    self.cf.GREEN_Play = self.cf.GREEN_Play + 1
                    if (self.cf.GREEN_Play == 4):
                        WinGg = True

                elif (Color == "RED"):
                    self.cf.RED_Play = self.cf.RED_Play + 1
                    if (self.cf.RED_Play == 4):
                        WinGg = True

                elif (Color == "BLUE"):
                    self.cf.BLUE_Play = self.cf.BLUE_Play + 1
                    if (self.cf.BLUE_Play == 4):
                        WinGg = True

                else:
                    self.cf.YELLOW_Play = self.cf.YELLOW_Play + 1
                    if (self.cf.YELLOW_Play == 4):
                        WinGg = True
                
                if (WinGg == True):
                    self.sound.PlayWin()
                    messagebox.showinfo("Ludo", "Jucatorul " +str(Color)+ " a castigat.")

                    self.print("PLay a new game.")
                    self.cf.ITEMS_Pos = self.bkItemPos

                print (str(Color) + ": Ceva: " + str(ifZar) + " cu: " + str(iCheck))

        if (i == 0 and self.zar < 5):
            self.cf.ITEMS_Pos[pos][1] = ColorWin[self.zar][0]
            self.cf.ITEMS_Pos[pos][2] = ColorWin[self.zar][1]
            self.sound.PlayMove()
            self.move = True

            print (str(Color) + ": Move 1" )

        elif (i == 1 and self.zar < 3): 
            self.cf.ITEMS_Pos[pos][1] = ColorWin[self.zar + 1][0]
            self.cf.ITEMS_Pos[pos][2] = ColorWin[self.zar + 1][1]
            self.sound.PlayMove()
            self.move = True

            print (str(Color) + ": Move 2" )
        elif (i == 2 and self.zar < 3): 
            self.cf.ITEMS_Pos[pos][1] = ColorWin[self.zar + 2][0]
            self.cf.ITEMS_Pos[pos][2] = ColorWin[self.zar + 2][1]
            self.sound.PlayMove()
            self.move = True

            print (str(Color) + ": Move 3" )
        elif (i == 3 and self.zar < 2): 
            self.cf.ITEMS_Pos[pos][1] = ColorWin[self.zar + 3][0]
            self.cf.ITEMS_Pos[pos][2] = ColorWin[self.zar + 3][1]
            self.sound.PlayMove()
            self.move = True

            print (str(Color) + ": Move 4" )

    def MoveToNext(self, pos):
        x = self.cf.ITEMS_Pos[pos][1]
        y = self.cf.ITEMS_Pos[pos][2]

        oFound = -1
        for i in range(0, len(self.cf.MAP)):
            if (self.cf.MAP[i][0] == x and self.cf.MAP[i][1] == y):
                oFound = i

        if (oFound == -1):
            self.print("Pionul selectat nu poate fi mutat.")
            return 0
        
        if (oFound + self.zar >= len(self.cf.MAP)):
            found = oFound + self.zar - len(self.cf.MAP)
        else:
            found = oFound + self.zar
                
        if ( found > -1):
            player = self.cf.PList[self.cf.CurrentPos]
            mvx = True

            if ( player == "GREEN"):
                if (oFound + self.zar >= 51 and oFound < 51):
                    print ("GREEN: Must be moved to tot")
                    
                    found = oFound + self.zar - 51
                    print (found)

                    self.cf.ITEMS_Pos[pos][1] = self.cf.GREEN_Win[found][0]
                    self.cf.ITEMS_Pos[pos][2] = self.cf.GREEN_Win[found][1]
                    self.sound.PlayMove()
                    self.move = True

                    mvx = False
                    # GREEN_Win

            elif ( player == "RED" ):
                if (oFound + self.zar >= 11 and oFound < 11):
                    # RED_Win
                    print ("RED: Must be moved to tot")

                    found = oFound + self.zar - 12
                    print (found)

                    self.cf.ITEMS_Pos[pos][1] = self.cf.RED_Win[found][0]
                    self.cf.ITEMS_Pos[pos][2] = self.cf.RED_Win[found][1]
                    self.sound.PlayMove()
                    self.move = True

                    mvx = False


            elif ( player == "BLUE" ):
                if (oFound + self.zar >= 25 and oFound < 25):
                    # BLUE_Win
                    print ("BLUE: Must be moved to tot")

                    found = oFound + self.zar - 25
                    print (found)

                    self.cf.ITEMS_Pos[pos][1] = self.cf.BLUE_Win[found][0]
                    self.cf.ITEMS_Pos[pos][2] = self.cf.BLUE_Win[found][1]
                    self.sound.PlayMove()
                    self.move = True

                    mvx = False


            elif ( player == "YELLOW" ):
                if (oFound + self.zar >= 38 and oFound < 38):
                    # YELLOW_Win
                    print ("YELLOW: Must be moved to tot")

                    found = oFound + self.zar - 38
                    print (found)

                    self.cf.ITEMS_Pos[pos][1] = self.cf.YELLOW_Win[found][0]
                    self.cf.ITEMS_Pos[pos][2] = self.cf.YELLOW_Win[found][1]
                    self.sound.PlayMove()
                    self.move = True

                    mvx = False

            else:
                self.print("Unknown Player: {" +str(player)+ "}.")


            if (mvx == True):
                print("move here ")
                self.cf.ITEMS_Pos[pos][1] = self.cf.MAP[found][0]
                self.cf.ITEMS_Pos[pos][2] = self.cf.MAP[found][1]
                self.sound.PlayMove()
                self.move = True
            else:
                print ("Not move")

    def Unlock_Move(self):
        if (self.move == False):
            self.print("Next PLAYER.")
            self.move = True