class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reached = 0
        min_jumps = 0
        length = len(nums)
        
        if length <= 1:  # If only one element, no jumps needed
            return 0

        cur_end = 0  # Tracks the farthest point within the current jump

        index = 0
        while index < length - 1:
            cur = index
            max_reached = max(max_reached, nums[cur] + cur)  # Update the farthest point we can reach from 'cur'

            # Now we check if we need to make another jump
            if index == cur_end:  # If we've reached the farthest point of our current jump
                min_jumps += 1
                cur_end = max_reached  # Update the farthest point for the next jump
                
                # If we can reach the last index, break early
                if cur_end >= length - 1:
                    break

            index += 1

        return min_jumps
