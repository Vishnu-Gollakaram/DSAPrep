class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        prev = nums[0] % 2
        for i in range(1, n):
            cur = nums[i] % 2
            if prev == cur:
                return False
            prev = cur
        return True