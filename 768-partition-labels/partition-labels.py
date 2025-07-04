class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = {}
        last_seen = p = 0
        partitions = []

        for i, c in enumerate(s):
            idx_map[c] = i

        for seek in range(len(s)):
            last_seen = max(last_seen, idx_map[s[seek]])
            
            if seek == last_seen:
                partitions.append(seek - p + 1)
                p = seek + 1

        return partitions