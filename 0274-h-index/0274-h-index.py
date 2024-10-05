class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # if current citation value > rem count
        # return rem citations + 1 (total value)
        citations.sort()
        l = len(citations)
        for i in range(0 , l):
            rem = l - i
            if citations[i] >= rem:
                return rem
        return 0