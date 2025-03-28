class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for c in s:
            if (len(stack) < 2 or 
               (len(stack) > 1 and 
                not stack[-1] == stack[-2] == c)):
                stack.append(c)

        return "".join(stack)
