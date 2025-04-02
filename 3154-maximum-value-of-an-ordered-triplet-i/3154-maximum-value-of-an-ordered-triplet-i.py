class Solution:
    def maximumTripletValue(self, nums):
        maxTriplet, maxElement, maxDiff = 0, 0, 0
        for num in nums:
            maxTriplet = max(maxTriplet, maxDiff * num)
            maxDiff = max(maxDiff, maxElement - num)
            maxElement = max(maxElement, num)
        return maxTriplet