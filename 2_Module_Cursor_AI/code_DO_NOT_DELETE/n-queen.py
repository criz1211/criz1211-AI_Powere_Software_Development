#write code for n queen problem using backtracking

def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this column on upper side
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def solve(board, row, solutions):
        if row == n:
            # Found a solution
            solutions.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1, solutions)
                board[row][col] = '.'  # Backtrack

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, solutions)
    return solutions


def print_solutions(solutions):
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()


def main():
    n = int(input("Enter the value of N: "))
    solutions = solve_n_queens(n)
    print(f"Total solutions: {len(solutions)}")
    print_solutions(solutions)


if __name__ == "__main__":
    main()
