class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        hash_map = {}
        subs = set()

        def get_word_hash(word):
            word_hash = 0

            for c in word:
                word_hash *= 29
                word_hash += ord(c) - ord("a") + 1

            return word_hash

        def find_subs(start, end, word):
            cur = 0

            for idx in range(start, end):
                cur *= 29
                cur += ord(word[idx]) - ord("a") + 1

                if (not (start == 0 and idx == end - 1) and
                    cur in hash_map):
                    subs.add(hash_map[cur])

        for word in words:
            word_hash = get_word_hash(word)
            hash_map[word_hash] = word

        for word in words:
            n = len(word)

            for i in range(n):
                find_subs(i, n, word)

        return list(subs)
