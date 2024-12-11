from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        ideal = Counter(t)
        real = Counter()
        matched = 0
        left = 0
        ans = [float('inf'), 0, -1]

        for right in range(n):
            real[s[right]] += 1
            if real[s[right]] == ideal[s[right]]:
                matched += 1

            while matched == len(ideal):
                if ans[0] > right - left + 1:
                    ans = [right - left + 1, left, right]
                
                # Remove left character and adjust counts
                real[s[left]] -= 1
                if real[s[left]] < ideal[s[left]]:
                    matched -= 1
                left += 1

        return s[ans[1] : ans[2] + 1]