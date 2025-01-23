class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j, prev):
            nonlocal ans
            connected = False

            for r in range(m):
                if grid[r][j]:
                    grid[r][j] = 0
                    connected = True
                    dfs(r, j, True)

            for c in range(n):
                if grid[i][c]:
                    grid[i][c] = 0
                    connected = True
                    dfs(i, c, True)

            if prev or connected:
                ans += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    dfs(i, j, False)
        
        return ans