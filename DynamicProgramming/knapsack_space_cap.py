class Solution:
    
    #Function to return max value that can be put in knapsack of capacity cap.
    def knapSack(self, cap, wt, val):
        
        n = len(wt)
        #Base Case
        mem = [0 for _ in range(cap + 1)]
        
        # Helper Function
        def kanp(n, cap):
            # Processing depends on prev day, so look up in same arr and modify
            for i in range(1, n + 1):
                # process from last to first to aavoid overriting prev day values
                for j in range(cap, wt[i - 1] - 1, -1):

                    mem[j] = max(mem[j], val[i - 1] + mem[j - wt[i - 1]])
                
            return mem[cap]
            
        return kanp(n, cap)