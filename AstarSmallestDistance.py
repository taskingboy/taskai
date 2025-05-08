import heapq
import math

class CityGraph:
    def __init__(self):
        self.edges = {}
        self.coords = {}

    def add_edge(self, a, b, cost):
        self.edges.setdefault(a, []).append((b, cost))
        self.edges.setdefault(b, []).append((a, cost))

    def set_coord(self, city, x, y):
        self.coords[city] = (x, y)

    def heuristic(self, a, b):
        x1, y1 = self.coords[a]
        x2, y2 = self.coords[b]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def a_star(self, start, goal):
        open_list = [(self.heuristic(start, goal), 0, start, [])]
        visited = set()

        while open_list:
            f, g, current, path = heapq.heappop(open_list)

            if current in visited:
                continue

            visited.add(current)
            path = path + [current]

            if current == goal:
                return path, g

            for neighbor, cost in self.edges.get(current, []):
                if neighbor not in visited:
                    new_g = g + cost
                    heapq.heappush(open_list, (new_g + self.heuristic(neighbor, goal), new_g, neighbor, path))

        return None, float('inf')

# Example usage
g = CityGraph()
g.add_edge("A", "B", 1)
g.add_edge("B", "C", 3)
g.add_edge("A", "D", 4)
g.add_edge("D", "C", 1)

g.set_coord("A", 0, 0)
g.set_coord("B", 1, 1)
g.set_coord("C", 4, 1)
g.set_coord("D", 2, 0)

path, dist = g.a_star("A", "C")
print("Path:", path)
print("Total distance:", dist)
