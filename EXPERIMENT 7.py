
def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]

        # Same column
        if placed == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


# Solve N-Queens using Backtracking
def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

                # Backtrack
                board[row] = -1
                backtrack_count[0] += 1

    backtrack(0)
    return solutions, backtrack_count[0]


# Display Chess Board
def display_board(solution, n):
    print(" +" + "---+" * n)

    for row in range(n):
        print(" |", end="")

        for col in range(n):
            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()
        print(" +" + "---+" * n)


# ---------------- Main Program ----------------

for n in [4, 6, 8]:
    solutions, backtracks = solve_n_queens(n)

    print(f"\nN = {n}")
    print(f"Total Solutions = {len(solutions)}")
    print(f"Backtracks = {backtracks}")

    if n == 4:
        print("\nSolutions for 4-Queens:")

        for i, sol in enumerate(solutions, 1):
            print(f"\nSolution {i}: {sol}")
            display_board(sol, n)

