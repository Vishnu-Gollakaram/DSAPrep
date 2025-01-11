# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(i, p):
            if len(p) == 0:
                return None
            root = TreeNode(p[-1])
            i_i = i.index(p[-1])
            root.left = build(i[:i_i], p[:i_i])
            root.right = build(i[i_i + 1:], p[i_i: - 1])
            return root
        return build(inorder, postorder)