import pygame
import sys
from projectile import Projectile

class Avatar():
    def __init__(self, up = pygame.K_UP, down = pygame.K_DOWN, left = pygame.K_LEFT, right = pygame.K_RIGHT, shoot = pygame.K_RCTRL, 
    health = 100, attack = 25, moveSpeed = 4, position = [660,220], color = (0,0,0), width=20, current="N") -> None:
        self.health = health
        self.attack = attack
        self.moveSpeed = moveSpeed
        self.color = color
        self.width = width
        self.position = position
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.current = current
        self.shoot = shoot
        self.projectile = Projectile()
    

    def draw(self,screen):
        """draws player character to the screen"""
        # a rectangle object will contain our player image, at the coordinates specificed and the dimensions specified
        self.rect = pygame.Rect((self.position[0],self.position[1]), (40,50))
        # 'bit' places an object onto the screen based on coordinates from the top left corner
        screen.blit(self.playerCurrent, ((self.position[0],self.position[1]), (40,50)))
    
    def checkAttack(self, event):
        # checks if the player pressed the 'shoot' key but do not accept holding down input
        # allows quiting of the game window via 'x' button
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == self.shoot:
                self.projectile.create(self.current,self.position)

    def move(self, obstacle):
        """allows for player movement via keypresses"""
        # this checks for any pressed keys and includes held keys
        # I have changed the key press values to variables set in the init to allow for both player classes to change it
        # it also prevents players from leaving the border by checking if moving would make them exit the dimensions of the window.
        if pygame.key.get_pressed()[self.up] and self.position[1] - self.moveSpeed > 0:
            # checks if the position is below or above the obstacle and if moving would place the player on top.
            if self.position[0] > obstacle.position[0] and self.position[0] < obstacle.position[0]+obstacle.dimension[0] and self.position[1] - self.moveSpeed < obstacle.position[1]:
                pass
            else:
                # changes position based on set speed of player
                self.position[1] -= self.moveSpeed 
                # updates character sprite to reflect direction
                self.playerCurrent = self.playerModelUp
                # updates value of indicator for projectile direction
                self.current = "N"
        elif pygame.key.get_pressed()[self.down] and self.position[1] + self.moveSpeed < 450:
            self.position[1] += self.moveSpeed 
            self.playerCurrent = self.playerModelDown
            self.current = "S"
        elif pygame.key.get_pressed()[self.left] and self.position[0] - self.moveSpeed > 0:
            # checks if player is within y position of obstacle and if moving would cross the boundary
            if self.position[1]+40 > obstacle.position[1] and self.position[1] < obstacle.position[1]+obstacle.dimension[1] and self.position[0] - self.moveSpeed - obstacle.dimension[0] < obstacle.position[0] and self.position[0] > obstacle.position[0]:
                pass
            else:
                self.position[0] -= self.moveSpeed 
                self.playerCurrent = self.playerModelLeft
                self.current = "W"
        elif pygame.key.get_pressed()[self.right] and self.position[0] + self.moveSpeed < 850:
            if self.position[1]+40 > obstacle.position[1] and self.position[1] < obstacle.position[1]+obstacle.dimension[1] and self.position[0] + self.moveSpeed + obstacle.dimension[0] + 40 > obstacle.position[0] and self.position[0] < obstacle.position[0]:
                pass
            else:
                self.position[0] += self.moveSpeed 
                self.playerCurrent = self.playerModelRight
                self.current = "E"

