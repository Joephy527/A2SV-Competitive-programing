class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return (self.checkPalindromePossibility(a, b) or
                self.checkPalindromePossibility(b, a))

    def checkPalindromePossibility(self, arr1, arr2):
        i = 0
        j = len(arr1) - 1
        
        while i < j and arr1[i] == arr2[j]:
            i += 1
            j -= 1
        
        return (self.isPalindrome(arr1[:i] + arr2[i:]) or
                self.isPalindrome(arr1[:j + 1] + arr2[j + 1:]))

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
