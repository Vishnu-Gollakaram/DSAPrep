from collections import deque
from heapq import heappush, heappop
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        q = deque()
        safeness = [[float('inf')] * c for _ in range(r)]
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]

        # Step 1: Multi-source BFS to calculate safeness factors
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:  # Thief cells
                    q.append((0, i, j))
                    safeness[i][j] = 0

        while q:
            s, x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and safeness[nx][ny] > s + 1:
                    safeness[nx][ny] = s + 1
                    q.append((s + 1, nx, ny))

        # Step 2: Max-heap for finding the safest path
        pq = [(-safeness[0][0], 0, 0)]  # (negative safeness, x, y)
        visited = [[False] * c for _ in range(r)]

        while pq:
            s, x, y = heappop(pq)
            s = -s  # Negate back to get the actual safeness factor

            if (x, y) == (r - 1, c - 1):  # Reached the destination
                return s

            if visited[x][y]:
                continue
            visited[x][y] = True

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    min_safeness = min(s, safeness[nx][ny])
                    heappush(pq, (-min_safeness, nx, ny))

        return 0
