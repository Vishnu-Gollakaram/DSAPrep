# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (valid(node.left, left, node.val) # left boundary stays the same
            and valid(node.right, node.val, right) ) # right boundary stays the same

        return valid(root, float('-inf'), float('inf'))