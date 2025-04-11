class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric = 0
        
        def is_symmetric(s):
            if len(s) % 2:
                return 0

            left, right = 0, len(s) - 1
            left_sum = right_sum = 0

            while left < right:
                left_sum += int(s[left])
                right_sum += int(s[right])

                left += 1
                right -= 1

            return left_sum == right_sum
        
        for num in range(low, high + 1):
            string = str(num)
            symmetric += is_symmetric(string)

        return symmetric