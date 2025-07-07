class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n == 1: return s

        def find_palindrome(start, end):
            while (
                start >= 0 and
                end < n and
                s[start] == s[end]
            ):
                start -= 1
                end += 1

            return start, end

        max_left = max_right = 0

        for idx in range(n):
            max_dif = max_right - max_left

            left_one, right_one = find_palindrome(idx, idx)
            left_two, right_two = find_palindrome(idx, idx + 1)

            if right_one - left_one > max_dif:
                max_left, max_right = left_one, right_one
            
            if right_two - left_two > max_dif:
                max_left, max_right = left_two, right_two

        return s[max_left + 1:max_right]