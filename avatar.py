import pygame

class Avatar():
    def __init__(self, health = 100, attack = 25, moveSpeed = 10, position = [160,120], color = (0,0,0), width=100) -> None:
        self.health = health
        self.attack = attack
        self.moveSpeed = moveSpeed
        self.color = color
        self.width = width
        self.position = position
    
    
    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.position[0], self.position[1]),self.width)
        