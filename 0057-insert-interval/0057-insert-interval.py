class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        left = 0
        right = n - 1
        target = newInterval[0]

        while left <= right:
            mid = (left + right) // 2
            if target > intervals[mid][0]:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)
        ans = [intervals[0]]
        for st, ed in intervals[1:]:
            if ans[-1][1] < st:
                ans.append([st, ed])
            else:
                ans[-1][1] = max(ans[-1][1], ed)

        return ans