# Sudoku Solver Using Backtracking
# Write a Python program that solves a Sudoku puzzle using a backtracking algorithm.


# Function to print the Sudoku board
def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

# Function to check if placing num in board[row][col] is valid
def is_valid(board, row, col, num):
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve Sudoku using backtracking
def solve_sudoku(board):
    # Find an empty cell
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    # Try numbers 1 through 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Place num in the cell

            # Recur to solve the rest of the board
            if solve_sudoku(board):
                return True

            # If placing num doesn't lead to a solution, undo it
            board[row][col] = 0

    return False

# Function to find an empty location on the board
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to input the Sudoku board
def input_board():
    print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
    board = []
    for i in range(9):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        if len(row) != 9:
            print("Please enter exactly 9 numbers for each row.")
            return None
        board.append(row)
    return board

# Main function to execute the solver
def main():
    board = input_board()
    if board is None:
        return

    print("\nSudoku Puzzle:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("\nNo solution exists for the provided Sudoku puzzle.")

# Run the program
main()
