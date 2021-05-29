from game.mastermind import Mastermind
from game.console import Console
from game.turn import Turn
from game.player import Player
from game.roster import Roster


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        mastermind (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        roster (Roster): An instance of the class of objects known as Roster.
        player (Player): An instance of the class of objects known as Player.
        turn (Guess): An instance of the class of objects known as Turn.
        keep_playing (boolean): Whether or not the game can continue.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._mastermind = Mastermind()
        self._console = Console()
        self._roster = Roster()
        self._player = Player()
        self._turn = Turn()
        self._keep_playing = True
        self._move = None

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
           # self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._player.set_move('----')
            self._roster.add_player(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        board = self._mastermind.hint(self._roster.get_players())
        self._console.write(board)
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your guess? ")
        turn = self._turn(guess)
        player.set_turn(turn)

    
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if guess is equals to the secret number.

        Args:
            self (Director): An instance of Director.
        """
        self._player
        if self._mastermind.is_won(self._player.get_turn()):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        else:
            self._roster.next_player()
