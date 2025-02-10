class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        num = 0
        ans = ''
        for i in range(n - 1, -1, -1):
            if s[i] in '0123456789':
                num += 1
            else:
                if num > 0:
                    num -= 1
                else:
                    ans = s[i] + ans

        return ans