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

