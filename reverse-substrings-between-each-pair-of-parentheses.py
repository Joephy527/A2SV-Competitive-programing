class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ")":
                toBeReversed = []

                while stack[-1] != "(":
                    toBeReversed.append(stack.pop())

                stack.pop()
                stack.extend(toBeReversed)
            else:
                stack.append(c)

        return "".join(stack)
