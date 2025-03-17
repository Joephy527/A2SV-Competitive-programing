class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for c in count.values():
            if c % 2:
                return False

        return True
