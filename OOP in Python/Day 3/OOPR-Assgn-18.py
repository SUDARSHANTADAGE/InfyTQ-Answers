#OOPR-Assgn-18
#Start writing your code here

class Bill:
    counter=1000
    def __init__(self):
        self.__bill_id=1000
        self.__bill_amount=0 
        
    def generate_bill_amount(self,item_quantity,items):
        Bill.counter+=1
        self.__bill_amount=0
        self.__bill_id='B'+str(Bill.counter)  
        tmp_dict=item_quantity  
        a={}
        for item in tmp_dict:
            a[item.lower()]=tmp_dict[item]    
        for prod,quan in a.items():
            for item in items:
                if item.get_item_id().lower()==prod:
                    self.__bill_amount+=quan*item.get_price_per_quantity()
                    break
        
    def get_bill_id(self):
        return self.__bill_id
        
    def get_bill_amount(self):
        return self.__bill_amount
        
class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None
        
    def pays_bill(self,bill):
        self.__payment_status="Paid"
        
        print(self.__customer_name)
        print(bill.get_bill_id())
        print(bill.get_bill_amount())
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_payment_status(self):
        return self.__payment_status
        
class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity
        
        
    def get_item_id(self):
        return self.__item_id
        
    def get_description(self):
        return self.__description
        
    def get_price_per_quantity(self):
        return self.__price_per_quantity
        
        
item_quantity = {'Ir987':3, 'IR346':2, 'IR658':4, 'IR123':2}
c=Customer("Sudarshan")
i1=Item("IR987","Sunfeast Marie",100.0)
i2=Item("ir658","Kellogs Oats",151.0)
i3=Item("Ir346","Maggie Noodles",35.75)
i4=Item("iR234","Kissan Jam",100.0)
i5=Item("IR123","Nescafe",55.5)
i6=Item("IR111","Milk",100.0)
items=[i1,i2,i3,i4,i5,i6]
b=Bill()
b.generate_bill_amount(item_quantity,items)
b.generate_bill_amount(item_quantity,items)
b.generate_bill_amount(item_quantity,items)
b.generate_bill_amount(item_quantity,items)
b.generate_bill_amount(item_quantity,items)

c.pays_bill(b)
print(b.get_bill_id())
print(b.get_bill_amount())
