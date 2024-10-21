class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minN, maxN = min(nums), max(nums)
        
        for num in range(maxN, 0, -1) :
            if (not minN % num and 
                not maxN % num):
                return num
