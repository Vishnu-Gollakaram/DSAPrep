from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for k in c:
            if c[k] & 1:
                return False
        return True