import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        updated_radius = old_radius - ASTEROID_MIN_RADIUS

        old_velocity = self.velocity
        old_position = self.position

        #destroy the larger asteroid
        self.kill()

        #don't split if the asteroid is too small
        if old_radius <= ASTEROID_MIN_RADIUS:
            return

        #let the two smaller asteroids travel in opposite directions
        random_angle = random.uniform(20, 50)        
        first_split = old_velocity.rotate(random_angle)
        second_split = old_velocity.rotate(-random_angle)

        first_smaller_asteroid = Asteroid(old_position.x, old_position.y, updated_radius)
        second_smaller_asteroid = Asteroid(old_position.x, old_position.y, updated_radius)

        first_smaller_asteroid.velocity = first_split * 1.2
        second_smaller_asteroid.velocity = second_split * 1.2


