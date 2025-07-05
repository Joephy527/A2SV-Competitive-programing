class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        ans = 0

        while left < right:
            if height[left] <= height[right]:
                left += 1
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += right_max - height[right]

        return ans