class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def maxDiff(l, r):
            if l == r:
                return nums[l]
            
            scoreFirst = nums[l] - maxDiff(l + 1,r)
            scoreLast = nums[r] - maxDiff(l,r - 1)

            return max(scoreFirst, scoreLast)
        
        return maxDiff(0, len(nums) - 1) >= 0
