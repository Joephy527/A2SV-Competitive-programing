class NumberContainers:

    def __init__(self):
        self.num_map = defaultdict(list)
        self.idx_map = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        self.idx_map[index] = number
        heappush(self.num_map[number], index)

    def find(self, number: int) -> int:
        while self.num_map[number]:
            idx = self.num_map[number][0]
            
            if self.idx_map[idx] == number:
                return idx

            heappop(self.num_map[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
