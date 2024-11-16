# N-Queens Problem
# Solve the N-Queens problem using a backtracking algorithm in Python.

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, N):
    # Check the column for conflicts
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal for conflicts
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal for conflicts
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, N):
    # If all queens are placed, return True
    if row >= N:
        return True

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Recursively place the rest of the queens
            if solve_n_queens(board, row + 1, N):
                return True

            # Backtrack if placing queen here does not lead to a solution
            board[row][col] = 0

    return False

def n_queens(N):
    # Initialize an empty N x N board
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solve_n_queens(board, 0, N):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists for this board size.")

# Get user input for the number of queens
N = int(input("Enter the number of queens (N): "))

# Run the N-Queens solver
n_queens(N)
