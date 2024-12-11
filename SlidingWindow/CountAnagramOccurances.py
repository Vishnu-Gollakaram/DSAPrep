from collections import Counter

class Solution:
    def search(self, pat, txt):
        k = len(pat)
        n = len(txt)
        
        if k > n:
            return 0
        
        # Frequency dictionary for the pattern
        ideal = Counter(pat)
        ref = Counter()
        
        match_count = 0  # Number of characters fully matched
        ans = 0
        
        for right in range(n):
            # Add the current character to the window
            char = txt[right]
            ref[char] += 1
            
            # If this character matches the frequency in `ideal`, increment match_count
            if ref[char] == ideal[char]:
                match_count += 1
            elif ref[char] == ideal[char] + 1:  # Mismatch: overcount
                match_count -= 1
            
            # Shrink the window if it exceeds size `k`
            if right >= k - 1:
                # Check if all characters are matched
                if match_count == len(ideal):
                    ans += 1
                
                # Remove the leftmost character from the window
                left_char = txt[right - k + 1]
                ref[left_char] -= 1
                
                # Adjust match count for the left_char
                if ref[left_char] == ideal[left_char]:
                    match_count += 1
                elif ref[left_char] + 1 == ideal[left_char]:  # Under-count
                    match_count -= 1
        
        return ans


''' Using dictionary comparision at each trace

class Solution:
    def search(self,pat, txt):
        k = len(pat)
        n = len(txt)
	    
        if k > n:
            return 0
	        
        ref = {}
        ideal = {}
        
        for char in pat:
            if ideal.get(char):
                ideal[char] += 1
            else:
                ideal[char] = 1
        
        left = 0
        right = 0
        ans = 0
        
        for right in range(n):
            char = txt[right]
            
            if ref.get(char):
                ref[char] += 1

            else:
                ref[char] = 1
            
            if right >= k - 1:
                
                if ideal == ref:
                    ans += 1
                    
                left_char = txt[left]
                
                if ref[left_char] == 1:
                    del ref[left_char]
                    
                else:
                    ref[left_char] -= 1
                    
                left += 1
                right += 1
                
            else:
                right += 1
                
        return ans
    
'''