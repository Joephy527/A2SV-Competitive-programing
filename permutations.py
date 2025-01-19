class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations, sub_sequence = [], []

        def back_track(mask=0): 
            if len(sub_sequence) == n:
                permutations.append(sub_sequence[:])
                
                return

            for i in range(n):
                bit = 1 << i
                
                if not (mask & bit):
                    sub_sequence.append(nums[i])
                    back_track(mask | bit)
                    sub_sequence.pop()
        
        back_track()
        
        return permutations
