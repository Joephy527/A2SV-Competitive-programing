class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = [[] for i in range(101)]
        pair = 0
        
        for j, x in enumerate(nums):
            for i in count[x]:
                pair += (i*j % k == 0)
            
            count[x].append(j)
        
        return pair