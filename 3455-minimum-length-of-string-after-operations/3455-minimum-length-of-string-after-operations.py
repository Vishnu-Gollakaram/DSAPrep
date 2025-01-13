from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for key in c:
            v = c[key]
            if v % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans