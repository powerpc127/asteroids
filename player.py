import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    # first sets the x and y values from the inputs
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Then imports the self.position and self.velocity values from the parent class
        # The third argument, radius, is also set to PLAYER_RADIUS while inheriting from CircleShape
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        # Provided by the tutorial, but it seems to draw a line from an origin to a destination self.radius pixels away.
        # Then it draws two more lines from the ends of the first ('- right' and '+ right') to the point where they intersect. 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        # dt here is tied to the clock function. See the main file for a formula. (Still trying to acurately understand workings here)
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        # This causes the object to rotate positively and negatively when d and a are pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def draw(self, screen):
        # This draws the player's triangle in white with width=2
        # I also added a hitbox for reference, which is the red circle. Removing or commenting the line out will not
        # disable the hitbox, it will only make the hitbox not appear. For debugging purposes so the hitbox is an appropriate size
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pygame.draw.circle(screen, "red", self.position, self.radius, 1)