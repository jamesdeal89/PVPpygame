from avatar import Avatar
import pygame
import sys

class Player(Avatar):
    def __init__(self) -> None:
        super().__init__()
    
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.position[1] -= self.moveSpeed 
                elif event.key == pygame.K_DOWN:
                    self.position[1] += self.moveSpeed 
                elif event.key == pygame.K_LEFT:
                    self.position[0] -= self.moveSpeed 
                elif event.key == pygame.K_RIGHT:
                    self.position[0] += self.moveSpeed 

