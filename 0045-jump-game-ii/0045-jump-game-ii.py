class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [float('inf')] * length
        dp[0] = 0
        
        for idx in range(length - 1):
            v = nums[idx]
            for ch_idx in range(idx + 1, idx + v + 1):
                if ch_idx == length:
                    break
                dp[ch_idx] = min(dp[idx] + 1, dp[ch_idx])
        return dp[length - 1]