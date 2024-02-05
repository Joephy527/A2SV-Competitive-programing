class Solution:
    def freqAlphabets(self, s: str) -> str:
        idx = len(s) - 1
        formedString = []

        while idx >= 0:
            c = s[idx]

            if s[idx] == "#":
                c = s[idx - 2:idx]
                idx -= 2
            
            char = chr(ord("a") + int(c) - 1)
            formedString.append(char)
            idx -= 1

        return "".join(formedString[::-1])
