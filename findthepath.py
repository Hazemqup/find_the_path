import heapq


#I will use A* algorithm to find the shortest path in a grid with different terrain costs.
#heapq is perfect for A* algorithm priority queue and it is fast for insertion and deletion.

LAND_COST = {
    "S": 1, # Start
    "G": 1, # Goal
    ".": 1, # Normal ground
    "~": 2, # Water
    "^": 3, # Mountain
    "#": None # Wall/Obstacle
}

#adding the movement directions
DIRECTIONS = [
    (1, 0),  # Down
    (-1, 0), # Up
    (0, 1),  # Right
    (0, -1)  # Left
]

def heuristic(a, b):
    """Manhattan distance heuristic for the grid (no diagonal movement)
    a, b are row, col tuples
    """
    (r1, c1) = a
    (r2, c2) = b
    return abs(r1 - r2) + abs(c1 - c2)


def in_bounds(grid, position):
    """Check if the position is within the grid bounds"""
    rows = len(grid)
    cols = len(grid[0])
    (r, c) = position
    return 0 <= r < rows and 0 <= c < cols

def is_passable(grid, position):
    """make sure if the position is passable to go (not a wall)"""
    r, c = position
    cell = grid[r][c]
    return LAND_COST.get(cell) is not None


def get_neighbors(grid, position):
    """Get all valid neighbors for the current position"""
    neighbors = []
    for dr, dc in DIRECTIONS:
        nr, nc = position[0] + dr, position[1] + dc
        neighbor = (nr, nc)
        if in_bounds(grid, neighbor) and is_passable(grid, neighbor):
            neighbors.append(neighbor)
    return neighbors


def cost_to_enter(grid, position):
    """Get the cost to enter a cell based on its terrain type"""
    r, c = position
    cell = grid[r][c]
    cost = LAND_COST.get(cell)
    if cost is None:
        raise ValueError(f"Impassable terrain at position {position}")
    return cost


def reconstruct_path(came_from, current):
    '''Reconstructs the path from start to goal using the came_from map'''
    path =[current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def a_star_search(grid, start, goal):
    """
    A* pathfinding on the grid with diffrent terrain costs."""

    #edge case: start is goal
    if start == goal:
        return [start]
    
    open_set = []
    #heapq needs a counter to avoid comparison of nodes with same f_score
    # "counter" will act as a tie-breaker

    counter = 0

    came_from = {}

    g_score = {}
    f_score = {}

    g_score[start] = 0
    f_score[start] = heuristic(start, goal)

    heapq.heappush(open_set, (f_score[start], counter, start))

    while open_set:
        _, _, current = heapq.heappop(open_set)
        
        # If we reached the goal, reconstruct and return the path
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(grid, current):
            tentative_g = g_score[current] + cost_to_enter(grid, neighbor)

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                # Add neighbor to open set if not already present
                # We use counter to ensure the heap order is maintained correctly
                #push to the heap with updated f_score
                counter += 1
                heapq.heappush(open_set, (f_score[neighbor], counter, neighbor))
    # if we exit the loop without finding the goal
    return None  # No path found

#print the grid with path
def print_grid_with_path(grid, path):
    """print the grid to the console, marking the path with '*' characters
    starting with S and ending with G
    """
    path_set = set(path) if path is not None else set()
    for r, row in enumerate(grid):
        line = ""
        for c, cell in enumerate(row):
            if (r, c) in path_set:
                line += "*"
            else:
                line += cell
        print(line)

