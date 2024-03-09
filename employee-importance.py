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
        employeesDict = {}
        for employee in employees:
            employeesDict[employee.id] = employee

        def calcImportance(node):
            if not node: return

            importance = node.importance

            for subordinate in node.subordinates:
                importance += calcImportance(employeesDict[subordinate])

            return importance

        for employee in employees:
            if employee.id == id:
                return calcImportance(employee)
