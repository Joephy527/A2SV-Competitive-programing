class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string):
            stack = []

            for c in string:
                if c == "#" and stack:
                    stack.pop()
                
                if c != "#":
                    stack.append(c)

            return stack

        return processString(s) == processString(t)
