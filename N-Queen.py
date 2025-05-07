# 🎯 N-Queens Problem using Backtracking and Branch & Bound (Constraint Satisfaction Problem)

def is_safe(board, row, col, n):
    """
    Check if placing a queen at board[row][col] is safe:
    - No other queen in the same column
    - No queen on the left-upper diagonal
    - No queen on the right-upper diagonal
    """
    for i in range(row):
        if board[i][col] == 1:
            return False  # Queen already in same column

    # Check left upper diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check right upper diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True  # Safe to place queen

def print_board(board, n):
    """Prints the current state of the chess board."""
    for i in range(n):
        for j in range(n):
            print("👑" if board[i][j] else ".", end=" ")
        print()
    print()

def solve_n_queens(board, row, n):
    """
    Recursive function to solve the N-Queens problem.
    Tries placing queens row by row using backtracking.
    """
    if row == n:
        print("✅ Final Solution Found:")
        print_board(board, n)
        return True  # One valid solution found

    # Try placing queen in each column of the current row
    for col in range(n):
        print(f"🔍 Trying Row {row}, Column {col}...")
        
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            print(f"✔️ Placed Queen at Row {row}, Column {col}")
            print_board(board, n)

            if solve_n_queens(board, row + 1, n):  # Recursive call for next row
                return True  # Stop after first solution

            # Backtrack: remove the queen
            board[row][col] = 0
            print(f"↩️ Backtracking from Row {row}, Column {col}")
            print_board(board, n)
        else:
            print(f"❌ Unsafe at Row {row}, Column {col}, Skipping...\n")
    return False  # No valid position in this row

# 🟢 Driver Code
n = 4  # You can change this to try 5, 6, 8, etc.
board = [[0] * n for _ in range(n)]  # Initialize empty board

print(f"\n🎯 Solving {n}-Queens Problem Step-by-Step...\n")
if not solve_n_queens(board, 0, n):
    print("❌ No solution exists.")
