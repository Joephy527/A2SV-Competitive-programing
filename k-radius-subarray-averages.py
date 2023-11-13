class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        win = k * 2 + 1
        
        if len(nums) < win: return avgs
        
        s = sum(nums[:win])
        avgs[k] = s // win
        l, r = 0, win

        while r < len(nums):
            s = s - nums[l] + nums[r]
            avg = s // win
            avgs[r - k] = avg
            l += 1
            r += 1

        return avgs
