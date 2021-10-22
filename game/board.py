import random
'''
The board class keeps track of the state of the game.
It shou
to_string() passes the current board into a string type, so it can be printed
'''
class Board():
    def __init__(self):
        self._items = []
        self.hint = ""
        self.code = 0
        self.prepare()
    def prepare(self, player):
        """Sets up the board with an entry for each player.
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        self.code = code
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.
        Args:
        self (Board): An instance of Board.
        code (string): The code to compare with.
        guess (string): The guess that was made.
        Returns:
        string: A hint in the form [xxxx]
        """
        self.guess = guess
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        self.hint = hint
        return hint
    def _is_complete(self):
        """checks if the number is complete, and if is returns a true boolean value"""
        if self.hint == "xxxx":
            return True
        else:
            return False
    def _to_string(self, player):
    string= "  
            --------------------
            Player self.name:self.code, self.hint
            Player John: 4356, oo**
            --------------------"