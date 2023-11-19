class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        nums, ans = [], []
        
        for val in arr2:
            dic[val] = 0
        
        for val in arr1:
            if val not in dic:
                nums.append(val)
            else: 
                dic[val] += 1
                
        for key, val in dic.items():
            ans.extend([key for _ in range(val)])
        
        ans.extend(sorted(nums))
        
        return ans
