class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkDuplicate = set()

        for num in nums:
            if num in checkDuplicate:
                return True

            checkDuplicate.add(num)
