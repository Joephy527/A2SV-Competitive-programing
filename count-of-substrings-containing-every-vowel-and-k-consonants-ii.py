class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def at_least_k(k):
            count = defaultdict(int)
            p = sub = consonant = 0

            for s in range(len(word)):
                if word[s] in "aeiou":
                    count[word[s]] += 1
                else:
                    consonant += 1

                while consonant >= k and len(count) == 5:
                    sub += len(word) - s

                    if word[p] in "aeiou":
                        count[word[p]] -= 1
                    else:
                        consonant -= 1
                    
                    if not count[word[p]]:
                        del count[word[p]]

                    p += 1

            return sub

        return at_least_k(k) - at_least_k(k + 1)
