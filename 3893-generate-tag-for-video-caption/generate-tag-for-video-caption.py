class Solution:
    def generateTag(self, caption: str) -> str:
        tag = ["#"]

        for i in range(len(caption)):
            p, c = caption[i - 1], caption[i]

            if c != " ":
                if p == " " and len(tag) != 1:
                    tag.append(c.upper())
                else:
                    tag.append(c.lower())

        return "".join(tag[:min(100, len(tag))])