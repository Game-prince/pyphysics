import pygame

class Space:
    """ This class will implement an empty space """

    def __init__(self, dimension:tuple) -> None:

        """ constructor """
        
        # properties
        self.dimension : tuple = dimension
        self.gravity : float = (0, 0)
        self.drag : float = (0, 0)
        self.attraction : bool = True

        # making the window
        self.screen = pygame.surface.set_mode(self.dimension)
    
    def render(self) -> None:
        """ function for rendering"""
        pass

    def update(self) -> None:
        """ Function for updating the screen """
        self.render()