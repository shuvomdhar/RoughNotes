# Breadth-First Search (BFS) Algorithm
# Write a Python program to find the shortest path in an unweighted graph using BFS.

from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Keep track of the paths to be checked using a queue
    queue = deque([[start]])
    visited = set()  # Keep track of visited nodes
    
    # Loop until all possible paths are checked
    while queue:
        # Get the first path in the queue
        path = queue.popleft()
        # Get the last node in the path
        node = path[-1]
        
        # Check if the path has reached the goal
        if node == goal:
            return path
        
        # Else, check all adjacent nodes, mark them as visited, and add them to the queue
        elif node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
            # Mark node as visited
            visited.add(node)
    
    # If there's no path to the goal
    return None

def create_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter each edge in the format 'node1 node2':")
    for _ in range(num_edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

# Get graph input
graph = create_graph()

# Get the start and goal nodes
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

# Find the shortest path using BFS
shortest_path = bfs_shortest_path(graph, start, goal)

# Output the result
if shortest_path:
    print(f"Shortest path from {start} to {goal}: {' -> '.join(shortest_path)}")
else:
    print(f"No path exists from {start} to {goal}.")
