from collections import deque
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        indegree = [[0] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Calculate indegree for each cell
        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[i][j] < matrix[ni][nj]:
                        indegree[ni][nj] += 1

        # Initialize queue with cells having indegree 0
        queue = deque([(i, j) for i in range(rows) for j in range(cols) if indegree[i][j] == 0])

        # Perform BFS
        longest_path = 0
        while queue:
            longest_path += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and matrix[x][y] < matrix[nx][ny]:
                        indegree[nx][ny] -= 1
                        if indegree[nx][ny] == 0:
                            queue.append((nx, ny))

        return longest_path
