class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        return (n:=len(nums))*(n-1)//2-sum(f*(f-1)//2 for f in Counter(x-i for i, x in enumerate(nums)).values())