class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.deque = [value] + self.deque
            return True

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque.append(value)
            return True

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque.pop(0)
            return True

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque.pop()
            return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
