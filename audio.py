#!/usr/bin/python3

# Imports
import pygame

# Audio Class
class Audio:
    def __init__(self):
        "ToDo"

    def PlayMove(self):
        pygame.mixer.music.load('resources/audio/move.mp3')
        pygame.mixer.music.play(0)

    def PlayStart(self):
        pygame.mixer.music.load('resources/audio/start.mp3')
        pygame.mixer.music.play(0)

    def PlayDice(self):
        pygame.mixer.music.load('resources/audio/dice.mp3')
        pygame.mixer.music.play(0)

    def PlayWin(self):
        pygame.mixer.music.load('resources/audio/win.mp3')
        pygame.mixer.music.play(0)
    
