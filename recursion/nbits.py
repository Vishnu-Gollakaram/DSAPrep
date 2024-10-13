#User function Template for python3
class Solution:
	def NBitBinary(self, n):
		# code here
		arr = []
		def n_bit(c, pattern, su):
		    if c == n:
		        arr.append(pattern)
		        return
		  6  
		    n_bit(c + 1, pattern + "1", su + 1)
		    
		    if su > 0:
		        n_bit(c + 1, pattern + "0", su - 1)
		        
		n_bit(0, "", 0)
		return arr