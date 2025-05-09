class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        cur = [0] * m
        cur[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                elif j > 0:
                    cur[j] += cur[j - 1]
                    
        return cur[m - 1]
