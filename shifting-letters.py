class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = [0] * (len(s) + 1)

        for idx, shift in enumerate(shifts):
            prefix[0] += shift
            prefix[idx + 1] -= shift

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        shifted = ""

        for i in range(len(s)):
            shifted += chr(((ord(s[i]) - ord("a") + prefix[i]) % 26) + ord("a"))

        return shifted
