class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while (
                left > -1 and right < len(s)
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return left + 1, right

        best_start = best_end = 0

        for center in range(len(s)):
            center_pairs = (
                (center, center),
                (center, center + 1),
            )

            for left_center, right_center in center_pairs:
                start, end = expand_around_center(left_center, right_center)

                if end - start > best_end - best_start:
                    best_start, best_end = start, end

        return s[best_start:best_end]