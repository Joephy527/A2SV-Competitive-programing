class Solution:
    def checkValidString(self, s: str) -> bool:
        countStar = []
        stack = []

        for idx, c in enumerate(s):
            if c == "*":
               countStar.append(idx)
            elif c == "(":
                stack.append(idx)
            else:
                if stack:
                    stack.pop()
                elif countStar:
                    countStar.pop()
                else:
                    return False

        while stack:
            if countStar and countStar[-1] > stack[-1]:
                stack.pop()
                countStar.pop()
            else:
                return False

        return not stack
