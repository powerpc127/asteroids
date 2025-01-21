import pygame
from constants import *
from player import Player

def main():
    pygame.init() # Initializes pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates a screen to be filled below
    clock = pygame.time.Clock() # Initializes the clock class
    player1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)) # Sets the player's starting position to the center of the screen
    dt = 0 # Creates a delta time variable to be used later. This is the time between drawing frames
    while True:
        # for loop to detect input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # Draws the background
        player1.update(dt) # Updates the position and velcoity of the player for the next frame (dt)
        player1.draw(screen) # Draws the player on the screen
        pygame.display.flip() # Prints all the data to the game window
        val = clock.tick(60) 
        dt = val/1000 # Combined with line above, sets the time increment before the loop is repeated
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()