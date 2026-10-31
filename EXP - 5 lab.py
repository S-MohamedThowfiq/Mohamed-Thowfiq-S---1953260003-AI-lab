
N = 8
board = [-1] * N
attempts = 0

def is_safe(row, col):
    for r in range(row):
        if board[r] == col:
            return False

        if abs(board[r] - col) == abs(r - row):
            return False

    return True

def solve(row):
    global attempts

    if row == N:
        return True

    for col in range(N):
        attempts += 1

        if is_safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1  # Backtrack

    return False

if solve(0):
    print("Valid 8-Queens arrangement:")
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("\nQueen positions (row, column):")
    for row in range(N):
        print((row + 1, board[row] + 1))

    print("Placement attempts:", attempts)
else:
    print("No solution found.")
