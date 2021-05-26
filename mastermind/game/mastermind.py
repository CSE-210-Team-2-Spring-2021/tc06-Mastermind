import random

class Mastermind:
    """This is the designated playing "surface".

    Stereotype:
    Information holder

    Attributes:
        _code_list - list of numbers"""

    def __init__(self):
        """Constructor
        Args:
            self - an instance of Board"""

    
    def _prepare(self):
        """Generate the secret code and turn it into a list"""

    def compare(self, guess_list):
        """Responsible for comparing the guess and code and returning the hint value(list)"""
        
    def hint(self, players):
        """Using compare return a str output with player guesses and hints
			 Example of string:
				-------------------------
				Player Matt: 9452, XXO*
				Player John: 5490, OXO*
				-------------------------
            players -  a list of player objects that will be passed in from director,
            here for the get_name and get_move functions"""

    def is_won(self, guess_list):
        """Responsible for seeing if the guess matches the code, if so return boolean True, otherwise False"""