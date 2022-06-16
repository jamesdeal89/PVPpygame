from enemy import Enemy
from player import Player
from obstacle import Obstacle
import pygame

width, height = 900,500
# creates the basic pygame display box
screen = pygame.display.set_mode((width,height))
# names the title of the display box
pygame.display.set_caption("PYTHON PVP")
# custom pygame events for enemy being hit and player being hit
playerHit = pygame.USEREVENT + 1
enemyHit = pygame.USEREVENT + 2

def checkCollision(player, enemy, obstacle):
    # for every projectile for the given player 
    for projectile in player.projectile.projectiles:
        # move the projectile by the projectile speed each frame
        # based on which direction the player was facing when projectile created
        if projectile[1] == "N":
            projectile[0].y -= enemy.projectile.moveSpeed
        elif projectile[1] == "E":
            projectile[0].x += enemy.projectile.moveSpeed
        elif projectile[1] == "S":
            projectile[0].y += enemy.projectile.moveSpeed
        elif projectile[1] == "W":
            projectile[0].x -= enemy.projectile.moveSpeed
        # if the projectile collides with the rect which represents the enemy
        if enemy.rect.colliderect(projectile[0]):
            # remove the projectile 
            player.projectile.projectiles.remove(projectile)
            # raise the pygame event we created for the enemy being hit
            pygame.event.post(pygame.event.Event(enemyHit))
        # check if the projectile hit the obstacle
        if obstacle.obstacle.colliderect(projectile[0]):
            # remove the projectile 
            player.projectile.projectiles.remove(projectile)
    # for every projectile for the given player
    for projectile in enemy.projectile.projectiles:
        # move the projectile by the projectile speed each frame
        if projectile[1] == "N":
            projectile[0].y -= enemy.projectile.moveSpeed
        elif projectile[1] == "E":
            projectile[0].x += enemy.projectile.moveSpeed
        elif projectile[1] == "S":
            projectile[0].y += enemy.projectile.moveSpeed
        elif projectile[1] == "W":
            projectile[0].x -= enemy.projectile.moveSpeed
        # if the projectile collides with the rect which represents the player
        if player.rect.colliderect(projectile[0]):
            # remove the projectile 
            enemy.projectile.projectiles.remove(projectile)
            # raise the pygame event we created for the player being hit
            pygame.event.post(pygame.event.Event(playerHit))
        # check if the projectile hit the obstacle
        if obstacle.obstacle.colliderect(projectile[0]):
            # remove the projectile 
            enemy.projectile.projectiles.remove(projectile)




def main():
    player = Player()
    enemy = Enemy()
    obstacle = Obstacle()
    run = True
    while run == True:
        # this creates a framerate of 60 frames per second
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            player.checkAttack(event)
            enemy.checkAttack(event)
        # pygame colors use RGB tuples, this is white
        screen.fill((255,255,255))
        obstacle.create(screen)
        enemy.move(obstacle)
        player.move(obstacle)
        enemy.draw(screen)
        player.draw(screen)
        checkCollision(player, enemy, obstacle)
        for projectile in enemy.projectile.projectiles:
            pygame.draw.rect(screen,(0,0,0),projectile[0])
        for projectile in player.projectile.projectiles:
            pygame.draw.rect(screen,(0,0,0), projectile[0])
        # pygame needs the display updated after each change
        pygame.display.update()


if __name__ == "__main__":
    main()