class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 12:
            return -1
        
        max_int = 2 ** 31

        num_str = [d for d in str(n)]

        for i in range(len(num_str) - 2, -1, -1):
            if int(num_str[i]) < int(num_str[i + 1]):
                for j in range(len(num_str) - 1, i, -1):
                    if int(num_str[j]) > int(num_str[i]):
                        num_str[i], num_str[j] = num_str[j], num_str[i]
                        num_str = num_str[:i + 1] + num_str[i + 1:][::-1]

                        break

                break

        num = int("".join(num_str))

        if num >= max_int or num == n:
            return -1

        return num