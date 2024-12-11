from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = Counter()
        n = len(s)
        ans = 0
        left = 0

        for right in range(n):
            bucket[s[right]] += 1

            while bucket[s[right]] > 1:
                bucket[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans