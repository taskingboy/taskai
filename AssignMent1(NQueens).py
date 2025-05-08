def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "-" for col in row))
    print()

def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper diagonal (left)
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check upper diagonal (right)
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        return True
    
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = False  # Backtrack
    
    return res

def n_queens(n):
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")

# Example usage
n_queens(8)  # Solve for 4 queens      