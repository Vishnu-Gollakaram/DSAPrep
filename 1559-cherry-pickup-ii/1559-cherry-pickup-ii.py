class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n - 1][j1][j2] = grid[n - 1][j1]
                else:
                    dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

        for i in range(n - 2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    max_cherries = float('-inf')
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            nj1, nj2 = j1 + dj1, j2 + dj2
                            if 0 <= nj1 < m and 0 <= nj2 < m:
                                curr_val = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
                                max_cherries = max(max_cherries, curr_val + dp[i + 1][nj1][nj2])
                    dp[i][j1][j2] = max_cherries

        return dp[0][0][m - 1]
