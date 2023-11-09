class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = defaultdict(int)

        for fruit in fruits:
            count[fruit] += 1
            
            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del(count[fruits[l]])
                
                l += 1

        ans = len(fruits) - l

        return len(fruits) - l
