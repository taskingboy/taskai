from heapq import heappop, heappush
import itertools

# Directions for moving the empty tile (0)
DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

# Converts a 1D list to a 2D grid
def to_grid(state, k):
    return [state[i:i + k] for i in range(0, len(state), k)]

# Converts a 2D grid to a 1D list
def to_list(grid):
    return [tile for row in grid for tile in row]

# Finds the position of the empty tile (0)
def find_empty_tile(state, k):
    idx = state.index(0)
    return divmod(idx, k)

# Heuristic: Manhattan distance
def manhattan_distance(state, goal_state, k):
    distance = 0
    for i in range(len(state)):
        if state[i] == 0:
            continue
        goal_pos = divmod(goal_state.index(state[i]), k)
        curr_pos = divmod(i, k)
        distance += abs(goal_pos[0] - curr_pos[0]) + abs(goal_pos[1] - curr_pos[1])
    return distance

# Generates all valid moves from the current state
def generate_moves(state, k):
    grid = to_grid(state, k)
    empty_row, empty_col = find_empty_tile(state, k)
    moves = []

    for direction, (dr, dc) in DIRECTIONS.items():
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < k and 0 <= new_col < k:
            # Swap empty tile with the adjacent tile
            new_grid = [row[:] for row in grid]
            new_grid[empty_row][empty_col], new_grid[new_row][new_col] = (
                new_grid[new_row][new_col],
                new_grid[empty_row][empty_col],
            )
            moves.append((to_list(new_grid), direction))

    return moves

# A* search algorithm
def solve_puzzle(start_state, goal_state, k):
    frontier = []
    heappush(frontier, (0, 0, start_state, []))  # (priority, cost, state, moves)
    visited = set()

    while frontier:
        _, cost, current_state, moves = heappop(frontier)

        if tuple(current_state) in visited:
            continue

        visited.add(tuple(current_state))

        if current_state == goal_state:
            return cost, moves

        for next_state, direction in generate_moves(current_state, k):
            if tuple(next_state) not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan_distance(next_state, goal_state, k)
                heappush(frontier, (priority, new_cost, next_state, moves + [direction]))

    return -1, []  # Return -1 if no solution is found

# Hill Climbing algorithm
def hill_climbing(start_state, goal_state, k):
    current_state = start_state
    current_moves = []

    while current_state != goal_state:
        possible_moves = generate_moves(current_state, k)
        next_state = None
        best_heuristic = float('inf')

        for state, direction in possible_moves:
            heuristic = manhattan_distance(state, goal_state, k)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                next_state = (state, direction)

        if not next_state or best_heuristic >= manhattan_distance(current_state, goal_state, k):
            # No better state found, terminate
            break

        current_state, direction = next_state
        current_moves.append(direction)

    return len(current_moves), current_moves

# Input processing
def main():
    print("Choose the algorithm to solve the puzzle:")
    print("1. A* Search")
    print("2. Hill Climbing")
    choice = int(input("Enter your choice (1 or 2): "))

    k = int(input("Enter grid size (e.g., 3 for 3x3): "))
    print("Enter the initial state row by row:")
    start_state = [int(input()) for _ in range(k * k)]

    # Define the goal state
    goal_state = list(range(k * k))

    if choice == 1:
        print("\nSolving with A* Search...")
        moves_count, moves = solve_puzzle(start_state, goal_state, k)
    elif choice == 2:
        print("\nSolving with Hill Climbing...")
        moves_count, moves = hill_climbing(start_state, goal_state, k)
    else:
        print("Invalid choice!")
        return

    # Output the result
    print(f"\nSolved in {moves_count} moves:")
    for move in moves:
        print(move)

    # Display the solved grid
    solved_grid = to_grid(goal_state, k)
    print("\nSolved Grid:")
    for row in solved_grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
