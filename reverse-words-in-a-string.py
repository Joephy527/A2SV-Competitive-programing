class Solution:
    def reverseWords(self, s: str) -> str:
        toReverse = s.strip().split()

        return " ".join(toReverse[::-1])
