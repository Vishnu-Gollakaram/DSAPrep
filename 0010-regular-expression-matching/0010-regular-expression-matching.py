class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize dp table where dp[i][j] indicates if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        dp[0][0] = True  # Empty string matches empty pattern
        
        # Handle cases where pattern has '*' at the start
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # '*' matches zero of the previous character
        
        # Fill the dp table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]  # If characters match, carry forward the previous state
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # '*' can represent zero occurrences of the preceding character
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # '*' can represent one or more occurrences of the preceding character
        
        return dp[len(s)][len(p)]  # Return if the full string matches the full pattern
