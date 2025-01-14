class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = [0] * (len(A) + 1)
        common = 0
        prefix = []

        for a, b in zip(A, B):
            count[a] += 1
            common += count[a] == 2

            count[b] += 1
            common += count[b] == 2

            prefix.append(common)

        return prefix
