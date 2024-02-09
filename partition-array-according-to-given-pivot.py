class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        rearrange = []
        pivotAmount = 0

        for num in nums:
            if num < pivot:
                rearrange.append(num)
            elif num == pivot:
                pivotAmount += 1
        
        for i in range(pivotAmount):
            rearrange.append(pivot)

        for num in nums:
            if pivot < num:
                rearrange.append(num)

        return rearrange
