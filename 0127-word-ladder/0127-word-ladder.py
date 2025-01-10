from collections import deque
class Solution:
	def ladderLength(self, startWord: str, targetWord: str, wordList: List[str]) -> int:
		s = set()
		for i in wordList:
			s.add(i)
		    
		q = deque()
		q.append((startWord,1))
		if startWord in s:
		    s.remove(startWord)
		k = len(startWord)
		    
		while q:
		    word, dist = q.popleft()
		    
		    if word == targetWord:
		        return dist
		    
		    for i in range(k):
		        for w in range(97, 123):
		            rep = word[:i] + chr(w) + word[i + 1:]

		            if rep in s:
		                s.remove(rep)
		                q.append((rep, dist + 1))

		return 0