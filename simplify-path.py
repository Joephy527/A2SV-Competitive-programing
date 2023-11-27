class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for pathName in path.split("/"):
            if pathName != "." and pathName != ".." and pathName != "":
                stack.append(pathName)

            if pathName == ".." and stack:
                    stack.pop()

        return "/" + "/".join(stack)
