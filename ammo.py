# the class for ammo packs
import random
import pygame

class AmmoPack():
    def __init__(self, size = 5, x= random.randint(0, 900), y = random.randint(0, 500)):
        self.size = size
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,coOrd):
        self._x = coOrd
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,coOrd):
        self._y = coOrd

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,amount):
        self._size = amount

    def create(self, screen):
        pack = pygame.Rect(self.x,self.y,15,15)
        pygame.draw.rect(screen, (0,255,0), pack)

    def pickedUp(self):
        # TODO: if an ammo pack is picked up, remove ammopack and generate a new location
        pass


