class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_right, right_left = [0] * n, [0] * n
        left_right_max = right_left_max = trapped = 0

        for idx, h in enumerate(height):
            left_right[idx] = left_right_max
            left_right_max = max(left_right_max, h)

        for idx in range(n - 1, -1, -1):
            right_left[idx] = right_left_max
            right_left_max = max(right_left_max, height[idx])

        for idx, h in enumerate(height):
            min_height = min(left_right[idx], right_left[idx])
            trapped += max(0, min_height - h)

        print(left_right)
        print(right_left)
        return trapped