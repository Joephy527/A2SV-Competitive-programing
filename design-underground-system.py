class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.travelTime = defaultdict(int)
        self.customers = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, checkIntime = self.checkInMap[id]
        self.travelTime[(checkInStation, stationName)] += t - checkIntime
        self.customers[(checkInStation, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totlaTravelTime = self.travelTime[(startStation, endStation)]
        totalCustomers = self.customers[(startStation, endStation)]

        return totlaTravelTime / totalCustomers


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
