import random
from typing import Text

from mastermind.game.guess import Guess
'''
The board class keeps track of the state of the game. 
It shou
to_string() passes the current board into a string type, so it can be printed 

'''
class Board():
    def __init__(self):
        
        self._current_hint =  '****'
        self._items = self.prepare()
        self._current_name = ''




    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]
        #list_one = self._items[name]
        #code= list_one[0]

    def update(self, player):

        name = player.get_name()

        list_one = self._items[name]
        
        list_one[1] = player.get_guess()
        hint = list_one[2] = self._current_hint
        self._items[name] = list_one

        
    def _create_hint(self, code, guess):
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
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        self._current_hint = hint
        return hint
    
    def _is_complete(self, player):
        """checks if the number is complete, and if is returns a true boolean value""" 
        
        name = player.get_name()
        info = self._items[name]
        

        if info[0] == info[1]:
            return True 

        else: 
            return False
        
        
    def _to_string(self, player):
        '''
        turns the board and returns a string so it can be printed by the console
        '''
        name = player.get_name()


        text = '-----------------------\n'
        text += 