import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    #set size of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #create models
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update game models
        updatable.update(dt)

        #check for any collisions
        for asteroid in asteroids:
            if player.hasCollidedWith(asteroid):
                print("Game over!")
                exit(0)

        #draw to GUI window
        screen.fill("black")
        for model in drawable:
            model.draw(screen)
        pygame.display.flip()

        #refresh and update player model
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
