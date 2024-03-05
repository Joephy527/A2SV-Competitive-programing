class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        greed = size = contentChildren = 0

        while greed < len(g) and size < len(s):
            if g[greed] <= s[size]:
                greed += 1
                contentChildren += 1

            size += 1

        return contentChildren
