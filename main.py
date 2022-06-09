from enemy import Enemy
from player import Player
from obstacle import Obstacle
import pygame

width, height = 900,500
# creates the basic pygame display box
screen = pygame.display.set_mode((width,height))
# names the title of the display box
pygame.display.set_caption("PYTHON PVP")

def main():
    player = Player()
    enemy = Enemy()
    obstacle = Obstacle()
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
        obstacle.create(screen)
        enemy.move(obstacle)
        player.move(obstacle)
        enemy.draw(screen)
        player.draw(screen)
        # pygame needs the display updated after each change
        pygame.display.update()


if __name__ == "__main__":
    main()