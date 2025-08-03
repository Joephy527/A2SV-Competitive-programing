class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            for idx, char in enumerate(word):
                for c in range(26):
                    cur = chr(ord("a") + c)
                    transformed = word[:idx] + cur + word[idx + 1:]

                    if transformed in words:
                        words.remove(transformed)
                        queue.append((transformed, step + 1))

        return 0