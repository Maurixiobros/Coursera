import random

def display_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def enter_move(board, move):
    row, col = divmod(move - 1, 3)
    if board[row][col] == " ":
        board[row][col] = "X"
    else:
        print("Invalid move! Try again.")
        enter_move(board, int(input("Enter your move (1-9): ")))
    display_board(board)
    return board

def list_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_fields.append((i, j))
    return free_fields

def winner(board):
    for row in board:
        if row.count("X") == 3:
            return "X wins!"
        if row.count("O") == 3:
            return "O wins!"
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return "X wins!"
        if all(board[row][col] == "O" for row in range(3)):
            return "O wins!"
    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return "X wins!"
    if all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return "O wins!"
    return None

def draw(board):
    if all(cell != " " for row in board for cell in row):
        print("It's a draw!")
        return True
    return False


print("Welcome to Tic Tac Toe!")
print("You are 'X' and the computer is 'O'.")
print("Enter your move as a number from 1 to 9, corresponding to the board positions:")

while True:
    board = [[" " for _ in range(3)] for _ in range(3)]
    display_board(board)
    
    while True:
        move = int(input("Enter your move (1-9): "))
        board = enter_move(board, move)
        
        if winner(board):
            print(winner(board))
            break
        
        if draw(board):
            break
        
        # Computer's turn
        free_fields = list_free_fields(board)
        if free_fields:
            row, col = random.choice(free_fields)
            board[row][col] = "O"
            display_board(board)
            
            if winner(board):
                print(winner(board))
                break
            
            if draw(board):
                break
        else:
            print("No more moves left!")
            break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break