class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in a:
                top = stack.pop() if stack else '#'
                if a[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack
