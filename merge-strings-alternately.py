class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2, answer = 0, 0, ""

        while pointer1 < len(word1) and pointer2 < len(word2):
            answer += word1[pointer1]
            answer += word2[pointer2]
            pointer1 += 1
            pointer2 += 1

        # if word1 is longer than word2
        while pointer1 < len(word1):
            answer += word1[pointer1]
            pointer1 += 1

        # if word2 is longer than word1
        while pointer2 < len(word2):
            answer += word2[pointer2]
            pointer2 += 1

        return answer
