class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQueue = deque(students)
        sandwichesQueue = deque(sandwiches)

        while studentQueue:
            if sandwichesQueue[0] not in studentQueue:
                break

            if studentQueue[0] == sandwichesQueue[0]:
                sandwichesQueue.popleft()
                studentQueue.popleft()
            else:
                studentQueue.append(studentQueue.popleft())

        return len(studentQueue)
