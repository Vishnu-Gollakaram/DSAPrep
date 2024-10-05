class Solution:
    def getProduct(self, nums):
        prod = 1
        for i in nums:
            if i != 0:
                prod *= i
        return prod
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if nums.count(0) > 1:
            return [0] * n
        elif nums.count(0) == 1:
            prod = self.getProduct(nums)
            return [prod if i==0 else 0 for i in nums]
        else:
            prod = self.getProduct(nums)
            return [prod // i for i in nums]