from typing import List


class Solution:

    def candy2(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1

        equal = 0
        up = 1
        down = -1

        total = 0

        windows = []
        for i in range(1, len(ratings)):
            if ratings[i] < ratings[i-1]:
                if len(windows) == 0 or windows[-1][0] != down:
                    windows.append([down, i-1, i])
                elif windows[-1][0] == down:
                    windows[-1][2] = i
            elif ratings[i] > ratings[i-1]:
                if len(windows) == 0 or windows[-1][0] != up:
                    windows.append([up, i-1, i])
                elif windows[-1][0] == up:
                    windows[-1][2] = i
            else:
                if len(windows) == 0 or windows[-1][0] != equal:
                    windows.append([equal, i-1, i])
                elif windows[-1][0] == equal:
                    windows[-1][2] = i

        for i in range(len(windows)):
            window = windows[i]
            last_window = None if i < 1 else windows[i-1]
            cur = window[2] - window[1] + 1
            if window[0] == equal:
                total = total + cur
            else:
                total = total + int(cur * (cur + 1) / 2)

            if last_window is not None:
                # deal with duplicate
                if window[0] == up:
                    total -= 1
                elif window[0] == down:
                    if last_window[0] == up:
                        last_duplicate = last_window[2] - last_window[1] + 1
                        if cur > last_duplicate:
                            total -= last_duplicate
                        else:
                            total -= cur
                    else:
                        total -= 1
                elif window[0] == equal:
                    total -= 1

        return total

    def candy(self, ratings: List[int]) -> int:
        given = 20001
        count = 0
        total = 0
        current_give = 0
        while count < len(ratings):
            current_give += 1
            marked = []
            for i in range(len(ratings)):
                if ratings[i] >= given:
                    continue
                left = ratings[i-1] >= ratings[i] if i - 1 >= 0 else True
                right = ratings[i+1] >= ratings[i] if i + 1 < len(ratings) else True
                if left and right:
                    count += 1
                    total += current_give
                    marked.append(i)
            for i in marked:
                ratings[i] = given
        return total


if __name__ == "__main__":
    r = [1, 2, 3, 3, 3, 2, 1]
    print(r)
    print(Solution().candy2(r))
    print(Solution().candy(r))

    r = [1, 2, 3, 4, 5]
    print(r)
    print(Solution().candy2(r))
    print(Solution().candy(r))

    r = [4, 1, 2, 3, 2, 1, 0, 5]
    print(r)
    print(Solution().candy2(r))
    print(Solution().candy(r))

    r = [2, 1, 0, 2]
    print(r)
    print(Solution().candy2(r))
    print(Solution().candy(r))

    r = [1, 2, 2]
    print(r)
    print(Solution().candy2(r))
    print(Solution().candy(r))
    r = [1, 3, 2, 2, 1]
    print(r)
    print(Solution().candy2(r))
    print(Solution().candy(r))
