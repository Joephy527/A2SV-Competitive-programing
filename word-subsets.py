class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = [0] * 26
        universal = []

        def get_word_count(word):
            cnt = [0] * 26

            for c in word:
                cnt[ord(c) - ord("a")] += 1

            return cnt

        def is_word_universal(word_count):
            for i in range(26):
                if count[i] > word_count[i]:
                    return

            return True

        for word in words2:
            cnt = get_word_count(word)

            for i in range(26):
                count[i] = max(count[i], cnt[i])

        for word in words1:
            cnt = get_word_count(word)

            if is_word_universal(cnt):
                universal.append(word)

        return universal
