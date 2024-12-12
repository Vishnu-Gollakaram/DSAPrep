class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        l, r, s = 1, len(A) - 2, sum(A)
        if s % 3 != 0:
            return False
        leftSum, rightSum, average = A[0], A[-1], s // 3
        while l <= r:
            if l < r and leftSum != average:
                leftSum += A[l]
                l += 1
            if l < r and rightSum != average:
                rightSum += A[r]
                r -= 1
            if leftSum == average == rightSum:
                return True    
            if l == r:
                return False
        return False