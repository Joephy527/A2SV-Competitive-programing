class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for i in path.split("/"):
            if i != "" and i != "." and i != "..":
                stack.append(i)
            elif i == ".." and len(stack) > 0:
                stack.pop()

        return "/" + "/".join(stack)
