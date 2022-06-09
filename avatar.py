import pygame

class Avatar():
    def __init__(self, up = pygame.K_UP, down = pygame.K_DOWN, left = pygame.K_LEFT, right = pygame.K_RIGHT, 
    health = 100, attack = 25, moveSpeed = 4, position = [660,220], color = (0,0,0), width=20) -> None:
        self.health = health
        self.attack = attack
        self.moveSpeed = moveSpeed
        self.color = color
        self.width = width
        self.position = position
        self.up = up
        self.down = down
        self.left = left
        self.right = right
    

    def draw(self,screen):
        """draws player character to the screen"""
        # a rectangle object will contain our player image, at the coordinates specificed and the dimensions specified
        p1 = pygame.Rect((100,300), (40,50))
        # 'bit' places an object onto the screen based on coordinates from the top left corner
        screen.blit(self.playerCurrent, ((self.position[0],self.position[1]), (40,50)))
    

    def move(self):
        """allows for player movement via keypresses"""
        # this checks for any pressed keys and includes held keys
        # I have changed the key press values to variables set in the init to allow for both player classes to change it
        if pygame.key.get_pressed()[self.up]:
            # changes position based on set speed of player
            self.position[1] -= self.moveSpeed 
            # updates character sprite to reflect direction
            self.playerCurrent = self.playerModelUp
        elif pygame.key.get_pressed()[self.down]:
            self.position[1] += self.moveSpeed 
            self.playerCurrent = self.playerModelDown
        elif pygame.key.get_pressed()[self.left]:
            self.position[0] -= self.moveSpeed 
            self.playerCurrent = self.playerModelLeft
        elif pygame.key.get_pressed()[self.right]:
            self.position[0] += self.moveSpeed 
            self.playerCurrent = self.playerModelRight