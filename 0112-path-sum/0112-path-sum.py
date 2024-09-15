# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def su(root, tar, cur):
            if not root:
                return False
            cur += root.val
            if not root.left and not root.right and cur == tar:
                return True
            return su(root.left, tar, cur) or su(root.right, tar, cur)
        return su(root, targetSum, 0)