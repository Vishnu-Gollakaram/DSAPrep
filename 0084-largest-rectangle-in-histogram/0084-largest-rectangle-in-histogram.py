from collections import deque

def pse(arr):
    n = len(arr)
    ans = [-1] * n  # Initialize with -1
    st = []  # Stack to store indices

    for i in range(n):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        if st:
            ans[i] = st[-1]
        st.append(i)

    return ans

def nse(arr):
    n = len(arr)
    ans = [n] * n  # Initialize with n (out of bounds)
    st = []  # Stack to store indices

    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        if st:
            ans[i] = st[-1]
        st.append(i)

    return ans

def mar(arr):
    p = pse(arr)  # Previous smaller element indices
    n = nse(arr)  # Next smaller element indices
    ans = 0

    for i in range(len(arr)):
        # Width = (n[i] - p[i] - 1)
        ans = max(ans, (n[i] - p[i] - 1) * arr[i])
    return ans

class Solution:
    def largestRectangleArea(self, heights):
        return mar(heights)
