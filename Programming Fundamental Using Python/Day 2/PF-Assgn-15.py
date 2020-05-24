#PF-Assgn-15

def find_product(num1,num2,num3):
    product=0
    #write your logic here
    if(num1!=7 and num2!=7 and num3!=7):
        product=num3*num1*num2
    elif(num1==7 and num2!=7 and num3!=7):
        product=num3*num2
    elif(num1!=7 and num2==7 and num3!=7):
        product=num3
    else:
        product=-1
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)
