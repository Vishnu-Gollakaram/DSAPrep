class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        first_occurrence = {tuple(vowel_count.values()): -1}  # Tuple tracks the counts of each vowel
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            ch = s[end]
            
            # If the character is a vowel, toggle its count between 0 (even) and 1 (odd)
            if ch in vowel_count:
                vowel_count[ch] = 1 - vowel_count[ch]
                
            # Check the current state of vowel counts
            state = tuple(vowel_count.values())
            
            # If we've seen this state before, calculate the possible max length
            if state in first_occurrence:
                max_length = max(max_length, end - first_occurrence[state])
            else:
                # Store the first occurrence of this state
                first_occurrence[state] = end

        return max_length
