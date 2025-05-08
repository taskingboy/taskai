import heapq
import math

class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def a_star_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    start_node = Node(start[0], start[1], 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    visited = set()

    while open_list:
        current = heapq.heappop(open_list)
        if (current.x, current.y) == goal:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]
        visited.add((current.x, current.y))
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if (nx, ny) not in visited:
                    g = current.g + 1
                    h = heuristic((nx, ny), goal)
                    heapq.heappush(open_list, Node(nx, ny, g, h, current))
    return None

def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Example usage
grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]
start = (0, 0)
goal = (3, 3)
path = a_star_grid(grid, start, goal)
print("Path:", path)
