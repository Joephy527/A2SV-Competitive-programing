class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        water = 0

        prefix[0], suffix[-1] = height[0], height[-1]

        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i - 1])

        for i in range(n - 2, -1, -1):
            suffix[i] = max(height[i], suffix[i + 1])

        for i, (left, right) in enumerate(zip(prefix, suffix)):
            water += min(left, right) - height[i]

        return water