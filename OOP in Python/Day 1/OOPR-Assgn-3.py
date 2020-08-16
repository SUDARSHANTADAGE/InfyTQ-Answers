#OOPR-Assgn-3
#Start writing your code here

class Customer:
    def __init__(self):
        self.customer_name="Sudarshan"
        self.bill_amount=0 
        
    def pays_bill(self,amount):
        print(self.customer_name+" pays bill amount of Rs. "+str(amount))
        
    def purchases(self):
        self.bill_amount=500
        bill=self.bill_amount-self.bill_amount*5/100
        self.pays_bill(bill)
        
        
c1=Customer()
c1.purchases()
