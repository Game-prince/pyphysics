from physics2D.object import Object


class Rigidbody(Object):
    """
    A class which represents a rigidbody
    """

    def __init__(self) -> None:
        """ constructor """

        super().__init__()

        # properties
        self.mass = 1
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.force = [0, 0]

        # flags
        self.apply_gravity = True