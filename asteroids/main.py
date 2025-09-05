import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    print(f"initialized? {pygame.get_init()}")

    #set size of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set clock
    clock = pygame.time.Clock()
    dt = 0

    #create player model
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update player position based on input keys
        player.update(dt)

        #draw to GUI window
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        #refresh and update player model
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
