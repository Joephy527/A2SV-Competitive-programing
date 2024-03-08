class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for i in range(len(nums)):
            count[nums[i]] += 1

            if count[nums[i]] > 2:
                nums[i] = "_"

        p = 0

        for s in range(len(nums)):
            if nums[s] != "_":
                nums[p], nums[s] = nums[s], nums[p]
                p += 1

        return p
