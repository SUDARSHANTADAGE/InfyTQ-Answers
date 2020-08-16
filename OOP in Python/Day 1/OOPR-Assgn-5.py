#OOPR-Assgn-5
#Start writing your code here

def check_type(type):
    vehicle_type=['Two Wheeler', 'Four Wheeler']
    if type not in vehicle_type:
            return 0
    return 1
class Vehicle:
    def __init__(self):
        self.__vehicle_cost=None
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__premium_amount=None
        
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_type(self,vehicle_type):
        if check_type(vehicle_type):
            self.__vehicle_type=vehicle_type
        else:
            return "invalid Vehicle DETAILS"
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount
        
    def calculate_premium(self):
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=self.__vehicle_cost*2/100
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=self.__vehicle_cost*6/100
        else:
            print("Invalid Vehicle Type")
            
    def display_vehicle_details(self):
        print(self.__premium_amount)
    
v1 = Vehicle()
#v1.set_vehicle_id=10
v1.set_vehicle_type("Two Wheeler")
v1.set_vehicle_cost(105000)
v1.calculate_premium()
v1.display_vehicle_details()
