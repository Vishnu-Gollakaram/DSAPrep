# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findmin(root):
            while root.left:
                root = root.left
            return root.val
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            root.val = findmin(root.right)
            root.right = self.deleteNode(root.right, root.val)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
            
            