class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        min_diff = inf
        if nums[0] + nums[1] + nums[2] > target:
            return nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[n-1] + nums[n-2] < target:
                if target - (nums[i] + nums[n-1] + nums[n-2]) < min_diff:
                    min_diff = target - (nums[i] + nums[n-1] + nums[n-2])
                ans = nums[i] + nums[n-1] + nums[n-2]
                continue
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if target == sum:
                    return target
                elif sum > target:
                    if sum - target < min_diff:
                        min_diff = sum - target
                        ans = sum
                    k -= 1
                else:
                    if target - sum < min_diff:
                        min_diff = target - sum
                        ans = sum
                    j += 1
        return ans