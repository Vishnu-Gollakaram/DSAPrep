class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}  # Use a dictionary to store calculated results

        def rec(i, su):

            if (i, su) in memo:
                return memo[(i, su)]

            elif i == n:
                if su == target:
                    return 1
                return 0

            else:
                memo[(i, su)] = rec(i + 1, su + nums[i]) + rec(i + 1, su - nums[i])
            
            return memo[(i, su)]

        return rec(0, 0)
            