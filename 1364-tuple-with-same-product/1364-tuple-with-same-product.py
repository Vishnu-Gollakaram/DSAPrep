class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_count = defaultdict(int)

        # Step 1: Compute products of all pairs and store their frequency
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        total = 0
        # Step 2: Count valid tuples based on frequency
        for count in product_count.values():
            if count >= 2:
                total += count * (count - 1) // 2  # Choose 2 pairs from count pairs
        
        return total * 8  # Each tuple (a, b, c, d) can be arranged in 8 ways