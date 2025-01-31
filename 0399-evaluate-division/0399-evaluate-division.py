from typing import List, Dict, Set

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        
        # Build the adjacency list (graph representation)
        for i in range(len(values)):
            num, den = equations[i]
            val = values[i]
            if num not in adj:
                adj[num] = {}
            if den not in adj:
                adj[den] = {}
            
            adj[num][den] = val
            adj[den][num] = 1 / val
        
        def dfs(start: str, end: str, visited: Set[str]) -> float:
            if start not in adj or end not in adj:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor, value in adj[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return result * value
            
            return -1.0
        
        results = []
        for query in queries:
            start, end = query
            results.append(dfs(start, end, set()))
        
        return results