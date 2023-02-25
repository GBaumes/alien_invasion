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

        # Set the game to fullscreen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)
    
    # The game is controlled by the run_game() method.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch the keyboard and mouse events.
        # Event loop to listen for events and perform appropriate tasks depending on the kind of event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
        # Move the ship to the right
            self.ship.moving_right = True
        # Move the ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Move the ship up
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        # Move the ship down
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        # Exit the game if the user hits the 'Esc' key
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    
    def _update_screen(self):
        """Update images on the screen, and flop to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        # Tells Pygame to make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()