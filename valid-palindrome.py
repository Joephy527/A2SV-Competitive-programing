class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalpha() or i.isdigit())
        s = s.lower()
        s_rev = s[::-1]
        if s == s_rev:
            return True
        else:
            return False
