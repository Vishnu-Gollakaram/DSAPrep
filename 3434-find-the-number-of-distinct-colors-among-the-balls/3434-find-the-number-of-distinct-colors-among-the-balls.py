class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_at_ind = {}
        color_count = {}
        total_balls = 0
        ans = []

        for ind, color in queries:
            if ind in ball_at_ind:
                if ball_at_ind[ind] != color:
                    cur_cl = ball_at_ind[ind]
                    if color_count[cur_cl] == 1:
                        total_balls -= 1
                        del color_count[cur_cl]
                    else:
                        color_count[cur_cl] -= 1
                    ball_at_ind[ind] = color
                    if color in color_count:
                        color_count[color] += 1
                    else:
                        color_count[color] = 1
                        total_balls += 1
            else:
                ball_at_ind[ind] = color
                if color in color_count:
                    color_count[color] += 1
                else:
                    color_count[color] = 1
                    total_balls += 1

            ans.append(total_balls)
            ball_at_ind[ind] = color

        return ans