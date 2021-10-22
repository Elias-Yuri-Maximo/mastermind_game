import random
'''
The board class keeps track of the state of the game.
It shou
to_string() passes the current board into a string type, so it can be printed
'''


class Board():
    def __init__(self):
        self._items = {}
        self.code = 0
        self.count = 0
        self.name_one = ""
        self.name_two = ""
        self.hint = 0

    def prepare(self, players):
        """Sets up the board with an entry for each player.
        Args:
            self (Board): an instance of Board.
        """

        self.name_one = players[0]
        self.name_one = self.name_one.get_name()
        self.name_two = players[1]
        self.name_two = self.name_two.get_name()
        code = str(random.randint(1000, 10000))
        self.code = code
        guess = "----"
        hint = "****"
        self._items[self.name_one] = [guess, hint]
        self._items[self.name_two] = [guess, hint]

    def _create_hint(self, guess):
        """Generates a hint based on the given code and guess.
        Args:
        self (Board): An instance of Board.
        code (string): The code to compare with.
        guess (string): The guess that was made.
        Returns:
        string: A hint in the form [xxxx]
        """

        hint = ""
        for index, letter in enumerate(guess):
            if self.code[index] == letter:
                hint += "x"
            elif letter in self.code:
                hint += "o"
            else:
                hint += "*"
        if (self.count % 2) == 0:
            self._items[self.name_one] = [guess, hint]
        else:
            self._items[self.name_two] = [guess, hint]
        self.count += 1
        self.hint = hint

    def _is_complete(self):
        """checks if the number is complete, and if is returns a true boolean value"""
        if self.hint == "xxxx":
            return True
        else:
            return False

    def _to_string(self):
        player_one = self._items[self.name_one]
        player_two = self._items[self.name_two]
        string = f"---------------------\nPlayer {self.name_one}: {player_one[0]}, {player_one[1]}\nPlayer {self.name_two}: {player_two[0]}, {player_two[1]}\n--------------------"
        return string
