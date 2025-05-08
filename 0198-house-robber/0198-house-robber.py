class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [-1] * n
    #     def help(n):
    #         if n < 0:
    #             return 0
    #         if n == 0:
    #             return nums[n]
    #         if dp[n] != -1:
    #             return dp[n]
            
    #         dp[n] = max(nums[n] + help(n - 2), help(n - 1))
    #         return dp[n]
    #     return help(n - 1)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            print(222)
            a = nums[i] + dp[i - 2]
            dp[i] = max(nums[i] + dp[i - 2] if i > 1 else nums[i], dp[i - 1])
        return dp[n - 1]