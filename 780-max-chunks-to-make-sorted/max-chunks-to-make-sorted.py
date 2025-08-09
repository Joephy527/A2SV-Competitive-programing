class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            cur_max = num

            if stack:
                cur_max = max(cur_max, stack[-1])
                
                while stack and stack[-1] > num:
                    stack.pop()

            stack.append(cur_max)

        return len(stack)