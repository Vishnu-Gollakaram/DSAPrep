class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adj_matrix = [[False for _ in range(n)] for x in range(n)]
        for edge in trust:
            adj_matrix[edge[0] - 1][edge[1] - 1] = True
        for row in adj_matrix:
            if True not in row:
                col_num = adj_matrix.index(row)
                flg = True
                for row_ind in range(n):
                    if not adj_matrix[row_ind][col_num] and row_ind != col_num:
                        flg = False
                        break
                if flg:
                    return col_num + 1
        return -1