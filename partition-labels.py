class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {c: i for i, c in enumerate(s)}
        p = anchor = 0
        res = []

        for seeker in range(len(s) + 1):
            if seeker == len(s):
                res.append(seeker - p)
                continue

            if lastSeen[s[seeker]] > lastSeen[s[anchor]]:
                if seeker > lastSeen[s[anchor]]:
                    res.append(seeker - p)
                    p = anchor = seeker
                else:
                    anchor = seeker

        return res
