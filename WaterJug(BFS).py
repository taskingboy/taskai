from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    def is_valid_state(state):
        return 0 <= state[0] <= jug1_capacity and 0 <= state[1] <= jug2_capacity

    visited = set()  # To track visited states
    queue = deque()  # BFS queue
    parent = {}  # To reconstruct the path

    # Initial state
    start_state = (0, 0)  # Both jugs are empty
    queue.append(start_state)   
    visited.add(start_state)
    parent[start_state] = None  # Root has no parent

    while queue:
        current = queue.popleft()

        # If we reached the target, reconstruct the path
        if current[0] == target or current[1] == target:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        # Generate all possible next states
        x, y = current  # Current state of the jugs
        next_states = [
            (jug1_capacity, y),       # Fill jug1
            (x, jug2_capacity),       # Fill jug2
            (0, y),                   # Empty jug1
            (x, 0),                   # Empty jug2
            (x - min(x, jug2_capacity - y), y + min(x, jug2_capacity - y)),  # Pour jug1 -> jug2
            (x + min(y, jug1_capacity - x), y - min(y, jug1_capacity - x))   # Pour jug2 -> jug1
        ]

        # Process all next states
        for state in next_states:
            if is_valid_state(state) and state not in visited:
                queue.append(state)
                visited.add(state)
                parent[state] = current

    return None  # No solution exists

# Example usage
jug1 = 3  # Capacity of Jug 1
jug2 = 5  # Capacity of Jug 2
target = 4  # Target amount

solution = water_jug_bfs(jug1, jug2, target)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
    