class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        a = Counter(arr)
        b = 0
        c = 0
        for i in sorted(a.values(), reverse=True):
            c += 1
            if b + i >= len(arr) // 2:
                return c
            b += i
