class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)
        self.cur = self.root

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url)
        temp = self.cur
        self.cur = self.cur.next
        self.cur.prev = temp

    def back(self, steps: int) -> str:
        while self.cur and self.cur.prev and steps:
            self.cur = self.cur.prev
            steps -= 1

        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur and self.cur.next and steps:
            self.cur = self.cur.next
            steps -= 1

        return self.cur.val



class ListNode:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
