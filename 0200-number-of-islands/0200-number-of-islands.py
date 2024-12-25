from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cc = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] != '0':
                    cc += 1

                    q = deque()
                    q.append((i, j))
                    grid[i][j] = '0'

                    while q:
                        cur = q.popleft()
                        if cur[0] != 0 and grid[cur[0] - 1][cur[1]] == '1':
                            grid[cur[0] - 1][cur[1]] = '0'
                            q.append((cur[0] - 1, cur[1]))

                        if cur[0] != n - 1 and grid[cur[0] + 1][cur[1]] == '1':
                            grid[cur[0] + 1][cur[1]] = '0'
                            q.append((cur[0] + 1, cur[1]))

                        if cur[1] != 0 and grid[cur[0]][cur[1] - 1] == '1':
                            grid[cur[0]][cur[1] - 1] = '0'
                            q.append((cur[0], cur[1] - 1))

                        if cur[1] != m - 1 and grid[cur[0]][cur[1] + 1] == '1':
                            grid[cur[0]][cur[1] + 1] = '0'
                            q.append((cur[0], cur[1] + 1))

        return cc