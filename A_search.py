import heapq
import time

def heuristic(a, b):
    """Heuristic function using Manhattan Distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """A* search algorithm to find the shortest path from start to goal in a grid"""
    open_list = []  # Priority queue to store nodes to explore
    heapq.heappush(open_list, (0, start))  # Start node with priority 0
    
    came_from = {}  # Dictionary to reconstruct the path
    g_score = {start: 0}  # Cost from start to each node
    f_score = {start: heuristic(start, goal)}  # Estimated total cost to goal
    visited_nodes = []  # Track visited nodes for visualization
    
    print("🔍 Starting A* Algorithm Search...")
    print("S = Start, G = Goal, V = Visited Nodes, # = Obstacle")
    while open_list:
        _, current = heapq.heappop(open_list)  # Get node with lowest f_score
        visited_nodes.append(current)  # Mark node as visited
        
        print(f"\n➡️ Visiting Node: {current}")
        print_grid(grid, visited_nodes, path=[], delay=0.5)
        
        if current == goal:  # If goal is reached, reconstruct the path
            print("\n🎯 Goal Reached! Reconstructing Path...")
            return reconstruct_path(came_from, start, goal)
        
        # Possible moves: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Ensure neighbor is within grid bounds and not an obstacle
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                temp_g_score = g_score[current] + 1  # Cost to reach neighbor
                
                # If this path to neighbor is better, update scores
                if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current  # Track path
                    g_score[neighbor] = temp_g_score  # Update cost to reach neighbor
                    f_score[neighbor] = temp_g_score + heuristic(neighbor, goal)  # Calculate total estimated cost
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))  # Add neighbor to open list
    
    return None  # Return None if no path is found

def reconstruct_path(came_from, start, goal):
    """Function to reconstruct the shortest path from goal to start"""
    path = []
    current = goal
    while current in came_from:
        path.append(current)  # Store path nodes
        current = came_from[current]  # Move to previous node
    path.append(start)  # Add start node
    return path[::-1]  # Reverse path to get correct order from start to goal

def print_grid(grid, visited, path, delay=0):
    """Function to print the grid with visited nodes, path, and obstacles"""
    display_grid = [['.' if cell == 0 else '#' for cell in row] for row in grid]
    for (x, y) in visited:
        display_grid[x][y] = 'V'  # Mark visited nodes
    for (x, y) in path:
        if (x, y) != (0, 0) and (x, y) != (4, 4):
            display_grid[x][y] = '*'  # Mark path nodes
    display_grid[0][0] = 'S'  # Start position
    display_grid[4][4] = 'G'  # Goal position
    
    print("\n🗺️ Grid Status:")
    for row in display_grid:
        print(" ".join(row))
    time.sleep(delay)

grid = [  # Define a grid where 0 represents open space and 1 represents obstacles
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting position
goal = (4, 4)  # Goal position

path = a_star_search(grid, start, goal)  # Run A* search and print the shortest path
if path:
    print("\n✅ Final Shortest Path Found:")
    print_grid(grid, path, path)
else:
    print("❌ No path found!")