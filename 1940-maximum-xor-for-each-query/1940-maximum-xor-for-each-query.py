class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = (2 ** maximumBit) - 1
        ans = []
        cur = 0
        for num in nums:
            cur = cur ^ num
            ans.append(cur ^ max_val)
        return ans[::-1]