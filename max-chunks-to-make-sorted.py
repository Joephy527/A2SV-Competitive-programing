class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                maxElement = stack[-1]
                
                while stack and num < stack[-1]:
                    stack.pop()
                
                stack.append(maxElement)

        return len(stack)
