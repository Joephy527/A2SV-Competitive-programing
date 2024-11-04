class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        comp = []
        p = 0

        while p < n:
            cur = word[p]
            count = 0

            while (
                p < n and
                cur == word[p] and
                count < 9
            ):
                count += 1
                p += 1

            comp.append(f"{count}{cur}")

        return "".join(comp)
