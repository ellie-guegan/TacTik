#!/usr/bin/python3

# imports
import pygame
import time
from tkinter import *

from functions import *
import config as cf


tGreen = 0
tRed = 0
tBlue = 0
tYellow = 0

gWindow = Tk()

def startGame():
    global gWindow, tGreen, tRed, tBlue, tYellow
    print ("Start Game")

    pionsColor = [tGreen, tRed, tBlue, tYellow]

    gWindow.destroy()

    window_width = 700
    window_height = 700

    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    done = False


    bg = pygame.image.load("resources/img-ludo/bg_game.jpg")
    gameDisplay = pygame.display.set_mode((window_width, window_height))
    gameDisplay.blit(bg, (0, 0))

    ludo = Ludo(cf, screen, gameDisplay, bg, pionsColor)

    #fpsClock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            ludo.Key_Event()

        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            ludo.Unlock_Move()

        ludo.Pions()

        ludo.Click_Event(event)
        
        ludo.CurrentPlayer()
        ludo.CurrentZar()

        pygame.display.flip()

        gameDisplay.blit(bg, (0, 0))
        #fpsClock.tick(30)

# Select Texture and Start Game
gWindow.geometry("300x170")
gWindow.resizable(False, False)

gWindow.title("LUDO: Alege textura dorita.")

pInfo = Label(gWindow, text = "Alege textura dorita pentru fiecare jucator:")
pInfo.place(x = 5, y = 10)



p0Name = Label(gWindow, text = "GREEN:")
p0Name.place(x = 5, y = 40)

def sel0():
    global tGreen
    print( "GREEN select: " + str(var0.get()) )
    tGreen = int(var0.get())
   
var0 = IntVar()
G0 = Radiobutton(gWindow, text = "G0", variable = var0, value = 0, command = sel0)
G0.place(x = 75, y = 40)

G1 = Radiobutton(gWindow, text = "G1", variable = var0, value = 1, command = sel0)
G1.place(x = 125, y = 40)

G2 = Radiobutton(gWindow, text = "G2", variable = var0, value = 2, command = sel0)
G2.place(x = 175, y = 40)

G3 = Radiobutton(gWindow, text = "G3", variable = var0, value = 3, command = sel0)
G3.place(x = 225, y = 40)



p1Name = Label(gWindow, text = "RED:")
p1Name.place(x = 5, y = 60)

def sel1():
    global tRed
    print( "RED select: " + str(var1.get()) )
    tRed = int(var1.get())
   
var1 = IntVar()
R0 = Radiobutton(gWindow, text = "R0", variable = var1, value = 0, command = sel1)
R0.place(x = 75, y = 60)

R1 = Radiobutton(gWindow, text = "R1", variable = var1, value = 1, command = sel1)
R1.place(x = 125, y = 60)

R2 = Radiobutton(gWindow, text = "R2", variable = var1, value = 2, command = sel1)
R2.place(x = 175, y = 60)

R3 = Radiobutton(gWindow, text = "R3", variable = var1, value = 3, command = sel1)
R3.place(x = 225, y = 60)



p2Name = Label(gWindow, text = "BLUE:")
p2Name.place(x = 5, y = 80)

def sel2():
    global tBlue
    print( "BLUE select: " + str(var2.get()) )
    tBlue = int(var2.get())
   
var2 = IntVar()
B0 = Radiobutton(gWindow, text = "B0", variable = var2, value = 0, command = sel2)
B0.place(x = 75, y = 80)

B1 = Radiobutton(gWindow, text = "B1", variable = var2, value = 1, command = sel2)
B1.place(x = 125, y = 80)

B2 = Radiobutton(gWindow, text = "B2", variable = var2, value = 2, command = sel2)
B2.place(x = 175, y = 80)

B3 = Radiobutton(gWindow, text = "B3", variable = var2, value = 3, command = sel2)
B3.place(x = 225, y = 80)



p3Name = Label(gWindow, text = "YELLOW:")
p3Name.place(x = 5, y = 100)

def sel3():
    global tYellow
    print( "YELLOW select: " + str(var3.get()) )
    tYellow = int(var3.get())
   
var3 = IntVar()
Y0 = Radiobutton(gWindow, text = "Y0", variable = var3, value = 0, command = sel3)
Y0.place(x = 75, y = 100)

Y1 = Radiobutton(gWindow, text = "Y1", variable = var3, value = 1, command = sel3)
Y1.place(x = 125, y = 100)

Y2 = Radiobutton(gWindow, text = "Y2", variable = var3, value = 2, command = sel3)
Y2.place(x = 175, y = 100)

Y3 = Radiobutton(gWindow, text = "Y3", variable = var3, value = 3, command = sel3)
Y3.place(x = 225, y = 100)



bSave = Button(gWindow, text = "Start Joc", command = startGame)
bSave.place(x = 100, y = 130)

gWindow.mainloop()
