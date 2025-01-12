class MaxHeap:
    def __init__(self):
        self.hp = [0]  # 0-index is unused
        self.size = 0

    def insert(self, data):
        self.size += 1
        self.hp.append(data)
        self._percolate_up(self.size)

    def pop(self):
        if self.size == 0:
            raise ValueError("Heap is Empty")
        max_ele = self.hp[1]
        self.hp[1] = self.hp[self.size]
        self.hp.pop()
        self.size -= 1
        self._percolate_down(1)
        return max_ele

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.hp[i] > self.hp[i // 2]:  # Max-heap comparison
                self.hp[i], self.hp[i // 2] = self.hp[i // 2], self.hp[i]
            i //= 2

    def _percolate_down(self, i):
        while i * 2 <= self.size:
            max_child = self._get_max_child(i)
            if self.hp[i] < self.hp[max_child]:
                self.hp[i], self.hp[max_child] = self.hp[max_child], self.hp[i]
            i = max_child

    def _get_max_child(self, i):
        if i * 2 + 1 > self.size:  # Only left child exists
            return i * 2
        if self.hp[i * 2] > self.hp[i * 2 + 1]:  # Compare left and right child
            return i * 2
        return i * 2 + 1

    def is_empty(self):
        return self.size == 0


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Combine capital and profits into a list of projects and sort by capital
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()  # Sort by capital in ascending order

        max_heap = MaxHeap()
        project_index = 0

        for _ in range(k):
            # Add all projects that can be started with the current capital to the heap
            while project_index < n and projects[project_index][0] <= w:
                max_heap.insert(projects[project_index][1])  # Insert profit into max-heap
                project_index += 1

            # If no projects are affordable, break early
            if max_heap.is_empty():
                break

            # Select the project with the maximum profit
            w += max_heap.pop()

        return w
