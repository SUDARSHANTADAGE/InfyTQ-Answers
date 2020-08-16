#OOPR-Exer-6
#Start writing your code here

class Vehicle:
    def __init__(self):
        self.fuel_left=None
        self.mileage=None
        self.initial_fuel=10
        
    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left>5:
            self.fuel=self.fuel_left-5
            self.distance=self.fuel*self.mileage
            return self.distance
        else:
            return 0
        
    def identify_distance_travelled(self,initial_fuel):
        self.initial_fuel=initial_fuel
        self.fuel=self.initial_fuel-self.fuel_left
        self.distance=self.fuel*self.mileage
        return self.distance
        
v1=Vehicle()
v1.mileage=50
v1.fuel_left=7
print(v1.identify_distance_that_can_be_travelled())
print(v1.identify_distance_travelled(20))
