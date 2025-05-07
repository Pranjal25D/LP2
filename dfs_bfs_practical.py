from collections import deque

def add_edge(graph, u, v):
    """Function to add an edge to an undirected graph"""
    graph[u].append(v)
    graph[v].append(u)

def dfs_recursive(graph, node, visited):
    """Recursive implementation of Depth First Search (DFS)"""
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

def bfs(graph, start):
    """Iterative implementation of Breadth First Search (BFS)"""
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Example usage
graph = {
    'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []
}

# Adding edges
add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'C')
add_edge(graph, 'B', 'D')
add_edge(graph, 'B', 'E')
add_edge(graph, 'C', 'F')
add_edge(graph, 'C', 'G')

print("Depth First Search (DFS):")
dfs_recursive(graph, 'A', set())

print("\nBreadth First Search (BFS):")
bfs(graph, 'A')

