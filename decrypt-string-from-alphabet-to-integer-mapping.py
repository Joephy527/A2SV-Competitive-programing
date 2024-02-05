class Solution:
    def freqAlphabets(self, s: str) -> str:
        alp = [chr(i) for i in range(97, 123)]
        chars = []
        formedStr = ""

        for c in s:
            char = c
            if c == "#":
                sec, first = chars.pop(), chars.pop()
                char = first + sec

            chars.append(char)

        for char in chars:
            formedStr += alp[int(char) - 1]

        return formedStr
