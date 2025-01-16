class Solution:
    def xorAllNums(self, num1: List[int], num2: List[int]) -> int:

        l1, l2 = len(num1),len(num2)
        ans = 0
        if l1 % 2 == 1:
            for i in num2:
                ans ^= i

        if l2 % 2 == 1:
            for i in num1:
                ans ^= i

        return ans