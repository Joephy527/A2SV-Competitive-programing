class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        sumCost = ans = p = 0

        for seek in range(len(s)):
            sumCost += abs(ord(s[seek]) - ord(t[seek]))

            while sumCost > maxCost:
                sumCost -= abs(ord(s[p]) - ord(t[p]))
                p += 1

            ans = max(ans, seek - p + 1)

        return ans
