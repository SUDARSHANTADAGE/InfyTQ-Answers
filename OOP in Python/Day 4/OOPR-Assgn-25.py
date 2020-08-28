#OOPR-Assgn-25
#Start writing your code here

class FruitInfo:
    __fruit_name_list=['Apple','Guava','Orange','Grape','Sweet Lime']
    __fruit_price_list=[200,80,70,110,60]
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            fruit_index=FruitInfo.__fruit_name_list.index(fruit_name)
            price_per_kg=FruitInfo.__fruit_price_list[fruit_index]
            return price_per_kg
        else:
            return -1
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
        
class Purchase:
    __counter=101
    def __init__(self,customer,fruit_name,quantity):
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity
        self.__purchase_id=None
        
    def calculate_price(self):
        price=FruitInfo.get_fruit_price(self.__fruit_name)
        if FruitInfo.get_fruit_price(self.__fruit_name) != -1:
            mx=FruitInfo.get_fruit_price_list()
            maximum=max(mx)
            minimum=min(mx)
            total_price=price*self.__quantity
            if price==maximum and self.__quantity>1:
                total_price*=0.98 
            
            if price==minimum and self.__quantity>=5:
                total_price*=0.95 
            
            if Customer.get_cust_type(self.__customer)=='wholesale':
                total_price*=0.90
                    
            self.__purchase_id="P"+str(Purchase.__counter)
            Purchase.__counter+=1
        
            return total_price
        
        else:
            return -1
            
    def get_purchase_id(self):
        return self.__purchase_id
        
    def get_customer(self):
        return self.__customer
        
    def get_quantity(self):
        return self.__quantity
        
        
class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_cust_type(self):
        return self.__cust_type
        
        
c=Customer("Tom", "wholesale")
p=Purchase(c,"Guava", 2)
print(p.calculate_price())
#fruit_name-Guava,quantity-2
