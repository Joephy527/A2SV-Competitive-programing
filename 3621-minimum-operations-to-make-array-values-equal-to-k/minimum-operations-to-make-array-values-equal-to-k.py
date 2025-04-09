class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        op = 0

        for num in count:
            if num < k:
                return -1
            elif num > k:
                op += 1

        return op