import heapq

"""
I will use A* algorithm to find the shortest path in a grid with different terrain costs.
heapq is perfect for A* algorithm priority queue and it is fast for insertion and deletion.
"""

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

