class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [0, 0, 1, -1, -1, 1, 1, -1]
        dy = [1, -1, 0, 0, -1, 1, -1, 1]
        m = len(board)
        n = len(board[0])

        # Use markers for transitions:
        # 0 -> 0: remains dead
        # 1 -> 1: remains alive
        # 1 -> 0: alive to dead (mark as -1)
        # 0 -> 1: dead to alive (mark as 2)

        for i in range(m):
            for j in range(n):
                live_neigh = 0

                # Count live neighbors
                for k in range(8):
                    nx, ny = dx[k] + i, dy[k] + j
                    if 0 <= nx < m and 0 <= ny < n and abs(board[nx][ny]) == 1:
                        live_neigh += 1

                # Apply rules based on live neighbors
                if board[i][j] == 1:  # Cell is currently alive
                    if live_neigh < 2 or live_neigh > 3:
                        board[i][j] = -1  # Mark as alive to dead
                else:  # Cell is currently dead
                    if live_neigh == 3:
                        board[i][j] = 2  # Mark as dead to alive

        # Final pass to update the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:  # Alive to dead
                    board[i][j] = 0
                elif board[i][j] == 2:  # Dead to alive
                    board[i][j] = 1
