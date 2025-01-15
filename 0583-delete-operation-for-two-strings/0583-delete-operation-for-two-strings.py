class Solution:
    def minDistance(self, x: str, y: str) -> int:
        n, m = len(x), len(y)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = dp[0]
            for j in range(1, m + 1):
                temp = dp[j]
                if x[i - 1] == y[j - 1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return n - dp[m] + m - dp[m]