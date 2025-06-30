class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []

        for num in arr:
            cur_max = num

            while stack and num < stack[-1]:
                cur_max = max(
                    cur_max,
                    stack.pop()
                )

            stack.append(cur_max)

        return len(stack)