from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def add_edge(graph, u, v):
    """Add an undirected edge between u and v"""
    graph[u].append(v)
    graph[v].append(u)

def dfs_recursive(graph, node, visited, depth=0):
    """Recursive DFS with depth level print"""
    if node not in visited:
        print(f"{'  ' * depth}↳ {node} (Depth: {depth})")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited, depth + 1)

def bfs(graph, start):
    """BFS with level tracking"""
    visited = set()
    queue = deque([(start, 0)])  # (node, level)

    print("BFS Traversal with Levels:")
    while queue:
        node, level = queue.popleft()
        if node not in visited:
            print(f"Level {level}: {node}")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))

def visualize_graph(graph_dict):
    """Visualizes the graph using networkx and matplotlib"""
    G = nx.Graph()
    for node in graph_dict:
        for neighbor in graph_dict[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()

# --------- Main Execution ---------

graph = {
    'A1': [], 'B2': [], 'C3': [], 'D4': [], 'E5': [], 'F6': [], 'G7': []
}

add_edge(graph, 'A1', 'B2')
add_edge(graph, 'A1', 'C3')
add_edge(graph, 'B2', 'D4')
add_edge(graph, 'B2', 'E5')
add_edge(graph, 'C3', 'F6')
add_edge(graph, 'C3', 'G7')

print("🌲 Depth First Search (DFS) with Depth Info:")
dfs_recursive(graph, 'A1', set())

print("\n🌐 Breadth First Search (BFS) with Levels:")
bfs(graph, 'A1')

# Optional: Uncomment to visualize the graph
# visualize_graph(graph)
