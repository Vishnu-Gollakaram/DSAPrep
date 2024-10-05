class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # In a star graph, the center will appear in both the first two edges
        # Return the common node in the first two edges
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
