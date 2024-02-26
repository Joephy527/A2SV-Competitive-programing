class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        m = len(nums) // 2

        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])

        pLeft = pRight = 0
        sortedArray = []
        
        while pLeft < len(left) and pRight < len(right):
            if left[pLeft] <= right[pRight]:
                sortedArray.append(left[pLeft])
                pLeft += 1
            else:
                sortedArray.append(right[pRight])
                pRight += 1

        while pLeft < len(left):
            sortedArray.append(left[pLeft])
            pLeft += 1
                

        while pRight < len(right):
            sortedArray.append(right[pRight])
            pRight += 1

        return sortedArray
