class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        total = 0
        
        for num in arr:
            if not stack:
                stack.append([num,1,0])
            else:
                count=0
                
                while stack and stack[-1][0] > num:
                    a, b, c = stack.pop()
                    total += (a * (count + b)) + (count * c * a)
                    count += b
                
                stack.append([num, 1 + count, count])

        count = 0

        while stack:
            a, b, c = stack.pop()
            total += (a * (count + b)) + (count * c * a)
            count += b
        
        return total % ((10**9)+7)
