from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        rep = [self.val]
        self.g(self.left, 2, rep)
        self.g(self.right, 3, rep)
        return str(rep)

    def __repr__(self):
        return self.__str__()

    def g(self, node, index, rep):
        if node is None:
            return

        if index > len(rep):
            rep.extend([None] * len(rep) * 2)
        rep[index - 1] = node.val
        self.g(node.left, index * 2, rep)
        self.g(node.right, index * 2 + 1, rep)
        return rep


class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:
        self.cache = [None] * (n + 1)
        self.cache[0] = [None]
        self._generate_cache(n)

        candidates = [i for i in range(1, n+1)]
        ans = []
        for index_node in self.cache[n]:
            ans.append(self._generate(index_node, candidates))
        return ans

    def _generate(self, cache_node: TreeNode, nums: List[int]) -> TreeNode:
        """Use the tree template to generate the real tree, ref to _generate_cache"""
        left = self._generate(cache_node.left, nums[:cache_node.val-1]) if cache_node.left else None
        right = self._generate(cache_node.right, nums[cache_node.val:]) if cache_node.right else None
        node = TreeNode(nums[cache_node.val-1], left, right)
        return node

    def _generate_cache(self, n: int):
        """
        Generate the tree template, the val-1 indicates the index of nums should be used, the nums can also be a dict.
        For example, the tree is [2, 1, 3] with the numbers of [9, 12, 15], the tree can be [12, 9, 15], the template
        can be saved in Redis, Database
        :param n: the n number
        :return: None
        """
        if self.cache[n] is not None:
            return

        ncache = list()
        for i in range(1, n+1):
            self._generate_cache(i-1)
            self._generate_cache(n-i)
            for left in self.cache[i-1]:
                for right in self.cache[n-i]:
                    node = TreeNode(i, left, right)
                    ncache.append(node)

        self.cache[n] = ncache


if __name__ == "__main__":
    s = Solution()
    n = 4
    print(s.generateTrees(n))
    print(s.cache[n])
