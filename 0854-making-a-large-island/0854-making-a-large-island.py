from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        island_sizes = {}  # Stores size of each island
        island_id = 2  # Start island IDs from 2 (to differentiate from 0s and 1s)
        
        # BFS to mark islands and calculate their sizes
        def bfs(x, y, island_id):
            q = deque([(x, y)])
            grid[x][y] = island_id
            size = 0
            while q:
                r, c = q.popleft()
                size += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = island_id
                        q.append((nr, nc))
            return size
        
        # Step 1: Label all islands and store their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = bfs(i, j, island_id)
                    island_id += 1
        
        # Step 2: Find the largest island we can form by flipping a zero
        max_island = max(island_sizes.values(), default=0)  # If grid has only 0s
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:  # Consider flipping this 0 to a 1
                    unique_islands = set()
                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            unique_islands.add(grid[ni][nj])
                    
                    # Compute the merged island size
                    new_size = 1 + sum(island_sizes[iid] for iid in unique_islands)
                    max_island = max(max_island, new_size)
        
        return max_island if max_island else n * n  # Edge case: All 1s
