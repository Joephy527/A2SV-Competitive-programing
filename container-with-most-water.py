class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] <= height[r]:
                curr = (r - l) * height[l]
                ans = max(ans, curr)
                l += 1
            else:
                curr = (r - l) * height[r]
                ans = max(ans, curr)
                r -= 1

        return ans
