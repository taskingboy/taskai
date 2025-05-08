def print_board(board, n):
    print("\n    " + "═" * (n * 4 + 1))
    for i in range(n):
        print(f" {n-i} ║", end=" ")
        for j in range(n):
            if board[i][j] == 1:
                print("👑", end=" ")
            else:
                print("⬜" if (i + j) % 2 == 0 else "⬛", end=" ")
        print("║")
    print("    " + "═" * (n * 4 + 1))
    print("     ", end="")
    for j in range(n):
        print(f"{chr(65+j)}  ", end="")
    print("\n")

def is_safe(board, row, col, n):
    for j in range(col):
        if board[row][j] == 1:
            return False
            
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    return True

def solve_nqueens(n):
    board = [[0 for x in range(n)] for y in range(n)]
    
    def solve_util(col):
        if col >= n:
            return True
            
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                print(f"\nPlacing queen at {chr(65+col)}{n-row}")
                print_board(board, n)
                
                if solve_util(col + 1):
                    return True
                    
                board[row][col] = 0
                print(f"\nRemoving queen from {chr(65+col)}{n-row}")
                print_board(board, n)
                
        return False

    print(f"\nSolving {n}x{n} N-Queens\n")
    if solve_util(0):
        print("\nSolution found!")
        print_board(board, n)
        return True
    else:
        print("\nNo solution exists")
        return False

n = int(input("Enter board size (e.g., 4 or 8): "))
solve_nqueens(n)