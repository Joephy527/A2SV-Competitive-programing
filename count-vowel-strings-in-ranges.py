class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        vowel_count = [0] * len(words)
        vowel_strings = [0] * len(queries)
        prefix_sum = 0

        for idx, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum += 1
            
            vowel_count[idx] = prefix_sum

        for idx, (left, right) in enumerate(queries):
            vowel_strings[idx] = vowel_count[right]
            vowel_strings[idx] -= vowel_count[left - 1] if left else 0

        return vowel_strings
