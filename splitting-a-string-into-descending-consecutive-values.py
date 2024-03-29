class Solution:
    def splitString(self, s: str) -> bool:
        def backTrack(idx, prev):
            if idx >= len(s):
                return True

            for j in range(idx, len(s)):
                val = int(s[idx:j+1])

                if val + 1 == prev and backTrack(j + 1, val):
                    return True

            return False

        for i in range(len(s) - 1):
            val = int(s[:i+1])

            if backTrack(i+1, val):
                return True

        return False
