class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        stack = []

        for i in range(len(position)):
            dic[position[i]] = (target - position[i]) / speed[i]

        position.sort(reverse=True)

        for p in position:
            if not stack:
                stack.append(dic[p])
            else:
                if stack[-1] < dic[p]:
                    stack.append(dic[p])

        return len(stack)
