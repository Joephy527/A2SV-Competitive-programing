class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        words = []
        
        def is_possible(word):
            p1 = p2 = 0

            while p2 < len(word) and p1 < len(s):
                if s[p1] == word[p2]:
                    p2 += 1

                p1 += 1

            return p2 == len(word)

        for word in dictionary:
            if is_possible(word):
                words.append(word)

        words.sort(key=lambda word: (-len(word), word))

        return words[0] if words else ""