# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        def iot(root):
            if not root:
                return
            iot(root.left)
            order.append(root.val)
            iot(root.right)
        iot(root)
        return order[k - 1]
