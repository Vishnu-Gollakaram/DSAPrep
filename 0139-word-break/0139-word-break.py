from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Helper function to insert words into a Trie
        def insert_word(word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
        
        # Helper function to search in Trie
        def search_in_trie(start):
            node = root
            for i in range(start, len(s)):
                if s[i] not in node.children:
                    return []
                node = node.children[s[i]]
                if node.is_end_of_word:
                    yield i + 1
        
        # Build the Trie from the word dictionary
        root = TrieNode()
        for word in wordDict:
            insert_word(word)
        
        # DP initialization with a deque to reduce memory overhead
        n = len(s)
        dp = deque([0])  # Tracks indices where words can break the string
        visited = [False] * (n + 1)  # To avoid visiting the same index multiple times
        
        while dp:
            start = dp.popleft()
            
            if visited[start]:
                continue
            
            for end in search_in_trie(start):
                if end == n:
                    return True
                dp.append(end)
                
            visited[start] = True
        
        return False
