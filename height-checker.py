class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        indices = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                indices += 1

        return indices
