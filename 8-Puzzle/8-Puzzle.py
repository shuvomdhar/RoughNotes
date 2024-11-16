# 8-Puzzle Solver Using A* Algorithm
# Solve the 8-puzzle problem using A* algorithm with a heuristic function like Manhattan distance.

import heapq

class PuzzleState:
    def __init__(self, board, g, h, parent=None):
        self.board = board              # Current board state as a 2D list
        self.g = g                      # Cost from the start node to this node
        self.h = h                      # Heuristic (Manhattan distance)
        self.f = g + h                  # Total cost
        self.parent = parent            # Parent state for path reconstruction

    def __lt__(self, other):
        return self.f < other.f         # For priority queue sorting

def manhattan_distance(board, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                x, y = divmod(goal.index(board[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def flatten(board):
    return [num for row in board for num in row]

def goal_state():
    return [1, 2, 3, 4, 5, 6, 7, 8, 0]

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def get_neighbors(board):
    neighbors = []
    zero_pos = flatten(board).index(0)
    i, j = divmod(zero_pos, 3)

    moves = {
        'up': (i - 1, j),
        'down': (i + 1, j),
        'left': (i, j - 1),
        'right': (i, j + 1)
    }

    for direction, (x, y) in moves.items():
        if 0 <= x < 3 and 0 <= y < 3:
            new_board = [row[:] for row in board]
            new_board[i][j], new_board[x][y] = new_board[x][y], new_board[i][j]
            neighbors.append(new_board)

    return neighbors

def a_star(initial_board):
    goal = goal_state()
    open_set = []
    g = 0
    h = manhattan_distance(initial_board, goal)
    initial_state = PuzzleState(initial_board, g, h)

    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)

        if flatten(current.board) == goal:
            return reconstruct_path(current)

        closed_set.add(tuple(flatten(current.board)))

        for neighbor in get_neighbors(current.board):
            if tuple(flatten(neighbor)) in closed_set:
                continue

            g = current.g + 1
            h = manhattan_distance(neighbor, goal)
            neighbor_state = PuzzleState(neighbor, g, h, current)

            heapq.heappush(open_set, neighbor_state)

    return None

def input_board():
    print("Enter the initial 8-puzzle board configuration as a 3x3 grid (use 0 for the empty space):")
    board = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != 3:
            print("Each row must have exactly 3 numbers.")
            return None
        board.append(row)
    return board

def main():
    initial_board = input_board()
    if initial_board is None:
        return

    print("\nInitial Board:")
    print_board(initial_board)

    solution = a_star(initial_board)
    if solution:
        print("Solution found:")
        for step, board in enumerate(solution):
            print(f"Step {step}:")
            print_board(board)
    else:
        print("No solution exists for this configuration.")

# Run the program
main()
