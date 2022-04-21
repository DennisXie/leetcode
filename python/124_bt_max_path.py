class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPath = None
        self.traverse(root)
        return self.maxPath

    def traverse(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        if self.maxPath is None:
            self.maxPath = left + node.val

        self.maxPath = max(self.maxPath, left+node.val, right+node.val, left+right+node.val, node.val)
        return max(left+node.val, right+node.val, node.val)
