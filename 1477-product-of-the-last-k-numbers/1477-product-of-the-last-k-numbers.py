class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.size = 0
            self.arr = []
        else:
            if self.size == 0:
                self.arr.append(num)
            else:
                self.arr.append(self.arr[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        elif k == self.size:
            return self.arr[self.size - 1]
        else:
            return self.arr[self.size - 1] // self.arr[self.size - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)