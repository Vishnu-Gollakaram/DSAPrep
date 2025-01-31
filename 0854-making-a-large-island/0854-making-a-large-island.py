class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
            [[0,0,0,0,0,0,0]
            ,[0,1,1,1,1,0,0]
            ,[0,1,0,0,1,0,0]
            ,[1,0,1,0,1,0,0]
            ,[0,1,0,0,1,0,0]
            ,[0,1,0,0,1,0,0]
            ,[0,1,1,1,1,0,0]]
        '''
        q = deque()
        path = set()
        paths = {}
        cp = 0
        n = len(grid)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    path.add((i, j))
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nx = dx[k] + r
                        ny = dy[k] + c

                        if -1 < nx < n and -1 < ny < n and (nx, ny) not in path and grid[nx][ny] == 1:
                            path.add((nx, ny))
                            q.append((nx, ny))

                    if len(q) == 0:
                        d = len(path)
                        for r, c in path:
                            paths[(r,c)] = cp
                            grid[r][c] = d
                        path = set()
                        cp += 1
    
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    near = 0
                    seen = set()
                    for k in range(4):
                        nx = dx[k] + i
                        ny = dy[k] + j

                        if -1 < nx < n and -1 < ny < n:
                            if paths.get((nx, ny)) != None and paths[(nx, ny)] not in seen:
                                seen.add(paths[(nx, ny)])
                                near += grid[nx][ny]
                            
                    ans = max(ans, near + 1)

        if grid[0][0] == n ** 2:
            ans = n ** 2

        return ans