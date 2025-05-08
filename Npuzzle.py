import heapq
import copy

def get_goal_state(k):
    """Generate the goal state for a k*k puzzle."""
    goal = [[(i * k + j) % (k * k) for j in range(k)] for i in range(k)]
    return goal

def find_position(value, state):
    """Find the position of a value in the state."""
    for i, row in enumerate(state):
        if value in row:
            return i, row.index(value)

def manhattan_distance(state, goal, k):
    """Calculate the Manhattan distance of the current state from the goal."""
    distance = 0
    for i in range(k):
        for j in range(k):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = find_position(value, goal)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def get_neighbors(state, k):
    """Generate all valid neighbors for the given state."""
    neighbors = []
    x, y = find_position(0, state)
    directions = [("UP", -1, 0), ("DOWN", 1, 0), ("LEFT", 0, -1), ("RIGHT", 0, 1)]
    for direction, dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < k and 0 <= new_y < k:
            new_state = copy.deepcopy(state)
            # Swap the empty cell with the neighbor
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append((direction, new_state))
    return neighbors

def solve_puzzle(k, initial_state):
    """Solve the N-Puzzle using A* algorithm."""
    goal = get_goal_state(k)
    priority_queue = []
    visited = set()

    # Push the initial state with its heuristic value
    heapq.heappush(priority_queue, (manhattan_distance(initial_state, goal, k), 0, initial_state, []))

    while priority_queue:
        _, moves, current_state, path = heapq.heappop(priority_queue)
        state_tuple = tuple(tuple(row) for row in current_state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        # Check if the current state is the goal
        if current_state == goal:
            return moves, path

        # Generate neighbors and push them to the priority queue
        for direction, neighbor in get_neighbors(current_state, k):
            if tuple(tuple(row) for row in neighbor) not in visited:
                heapq.heappush(priority_queue, (
                    moves + 1 + manhattan_distance(neighbor, goal, k),
                    moves + 1,
                    neighbor,
                    path + [direction]
                ))

# Input Reading
k = int(input())  # Size of the grid
flat_input = [int(input()) for _ in range(k * k)]  # Read k*k numbers from input
initial_state = [flat_input[i * k:(i + 1) * k] for i in range(k)]  # Convert to 2D grid

# Solve the puzzle
moves, path = solve_puzzle(k, initial_state)

# Output the result
print(moves)
for step in path:
    print(step)
