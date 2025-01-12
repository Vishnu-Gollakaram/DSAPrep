class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums2 or not nums1: return []
        heap = []
        for i, num1 in enumerate(nums1[:k]):
            for num2 in nums2[:k//(i+1)]:
                heapq.heappush(heap, [num1+num2, num1, num2])
        return [x[1:] for x in heapq.nsmallest(k, heap)]