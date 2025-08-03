class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        word = ""
        
        def is_possible(word):
            idx = 0

            for c in s:
                if idx < len(word) and c == word[idx]:
                    idx += 1

            return idx == len(word)

        for w in dictionary:
            if (
                is_possible(w) and
                (
                    len(w) > len(word) or
                    (
                        len(w) == len(word) and
                        w < word
                    )
                )
            ):
                word = w

        return word