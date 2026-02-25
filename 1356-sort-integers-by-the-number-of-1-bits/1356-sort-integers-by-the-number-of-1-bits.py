class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nl = []
        for i in arr:
            nl.append((i, bin(i).count('1')))
        nl.sort(key = lambda a: (a[1], a[0]))

        return [i[0] for i in nl]