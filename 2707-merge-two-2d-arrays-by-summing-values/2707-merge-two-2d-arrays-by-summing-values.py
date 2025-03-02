from collections import deque

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = deque()
        while nums1 and nums2:
            if nums1[-1][0] == nums2[-1][0]:
                ans.appendleft([nums1[-1][0], nums1[-1][1] + nums2[-1][1]])
                nums1.pop()
                nums2.pop()
            elif nums1[-1][0] > nums2[-1][0]:
                ans.appendleft(nums1.pop())
            else:
                ans.appendleft(nums2.pop())
        ans = list(ans)
        if nums1:
            ans = nums1 + ans
        if nums2:
            ans = nums2 + ans

        return ans