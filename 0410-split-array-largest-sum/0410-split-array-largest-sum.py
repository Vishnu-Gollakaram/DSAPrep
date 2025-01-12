class Solution:
    
    # Function to find the minimum number of pages.
    def splitArray(self, arr, k):
        mini = max(arr)  # Minimum possible pages (largest single book)
        maxi = sum(arr)  # Maximum possible pages (all books assigned to one student)
        n = len(arr)
        if k > n: return -1
        
        # Helper function to check feasibility.
        def is_fes(max_pages):
            c = 1  # Start with one student
            cur_sum = 0
            for i in range(n):
                if cur_sum + arr[i] > max_pages:
                    c += 1  # Allocate to a new student
                    cur_sum = arr[i]  # Start new sum with the current book
                    if c > k:  # If students exceed k, it's not feasible
                        return False
                else:
                    cur_sum += arr[i]
            return True  # Feasible if we used <= k students
        
        res = -1
        while mini <= maxi:
            mid = (mini + maxi) // 2
            
            if is_fes(mid):  # Check if the current mid is feasible
                res = mid  # Update result
                maxi = mid - 1  # Try for a smaller maximum pages
            else:
                mini = mid + 1  # Increase the maximum pages limit
        
        return res