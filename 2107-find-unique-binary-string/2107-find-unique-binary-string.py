class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k = len(nums[0])
        q = deque()
        q.append('0')
        q.append('1')

        i = 1
        while i < k:
            i += 1
            prev = q
            q = deque()

            while prev:
                cur = prev.popleft()
                for b in '01':
                    q.append(cur + b)

        return list(set(q) - set(nums))[0]