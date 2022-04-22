class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_deep = 1
        node = root
        while node is not None:
            node = node.left
            max_deep += 1
        empty = self.find2(root, 1, max_deep)
        return (1 << max_deep) - 1 - empty

    def find2(self, node: TreeNode, deep: int, max_deep: int) -> (bool, int):
        if deep == max_deep:
            if node is None:
                return False, 1
            else:
                return True, 0
        else:
            stop, right_count = self.find2(node.right, deep+1, max_deep)
            if stop:
                return stop, right_count
            else:
                stop, left_count = self.find2(node.left, deep+1, max_deep)
                return stop, right_count + left_count

    def countNodes(self, root: TreeNode) -> int:
        self.max_deep = None
        if root:
            empty_count = self.find(root, 1)[1]
            return (1 << self.max_deep + 1) - 1 - empty_count
        else:
            return 0

    def find(self, node: TreeNode, deep: int) -> (bool, int):
        if self.max_deep is None:
            if node.right is None:
                self.max_deep = deep
                if node.left:
                    return True, 1
                else:
                    return False, 2
            else:
                stop, right = self.find(node.right, deep+1)
                if stop:
                    return stop, right
                stop, left = self.find(node.left, deep+1)
                return left == 0 or stop, right + left
        else:
            if deep == self.max_deep:
                if node.right:
                    return True, 0
                else:
                    if node.left:
                        return True, 1
                    else:
                        return False, 2
            else:
                right_stop, right = self.find(node.right, deep+1)
                left_stop, left = self.find(node.left, deep+1)
                return right_stop or left_stop, right + left
