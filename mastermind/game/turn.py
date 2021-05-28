class Turn:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.

    Stereotype: 
        Information Holder

    Attributes:
        _guess(integer): The player's guess
        _guess_list (list): _guess converted to a list
    """

    def __init__(self, guess):
        """The class constructor.

        Args:
            self (Board): an instance of Board.
        """

    def to_list(self):
        """Converts the players guess into a list, sets _guess_list equal to it"""

    def get_turn(self):
        """Returns the number of stones to remove.

        Args:
            self (Turn): an instance of Turn.
        """
