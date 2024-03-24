class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k: int) -> int:
            count = defaultdict(int)
            p = subArr = 0

            for s in range(len(nums)):
                count[nums[s]] += 1

                while p <= s and len(count) > k:
                    count[nums[p]] -= 1

                    if not count[nums[p]]:
                        del count[nums[p]]

                    p += 1

                subArr += s - p + 1
                
            return subArr

        return atMostK(k) - atMostK(k - 1)
