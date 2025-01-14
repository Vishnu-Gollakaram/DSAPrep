class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] = max(dp[j], dp[j] + dp[j - coins[i - 1]])
        
        return dp[amount] if dp[amount] != float('inf') else -1