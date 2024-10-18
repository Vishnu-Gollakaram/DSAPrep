class Solution:
    def jump(self, nums):
        length = len(nums)
        mem = [-1] * length

        def jump_help(cur):
            if cur == length - 1:
                return 0
            
            if mem[cur] != -1:
                return mem[cur]
            max_reach = cur + nums[cur]

            mem[cur] = 1 + jump_help(cur + 1)
            for step in range(cur + 2, min(max_reach + 1, length)):
                mem[cur] = min(mem[cur], 1 + jump_help(step))

            return mem[cur]

        op = jump_help(0)
        return op