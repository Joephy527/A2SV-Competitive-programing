class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0

        while nums[0] < k:
            min_1, min_2 = heappop(nums), heappop(nums)
            heappush(nums, (min_1 * 2) + min_2)
            operations += 1

        return operations
