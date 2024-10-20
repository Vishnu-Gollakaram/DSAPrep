class Solution:
    
    #Function to return max value that can be put in knapsack of capacity cap.
    def knapSack(self, cap, wt, val):
        
        n = len(wt)
        dp = [[-1 for j in range(cap + 1)] for i in range(n + 1)]
        
        # Helper Function
        def kanp(n, cap):
            # If subproblem already solved, return meemorized value
            if dp[n][cap] != -1:
                return dp[n][cap]

            # Base Case (if no value in wt arr untraversed or 
            # remaining capacity is 0 we cannot pick any item)
            if n == 0 or cap == 0:
                dp[n][cap] = 0
                
            # If weight if item is greater than capacity, we cannot pick it
            elif wt[n - 1] > cap:
                dp[n][cap] = kanp(n - 1, cap)
                
            # We have a choice whether to pick or skip an item
            else:
                dp[n][cap] = max(kanp(n - 1, cap), val[n - 1] + kanp(n - 1, cap - wt[n - 1]))
                
            return dp[n][cap]
            
        return kanp(n, cap)