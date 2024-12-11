class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Early check for sorted array
        if all(nums[i - 1] <= nums[i] for i in range(1, len(nums))):
            return True

        # Precompute the bit counts for all numbers
        bit_counts = [bin(num).count('1') for num in nums]

        # Initialize variables for tracking ranges
        cur_min = cur_max = nums[0]
        prev_min = prev_max = None
        pre_set_b = bit_counts[0]

        for ind in range(1, len(nums)):
            num = nums[ind]
            set_b = bit_counts[ind]

            if set_b == pre_set_b:
                cur_min = min(cur_min, num)
                cur_max = max(cur_max, num)
            else:
                if prev_min is not None and (prev_min > cur_min or cur_max < prev_max or prev_max > cur_min):
                    return False
                prev_min = cur_min
                prev_max = cur_max
                cur_min = cur_max = num
            
            pre_set_b = set_b

        if prev_min is not None and (prev_min > cur_min or cur_max < prev_max or prev_max > cur_min):
            return False
        return True
