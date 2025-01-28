class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def dfs(r, c):
            val = grid[r][c] # Fish in current location
            grid[r][c] = 0
            for k in range(4):
                nx = r + dx[k]
                ny = c + dy[k]

                if -1 < nx < m and -1 < ny < n and grid[nx][ny] > 0:
                    val += dfs(nx, ny) # Also grad fish from all neighbours reachable

            return val

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(dfs(i, j), ans) # Find max reachable fish cluster

        return ans