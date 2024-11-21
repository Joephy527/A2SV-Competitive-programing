class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0] * 3
        window = [0] * 3
        p = extraChars = 0

        def checkEnoughChars():
            return (
                count[0] - window[0] < k or
                count[1] - window[1] < k or
                count[2] - window[2] < k
            )

        if not k: return 0
        
        for c in s:
            count[ord(c) - ord("a")] += 1

        for i in range(3):
            if count[i] < k:
                return -1

        for seek in range(n):
            window[ord(s[seek]) - ord("a")] += 1

            while p <= seek and checkEnoughChars():
                window[ord(s[p]) - ord("a")] -= 1
                p += 1

            extraChars = max(extraChars, seek - p + 1)

        return n - extraChars
