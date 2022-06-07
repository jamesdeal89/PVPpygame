"""the class for the player which inherits from the avatar class"""
from avatar import Avatar
import os
import pygame

class Player(Avatar):
    def __init__(self) -> None:
        super().__init__()
        # loads an image file from the computer
        self.playerModelUp = pygame.image.load(os.path.join('assets','P1_UP.gif'))
        # resizes image file
        self.playerModelUp = pygame.transform.scale(self.playerModelUp, (40,50))
        self.playerModelDown = pygame.image.load(os.path.join('assets','P1_DOWN.gif'))
        self.playerModelDown = pygame.transform.scale(self.playerModelDown, (40,50))
        self.playerModelLeft = pygame.image.load(os.path.join('assets','P1_LEFT.gif'))
        self.playerModelLeft = pygame.transform.scale(self.playerModelLeft, (40,50))
        self.playerModelRight = pygame.image.load(os.path.join('assets','P1_RIGHT.gif'))
        self.playerModelRight = pygame.transform.scale(self.playerModelRight, (40,50))
        self.playerCurrent = self.playerModelRight




