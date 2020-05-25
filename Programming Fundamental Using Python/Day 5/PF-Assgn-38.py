'''
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

1. The number and its double should have exactly the same number of digits.
2. Both the numbers should have the same digits ,but in different order.
Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
'''

#PF-Assgn-38

def check_double(number):
    double=2*number
    s1="".join(str(number))
    s2="".join(str(double))
    s3=sorted(s1)
    s4=sorted(s2)
    if s3==s4:
        return True
    else:
        return False
    
print(check_double(106))
