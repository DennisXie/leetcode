class StockPrice:

    def __init__(self):
        self._current = None
        self._price_dict = {}
        self._price = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self._price_dict:
            self._pop(self._price_dict[timestamp])

        if self._current is None or timestamp > self._current:
            self._current = timestamp

        self._price_dict[timestamp] = price
        self._insert(price)

    def current(self) -> int:
        return self._price_dict[self._current]

    def maximum(self) -> int:
        return self._price[-1]

    def minimum(self) -> int:
        return self._price[0]

    def _insert(self, price) -> int:
        pos = self._find(price)
        self._price.insert(pos, price)
        return price

    def _find(self, price) -> int:
        left = 0
        right = len(self._price) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._price[mid] == price:
                left = mid
                break
            elif self._price[mid] < price:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def _pop(self, price) -> int:
        pos = self._find(price)
        self._price.pop(pos)

    def insert(self, price) -> int:
        return self._insert(price)

    def pop(self, price) -> int:
        return self._pop(price)

    @property
    def price(self):
        return self._price


if __name__ == "__main__":
    sp = StockPrice()
    sp.insert(5)
    print(sp.price)
    sp.insert(2)
    print(sp.price)
    sp.insert(4)
    print(sp.price)
    sp.insert(4)
    print(sp.price)
    sp.insert(4)
    print(sp.price)
    sp.pop(4)
    print(sp.price)
    sp.pop(2)
    print(sp.price)
