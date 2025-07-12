class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        first, second, temp = [], [], []
        greater = [-1] * len(nums)

        for idx, num in enumerate(nums):
            while second and nums[second[-1]] < num:
                greater[second.pop()] = num

            while first and nums[first[-1]] < num:
                temp.append(first.pop())

            while temp:
                second.append(temp.pop())

            first.append(idx)

        return greater