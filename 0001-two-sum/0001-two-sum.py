class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,2,3] 6
        storage = {}
        n = len(nums)
        for i in range(0, n, 1):
            cur_ele = nums[i] #
            minus_op = target - cur_ele # 

            if storage.get(minus_op) is None:
                storage[cur_ele] = i
            else:
                return [storage.get(minus_op), i]