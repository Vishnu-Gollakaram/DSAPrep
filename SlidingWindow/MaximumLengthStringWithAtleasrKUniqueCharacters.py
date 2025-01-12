class Solution:

    def longestKSubstr(self, s, k):
        bucket = {}
        n = len(s)
        ans = -1
        left = 0

        for right in range(n):
            bucket[s[right]] = bucket.get(s[right], 0) + 1
            
            while len(bucket) > k and right > left:
                bucket[s[left]] -= 1
                if bucket[s[left]] == 0:
                    del bucket[s[left]]
                        
                left += 1
            
            if len(bucket) == k:
                ans = max(ans, right - left + 1)

        return ans