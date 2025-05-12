class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_evens = set()

        def is_unique(i, j, k):
            return (
                digits[k] % 2 == 0 and
                i != j and i != k and j != k and
                digits[i] != 0
            )
        
        def get_unique_num(hund_digit, tenth_digit, ones_digit):
            return (
                hund_digit * 100 + 
                tenth_digit * 10 + 
                ones_digit
            )

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if is_unique(i, j, k):
                        num = get_unique_num(
                            digits[i],
                            digits[j],
                            digits[k]
                        )
                        unique_evens.add(num)

        return sorted(unique_evens)