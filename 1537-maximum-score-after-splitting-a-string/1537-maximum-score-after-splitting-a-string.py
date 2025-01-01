class Solution:
    def maxScore(self, s: str) -> int:
        one_c = s.count('1')
        zero_c = s.count('0')
        ret = 0
        ans = one_c
        for i in range(len(s) - 1):
            if s[i] == '0':
                ans += 1
            else:
                ans -= 1
            ret = max(ans, ret)

        return ret