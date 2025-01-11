class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True

            # Check current node's value against the valid range
            if (min_val is not None and node.val <= min_val) or \
               (max_val is not None and node.val >= max_val):
                return False

            # Recursively validate left and right subtrees
            return validate(node.left, min_val, node.val) and \
                   validate(node.right, node.val, max_val)

        return validate(root, None, None)