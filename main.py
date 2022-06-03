from cv2 import circle
from player import Player
import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((320,240))
    player = Player()
    while True:
        screen.fill((255,255,255))
        player.draw(screen)
        player.move()
        pygame.display.flip()


if __name__ == "__main__":
    main()