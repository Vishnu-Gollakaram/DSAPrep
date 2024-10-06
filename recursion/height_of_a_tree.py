def height(node):
    if not node: return 0
    return 1 + max(height(node.left), height(node.right))