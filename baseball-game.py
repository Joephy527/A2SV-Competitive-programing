class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                val = stack[-1] * 2
                stack.append(val)
            elif op == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
            else:
                stack.append(int(op))

        ans = sum(stack)
        
        return ans
