class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        prefix = []
        groups = cur = 0

        for left, right in intervals:
            prefix.append((left, 1))
            prefix.append((right + 1, -1))

        prefix.sort()

        for i in range(len(prefix)):
            cur += prefix[i][1]
            groups = max(groups, cur)

        return groups
