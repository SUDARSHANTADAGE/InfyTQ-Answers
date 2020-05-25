'''
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

1. Always num1 should be less than num2
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
   a. Sum of the digits of the number is a multiple of 3
   b. Number has only two digits
   c. Number is a multiple of 5
3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.
'''



#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    
    l=[max_num]
    # Write your logic here
    if num1<num2:
       for i in range(num1,num2+1):
           if len(str(i))==2:
                sum=0
                for num in str(i):
                    sum=sum+int(num)
                if sum%3==0:
                    if i%5==0:
                        l.append(i)
    
    return max(l)


#Provide different values for num1 and num2 and test your program.
max_num=find_max(3,30)
print(max_num)
