class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    本题其他思路，可以考虑findMax返回列表，表示染色多少个节点，然后对左右子树进行遍历求解。比起目前的解法可以减少很多次函数调用时间
    """

    def maxValue(self, root: TreeNode, k: int) -> int:
        self.k = k
        self._cache = {
            root: [0] * (k+1)
        }
        self.findMax(root, k)
        return self._cache[root][k]

    def findMax(self, node: TreeNode, leftNum: int) -> int:
        """
        :param node: the current traversed node
        :param leftNum: the leftNum of nodes can be colored
        :return:
        """
        if node is None:
            return 0

        if self._cache.get(node) is not None and self._cache[node][leftNum] > 0:
            return self._cache[node][leftNum]

        if self._cache.get(node) is None:
            self._cache[node] = [0] * (self.k+1)

        # current node do not colored
        for i in range(self.k+1):
            left = self.findMax(node.left, self.k)
            right = self.findMax(node.right, self.k)
            self._cache[node][leftNum] = max(self._cache[node][leftNum], left+right)

        # current node colored
        for i in range(leftNum):
            left = self.findMax(node.left, i)
            right = self.findMax(node.right, leftNum-i-1)
            self._cache[node][leftNum] = max(self._cache[node][leftNum], left+right+node.val)
        return self._cache[node][leftNum]
