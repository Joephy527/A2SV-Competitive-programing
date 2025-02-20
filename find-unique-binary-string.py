class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        n = len(nums)
        
        for num in nums:
            integers.add(int(num, 2))
        
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                
                return "0" * (n - len(ans)) + ans
