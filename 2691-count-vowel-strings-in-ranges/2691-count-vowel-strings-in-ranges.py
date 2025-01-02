class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pre_sum = []
        vow = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        for word in words:
            if word[0] in vow and word[-1] in vow:
                ans += 1
            pre_sum.append(ans)
        ans =[]
        for query in queries:
            l = query[0]
            r = query[1]

            left = 0
            if l > 0:
                left = pre_sum[l - 1]
            right = pre_sum[r]

            ans.append(right - left)
        return ans