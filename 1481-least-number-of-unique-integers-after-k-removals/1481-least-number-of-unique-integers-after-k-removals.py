class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        countArr = []
        for i in d.keys():
            countArr.append([d[i],i])
        countArr.sort(key = lambda x:(x[0], x[1]), reverse = True)
        for rep in range(k):
            countArr[-1][0] -= 1
            if countArr[-1][0] == 0:
                del countArr[-1]
        return len(countArr)