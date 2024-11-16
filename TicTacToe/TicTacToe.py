# Tic-Tac-Toe Game (AI vs Player using Minimax)
# Build a Tic-Tac-Toe game where the AI uses the Minimax algorithm to play against a human player.

import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    # Display the Tic-Tac-Toe board
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

def check_winner(board, player):
    # All winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check if any winning condition is met
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    # Base case: check for a terminal state
    if check_winner(board, 'O'):  # AI wins
        return 1
    if check_winner(board, 'X'):  # Player wins
        return -1
    if is_board_full(board):      # Draw
        return 0

    # Minimax recursion
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                raise ValueError
            board[move] = 'X'
            break
        except ValueError:
            print("Invalid move. Please enter a number between 1 and 9 corresponding to an empty spot.")

def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI's turn
        print("AI is making a move...")
        ai_move = best_move()
        board[ai_move] = 'O'
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()
