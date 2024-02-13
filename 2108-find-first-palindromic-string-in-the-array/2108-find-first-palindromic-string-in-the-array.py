class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        for i in words:
            if i == i[::-1]:
                ans = i
                break
        return ans