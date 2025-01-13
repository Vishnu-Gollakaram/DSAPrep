from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ans = len(c)
        for key in c:
            v = c[key]
            if v % 2 == 0:
                ans += 1
        return ans