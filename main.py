from cv2 import circle
from enemy import Enemy
from player import Player
import pygame

width, height = 900,500
# creates the basic pygame display box
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("PYTHON RPG")


def main():
    player = Player()
    enemy = Enemy()
    run = True
    while run == True:
        # this creates a framerate of 60 frames per second
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            # stops program if player clicks 'x' in window
            if event.type == pygame.QUIT:
                run = False
        # pygame colors use RGB tuples, this is white
        screen.fill((255,255,255))
        enemy.move()
        player.move()
        enemy.draw(screen)
        player.draw(screen)
        # pygame needs the display updated after each change
        pygame.display.update()


if __name__ == "__main__":
    main()