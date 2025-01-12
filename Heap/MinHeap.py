class MinHeap:
    def __init__(self):
        self.hp = [0]
        self.size = 0

    def get_parent(self, i):
        return i // 2
    
    def left_child(self, i):
        return i * 2
    
    def right_child(self, i):
        return 2 * i + 1
    
    def get_min_child(self, i):
        return 2 * i if self.size < 2 * i + 1 or self.hp[2 * i + 1] > self.hp[2 * i] else 2 * i + 1
    
    def get_min(self):
        if self.size == 0:
            raise ValueError("Heap is Empty")
        return self.hp[1]
    
    def percolate_up(self, i):
        while i // 2 > 0:
            if self.hp[i // 2] > self.hp[i]:
                self.hp[i // 2], self.hp[i] = self.hp[i], self.hp[i // 2]
            i //= 2
    
    def percolate_down(self, i):
        while i * 2 <= self.size:
            min_child = self.get_min_child(i)
            if self.hp[min_child] < self.hp[i]:
                self.hp[i], self.hp[min_child] = self.hp[min_child], self.hp[i]
            i = min_child
    
    def insert(self, data):
        self.size += 1
        self.hp.append(data)
        self.percolate_up(self.size)

    def pop(self):
        if self.size == 0:
            raise ValueError("Heap is Empty")
        min_ele = self.hp[1]
        self.hp[1] = self.hp[self.size]
        del self.hp[self.size]
        self.size -= 1
        self.percolate_down(1)
        return min_ele
    
    def delete(self):
        self.pop()

    def heapify(self, arr, n):
        self.size = n
        self.hp = [0] + arr
        i = n // 2
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def heap_sort(self, arr, n):
        self.heapify(arr, n)
        sorted_arr = []

        while (self.size):
            sorted_arr.append(self.pop())

        return sorted_arr
