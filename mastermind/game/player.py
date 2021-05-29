class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last move.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _turn (Turn): The player's last turn.
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._turn = None
        
    def get_turn(self):
        """Returns the player's last move (an instance of Move). If the player 
        hasn't moved yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._turn

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def set_move(self, turn):
        """Sets the player's last move to the given instance of Move.

        Args:
            self (Player): an instance of Player.
            turn (Turn): an instance of Turn
        """
        self._turn = turn