class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        diffs = 0
        pre = None
        cur = None

        for i in range(n):
            if s1[i] != s2[i]:
                diffs += 1
                pre = cur
                cur = [s1[i], s2[i]]

        if diffs == 0:
            return True
        elif diffs == 2 and pre[0] == cur[1] and pre[1] == cur[0]:
            return True
        return False