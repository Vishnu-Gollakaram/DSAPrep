class Solution:
    def jump(self, nums):
        length = len(nums)

        def jump_help(cur):
            if cur >= length - 1:
                return 0
            

            max_reach = cur + nums[cur]

            min_jumps = 1 + jump_help(cur + 1)
            for step in range(cur + 2, max_reach + 1):
                min_jumps = min(min_jumps, 1 + jump_help(step))

            return min_jumps

        op = jump_help(0)
        return op