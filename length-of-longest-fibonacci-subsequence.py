class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        sequence = 0

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                cur_length = 2

                while nxt in nums:
                    prev, cur = cur, nxt
                    nxt = prev + cur
                    cur_length += 1

                sequence = max(sequence, cur_length)

        return sequence if sequence > 2 else 0
