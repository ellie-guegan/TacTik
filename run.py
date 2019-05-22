#!/usr/bin/python3

# imports
import pygame
import time
from tkinter import *

from functions import *
import config as cf

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


    bg = pygame.image.load("resources/background/TacTikBoard.png")
    gameDisplay = pygame.display.set_mode((window_width, window_height))
    gameDisplay.blit(bg, (0, 0))

    ludo = Ludo(cf, screen, gameDisplay, bg)

    #fpsClock = pygame.time.Clock()

    while not done:
        ludo.displayTokens()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                ludo.Key_Event()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ludo.Click_Event(event)
        
        ludo.PrintCurrentPlayer()
        ludo.DisplayCurrentDice()

        pygame.display.flip()

        gameDisplay.blit(bg, (0, 0))
        #fpsClock.tick(30)

startGame()
