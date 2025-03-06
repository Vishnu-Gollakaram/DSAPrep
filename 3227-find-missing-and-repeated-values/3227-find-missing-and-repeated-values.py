class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        s = set([x + 1 for x in range(n ** 2)])
        dup = 1
        seen = set()
        for r in grid:
            for x in r:
                if x in seen:
                    dup = x
                else:
                    seen.add(x)
        return [dup, list(s - seen)[0]]