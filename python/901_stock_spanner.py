class StockSpanner:

    def __init__(self):
        self._prices = []
        self._idx = []

    def next(self, price: int) -> int:
        count = 1
        while len(self._prices) >= count and price >= self._prices[-count]:
            count = count + self._idx[-count]
        self._prices.append(price)
        self._idx.append(count)
        return self._idx[-1]

    def next2(self, price: int) -> int:
        # monotonic stack solution.
        count = 1
        while len(self._prices) > 0 and price >= self._prices[-1][0]:
            count = count + self._prices.pop()[1]
        self._prices.append((price, count))
        return count

    @property
    def idx(self):
        return self._idx

    @property
    def prices(self):
        return self._prices


if __name__ == "__main__":
    ss = StockSpanner()

    ss.next(3)
    print(ss.idx)
    print(ss.prices)
    ss.next(2)
    print(ss.idx)
    print(ss.prices)
    ss.next(2)
    print(ss.idx)
    print(ss.prices)
    ss.next(4)
    print(ss.idx)
    print(ss.prices)
    ss.next(1)
    print(ss.idx)
    print(ss.prices)
    ss.next(3)
    print(ss.idx)
    print(ss.prices)
    ss.next(5)
    print(ss.idx)
    print(ss.prices)