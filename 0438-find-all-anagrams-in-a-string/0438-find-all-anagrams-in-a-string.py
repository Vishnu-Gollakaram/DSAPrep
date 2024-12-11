from collections import Counter

class Solution:
    def findAnagrams(self, txt: str, pat: str) -> List[int]:
        k = len(pat)
        n = len(txt)
        
        if k > n:
            return []
        
        # Frequency dictionary for the pattern
        ideal = Counter(pat)
        ref = Counter()
        
        match_count = 0  # Number of characters fully matched
        ans = []
        
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
                    ans.append(right - k + 1)
                
                # Remove the leftmost character from the window
                left_char = txt[right - k + 1]
                ref[left_char] -= 1
                
                # Adjust match count for the left_char
                if ref[left_char] == ideal[left_char]:
                    match_count += 1
                elif ref[left_char] + 1 == ideal[left_char]:  # Under-count
                    match_count -= 1
        
        return ans