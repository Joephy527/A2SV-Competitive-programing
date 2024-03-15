class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s: return 0

        maxInt = (2 ** 31) - 1
        minInt = (-2 ** 31)

        sign = -1 if s[0] == "-" else 1
        i = 1 if s[0] == "-" or s[0] == "+" else 0
        integer = 0

        while i < len(s) and s[i].isdigit():
            integer = (integer * 10) + int(s[i])
            i += 1

        integer *= sign

        if minInt < integer < maxInt:
            return integer
        elif minInt >= integer:
            return minInt
        else:
            return maxInt
