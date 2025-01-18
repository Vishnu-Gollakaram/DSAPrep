from heapq import heappop, heappush
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = {
            1: (0, 1),   # right
            2: (0, -1),  # left
            3: (1, 0),   # down
            4: (-1, 0)   # up
        }

        # Min-heap to store (cost, i, j)
        heap = [(0, 0, 0)]  # (current cost, row, column)
        costs = [[float('inf')] * n for _ in range(m)]
        costs[0][0] = 0

        while heap:
            cost, i, j = heappop(heap)

            # If we reach the bottom-right cell, return the cost
            if (i, j) == (m - 1, n - 1):
                return cost

            # If this path is not optimal, skip it
            if cost > costs[i][j]:
                continue

            # Explore all neighbors
            for direction, (di, dj) in directions.items():
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    # Calculate cost for this move
                    new_cost = cost + (1 if grid[i][j] != direction else 0)
                    if new_cost < costs[ni][nj]:
                        costs[ni][nj] = new_cost
                        heappush(heap, (new_cost, ni, nj))

        # If the loop ends, return the cost for the bottom-right cell
        return costs[m - 1][n - 1]
