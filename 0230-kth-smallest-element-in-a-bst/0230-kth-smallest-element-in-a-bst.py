# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def iot(root):
            nonlocal k, res
            if not root:
                return
            iot(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            iot(root.right)
        iot(root)
        return res