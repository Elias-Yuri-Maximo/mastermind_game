class Guess:
   
    '''
    guesss will be responsible for storing a copy of the guess 
    and passing it into the board, which will the give the hint. 
    This will be only a store class. 
    Refer to the director if any questions.

    '''
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _pile (integer): The pile to remove from.
        _stones (integer): The number of stones to remove.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess
      

    def get_guess(self):
        """Returns the pile to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess

   