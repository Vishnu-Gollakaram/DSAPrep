class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_till_here = 0
        length = len(nums)
        for i in range(length):
            if(max_till_here < i):
                return False
            max_till_here = max(max_till_here, i + nums[i])
        if max_till_here >= length - 1:
            return True
        return False