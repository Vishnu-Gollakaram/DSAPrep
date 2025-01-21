class Solution:
    def gridGame(self, grid):
        n = len(grid[0])
        
        # Precompute prefix sums for the top and bottom rows
        top_sum = [0] * n
        bottom_sum = [0] * n
        
        top_sum[0] = grid[0][0]
        bottom_sum[0] = grid[1][0]
        
        for i in range(1, n):
            top_sum[i] = top_sum[i - 1] + grid[0][i]
            bottom_sum[i] = bottom_sum[i - 1] + grid[1][i]
        
        # Calculate Robot 2's max points for each Robot 1's path
        result = float('inf')
        
        for c in range(n):
            # Points remaining in the top row after column c
            points_top = top_sum[-1] - top_sum[c]
            # Points collected in the bottom row up to column c
            points_bottom = bottom_sum[c - 1] if c > 0 else 0
            
            # Robot 2's maximum points for this split
            robot2_points = max(points_top, points_bottom)
            # Robot 1 tries to minimize Robot 2's points
            result = min(result, robot2_points)
        
        return result
