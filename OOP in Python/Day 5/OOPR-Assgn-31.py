#OOPR-Assgn-31
import math
from abc import ABCMeta, abstractmethod
class Logistics(metaclass=ABCMeta):
    __counter=7001
    def __init__(self,start_reading,end_reading):
        self.__consumer_id=0
        self.__start_reading=start_reading
        self.__end_reading=end_reading
    def get_consumer_id(self):
        return self.__consumer_id
    def get_start_reading(self):
        return self.__start_reading
    def get_end_reading(self):
        return self.__end_reading
    def validate_meter_reading(self):
        if(self.__start_reading >= self.__end_reading):
            return False
        else:
            return True
    def generate_consumer_id(self):
        if not Logistics.__counter:
            Logistics.__counter=7001
        if not self.__consumer_id:
            self.__consumer_id = Logistics.__counter
            Logistics.__counter = Logistics.__counter + 1 
        
    @abstractmethod
    def calculate_bill_amount(self):
        pass
class PassengerLogistics(Logistics):
    __list_vehicle=["BMW","TOYOTA","FORD"]
    __list_minimum_charge=[3000,1500,1000] #these lists are storing vehicle type, minimum charge, rate per kilometer for first hundred and rate per kilometer for rest of distance
    __list_charge_for_hundred=[30,15,10]   #there is a one to one correspondence
    __list_charge_after_hundred=[25,12,7]
    def __init__(self,vehicle_type,start_reading,end_reading):
        super().__init__(start_reading,end_reading)
        self.__vehicle_type=vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type
    def validate_vehicle_type(self):
        for index in range(0,len(PassengerLogistics.__list_vehicle)):
            if(PassengerLogistics.__list_vehicle[index]==self.__vehicle_type):
                return index
        return -1
    def calculate_bill_amount(self):
        bill=0 
        if self.validate_vehicle_type()>=0 and Logistics.validate_meter_reading(self)==True:
            Logistics.generate_consumer_id(self)
            total_distance=self.get_end_reading() - self.get_start_reading()
            v_index=PassengerLogistics.__list_vehicle.index(self.__vehicle_type)
            if total_distance<=100:
                bill=PassengerLogistics.__list_charge_for_hundred[v_index] * total_distance
            else:
                distance=total_distance-100
                bill = (PassengerLogistics.__list_charge_for_hundred[v_index] * 100) + (PassengerLogistics.__list_charge_after_hundred[v_index] * distance)
            
            if bill <PassengerLogistics.__list_minimum_charge[v_index]:
                bill = PassengerLogistics.__list_minimum_charge[v_index]
            
            bill_amount = bill + bill*0.05
            return bill_amount
        else:
            return -1 
    # implement the code to calculate the bill amount according to the requirement
class GoodsLogistics(Logistics):
    __carrier_dict={"TATA":20,"EICHER":30,"FORCE":35} # stores the carrier type and rate per kilometer for 1000kg
    def __init__(self,carrier_type,goods_weight,start_reading,end_reading):
        super().__init__(start_reading,end_reading)
        self.__carrier_type=carrier_type
        self.__goods_weight=goods_weight
    def get_carrier_type(self):
        return self.__carrier_type
    def get_goods_weight(self):
        return self.__goods_weight
    def validate_carrier_type(self):
        for carrier in GoodsLogistics.__carrier_dict:
            if(carrier==self.__carrier_type):
                return True
        return False
    def calculate_bill_amount(self):
        if(self.validate_carrier_type()):
            if(self.validate_meter_reading()):
                self.generate_consumer_id()
                total_distance=self.get_end_reading()-self.get_start_reading()
                multiplier = math.ceil(self.__goods_weight/1000)-1 
                if(self.__goods_weight<=1000):
                    charge_per_kilometer=GoodsLogistics.__carrier_dict[self.__carrier_type]
                elif(self.__goods_weight >1000 and self.__goods_weight<=3000):
                    charge_per_kilometer=GoodsLogistics.__carrier_dict[self.__carrier_type] * 2 ** multiplier
                else:
                    charge_per_kilometer=200
                bill_amount=total_distance*charge_per_kilometer
                bill_amount=bill_amount+(bill_amount*0.1)+2000
                return bill_amount
            else:
                return -1
        else:
            return -1
passenger_logistic=PassengerLogistics("BMW",300,400)
bill_amount=passenger_logistic.calculate_bill_amount()
if(bill_amount==-1):
    print("Invalid vehicle type or meter reading ")
else:
    print("Consumer id    :",passenger_logistic.get_consumer_id())
    print("Start reading  :",passenger_logistic.get_start_reading())
    print("End reading    :",passenger_logistic.get_end_reading())
    print("Total Amount   :",bill_amount)
print("------------------------------------------------------------")
goods_logistic=GoodsLogistics("FORCE",3000,300,400)
bill_amount=goods_logistic.calculate_bill_amount()
if(bill_amount==-1):
    print("Invalid career type or meter reading ")
else:
    print("Consumer id    :",goods_logistic.get_consumer_id())
    print("Goods weight   :",goods_logistic.get_goods_weight())
    print("Start reading  :",goods_logistic.get_start_reading())
    print("End reading    :",goods_logistic.get_end_reading())
    print("Total Amount   :",bill_amount)
