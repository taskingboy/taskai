import matplotlib.pyplot as plt
import networkx as nx
import random

def is_valid_coloring(region, color, assignment, graph):
    """Check if a color is valid for a region."""
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, graph, colors):
    """Backtracking function for map coloring."""
    if len(assignment) == len(graph):
        return assignment

    unassigned = [region for region in graph if region not in assignment][0]
    for color in colors:
        if is_valid_coloring(unassigned, color, assignment, graph):
            assignment[unassigned] = color
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[unassigned]  # backtrack
    return None

def map_coloring_min_colors(graph, color_palette):
    """Find the minimal coloring solution using increasing number of colors."""
    for k in range(1, len(color_palette) + 1):
        colors = color_palette[:k]
        solution = backtrack({}, graph, colors)
        if solution:
            return solution, k
    return None, None

def draw_colored_graph(graph, solution):
    """Draw the graph using matplotlib and networkx."""
    G = nx.Graph()

    # Add edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)  # layout for visualization
    node_colors = [solution[node] for node in G.nodes]

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=12, font_color='white')
    plt.title("Graph Coloring Solution")
    plt.show()

# ----------- User Input Section -----------
graph = {}
num_regions = int(input("Enter number of regions: "))
num_edges = int(input("Enter number of edges: "))

print("Enter edges (region1 region2):")
for _ in range(num_edges):
    region1, region2 = input().split()
    graph.setdefault(region1, []).append(region2)
    graph.setdefault(region2, []).append(region1)

# Predefined palette of colors
color_palette = [
    'red', 'green', 'blue', 'yellow', 'purple', 'orange',
    'pink', 'brown', 'cyan', 'magenta', 'gray', 'lime', 'olive'
]

solution, num_colors_used = map_coloring_min_colors(graph, color_palette)

if solution:
    print(f"\n✅ Coloring Solution Found using {num_colors_used} color(s):")
    for region, color in solution.items():
        print(f"{region} -> {color}")
    draw_colored_graph(graph, solution)
else:
    print("\n❌ No solution found.")
