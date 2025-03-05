import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    current_player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2) )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        current_player.update(dt)
        screen.fill((0, 0, 0))
        current_player.draw(screen)
        pygame.display.flip()
        dt = (game_clock.tick(60) / 1000)
       



if __name__ == "__main__":
    main()