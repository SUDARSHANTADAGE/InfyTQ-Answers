#OOPR-Assgn-30
#Start writing your code here
pizza=["small","medium"]
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
        
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
            
    def get_customer_name(self):
        return self.__customer_name
        
    def get_quantity(self):
        return self.__quantity
        
        
class Pizzaservice:
    counter=100
    
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.__service_id=None
        self.pizza_cost=0 
        
    
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in pizza:
            return True
        else:
            return False
            
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() ==True and Customer.validate_quantity(self.__customer)==True:
            if self.__pizza_type.lower()=="small" and self.__additional_topping==True:
                self.pizza_cost=185 * Customer.get_quantity(self.__customer)
            elif self.__pizza_type.lower()=="small" and self.__additional_topping==False:
                self.pizza_cost=150 * Customer.get_quantity(self.__customer)
            elif self.__pizza_type.lower()=="medium" and self.__additional_topping==True:
                self.pizza_cost=250 * Customer.get_quantity(self.__customer)
            elif self.__pizza_type.lower()=="medium" and self.__additional_topping==False:
                self.pizza_cost=200 * Customer.get_quantity(self.__customer)
                
            self.__service_id=self.__pizza_type[0]+str(Pizzaservice.counter+1)
            Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1
            
            
    def get_service_id(self):
        return self.__service_id
        
    def get_pizza_type(self):
        return self.__pizza_type
        
    def get_customer(self):
        return self.__customer
        
    def get_additional_topping(self):
        return self.__additional_topping
        

class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer,pizza_type,additional_topping)
        self.__distance_in_kms=distance_in_kms
        self.__delivery_charge=0 
        
    def validate_distance_in_kms(self):
        if 1<=self.__distance_in_kms<=10:
            return True
        else:
            return False
            
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms() == True:
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost != -1:
                if self.__distance_in_kms<6:
                    self.__delivery_charge=self.__distance_in_kms*5 
                else:
                    distance=self.__distance_in_kms-5
                    self.__delivery_charge=25+(distance * 7)
                self.pizza_cost +=self.__delivery_charge
        else:
            self.pizza_cost=-1
            
    def get_delivery_charge(self):
        return self.__delivery_charge
        
    def get_distance_in_kms(self):
        return self.__distance_in_kms
        

c=Customer("Asha",5)
p=Pizzaservice(c,"medium",False)
d=Doordelivery(c,"medium",False,8)
#print(c.validate_quantity())
#print(p.validate_pizza_type())
d.calculate_pizza_cost()
print(d.pizza_cost)
