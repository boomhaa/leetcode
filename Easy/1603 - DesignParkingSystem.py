# link to the problem - https://leetcode.com/problems/design-parking-system/

# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.
# Implement the ParkingSystem class:
# ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

# link to submission - https://leetcode.com/submissions/detail/686212891/

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small
        self.new_list = []
        self.new_list.append(big)
        self.new_list.append(medium)
        self.new_list.append(small)

    def addCar(self, carType):
        if self.new_list[carType - 1] > 0:
            self.new_list[carType - 1] -= 1
            return True
        return False
