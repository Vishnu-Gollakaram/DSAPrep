class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        cur = [0] * m
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            cur[i] = 1

        for i in range(1, n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                elif j > 0:
                    cur[j] += cur[j - 1]
                    
        return cur[m - 1]
