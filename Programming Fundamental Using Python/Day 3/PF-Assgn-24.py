'''
Write a python function to check whether three given numbers can form the sides of a triangle.
Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.
'''

#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    a = num1+num2
    b = num1+num3
    c = num3+num2
    #Write your logic here
    if a>num3 and b>num2 and c>num1:
       return success
    else:
       return failure
    #Use the following messages to return the result wherever necessary
    #return success
    #return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=8
num2=5
num3=15
print(form_triangle(num1, num2, num3))
