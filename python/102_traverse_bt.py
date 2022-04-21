from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = [(root, 0)]
        i = 0
        ans = []
        while i < len(queue):
            node, deep = queue[i]
            if deep >= len(ans):
                ans.append([node.val])
            else:
                ans[deep].append(node.val)
            if node.left is not None:
                queue.append((node.left, deep+1))
            if node.right is not None:
                queue.append((node.right, deep+1))
            i += 1
        return ans
