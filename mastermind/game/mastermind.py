import random


class Mastermind:
    """ This is the designated playing "surface".


        Stereotype:
        Information holder


        Attributes:
            _code_list - list of numbers
    """

    def __init__(self):
        """ Constructor, initializes the variables.

            Args:
                self - an instance of Mastermind
        """

        self._code_list = []
        self._prepare()

    def _prepare(self, player):
        """ Generate the secret code and turn it into a list

            Args:
                self - an instance of Mastermind
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def compare(self, code, guess):
        """ Responsible for comparing the guess with the code and returning the hint value(list)

            Args:
                self (Mastermind): an instance of Mastermind
                code (string): The code to compare with
                guess (string): The guess that made

            Returns:
            string: A hint with the form of [xxxx]
        """
        hint = ""
        for turn, letter in enumerate(guess):
            if code[turn] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def display(self, player, turn):
        """ Using compare return a str output with player guesses and hints.

            Args:
                self - an instance of Mastermind

            Example of string:
            -------------------------
            Player Matt: 9452, XXO*
            Player John: 5490, OXO*
            -------------------------
            players -  a list of player objects that will be passed in from director,
            here for the get_name and get_turn functions
        """
        player = player.get_name()
        guess = turn.get_turn()
        hint = 0
        text = "\n-------------------------"
        text += f"\nPlayer {player}: " + "{}, " * guess + "{}" * hint
        text += f"\nPlayer {player}: "
        text = "\n-------------------------"
        return text

    def is_won(self):
        """ Responsible for seeing if the guess matches the code, if so return boolean True, otherwise False

            Args:
                self - an instance of Mastermind
        """
        won = ["*"] * len(self._code_list)
        return self._code_list == won
