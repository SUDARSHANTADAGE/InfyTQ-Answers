'''
Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself.
145 is a Strong number as 1! + 4! + 5! = 145.
'''

#PF-Exer-26
def factorial(number):
     #remove pass and write your logic to find and return the factorial of given number
     if number==0 or number==1:
         fact=1
     else:
        fact=number*factorial(number-1)
     return fact
def find_strong_numbers(num_list):
     #remove pass and write your logic to find and return the list of strong numbers from the given list
     l=[]
     for i in num_list:
         temp=i
         if i==0:
             temp=1
         sum=0
         while(temp):
             rem=temp%10
             sum=sum+factorial(rem)
             temp=temp//10
         if sum==i:
             l.append(i)
         else:
             pass
     return l
num_list=[145,375,100,2,10,40585,0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
