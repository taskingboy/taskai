import heapq
import math

class GridNode:
    def __init__(self, x, y, cost=0, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def best_first_search_robot(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    start_node = GridNode(*start, euclidean_distance(*start, *goal))
    pq = []
    heapq.heappush(pq, start_node)
    visited = set()
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        current = heapq.heappop(pq)
        if (current.x, current.y) == goal:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]
        
        visited.add((current.x, current.y))

        for dx, dy in directions:
            new_x, new_y = current.x + dx, current.y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 0:
                if (new_x, new_y) not in visited:
                    cost = euclidean_distance(new_x, new_y, *goal)
                    heapq.heappush(pq, GridNode(new_x, new_y, cost, current))
    
    return None

# User Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter grid row-wise (0 for open, 1 for obstacle):")
grid = [list(map(int, input().split())) for _ in range(rows)]

start = tuple(map(int, input("Enter start position (row column): ").split()))
goal = tuple(map(int, input("Enter goal position (row column): ").split()))

print("\nGrid:")
for row in grid:
    print(row)

print("\nStart Position:", start)
print("Goal Position:", goal)

solution = best_first_search_robot(grid, start, goal)
if solution:
    print("\nRobot Path:", solution)
else:
    print("\nNo path found!")
