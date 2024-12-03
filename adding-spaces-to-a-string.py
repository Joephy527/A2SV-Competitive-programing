class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        spaceIdx = 0

        for idx, char in enumerate(s):
            if spaceIdx < len(spaces) and idx == spaces[spaceIdx]:
                words.append(" ")
                spaceIdx += 1

            words.append(char)

        return "".join(words)
