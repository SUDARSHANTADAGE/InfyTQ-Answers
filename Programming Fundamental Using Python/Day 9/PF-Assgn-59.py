#PF-Assgn-59
def check_perfect_number(number):
    
    num=[]
    for i in range(1,number):
        if number%i==0:
            num.append(i)
    total=sum(num)
    if number==total and number!=0:
        return True
    else:
        return False
def check_perfectno_from_list(no_list):
    perfect=[]
    for i in no_list:
        result=check_perfect_number(i)
        if result:
            perfect.append(i)
    return perfect
 
    
perfectno_list=check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)
