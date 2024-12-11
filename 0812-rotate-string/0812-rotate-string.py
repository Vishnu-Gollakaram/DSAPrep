class Solution:
    def rotateString(self, s: str, g: str) -> bool:
        if len(s) != len(g):
            return False
        c = 0
        while c < len(g):
            if g[c] == s[0]:
                if g[:c] in s and g[c:] in s:
                    return True
            c += 1
        return False