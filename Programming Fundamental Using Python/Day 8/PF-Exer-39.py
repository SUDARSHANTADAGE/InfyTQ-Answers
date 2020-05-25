'''
Write a python lambda expression for calculating simple interest.
If simple interest is greater than 1000, display as “Platinum Member”, otherwise “Gold Member”.

Use the below formula to calculate the simple interest.
simple_interest=(principal_amount*duration in years*rate_of_interest)/100
'''

#PF-Exer-39
#This verification is based on string match.

principal_amount=4000
duration=12
rate_of_interest=13

simple_interest =lambda x,y,z:(x*y*z)/100

if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
    print("Platinum Member")
else:
    print("Gold Member")
