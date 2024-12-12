class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = [0, nums[0]]
        for i in nums[1:]:
            pre_sum.append(pre_sum[-1] + i)
        pre_sum.append(pre_sum[-1])
        n = len(nums)
        print(pre_sum)
        for i in range(n):
            if pre_sum[i] == pre_sum[-1] - pre_sum[i + 1]:
                return i
        return -1
