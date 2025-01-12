import heapq

class MedianFinder:
    def __init__(self):
        # MaxHeap for the smaller half (invert values to simulate a max-heap)
        self.left = []  
        # MinHeap for the larger half
        self.right = []  

    def addNum(self, num: int) -> None:
        # Add to MaxHeap first (use negative for max-heap simulation)
        heapq.heappush(self.left, -num)

        # Ensure the largest of MaxHeap is less than or equal to the smallest of MinHeap
        if self.left and self.right and (-self.left[0] > self.right[0]):
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # Balance the size: MaxHeap can only have at most one more element than MinHeap
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # If odd, return the middle element from MaxHeap
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If even, return the average of the middle two elements
        return (-self.left[0] + self.right[0]) / 2.0

# Example usage:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())  # Output: 1.5
# obj.addNum(3)
# print(obj.findMedian())  # Output: 2.0
