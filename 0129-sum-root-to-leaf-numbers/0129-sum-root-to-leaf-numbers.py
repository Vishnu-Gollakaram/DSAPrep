# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def extract(node, path):
            if not node:
                return 0  # Return 0 if the node is None
            
            path += str(node.val)
            
            # If it's a leaf node, return the path as an integer
            if not node.left and not node.right:
                return int(path)
            
            # Recursively calculate for left and right subtrees
            return extract(node.left, path) + extract(node.right, path)

        return extract(root, '')
