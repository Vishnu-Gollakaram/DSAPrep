class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        tot = 0
        n, m = len(grid), len(grid[0])
        cur = [0] * m

        for i in range(m):
            tot += grid[0][i]
            cur[i] = tot

        for i in range(1, n):
            for j in range(m):
                if j > 0:
                    cur[j] = grid[i][j] + min(cur[j], cur[j - 1])
                else:
                    cur[j] += grid[i][j]
        return cur[m - 1]
