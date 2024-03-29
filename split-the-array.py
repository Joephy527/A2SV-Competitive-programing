class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if count[num] > 2:
                return False

        return True
