class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_prefix(self, s: str, start: int) -> List[int]:
        """Search all valid end indices of words starting from 'start'."""
        node = self.root
        result = []
        for i in range(start, len(s)):
            if s[i] not in node.children:
                break
            node = node.children[s[i]]
            if node.is_end_of_word:
                result.append(i + 1)  # End of a word, append index after the word
        return result

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Step 1: Build the Trie
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        # Step 2: Use DFS with memoization
        memo = {}
        
        def dfs(index: int) -> bool:
            # If we reach the end of the string, return True
            if index == len(s):
                return True
            # If we have already checked from this index, return the stored result
            if index in memo:
                return memo[index]
            
            # Step 3: Search for all words in Trie starting from 'index'
            valid_ends = trie.search_prefix(s, index)
            
            # Try breaking at each valid end position
            for end in valid_ends:
                if dfs(end):
                    memo[index] = True
                    return True
            
            # If no valid break was found, mark this index as False in the memo
            memo[index] = False
            return False
        
        # Start DFS from index 0
        return dfs(0)