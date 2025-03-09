class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        alt = 1
        groups = 0

        for i in range(1, len(colors) + k - 1):
            idx = i % len(colors)

            if colors[idx] != colors[idx - 1]:
                alt += 1
            else:
                alt = 1

            if alt >= k:
                groups += 1

        return groups
