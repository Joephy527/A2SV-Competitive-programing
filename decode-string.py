class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        res = ""

        for c in s:
            if c.isnumeric():
                num = num * 10 + int(c)
            elif c == "[":    
                stack.append(res)
                stack.append(num)
                res = ""
                num = 0
            elif c == "]":
                count = stack.pop()
                prev = stack.pop()
                res = prev + count * res
            else:
                res += c

        return res
