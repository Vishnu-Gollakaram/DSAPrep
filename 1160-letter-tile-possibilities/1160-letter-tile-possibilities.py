from collections import Counter

def numTilePossibilities(tiles: str) -> int:
    def backtrack(counter):
        total = 0
        for tile in counter:
            if counter[tile] > 0:
                counter[tile] -= 1
                total += 1 + backtrack(counter)
                counter[tile] += 1  # Restore the count after recursion
        return total

    return backtrack(Counter(tiles))



class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return numTilePossibilities(tiles)