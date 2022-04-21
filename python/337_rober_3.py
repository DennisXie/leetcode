class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rob(self, root: TreeNode) -> int:
        self.rob_current = dict()
        self.not_rob_current = dict()
        return self._rob(root, False)

    def _rob(self, node: TreeNode, father_robed) -> int:
        if node is None:
            return 0

        if father_robed:
            if self.not_rob_current.get(node) is not None:
                return self.not_rob_current[node]
            else:
                self.not_rob_current[node] = self._rob(node.left, False)+self._rob(node.right, False)
                return self.not_rob_current[node]
        else:
            if self.not_rob_current.get(node) is None:
                self.not_rob_current[node] = self._rob(node.left, False)+self._rob(node.right, False)
            if self.rob_current.get(node) is None:
                self.rob_current[node] = self._rob(node.left, True) + self._rob(node.right, True) + node.val
            return max(self.not_rob_current[node], self.rob_current[node])
