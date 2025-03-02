class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        while nums1 and nums2:
            if nums1[0][0] == nums2[0][0]:
                ans.append([nums1[0][0], nums1[0][1] + nums2[0][1]])
                nums1.pop(0)
                nums2.pop(0)
            elif nums1[0][0] < nums2[0][0]:
                ans.append(nums1.pop(0))
            else:
                ans.append(nums2.pop(0))
        if nums1:
            ans += nums1
        if nums2:
            ans += nums2

        return ans