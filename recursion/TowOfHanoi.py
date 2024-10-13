class Solution:
    def __init__(self):
        self.count = 0
    def toh(self, n, fromm, to, aux):
        # Your code here
        self.toh_help(n, fromm, to, aux)
        return self.count
        
    def toh_help(self, n, fromm, to, aux):
        self.count += 1
        
        # Base Case
        if n == 1:
            print(f"move disk {n} from rod {fromm} to rod {to}")
            return
        
        # reduce input and move from source to helper
        self.toh(n - 1, fromm, aux, to)
        
        print(f"move disk {n} from rod {fromm} to rod {to}")
        
        # shift from helper to dest after base case via source as auxilary
        self.toh(n - 1, aux, to, fromm)