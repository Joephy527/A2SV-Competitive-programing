class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {s[i]: i for i in range(len(s))}
        i = 0
        res = []

        while i < len(s):
            l, r = i + 1, count[s[i]]

            while l < r:
                if count[s[l]] > r:
                    r = count[s[l]]
                l += 1

            res.append(r - i + 1)
            i = r + 1

        return res
