from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        cur_start = image[sr][sc]
        if cur_start == color:
            return image

        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color
        
        while q:
            row, col = q.popleft()

            # if row != 0 and col != 0 and image[row - 1][col - 1] == cur_start:
            #     image[row - 1][col - 1] = color
            #     q.append((row - 1, col - 1))

            if row != 0 and image[row - 1][col] == cur_start:
                image[row - 1][col] = color
                q.append((row - 1, col))

            # if row != 0 and col != m - 1 and image[row - 1][col + 1] == cur_start:
            #     image[row - 1][col + 1] = color
            #     q.append((row - 1, col + 1))

            if col != 0 and image[row][col - 1] == cur_start:
                image[row][col - 1] = color
                q.append((row, col - 1))

            if col != m - 1 and image[row][col + 1] == cur_start:
                image[row][col + 1] = color
                q.append((row, col + 1))

            # if row != n - 1 and col != 0 and image[row + 1][col - 1] == cur_start:
            #     image[row + 1][col - 1] = color
            #     q.append((row + 1, col - 1))

            if row != n - 1 and image[row + 1][col] == cur_start:
                image[row + 1][col] = color
                q.append((row + 1, col))

            # if row != n - 1 and col != m - 1 and image[row + 1][col + 1] == cur_start:
            #     image[row + 1][col + 1] = color
            #     q.append((row + 1, col + 1))

        return image