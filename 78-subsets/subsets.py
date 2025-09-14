class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs, cur = [], []

        def back_track(idx = 0):
            if idx == len(nums):
                subs.append(cur[:])

                return

            cur.append(nums[idx])
            back_track(idx + 1)
            
            cur.pop()
            back_track(idx + 1)

        back_track()

        return subs