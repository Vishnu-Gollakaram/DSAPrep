class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        for ind in range(1, len(nums)):
            if nums[ind - 1] > nums[ind]:
                break
        else:
            return True

        cur_min = nums[0]
        cur_max = nums[0]
        prev_min = None
        prev_max = None
        pre_set_b = bin(nums[0]).count('1')
        pre = nums[0]

        for ind in range(1, len(nums)):
            num = nums[ind]
            set_b = bin(num).count('1')
            if set_b == pre_set_b:
                cur_min = min(cur_min, num)
                cur_max = max(cur_max, num)
            else:
                if prev_min is not None and (prev_min > cur_min or cur_max < prev_max or prev_max > cur_min):
                    return False
                prev_min = cur_min
                prev_max = cur_max
                cur_min = num
                cur_max = num
            pre_set_b = set_b
        print(cur_min, cur_max, prev_min, prev_max)
        if prev_min is not None and (prev_min > cur_min or cur_max < prev_max or prev_max > cur_min):
            return False
        return True
