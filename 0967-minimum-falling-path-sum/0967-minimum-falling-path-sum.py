class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        prev = matrix[0]

        for i in range(1, n):
            cur = matrix[i]
            for j in range(n):
                if j == 0:
                    cur[j] += min(prev[j], prev[j + 1])
                elif j == n - 1:
                    cur[j] += min(prev[j], prev[j - 1])
                else:
                    cur[j] += min(prev[j], prev[j + 1], prev[j - 1])
            prev = cur

        return min(cur)
