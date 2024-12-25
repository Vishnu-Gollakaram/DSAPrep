from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        n = len(board)
        m = len(board[0])
        vis = [[False for _ in range(m)] for _ in range(n)]
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        
        def dfs(r, c):
            vis[r][c] = True
            for x in range(4):
                row = r + dx[x]
                col = c + dy[x]
                if 0 <= row < n and 0 <= col < m and not vis[row][col] and board[row][col] == 'O':
                    dfs(row, col)
        
        # Check all 'O's on the boundaries (top, bottom, left, right)
        for col in range(m):
            if board[0][col] == 'O' and not vis[0][col]:
                dfs(0, col)
            if board[n - 1][col] == 'O' and not vis[n - 1][col]:
                dfs(n - 1, col)
        
        for row in range(n):
            if board[row][0] == 'O' and not vis[row][0]:
                dfs(row, 0)
            if board[row][m - 1] == 'O' and not vis[row][m - 1]:
                dfs(row, m - 1)
        
        # Flip all unvisited 'O's to 'X'
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O' and not vis[row][col]:
                    board[row][col] = 'X'