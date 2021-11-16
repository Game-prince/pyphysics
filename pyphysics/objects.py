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
        self.friction = 0.1
        self.force = (0, 0)

        self.image = pygame.Surface(self.dimension)
        self.image.fill((255, 255, 255))

        space.add_object(self)
    
    def update(self):
        """ updates the object """

        self.velocity = (self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1])
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    def applyForce(self, x,y):
        """ applies a force to the object """

        self.force = (x, y)
        self.acceleration = (self.acceleration[0] + self.force[0] / self.mass, self.acceleration[1] + self.force[1] / self.mass)
    

class Rectangle(gameObject):
    """ This is a rectangle object """

    def __init__(self, dimension : tuple, position : tuple, space: pyphysics.space.Space) -> None:
        
        """ constructor """

        super().__init__(dimension, position, space)

class Circle(gameObject):
    """ This is a circle object """

    def __init__(self, radius : int, position : tuple, space: pyphysics.space.Space) -> None:
        
        """ constructor """

        super().__init__((radius * 2, radius * 2), position, space)

        self.radius = radius
        self.space = space

        self.image = pygame.Surface((radius * 2, radius * 2))
        self.circle = pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)
    
class Triangle(gameObject):
    """ This is a triangle object """

    def __init__(self, dimension : tuple, position : tuple, space: pyphysics.space.Space) -> None:
        
        """ constructor """

        super().__init__(dimension, position, space)
        
        self.image = pygame.Surface((dimension[0], dimension[1]))
        self.triangle = pygame.draw.polygon(self.image, (255, 255, 255), ((0, 0), (dimension[0], 0), (dimension[0] / 2, dimension[1])))
