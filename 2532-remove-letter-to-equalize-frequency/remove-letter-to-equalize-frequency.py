class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        freq = Counter(count.values())
        min_freq = min(freq)

        if (
            (
                len(freq) == 2 and
                (
                    freq[1] == 1 or freq[min_freq + 1] == 1
                )
            )or
            (
                len(freq) == 1 and
                (
                    1 in freq or 1 in freq.values()
                )
            )
        ):
            return True

        return False