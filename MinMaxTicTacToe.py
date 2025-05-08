import math

# Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check for winner
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check for draw
def is_draw(board):
    return all(cell != '-' for row in board for cell in row)

# Get available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i, j in get_available_moves(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = '-'
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i, j in get_available_moves(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = '-'
            best_score = min(score, best_score)
        return best_score

# Find best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i, j in get_available_moves(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = '-'
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Main game loop
def play_game():
    board = [['-' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are 'X', AI is 'O'.")
    print_board(board)

    while True:
        # Human move
        row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        if board[row][col] != '-':
            print("Cell is already taken. Try again.")
            continue
        board[row][col] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("🎉 You win!")
            break
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
            print("\nAI played its move:")
            print_board(board)

            if check_winner(board, 'O'):
                print("😞 AI wins!")
                break
            if is_draw(board):
                print("🤝 It's a draw!")
                break

play_game()
