# Import the sys and pygame modules.
import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initializes the background settings that Pygame needs to work properly.
        pygame.init()
        
        # Create a display window (The object assigned to self.screen is called a surface)
        # A surface in Pygame is a part of the screen where a game element can be displayed.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)
    
    # The game is controlled by the run_game() method.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch the keyboard and mouse events.
            # Event loop to listen for events and perform appropriate tasks depending on the kind of event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            # Tells Pygame to make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()