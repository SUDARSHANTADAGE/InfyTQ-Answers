'''
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
'''

#PF-Assgn-46

def nearest_palindrome(number):
    #start writitng your code here
    number=number+1
    for i in range(number,number+1000):
        sum=0
        temp=i
        while(i>0):
            rem=i%10 
            sum=sum*10+rem
            i=i//10
        if sum==temp:
            return temp
            break
number=111
print(nearest_palindrome(number))
