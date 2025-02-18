class Solution:
    def smallestNumber(self, pattern: str) -> str:
        length = len(pattern)
        num = [str(num) for num in range(1, length + 2)]

        def reverse(l, r):
            while l < r:
                num[l], num[r] = num[r], num[l]
                l += 1
                r -= 1

        idx = 0

        while idx < length:
            i = idx
            
            while  i < length and pattern[i] == "D":
                i += 1

            reverse(idx, i)

            idx = i + 1

        return "".join(num)
