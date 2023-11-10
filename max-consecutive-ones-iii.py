class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p, ans = 0, 0

        for s in range(len(nums)):
            if nums[s] == 0:
                if k > 0:
                    k -= 1
                else:
                    while nums[p] == 1:
                        p += 1
                    
                    p += 1

            ans = max(ans, s - p + 1)

        return ans
