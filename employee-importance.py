"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeesMap = {}

        for employee in employees:
            employeesMap[employee.id] = employee

        def dfs(vertex):
            importance = vertex.importance

            for employeeId in vertex.subordinates:
                importance += dfs(employeesMap[employeeId])

            return importance

        for employee in employees:
            if employee.id == id:
                return dfs(employee)
