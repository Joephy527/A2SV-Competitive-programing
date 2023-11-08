class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]
        if len(num) == k: return "0"

        for s in num:
            while stack and s < stack[-1] and k:
                stack.pop()
                k -= 1

            if stack or s != "0":
                stack.append(s)

        if k: stack = stack[:-k]

        return "".join(stack) or "0"
