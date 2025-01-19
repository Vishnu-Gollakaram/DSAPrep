class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [[10,16],[2,8],[1,6],[7,12]]
        # [[1, 6] + [2, 8], [7, 12] + [10, 16]] step 1: sort
        # [[2, 6], [10, 12]] # step 2: Merge
        # Step 3: Ans is length
        points.sort()
        ans = [points[0]]
        for i in range(1, len(points)):
            st, ed = points[i]
            if ans[-1][1] < st:
                ans.append([st, ed])
            else:
                ans[-1][0] = max(ans[-1][0], st)
                ans[-1][1] = min(ans[-1][1], ed)

        return len(ans)