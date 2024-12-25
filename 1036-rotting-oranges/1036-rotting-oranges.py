from collections import deque

class Solution:
    def orangesRotting(self, mat):
        max_time = 0
        q = deque()
        
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            row, col, time = q.popleft()
            max_time = max(time, max_time)

                    
            if row != 0 and mat[row - 1][col] == 1:
                mat[row - 1][col] = 2
                q.append((row - 1, col, time + 1))
		                
            if row != n - 1 and mat[row + 1][col] == 1:
                mat[row + 1][col] = 2
                q.append((row + 1, col, time + 1))
		                
            if col != 0 and mat[row][col - 1] == 1:
                mat[row][col - 1] = 2
                q.append((row, col - 1, time + 1))
		                
            if col != m - 1 and mat[row][col + 1] == 1:
                mat[row][col + 1] = 2
                q.append((row, col + 1, time + 1))
                
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    return -1
		                
        return max_time