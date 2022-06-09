"""the class for projectiles"""
class Projectile():
    def __init__(self,direct,moveSpeed=5) -> None:
        self.direct = direct
        self.moveSpeed = moveSpeed
    
    def create(self, playerPos):
        """based on the player position, creates a projectile 
        which moves in whichever direction the player is facing"""
        pass