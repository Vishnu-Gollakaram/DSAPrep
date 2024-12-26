class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Adjust range based on the maximum possible sum/difference
        dp = [[0] * 2001 for _ in range(n + 1)]  # Range: -1000 to 1000

        # Base case: No numbers, only possible sum is 0
        dp[0][1000] = 1  # Offset by 1000 to handle negative sums

        for i in range(1, n + 1):
            for s in range(2001):
                if s - nums[i - 1] >= 0:
                    dp[i][s] += dp[i - 1][s - nums[i - 1]]
                if s + nums[i - 1] <= 2000:
                    dp[i][s] += dp[i - 1][s + nums[i - 1]]

        return dp[n][target + 1000]

        return rec(0, 0)
            