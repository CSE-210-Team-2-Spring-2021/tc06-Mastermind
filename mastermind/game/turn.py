class Turn:
    """ A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.

        Stereotype: 
            Information Holder

        Attributes:
            _guess(integer): The player's guess
            _guess_list (list): _guess converted to a list
    """

    def __init__(self, guess):
        """ The class constructor.

            Args:
                self (Board): an instance of Board.
        """
        self._guess = guess
        self._guess_list = []

    def to_list(self):
        """ Converts the players guess into a list, sets _guess_list equal to it

            Args:
                self (Turn): an instance of Turn.
        """
        self._guess = map(int, str(self._guess))
        self._guess_list = list(self._guess)
        return self._guess_list

    def get_turn(self):
        """Returns the number of stones to remove.

        Args:
            self (Turn): an instance of Turn.
        """
        return self._guess_list
