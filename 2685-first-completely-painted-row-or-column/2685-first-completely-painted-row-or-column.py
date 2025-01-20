class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [n] * m
        cols = [m] * n

        vals = {}
        for i in range(m):
            for j in range(n):
                vals[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            cur_val = arr[i]
            row, col = vals[cur_val]
            rows[row] -= 1
            cols[col] -= 1
            if rows[row] == 0 or cols[col] == 0:
                return i
        return -1