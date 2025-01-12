from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        left = 0
        n = len(s)
        k = len(words)
        size = len(words[0])
        window = size * k

        if window > n:
            return []

        ans = []
        word_count = Counter(words)

        # Slide a window of size `window`
        for i in range(size):
            left = i
            cur_count = Counter()
            count = 0  # Number of valid words in the current window

            for right in range(i, n, size):
                # Extract the current word
                word = s[right:right + size]

                if word in word_count:
                    cur_count[word] += 1
                    count += 1

                    # Remove extra occurrences of the word
                    while cur_count[word] > word_count[word]:
                        left_word = s[left:left + size]
                        cur_count[left_word] -= 1
                        count -= 1
                        left += size

                    # If the window matches the desired size, add the index
                    if count == k:
                        ans.append(left)

                else:
                    # Reset if the word is not in `words`
                    cur_count.clear()
                    count = 0
                    left = right + size

        return ans
