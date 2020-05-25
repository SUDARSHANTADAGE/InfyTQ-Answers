'''
We have ‘N’ flavors of toppings that can be added to a coffee. For example  chocolate, hazelnut, vanilla, Irish and so on.

Write a function that takes the number of available flavors as input and returns the total number of different ways we can have our coffee.
 Note that we can have coffee without any toppings or with different combination of toppings.
 '''
 
 
 #PF-Exer-34

def find_number_of_combination(number_of_flavours):
    total_combination=0
    #write your logic here
    total_combination=2**number_of_flavours
    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(4)
print(number_of_combination)
