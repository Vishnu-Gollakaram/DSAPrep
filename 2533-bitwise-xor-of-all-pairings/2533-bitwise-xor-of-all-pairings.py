class Solution:
    def xorAllNums(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        x1 = 0
        x2 = 0
        
        if l2 % 2 != 0:
            for i in nums1:
                x2 ^= i

        if l1 % 2 != 0:
            for i in nums2:
                x1 ^= i

        return x1 ^ x2