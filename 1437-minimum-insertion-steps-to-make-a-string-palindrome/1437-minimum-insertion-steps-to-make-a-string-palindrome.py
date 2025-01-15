def longest_palindromic_subsequence(s):
    n = len(s)
    x = s
    y = s[::-1]  # Reverse of the string

    # Initialize a 1D DP array with size n+1
    dp = [0] * (n + 1)

    # Compute LCS of x and y (s and its reverse)
    for i in range(1, n + 1):
        prev = 0  # This stores dp[j-1] from the previous row
        for j in range(1, n + 1):
            temp = dp[j]  # Temporarily store current dp[j] for the next iteration
            if x[i - 1] == y[j - 1]:
                dp[j] = 1 + prev  # Characters match
            else:
                dp[j] = max(dp[j], dp[j - 1])  # Take the maximum value
            prev = temp  # Update prev for the next column
    return dp[n]

class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s) - longest_palindromic_subsequence(s)