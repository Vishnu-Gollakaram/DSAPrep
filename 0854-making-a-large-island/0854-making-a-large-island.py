from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        q = deque()
        path = set()
        paths = {}
        cp = 0
        n = len(grid)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        # Step 1: Identify all islands and store their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in paths:
                    q.append((i, j))
                    path.add((i, j))

                    while q:
                        r, c = q.popleft()
                        for k in range(4):
                            nx, ny = r + dx[k], c + dy[k]

                            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path and grid[nx][ny] == 1:
                                path.add((nx, ny))
                                q.append((nx, ny))

                    # Assign the island size to all its cells
                    d = len(path)
                    for r, c in path:
                        paths[(r, c)] = cp
                        grid[r][c] = d

                    path.clear()
                    cp += 1

        # Step 2: Try flipping a 0 and compute the max island size
        ans = max(grid[i][j] for i in range(n) for j in range(n))  # Maximum existing island

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    near = 1  # Start with the flipped 1
                    seen = set()
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) in paths:
                            island_id = paths[(nx, ny)]
                            if island_id not in seen:
                                seen.add(island_id)
                                near += grid[nx][ny]

                    ans = max(ans, near)

        return ans
