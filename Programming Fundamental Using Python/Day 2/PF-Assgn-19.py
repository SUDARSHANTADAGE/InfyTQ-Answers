#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    amt=0
    #write your logic here
    if quantity_ordered>0 and distance_in_kms>0 :
        if food_type == "n" or food_type == "v":
            return -1
        if food_type =="N":
            amt=150
        elif food_type=="V":
            amt=120
        bill_amt=amt*quantity_ordered
        if distance_in_kms<4:
            dist_amt=0
            bill_amount=bill_amt
        elif 3<=distance_in_kms<=6:
            dist_amt=(distance_in_kms-3)*3
            bill_amount=bill_amt+dist_amt
        else:
            dist_amt1=((distance_in_kms-6)*6)+9
            bill_amount=bill_amt+dist_amt1
    else:
        bill_amount=-1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("v",2,8)
print(bill_amount)
