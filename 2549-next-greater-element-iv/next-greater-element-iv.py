class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        first, second = [], []
        greater = [-1] * len(nums)

        for idx, num in enumerate(nums):
            while second and nums[second[0][1]] < num:
                _, i = heappop(second)
                greater[i] = num

            while first and nums[first[-1]] < num:
                i = first.pop()
                heappush(second, (nums[i], i))

            first.append(idx)

        return greater