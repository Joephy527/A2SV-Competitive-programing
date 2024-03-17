class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        subStringSet = set()

        for i in range(len(s) - 1):
            sub = s[i:i + 2]
            subStringSet.add(sub)

        for i in range(len(s) - 1, 0, -1):
            sub = s[i - 1:i + 1]
            
            if sub[::-1] in subStringSet:
                return True
