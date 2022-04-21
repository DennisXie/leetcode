class Solution:

    def numTree(self, n: int) -> int:
        self.num = [0] * (n+1)
        self.num[0] = 1
        self.num[1] = 1
        return self.bstNum(n)

    def bstNum(self, n: int) -> int:
        if self.num[n] > 0:
            return self.num[n]

        for i in range(1, n+1):
            left = self.bstNum(i - 1)
            right = self.bstNum(n - i)
            self.num[n] = left * right + self.num[n]
        return self.num[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numTree(1), s.numTree(2), s.numTree(3), s.numTree(4), s.numTree(5), s.numTree(8))
