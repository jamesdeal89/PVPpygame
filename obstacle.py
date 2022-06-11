"""the class for obstacles in the game"""
import pygame

class Obstacle():
    def __init__(self, position = [450,70], dimension = [3,300]) -> None:
        self.position = position
        self.dimension = dimension
        
    def create(self, screen):
        obstacle = pygame.Rect(self.position[0],self.position[1],self.dimension[0],self.dimension[1])
        pygame.draw.rect(screen, (0,0,0), obstacle)

