from collections import Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common_pref = []
        n = len(A)
        ca = Counter()
        cb = Counter()

        for i in range(n):
            ca[A[i]] += 1
            cb[B[i]] += 1

            ans = 0
            for key in ca:
                ans += min(cb[key], ca[key])

            common_pref.append(ans)

        return common_pref