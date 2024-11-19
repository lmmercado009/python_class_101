# Author: Luis Mercado
# Date: 11/10/2024
# Description: Creates a class containing necessary methods for game called "Add Three"


class AddThreeGame:
    """
    Creates AddThreeGame class for a 2-player game in which players alternate choosing numbers
    from 1 to 9. A player may not select a number already chosen by either player. If at any point,
    exactly three of a player's selected numbers sum to 15, that player has won.
    If all numbers are chosen, but the win condition has not been met by either player, the game
    ends in a draw.
    """

    def __init__(self):
        """
        Initializes instance of game without any inputs
        """
        
        # at the start of the game, no numbers have been chosen, the game is unfinished, it is
        # first player's turn, and no player has achieved a winning score of 15
        self._numbers_chosen: list[int] = []
        self._current_state: str = "UNFINISHED"
        self._which_player_turn: str = "first"
        self._player_score: int = 0
    
    def get_current_state(self):
        """
        Returns state of the game based on player actions
        """

        return self._current_state
    
    def get_player_turn(self):
        """
        Returns a string indicating which player currently has an active turn
        (first or second)
        """

        return self._which_player_turn
    
    def get_player_nums(self):
        """
        Returns the list of selected numbers by the current player
        """

        # define starting index of full nums_chosen list based on p1 or p2

        if self._which_player_turn == "first":
            n = 0
        else:
            n = 1
        
        # slice every other number from full list of chosen numbers
        # start at first value (index 0) if first player or second value (index 1) if second player
        return self._numbers_chosen[n::2]
    
    def _set_player_score(self, player_nums: list[int]):
        """
        Checks whether any 3 values in current player's list of selected numbers sum to 15
        If yes, sets self._player_score equal to 15
        If no, self._player_score remains 0
        Player score is used to set new current state
        """

        # if player has not yet selected 3 or more values, score remains 0
        if len(player_nums) < 3:
            return
        # if player has selected at least 3 values, iterate through all combinations of 3 and check their sum
        else:
            # create a new empty set that will receive all combinations of player's numbers
            sum_set: set[int] = set()
            # iterate through all possible combinations of player's numbers
            for i in range(len(player_nums)):
                for j in range(len(player_nums)):
                    for k in range(len(player_nums)):
                        # add all currently indexed values from player's list to placeholder set
                        sum_set.add(player_nums[i])
                        sum_set.add(player_nums[j])
                        sum_set.add(player_nums[k])
                        # if current iteration of set has 3 values and they sum to 15, update self._player_score to initiate win condition
                        if sum(sum_set) == 15 and len(sum_set) == 3:
                            self._player_score += 15
                            return
                        # if win condition is NOT met, empty the set and move to next iteration
                        else:
                            sum_set.clear()
    
    def _set_current_state(self):
        """
        Checks for Win Conditions and updates game state accordingly:
        Player not achieving win condition -> UNFINISHED
        Player x achieving win condition -> X_WON
        All available numbers being chosen with NO win condition -> DRAW
        """

        if self._which_player_turn == "first" and self._player_score == 15:
            self._current_state = "FIRST_WON"
        elif self._which_player_turn == "second" and self._player_score == 15:
            self._current_state = "SECOND_WON"
        elif len(self._numbers_chosen) == 9 and self._player_score != 15:
            self._current_state = "DRAW"
        else:
            self._current_state = "UNFINISHED"
    
    def _set_player_turn(self):
        """
        Changes value of _which_player_turn to be the OTHER player after a turn
        is completed
        """

        if self._which_player_turn == "first":
            self._which_player_turn = "second"
        else:
            self._which_player_turn = "first"
        
    def make_move(self, move_player: str, player_num: int):
        """
        Checks for validity of move conditions (i.e. game not already being won or drawn,
        player number being in range, player number NOT already being chosen, current turn being
        entered player's turn)
        If all conditions are met, move is recorded, score is checked, current state is updated, and player turn is updated
        """

        # Define variables for each move condition --> all TRUE proceeds to move, any FALSE ends turn

        state_valid: bool = self._current_state == "UNFINISHED"
        turn_valid: bool = self._which_player_turn == move_player
        num_in_range: bool = 0 < player_num < 10
        num_available: bool = player_num not in self._numbers_chosen

        if state_valid and turn_valid and num_in_range and num_available:
            self._numbers_chosen.append(player_num)
            self._set_player_score(self.get_player_nums())
            self._set_current_state()
            self._set_player_turn()

            return True
        else:
            return False