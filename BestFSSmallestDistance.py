import heapq
import math

class Graph:
    def __init__(self):
        self.graph = {}
        self.coordinates = {}

    def add_edge(self, city1, city2, distance):
        """Adds a bidirectional edge between two cities"""
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
        
        self.graph[city1].append((distance, city2))
        self.graph[city2].append((distance, city1))

    def set_coordinates(self, city, x, y):
        """Stores the coordinates of a city"""
        self.coordinates[city] = (x, y)

    def euclidean_heuristic(self, city, goal):
        """Computes the Euclidean distance heuristic"""
        x1, y1 = self.coordinates[city]
        x2, y2 = self.coordinates[goal]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def best_first_search(self, start, goal):
        """Finds the shortest path using Best First Search with Euclidean heuristic"""
        priority_queue = [(self.euclidean_heuristic(start, goal), 0, start, [])]  # (Heuristic, Cost, City, Path)
        visited = set()

        while priority_queue:
            heuristic, cost, city, path = heapq.heappop(priority_queue)

            if city in visited:
                continue
            path = path + [city]
            visited.add(city)

            if city == goal:
                return path, cost  # Return the shortest path and accumulated total distance

            for distance, neighbor in self.graph[city]:
                if neighbor not in visited:
                    total_cost = cost + distance
                    heapq.heappush(priority_queue, (self.euclidean_heuristic(neighbor, goal), total_cost, neighbor, path))
        
        return None, float('inf')  # If no path is found

# Take user input for the graph
g = Graph()

num_edges = int(input("Enter the number of connections between cities: "))
print("Enter the connections in the format: City1 City2 Distance")
for _ in range(num_edges):
    city1, city2, distance = input().split()
    g.add_edge(city1, city2, int(distance))

# Set coordinates for cities
num_cities = int(input("Enter the number of cities: "))
print("Enter coordinates for each city in the format: City X Y")
for _ in range(num_cities):
    city, x, y = input().split()
    g.set_coordinates(city, int(x), int(y))

start_city = input("Enter the starting city: ")
goal_city = input("Enter the goal city: ")

# Perform Best First Search
shortest_path, total_distance = g.best_first_search(start_city, goal_city)

# Output the result
if shortest_path:
    print("\nShortest Path:", " → ".join(shortest_path))
    print("Total Distance:", total_distance)
else:
    print("No path found between", start_city, "and", goal_city)
