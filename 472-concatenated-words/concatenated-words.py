class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        concatenated = []

        def dfs(idx, word):
            if idx == len(word):
                return True

            if visited[idx]:
                return

            visited[idx] = True

            for i in range(idx, len(word)):
                if (
                    word[idx:i + 1] in words_set and
                    dfs(i + 1, word)
                ):
                    return True

        for word in words:
            words_set.remove(word)
            visited = [False] * len(word)

            if dfs(0, word):
                concatenated.append(word)

            words_set.add(word)

        return concatenated