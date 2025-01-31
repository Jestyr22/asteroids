import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0 #Delta Time = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #Makes the windows Close button correctly exit the game
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        #Clock.tick(60) Might not be needed, instructions said to do it in two lines but I think I can do it all in one?
        dt = (Clock.tick(60) / 1000) #Limit frames to 60FPS, assigns DT the value in seconds (Hence the / 1000, otherwise it would be milliseconds)




if __name__ == "__main__":
    main()