import pygame

class Space:
    """ This class will implement an empty space """

    def __init__(self, dimension:tuple, caption="My game") -> None:

        """ constructor """
        
        # properties
        self.dimension : tuple = dimension
        self.gravity : float = (0, 0)
        self.drag : float = (0, 0)
        self.attraction : bool = True
        

        # making the window
        self.caption = caption
        self.screen = pygame.display.set_mode(self.dimension)
        pygame.display.set_caption(self.caption)

        # all the objects on the screen
        self.objects = []
    
    def render(self) -> None:
        """ function for rendering """

        self.screen.fill((0, 0, 0))
        
        for object in self.objects:
            self.screen.blit(object.image, object.position)

    def update(self) -> None:
        """ Function for updating the screen """

        if self.gravity != (0, 0):
            for object in self.objects:
                object.acceleration = self.gravity
                object.update()
        
        pygame.display.update()
        self.render()
    
    def add_object(self, object) -> None:
        """ function for adding an object to the space """
        self.objects.append(object)