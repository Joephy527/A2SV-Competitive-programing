class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindrome = []
        partition = []

        def backTrack(idx):
            if idx >= len(s):
                palindrome.append(partition[:])

                return

            for i in range(idx, len(s)):
                if self.isPalindrome(s, idx, i):
                    partition.append(s[idx:i + 1])
                    backTrack(i + 1)
                    partition.pop()

        backTrack(0)

        return palindrome

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
