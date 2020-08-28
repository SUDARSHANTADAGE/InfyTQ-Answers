#OOPR-Assgn-24
#Start writing your code here

class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__price=price
        self.__item_type=item_type
        self.__item_id=None
        if self.__item_type=="Cotton":
            Apparel.counter+=1 
            self.__item_id="C"+str(Apparel.counter)
        elif self.__item_type=="Silk":
            Apparel.counter+=1
            self.__item_id="S"+str(Apparel.counter)
            
    def calculate_price(self):
        self.__price=self.__price+self.__price*0.05
        
    def get_item_id(self):
        return self.__item_id
        
    def get_price(self):
        return self.__price
        
    def get_item_type(self):
        return self.__item_type
        
    def set_price(self,price):
        self.__price=price
        
        
class Cotton(Apparel):
    def __init__(self,price,discount):
        Apparel.__init__(self,price,"Cotton")
        self.__discount=discount
        
        
    def calculate_price(self):
        Apparel.calculate_price(self)
        price=self.get_price()
        price = price - (price*(self.__discount)/100)
        price=price+price*0.05
        Apparel.set_price(self,price)
        
    def get_discount(self):
        return self.__discount
        
class Silk(Apparel):
    def __init__(self,price):
        Apparel.__init__(self,price,"Silk")
        self.__points=0
        
        
    def calculate_price(self):
        Apparel.calculate_price(self)
        price=self.get_price()
        if price>10000:
            self.__points=10 
        else:
            self.__points=3
            
        price = price * 1.10 
        Apparel.set_price(self,price)
    def get_points(self):
        return self.__points
