# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.x = None
        self.y = None
        self.pre = None
        self.recover(root)
        self.x.val, self.y.val = self.y.val, self.x.val

    def recover(self, node: TreeNode) -> None:
        if node is None:
            return

        self.recover(node.left)
        if self.pre is not None and self.pre.val > node.val:
            self.y = node
            if self.x is None:
                self.x = self.pre

        self.pre = node
        self.recover(node.right)
