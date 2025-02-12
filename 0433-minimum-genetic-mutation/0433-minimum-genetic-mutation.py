from heapq import heappush, heappop

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        minDist_till_now = {i : float('inf') for i in bank}
        q = [[0, startGene]]

        while q:
            d, nod = heappop(q)

            if nod == endGene:
                return d
            else:
                minDist_till_now[nod] = d
            
            for i in range(8):
                for x in 'ACGT':
                    if nod[i] != x and nod[ : i] + x + nod[i + 1 : ] in minDist_till_now and d + 1 < minDist_till_now[nod[ : i] + x + nod[i + 1 : ]]:
                        heappush(q, [d + 1, nod[ : i] + x + nod[i + 1 : ]])

        return -1
