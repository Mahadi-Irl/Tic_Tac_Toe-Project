import random

# create tic tac toe class

class TTT:

    # set up empty board with 9 spaces
    def __init__(self):
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # set up a function to print the board
    def view_board(self):
        print(f' {self.board[0]} | {self.board[1]} | {self.board[2]} ')
        print('---|---|---')
        print(f' {self.board[3]} | {self.board[4]} | {self.board[5]} ')
        print('---|---|---')
        print(f' {self.board[6]} | {self.board[7]} | {self.board[8]} ')
    
    # randomly determine which player goes first
    def random_first_player(self):
        return random.randint(0, 1)
    
    # take input from the player and find the position from it
    def user_input(self):
        row, col = [int(x) for x in (input("Enter row and column numbers to fix spot: ").strip()).split()]
        if 1<= row <=3 and 1<= col <=3:
            position = (col + 3 * (row - 1)) - 1
            if self.board[position] != ' ':
                print('\nThis spot is already taken, Please try again\n')
                self.user_input()
            else:
                return position
        else:
            print('\nInvalid spot on the board, Please try again\n')
            self.user_input()

    # set the player's move on the board
    def fix_spot_on_board(self, position, player):
        self.board[position] = player
    
    # check if the player has won already
    def did_player_win(self, player):
        win = False

        # check if there's a match along the rows
        for i in range(0,8,2):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                win = True
                break
        if win:
            return win

        # check if there's a match along the columns
        for i in range(0,3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                win = True
                break
        if win:
            return win

        # check if there's a match along the diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
                win = True
        if self.board[2] == self.board[4] == self.board[6] == player:
                win = True
        if win:
            return win
        
        return win
    
    # check if board is fully filled to stop game and declare draw
    def is_board_filled(self):
        if ' ' in self.board:
            return False
        return True
    
    # swap to let the other player play his/her move
    def swap_player_turn(self, player):
        if player == 'O':
            return 'X' 
        return 'O'
    
    # start the game
    def start(self):

        player_1 = input('Please enter your name player 1: ')
        player_2 = input('Please enter your name player 2: ')
        player_to_symbol = {'X' : player_1, 'O' : player_2}

        if self.random_first_player() == 1:
            player = 'X'
        else:
            player = 'O'

        while True:
            print(f"It's {player_to_symbol[player]}'s turn (Your symbol is {player})")

            # view the board after move
            self.view_board()

            # taking user input
            position = self.user_input()
            print()

            # fixing the spot
            self.fix_spot_on_board(position, player)

            # checking whether current player has won or not
            if self.did_player_win(player):
                print(f"{player_to_symbol[player]} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print(f"Match Draw between {player_1} and {player_2}. Play Again!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.view_board()

# end


# create an object and start the game
game = TTT()
game.start()
