class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = list(range(26))
        smallest = [""] * len(baseStr)
        
        def find(char):
            c = ord(char) - ord("a")
            
            while graph[c] != c:
                c = graph[c]

            return c

        def union(c1, c2):
            char1, char2 = find(c1), find(c2)

            if char1 < char2:
                graph[char2] = char1
            elif char1 > char2:
                graph[char1] = char2

        for c1, c2 in zip(s1, s2):
            union(c1, c2)

        for i, c in enumerate(baseStr):
            char = find(c) + ord("a")
            smallest[i] = chr(char)

        return "".join(smallest)