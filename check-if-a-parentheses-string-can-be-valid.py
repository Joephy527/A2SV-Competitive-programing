class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
			
        openCount = options = optionsBorrowed = 0
        
        for i in range(len(s)):
            if locked[i] == "0":
                if openCount:
                    openCount -= 1
                    optionsBorrowed += 1
                else:
                    options += 1
                continue
                
            if s[i] == "(":
                openCount += 1
                continue
                
            if openCount:
                openCount -= 1
            elif optionsBorrowed:
                optionsBorrowed -= 1
                options += 1
            elif options:
                options -= 1
            else:
                return False
                
        if not openCount:
            return True
