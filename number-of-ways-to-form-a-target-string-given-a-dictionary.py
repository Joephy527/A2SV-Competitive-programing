class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        target_length, word_length = len(target), len(words[0])
        memo = [[0] * (target_length + 1) for _ in range(word_length + 1)]
        count = [[0] * 26 for _ in range(word_length)]

        for word in words:
            for idx, char in enumerate(word):
                count[idx][ord(char) - ord("a")] += 1

        for idx in range(word_length + 1):
            memo[idx][0] = 1

        for word_idx in range(1, word_length + 1):
            for target_idx in range(1, target_length + 1):
                memo[word_idx][target_idx] = memo[word_idx - 1][target_idx]
                char_idx = ord(target[target_idx - 1]) - ord("a")
                memo[word_idx][target_idx] += (
                    count[word_idx - 1][char_idx] *
                    memo[word_idx - 1][target_idx - 1]
                ) % ((10 ** 9) + 7)
                memo[word_idx][target_idx] %= ((10 ** 9) + 7)

        return memo[word_length][target_length]
