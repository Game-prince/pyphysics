import pygame
import pyphysics

class gameObject:
    """ This is a base class for all the game objects present in the game. """

    def __init__(self, dimension : tuple, position : tuple, space: pyphysics.space.Space) -> None:
        
        """ constructor """

        # properties
        self.dimension = dimension
        self.position = position
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.mass = 1

        self.image = pygame.Surface(self.dimension)
        self.image.fill((255, 255, 255))

        space.add_object(self)
    
    def update(self):
        """ updates the object """

        self.velocity = (self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1])
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])