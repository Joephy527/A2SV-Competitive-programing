class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = [i for i, j in Counter(nums).most_common()]
        return a[0]
