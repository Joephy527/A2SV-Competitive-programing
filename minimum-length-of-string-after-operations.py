class Solution:
    def minimumLength(self, s: str) -> int:
        return sum([1 if cnt % 2 else 2 for cnt in Counter(s).values()])
