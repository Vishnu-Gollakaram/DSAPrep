#User function Template for python3

class Solution:
    def isSubsetSum (self, arr, su):
        # code here 
        mem = [False for _ in range(su + 1)]
        
        def sub_sum(n, su):
            # Base Case
            mem[0] = True
            
            for i in range(1, n + 1):
                for j in range(su, arr[i - 1] - 1, -1):
                    mem[j] = mem[j] or mem[j - arr[i - 1]]
                    
            return mem[su]
        
        return sub_sum(len(arr), su)
    
'''
Derived From tabulation
class Solution:
    def isSubsetSum (self, arr, su):
        # code here 
        dp = [[False for _ in range(su + 1)] for i in range(n + 1)]
        
        def sub_sum(n, su):
            # Base Case
            for i in range(n + 1):
                dp[i][0] = True
            for j in range(1, su + 1):
                dp[0][j] = False
            
            for i in range(1, n + 1):
                for j in range(su, arr[i - 1] - 1, -1):
                    if su - arr[i - 1] < 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                    
            return dp[n][su]
        
        return sub_sum(len(arr), su)
'''

'''
Derived From memorization
class Solution:
    def isSubsetSum (self, arr, su):
        # code here 
        dp = [[False for _ in range(su + 1)] for i in range(n + 1)]
        
        def sub_sum(n, su):
            if dp[n][su] != -1:
                return dp[n][su]
            
            # Base Case
            if su == 0:
                dp[n][su] = True
            elif n == 0:
                dp[n][su] = False
            
            elif su - arr[i - 1] < 0:
                dp[n][su] = sub_sum(n - 1, su)
            else:
                dp[n][su] = sub_sum(n - 1, su) or sub_sum(n - 1, su - arr[i - 1])
                    
            return dp[n][su]
        
        return sub_sum(len(arr), su)
'''

'''
Derived From Recursion
class Solution:
    def isSubsetSum (self, arr, su):
        def sub_sum(n, su):
            # Base Case
            if su == 0:
                return True
            if n == 0:
                return False
            
            if su - arr[i - 1] < 0:
                return sub_sum(n - 1, su)

            return sub_sum(n - 1, su) or sub_sum(n - 1, su - arr[i - 1])
        
        return sub_sum(len(arr), su)
'''