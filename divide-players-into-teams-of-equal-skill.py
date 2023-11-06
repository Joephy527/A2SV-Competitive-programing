class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2: return skill[0] * skill[1]

        skill.sort()
        l, r = 0, len(skill) - 1
        Sum = skill[l] + skill[r]
        res = 0

        while l < r:
            if skill[l] + skill[r] != Sum:
                return -1
            else:
                res += skill[l] * skill[r]

            l += 1
            r -= 1

        return res
