import numpy as np

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    for row in board:
        if np.all(row == player):
            return True
    for col in board.T:
        if np.all(col == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def is_draw(board):
    return not np.any(board == '-')

def tic_tac_toe():
    board = np.full((3, 3), '-', dtype=str)
    players = ['X', 'O']
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
        
        if board[row, col] == '-':
            board[row, col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Cell already occupied! Try again.")

# Example usage
tic_tac_toe()
