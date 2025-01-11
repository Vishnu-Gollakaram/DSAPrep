class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n=len(s)
        if n<k: return False
        freq=[0]*26
        for c in s:
            freq[ord(c)-97]^=1
        return freq.count(1)<=k
        