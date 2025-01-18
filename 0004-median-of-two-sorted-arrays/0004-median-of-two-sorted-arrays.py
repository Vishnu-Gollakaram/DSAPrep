from heapq import heappush, heappop

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge nums1 and nums2
        merged = nums1 + nums2
        # Min heap and max heap
        min_heap = []  # Stores the larger half
        max_heap = []  # Stores the smaller half (inverted)

        # Add all numbers into heaps
        for num in merged:
            if not max_heap or num <= -max_heap[0]:
                heappush(max_heap, -num)  # Add to max heap
            else:
                heappush(min_heap, num)  # Add to min heap

            # Balance heaps
            if len(max_heap) > len(min_heap) + 1:
                heappush(min_heap, -heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

        # Calculate median
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        else:
            return -max_heap[0] * 1.0