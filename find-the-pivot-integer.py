class Solution:
    def pivotInteger(self, n: int) -> int:
        pre = []
        s = 0
        for i in range(1, n + 1):
            s += i
            pre.append(s)
        
        suf = []
        s = 0
        for i in range(n, 0, -1):
            s += i
            suf.append(s)

        for i in range(n):
            if pre[i] == suf[n - i - 1]:
                return i + 1

        return -1
