class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        valIdxPair = []

        for idx, num in enumerate(nums):
            val = 0

            for c in str(num):
                val *= 10
                val += mapping[int(c)]

            valIdxPair.append((val, idx))

        valIdxPair.sort()

        return [nums[pair[1]] for pair in valIdxPair]
