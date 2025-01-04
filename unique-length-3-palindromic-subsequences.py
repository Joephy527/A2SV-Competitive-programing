class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_side, right_side = set(), Counter(s)
        palindromes = set()

        for c in s:
            right_side[c] -= 1

            for char in left_side:
                if right_side[char]:
                    palindromes.add((char, c))

            left_side.add(c)

        return len(palindromes)
