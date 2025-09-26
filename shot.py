import pygame
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'purple', (self.position.x, self.position.y), self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt