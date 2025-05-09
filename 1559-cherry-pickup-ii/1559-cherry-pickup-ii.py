class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j1, j2):
            # Out of bounds
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')

            # Last row
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]

            max_cherries = float('-inf')
            for dj1 in [-1, 0, 1]:
                for dj2 in [-1, 0, 1]:
                    next_cherries = dfs(i + 1, j1 + dj1, j2 + dj2)
                    if j1 == j2:
                        curr = grid[i][j1]
                    else:
                        curr = grid[i][j1] + grid[i][j2]
                    max_cherries = max(max_cherries, curr + next_cherries)
            return max_cherries

        return dfs(0, 0, m - 1)
