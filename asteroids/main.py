import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    #set size of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()


    #create player model
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update game models
        updatable.update(dt)

        #draw to GUI window
        screen.fill("black")
        for model in drawable:
            model.draw(screen)
        pygame.display.flip()

        #refresh and update player model
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
