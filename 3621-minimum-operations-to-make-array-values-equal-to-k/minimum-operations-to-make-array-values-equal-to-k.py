class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()

        for num in nums:
            if num < k:
                return -1
            
            seen.add(num)

        return len(seen) - 1 if k in seen else len(seen)