class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countZero = 0
        prod = 1
        ans = []
        n = len(nums)
        zero_ind = -1

        for i in range(n):
            val = nums[i]
            if val == 0:
                countZero += 1
                zero_ind = i
            else:
                prod *= val

        if countZero > 1:
            ans = [0] * n

        elif countZero == 0:
            for i in nums:
                ans.append(prod // i)

        else:
            ans = [0] * n
            ans[zero_ind] = prod

        return ans