import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        
        #COMPLETE
        #set self.screen to ai_game.screen
        #set self.settings to ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        
        #COMPLETE
        #set self.rect.x to self.rect.width
        #set self.rect.y to self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        
        #COMPLETE
        #Make the code run when self.rect.right is greater than or equal to
        #screen_rect.right or self.rect.left is less than or equal to 0
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x