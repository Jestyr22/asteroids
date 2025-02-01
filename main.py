import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0 #Delta Time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #Makes the windows Close button correctly exit the game
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        #Clock.tick(60) Might not be needed, instructions said to do it in two lines but I think I can do it all in one?
        dt = (Clock.tick(60) / 1000) #Limit frames to 60FPS, assigns DT the value in seconds (Hence the / 1000, otherwise it would be milliseconds)




if __name__ == "__main__":
    main()