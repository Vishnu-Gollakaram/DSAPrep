class Solution:
    
    #Function to return max value that can be put in knapsack of capacity cap.
    def knapSack(self, cap, wt, val):
        
        n = len(wt)
        #Base Case
        prev = [0 for _ in range(cap + 1)]
        cur = [0 for _ in range(cap + 1)]
        
        # Helper Function
        def kanp(n, cap):
            # Processing depends on prev day, so look up in same arr and modify
            for i in range(1, n + 1):
                # process from last to first to aavoid overriting prev day values
                for j in range(1, cap + 1):
                    
                    # if weight is greater than capacity, we cannot pick item
                    if wt[i - 1] > j:
                        cur[j] = prev[j]
                        
                    # 2 Choices
                    else:
                        cur[j] = max(prev[j], val[i - 1] + prev[j - wt[i - 1]])
                prev = cur
                
            return cur[cap]
            
        return kanp(n, cap)