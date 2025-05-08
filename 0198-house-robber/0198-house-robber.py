class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def help(n):
            if n < 0:
                return 0
            if n == 0:
                return nums[n]
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = max(nums[n] + help(n - 2), help(n - 1))
            return dp[n]
        return help(n - 1)