import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
   
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Player.containers = (updateable,drawable)
    current_player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2) )
    


    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        updateable.update(dt)
        
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)
      
        pygame.display.flip()

        #limit the framerate to 60 FPS
        dt = (game_clock.tick(60) / 1000)
       



if __name__ == "__main__":
    main()