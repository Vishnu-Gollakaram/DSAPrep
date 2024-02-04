class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        lss = 1
        cs = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cs += 1
            else:
                lss = max(lss, cs)
                cs = 1
        return max(lss, cs)