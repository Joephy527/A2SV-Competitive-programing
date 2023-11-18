class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        output = 0
        sign = 1
        stack = [sign]

        for i in s:
            if i.isdigit():
                output = output * 10 + int(i)
            elif i == '(':
                stack.append(sign)
            elif i == ')':
                stack.pop()
            elif i == '+' or i == '-':
                curr += sign * output
                sign = (1 if i == '+' else -1) * stack[-1]
                output = 0

        return curr + sign * output
