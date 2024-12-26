class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n == 1:
            return s
        
        memo = [[False] * n for _ in range(n)]
        length = 1
        longest = s[0]

        for end in range(n):
            memo[end][end] = True

            for start in range(end):
                if (s[start] == s[end] and
                    (end - start < 3 or
                    memo[start + 1][end - 1])):
                    memo[start][end] = True
                    
                    if length < end - start + 1:
                        length = end - start + 1
                        longest = s[start:end + 1]

        return longest
