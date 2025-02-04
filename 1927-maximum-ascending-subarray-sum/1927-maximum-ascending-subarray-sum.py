class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total_length = len(nums)
        maxSum = nums[0]
        current_pattern = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_pattern += nums[i]
            else:
                current_pattern = nums[i]
            maxSum = max(maxSum,current_pattern)
        return maxSum