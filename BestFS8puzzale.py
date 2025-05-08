import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def manhattan_distance(board, goal):
    """Calculate Manhattan Distance heuristic."""
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                x, y = divmod(goal.index(board[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state, goal_state):
    """Generate possible moves (Up, Down, Left, Right)."""
    neighbors = []
    board = state.board
    x, y = next((i, j) for i in range(3) for j in range(3) if board[i][j] == 0)
    moves = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]

    for move, dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            cost = manhattan_distance(new_board, sum(goal_state, []))
            neighbors.append(PuzzleState(new_board, state, move, state.depth + 1, cost))
    
    return neighbors

def best_first_search_8_puzzle(start, goal):
    """Best First Search for 8-puzzle problem."""
    goal_flat = sum(goal, [])
    start_state = PuzzleState(start, cost=manhattan_distance(start, goal_flat))
    pq = []
    heapq.heappush(pq, start_state)
    visited = set()

    while pq:
        current = heapq.heappop(pq)
        if current.board == goal:
            path = []
            while current:
                if current.move:
                    path.append(current.move)
                current = current.parent
            return path[::-1]  # Return path in correct order
        
        visited.add(tuple(map(tuple, current.board)))
        for neighbor in get_neighbors(current, goal):
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(pq, neighbor)

    return None  # No solution found

# User Input
print("Enter start state (row-wise, use 0 for the empty tile):")
start = [list(map(int, input().split())) for _ in range(3)]

print("Enter goal state (row-wise, use 0 for the empty tile):")
goal = [list(map(int, input().split())) for _ in range(3)]

print("\nStart State:")
for row in start:
    print(row)

print("\nGoal State:")
for row in goal:
    print(row)

solution = best_first_search_8_puzzle(start, goal)
if solution:
    print("\nSolution Steps:", solution)
else:
    print("\nNo solution found!")
