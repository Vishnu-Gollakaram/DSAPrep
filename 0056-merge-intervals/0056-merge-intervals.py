class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0], x[1]))
        ans = [intervals[0]]
        for st, ed in intervals[1:]:
            if ans[-1][1] < st:
                ans.append([st, ed])
            else:
                ans[-1][1] = max(ans[-1][1], ed)
        return ans