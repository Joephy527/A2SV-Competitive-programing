class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        a = []
        for i in range(len(l)):
            b = nums[l[i]:r[i]+1]
            if len(b) == 2:
                a.append(True)
            else:
                b.sort()
                c = []
                for j in range(len(b) - 2):
                    if b[j + 1] - b[j] == b[j + 2] - b[j + 1]:
                        c.append(True)
                    else:
                        c.append(False)
                if False in c:
                    a.append(False)
                else:
                    a.append(True)
        return a
