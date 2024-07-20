class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {c: i for i, c in enumerate(s)}
        p = anchor = 0
        partitions = []

        for seek in range(len(s)):
            if lastSeen[s[seek]] > lastSeen[s[anchor]]:
                anchor = seek

            if lastSeen[s[anchor]] == seek:
                partitions.append(seek - p + 1)
                p = seek + 1

        return partitions
