class Object:
    """
    This is the object class. Every game object has atleast these properties.
    """

    def __init__(self) -> None:
        """ constructor class """

        # properties
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.image = None
        self.rect = None

        # flags
        self.is_visible = True