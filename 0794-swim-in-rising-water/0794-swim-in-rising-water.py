class Solution:
    def swimInWater(self, heights: List[List[int]]) -> int:
        rows, columns = len(heights), len(heights[0])
        distances = [[float('inf')] * columns for _ in range(rows)]
        src_x, src_y, dest_x, dest_y = 0, 0, rows - 1, columns - 1
        distances[src_x][src_y] = 0
        q = [(heights[0][0], src_x, src_y)]  # (current effort, x, y)
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        
        while q:
            effort, x, y = heappop(q)
            
            if (x, y) == (dest_x, dest_y):
                return effort
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0 <= nx < rows and 0 <= ny < columns:
                    new_effort = abs(heights[nx][ny])
                    max_effort = max(effort, new_effort)
                    if distances[nx][ny] > max_effort:
                        distances[nx][ny] = max_effort
                        heappush(q, (max_effort, nx, ny))
        
        return -1