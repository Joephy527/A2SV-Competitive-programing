class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda left, right: left + right,
            "-": lambda left, right: left - right,
            "*": lambda left, right: left * right,
            "/": lambda left, right: int(left / right)
        }

        for token in tokens:
            if token in operations:
                right, left = stack.pop(), stack.pop()
                stack.append(operations[token](left, right))
            else:
                stack.append(int(token))

        return stack.pop()
