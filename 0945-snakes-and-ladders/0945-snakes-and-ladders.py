class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 1 -> 6 [1, target]
        #[1, 15], [1, 3], [1, 4]... [1, 7]
        #[1, 3], [1, 4]... [1, 7] [2, 16], [2, 13] [2, 18] ... [2, 22]
        # ..... [3, 35] [3, 15] [3 16] [3 13] ........
        # ........[4, 36]
        
        # Check Every value and sequence
        # unnecessay ignore
        # check if last target reached
        n = len(board)

        # Convert 2D board to 1D representation for easier traversal
        def get_board_value(pos):
            row, col = divmod(pos - 1, n)
            actual_row = n - 1 - row
            actual_col = col if row % 2 == 0 else n - 1 - col
            return board[actual_row][actual_col]

        # BFS using heap for faster access to shortest path
        distance = [float('inf')] * (n * n + 1)
        heap = [(0, 1)]  # (rolls to reach, current position)
        distance[1] = 0

        while heap:
            rolls, curr = heappop(heap)

            # If we reach the target, return the number of rolls
            if curr == n * n:
                return rolls

            # Avoid unnecessary traversal
            if rolls > distance[curr]:
                continue

            # Check all possible next moves (1 to 6)
            for dice in range(1, 7):
                next_pos = curr + dice
                if next_pos > n * n:
                    break

                # Move to the next position and account for snakes or ladders
                board_value = get_board_value(next_pos)
                destination = board_value if board_value != -1 else next_pos

                # Update distance if a shorter path is found
                if rolls + 1 < distance[destination]:
                    distance[destination] = rolls + 1
                    heappush(heap, (rolls + 1, destination))

        # If target is unreachable, return -1
        return -1
