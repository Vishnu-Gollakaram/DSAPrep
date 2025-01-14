class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        
        moves = 0
        while target > 1 and maxDoubles:
            if target & 1:
                moves += 1
                target -= 1
            else:
                target //= 2
                moves += 1
                maxDoubles -= 1

        return moves + target - 1