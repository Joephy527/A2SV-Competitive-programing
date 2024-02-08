class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        totalSalary = 0

        for i in range(1, len(salary) - 1):
            totalSalary += salary[i]

        return totalSalary / (len(salary) - 2)
