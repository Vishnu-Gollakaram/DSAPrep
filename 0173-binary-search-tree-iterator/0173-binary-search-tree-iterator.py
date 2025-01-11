# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order = [-1]
        def iot(root):
            if not root:
                return
            iot(root.left)
            self.order.append(root.val)
            iot(root.right)
        iot(root)
        self.size = len(self.order)
        self.ptr = 0

    def next(self) -> int:
        self.ptr += 1
        return self.order[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr < self.size - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()