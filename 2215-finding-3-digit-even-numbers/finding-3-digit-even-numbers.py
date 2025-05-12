class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        unique_even = []

        def change_count(digs, change):
            for d in digs:
                count[d] += change

        def is_unique(digs):
            for d in digs:
                if count[d] < 0:
                    return False

            return True

        for digit in range(100, 1000, 2):
            digs = digit % 10, (digit // 10) % 10, digit // 100
            
            change_count(digs, -1)
            
            if is_unique(digs):
                unique_even.append(digit)

            change_count(digs, 1)

        return unique_even