class Solution:
    def maxDepth(self, s: str) -> int:
        curDepth = maxDepth = 0

        for c in s:
            if c == "(":
                curDepth += 1
                maxDepth = max(maxDepth, curDepth)
            elif c == ")":
                curDepth -= 1

        return maxDepth
