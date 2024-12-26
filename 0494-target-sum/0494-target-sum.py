class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}  # Use a dictionary to store calculated results

        def rec(i, su):
            if i == n:
                if su == target:
                    return 1
                return 0

            if (i, su) not in memo:  # Check if the result is already calculated
                memo[(i, su)] = rec(i + 1, su + nums[i]) + rec(i + 1, su - nums[i])
            return memo[(i, su)]

        return rec(0, 0)
            