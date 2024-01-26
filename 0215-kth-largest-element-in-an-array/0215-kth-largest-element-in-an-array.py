# from collections import heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ''' intuition -> sort based
        nums.sort()
        return nums[-k]
        '''
        # heap solution
        li = nums[:k]
        heapify(li)
        for i in range(k, len(nums)):
            heappushpop(li, nums[i])
        print(li)
        return li[0]