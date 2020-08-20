#OOPR-Assgn-12
#Start writing your code here


class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=0
        
    def get_bill_id(self):
        return self.__bill_id
        
    def get_patient_name(self):
        return self.__patient_name
        
    def get_bill_amount(self):
        return self.__bill_amount
        
    def calculate_bill_amount(self, consultation_fees, quantity_list,price_list):
        for i in range(len(quantity_list)):
            self.__bill_amount+= (quantity_list[i]*price_list[i])
            
        self.__bill_amount+=consultation_fees
        
        print(self.__bill_id)
        print(self.__patient_name)
        print(self.__bill_amount)
        
b=Bill(1,'Sudarshan')
b.calculate_bill_amount(200,[2,4,6],[100,100,500])
