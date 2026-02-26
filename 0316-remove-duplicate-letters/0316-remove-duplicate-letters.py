from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = Counter(s)   # how many of each char still ahead
        in_result = set()
        stack = []

        for ch in s:
            remaining[ch] -= 1

            if ch in in_result:
                continue

            # while we can improve lexicographic order AND we can still use popped char later
            while stack and ch < stack[-1] and remaining[stack[-1]] > 0:
                removed = stack.pop()
                in_result.remove(removed)

            stack.append(ch)
            in_result.add(ch)

        return "".join(stack)