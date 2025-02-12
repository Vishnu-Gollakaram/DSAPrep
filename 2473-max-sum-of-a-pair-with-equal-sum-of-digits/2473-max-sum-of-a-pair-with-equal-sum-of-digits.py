from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = {}
        ans = -1

        for num in nums:
            sod = sum(int(digit) for digit in str(num))

            if sod in digits:
                first_max, second_max = digits[sod]
                if num > first_max:
                    second_max, first_max = first_max, num
                elif num > second_max:
                    second_max = num
                digits[sod] = (first_max, second_max)
                ans = max(ans, first_max + second_max)
            else:
                digits[sod] = (num, -1)

        return ans
