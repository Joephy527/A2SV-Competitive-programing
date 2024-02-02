class Solution:
    def defangIPaddr(self, address: str) -> str:
        defangedAddress = ""

        for char in address:
            if char == ".":
                defangedAddress += "[.]"
            else:
                defangedAddress += char

        return defangedAddress
