class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        candidates = []
        for i in range(1, 320):
            i2 = i * i
            if i2 <= n:
                candidates.append(i2)
            else:
                break

        f = [None] * (n + 1)

        # f[i] represents who need to act when there is i stone left
        # f[i][0] = True represents Alice act
        # f[i][1] = True represents Bob act
        # We assume Alice can win, so the first state is f[0] = (False, True).
        # If Alice can wine, we can infer f[n] = (True, False)
        f[0] = (False, True)

        def dfs(i: int) -> (bool, bool):
            if i < 0:
                return False, False

            if f[i] is not None:
                return f[i][0], f[i][1]

            for k in candidates:
                fir, sec = dfs(i-k)
                if sec is True:
                    f[i] = (sec, fir)
                    break
            else:
                f[i] = (False, True)
            return f[i][0], f[i][1]

        ret = dfs(n)
        return ret[0]


if __name__ == "__main__":
    print(Solution().winnerSquareGame(8))
