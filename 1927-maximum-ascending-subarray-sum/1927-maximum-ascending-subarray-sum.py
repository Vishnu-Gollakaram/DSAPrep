class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total_length = len(nums)
        maxSum = nums[0]
        current_pattern = nums[0]
        for i in range(1, len(nums)):
            previous_element = nums[i - 1]
            current_element = nums[i]
            if current_element > previous_element:
                current_pattern += current_element
            else:
                current_pattern = current_element
            maxSum = max(maxSum,current_pattern)
        return maxSum