class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        word = ""
        
        def is_possible(word):
            p1 = p2 = 0

            while p2 < len(word) and p1 < len(s):
                if s[p1] == word[p2]:
                    p2 += 1

                p1 += 1

            return p2 == len(word)

        for w in dictionary:
            if is_possible(w):
                if (
                    len(w) > len(word) or
                    (
                        len(w) == len(word) and
                        w < word
                    )
                ):
                    word = w

        return word