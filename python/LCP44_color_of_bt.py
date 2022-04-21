class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numColor(self, root: TreeNode) -> int:
        self._dict = dict()
        self.traverse(root)
        return len(self._dict)

    def traverse(self, node: TreeNode):
        if node is None:
            return
        self._dict[node.val] = 1
        self.traverse(node.left)
        self.traverse(node.right)
