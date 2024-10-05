# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        queue = []

        def iot(t):
            if not t:
                return
            queue.append(t)
            iot(t.left)
            iot(t.right)

        iot(root)
        while queue:
            t = queue.pop(0)
            t.left = None
            t.right = queue[0] if queue else None
