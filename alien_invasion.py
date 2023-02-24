# Import the sys and pygame modules.
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initializes the background settings that Pygame needs to work properly.
        pygame.init()
        # Make and instance of the settings class
        self.settings = Settings()

        # Create a display window (The object assigned to self.screen is called a surface)
        # A surface in Pygame is a part of the screen where a game element can be displayed.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    # The game is controlled by the run_game() method.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            # Tells Pygame to make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch the keyboard and mouse events.
        # Event loop to listen for events and perform appropriate tasks depending on the kind of event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()