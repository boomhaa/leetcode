# link to the problem - https://leetcode.com/problems/design-underground-system/

# An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.
# Implement the UndergroundSystem class:
# void checkIn(int id, string stationName, int t)
# A customer with a card ID equal to id, checks in at the station stationName at time t.
# A customer can only be checked into one place at a time.
# void checkOut(int id, string stationName, int t)
# A customer with a card ID equal to id, checks out from the station stationName at time t.
# double getAverageTime(string startStation, string endStation)
# Returns the average time it takes to travel from startStation to endStation.
# The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
# The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
# There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
# You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

# link to submission - https://leetcode.com/submissions/detail/701542087/

class UndergroundSystem:

    def __init__(self):
        self.checkedInUsers = {}
        self.averageTimes = {}

    def checkIn(self, id, stationName, t):
        self.checkedInUsers[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        startStation, startTime = self.checkedInUsers[id]

        endStation, endTime = stationName, t

        trip = (startStation, endStation) if startStation < endStation else (endStation, startStation)
        average, count = self.averageTimes.get(trip, (0, 0))
        self.averageTimes[trip] = ((average * count + (endTime - startTime)) / (count + 1), count + 1)

    def getAverageTime(self, startStation, endStation):
        trip = (startStation, endStation) if startStation < endStation else (endStation, startStation)
        return self.averageTimes[trip][0]
a=UndergroundSystem()
a.checkIn(10,"a",3)
a.checkOut(10,"b",8)
print(a.getAverageTime("a","b"))
a.checkIn(5,"a",10)
a.checkOut(5,"b",16)
print(a.getAverageTime("a","b"))
a.checkIn(2,"a",21)
a.checkOut(2,"b",30)
print(a.getAverageTime("a","b"))
