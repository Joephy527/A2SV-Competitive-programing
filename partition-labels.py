class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        
        for i, c in enumerate(s):
            lastSeen[c] = i
        
        p = curr = 0
        res = []

        for seek, c in enumerate(s):
            if lastSeen[c] > lastSeen[s[curr]]:
                curr = seek

            if lastSeen[c] == seek and c == s[curr]:
                res.append(seek - p + 1)
                p = seek + 1

        return res
