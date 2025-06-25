class Vehicle:
    def __init__(self, km):
        self.km = km

class Bus(Vehicle):
    def __init__(self, km, fare):
        Vehicle.__init__(self, km)
        self.fare = fare

    def display_fare(self):
        print("The total fare is:", self.km * self.fare)

citybus = Bus(15, 5)
citybus.display_fare()