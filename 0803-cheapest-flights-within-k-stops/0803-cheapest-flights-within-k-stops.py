from typing import List
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v, w in flights:
            adj_list[u].append((v, w))
        
        # Priority queue: (cost, current_node, stops)
        q = [(0, src, 0)]
        
        # Store the minimum cost for a specific stop count at each node
        costs = {}
        
        while q:
            current_cost, node, stops = heappop(q)
            
            # If destination is reached, return the cost
            if node == dst:
                return current_cost
            
            # If stops exceed limit, skip further exploration
            if stops > k:
                continue
            
            # Explore neighbors
            for neighbor, price in adj_list[node]:
                new_cost = current_cost + price
                
                # Only add to queue if the new cost is better for this stop count
                if (neighbor, stops + 1) not in costs or new_cost < costs[(neighbor, stops + 1)]:
                    costs[(neighbor, stops + 1)] = new_cost
                    heappush(q, (new_cost, neighbor, stops + 1))
        
        return -1
