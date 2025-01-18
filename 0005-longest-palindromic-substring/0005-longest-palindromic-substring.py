class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        dp = [False] * n  # To store palindromic status for the current row
        start, max_length = 0, 1
        
        # Iterate from the end of the string to the beginning
        for i in range(n - 1, -1, -1):
            # Update DP row from right to left to avoid overwriting data
            for j in range(n - 1, i - 1, -1):
                if s[i] == s[j] and (j - i < 2 or dp[j - 1]):
                    dp[j] = True
                    # Check if the current palindrome is the longest
                    if j - i + 1 > max_length:
                        start = i
                        max_length = j - i + 1
                else:
                    dp[j] = False
        
        return s[start:start + max_length]