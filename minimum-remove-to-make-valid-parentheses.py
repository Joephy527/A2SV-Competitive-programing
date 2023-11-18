class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = []
        res = []
        dis = set()

        for i, c in enumerate(s):
            if c == "(":
                opened.append(i)
            
            if c == ")":
                if opened:
                    opened.pop()
                else:
                    dis.add(i)

        for i in opened:
            dis.add(i)

        for i, c in enumerate(s):
            if i not in dis:
                res.append(c)

        return "".join(res)
