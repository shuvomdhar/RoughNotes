# A* Algorithm
# Develop a Python program to solve the shortest path problem using the A* algorithm with heuristics.

import heapq

class Graph:
    def __init__(self):
        self.edges = {}  # Stores the adjacency list of the graph
        self.h = {}      # Stores heuristic values (e.g., distances to the goal)

    def add_edge(self, u, v, cost):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, cost))
        self.edges[v].append((u, cost))

    def set_heuristic(self, node, heuristic_value):
        self.h[node] = heuristic_value

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))  # Priority queue of (f_score, node)
        came_from = {}                        # Track the optimal path
        g_score = {start: 0}                  # Start node has a g_score of 0
        f_score = {start: self.h.get(start, 0)}  # f_score = g_score + h

        while open_set:
            current_f_score, current = heapq.heappop(open_set)

            # Goal check
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            # Explore neighbors
            for neighbor, cost in self.edges.get(current, []):
                tentative_g_score = g_score[current] + cost

                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.h.get(neighbor, 0)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        # If there is no path to the goal
        return None

def create_graph():
    graph = Graph()
    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge in the format 'node1 node2 cost':")
    for _ in range(num_edges):
        u, v, cost = input().split()
        graph.add_edge(u, v, float(cost))

    num_heuristics = int(input("Enter the number of heuristic values: "))
    print("Enter heuristic values in the format 'node heuristic_value':")
    for _ in range(num_heuristics):
        node, heuristic_value = input().split()
        graph.set_heuristic(node, float(heuristic_value))

    return graph

# Initialize graph with user input
graph = create_graph()

# Get start and goal nodes
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

# Find shortest path using A* algorithm
shortest_path = graph.a_star(start, goal)

# Output the result
if shortest_path:
    print(f"Shortest path from {start} to {goal}: {' -> '.join(shortest_path)}")
else:
    print(f"No path exists from {start} to {goal}.")
