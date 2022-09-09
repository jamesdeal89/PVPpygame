from enemy import Enemy
from player import Player
from obstacle import Obstacle
from ammo import AmmoPack
import pygame
import sys
import time


# TODO: make ammo packs
# TODO: make healing hearts
# TODO: make cooldown for shooting (1 second cooldown between shots?)
# TODO: make multiple stages


width, height = 900,500
# creates the basic pygame display box
screen = pygame.display.set_mode((width,height))
# names the title of the display box
pygame.display.set_caption("PYTHON PVP")
# intialises the font to be used for health display
pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# custom pygame events to be used later
playerHit = pygame.USEREVENT + 1
enemyHit = pygame.USEREVENT + 2
playerWin = pygame.USEREVENT + 3
enemyWin = pygame.USEREVENT + 4

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
        # based on player direction when the projectile was created
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

def checkAmmoPack(player, enemy, pack):
    # checks if either player has colided with an ammo pack and change their ammo level
    pass



def lives(event, player, enemy):
    # uses the pygame events we established in checkCollision() to adjust the health attribute
    # raises an event for a winner when one has no more health
    if event == pygame.event.Event(enemyHit) and enemy.health > 0:
        # change enemy's health by the player's attack value using it's setter
        enemy.health -= player.attack
    elif event == pygame.event.Event(playerHit) and player.health > 0:
        player.health -= enemy.attack
    if enemy.health <= 0:
        print("Player Wins!")
        pygame.event.post(pygame.event.Event(playerWin))
    elif player.health <= 0:
        print("Enemy Wins!")
        pygame.event.post(pygame.event.Event(enemyWin))


def healthBars(avatar):
    # adjusts text to be rendered on screen for health bars and ammo
    if type(avatar) == Enemy:
        bar = my_font.render("Left: " + str(avatar.health) + " Ammo: " + str(avatar.ammo), False, (0, 0, 0))
    elif type(avatar) == Player:
        bar = my_font.render("Right: " + str(avatar.health) + " Ammo: " + str(avatar.ammo), False, (0, 0, 0))
    return bar


def endScreen(event):
    # checks for the enemyWin or playerWin event and ends the game if raised. Stops main(). 
    if event == pygame.event.Event(playerWin) or event == pygame.event.Event(enemyWin):
        return True

def main():
    player = Player()
    enemy = Enemy()
    obstacle = Obstacle()
    ammo = AmmoPack()
    run = True
    while run == True:
        # this creates a framerate of 60 frames per second
        pygame.time.Clock().tick(60)
        # checks for end of game
        for event in pygame.event.get():
            player.checkAttack(event)
            enemy.checkAttack(event)
            lives(event, player, enemy)
            if endScreen(event):
                run = False
        # pygame colors use RGB tuples, this is white
        screen.fill((255,255,255))
        obstacle.create(screen)
        ammo.create(screen)
        enemy.move(obstacle)
        player.move(obstacle)
        enemy.draw(screen)
        player.draw(screen)
        checkCollision(player, enemy, obstacle)
        for projectile in enemy.projectile.projectiles:
            pygame.draw.rect(screen,(0,0,0),projectile[0])
        for projectile in player.projectile.projectiles:
            pygame.draw.rect(screen,(0,0,0), projectile[0])
        # blit health bars to the screen
        screen.blit(healthBars(player), (700,0))
        screen.blit(healthBars(enemy), (10,0))
        # pygame needs the display updated after each change
        pygame.display.update()
    if run == False:
        # runs when the game is complete to create an endscreen
        pygame.time.Clock().tick(60)
        screen.fill((255,255,255))
        if enemy.health <= 0:
            screen.blit(my_font.render("Right wins!", False, (0, 0, 0)),(370,200))
        else:
            screen.blit(my_font.render("Left wins!", False, (0, 0, 0)),(370,200))
        pygame.display.update()
        # displays endscreen for 10 seconds and then quits
        time.sleep(10)
        sys.exit()



if __name__ == "__main__":
    main()