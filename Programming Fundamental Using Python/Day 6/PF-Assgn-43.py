'''
Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
Handle the possible errors in the code written inside the function.
'''

#PF-Assgn-43

def find_smallest_number(num):
    #start writing your code here
    for i in  range(1,num*10):
        #count=0 
        l=[]
        for j in range(1,i+1):
            if i%j==0:
                l.append(j)
                #count+=1
        if len(l)==num:
            return i

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
