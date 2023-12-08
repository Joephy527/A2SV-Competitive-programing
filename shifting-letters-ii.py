class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        amountToShift = [0] * (len(s) + 1)
        shifted = 0
        ans = ""

        for start, end, direction in shifts:
            newDir = 1 if direction == 1 else -1
            amountToShift[start] += newDir
            amountToShift[end + 1] -= newDir

        for i in range(len(s)):
            shifted += amountToShift[i]
            amountShifted = (ord(s[i]) - ord("a") + shifted) % 26
            newChar = amountShifted + ord("a")
            ans += chr(newChar)

        return ans
