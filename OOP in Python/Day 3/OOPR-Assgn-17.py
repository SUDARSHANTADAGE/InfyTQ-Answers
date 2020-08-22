#OOPR-Assgn-17
#Start writing your code here

class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address
        
    def validate_customer_id(self):
        id=str(self.__customer_id)
        if len(id)==6:
            if id[0]=="1":
                return True
        return False
        
    def get_customer_id(self):
        return self.__customer_id
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_address(self):
        return self.__address
        
    
class Freight:
    counter=198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__freight_id=Freight.counter + 2
        self.__freight_charge=None
        
    def validate_weight(self):
        if self.__weight%5==0:
            return True
        return False
        
    def validate_distance(self):
        if 500<=self.__distance<=5000:
            return True
        return False
        
    def forward_cargo(self):
        if Customer.validate_customer_id(self.__from_customer) and Customer.validate_customer_id(self.__recipient_customer) and self.validate_distance() and self.validate_weight():
            
            Freight.counter += 2
            
            self.__freight_charge=self.__weight*150 + self.__distance*60
            
        else:
            self.__freight_charge=0 
    
    def get_freight_charge(self):
        return self.__freight_charge
        
    def get_freight_id(self):
        return self.__freight_id
        
    def get_recipient_customer(self):
        return self.__recipient_customer
        
    def get_from_customer(self):
        return self.__from_customer
        
    def get_weight(self):
        return self.__distance
        
    def get_distance(self):
        return self.__distance
