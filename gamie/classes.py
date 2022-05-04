class Player:
    """A class for player character."""

    def __init__(self):

        self.denars = 0
        self.energy = 100
        self.max_hp = 100
        self.hp = 100

class Enemy:
    """A class for enemies."""

    def __init__(self, PCLevel):

        self.hp = 50