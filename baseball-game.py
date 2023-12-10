class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op != "C" and op != "D" and op != "+":
                stack.append(int(op))
            
            if op == "C":
                stack.pop()

            if op == "D":
                val = stack[-1] * 2
                stack.append(val)

            if op == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)

        ans = sum(stack)
        
        return ans
