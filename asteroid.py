import pygame
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        #Note for future me reviewing: Inheriting from CircleShape gives it the position, I don't need to do anything with it, despite thinking I did
        #First time working with their code like this, should read though it more thoroughly

    def update(self, dt):
        self.position += self.velocity * dt

