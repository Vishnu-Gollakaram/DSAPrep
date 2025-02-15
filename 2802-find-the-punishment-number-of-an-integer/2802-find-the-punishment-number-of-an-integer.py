import bisect

class Solution:
    def __init__(self):
        # Precomputed valid punishment numbers
        self.punishment_numbers = [0, 1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 
                                   370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 
                                   964, 990, 991, 999, 1000]
        
        # Precompute prefix sum of squares
        self.prefix_sums = [0]  # Stores cumulative sums for fast lookup
        for num in self.punishment_numbers:
            self.prefix_sums.append(self.prefix_sums[-1] + num * num)

    def punishmentNumber(self, n: int) -> int:
        # Find the largest index where the value is ≤ n using binary search
        idx = bisect.bisect_right(self.punishment_numbers, n)  # O(log m)
        
        # Return the precomputed prefix sum
        return self.prefix_sums[idx]