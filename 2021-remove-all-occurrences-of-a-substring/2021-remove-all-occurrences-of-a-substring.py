class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        n = len(part)
        while i+n<=len(s):
            if s[i:i+n]==part:
                s = s[0:i]+s[i+n:]
                i=0                
            else:
                i+=1
        return s