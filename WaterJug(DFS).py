def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    # Helper function to check if a state is valid
    def is_valid_state(state):
        return 0 <= state[0] <= jug1_capacity and 0 <= state[1] <= jug2_capacity

    # Helper function for DFS
    def dfs(state, visited, path):
        # Base case: if the target is reached
        if state[0] == target or state[1] == target:
            path.append(state)
            return True

        # Mark the current state as visited
        visited.add(state)
        path.append(state)

        # Generate all possible next states
        x, y = state  # Current state of the jugs
        next_states = [
            (jug1_capacity, y),       # Fill jug1
            (x, jug2_capacity),       # Fill jug2
            (0, y),                   # Empty jug1
            (x, 0),                   # Empty jug2
            (x - min(x, jug2_capacity - y), y + min(x, jug2_capacity - y)),  # Pour jug1 -> jug2
            (x + min(y, jug1_capacity - x), y - min(y, jug1_capacity - x))   # Pour jug2 -> jug1
        ]

        # Explore each state using DFS
        for next_state in next_states:
            if is_valid_state(next_state) and next_state not in visited:
                if dfs(next_state, visited, path):  # Recursive call
                    return True

        # Backtrack if no solution is found from the current state
        path.pop()
        return False

    # Initialize visited states and path
    visited = set()
    path = []

    # Start DFS from the initial state (0, 0)
    if dfs((0, 0), visited, path):
        return path
    else:
        return None  # No solution exists

# Example usage
jug1 = 3  # Capacity of Jug 1
jug2 = 5  # Capacity of Jug 2
target = 4  # Target amount

solution = water_jug_dfs(jug1, jug2, target)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
    