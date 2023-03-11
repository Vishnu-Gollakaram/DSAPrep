class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #iterate from n-sized array to 0 size
        #In each iteration swap the highest element to right side
        #reduce the right most index by 1
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]