class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per = []
        sub = []
        seen = set()

        def backTrack():
            if len(sub) == len(nums):
                per.append(sub[:])

                return
            
            for i, num in enumerate(nums):
                if i not in seen:
                    sub.append(num)
                    seen.add(i)
                    backTrack()
                    sub.pop()
                    seen.remove(i)

        backTrack()

        return per
