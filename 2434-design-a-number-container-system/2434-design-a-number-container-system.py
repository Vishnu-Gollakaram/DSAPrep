class NumberContainers:
    def __init__(self):
        self.id_num = defaultdict(int)
        self.num_ids = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        prev_num = self.id_num[index]
        if prev_num:
            self.num_ids[prev_num].remove(index)
        self.num_ids[number].add(index)
        self.id_num[index] = number

    def find(self, number: int) -> int:
        return self.num_ids[number][0] if self.num_ids[number] else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)