class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        
        for i in nums:
            if i in Set:
                return True

            Set.add(i)
