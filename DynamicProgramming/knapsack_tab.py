class Solution:
    
    #Function to return max value that can be put in knapsack of capacity cap.
    def knapSack(self, cap, wt, val):
        
        n = len(wt)
        dp = [[-1 for j in range(cap + 1)] for i in range(n + 1)]
        
        # Helper Function
        def kanp(n, cap):

            # Base Case (if no value in wt arr untraversed or 
            # remaining capacity is 0 we cannot pick any item)
            for ind in range(n + 1):
                dp[ind][0] = 0
                
            for ind in range(cap + 1):
                dp[0][ind] = 0
                
            for i in range(1, n + 1):
                for j in range(1, cap + 1):
                    
                    # If weight if item is greater than capacity, we cannot pick it
                    if wt[i - 1] > j:
                        dp[i][j] = dp[i - 1][j]
                
                    # We have a choice whether to pick or skip an item
                    else:
                        dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - wt[i - 1]])
                
            return dp[n][cap]
            
        return kanp(n, cap)