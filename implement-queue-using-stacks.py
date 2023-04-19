class MyQueue:

    def __init__(self):
        self.one = []
        self.two = []

    def push(self, x: int) -> None:
        self.two.append(x)

    def pop(self) -> int:
        self.peek()
        return self.one.pop()

    def peek(self) -> int:
        if not self.one:
            while self.two:
                self.one.append(self.two.pop())
        return self.one[-1]

    def empty(self) -> bool:
        return not self.one and not self.two


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
