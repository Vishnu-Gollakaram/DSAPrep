class Solution:
    def gridGame(self, grid):
        n = len(grid[0])
        
        # Precompute prefix and suffix sums
        top_sum = [0] * n
        bottom_sum = [0] * n
        
        # Suffix sum for the top row
        top_sum[n - 1] = grid[0][n - 1]
        for i in range(n - 2, -1, -1):
            top_sum[i] = top_sum[i + 1] + grid[0][i]
        
        # Prefix sum for the bottom row
        bottom_sum[0] = grid[1][0]
        for i in range(1, n):
            bottom_sum[i] = bottom_sum[i - 1] + grid[1][i]
        
        # Calculate the result
        result = float('inf')
        
        for i in range(n):
            # Points left in the top row (right of column i)
            points_top = top_sum[i + 1] if i + 1 < n else 0
            # Points collected in the bottom row (left of column i)
            points_bottom = bottom_sum[i - 1] if i > 0 else 0
            
            # Robot 2's maximum points for this split
            robot2_points = max(points_top, points_bottom)
            # Robot 1 tries to minimize Robot 2's points
            result = min(result, robot2_points)
        
        return result
