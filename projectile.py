"""the class for projectiles"""
import pygame

class Projectile():
    def __init__(self,moveSpeed=5) -> None:
        self.moveSpeed = moveSpeed
        self.projectiles = []
    
    def create(self, playerPos, coOrd):
        """based on the player position, creates a projectile 
        which moves in whichever direction the player is facing"""
        if playerPos == "E":
            # creates an object at the players position
            # we add half the player images height to make the projectile come from the middle of their avatar
            # we also store the current direction with the rect object
            projectile = pygame.Rect(coOrd[0]+ 30, coOrd[1] + 25, 5,5)
            self.projectiles.append([projectile,playerPos])
        elif playerPos == "N":
            projectile = pygame.Rect(coOrd[0]+ 15, coOrd[1], 5,5)
            self.projectiles.append([projectile,playerPos])
        elif playerPos == "S":
            projectile = pygame.Rect(coOrd[0]+ 15, coOrd[1]+50, 5,5)
            self.projectiles.append([projectile, playerPos])
        elif playerPos == "W":
            projectile = pygame.Rect(coOrd[0], coOrd[1]+25, 5,5)
            self.projectiles.append([projectile, playerPos])


