class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        total = sum(nums)

        cum_sum = 0
        for num in nums[:-1]:
            cum_sum += num

            if cum_sum >= total - cum_sum:
                ans += 1

        return ans