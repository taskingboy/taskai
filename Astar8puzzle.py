import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.depth + self.manhattan_distance()

    def __lt__(self, other):
        return self.cost < other.cost

    def manhattan_distance(self):
        distance = 0
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        for i in range(9):
            if self.board[i] == 0:
                continue
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal.index(self.board[i]), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
        return distance

    def get_neighbors(self):
        neighbors = []
        index = self.board.index(0)
        moves = [("Up", -3), ("Down", 3), ("Left", -1), ("Right", 1)]
        for move, pos in moves:
            new_index = index + pos
            if 0 <= new_index < 9:
                if (move == "Left" and index % 3 == 0) or (move == "Right" and index % 3 == 2):
                    continue
                new_board = self.board[:]
                new_board[index], new_board[new_index] = new_board[new_index], new_board[index]
                neighbors.append(PuzzleState(new_board, self, move, self.depth + 1))
        return neighbors

def a_star_8_puzzle(start):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    start_state = PuzzleState(start)
    heap = [start_state]
    visited = set()

    while heap:
        current = heapq.heappop(heap)
        if current.board == goal:
            path = []
            while current.parent:
                path.append(current.move)
                current = current.parent
            return path[::-1]
        visited.add(tuple(current.board))
        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(heap, neighbor)
    return None

# Example usage
start_input = [1, 2, 3, 4, 0, 5, 6, 7, 8]
result = a_star_8_puzzle(start_input)
print("Moves:", result)
