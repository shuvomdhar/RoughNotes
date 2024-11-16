# Depth-First Search (DFS) Algorithm
# Implement DFS in Python to explore a graph and find paths or cycles.

def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    if path is None:
        path = []  # List to store the current path
    
    visited.add(start)
    path.append(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
        elif neighbor in path:
            print("Cycle detected!")
            return
    
    path.pop()  # Backtrack from the current node

def find_path_dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path.append(start)
    
    if start == goal:
        return path[:]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = find_path_dfs(graph, neighbor, goal, visited, path)
            if result:
                return result
    
    path.pop()  # Backtrack
    visited.remove(start)  # Remove node from visited for other paths
    return None

# Take user input for the graph
def build_graph():
    graph = {}
    edges = int(input("Enter the number of edges: "))
    
    for _ in range(edges):
        u, v = input("Enter edge (e.g., A B): ").split()
        
        # Add the edge to the graph (undirected graph for cycle detection)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

# Main program
graph = build_graph()
print("\nGraph:", graph)

start_node = input("\nEnter the starting node for DFS traversal: ")
dfs(graph, start_node)

goal_node = input("\nEnter the goal node for finding a path from the start node: ")
path = find_path_dfs(graph, start_node, goal_node)
if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
