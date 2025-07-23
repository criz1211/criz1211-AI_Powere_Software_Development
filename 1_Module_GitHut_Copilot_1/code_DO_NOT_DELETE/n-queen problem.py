#create code for n-queen problem using backtracking
# https://en.wikipedia.org/wiki/Backtracking
#     
# The N-Queens problem is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each other. 
# This means that no two queens can be in the same row, column, or diagonal.
import numpy as np

def print_board(board, N):
    for i in range(N):
        row = ""
        for j in range(N):
            if board[i][j] == 1:
                row += "Q "
            else:
                row += ". "
        print(row)
    print()

def is_safe(board, row, col, N):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N):
                return True
            board[row][col] = 0
    return False

def solve_n_queens(N):
    board = np.zeros((N, N), dtype=int)
    if solve_n_queens_util(board, 0, N):
        print("Solution for N =", N)
        print_board(board, N)
    else:
        print("No solution exists for N =", N)

# Example usage:
if __name__ == "__main__":
    N = 8  # You can change N to any value
    solve_n_queens(N)