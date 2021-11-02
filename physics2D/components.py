import pygame
from pygame.color import THECOLORS

from physics2D.object import Object

class components:
    """
    This is the basic class for differnt components
    """

    def __init__(self, pos : tuple, size : tuple, color : tuple) -> None:
        """ constructor class """
        self.pos = pos
        self.size = size
        self.color = color

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def draw(self, surface: pygame.Surface) -> None:
        """
        This function draws the component
        """
        
        surface.blit(self.image, self.pos)
    
    def update(self, dt: float) -> None:
        """
        This function updates the component
        """
        pass

class sun(components, Object):
    """ Makes a sun """

    def __init__(self, pos: tuple, size: tuple, color: tuple) -> None:
        super().__init__(pos, size, color)

class ground(components, Object):
    """
    Makes a ground
    """

    def __init__(self, width, height, color):
        super().__init__((0, 0), (width, height), color)

# Making differnt components using pygame
def make_ground(width, height, color):
    """
    Makes a ground
    """
    ground = pygame.Surface((width, height))
    ground.fill(color)
    return ground

def make_sun(r, color):
    """
    Makes a sun
    """
    sun = pygame.Surface((r, r))
    sun.fill(THECOLORS["skyblue"])
    pygame.draw.circle(sun, color, (r//2, r//2), r//2)
    return sun

def make_box2D(width, height, color):
    """
    Makes a box2D
    """
    box = pygame.Surface((width, height))
    box.fill(color)
    return box