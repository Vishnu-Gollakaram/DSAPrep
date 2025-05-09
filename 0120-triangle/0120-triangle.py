class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cur = triangle[0]  # Initialize with the first row

        for i in range(1, n):
            prev = cur[:]  # Copy previous row before updating
            cur = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0:
                    cur[j] = prev[j] + triangle[i][j]
                elif j == i:
                    cur[j] = prev[j - 1] + triangle[i][j]
                else:
                    cur[j] = min(prev[j - 1], prev[j]) + triangle[i][j]

        return min(cur)
