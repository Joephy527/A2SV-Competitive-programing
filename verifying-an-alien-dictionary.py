class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {char: idx for idx, char in enumerate(order)}

        for i in range(len(words) - 1):
            isNotOrdered = True
            minLength = min(len(words[i]), len(words[i + 1]))
            for j in range(minLength):
                if orderMap[words[i][j]] > orderMap[words[i + 1][j]]:
                    return False
                elif orderMap[words[i][j]] < orderMap[words[i + 1][j]]:
                    isNotOrdered = False
                    break

            if isNotOrdered and len(words[i]) > len(words[i + 1]):
                return False

        return True
