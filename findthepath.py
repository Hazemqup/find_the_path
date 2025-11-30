import heapq
"""I will use A* algorithm to find the shortest path in a grid"""
"""heapq is perfect for A* algorithm priority queue and it is fast for insertion and deletion"""

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

