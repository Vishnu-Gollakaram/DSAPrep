class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = {}
        n = len(nums)
        ans = -1
        for i in range(n):
            num = nums[i]
            sod = sum([int(k) for k in str(num)])

            if sod not in digits:
                digits[sod] = [num]
            else:
                vals = digits[sod]
                if len(vals) == 1:
                    if vals[-1] > num:
                        vals = [num] + vals
                    else:
                        vals.append(num)
                else:
                    if num >= vals[-1]:
                        vals[0] = vals[-1]
                        vals[-1] = num
                    elif num > vals[0]:
                        vals[0] = num
                ans = max(ans, sum(vals))
                digits[sod] = vals

        return ans