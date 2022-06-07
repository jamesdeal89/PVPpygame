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

    def draw(self,screen):
        """draws player character to the screen"""
        # a rectangle object will contain our player image, at the coordinates specificed and the dimensions specified
        p1 = pygame.Rect((100,300), (40,50))
        # 'bit' places an object onto the screen based on coordinates from the top left corner
        screen.blit(self.playerCurrent, ((self.position[0],self.position[1]), (40,50)))
    
    def move(self):
        """allows for player movement via keypresses"""
        # this checks for any pressed keys and includes held keys
        if pygame.key.get_pressed()[pygame.K_UP]:
            # changes position based on set speed of player
            self.position[1] -= self.moveSpeed 
            # updates character sprite to reflect direction
            self.playerCurrent = self.playerModelUp
        elif pygame.key.get_pressed()[ pygame.K_DOWN]:
            self.position[1] += self.moveSpeed 
            self.playerCurrent = self.playerModelDown
        elif pygame.key.get_pressed()[ pygame.K_LEFT]:
            self.position[0] -= self.moveSpeed 
            self.playerCurrent = self.playerModelLeft
        elif pygame.key.get_pressed()[ pygame.K_RIGHT]:
            self.position[0] += self.moveSpeed 
            self.playerCurrent = self.playerModelRight


