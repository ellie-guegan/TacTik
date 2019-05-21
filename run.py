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

startGame()
