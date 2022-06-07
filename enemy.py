"""the class for the enemy player which inherits from the avatar class"""
from avatar import Avatar
import pygame
import os

class Enemy(Avatar):
    def __init__(self):
        # initializing inherited class and changing movement keymap and changing starting coordinates
        super().__init__(up=pygame.K_w,down=pygame.K_s,left=pygame.K_a,right=pygame.K_d, position=[160,220])
        # loads an image file from the computer
        self.playerModelUp = pygame.image.load(os.path.join('assets','EN_UP.gif'))
        # resizes image file
        self.playerModelUp = pygame.transform.scale(self.playerModelUp, (40,50))
        self.playerModelDown = pygame.image.load(os.path.join('assets','EN_DOWN.gif'))
        self.playerModelDown = pygame.transform.scale(self.playerModelDown, (40,50))
        self.playerModelLeft = pygame.image.load(os.path.join('assets','EN_LEFT.gif'))
        self.playerModelLeft = pygame.transform.scale(self.playerModelLeft, (40,50))
        self.playerModelRight = pygame.image.load(os.path.join('assets','EN_RIGHT.gif'))
        self.playerModelRight = pygame.transform.scale(self.playerModelRight, (40,50))
        self.playerCurrent = self.playerModelRight
