class Player:
    '''
    This class will carry information about the player do it will 
    be wehere we put the encapsulation 

        def get_guess(self):
        """Returns the player's last move (an instance of Move). If the player 
        hasn't moved yet this method returns None.

            def get_name(self):
        """Returns the player's name.

        #these two functions are here to get information from the private 
        attributes name and guess

        def set_guess(self, guess):
            """This function gets an instance of guess (the current guess)
            and set the attribute guess"""
             
    
    '''
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._move = None
        
    def get_move(self):
        """Returns the player's last move (an instance of Move). If the player 
        hasn't moved yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._move

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def set_move(self, move):
        """Sets the player's last move to the given instance of Move.

        Args:
            self (Player): an instance of Player.
            move (Move): an instance of Move
        """
        self._move = move