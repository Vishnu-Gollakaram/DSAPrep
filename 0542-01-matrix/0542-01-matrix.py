from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[0 for _ in range(m)] for z in range(n)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        q = deque()

        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    q.append((row, col, 0))

        while q:
            r, c, d = q.popleft()
            for x in range(4):
                row = r + dx[x]
                col = c + dy[x]
                if 0 <= row < n and 0 <= col < m:
                    if mat[row][col] == 1:
                        mat[row][col] = 0
                        q.append((row, col, d + 1))
                        ans[row][col] = d + 1

        return ans