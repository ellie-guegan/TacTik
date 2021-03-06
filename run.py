#!/usr/bin/python3

# imports
import pygame
import time
from tkinter import *

from functions import *

gWindow = Tk()

def startGame():
    global gWindow
    print ("Start Game")

    gWindow.destroy()

    window_width = 700
    window_height = 700

    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    done = False


    bg = pygame.image.load("resources/img/background/TacTikBoard.png")
    gameDisplay = pygame.display.set_mode((window_width, window_height))
    gameDisplay.blit(bg, (0, 0))

    tacTik = TacTik(screen, gameDisplay, bg)

    #fpsClock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                tacTik.Key_Event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                tacTik.Click_Event(event)
        
        tacTik.refreshDisplay()

        #fpsClock.tick(30)

startGame()
