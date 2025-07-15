class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = offset = 0

        for expected, current in enumerate(arr):
            offset += current - expected
            chunks += offset == 0

        return chunks