class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[False for k in range(m)]for _ in range(n)]
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        def dfs(r, c):
            vis[r][c] = True
            for x in range(4):
                row = r + dx[x]
                col = c + dy[x]
                
                if 0 <= row < n and 0 <= col < m and not vis[row][col] and grid[row][col] == 1:
                    grid[row][col] = 0
                    dfs(row, col)
        
        for row in range(n):
            if not vis[row][0] and grid[row][0] == 1:
                grid[row][0] = 0
                dfs(row, 0)
                
            if not vis[row][m - 1] and grid[row][m - 1] == 1:
                grid[row][m - 1] = 0
                dfs(row, m - 1)
            
        for col in range(m):
            if not vis[0][col] and grid[0][col] == 1:
                grid[0][col] = 0
                dfs(0, col)
                
            if not vis[n - 1][col] and grid[n - 1][col] == 1:
                grid[n - 1][col] = 0
                dfs(n - 1, col)
                
        return sum([sum(grid[i]) for i in range(n)])