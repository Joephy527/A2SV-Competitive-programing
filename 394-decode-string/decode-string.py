class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                cur = []

                while stack[-1] != "[":
                    cur.append(stack.pop())

                stack.pop()
                digit = ""

                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit

                stack.append("".join(reversed(cur)) * int(digit))
            else:
                stack.append(c)

        return "".join(stack)