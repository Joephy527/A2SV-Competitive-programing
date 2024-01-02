class Solution:
    def checkString(self, s: str) -> bool:
        characters = set()
        for c in s:
            if c == "a" and "b" in characters:
                return False
                
            characters.add(c)
            
        return True
