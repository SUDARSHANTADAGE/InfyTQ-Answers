'''
Write a python lambda expression for the following:

1. Find the modulo of two numbers and add it to the difference of the same two numbers.
2. Find the square root of a number using math library built-in function.
3. Find the square root of a number without using built-in function.
'''

#PF-Exer-38
#This verification is based on string match.
import math 
num1=36
num2=7
num3=18

calc = lambda x,y:(x%y + x-y)
print(calc(num1,num2))

square_root = lambda x:math.sqrt(x)
print(square_root(num3))

square_root2= lambda x:x**(1/2)
print(square_root2(num3))
