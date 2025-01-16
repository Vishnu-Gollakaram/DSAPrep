class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        q = []
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.pop()
            for x in range(n):
                matrix[x][j] = 0
            
            for y in range(m):
                matrix[i][y] = 0