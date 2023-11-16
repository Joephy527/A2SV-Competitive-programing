class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i in range(len(heights)):
            startIdx = i

            while stack and stack[-1][1] > heights[i]:
                idx, h = stack.pop()
                ans = max(ans, (i - idx) * h)
                startIdx = idx

            stack.append([startIdx, heights[i]])

        for pair in stack:
            ans = max(ans, (len(heights) - pair[0]) * pair[1])

        return ans
