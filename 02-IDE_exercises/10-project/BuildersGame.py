# Author: Luis Mercado
# Date: 11/18/2024
# Description: Creates a class containing necessary methods
#              for a game called Builder's Game


class BuildersGame():
    """
    Class that creates a game in which 2 players each place 2 "builders" on a 5x5
    game board, and take turns moving those builders to new squares, constructing
    towers by adding levels to adjacent squares.
    The first player to move a builder on top of a 3-story tower wins.
    """

    def __init__(self):
        """
        Initializes instance of Builder's Game with no inputs
        """
        # initialize the game board as empty, representing non-built spaces as zeros
        self._game_board: list[list[str]] = [["0","0","0","0","0"],
                                             ["0","0","0","0","0"],
                                             ["0","0","0","0","0"],
                                             ["0","0","0","0","0"],
                                             ["0","0","0","0","0"]]
        
        # start game with state of UNFINISHED so that turns can be taken
        self._current_state: str = "UNFINISHED"
        
        # define up front that x moves first
        self._player_turn: str = "x"


    def _check_in_range_init(self, row1: int, col1: int, row2: int, col2: int):
        """
        Checks that starting spaces for initial placement are in legal range
        Returns False if out of range
        Returns True if in range
        """

        if 4 < row1 or row1 < 0:
            return False
        
        elif 4 < row2 or row2 < 0:
            return False
        
        elif 4 < col1 or col1 < 0:
            return False
    
        elif 4 < col2 or col2 < 0:
            return False


    def initial_placement(self, row1: int, col1: int, row2: int, col2: int, player: str):
        """
        Checks that initial placement is generally legal (no spaces off board, correct player turn, not duplicating placement)
        If those conditions are met, make sure player is placing builders on empty spaces
        If any conditions are NOT met, returns False
        If move is legal, player places 2 builders then game proceeds to the other player if they have not made initial placement
        If they have, game proceeds to standard moves
        """

        if self._check_in_range_init(row1, col1, row2, col2) == False:
            return False

        # define conditions for initial placement to be a valid action
        incorrect_player: bool = player != self._player_turn
        already_placed: bool = player in self._game_board
        first_space_occupied: bool = len(self._game_board[row1][col1]) > 1
        second_space_occupied: bool = len(self._game_board[row2][col2]) > 1
        place_on_self: bool = row1 == row2 and col1 == col2
        
        if incorrect_player:
            return False
        
        if already_placed:
            return False
        
        if first_space_occupied:
            return False
        
        if second_space_occupied:
            return False
        
        if place_on_self:
            return False
        
        else:
            self._game_board[row1][col1] += player
            self._game_board[row2][col2] += player
            self._set_player_turn()
            return True
    

    def print_game_board(self):
        """
        Returns the game board in its current state
        Visualized as a 5x5 grid
        """

        print(self._game_board[0])
        print(self._game_board[1])
        print(self._game_board[2])
        print(self._game_board[3])
        print(self._game_board[4])


    def get_current_state(self):
        """
        Returns current game state of "Player __ Won" or "UNFINISHED"
        """

        return self._current_state
    

    def _check_player_turn(self, from_row: int, from_col: int):
        """
        Checks whether it is currently the turn of the player attempting to move and build
        If player does NOT already have a builder placed at the FROM location, returns a boolean of FALSE
        """

        if self._player_turn not in self._game_board[from_row][from_col]:
            return False


    def _check_in_range_main(self, from_row: int, from_col: int, to_row: int, to_col: int, build_row: int, build_col: int):
        """
        Checks that starting, ending, and building spaces during regular turn are in range of board
        Returns False if any proposed spaces are off board
        Returns True if in range
        """

        if 4 < from_row or from_row < 0:
            return False
        
        elif 4 < to_row or to_row < 0:
            return False
        
        elif 4 < from_col or from_col < 0:
            return False
    
        elif 4 < to_col or to_col < 0:
            return False
        
        elif 4 < build_row or build_row < 0:
            return False
        
        elif 4 < build_col or build_col < 0:
            return False
        
        else:
            return True


    def _check_non_adjacent_move(self, from_row: int, from_col: int, to_row: int, to_col: int, build_row: int, build_col: int):
        """
        Checks whether current player is attempting to move more than 1 space away from builder or build more than 1 space away from moved builder
        If move is > 1 space away, returns boolean of True
        If build is > 1 space away, returns boolean of True
        """

        move_distance_row: int = abs(to_row - from_row)
        move_distance_col: int = abs(to_col - from_col)
        build_distance_row: int = abs(build_row - to_row)
        build_distance_col: int = abs(build_col - to_col)

        if move_distance_row > 1 or move_distance_col > 1:
            return True
        
        elif build_distance_row > 1 or build_distance_col > 1:
            return True  
        

    def _check_spaces_occupied(self, from_row: int, from_col: int, to_row: int, to_col: int, build_row: int, build_col: int):
        """
        Checks whether space being moved to is already occupied by any player's builder
        If occupied already, returns boolean of True
        Checks whether space being built on is already occupied by any player's builder
        If occupied already, returns boolean of True
        **One exception check is made -- if the build space is the to space, this is still allowed since that space WILL be empty
        after the move is made and before the build is done
        """

        to_space_length: int = len(self._game_board[to_row][to_col])

        if to_space_length > 1:
            return True     

        build_space_length: int = len(self._game_board[build_row][build_col])

        if build_space_length > 1:
            if build_row == from_row and build_col == from_col:
                return False
            else:
                return True
        
    
    def _check_move_tower_height(self, from_row: int, from_col: int, to_row: int, to_col: int):
        """
        Checks the height difference between the tower at FROM space and tower at TO space
        If TO space's tower is MORE than 1 level higher than FROM space's tower, returns boolean of False
        """

        move_height: int = int(self._game_board[to_row][to_col][0]) - int(self._game_board[from_row][from_col][0])

        if move_height > 1:
            return False
    

    def _check_illegal_build_height(self, build_row: int, build_col: int):
        """
        Checks whether tower being built on is higher than 3 levels
        If so, returns True and makes the move illegal
        """

        build_height: int = int(self._game_board[build_row][build_col][0])

        if build_height > 3:
            return True

    
    def _check_legal_turn(self, from_row: int, to_row: int, from_col: int, to_col: int, build_row: int, build_col: int):
        """
        Checks that an attempted move is legal based on all current game conditions
        """

        if self._current_state != "UNFINISHED":
            return False

        elif self._check_player_turn(from_row, from_col) == False:
            return False
        
        elif self._check_in_range_main(from_row, from_col, to_row, to_col, build_row, build_col) == False:
            return False
        
        elif self._check_non_adjacent_move(from_row, from_col, to_row, to_col, build_row, build_col) == True:
            return False
        
        elif self._check_spaces_occupied(from_row, from_col, to_row, to_col, build_row, build_col) == True:
            return False
        
        elif self._check_move_tower_height(from_row, from_col, to_row, to_col) == False:
            return False
        
        elif self._check_illegal_build_height(build_row, build_col) == True:
            return False        
    
    
    def _move_builder(self, from_row: int, from_col: int, to_row: int, to_col: int):
        """
        Checks that all conditions are met for current player to move one of their builders
        from its current space to a new space that is unoccupied, adjacent, and no more than
        1 level higher than the current space
        """
        
        self._game_board[from_row][from_col] = self._game_board[from_row][from_col][0]
        self._game_board[to_row][to_col] += self._player_turn


    def _check_for_move_win(self, to_row: int, to_col: int):
        """
        Checks whether current player has won by moving on top of a 3-story tower
        If TRUE, changes game state to reflect current player has won
        """

        # if builder is on top of 3-story tower, update game status -- otherwise, exit function
        if int(self._game_board[to_row][to_col][0]) >= 3:
            self._current_state = self._player_turn.upper() + "_WON"


    def _build_level(self, to_row: int, to_col: int, build_row: int, build_col: int):
        """
        Checks that all conditions are met for current player's now-moved builder to build
        an additional level on an adjacent and unoccupied space
        """   
        self._game_board[build_row][build_col] = str(int(self._game_board[build_row][build_col][0]) + 1)


    def _set_player_turn(self):
        """
        Moves self._player_turn to the next player
        """

        if self._player_turn == "x":
            self._player_turn = "o"
        
        else:
            self._player_turn = "x"


    def make_move(self, from_row: int, from_col: int, to_row: int, to_col: int, build_row: int, build_col: int):
        """
        Checks that all conditions are met for move to be considered valid
        If valid, moves builder at space in argument to new space in argument
        and builds a level at the adjacent space in argument
        """

        if self._check_legal_turn(from_row, from_col, to_row, to_col, build_row, build_col) == False:
            return False
        
        else:
            self._move_builder(from_row, from_col, to_row, to_col)
            self._check_for_move_win(to_row, to_col)
            self._build_level(to_row, to_col, build_row, build_col)
            self._set_player_turn()
            return True