class MinHeap:
    def __init__(self):
        self.hp = [0]  # Placeholder for 1-based indexing
        self.size = 0

    def insert(self, data):
        self.size += 1
        self.hp.append(data)
        self._percolate_up(self.size)

    def pop(self):
        if self.size == 0:
            raise ValueError("Heap is Empty")
        min_elem = self.hp[1]
        self.hp[1] = self.hp[self.size]
        self.hp.pop()
        self.size -= 1
        self._percolate_down(1)
        return min_elem

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.hp[i][0] < self.hp[i // 2][0]:  # Compare based on sum
                self.hp[i], self.hp[i // 2] = self.hp[i // 2], self.hp[i]
            i //= 2

    def _percolate_down(self, i):
        while i * 2 <= self.size:
            min_child = self._get_min_child(i)
            if self.hp[i][0] > self.hp[min_child][0]:  # Compare based on sum
                self.hp[i], self.hp[min_child] = self.hp[min_child], self.hp[i]
            i = min_child

    def _get_min_child(self, i):
        if i * 2 + 1 > self.size:  # Only left child exists
            return i * 2
        if self.hp[i * 2][0] < self.hp[i * 2 + 1][0]:  # Compare left and right child
            return i * 2
        return i * 2 + 1

    def is_empty(self):
        return self.size == 0

    def get_n_smallest(self, n):
        result = []
        for _ in range(min(n, self.size)):
            result.append(self.pop())
        return result


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        min_heap = MinHeap()

        # Iterate over nums1 and a limited slice of nums2
        for i, num1 in enumerate(nums1[:k]):  # Restrict to at most `k` elements from nums1
            for num2 in nums2[:k // (i + 1)]:  # Restrict nums2 to at most `k/(i+1)` elements
                pair_sum = num1 + num2
                min_heap.insert([pair_sum, num1, num2])  # Push pair with its sum

        # Extract the k smallest pairs
        smallest_pairs = min_heap.get_n_smallest(k)

        # Return only the pairs (without the sums)
        return [pair[1:] for pair in smallest_pairs]
