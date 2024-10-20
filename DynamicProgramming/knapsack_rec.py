class Solution:
    
    #Function to return max value that can be put in knapsack of capacity cap.
    def knapSack(self, cap, wt, val):
        
        n = len(wt)
        
        # Helper Function
        def kanp(n, cap):
            # Base Case (if no value in wt arr untraversed or 
            # remaining capacity is 0 we cannot pick any item)
            if n == 0 or cap == 0:
                return 0
                
            # If weight if item is greater than capacity, we cannot pick it
            if wt[n - 1] > cap:
                return kanp(n - 1, cap)
                
            # We have a choice whether to pick or skip an item
            return max(kanp(n - 1, cap), val[n - 1] + kanp(n - 1, cap - wt[n - 1]))
            
        return kanp(n, cap)