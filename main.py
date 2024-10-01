board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
game_still_going = True
winner = None
current_player = "X"

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def restart_game():
    answer= input("Play again? Type y or n:")

    if answer == "y" or answer=="Y" or answer=="Y " or answer=="y " or answer==" y" or answer==" Y" or answer==" Y " or answer==" y ":
        global board
        board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        global game_still_going
        game_still_going = True
        global winner
        winner = None
        global current_player
        current_player = "X"
        play_game()
    elif answer=="N" or answer=="n" or answer=="n " or answer=="N " or answer==" n" or answer==" N" or answer==" N " or answer==" n ":
      print("Thanks for playing!\n")
    else: 
      print("valid input. please try typing again.\n")
      restart_game()
      
      
def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner:
        print(winner + " won.\n")
        restart_game()
    else:
        print("Tie.\n")
        restart_game()

def handle_turn(player):
    valid = False
    while not valid:
        position = input(f"{player}, choose a position from 1-9: ")
        position = int(position) - 1
        if position >= 0 and position < 9 and board[position] == "_":
            board[position] = player
            valid = True
        else:
            print("Invalid position, try again.")
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner

def check_rows():
    global game_still_going
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != "_":
            game_still_going = False
            return board[i]
    return None

def check_columns():
    global game_still_going
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != "_":
            game_still_going = False
            return board[i]
    return None

def check_diagonals():
    global game_still_going
    if board[0] == board[4] == board[8] != "_":
        game_still_going = False
        return board[0]
    if board[2] == board[4] == board[6] != "_":
        game_still_going = False
        return board[2]
    return None

def check_if_tie():
    global game_still_going
    if "_" not in board and winner is None:
        game_still_going = False

def flip_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

play_game()
